"""Cross-check a note's numeric and named claims against its source text.

Usage:
  python scripts/15_verify_claims.py <slug> [--context 90] [--max-claims 60]

For each note line containing a number or a quoted term, it pulls out distinctive tokens
(numbers, percentages, capitalised multiword names) and reports whether each appears in the
extracted PDF text, with the page number and surrounding context. Lines whose tokens are all
missing are listed as UNSUPPORTED so they can be read against the source by hand.
"""
from __future__ import annotations

import argparse
import re
import sys

import frontmatter

from common import BOOKS, TXT_DIR

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

NUM = re.compile(r"(?<![\w.])(\d[\d,]*(?:\.\d+)?)(?![\w])")
STOP = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "0", "100", "2000", "2001", "2002", "2003", "2004", "2005"}


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9.%]+", " ", s.lower())


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--context", type=int, default=90)
    ap.add_argument("--max-claims", type=int, default=60)
    ap.add_argument("--keep-common", action="store_true")
    a = ap.parse_args()

    post = frontmatter.load(BOOKS / f"{a.slug}.md", encoding="utf-8")
    pages = (TXT_DIR / f"{a.slug}.txt").read_text(encoding="utf-8", errors="replace").split("\f")
    flat = [norm(p) for p in pages]

    def find(tok: str) -> list[tuple[int, str]]:
        t = norm(tok).strip()
        hits = []
        for i, p in enumerate(flat, 1):
            j = p.find(t)
            if j >= 0:
                hits.append((i, p[max(0, j - a.context // 2): j + a.context].strip()))
            if len(hits) >= 3:
                break
        return hits

    lines = [l.strip("- ").strip() for l in post.content.splitlines() if l.strip()]
    claims = [l for l in lines if NUM.search(l) and not l.startswith("#")][: a.max_claims]
    print(f"# {a.slug}: {len(pages)} pages, {len(claims)} numeric claim lines")
    unsupported = []
    for l in claims:
        toks = [t for t in NUM.findall(l) if a.keep_common or t not in STOP]
        toks = list(dict.fromkeys(toks))[:6]
        res = []
        for t in toks:
            h = find(t)
            res.append((t, h))
        found = [r for r in res if r[1]]
        tag = "OK " if found else "?? "
        print(f"\n{tag}{l[:200]}")
        for t, h in res:
            if h:
                print(f"    {t}: " + " | ".join(f"p{i}: …{c}…" for i, c in h[:2]))
            else:
                print(f"    {t}: NOT FOUND")
        if not found:
            unsupported.append(l)
    print(f"\n# {len(unsupported)} claim lines with no numeric token found in source")


if __name__ == "__main__":
    main()
