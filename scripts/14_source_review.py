"""Retrospective source review: pair an existing note with its extracted PDF text, then record coverage.

Usage:
  python scripts/14_source_review.py --list [--max-words 4000] [--limit 40]
  python scripts/14_source_review.py --show <slug> [<slug> ...] [--max-words 9000]
  python scripts/14_source_review.py --record-file data/review_records.json

The record file maps slug -> {"source_review": "full"|"partial", "reviewed_pdf_pages": "1-24"}.
Only `source_review` and `reviewed_pdf_pages` are written; note bodies are edited by hand.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

import frontmatter

from common import BOOKS, TXT_DIR

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def pages_of(slug: str) -> list[str]:
    p = TXT_DIR / f"{slug}.txt"
    if not p.exists():
        return []
    return p.read_text(encoding="utf-8", errors="replace").split("\f")


def clean(page: str) -> str:
    page = re.sub(r"[ \t]{3,}", "  ", page)
    page = re.sub(r"\n{3,}", "\n\n", page)
    return page.strip()


def words(s: str) -> int:
    return len(s.split())


def parents() -> list[Path]:
    return [f for f in sorted(BOOKS.glob("*.md")) if "--" not in f.stem]


def do_list(a) -> None:
    rows = []
    for f in parents():
        post = frontmatter.load(f, encoding="utf-8")
        if post.get("source_review") and not a.include_recorded:
            continue
        pgs = pages_of(f.stem)
        w = sum(words(p) for p in pgs)
        rows.append((w, f.stem, post.get("pages") or len(pgs), len(pgs), post.get("tier"), post.get("category"), post.get("source_review") or "-"))
    rows.sort()
    rows = [r for r in rows if r[0] <= a.max_words]
    total = 0
    for w, slug, pg, txtpg, tier, cat, sr in rows[: a.limit]:
        total += w
        print(f"{w:>7} w | {pg:>4}p | txt {txtpg:>4}p | {tier} | {cat[:28]:<28} | {sr:<8} | {slug}")
    print(f"# {len(rows)} unrecorded within limit; showing {min(len(rows), a.limit)}; shown words {total}")


def do_show(a) -> None:
    for slug in a.slugs:
        f = BOOKS / f"{slug}.md"
        if not f.exists():
            print(f"!! no note {slug}")
            continue
        post = frontmatter.load(f, encoding="utf-8")
        pgs = pages_of(slug)
        print(f"\n\n########## NOTE {slug} | tier={post.get('tier')} | pages={post.get('pages')} | txt_pages={len(pgs)} | words={sum(words(p) for p in pgs)}")
        print(f"# title={post.get('title')!r} author={post.get('author')!r} year={post.get('year')} category={post.get('category')!r} doc_type={post.get('doc_type')}")
        if not a.source_only:
            print("---------- NOTE BODY ----------")
            print(post.content.strip())
        print("---------- SOURCE TEXT ----------")
        budget = a.max_words
        for i, p in enumerate(pgs, 1):
            c = clean(p)
            if not c:
                continue
            print(f"\n===== p{i} =====")
            print(c)
            budget -= words(c)
            if budget <= 0:
                print(f"\n[SOURCE TRUNCATED at ~{a.max_words} words of {len(pgs)} pages]")
                break


def do_record(a) -> None:
    recs = json.loads(Path(a.record_file).read_text(encoding="utf-8"))
    n = 0
    for slug, meta in recs.items():
        f = BOOKS / f"{slug}.md"
        if not f.exists():
            print(f"!! missing note {slug}")
            continue
        post = frontmatter.load(f, encoding="utf-8")
        post["source_review"] = meta["source_review"]
        post["reviewed_pdf_pages"] = meta["reviewed_pdf_pages"]
        f.write_text(frontmatter.dumps(post) + "\n", encoding="utf-8")
        n += 1
    print(f"recorded {n} notes")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--show", dest="slugs", nargs="*")
    ap.add_argument("--source-only", action="store_true")
    ap.add_argument("--include-recorded", action="store_true")
    ap.add_argument("--record-file")
    ap.add_argument("--max-words", type=int, default=9000)
    ap.add_argument("--limit", type=int, default=60)
    a = ap.parse_args()
    if a.record_file:
        do_record(a)
    elif a.slugs:
        do_show(a)
    else:
        if not a.list:
            a.max_words = a.max_words if a.max_words != 9000 else 4000
        do_list(a)


if __name__ == "__main__":
    main()
