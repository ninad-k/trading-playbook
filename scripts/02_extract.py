"""Phase 1b: pdfinfo + pdftotext for every downloaded PDF -> downloads/txt/<slug>.txt

Records pages, chars, chars_per_page, and text_status (ok | no_text | corrupt) in the manifest.
Usage: python scripts/02_extract.py [--workers 6] [--force]
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import re
import subprocess
import sys

from common import PDF_DIR, TXT_DIR, load_manifest, save_manifest

NO_TEXT_THRESHOLD = 150  # chars per page below this = scanned image PDF


def run(cmd: list[str], timeout: int = 600) -> tuple[int, str, str]:
    p = subprocess.run(cmd, capture_output=True, timeout=timeout)
    return p.returncode, p.stdout.decode("utf-8", "replace"), p.stderr.decode("utf-8", "replace")


def extract(row: dict, force: bool) -> dict:
    pdf = PDF_DIR / f"{row['slug']}.pdf"
    txt = TXT_DIR / f"{row['slug']}.txt"
    if not pdf.exists():
        row["text_status"] = "missing_pdf"
        return row
    if txt.exists() and not force and row.get("text_status") == "ok":
        return row
    try:
        rc, out, _ = run(["pdfinfo", str(pdf)], timeout=120)
        m = re.search(r"Pages:\s+(\d+)", out)
        row["pages"] = int(m.group(1)) if m else 0
        t = re.search(r"Title:\s+(.+)", out)
        row["pdf_title"] = t.group(1).strip()[:200] if t else ""
        a = re.search(r"Author:\s+(.+)", out)
        row["pdf_author"] = a.group(1).strip()[:120] if a else ""
        rc, _, err = run(["pdftotext", "-layout", "-enc", "UTF-8", str(pdf), str(txt)])
        if rc != 0 and not txt.exists():
            row["text_status"] = "corrupt"
            row["error"] = err.strip()[:200]
            return row
        text = txt.read_text(encoding="utf-8", errors="replace")
        # collapse whitespace-only pages for the density measure
        dense = re.sub(r"\s+", " ", text)
        row["chars"] = len(dense)
        row["chars_per_page"] = round(len(dense) / max(row["pages"], 1))
        row["text_status"] = "ok" if row["chars_per_page"] >= NO_TEXT_THRESHOLD else "no_text"
        row.pop("error", None)
    except subprocess.TimeoutExpired:
        row["text_status"] = "corrupt"
        row["error"] = "timeout"
    except Exception as e:  # noqa: BLE001
        row["text_status"] = "corrupt"
        row["error"] = str(e)[:200]
    return row


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()
    TXT_DIR.mkdir(parents=True, exist_ok=True)
    rows = load_manifest()
    pdfs = [r for r in rows if r.get("status") == "downloaded"]
    done = 0
    with cf.ThreadPoolExecutor(args.workers) as ex:
        for row in ex.map(lambda r: extract(r, args.force), pdfs):
            done += 1
            if done % 50 == 0:
                print(f"[{done}/{len(pdfs)}]", flush=True)
    save_manifest(rows)
    from collections import Counter
    c = Counter(r.get("text_status") for r in pdfs)
    print("text_status:", dict(c))
    print("total pages:", sum(r.get("pages", 0) for r in pdfs))
    for r in pdfs:
        if r.get("text_status") in ("corrupt", "missing_pdf"):
            print("  ", r["text_status"], r["filename"], r.get("error", ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
