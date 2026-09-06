"""Build the static site into docs/ from content/ + data/manifest.json.

Usage: python scripts/06_build_site.py
Output: docs/index.html, docs/search.html, docs/books/<slug>.html, docs/topics/<slug>.html,
        docs/paths.html, docs/search-index.json, docs/assets/*
All links are relative so the site works on GitHub Pages (/trading-playbook/) and from file://.
"""
from __future__ import annotations

import json
import hashlib
import re
import shutil
from html import escape
from collections import Counter, defaultdict

import frontmatter
import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

from common import BOOKS, CATEGORIES, CONTENT, DOCS, ROOT, TOPICS, load_manifest

SITE_TITLE = "Trading Playbook"
TAGLINE = "Trading books, explained and connected."
DISCLAIMER = "Educational summaries only. Nothing here is financial advice. Test every rule before risking capital."

BLANK = chr(10) * 2  # forces the figure onto its own markdown block

DIAGRAMS: dict[str, str] = {}

# Which schematic leads which topic page. A topic absent from this map simply has no hero figure.
TOPIC_DIAGRAM = {
    "market-structure-price-action": ("market-structure", "Swing structure, and the break that ends it."),
    "candlesticks-chart-patterns": ("candle-anatomy", "What a single candle records, and three shapes the books return to."),
    "indicators": ("divergence", "Divergence: the disagreement between price and an oscillator."),
    "fibonacci-gann-elliott-wave": ("elliott-fibonacci", "The wave count and the retracement ratios these books argue over."),
    "trend-following-mechanical-systems": ("ma-crossover", "Why a bare crossover rule needs a filter."),
    "day-trading-scalping": ("opening-range", "The opening-range breakout, the session's most-written-about trade."),
    "swing-trading": ("pullback-entry", "The pullback entry, priced in R."),
    "forex-mechanics-macro-drivers": ("forex-quote", "The quote you actually trade against."),
    "options-futures-derivatives": ("option-payoffs", "Four shapes every options position reduces to."),
    "money-management-position-sizing": ("position-sizing", "Size comes from risk; recovery arithmetic is why."),
    "trading-psychology-discipline": ("psychology-loop", "The loop the discipline books are trying to break."),
    "quant-microstructure-academic-research": ("order-book", "The costs a close-only backtest cannot see."),
    "investing-value-market-history": ("market-cycle", "The four phases, named since Wyckoff."),
}


def load_diagrams() -> dict[str, str]:
    d = CONTENT / "diagrams"
    if not d.exists():
        return {}
    return {f.stem: f.read_text(encoding="utf-8").strip() for f in sorted(d.glob("*.svg"))}


def figure(name: str, caption: str = "") -> str:
    """Inline a generated schematic as a self-contained <figure>."""
    svg = DIAGRAMS.get(name)
    if not svg:
        return ""
    cap = f"<figcaption>{escape(caption)}</figcaption>" if caption else ""
    return f'<figure class="fig" id="fig-{escape(name)}">{svg}{cap}</figure>'


env = Environment(loader=FileSystemLoader(ROOT / "templates"), autoescape=select_autoescape(["html"]))
MD = markdown.Markdown(extensions=["tables", "toc", "sane_lists", "smarty", "attr_list"], extension_configs={"toc": {"toc_depth": "2-3"}})


