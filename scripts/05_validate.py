"""Validate content/books/*.md and content/topics/*.md against the schema; reconcile with manifest.

Exit code 1 on any error. Usage: python scripts/05_validate.py [--fix-related]
"""
from __future__ import annotations

import argparse
import re
import sys

import frontmatter

from common import BOOKS, CATEGORIES, TOPICS, load_manifest

REQ_BOOK = ["title", "author", "year", "slug", "tier", "category", "tags", "difficulty", "doc_type", "pages", "one_liner", "related", "source_file"]
SECTIONS_A = ["Overview", "Core thesis", "Key concepts", "Rules and setups", "Risk and money management", "Psychology and discipline", "Chapter map", "Strengths and caveats", "Who should read it", "Related books in this library"]
SECTIONS_B = ["Summary", "Key points", "Actionable rules", "Caveats", "Who it is for"]
SECTIONS_SYS = ["What it is", "Rules", "Risk", "Caveats"]
SECTIONS_TOPIC = ["What it is", "Core principles", "Concrete rules and setups", "Common mistakes", "Best books for this topic", "Open debates"]
DIFF = {"beginner", "intermediate", "advanced"}
DOCT = {"book", "course", "article", "paper", "manual", "system"}
FORBIDDEN = re.compile(r"dl\.fxf1\.com", re.I)


def headings(body: str) -> list[str]:
    return [re.sub(r"\s+", " ", h.strip()) for h in re.findall(r"^##\s+(.+)$", body, flags=re.M)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix-related", action="store_true", help="drop unresolved related slugs")
    a = ap.parse_args()
    errors: list[str] = []
    rows = load_manifest()
    by_slug = {r["slug"]: r for r in rows}
    files = sorted(BOOKS.glob("*.md"))
    slugs = {f.stem for f in files}
    posts = {}
    for f in files:
        try:
            post = frontmatter.load(f, encoding="utf-8")
        except Exception as e:  # noqa: BLE001
            errors.append(f"{f.name}: frontmatter parse error {e}")
            continue
        posts[f.stem] = post
        m = post.metadata
        for k in REQ_BOOK:
            if k not in m:
                errors.append(f"{f.name}: missing {k}")
        if m.get("slug") != f.stem:
            errors.append(f"{f.name}: slug {m.get('slug')!r} != filename")
        if m.get("category") not in CATEGORIES:
            errors.append(f"{f.name}: bad category {m.get('category')!r}")
        if m.get("difficulty") not in DIFF:
            errors.append(f"{f.name}: bad difficulty {m.get('difficulty')!r}")
        if m.get("doc_type") not in DOCT:
            errors.append(f"{f.name}: bad doc_type {m.get('doc_type')!r}")
        if m.get("tier") not in ("A", "B"):
            errors.append(f"{f.name}: bad tier {m.get('tier')!r}")
        if not isinstance(m.get("tags"), list) or not m.get("tags"):
            errors.append(f"{f.name}: tags must be a non-empty list")
        if not isinstance(m.get("related"), list):
            errors.append(f"{f.name}: related must be a list")
        else:
            bad = [s for s in m["related"] if s not in slugs]
            if bad and a.fix_related:
                m["related"] = [s for s in m["related"] if s in slugs]
                f.write_text(frontmatter.dumps(post), encoding="utf-8")
            elif bad:
                errors.append(f"{f.name}: unresolved related {bad}")
        if m.get("doc_type") == "system":
            if m.get("parent") not in slugs:
                errors.append(f"{f.name}: system page parent {m.get('parent')!r} not found")
            req = SECTIONS_SYS
        else:
            if m.get("source_file") and m.get("source_file") not in {r["filename"] for r in rows}:
                errors.append(f"{f.name}: source_file not in manifest")
            req = SECTIONS_A if m.get("tier") == "A" else SECTIONS_B
        hs = headings(post.content)
        for s in req:
            if not any(h.lower().startswith(s.lower()) for h in hs):
                errors.append(f"{f.name}: missing section '## {s}'")
        if FORBIDDEN.search(post.content) or FORBIDDEN.search(str(m)):
            errors.append(f"{f.name}: contains source mirror URL")
        wc = len(post.content.split())
        if m.get("doc_type") != "system":
            lo = 600 if m.get("tier") == "A" else 150
            if wc < lo:
                errors.append(f"{f.name}: too short ({wc} words)")

    # manifest reconciliation
    want = {r["slug"] for r in rows if r.get("tier") in ("A", "B")}
    have = {s for s, p in posts.items() if p.metadata.get("doc_type") != "system"}
    for s in sorted(want - have):
        errors.append(f"manifest tier {by_slug[s]['tier']} without page: {s}")
    for s in sorted(have - want):
        errors.append(f"page without manifest A/B row: {s}")

    for f in sorted(TOPICS.glob("*.md")):
        post = frontmatter.load(f, encoding="utf-8")
        hs = headings(post.content)
        if f.stem != "glossary":
            for s in SECTIONS_TOPIC:
                if not any(h.lower().startswith(s.lower()) for h in hs):
                    errors.append(f"topics/{f.name}: missing section '## {s}'")
        for m in re.findall(r"\[\[([^\]]+)\]\]", post.content):
            if m not in slugs:
                errors.append(f"topics/{f.name}: unresolved link [[{m}]]")
        if FORBIDDEN.search(post.content):
            errors.append(f"topics/{f.name}: contains source mirror URL")

    print(f"pages: {len(posts)} (books {len(have)}, systems {len(posts)-len(have)}); manifest A/B rows: {len(want)}; topics: {len(list(TOPICS.glob('*.md')))}")
    for e in errors:
        print("ERR", e)
    print("OK" if not errors else f"{len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
