"""Give an agent a readable slice of a document's extracted text.

Usage:
  python scripts/04_chunk.py <slug>                 # overview: stats + TOC guess + first pages + N windows
  python scripts/04_chunk.py <slug> --windows 16    # more evenly spaced windows
  python scripts/04_chunk.py <slug> --pages 40-55   # exact page range (1-based, inclusive)
  python scripts/04_chunk.py <slug> --full          # whole text (only for short docs; capped at --max-words)
  python scripts/04_chunk.py <slug> --grep "kelly|fixed fractional"   # lines matching regex with page numbers

Pages are delimited by form-feed characters emitted by pdftotext.
"""
from __future__ import annotations

import argparse
import re
import sys

from common import TXT_DIR, load_manifest

TOC_PAT = re.compile(r"^\s*(contents|table of contents)\s*$", re.I)
CHAPTER_PAT = re.compile(r"^\s*(chapter|part|section|lesson)\s+[\divxlc]+\b.*$|^\s*\d{1,2}\s{2,}[A-Z][^.]{4,80}$", re.I | re.M)


def pages_of(slug: str) -> list[str]:
    p = TXT_DIR / f"{slug}.txt"
    if not p.exists():
        sys.exit(f"no text for {slug} (expected {p})")
    return p.read_text(encoding="utf-8", errors="replace").split("\f")


def words(s: str) -> int:
    return len(s.split())


def clean(page: str) -> str:
    # collapse runs of spaces from -layout, drop blank-line runs
    page = re.sub(r"[ \t]{3,}", "  ", page)
    page = re.sub(r"\n{3,}", "\n\n", page)
    return page.strip()


def emit(label: str, body: str) -> None:
    print(f"\n===== {label} =====")
    print(body)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--windows", type=int, default=12)
    ap.add_argument("--window-words", type=int, default=1800)
    ap.add_argument("--intro-pages", type=int, default=6)
    ap.add_argument("--pages")
    ap.add_argument("--full", action="store_true")
    ap.add_argument("--max-words", type=int, default=18000)
    ap.add_argument("--grep")
    a = ap.parse_args()

    pages = pages_of(a.slug)
    row = next((r for r in load_manifest() if r["slug"] == a.slug), {})
    total_words = sum(words(p) for p in pages)
    print(f"# {row.get('filename', a.slug)} | pages={len(pages)} | words={total_words} | pdf_title={row.get('pdf_title','')!r} | pdf_author={row.get('pdf_author','')!r}")

    if a.grep:
        rx = re.compile(a.grep, re.I)
        n = 0
        for i, p in enumerate(pages, 1):
            for line in p.splitlines():
                if rx.search(line):
                    print(f"p{i}: {line.strip()[:200]}")
                    n += 1
                    if n >= 150:
                        print("... (truncated)")
                        return
        return

    if a.pages:
        lo, hi = a.pages.split("-") if "-" in a.pages else (a.pages, a.pages)
        lo, hi = max(1, int(lo)), min(len(pages), int(hi))
        for i in range(lo, hi + 1):
            emit(f"page {i}", clean(pages[i - 1]))
        return

    if a.full:
        budget = a.max_words
        for i, p in enumerate(pages, 1):
            c = clean(p)
            if not c:
                continue
            emit(f"page {i}", c)
            budget -= words(c)
            if budget <= 0:
                print(f"\n[capped at {a.max_words} words; use --pages for more]")
                return
        return

    # overview mode
    toc_idx = [i for i, p in enumerate(pages[:40]) if any(TOC_PAT.match(l) for l in p.splitlines())]
    if toc_idx:
        i = toc_idx[0]
        emit(f"TOC (pages {i+1}-{min(i+4, len(pages))})", "\n".join(clean(p) for p in pages[i:i + 4]))
    else:
        heads = []
        for i, p in enumerate(pages, 1):
            for m in CHAPTER_PAT.finditer(p):
                heads.append(f"p{i}: {m.group(0).strip()[:100]}")
        if heads:
            emit("chapter-like headings (heuristic)", "\n".join(heads[:80]))

    emit(f"intro pages 1-{a.intro_pages}", "\n".join(clean(p) for p in pages[:a.intro_pages]))

    # evenly spaced windows over the remaining pages
    start = a.intro_pages
    span = max(len(pages) - start, 1)
    n = max(1, min(a.windows, span))
    for k in range(n):
        i = start + int(k * span / n)
        buf, j = [], i
        while j < len(pages) and words(" ".join(buf)) < a.window_words:
            buf.append(clean(pages[j]))
            j += 1
        emit(f"window {k+1}/{n}: pages {i+1}-{j}", "\n".join(buf))


if __name__ == "__main__":
    main()
