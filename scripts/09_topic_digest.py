"""Digest of every book page in a category, for the topic-synthesis agents.

Usage:
  python scripts/09_topic_digest.py "Money Management & Position Sizing"            # frontmatter + key sections
  python scripts/09_topic_digest.py "Indicators" --sections "Key concepts,Rules and setups,Key points,Actionable rules"
  python scripts/09_topic_digest.py --list                                           # categories with counts
  python scripts/09_topic_digest.py --terms                                          # every **Term** — definition across all pages (for the glossary)
  python scripts/09_topic_digest.py --tag kelly                                      # pages whose tags/title/one_liner mention a word
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict

import frontmatter

from common import BOOKS, CATEGORIES

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
DEFAULT_SECTIONS = ["Core thesis", "Key concepts", "Rules and setups", "Risk and money management", "Strengths and caveats", "Summary", "Key points", "Actionable rules", "Caveats", "What it is", "Rules"]


def sections(body: str) -> dict[str, str]:
    out, cur, buf = {}, None, []
    for ln in body.splitlines():
        m = re.match(r"^##\s+(.+)$", ln)
        if m:
            if cur:
                out[cur] = "\n".join(buf).strip()
            cur, buf = m.group(1).strip(), []
        else:
            buf.append(ln)
    if cur:
        out[cur] = "\n".join(buf).strip()
    return out


def load():
    pages = {}
    for f in sorted(BOOKS.glob("*.md")):
        try:
            pages[f.stem] = frontmatter.load(f, encoding="utf-8")
        except Exception as e:  # noqa: BLE001
            print(f"[skip {f.name}: {e}]", file=sys.stderr)
    return pages


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("category", nargs="?")
    ap.add_argument("--sections", default=",".join(DEFAULT_SECTIONS))
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--terms", action="store_true")
    ap.add_argument("--tag")
    ap.add_argument("--max-words", type=int, default=450, help="cap per section per page")
    a = ap.parse_args()
    pages = load()

    if a.list:
        c = Counter(p.metadata.get("category") for p in pages.values() if p.metadata.get("doc_type") != "system")
        for cat in CATEGORIES:
            print(f"{c.get(cat,0):4}  {cat}")
        return

    if a.terms:
        terms = defaultdict(list)
        for s, p in pages.items():
            for m in re.finditer(r"^\s*[-*]\s+\*\*([^*]{2,60})\*\*\s*[—–:-]+\s*(.+)$", p.content, flags=re.M):
                terms[m.group(1).strip()].append((s, m.group(2).strip()[:220]))
        for t in sorted(terms, key=str.lower):
            for s, d in terms[t][:2]:
                print(f"**{t}** — {d}  [[{s}]]")
        return

    if a.tag:
        rx = re.compile(a.tag, re.I)
        for s, p in pages.items():
            m = p.metadata
            hay = " ".join([m.get("title", ""), m.get("one_liner", ""), " ".join(m.get("tags", [])), p.content[:3000]])
            if rx.search(hay):
                print(f"[[{s}]] | {m.get('title')} | {m.get('author')} | {m.get('category')} | tier {m.get('tier')} | {m.get('one_liner')}")
        return

    want = [x.strip() for x in a.sections.split(",")]
    cat = a.category
    items = [(s, p) for s, p in pages.items() if p.metadata.get("category") == cat]
    items.sort(key=lambda x: (x[1].metadata.get("tier") != "A", x[1].metadata.get("doc_type") == "system", x[0]))
    print(f"# {cat}: {len(items)} pages\n")
    for s, p in items:
        m = p.metadata
        print(f"\n=== [[{s}]] — {m.get('title')} ({m.get('author')}, {m.get('year')}) · tier {m.get('tier')} · {m.get('doc_type')} · {m.get('difficulty')}")
        print(f"one_liner: {m.get('one_liner')}")
        print(f"tags: {', '.join(m.get('tags', []))}")
        secs = sections(p.content)
        for w in want:
            for name, body in secs.items():
                if name.lower().startswith(w.lower()):
                    words = body.split()
                    txt = " ".join(words[: a.max_words]) + (" …" if len(words) > a.max_words else "")
                    print(f"-- {name}:\n{txt}")


if __name__ == "__main__":
    main()
