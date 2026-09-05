"""Build the static site into docs/ from content/ + data/manifest.json.

Usage: python scripts/06_build_site.py
Output: docs/index.html, docs/search.html, docs/books/<slug>.html, docs/topics/<slug>.html,
        docs/paths.html, docs/search-index.json, docs/assets/*
All links are relative so the site works on GitHub Pages (/trading-playbook/) and from file://.
"""
from __future__ import annotations

import json
import re
import shutil
from collections import defaultdict

import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

from common import BOOKS, CATEGORIES, CONTENT, DOCS, ROOT, TOPICS, load_manifest

SITE_TITLE = "Trading Playbook"
TAGLINE = "700+ trading books, distilled and indexed."
DISCLAIMER = "Educational summaries only. Nothing here is financial advice. Test every rule before risking capital."

env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html"]))
MD = markdown.Markdown(extensions=["tables", "toc", "sane_lists", "smarty", "attr_list"], extension_configs={"toc": {"toc_depth": "2-3"}})


def topic_slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def render_md(text: str, link_prefix: str, slugs: set[str], titles: dict[str, str]) -> str:
    def repl(m):
        s = m.group(1)
        if s in slugs:
            return f'<a class="xref" href="{link_prefix}books/{s}.html">{titles.get(s, s)}</a>'
        return m.group(0)
    text = re.sub(r"\[\[([^\]|]+)\]\]", repl, text)
    MD.reset()
    return MD.convert(text)


def load_books():
    books = {}
    for f in sorted(BOOKS.glob("*.md")):
        p = frontmatter.load(f, encoding="utf-8")
        books[f.stem] = p
    return books


