"""Recover explicitly selected scans; preserve old text and record exact OCR coverage."""
import concurrent.futures
import json
import os
import sys
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "4")
from common import DATA, PDF_DIR, TXT_DIR


def recover(job):
    import pymupdf
    slug = job["slug"]
    doc = pymupdf.open(PDF_DIR / (slug + ".pdf"))
    n = len(doc)
    if not n:
        return {"slug": slug, "status": "corrupt", "pages": 0}
    front = job.get("front", 8)
    selected = list(range(n)) if n <= 60 else sorted(set(range(min(front, n))) | {front + int(k * (n - front) / 20) for k in range(20)})
    backend = job.get("engine", "rapidocr")
    if backend == "rapidocr":
        from rapidocr_onnxruntime import RapidOCR
        engine = RapidOCR(intra_op_num_threads=4)
    elif backend != "tesseract":
        raise ValueError("Unknown OCR engine: " + backend)
    texts = [""] * n
    failures = []
    for i in selected:
        try:
            page = doc[i]
            if job.get("rotation"):
                page.set_rotation((page.rotation + job["rotation"]) % 360)
            if backend == "tesseract":
                tp = page.get_textpage_ocr(language="eng", dpi=200, full=True,
                                          tessdata=str((PDF_DIR.parent / "tessdata").resolve()))
                texts[i] = page.get_text(textpage=tp)
            else:
                result, _ = engine(page.get_pixmap(dpi=130).tobytes("png"))
                texts[i] = "\n".join(x[1] for x in (result or []))
        except Exception as e:
            failures.append({"page": i + 1, "error": str(e)})
    text = "\f".join(texts)
    old = TXT_DIR / (slug + ".txt")
    backup = TXT_DIR / (slug + ".before-recovery.txt")
    if old.exists() and not backup.exists():
        backup.write_bytes(old.read_bytes())
    old.write_text(text, encoding="utf-8")
    return {"slug": slug, "status": "ocr_full" if len(selected) == n and not failures else "ocr_sampled",
            "pages": n, "ocr_pages": [i + 1 for i in selected], "chars": len(text), "failures": failures,
            "ocr_engine": backend, "render_rotation": job.get("rotation", 0)}


if __name__ == "__main__":
    jobs = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    target = DATA / "resume_assignments" / "recovery_report.json"
    report = json.loads(target.read_text(encoding="utf-8")) if target.exists() else []
    done = {x["slug"] for x in report}
    with concurrent.futures.ProcessPoolExecutor(2) as pool:
        futures = {pool.submit(recover, x): x["slug"] for x in jobs if x["slug"] not in done}
        for future in concurrent.futures.as_completed(futures):
            try:
                row = future.result()
            except Exception as e:
                row = {"slug": futures[future], "status": "error", "error": str(e)}
            report.append(row)
            target.write_text(json.dumps(report, indent=2), encoding="utf-8")
            print(row["slug"], row["status"], row.get("chars", 0), flush=True)
