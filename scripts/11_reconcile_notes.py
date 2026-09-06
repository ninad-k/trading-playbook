"""Apply explicit note-review outcomes and reconcile exclusions without inventing summaries."""
import argparse
import json
import re
from pathlib import Path

import frontmatter

from common import BOOKS, DATA, ROOT, load_manifest, save_manifest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    rows = load_manifest()
    tiers = json.loads((DATA / "tiers.json").read_text(encoding="utf-8"))
    skips = json.loads((DATA / "skips.json").read_text(encoding="utf-8"))
    outcomes = {}
    # Later recovery reviews supersede earlier unreadable decisions.
    for name in ("short_a", "short_b", "long", "root", "legacy"):
        path = DATA / "resume_assignments" / (name + "_report.json")
        if path.exists():
            for item in json.loads(path.read_text(encoding="utf-8")):
                outcomes[item["slug"]] = item
    recovery_path = DATA / "resume_assignments" / "recovery_report.json"
    recovery = {r["slug"]: r for r in json.loads(recovery_path.read_text(encoding="utf-8"))} if recovery_path.exists() else {}
    decisions = {}
    for slug, old in skips.items():
        decisions[slug] = {"status": old["status"], "reason": old.get("note", "Previously reviewed duplicate"), "dup_of": old.get("dup_of")}
    for slug, item in outcomes.items():
        outcome = item["outcome"]
        if outcome == "written":
            decisions.pop(slug, None)
        elif outcome in ("duplicate", "off_topic", "corrupt", "unreadable"):
            decisions[slug] = {"status": "no_text" if outcome == "unreadable" else outcome,
                               "reason": item.get("limitations", ""), "dup_of": item.get("duplicate_of")}
        else:
            raise ValueError(f"Unrecognized review outcome: {slug}: {outcome}")
    aliases = {s: d["dup_of"] for s, d in decisions.items() if d["status"] == "duplicate" and d.get("dup_of")}
    def canonical(slug):
        seen = set()
        while slug in aliases:
            if slug in seen:
                raise ValueError("Duplicate cycle: " + slug)
            seen.add(slug)
            slug = aliases[slug]
        return slug
    for slug in aliases:
        target = canonical(slug)
        if not (BOOKS / (target + ".md")).exists():
            raise ValueError(f"Duplicate target has no note: {slug} -> {target}")
        decisions[slug]["dup_of"] = target
    archive = DATA / "retired_notes"
    for slug, decision in decisions.items():
        path = BOOKS / (slug + ".md")
        if path.exists():
            if decision["status"] != "duplicate" or slug not in outcomes:
                raise ValueError(f"Exclusion conflicts with existing note: {slug}")
            if args.apply:
                archive.mkdir(exist_ok=True)
                destination = archive / path.name
                if archive.resolve() != ROOT.resolve() / "data" / "retired_notes":
                    raise ValueError("Archive path escapes repository")
                if destination.exists():
                    raise ValueError("Refusing to overwrite archived note")
                path.rename(destination)
    changes = []
    for row in rows:
        slug = row["slug"]
        if slug in recovery:
            r = recovery[slug]
            if r["status"] in ("ocr_full", "ocr_sampled"):
                row.update(text_status=r["status"], pages=r["pages"], chars=r["chars"],
                           chars_per_page=round(r["chars"] / max(r["pages"], 1)),
                           recovered_ocr_pages=r["ocr_pages"])
        path = BOOKS / (slug + ".md")
        if slug in decisions:
            d = decisions[slug]
            before = row.get("tier")
            row.update(tier="C", c_status=d["status"], tier_reason=d["reason"])
            if d["status"] == "corrupt":
                row["text_status"] = "corrupt"
            if d.get("dup_of"):
                row["dup_of"] = d["dup_of"]
            else:
                row.pop("dup_of", None)
            tiers[slug] = {"tier": "C", "status": d["status"], "reason": d["reason"]}
            skips[slug] = {"status": d["status"], "note": d["reason"]}
            if d.get("dup_of"):
                skips[slug]["dup_of"] = d["dup_of"]
            changes.append({"slug": slug, "previous_tier": before, "tier": "C", **d})
        elif path.exists() and slug in outcomes:
            note = frontmatter.load(path, encoding="utf-8")
            row.update(tier=note["tier"], tier_reason="Source-reviewed study note", note_review=note.get("source_review", "unspecified"))
            row.pop("c_status", None)
            row.pop("dup_of", None)
            tiers[slug] = {"tier": note["tier"], "reason": "Source-reviewed study note", "status": ""}
            skips.pop(slug, None)
    remaining = [r["slug"] for r in rows if r.get("tier") in ("A", "B") and not (BOOKS / (r["slug"] + ".md")).exists()]
    print(json.dumps({"review_outcomes": len(outcomes), "exclusions_reconciled": len(decisions), "missing_notes": remaining}, indent=2))
    if not args.apply:
        return
    save_manifest(rows)
    (DATA / "tiers.json").write_text(json.dumps(tiers, indent=1, ensure_ascii=False), encoding="utf-8")
    (DATA / "skips.json").write_text(json.dumps(skips, indent=1, ensure_ascii=False), encoding="utf-8")
    (DATA / "resume_assignments" / "reconciliation.json").write_text(json.dumps(changes, indent=2), encoding="utf-8")
    # Preserve references to canonical copies; remove only unavailable related links.
    unavailable_titles = {
        "new-concepts-in-technical-trading-systems-welles-wilder": "New Concepts in Technical Trading Systems",
        "daytrading-university-trading-course": "Daytrading University Trading Course",
        "money-management-for-gambler": "Money Management for Gambler",
        "gann-w-d-1953-magic-words": "Magic Words",
    }
    changed_links = []
    for path in BOOKS.glob("*.md"):
        post = frontmatter.load(path, encoding="utf-8")
        before = frontmatter.dumps(post)
        related = []
        for slug in post.get("related", []):
            target = canonical(slug)
            if target not in decisions and target not in related:
                related.append(target)
        post["related"] = related
        def link(match):
            slug = match[1]
            target = canonical(slug)
            if target != slug:
                return "[[" + target + "]]"
            if slug in decisions:
                title = unavailable_titles.get(slug)
                if not title:
                    raise ValueError("Need explicit title for unavailable body reference: " + slug)
                return "**" + title + "** (no library summary: " + decisions[slug]["status"].replace("_", " ") + ")"
            return match[0]
        post.content = re.sub(r"\[\[([^\]|]+)\]\]", link, post.content)
        if frontmatter.dumps(post) != before:
            path.write_text(frontmatter.dumps(post), encoding="utf-8")
            changed_links.append(path.stem)
    print("Updated canonical/unavailable references in", len(changed_links), "notes")


if __name__ == "__main__":
    main()
