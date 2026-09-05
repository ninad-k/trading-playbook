"""Sampled OCR for scanned PDFs (no text layer). CPU-only RapidOCR is slow (~10 s/page),
so we OCR a sample: the first N pages (front matter + TOC) plus M evenly spaced pages.
Un-sampled pages are written as empty strings so page numbering stays intact.

Usage: python scripts/02b_ocr_sample.py data/ocr_targets.json [--workers 2]
ocr_targets.json: {"<slug>": {"front": 8, "spread": 28}, ...}
Writes downloads/txt/<slug>.txt and data/ocr_status.json (merge into manifest with 03_triage --apply).
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import re
import sys
import time

import fitz  # PyMuPDF

from common import DATA, PDF_DIR, TXT_DIR

STATUS = DATA / "ocr_status.json"


def ocr_book(slug: str, front: int, spread: int) -> dict:
    from rapidocr_onnxruntime import RapidOCR
    ocr = RapidOCR()
    pdf = PDF_DIR / f"{slug}.pdf"
    doc = fitz.open(pdf)
    n = doc.page_count
    idx = sorted(set(list(range(min(front, n))) + [min(n - 1, front + int(k * (n - front) / spread)) for k in range(spread)]))
    pages = [""] * n
    t0 = time.time()
    chars = 0
    for i in idx:
        try:
            pix = doc[i].get_pixmap(dpi=140)
            res, _ = ocr(pix.tobytes("png"))
            lines = [r[1] for r in (res or [])]
            pages[i] = "\n".join(lines)
            chars += len(pages[i])
        except Exception as e:  # noqa: BLE001
            pages[i] = f"[ocr error: {e}]"
    doc.close()
    (TXT_DIR / f"{slug}.txt").write_text("\f".join(pages), encoding="utf-8")
    return {"slug": slug, "pages": n, "ocr_pages": idx, "chars": chars, "seconds": round(time.time() - t0), "text_status": "ocr_sampled" if chars > 2000 else "no_text"}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("targets")
    ap.add_argument("--workers", type=int, default=2)
    a = ap.parse_args()
    targets = json.loads(open(a.targets, encoding="utf-8").read())
    status = json.loads(STATUS.read_text(encoding="utf-8")) if STATUS.exists() else {}
    todo = [(s, v.get("front", 8), v.get("spread", 28)) for s, v in targets.items() if s not in status]
    print(f"{len(todo)} books to OCR", flush=True)
    with cf.ProcessPoolExecutor(a.workers) as ex:
        futs = {ex.submit(ocr_book, s, f, sp): s for s, f, sp in todo}
        for fut in cf.as_completed(futs):
            r = fut.result()
            status[r["slug"]] = r
            STATUS.write_text(json.dumps(status, indent=1), encoding="utf-8")
            print(f"done {r['slug']} pages={r['pages']} ocr={len(r['ocr_pages'])} chars={r['chars']} {r['seconds']}s -> {r['text_status']}", flush=True)


if __name__ == "__main__":
    main()
