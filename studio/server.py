"""Book Studio: a local-only page for adding books to the library with Ollama.

Usage:  python studio/server.py [--port 8799]
Then open http://127.0.0.1:8799

It binds to the loopback interface only and is never part of the published site. It talks to
nothing but http://localhost:11434 and this repository's own files, so the whole thing works
with the network cable out — provided the Ollama model you pick is a local one.

Long operations stream progress as server-sent events; everything else is plain JSON.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import threading
import traceback
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import pipeline as pl  # noqa: E402

PY = str(ROOT / ".venv" / "Scripts" / "python.exe")
if not Path(PY).exists():
    PY = sys.executable

_lock = threading.Lock()          # one heavy job at a time; a 4B model is not re-entrant-friendly
_books: dict[str, pl.Book] = {}   # filename -> parsed book, kept between analyse and draft


class Handler(BaseHTTPRequestHandler):
    server_version = "BookStudio"

    def log_message(self, fmt, *args):
        sys.stderr.write("  %s\n" % (fmt % args))

    # ---------------------------------------------------------------- helpers
    def _guard(self) -> bool:
        """Loopback only, and no cross-origin host header."""
        host = (self.headers.get("Host") or "").split(":")[0]
        if host not in ("127.0.0.1", "localhost", "[::1]"):
            self.send_error(403, "Book Studio only serves localhost")
            return False
        return True

    def _json(self, obj, code=200):
        body = json.dumps(obj).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _sse_open(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.send_header("X-Accel-Buffering", "no")
        self.end_headers()

    def _sse(self, kind: str, **data):
        try:
            self.wfile.write(f"data: {json.dumps({'k': kind, **data})}\n\n".encode())
            self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError):
            raise

    def _body(self) -> bytes:
        n = int(self.headers.get("Content-Length") or 0)
        return self.rfile.read(n) if n else b""

    def _payload(self) -> dict:
        raw = self._body()
        return json.loads(raw.decode()) if raw else {}

    # ---------------------------------------------------------------- GET
    def do_GET(self):
        if not self._guard():
            return
        path = self.path.split("?")[0]
        if path in ("/", "/index.html"):
            html = (HERE / "app.html").read_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(html)))
            self.end_headers()
            self.wfile.write(html)
        elif path == "/api/status":
            self._json(self._status())
        elif path == "/api/drafts":
            self._json({"drafts": self._drafts()})
        else:
            self.send_error(404)

    def _status(self) -> dict:
        st = pl.ollama_status()
        idx = pl.load_index()
        notes = len(list(pl.BOOKS.glob("*.md")))
        return {
            "ollama": st,
            "index": {"built": bool(idx), "notes": len(idx), "stale": len(idx) != notes,
                      "texts": len(pl.dedup.load_index())},
            "library": {"notes": notes, "manifest": len(pl.load_manifest())},
            "staged": sorted(_books),
            "drafts": self._drafts(),
            "embed_model": pl.EMBED_MODEL,
        }

    def _drafts(self) -> list:
        if not pl.DRAFTS.exists():
            return []
        import frontmatter
        out = []
        for f in sorted(pl.DRAFTS.glob("*.md")):
            m = frontmatter.load(f, encoding="utf-8").metadata
            out.append({"slug": f.stem, "title": m.get("title", f.stem),
                        "author": m.get("author", ""), "category": m.get("category", ""),
                        "coverage": m.get("reviewed_pdf_pages", ""),
                        "drafted_by": m.get("drafted_by", ""),
                        "warnings": m.get("draft_warnings") or []})
        return out

    # ---------------------------------------------------------------- POST
    def do_POST(self):
        if not self._guard():
            return
        path = self.path.split("?")[0]
        try:
            if path == "/api/upload":
                self._upload()
            elif path == "/api/clear":
                _books.clear()
                self._json({"ok": True})
            elif path == "/api/index":
                self._stream(self._job_index)
            elif path == "/api/analyze":
                self._stream(self._job_analyze)
            elif path == "/api/draft":
                self._stream(self._job_draft)
            elif path == "/api/approve":
                self._json(self._approve(self._payload()))
            elif path == "/api/rebuild":
                self._stream(self._job_rebuild)
            else:
                self.send_error(404)
        except Exception as e:  # noqa: BLE001
            traceback.print_exc()
            try:
                self._json({"error": str(e)}, 500)
            except Exception:  # noqa: BLE001
                pass

    def _upload(self):
        name = self.headers.get("X-Filename") or "upload.pdf"
        name = Path(name).name
        if not name.lower().endswith(".pdf"):
            self._json({"error": "only PDF files are accepted"}, 400)
            return
        pl.UPLOADS.mkdir(parents=True, exist_ok=True)
        dest = pl.UPLOADS / name
        dest.write_bytes(self._body())
        book = pl.read_pdf(dest)
        _books[name] = book
        self._json({"filename": name, "pages": len(book.pages), "chars": book.chars,
                    "text": book.chars > 2000})

    def _stream(self, job):
        payload = self._payload()
        self._sse_open()
        if not _lock.acquire(blocking=False):
            self._sse("error", message="Another job is already running. Wait for it to finish.")
            self._sse("done")
            return
        try:
            job(payload)
        except Exception as e:  # noqa: BLE001
            traceback.print_exc()
            self._sse("error", message=f"{type(e).__name__}: {e}")
        finally:
            _lock.release()
            try:
                self._sse("done")
            except Exception:  # noqa: BLE001
                pass

    # ---------------------------------------------------------------- jobs
    def _job_index(self, _payload):
        self._sse("log", message="Fingerprinting every extracted source text. This is what actually "
                                 "detects a duplicate book.")

        def tprog(done, of):
            self._sse("progress", done=done, total=of)

        tres = pl.dedup.build_index(tprog)
        pl.dedup.invalidate()
        self._sse("log", message=f"  {tres['texts']} of {tres['of']} texts fingerprinted "
                                 f"({tres['mb']} MB). The rest are image-only scans.")

        self._sse("log", message=f"Embedding every note with {pl.EMBED_MODEL} for topic lookup.")

        def eprog(done, of):
            self._sse("progress", done=done, total=of)

        res = pl.build_index(eprog)
        self._sse("log", message=f"  {res['notes']} notes embedded.")
        self._sse("result", index={"notes": res["notes"], "texts": tres["texts"]})

    def _job_analyze(self, payload):
        names = payload.get("files") or sorted(_books)
        results = []
        for i, name in enumerate(names, 1):
            book = _books.get(name)
            if not book:
                continue
            self._sse("log", message=f"[{i}/{len(names)}] {name} — {len(book.pages)} pages")
            res = pl.analyse(book)
            for r in res["reasons"]:
                self._sse("log", message=f"    {r}")
            if res["matches"]:
                top = res["matches"][0]
                self._sse("log", message=f"    Nearest by subject: {top['title']}")
            if res["novel_sections"]:
                pages = ", ".join(str(s["page"]) for s in res["novel_sections"])
                self._sse("log", message=f"    Least familiar sampled pages: {pages}")
            results.append(res)
            self._sse("progress", done=i, total=len(names))
        self._sse("result", analysis=results)

    def _job_draft(self, payload):
        model = payload.get("model")
        names = payload.get("files") or []
        analyses = {a["filename"]: a for a in payload.get("analysis") or []}
        if not model:
            raise ValueError("pick a model first")
        drafted = []
        for i, name in enumerate(names, 1):
            book = _books.get(name)
            if not book:
                continue
            self._sse("log", message=f"[{i}/{len(names)}] {name} — drafting with {model}")

            def prog(step, detail, _n=name):
                self._sse("log", message=f"    {step}: {detail}")

            res = pl.draft_note(book, model, analyses.get(name, {}), prog)
            self._sse("log", message=f"    wrote {res['path']}")
            res["sha1"], res["filename"] = book.sha1, book.filename
            res["book_pages"], res["book_chars"] = len(book.pages), book.chars
            drafted.append(res)
            self._sse("progress", done=i, total=len(names))
        self._sse("result", drafts=drafted)

    def _approve(self, payload) -> dict:
        return pl.approve(payload["slug"], payload.get("sha1", ""), payload.get("filename", ""),
                          int(payload.get("pages") or 0), int(payload.get("chars") or 0))

    def _job_rebuild(self, _payload):
        for label, script in [("validate", "05_validate.py"), ("build", "06_build_site.py"),
                              ("check", "12_check_site.py")]:
            self._sse("log", message=f"$ python scripts/{script}")
            p = subprocess.run([PY, str(ROOT / "scripts" / script)], cwd=ROOT,
                               capture_output=True, text=True, encoding="utf-8", errors="replace")
            for line in (p.stdout or "").strip().splitlines()[-14:]:
                self._sse("log", message="    " + line)
            if p.returncode != 0:
                for line in (p.stderr or "").strip().splitlines()[-6:]:
                    self._sse("log", message="    ! " + line)
                self._sse("error", message=f"{label} failed. The site was not updated.")
                return
        self._sse("log", message="Site rebuilt. docs/ is current.")
        self._sse("result", rebuilt=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port", type=int, default=8799)
    a = ap.parse_args()
    srv = ThreadingHTTPServer(("127.0.0.1", a.port), Handler)
    print(f"Book Studio  ->  http://127.0.0.1:{a.port}")
    print("Local only. Ctrl-C to stop.")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")


if __name__ == "__main__":
    main()
