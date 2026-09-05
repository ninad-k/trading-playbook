"""Phase 2b: combine triage proposals + data/tier_overrides.json + OCR targets -> data/tiers.json, then apply.

Usage: python scripts/03b_apply_overrides.py
"""
from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter

from common import DATA, ROOT, load_manifest, save_manifest


def main() -> int:
    rows = load_manifest()
    ov = json.loads((DATA / "tier_overrides.json").read_text(encoding="utf-8"))
    ocr = set(json.loads((DATA / "ocr_targets.json").read_text(encoding="utf-8")))
    pdfs = [r for r in rows if r.get("ext") == "pdf"]

    def match(r, key):
        return key.lower() in r["filename"].lower() or key.lower() == r["slug"]

    tiers = {}
    for r in pdfs:
        t = r.get("proposed_tier")
        reason = f"triage: {t}"
        if t == "A?":
            t, reason = "B", "long but not a core trading text"
        tiers[r["slug"]] = {"tier": t, "reason": reason, "status": r.get("c_status", "")}
    for r in pdfs:
        s = r["slug"]
        for k in ov["A"]:
            if match(r, k):
                tiers[s].update(tier="A", reason="manual: core trading text", status="")
        for k in ov["B"]:
            if match(r, k):
                tiers[s].update(tier="B", reason="manual: concise is enough", status="")
        for k, dup in ov["C_duplicate"].items():
            if match(r, k):
                tiers[s].update(tier="C", reason="manual: duplicate of " + dup, status="duplicate")
                r["dup_of"] = dup
        for k in ov["C_off_topic"]:
            if match(r, k):
                tiers[s].update(tier="C", reason="manual: not trading related", status="off_topic")
    for r in pdfs:
        s = r["slug"]
        scanned = r.get("text_status") in ("no_text", "corrupt")
        if scanned and s not in ocr and tiers[s]["tier"] != "C":
            tiers[s].update(tier="C", reason="scanned PDF without text layer (no OCR)", status="no_text" if r.get("text_status") == "no_text" else "corrupt")
        if s in ocr and tiers[s]["tier"] == "C" and tiers[s]["status"] in ("no_text", ""):
            tiers[s].update(tier="B", reason="sampled OCR; concise notes", status="")
        if s in ocr:
            tiers[s]["ocr"] = True
        if tiers[s]["tier"] == "C" and not tiers[s]["status"]:
            tiers[s]["status"] = r.get("c_status") or "excluded"
    (DATA / "tiers.json").write_text(json.dumps(tiers, indent=1), encoding="utf-8")
    save_manifest(rows)
    print("tiers:", dict(Counter(v["tier"] for v in tiers.values())))
    print("C by status:", dict(Counter(v["status"] for v in tiers.values() if v["tier"] == "C")))
    print("OCR-backed A/B:", sum(1 for v in tiers.values() if v.get("ocr") and v["tier"] != "C"))
    return subprocess.call([sys.executable, str(ROOT / "scripts" / "03_triage.py"), "--apply", str(DATA / "tiers.json")])


if __name__ == "__main__":
    sys.exit(main())
