"""Phase 3 prep: assign Tier A/B documents to agent batches -> data/batches.json, data/slugs.txt

Usage: python scripts/03c_batches.py [--a-per 3] [--b-per 12]
OCR-backed documents go into their own batches (dispatched last, after OCR completes).
"""
from __future__ import annotations

import argparse
import json

from common import DATA, load_manifest


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--a-per", type=int, default=3)
    ap.add_argument("--b-per", type=int, default=12)
    a = ap.parse_args()
    rows = load_manifest()
    tiers = json.loads((DATA / "tiers.json").read_text(encoding="utf-8"))
    ab = [r for r in rows if r.get("tier") in ("A", "B")]
    for r in ab:
        r["_ocr"] = bool(tiers.get(r["slug"], {}).get("ocr"))
    # slug list for cross-references
    lines = [f"{r['slug']} | {r.get('pdf_title') or r['filename'].rsplit('.',1)[0]}" for r in sorted(ab, key=lambda x: x["slug"])]
    (DATA / "slugs.txt").write_text("\n".join(lines), encoding="utf-8")

    def item(r):
        return {"slug": r["slug"], "filename": r["filename"], "pages": r.get("pages", 0), "tier": r["tier"], "ocr": r["_ocr"]}

    batches = []
    for tier, per in (("A", a.a_per), ("B", a.b_per)):
        normal = sorted([r for r in ab if r["tier"] == tier and not r["_ocr"]], key=lambda x: -x.get("pages", 0))
        # balance by pages: snake order
        groups = [[] for _ in range((len(normal) + per - 1) // per)]
        for i, r in enumerate(normal):
            g = i // len(groups) if False else (i % len(groups) if (i // len(groups)) % 2 == 0 else len(groups) - 1 - i % len(groups))
            groups[g].append(r)
        for g in groups:
            if g:
                batches.append({"tier": tier, "ocr": False, "items": [item(r) for r in g]})
        ocr = [r for r in ab if r["tier"] == tier and r["_ocr"]]
        for g in chunks(ocr, per if tier == "B" else 3):
            batches.append({"tier": tier, "ocr": True, "items": [item(r) for r in g]})
    for i, b in enumerate(batches, 1):
        b["id"] = f"{b['tier']}{i:02d}"
        b["pages"] = sum(x["pages"] for x in b["items"])
    (DATA / "batches.json").write_text(json.dumps(batches, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{len(batches)} batches; A: {sum(1 for b in batches if b['tier']=='A')}, B: {sum(1 for b in batches if b['tier']=='B')}; docs: {len(ab)}")
    for b in batches:
        print(f"  {b['id']:5} tier={b['tier']} ocr={int(b['ocr'])} n={len(b['items']):2} pages={b['pages']:5}  {', '.join(x['slug'][:28] for x in b['items'][:4])}{' …' if len(b['items'])>4 else ''}")


if __name__ == "__main__":
    main()