def topic_slug(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def render_md(text: str, link_prefix: str, slugs: set[str], titles: dict[str, str]) -> str:
    figs: list[str] = []

    def fig_repl(m):
        name, _, caption = m.group(1).partition("|")
        html = figure(name.strip(), caption.strip())
        if not html:
            return ""
        figs.append(html)
        return BLANK + f"FIGPLACEHOLDER{len(figs) - 1}ENDFIG" + BLANK

    text = re.sub(r"!\[\[diagram:([^\]]+)\]\]", fig_repl, text)

    def repl(m):
        s = m.group(1)
        if s in slugs:
            return f'<a class="xref" href="{link_prefix}books/{s}.html">{escape(titles.get(s, s))}</a>'
        return m.group(0)
    text = re.sub(r"\[\[([^\]|]+)\]\]", repl, text)
    MD.reset()
    html = MD.convert(text)
    for i, f in enumerate(figs):
        html = html.replace(f"<p>FIGPLACEHOLDER{i}ENDFIG</p>", f).replace(f"FIGPLACEHOLDER{i}ENDFIG", f)
    return html


CHART_FONT = "-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif"
CHART_CSS = (
    "<style>"
    ".c-bg{fill:var(--card,#ffffff)}"
    ".c-a{fill:var(--accent,#0b6e4f)}.c-b{fill:var(--accent2,#b8862b)}"
    ".c-m{fill:var(--muted,#6b6b66)}.c-l{fill:var(--line,#e4e2dc)}"
    f".c-t{{fill:var(--fg,#1c1c1a);font:600 13px {CHART_FONT}}}"
    f".c-s{{fill:var(--muted,#6b6b66);font:12px {CHART_FONT}}}"
    f".c-n{{fill:var(--fg,#1c1c1a);font:600 12px {CHART_FONT}}}"
    f".c-w{{fill:#ffffff;font:600 12px {CHART_FONT}}}"
    "</style>"
)


def chart_categories(rows: list[tuple[str, int]]) -> str:
    """Horizontal bar chart of notes per category, drawn from the live counts."""
    if not rows:
        return ""
    lab_w, bar_w, rh, top = 250, 372, 24, 34
    h = top + len(rows) * rh + 30
    top_n = max(n for _, n in rows)
    body = [f'<rect width="720" height="{h}" rx="8" class="c-bg"/>' + CHART_CSS]
    body.append(f'<text x="20" y="22" class="c-t">Notes per category &#8212; {sum(n for _, n in rows)} in total</text>')
    for i, (name, n) in enumerate(rows):
        y = top + i * rh
        w = max(2, n / top_n * bar_w)
        body.append(f'<text x="{lab_w - 8}" y="{y + 15}" class="c-s" text-anchor="end">{escape(name)}</text>')
        body.append(f'<rect x="{lab_w}" y="{y + 4}" width="{w:.1f}" height="15" rx="2" class="c-a"/>')
        body.append(f'<text x="{lab_w + w + 7:.1f}" y="{y + 16}" class="c-n">{n}</text>')
    body.append(f'<text x="20" y="{h - 10}" class="c-s">Every note sits in exactly one category. Method sub-pages are counted with their parent book.</text>')
    return ('<figure class="fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 '
            f'{h}" class="diagram" role="img" aria-label="Bar chart of the number of notes in each '
            f'category">{"".join(body)}</svg></figure>')


def _stack(y, segs, total, label, note):
    """One stacked bar plus a swatch legend, so each slice is identifiable."""
    x, out = 20, [f'<text x="20" y="{y - 10}" class="c-t">{escape(label)}</text>']
    shades = [1.0, 0.72, 0.5, 0.33]
    for i, (name, n, cls) in enumerate(segs):
        w = n / total * 680
        op = "" if cls == "c-a" else f' opacity="{shades[min(i, 3)]}"'
        out.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="30" class="{cls}"{op}/>')
        if w > 40:
            out.append(f'<text x="{x + w / 2:.1f}" y="{y + 20}" class="c-w" text-anchor="middle">{n}</text>')
        x += w
    lx = 20
    for i, (name, n, cls) in enumerate(segs):
        op = "" if cls == "c-a" else f' opacity="{shades[min(i, 3)]}"'
        out.append(f'<rect x="{lx}" y="{y + 40}" width="11" height="11" rx="2" class="{cls}"{op}/>')
        out.append(f'<text x="{lx + 16}" y="{y + 50}" class="c-s">{escape(name)} {n}</text>')
        lx += 26 + len(f"{name} {n}") * 6.6
    if note:
        out.append(f'<text x="20" y="{y + 72}" class="c-s">{escape(note)}</text>')
    return "".join(out)


def chart_coverage(full: int, partial: int, buckets: list[tuple[str, int]]) -> str:
    """Two stacked bars: what became of every PDF, and how deeply the notes were read."""
    total_pdf = sum(n for _, n in buckets)
    body = ['<rect width="720" height="278" rx="8" class="c-bg"/>' + CHART_CSS]
    body.append(_stack(46, [(n, v, "c-a" if i == 0 else "c-b") for i, (n, v) in enumerate(buckets)],
                       total_pdf, f"All {total_pdf} source PDFs",
                       "A duplicate points at its canonical note; an off-topic or damaged file gets a "
                       "stated reason, never an invented summary."))
    body.append(_stack(184, [("full source review", full, "c-a"), ("partial", partial, "c-b")],
                       full + partial, f"Reading depth recorded on the {full + partial} notes",
                       "Partial is not a gap in the record: it names the exact pages read, and why the "
                       "rest could not be."))
    return ('<figure class="fig"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 278" '
            'class="diagram" role="img" aria-label="Stacked bars showing how the source PDFs were '
            'classified and how deeply each note was read">' + "".join(body) + "</svg></figure>")


def load_books():
    books = {}
    for f in sorted(BOOKS.glob("*.md")):
        p = frontmatter.load(f, encoding="utf-8")
        books[f.stem] = p
    return books


def main() -> None:
    DIAGRAMS.update(load_diagrams())
    if DOCS.resolve() != ROOT.resolve() / "docs":
        raise ValueError("Refusing to regenerate an output directory outside the repository")
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
        post = frontmatter.load(f, encoding="utf-8") if f.exists() else None
        topics.append({"name": name, "slug": ts, "post": post})
    nav_topics = [{"name": t["name"], "slug": t["slug"]} for t in topics]

    style_version = hashlib.sha256((DOCS / "assets" / "site.css").read_bytes()).hexdigest()[:12]
    base_ctx = dict(site_title=SITE_TITLE, tagline=TAGLINE, disclaimer=DISCLAIMER, nav_topics=nav_topics, has_paths=(CONTENT / "paths.md").exists(), has_about=(CONTENT / "about.md").exists(), style_version=style_version)

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
        out = tpl_book.render(**base_ctx, root="../", m=m, body=html, related=related, parent=parent,
                              systems=systems, cat_slug=cat_slug, toc=MD.toc,
                              hero=figure(str(m.get("diagram", "")), str(m.get("diagram_caption", ""))))
        (DOCS / "books" / f"{s}.html").write_text(out, encoding="utf-8")
        # Keep the complete note in the local search index. The browser search is
        # intentionally simple, so it can also run when search.html is opened via file://.
        plain = re.sub(r"[#*`>\[\]_]|\[\[|\]\]", " ", p.content)
        plain = re.sub(r"\s+", " ", plain).strip()
        search_rows.append({
            "slug": s, "title": m["title"], "author": str(m.get("author", "")), "year": str(m.get("year", "")),
            "category": m.get("category", ""), "tier": m.get("tier", ""), "difficulty": m.get("difficulty", ""),
            "doc_type": m.get("doc_type", ""), "tags": " ".join(m.get("tags", [])), "one_liner": m.get("one_liner", ""),
            "text": plain, "url": f"books/{s}.html",
        })

    # ---- topic pages
    tpl_topic = env.get_template("topic.html")
    for t in topics:
        post = t["post"]
        m = post.metadata if post else {}
        html = render_md(post.content, "../", slugs, titles) if post else ""
        in_cat = sorted(
            [{"slug": s, "title": titles[s], "author": p.metadata.get("author", ""), "tier": p.metadata.get("tier"), "one_liner": p.metadata.get("one_liner", ""), "doc_type": p.metadata.get("doc_type")}
             for s, p in books.items() if p.metadata.get("category") == t["name"] and p.metadata.get("doc_type") != "system"],
            key=lambda x: (x["tier"] != "A", x["title"].lower()))
        hero_name, hero_cap = TOPIC_DIAGRAM.get(t["slug"], ("", ""))
        out = tpl_topic.render(**base_ctx, root="../", name=t["name"], m=m, body=html, in_cat=in_cat,
                               toc=MD.toc, has_synthesis=bool(post), hero=figure(hero_name, hero_cap))
        (DOCS / "topics" / f"{t['slug']}.html").write_text(out, encoding="utf-8")
        search_rows.append({
            "slug": t["slug"], "title": t["name"], "author": "", "year": "",
            "category": t["name"], "tier": "", "difficulty": "", "doc_type": "topic",
            "tags": t["name"], "one_liner": m.get("summary", "Catalog of available notes in this category."),
            "text": re.sub(r"\s+", " ", post.content if post else "").strip(),
            "url": f"topics/{t['slug']}.html",
        })

    (DOCS / "search-data.js").write_text(
        "window.TRADING_PLAYBOOK_SEARCH = " + json.dumps(search_rows, ensure_ascii=False) + ";\n",
        encoding="utf-8",
    )
    # Preserve the JSON export for existing consumers; search.html uses the
    # adjacent JS file so it also works when opened directly from disk.
    (DOCS / "search-index.json").write_text(json.dumps(search_rows, ensure_ascii=False), encoding="utf-8")

    # ---- paths page
    pf = CONTENT / "paths.md"
    if pf.exists():
        post = frontmatter.load(pf, encoding="utf-8")
        html = render_md(post.content, "", slugs, titles)
        (DOCS / "paths.html").write_text(env.get_template("page.html").render(**base_ctx, root="", title="Reading paths", body=html, toc=MD.toc), encoding="utf-8")

    # ---- about page
    af = CONTENT / "about.md"
    if af.exists():
        post = frontmatter.load(af, encoding="utf-8")
        html = render_md(post.content, "", slugs, titles)
        (DOCS / "about.html").write_text(
            env.get_template("page.html").render(**base_ctx, root="", title=post.metadata.get("title", "About"),
                                                 body=html, toc=MD.toc), encoding="utf-8")

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
    counts["pending"] = sum(r.get("tier") in ("A", "B") and r["slug"] not in books for r in manifest)
    counts["partial"] = sum(p.get("source_review") == "partial" and p.get("doc_type") != "system" for p in books.values())
    counts["full"] = sum(p.get("source_review") == "full" and p.get("doc_type") != "system" for p in books.values())
    cat_chart = chart_categories([(c_, len(by_cat[c_])) for c_ in CATEGORIES if by_cat.get(c_)])
    cstat = Counter(r.get("c_status") for r in manifest if r.get("tier") == "C")
    buckets = [("with a note", counts["tier_a"] + counts["tier_b"]), ("duplicate", cstat.get("duplicate", 0)),
               ("off topic", cstat.get("off_topic", 0)), ("damaged", cstat.get("corrupt", 0))]
    cov_chart = chart_coverage(counts["full"], counts["partial"], [b for b in buckets if b[1]])
    cat_groups = [{"name": c, "slug": topic_slug(c), "items": by_cat.get(c, [])} for c in CATEGORIES if by_cat.get(c)]
    authors = sorted(((a, sorted(l, key=lambda x: x["title"].lower())) for a, l in by_author.items() if a.lower() not in ("unknown", "various", "")), key=lambda x: x[0].split()[-1].lower())
    out = env.get_template("index.html").render(**base_ctx, root="", counts=counts, cat_chart=cat_chart, cat_groups=cat_groups, az=az, authors=authors, systems=sorted(systems, key=lambda x: x["title"].lower()), articles=sorted(articles, key=lambda x: x["title"].lower()), excluded=dict(excluded))
    (DOCS / "index.html").write_text(out, encoding="utf-8")
    search_version = hashlib.sha256((DOCS / "search-data.js").read_bytes()).hexdigest()[:12]
    (DOCS / "search.html").write_text(env.get_template("search.html").render(**base_ctx, root="", categories=CATEGORIES, search_version=search_version, hide_topsearch=True), encoding="utf-8")
    # Public inventory exposes bibliographic labels and review outcomes, never source URLs.
    manifest_by_slug = {r["slug"]: r for r in manifest}
    coverage = []
    for row in manifest:
        if row.get("ext") != "pdf":
            continue
        slug = row["slug"]
        post = books.get(slug)
        target = slug
        seen = set()
        while target not in books and target not in seen:
            seen.add(target)
            target = manifest_by_slug.get(target, {}).get("dup_of")
            if not target:
                break
        target = target if target in books else None
        state = ("Full source review" if post.get("source_review") == "full" else "Partial source review" if post.get("source_review") == "partial" else "Existing note; coverage not recorded") if post else row.get("c_status", "Awaiting note").replace("_", " ").capitalize()
        entry = {"slug": slug, "title": titles.get(slug) or row.get("pdf_title") or row["filename"],
                 "state": state, "detail": post.get("reviewed_pdf_pages", "") if post else row.get("tier_reason", ""),
                 "target": target, "target_title": titles.get(target, "")}
        coverage.append(entry)
        if not post and row.get("c_status") == "duplicate" and target:
            (DOCS / "books" / (slug + ".html")).write_text(env.get_template("alias.html").render(**base_ctx, root="../", item=entry), encoding="utf-8")
    (DOCS / "coverage.html").write_text(env.get_template("coverage.html").render(**base_ctx, root="", coverage=coverage, cov_chart=cov_chart), encoding="utf-8")
    print(f"built: {len(books)} book pages, {len(topics)} topics, index, search ({len(search_rows)} entries)")


if __name__ == "__main__":
    main()
