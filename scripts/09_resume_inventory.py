"""Reconcile local source files and notes; emit a resumable backlog, without changing tiers."""
import csv
import json
from collections import Counter

import frontmatter

from common import BOOKS, DATA, PDF_DIR, TXT_DIR, load_manifest


def main():
    manifest = load_manifest()
    skips = json.loads((DATA / "skips.json").read_text(encoding="utf-8"))
    notes = {p.stem: frontmatter.load(p, encoding="utf-8") for p in BOOKS.glob("*.md")}
    backlog = []
    for row in manifest:
        if row.get("tier") not in ("A", "B") or row["slug"] in notes:
            continue
        slug = row["slug"]
        text_path = TXT_DIR / (slug + ".txt")
        backlog.append({
            "slug": slug, "tier": row["tier"], "filename": row["filename"],
            "pages": row.get("pages", 0), "text_status": row.get("text_status", "unknown"),
            "pdf_present": (PDF_DIR / (slug + ".pdf")).exists(),
            "text_present": text_path.exists() and text_path.stat().st_size > 0,
            "status": "reconcile_skip:" + skips[slug]["status"] if slug in skips else "needs_source_review",
        })
    backlog.sort(key=lambda r: (r["tier"], r["slug"]))
    summary = {
        "scope": "Local manifest; live listing not reverified",
        "manifest_files": len(manifest),
        "manifest_pdfs": sum(r.get("ext") == "pdf" for r in manifest),
        "tiers": dict(Counter(r.get("tier", "unassigned") for r in manifest)),
        "book_notes": sum(p.get("doc_type") != "system" for p in notes.values()),
        "system_notes": sum(p.get("doc_type") == "system" for p in notes.values()),
        "missing_notes": len(backlog),
        "missing_by_tier": dict(Counter(r["tier"] for r in backlog)),
        "provisional_skips": sum(r["slug"] in skips for r in backlog),
        "remaining_candidates": sum(r["slug"] not in skips for r in backlog),
        "source_review": dict(Counter(p.get("source_review", "unrecorded") for p in notes.values() if p.get("doc_type") != "system")),
        "excluded_pdfs": dict(Counter(r.get("c_status", "excluded") for r in manifest if r.get("ext") == "pdf" and r.get("tier") == "C")),
        "unresolved_scans": [r["slug"] for r in manifest if r.get("tier") == "C" and r.get("c_status") == "no_text"],
        "backlog": backlog,
    }
    (DATA / "resume_inventory.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    with (DATA / "resume_backlog.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["slug", "tier", "filename", "pages", "text_status", "pdf_present", "text_present", "status"])
        writer.writeheader()
        writer.writerows(backlog)
    print(json.dumps({k: v for k, v in summary.items() if k != "backlog"}, indent=2))


if __name__ == "__main__":
    main()