def main() -> None:
    if DOCS.exists():
        for child in DOCS.iterdir():
            if child.name in (".nojekyll", "CNAME"):
                continue
            shutil.rmtree(child) if child.is_dir() else child.unlink()
    (DOCS / "books").mkdir(parents=True, exist_ok=True)
    (DOCS / "topics").mkdir(parents=True, exist_ok=True)
    (DOCS / "assets").mkdir(parents=True, exist_ok=True)
    (DOCS / ".nojekyll").write_text("")
    for asset in (ROOT / "templates" / "assets").glob("*"):
        shutil.copy(asset, DOCS / "assets" / asset.name)

    manifest = load_manifest()
    books = load_books()
    titles = {s: p.metadata["title"] for s, p in books.items()}
    slugs = set(books)
    systems_by_parent = defaultdict(list)
    for s, p in books.items():
        if p.metadata.get("doc_type") == "system":
            systems_by_parent[p.metadata.get("parent")].append(s)

    topics = []
    for name in CATEGORIES:
        ts = topic_slug(name)
        f = TOPICS / f"{ts}.md"
        if f.exists():
            topics.append({"name": name, "slug": ts, "post": frontmatter.load(f, encoding="utf-8")})
    nav_topics = [{"name": t["name"], "slug": t["slug"]} for t in topics]

    base_ctx = dict(site_title=SITE_TITLE, tagline=TAGLINE, disclaimer=DISCLAIMER, nav_topics=nav_topics)

    # ---- book pages
    tpl_book = env.get_template("book.html")
    search_rows = []
    for s, p in books.items():
        m = p.metadata
        html = render_md(p.content, "../", slugs, titles)
        related = [{"slug": r, "title": titles[r], "one_liner": books[r].metadata.get("one_liner", "")} for r in m.get("related", []) if r in books]
        parent = None
        if m.get("parent") in books:
            parent = {"slug": m["parent"], "title": titles[m["parent"]]}
        systems = [{"slug": x, "title": titles[x]} for x in systems_by_parent.get(s, [])]
        cat_slug = topic_slug(m.get("category", ""))
        out = tpl_book.render(**base_ctx, root="../", m=m, body=html, related=related, parent=parent, systems=systems, cat_slug=cat_slug, toc=MD.toc)
        (DOCS / "books" / f"{s}.html").write_text(out, encoding="utf-8")
        # search text: strip markdown, keep headings + first 1200 words
        plain = re.sub(r"[#*`>\[\]_]|\[\[|\]\]", " ", p.content)
        plain = re.sub(r"\s+", " ", plain)[:6000]
        search_rows.append({
            "slug": s, "title": m["title"], "author": str(m.get("author", "")), "year": str(m.get("year", "")),
            "category": m.get("category", ""), "tier": m.get("tier", ""), "difficulty": m.get("difficulty", ""),
            "doc_type": m.get("doc_type", ""), "tags": " ".join(m.get("tags", [])), "one_liner": m.get("one_liner", ""),
            "text": plain,
        })
    (DOCS / "search-index.json").write_text(json.dumps(search_rows, ensure_ascii=False), encoding="utf-8")

    # ---- topic pages
    tpl_topic = env.get_template("topic.html")
    for t in topics:
        m = t["post"].metadata
        html = render_md(t["post"].content, "../", slugs, titles)
        in_cat = sorted(
            [{"slug": s, "title": titles[s], "author": p.metadata.get("author", ""), "tier": p.metadata.get("tier"), "one_liner": p.metadata.get("one_liner", ""), "doc_type": p.metadata.get("doc_type")}
             for s, p in books.items() if p.metadata.get("category") == t["name"] and p.metadata.get("doc_type") != "system"],
            key=lambda x: (x["tier"] != "A", x["title"].lower()))
        out = tpl_topic.render(**base_ctx, root="../", name=t["name"], m=m, body=html, in_cat=in_cat, toc=MD.toc)
        (DOCS / "topics" / f"{t['slug']}.html").write_text(out, encoding="utf-8")

    # ---- paths page
    pf = CONTENT / "paths.md"
    if pf.exists():
        post = frontmatter.load(pf, encoding="utf-8")
        html = render_md(post.content, "", slugs, titles)
        (DOCS / "paths.html").write_text(env.get_template("page.html").render(**base_ctx, root="", title="Reading paths", body=html, toc=MD.toc), encoding="utf-8")

    # ---- index
    by_cat = defaultdict(list)
    by_author = defaultdict(list)
    articles, systems = [], []
    for s, p in books.items():
        m = p.metadata
        entry = {"slug": s, "title": m["title"], "author": m.get("author", ""), "tier": m.get("tier"), "one_liner": m.get("one_liner", ""), "doc_type": m.get("doc_type"), "year": m.get("year", ""), "pages": m.get("pages", "")}
        if m.get("doc_type") == "system":
            systems.append({**entry, "parent_title": titles.get(m.get("parent"), "")})
            continue
        by_cat[m.get("category")].append(entry)
        by_author[str(m.get("author", "Unknown")).strip() or "Unknown"].append(entry)
        if m.get("doc_type") in ("article", "paper"):
            articles.append(entry)
    for lst in by_cat.values():
        lst.sort(key=lambda x: (x["tier"] != "A", x["title"].lower()))
    az = sorted(by_cat_entries := [e for l in by_cat.values() for e in l], key=lambda x: re.sub(r"^(the|a|an)\s+", "", x["title"].lower()))
    excluded = defaultdict(list)
    for r in manifest:
        if r.get("ext") != "pdf":
            excluded["not_pdf"].append(r["filename"])
        elif r.get("tier") == "C":
            excluded[r.get("c_status", "excluded")].append(r["filename"] + (f"  (same as: {r['dup_of']})" if r.get("dup_of") else ""))
    counts = {
        "files": len(manifest), "pdfs": sum(r.get("ext") == "pdf" for r in manifest),
        "tier_a": sum(1 for p in books.values() if p.metadata.get("tier") == "A" and p.metadata.get("doc_type") != "system"),
        "tier_b": sum(1 for p in books.values() if p.metadata.get("tier") == "B" and p.metadata.get("doc_type") != "system"),
        "systems": len(systems), "excluded": sum(len(v) for v in excluded.values()),
    }
    cat_groups = [{"name": c, "slug": topic_slug(c), "items": by_cat.get(c, [])} for c in CATEGORIES if by_cat.get(c)]
    authors = sorted(((a, sorted(l, key=lambda x: x["title"].lower())) for a, l in by_author.items() if a.lower() not in ("unknown", "various", "")), key=lambda x: x[0].split()[-1].lower())
    out = env.get_template("index.html").render(**base_ctx, root="", counts=counts, cat_groups=cat_groups, az=az, authors=authors, systems=sorted(systems, key=lambda x: x["title"].lower()), articles=sorted(articles, key=lambda x: x["title"].lower()), excluded=dict(excluded), has_paths=pf.exists())
    (DOCS / "index.html").write_text(out, encoding="utf-8")
    (DOCS / "search.html").write_text(env.get_template("search.html").render(**base_ctx, root="", categories=CATEGORIES[:-1]), encoding="utf-8")
    print(f"built: {len(books)} book pages, {len(topics)} topics, index, search ({len(search_rows)} entries)")


if __name__ == "__main__":
    main()
