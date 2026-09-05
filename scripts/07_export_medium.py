"""Export Medium-ready markdown: one file per topic page and per Tier A book.

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
    # Medium has no H2/H3 distinction worth keeping; promote ## to # style headings
    text = re.sub(r"^###\s+", "**", text, flags=re.M)
    text = re.sub(r"^(\*\*[^\n]+)$", lambda m: m.group(1) + "**", text, flags=re.M)
    text = re.sub(r"^##\s+", "## ", text, flags=re.M)
    return text


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--site", default="https://ninad-k.github.io/trading-playbook/")
    a = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    for f in OUT.glob("*.md"):
        f.unlink()
    books = {f.stem: frontmatter.load(f, encoding="utf-8") for f in BOOKS.glob("*.md")}
    titles = {s: p.metadata["title"] for s, p in books.items()}
    n = 0
    for s, p in books.items():
        m = p.metadata
        if m.get("tier") != "A" or m.get("doc_type") == "system":
            continue
        body = convert(p.content, a.site, titles)
        md = f"# {m['title']}: the trader's summary\n\n*{m['one_liner']}*\n\n**{m['author']}**{' · ' + str(m['year']) if m.get('year') not in (None, 'unknown') else ''} · {m['category']} · {m['difficulty']}\n\n{body}\n\n---\n{DISCLAIMER}\n\nMore notes like this: [{a.site}]({a.site}) · Tags: {', '.join(m.get('tags', []))}\n"
        (OUT / f"book--{s}.md").write_text(md, encoding="utf-8")
        n += 1
    for name in CATEGORIES:
        f = TOPICS / f"{topic_slug(name)}.md"
        if not f.exists():
            continue
        p = frontmatter.load(f, encoding="utf-8")
        body = convert(p.content, a.site, titles)
        md = f"# {name}: what 700 trading books agree on\n\n*{p.metadata.get('summary','')}*\n\n{body}\n\n---\n{DISCLAIMER}\n\nFull library with search: [{a.site}]({a.site})\n"
        (OUT / f"topic--{topic_slug(name)}.md").write_text(md, encoding="utf-8")
        n += 1
    print(f"exported {n} Medium posts -> export/medium/")


if __name__ == "__main__":
    main()
