"""Phase 1a: build the manifest from the directory listing and download every PDF.

Usage:  python scripts/01_fetch.py [--workers 8] [--dry-run]
Resumable: files whose on-disk size equals Content-Length are skipped.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import hashlib
import html
import re
import sys
import time
import urllib.parse
import urllib.request

from common import BASE_URL, PDF_DIR, load_manifest, save_manifest, slugify

UA = {"User-Agent": "Mozilla/5.0 (trading-playbook fetch)"}


def listing() -> list[dict]:
    raw = urllib.request.urlopen(urllib.request.Request(BASE_URL, headers=UA), timeout=60).read().decode("utf-8", "replace")
    hrefs = re.findall(r'<A HREF="([^"]+)">', raw, flags=re.I)
    rows, seen = [], set()
    for h in hrefs:
        if h.endswith("/books/"):
            continue
        fname = urllib.parse.unquote(html.unescape(h.rsplit("/", 1)[-1]))
        if fname in seen:
            continue
        seen.add(fname)
        ext = fname.rsplit(".", 1)[-1].lower() if "." in fname else ""
        rows.append({
            "filename": fname,
            "url": BASE_URL.rstrip("/").rsplit("/files", 1)[0] + h if BASE_URL else "",
            "ext": ext,
            "slug": slugify(fname),
            "status": "pending" if ext == "pdf" else "not_pdf",
        })
    # make slugs unique
    counts: dict[str, int] = {}
    for r in rows:
        s = r["slug"]
        counts[s] = counts.get(s, 0) + 1
        if counts[s] > 1:
            r["slug"] = f"{s}-{counts[s]}"
    return rows


def fetch_one(row: dict, dry: bool) -> dict:
    dest = PDF_DIR / f"{row['slug']}.pdf"
    for attempt in range(4):
        try:
            head = urllib.request.urlopen(urllib.request.Request(row["url"], method="HEAD", headers=UA), timeout=60)
            size = int(head.headers.get("Content-Length") or 0)
            row["bytes"] = size
            if dest.exists() and dest.stat().st_size == size and size > 0:
                row["status"] = "downloaded"
                break
            if dry:
                row["status"] = "dry"
                break
            with urllib.request.urlopen(urllib.request.Request(row["url"], headers=UA), timeout=300) as r, open(dest, "wb") as f:
                while True:
                    chunk = r.read(1 << 20)
                    if not chunk:
                        break
                    f.write(chunk)
            if size and dest.stat().st_size != size:
                raise IOError(f"short read {dest.stat().st_size}/{size}")
            row["status"] = "downloaded"
            break
        except Exception as e:  # noqa: BLE001
            row["status"] = "error"
            row["error"] = str(e)[:200]
            time.sleep(2 * (attempt + 1))
    if row["status"] == "downloaded":
        h = hashlib.sha1()
        with open(dest, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
        row["sha1"] = h.hexdigest()
        row.pop("error", None)
    return row


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    PDF_DIR.mkdir(parents=True, exist_ok=True)
    existing = {r["filename"]: r for r in load_manifest()}
    rows = listing()
    for r in rows:  # carry over previous results
        old = existing.get(r["filename"])
        if old:
            r.update({k: v for k, v in old.items() if k not in ("url", "ext")})
    pdfs = [r for r in rows if r["ext"] == "pdf"]
    print(f"listing: {len(rows)} files, {len(pdfs)} pdfs", flush=True)

    done = 0
    with cf.ThreadPoolExecutor(args.workers) as ex:
        for row in ex.map(lambda r: fetch_one(r, args.dry_run), pdfs):
            done += 1
            if done % 25 == 0 or row["status"] == "error":
                print(f"[{done}/{len(pdfs)}] {row['status']:10} {row['filename'][:70]}", flush=True)
    save_manifest(rows)
    ok = sum(r["status"] == "downloaded" for r in pdfs)
    err = [r for r in pdfs if r["status"] == "error"]
    print(f"downloaded {ok}/{len(pdfs)}; errors {len(err)}; total {sum(r.get('bytes',0) for r in pdfs)/1e9:.2f} GB")
    for r in err:
        print("  ERROR", r["filename"], r.get("error"))
    return 0 if not err else 1


if __name__ == "__main__":
    sys.exit(main())
