"""Validate content/books/*.md and content/topics/*.md against the schema; reconcile with manifest.

Exit code 1 on any error. Usage: python scripts/05_validate.py [--fix-related]
"""
from __future__ import annotations

import argparse
import re
import sys

import frontmatter

from common import BOOKS, CATEGORIES, CONTENT, TOPICS, load_manifest

REQ_BOOK = ["title", "author", "year", "slug", "tier", "category", "tags", "difficulty", "doc_type", "pages", "one_liner", "related", "source_file"]
SECTIONS_A = ["Overview", "Core thesis", "Key concepts", "Rules and setups", "Risk and money management", "Psychology and discipline", "Chapter map", "Strengths and caveats", "Who should read it", "Related books in this library"]
SECTIONS_B = ["Summary", "Key points", "Actionable rules", "Caveats", "Who it is for"]
SECTIONS_SYS = ["What it is", "Rules", "Risk", "Caveats"]
REQ_LESSON = ["stage", "title", "slug", "goal"]
SECTIONS_LESSON = ["What you will be able to do", "The lesson", "Worked example", "Practice", "Self-check"]
SECTIONS_TOPIC = ["What it is", "Core principles", "Concrete rules and setups", "Common mistakes", "Best books for this topic", "Open debates"]
DIFF = {"beginner", "intermediate", "advanced"}
DOCT = {"book", "course", "article", "paper", "manual", "system"}
# no note may carry a link to a downloadable source file, from any host
FORBIDDEN = re.compile(r"https?://\S+\.(?:pdf|epub|djvu|chm|zip|rar)", re.I)


def headings(body: str) -> list[str]:
    return [re.sub(r"\s+", " ", h.strip()) for h in re.findall(r"^##\s+(.+)$", body, flags=re.M)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fix-related", action="store_true", help="drop unresolved related slugs")
    ap.add_argument("--only", help="comma-separated slugs: validate just these files, skip manifest reconciliation")
    a = ap.parse_args()
    only = set(a.only.split(",")) if a.only else None
    errors: list[str] = []
    rows = load_manifest()
    by_slug = {r["slug"]: r for r in rows}
    files = sorted(BOOKS.glob("*.md"))
    # cross-references may point at any Tier A/B document (written or not yet) plus any existing page
    slugs = {f.stem for f in files} | {r["slug"] for r in rows if r.get("tier") in ("A", "B")}
    if only:
        files = [f for f in files if f.stem in only or any(f.stem.startswith(o + "--") for o in only)]
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
            errors.append(f"{f.name}: links to a downloadable source file")
        wc = len(post.content.split())
        if m.get("doc_type") != "system":
            lo = 600 if m.get("tier") == "A" else 150
            if wc < lo:
                errors.append(f"{f.name}: too short ({wc} words)")

    # manifest reconciliation
    if only:
        print(f"validated {len(files)} files")
        for e in errors:
            print("ERR", e)
        print("OK" if not errors else f"{len(errors)} errors")
        return 1 if errors else 0
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
            errors.append(f"topics/{f.name}: links to a downloadable source file")

    # ---- Manual Trader course: a sequence, so it is checked as one
    manual = CONTENT / "manual"
    if manual.exists():
        diagram_names = {f.stem for f in (CONTENT / "diagrams").glob("*.svg")}
        stages = {}
        for f in sorted(manual.glob("*.md")):
            if f.stem == "index":
                continue
            post = frontmatter.load(f, encoding="utf-8")
            m = post.metadata
            for k in REQ_LESSON:
                if k not in m:
                    errors.append(f"manual/{f.name}: missing {k}")
            if m.get("slug") != f.stem:
                errors.append(f"manual/{f.name}: slug {m.get('slug')!r} != filename")
            hs = headings(post.content)
            for s in SECTIONS_LESSON:
                if not any(h.lower().startswith(s.lower()) for h in hs):
                    errors.append(f"manual/{f.name}: missing section '## {s}'")
            # the course teaches in one flow: sending the reader to the library mid-lesson breaks it
            for link in re.findall(r"\[\[([^\]]+)\]\]", post.content):
                if not link.startswith("diagram:"):
                    errors.append(f"manual/{f.name}: lesson links out to [[{link}]]; the course must stand alone")
            d = m.get("diagram")
            if d and d not in diagram_names:
                errors.append(f"manual/{f.name}: unknown diagram {d!r}")
            if d and not m.get("diagram_caption"):
                errors.append(f"manual/{f.name}: diagram without diagram_caption")
            for fig in re.findall(r"!\[\[diagram:([^\]|]+)", post.content):
                if fig.strip() not in diagram_names:
                    errors.append(f"manual/{f.name}: unknown inline diagram {fig.strip()!r}")
            try:
                n = int(m.get("stage"))
            except (TypeError, ValueError):
                errors.append(f"manual/{f.name}: stage is not a number")
                continue
            if n in stages:
                errors.append(f"manual/{f.name}: duplicate stage {n} (also {stages[n]})")
            stages[n] = f.name
            for b in m.get("builds_on") or []:
                if int(b) >= n:
                    errors.append(f"manual/{f.name}: builds_on {b} is not an earlier stage")
        if stages and sorted(stages) != list(range(1, len(stages) + 1)):
            errors.append(f"manual: stages are not contiguous from 1: {sorted(stages)}")
        print(f"course: {len(stages)} lessons")

    print(f"pages: {len(posts)} (books {len(have)}, systems {len(posts)-len(have)}); manifest A/B rows: {len(want)}; topics: {len(list(TOPICS.glob('*.md')))}")
    for e in errors:
        print("ERR", e)
    print("OK" if not errors else f"{len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
