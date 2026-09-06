"""Duplicate detection by text overlap.

The first design compared a new book's embedding against the embeddings of existing notes.
Measured against the library, that does not work: the median similarity between two *different*
trading books is 0.85, higher than some genuine duplicates score. Every book in this collection
reads like "a trading book about charts" to a sentence embedder, so no threshold separates them.

What does work is comparing source text to source text. Each book is reduced to a sampled set of
hashed 8-word shingles; two texts are compared by Jaccard overlap and by containment. Measured
against the 106 duplicate pairs the manifest already knows about:

    same book       jaccard 0.80 - 1.00   (or containment 1.00 when one is an excerpt)
    different books jaccard 0.000

That is not a close call, which is why this is the verdict-maker and embeddings are demoted to
advisory topic-neighbour lookup.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from common import ROOT  # noqa: E402

TEXT_DIRS = [ROOT / "downloads" / "txt", ROOT / "downloads" / "txt_ninad"]
INDEX = ROOT / "downloads" / "text_index.json"

NGRAM = 8          # words per shingle
KEEP = 64          # keep 1 hash in 64: enough to estimate overlap, small enough to hold in memory
MAX_CHARS = 400_000
MIN_SHINGLES = 12  # below this the sample is too thin to judge

DUP_JACCARD = 0.30      # different books measure 0.000, so this is a wide margin
DUP_CONTAINMENT = 0.60  # catches an excerpt or a chapter lifted from a longer work

_WORD = re.compile(r"[a-z0-9]+")


def shingles(text: str) -> set[int]:
    toks = _WORD.findall(text.lower()[:MAX_CHARS])
    out = set()
    for i in range(len(toks) - NGRAM + 1):
        h = int.from_bytes(
            hashlib.blake2b(" ".join(toks[i:i + NGRAM]).encode(), digest_size=8).digest(), "big")
        if h % KEEP == 0:
            out.add(h)
    return out


def build_index(progress=lambda *_: None) -> dict:
    """Fingerprint every extracted source text once."""
    files = sorted(f for d in TEXT_DIRS if d.exists() for f in d.glob("*.txt"))
    data = {}
    for i, f in enumerate(files, 1):
        s = shingles(f.read_text(encoding="utf-8", errors="ignore"))
        if len(s) >= MIN_SHINGLES:
            data[f.stem] = sorted(s)
        if i % 50 == 0 or i == len(files):
            progress(i, len(files))
    INDEX.parent.mkdir(parents=True, exist_ok=True)
    INDEX.write_text(json.dumps(data), encoding="utf-8")
    return {"texts": len(data), "of": len(files),
            "mb": round(INDEX.stat().st_size / 1e6, 1)}


_cache: dict | None = None


def load_index() -> dict[str, set[int]]:
    global _cache
    if _cache is None:
        if not INDEX.exists():
            _cache = {}
        else:
            _cache = {k: set(v) for k, v in json.loads(INDEX.read_text(encoding="utf-8")).items()}
    return _cache


def invalidate() -> None:
    global _cache
    _cache = None


def compare(candidate: set[int], index: dict[str, set[int]]) -> list[dict]:
    """Every existing text this candidate meaningfully overlaps, strongest first."""
    hits = []
    if len(candidate) < MIN_SHINGLES:
        return hits
    for slug, other in index.items():
        inter = len(candidate & other)
        if not inter:
            continue
        union = len(candidate | other)
        jac = inter / union if union else 0.0
        cont = inter / min(len(candidate), len(other))
        if jac >= DUP_JACCARD or cont >= DUP_CONTAINMENT:
            hits.append({"slug": slug, "jaccard": round(jac, 3), "containment": round(cont, 3),
                         "shared": inter})
    hits.sort(key=lambda h: (-h["containment"], -h["jaccard"]))
    return hits


def describe(hit: dict, title: str) -> str:
    if hit["jaccard"] >= 0.85:
        return f"The same text as {title} (word-for-word overlap {hit['jaccard']:.0%})."
    if hit["containment"] >= 0.85:
        return (f"This text is almost entirely contained in {title} — an excerpt, a chapter, or a "
                f"shorter edition of it ({hit['containment']:.0%} of it appears there).")
    return (f"Substantial verbatim overlap with {title}: {hit['jaccard']:.0%} of the combined text "
            f"is shared.")
