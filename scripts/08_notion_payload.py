"""Emit Notion-ready payloads (properties + Notion-flavored Markdown) for book/topic pages.

Usage:
  python scripts/08_notion_payload.py <slug> [<slug> ...]      # payloads for these slugs (JSON list on stdout)
  python scripts/08_notion_payload.py --pending [--limit 10] [--kind book|system|topic]
                                                                # next unsynced pages per data/notion_ids.json
  python scripts/08_notion_payload.py --record slug=notion_page_id [...]   # record created page ids
  python scripts/08_notion_payload.py --topic <topic-slug>       # payload for a topic page

Each payload: {"slug", "kind": "book|system|topic", "parent_slug" (systems only), "title", "properties": {...}, "content": "..."}
Books/systems go in the Books data source (data/notion_ids.json -> books_data_source_id); system pages should be
created as children of their parent book page (parent page_id = pages[parent_slug]) so they nest under the book.
"""
from __future__ import annotations

import argparse
import json
import re
import sys

import frontmatter

from common import BOOKS, CATEGORIES, DATA, TOPICS

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
IDS = DATA / "notion_ids.json"
SITE = "https://ninad-k.github.io/trading-playbook/"
DISCLAIMER = "Educational summary in the author's own words. Not financial advice. Please buy the book if these notes are useful."
NOTION_CATEGORY = {c: c.replace(",", "") for c in CATEGORIES}  # Notion select options cannot contain commas
KNOWN_TAGS = {"trend-following", "money-management", "psychology", "forex", "options", "candlesticks", "fibonacci", "elliott-wave", "indicators", "day-trading", "swing-trading", "microstructure", "value-investing"}


def load_ids() -> dict:
    d = json.loads(IDS.read_text(encoding="utf-8")) if IDS.exists() else {}
    d.setdefault("pages", {})
    return d


def titles() -> dict:
    out = {}
    for f in BOOKS.glob("*.md"):
        try:
            out[f.stem] = frontmatter.load(f, encoding="utf-8").metadata.get("title", f.stem)
        except Exception:  # noqa: BLE001
            out[f.stem] = f.stem
    return out


def esc(text: str) -> str:
    """Escape characters Notion treats specially, outside code spans, while keeping **bold**, *italic*, [links](url)."""
    parts = re.split(r"(`[^`]*`)", text)
    for i, p in enumerate(parts):
        if i % 2 == 1:
            continue
        p = p.replace("\\", "\\\\")
        p = re.sub(r"[<>{}|^$]", lambda m: "\\" + m.group(0), p)
        p = re.sub(r"(?<!~)~(?!~)", r"\\~", p)
        parts[i] = p
    return "".join(parts)


