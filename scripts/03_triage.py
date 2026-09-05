"""Phase 2a: dedupe, flag unreadable, prefilter off-topic, propose tiers.

Writes proposals into the manifest (fields: dup_of, proposed_tier, tier_reason) and
prints the ambiguous list for agent review. Final tiers are written to data/tiers.json
by the reviewing agent and merged with `--apply data/tiers.json`.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict

from common import DATA, TXT_DIR, load_manifest, normalized_title, save_manifest

OFF_TOPIC = re.compile(
    r"grisham|broker\.pdf|course in miracles|carnegie|credit repair|quality management|"
    r"small business|100ways|tom peters|moral-reasoning|lifestyle\.pdf|statistically speaking|"
    r"world bank|european integration|calming_the_mind|withdrawal|raveshmokhatereh|"
    r"training intelligent agents|manifesto|rich dad|choose to be rich|masters of enterprise|"
    r"advanced international trade|money secrets|handbook for small",
    re.I,
)

# Authors / titles that anchor Tier A regardless of page count
MAJOR = re.compile(
    r"elder|schwager|larry williams|williams larry|bernstein|murphy|nison|bollinger|wilder|pring|"
    r"tharp|douglas|curtis faith|covel|turtletrader|hull|graham|damodaran|taleb|joe ross|demark|"
    r"fontanills|mcmillan|guy cohen|kaufman|miner|farley|connors|street smarts|steenbarger|"
    r"prechter|neely|gann|wyckoff|livermore|reminiscences|lefevre|mark fisher|logical trader|"
    r"weissman|pruitt|balsara|ryan jones|madhavan|jesse|market wizards|wilmott|cooper|velez|"
    r"bill williams|chande|bressert|raschke|lien|day trading the currency|encyclopedia of trading|"
    r"trading in the zone|disciplined_trader|way of the turtle|complete turtletrader|trend following|"
    r"dorsey|dreman|fisher, robert|robert fisher|fibonacci applications|hagstrom|buffett|"
    r"intelligent investor|swing trading|momentum|options course|option trader handbook|"
    r"mathematics of financial|quantitative finance|monte.carlo|value at risk|money management",
    re.I,
)

TIER_A_MIN_PAGES = 120
TIER_B_MAX_PAGES = 119


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", help="tiers.json produced by the reviewing agent")
    a = ap.parse_args()
    rows = load_manifest()
    pdfs = [r for r in rows if r.get("ext") == "pdf"]

    if a.apply:
        final = json.loads(open(a.apply, encoding="utf-8").read())
        by_slug = {r["slug"]: r for r in rows}
        n = 0
        for slug, info in final.items():
            r = by_slug.get(slug)
            if not r:
                print("unknown slug", slug)
                continue
            r["tier"] = info["tier"]
            r["tier_reason"] = info.get("reason", "")
            if info.get("category"):
                r["category"] = info["category"]
            if info["tier"] == "C":
                r["c_status"] = info.get("status", r.get("c_status", "excluded"))
            n += 1
        save_manifest(rows)
        from collections import Counter
        print("applied", n, Counter(r.get("tier") for r in pdfs))
        return 0

    # 1) exact duplicates by sha1
    by_sha = defaultdict(list)
    for r in pdfs:
        if r.get("sha1"):
            by_sha[r["sha1"]].append(r)
    # 2) loose duplicates by normalized title (keep the one with most chars)
    by_title = defaultdict(list)
    for r in pdfs:
        by_title[normalized_title(r["filename"])].append(r)

    for r in pdfs:
        r.pop("dup_of", None)
        r.pop("proposed_tier", None)
        r.pop("c_status", None)

    def keep_best(group):
        group = sorted(group, key=lambda x: (x.get("text_status") == "ok", x.get("chars", 0)), reverse=True)
        best = group[0]
        for d in group[1:]:
            d["dup_of"] = best["slug"]
            d["proposed_tier"] = "C"
            d["c_status"] = "duplicate"
        return best

    for g in by_sha.values():
        if len(g) > 1:
            keep_best(g)
    for g in by_title.values():
        g = [x for x in g if not x.get("dup_of")]
        if len(g) > 1:
            keep_best(g)

    ambiguous = []
    for r in pdfs:
        if r.get("dup_of"):
            continue
        if r.get("text_status") in ("no_text", "corrupt", "missing_pdf"):
            r["proposed_tier"] = "C"
            r["c_status"] = "no_text" if r.get("text_status") == "no_text" else "corrupt"
            continue
        if OFF_TOPIC.search(r["filename"]):
            r["proposed_tier"] = "C"
            r["c_status"] = "off_topic"
            continue
        pages = r.get("pages", 0)
        if MAJOR.search(r["filename"]) and pages >= 60:
            r["proposed_tier"] = "A"
        elif pages >= TIER_A_MIN_PAGES:
            r["proposed_tier"] = "A?"
            ambiguous.append(r)
        else:
            r["proposed_tier"] = "B"
        if not MAJOR.search(r["filename"]) and pages < 60:
            pass  # plain B
    save_manifest(rows)

    from collections import Counter
    c = Counter(r.get("proposed_tier") for r in pdfs)
    print("proposed:", dict(c))
    print("c_status:", dict(Counter(r.get("c_status") for r in pdfs if r.get("proposed_tier") == "C")))

    # review sheet for the agent: every non-duplicate readable file, with first ~60 words
    sheet = []
    for r in pdfs:
        if r.get("dup_of"):
            continue
        snippet = ""
        t = TXT_DIR / f"{r['slug']}.txt"
        if t.exists():
            txt = t.read_text(encoding="utf-8", errors="replace")
            snippet = " ".join(re.sub(r"\s+", " ", txt[:6000]).split()[:60])
        sheet.append({
            "slug": r["slug"], "filename": r["filename"], "pages": r.get("pages", 0),
            "chars_per_page": r.get("chars_per_page", 0), "pdf_title": r.get("pdf_title", ""),
            "pdf_author": r.get("pdf_author", ""), "proposed_tier": r.get("proposed_tier"),
            "c_status": r.get("c_status", ""), "snippet": snippet,
        })
    (DATA / "review_sheet.json").write_text(json.dumps(sheet, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"review sheet: {len(sheet)} rows -> data/review_sheet.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
