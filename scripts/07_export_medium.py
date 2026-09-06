"""Export Medium draft markdown: topics and Tier A books, or all parents with --all-books.

Usage: python scripts/07_export_medium.py [--site https://ninad-k.github.io/trading-playbook/]
Medium accepts pasted markdown-ish text and can also import a public URL ("Import a story").
"""
from __future__ import annotations

import argparse
import re

import frontmatter

from common import BOOKS, CATEGORIES, ROOT, TOPICS

OUT = ROOT / "export" / "medium"
DISCLAIMER = "*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*"


def topic_slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def convert(text: str, site: str, titles: dict) -> str:
    def repl(m):
        s = m.group(1)
        return f"[{titles.get(s, s)}]({site}books/{s}.html)"
    text = re.sub(r"\[\[([^\]|]+)\]\]", repl, text)
    # Keep valid Markdown headings and existing emphasis intact in the editable draft.
    return text


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default="https://ninad-k.github.io/trading-playbook/")
    ap.add_argument("--all-books", action="store_true", help="Include concise Tier B notes as well as Tier A books")
    a = ap.parse_args()
    a.site = a.site.rstrip('/') + '/'
    if OUT.resolve() != ROOT.resolve() / "export" / "medium":
        raise ValueError("Refusing to regenerate exports outside the repository")
    OUT.mkdir(parents=True, exist_ok=True)
    for f in [*OUT.glob("book--*.md"), *OUT.glob("topic--*.md")]:
        f.unlink()
    books = {f.stem: frontmatter.load(f, encoding="utf-8") for f in BOOKS.glob("*.md")}
    titles = {s: p.metadata["title"] for s, p in books.items()}
    n = 0
    for s, p in books.items():
        m = p.metadata
        if (m.get("tier") != "A" and not a.all_books) or m.get("doc_type") == "system":
            continue
        body = convert(p.content, a.site, titles)
        coverage = m.get("source_review", "not recorded")
        inspected = m.get("reviewed_pdf_pages", "not recorded")
        body = f"*Source coverage: {coverage}. PDF pages inspected: {inspected}. These are study notes, not verified trading results.*\n\n" + body
        md = f"# {m['title']}: the trader's summary\n\n*{m['one_liner']}*\n\n**{m['author']}**{' · ' + str(m['year']) if m.get('year') not in (None, 'unknown') else ''} · {m['category']} · {m['difficulty']}\n\n{body}\n\n---\n{DISCLAIMER}\n\nMore notes like this: [{a.site}]({a.site}) · Tags: {', '.join(m.get('tags', []))}\n"
        (OUT / f"book--{s}.md").write_text(md, encoding="utf-8")
        n += 1
    for name in CATEGORIES:
        f = TOPICS / f"{topic_slug(name)}.md"
        if not f.exists():
            continue
        p = frontmatter.load(f, encoding="utf-8")
        body = convert(p.content, a.site, titles)
        md = f"# {name}: a trading-library study guide\n\n*{p.metadata.get('summary','')}*\n\n{body}\n\n---\n{DISCLAIMER}\n\nFull library with search: [{a.site}]({a.site})\n"
        (OUT / f"topic--{topic_slug(name)}.md").write_text(md, encoding="utf-8")
        n += 1
    print(f"exported {n} Medium posts -> export/medium/")


if __name__ == "__main__":
    main()