def table_to_notion(lines: list[str]) -> str:
    rows = []
    for ln in lines:
        cells = [c.strip() for c in ln.strip().strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            continue
        rows.append(cells)
    if not rows:
        return ""
    out = ['<table header-row="true" fit-page-width="true">']
    for r in rows:
        out.append("\t<tr>" + "".join(f"<td>{esc(c)}</td>" for c in r) + "</tr>")
    out.append("</table>")
    return "\n".join(out)


def convert(md: str, tmap: dict) -> str:
    md = re.sub(r"\[\[([^\]|]+)\]\]", lambda m: f"[{tmap.get(m.group(1), m.group(1))}]({SITE}books/{m.group(1)}.html)", md)
    out, i, lines = [], 0, md.splitlines()
    in_code = False
    while i < len(lines):
        ln = lines[i]
        if ln.strip().startswith("```"):
            in_code = not in_code
            out.append(ln)
            i += 1
            continue
        if in_code:
            out.append(ln)
            i += 1
            continue
        if ln.lstrip().startswith("|"):
            j = i
            while j < len(lines) and lines[j].lstrip().startswith("|"):
                j += 1
            out.append(table_to_notion(lines[i:j]))
            i = j
            continue
        if not ln.strip():
            i += 1
            continue
        m = re.match(r"^(\s+)([-*+]|\d+\.)\s", ln)
        if m:
            depth = len(m.group(1).replace("\t", "    ")) // 2
            ln = "\t" * max(1, depth // 1 if depth < 2 else depth // 2) + ln.lstrip()
        if re.match(r"^#{5,}\s", ln):
            ln = "#### " + ln.lstrip("#").strip()
        # escape body text but keep heading markers / list markers intact
        mm = re.match(r"^(\t*)(#{1,4}\s|[-*+]\s|\d+\.\s|>\s?)?(.*)$", ln)
        prefix = (mm.group(1) or "") + (mm.group(2) or "")
        body = mm.group(3)
        out.append(prefix + esc(body))
        i += 1
    return "\n".join(out)


def book_payload(slug: str, tmap: dict) -> dict:
    p = frontmatter.load(BOOKS / f"{slug}.md", encoding="utf-8")
    m = p.metadata
    kind = "system" if m.get("doc_type") == "system" else "book"
    tags = [t for t in m.get("tags", []) if t in KNOWN_TAGS]
    props = {
        "Title": m["title"], "Author": str(m.get("author", "")), "Year": str(m.get("year", "")),
        "Tier": m.get("tier"), "Category": NOTION_CATEGORY.get(m.get("category"), m.get("category")),
        "Difficulty": m.get("difficulty"), "Doc type": m.get("doc_type"), "Tags": tags,
        "Pages": int(m.get("pages") or 0), "One-liner": m.get("one_liner", ""), "Slug": slug,
        "Site URL": f"{SITE}books/{slug}.html",
    }
    head = (f'<callout icon="📘" color="gray_bg">\n\t**{esc(str(m.get("author","")))}**'
            f'{" · " + esc(str(m["year"])) if m.get("year") not in (None, "unknown") else ""} · {esc(m.get("category",""))} · Tier {m.get("tier")} · {m.get("difficulty")}\n'
            f'\t{esc(m.get("one_liner",""))}\n</callout>')
    body = convert(p.content, tmap)
    coverage = esc(str(m.get("source_review", "not recorded")))
    inspected = esc(str(m.get("reviewed_pdf_pages", "not recorded")))
    body = f"**Source coverage:** {coverage}. PDF pages inspected: {inspected}. Study notes do not establish verified trading results.\n\n" + body
    related = [f"[{tmap.get(r, r)}]({SITE}books/{r}.html)" for r in m.get("related", []) if r in tmap]
    tail = ("\n---\n" + (("**Related in this library:** " + " · ".join(related) + "\n") if related else "") + f"*{DISCLAIMER}*")
    return {"slug": slug, "kind": kind, "parent_slug": m.get("parent"), "title": m["title"], "properties": props, "content": head + "\n" + body + tail}


def topic_payload(tslug: str, tmap: dict) -> dict:
    p = frontmatter.load(TOPICS / f"{tslug}.md", encoding="utf-8")
    title = p.metadata.get("title") or tslug.replace("-", " ").title()
    head = f'<callout icon="🧭" color="blue_bg">\n\t{esc(p.metadata.get("summary",""))}\n</callout>' if p.metadata.get("summary") else ""
    return {"slug": tslug, "kind": "topic", "title": title, "properties": {"title": title}, "content": head + "\n" + convert(p.content, tmap) + f"\n---\n*{DISCLAIMER}*"}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--pending", action="store_true")
    ap.add_argument("--limit", type=int, default=10)
    ap.add_argument("--kind", default="book")
    ap.add_argument("--record", nargs="*")
    ap.add_argument("--topic")
    a = ap.parse_args()
    ids = load_ids()
    if a.record:
        for kv in a.record:
            s, pid = kv.split("=", 1)
            ids["pages"][s] = pid
        IDS.write_text(json.dumps(ids, indent=1), encoding="utf-8")
        print(f"recorded {len(a.record)}; total {len(ids['pages'])}")
        return
    tmap = titles()
    if a.topic:
        print(json.dumps([topic_payload(a.topic, tmap)], ensure_ascii=False, indent=1))
        return
    slugs = a.slugs
    if a.pending:
        done = set(ids["pages"])
        cand = []
        for f in sorted(BOOKS.glob("*.md")):
            if f.stem in done:
                continue
            is_sys = "--" in f.stem
            if a.kind == "book" and is_sys:
                continue
            if a.kind == "system":
                if not is_sys:
                    continue
                parent = f.stem.split("--")[0]
                if parent not in done:
                    continue  # parent must exist first
            cand.append(f.stem)
        slugs = cand[: a.limit]
        if not slugs:
            print("[]")
            return
    print(json.dumps([book_payload(s, tmap) for s in slugs], ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
