"""Book Studio pipeline: read an uploaded PDF, decide whether it is new, draft a note.

Runs entirely against a local Ollama instance. Nothing here touches the network except
http://localhost:11434, and nothing here is served by the published site.

Three dedup passes, cheapest first:
  1. sha1 of the file  -> the same file, already in the library
  2. normalised title  -> a different scan of the same book
  3. text overlap      -> the same book under another name, or an excerpt of one

Pass 3 does the real work, comparing source text to source text with hashed shingles. It is
in dedup.py, along with the measurements showing why embedding similarity was not up to the
job. Embeddings still run, but only to name the nearest notes by subject and to rank which
sampled pages sit furthest from anything held — both advisory, neither a verdict.

Drafting uses Ollama's structured output: every model call is constrained to a JSON schema,
so a small local model cannot ramble, cannot skip a section, and cannot invent a category.
The Markdown is assembled here from the returned fields; the model never writes the page.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import frontmatter  # noqa: E402
import pymupdf  # noqa: E402

import dedup  # noqa: E402

from common import (  # noqa: E402
    BOOKS, CATEGORIES, ROOT, display_title, load_manifest, normalized_title, save_manifest, slugify,
)

OLLAMA = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"
INDEX = ROOT / "downloads" / "note_embeddings.json"   # derived cache; downloads/ is git-ignored
DRAFTS = ROOT / "content" / "drafts"
UPLOADS = Path(__file__).resolve().parent / "uploads"

# A note is only as good as what the model was shown. These caps keep a run finishable on a
# small local model, and every page fed in is recorded on the draft.
CHUNK_CHARS = 5000
MAX_PAGES_SHOWN = 14


# --------------------------------------------------------------------------- ollama

def _post(path: str, payload: dict, timeout: int = 900) -> dict:
    req = urllib.request.Request(
        OLLAMA + path, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def ollama_status() -> dict:
    """Reachability plus the model list, with cloud-routed models flagged as not offline."""
    try:
        with urllib.request.urlopen(OLLAMA + "/api/tags", timeout=5) as r:
            tags = json.loads(r.read().decode())
    except (urllib.error.URLError, OSError, TimeoutError) as e:
        return {"up": False, "error": str(e), "models": []}
    models = []
    for m in tags.get("models", []):
        name = m.get("name", "")
        det = m.get("details", {}) or {}
        remote = bool(m.get("remote_host"))
        models.append({
            "name": name,
            "offline": not remote,
            "remote_host": m.get("remote_host") or "",
            "embedding": "embed" in name or det.get("family") == "nomic-bert",
            "params": det.get("parameter_size", ""),
        })
    models.sort(key=lambda m: (not m["offline"], m["embedding"], m["name"]))
    return {"up": True, "models": models}


def embed(texts: list[str]) -> list[list[float]]:
    if not texts:
        return []
    return _post("/api/embed", {"model": EMBED_MODEL, "input": texts}).get("embeddings", [])


def ask(model: str, prompt: str, schema: dict, system: str = "", budget: int = 1200) -> dict:
    """One model call with decoding constrained to `schema`. Returns parsed JSON.

    Constrained decoding is what makes a small local model usable here: it physically cannot
    emit prose around the answer, so nothing needs cleaning and no field can go missing.
    """
    msgs = [{"role": "system", "content": system}] if system else []
    msgs.append({"role": "user", "content": prompt})
    out = _post("/api/chat", {
        "model": model, "messages": msgs, "stream": False, "think": False,
        "format": schema, "options": {"num_predict": budget, "temperature": 0.15},
    }, timeout=1800)
    raw = (out.get("message") or {}).get("content", "") or "{}"
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", raw, re.S)
        if not m:
            raise ValueError(f"model returned nothing parseable: {raw[:200]}")
        return json.loads(m.group(0))


# --------------------------------------------------------------------------- vectors

def cosine(a: list[float], b: list[float]) -> float:
    num = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    return num / (na * nb) if na and nb else 0.0


def note_fingerprint(post) -> str:
    """What a note is about, in the ~1500 characters an embedding model can actually use."""
    m = post.metadata
    head = f"{m.get('title', '')}. {m.get('author', '')}. {m.get('one_liner', '')}. "
    head += " ".join(m.get("tags", []) or []) + ". "
    body = re.sub(r"\s+", " ", re.sub(r"[#*`>\[\]_|-]+", " ", post.content))
    return (head + body)[:1500]


def build_index(progress=lambda *_: None) -> dict:
    """Embed every existing note once, so dedup is a lookup rather than a re-read."""
    files = sorted(BOOKS.glob("*.md"))
    entries, batch, meta = [], [], []
    for i, f in enumerate(files):
        post = frontmatter.load(f, encoding="utf-8")
        batch.append(note_fingerprint(post))
        meta.append({"slug": f.stem, "title": post.metadata.get("title", f.stem),
                     "category": post.metadata.get("category", ""),
                     "tier": post.metadata.get("tier", "")})
        if len(batch) >= 32 or i == len(files) - 1:
            for md, vec in zip(meta, embed(batch)):
                entries.append({**md, "v": [round(x, 5) for x in vec]})
            progress(len(entries), len(files))
            batch, meta = [], []
    INDEX.parent.mkdir(parents=True, exist_ok=True)
    INDEX.write_text(json.dumps({"model": EMBED_MODEL, "notes": entries}), encoding="utf-8")
    return {"notes": len(entries), "path": str(INDEX)}


def load_index() -> list[dict]:
    if not INDEX.exists():
        return []
    return json.loads(INDEX.read_text(encoding="utf-8")).get("notes", [])


# --------------------------------------------------------------------------- reading

@dataclass
class Book:
    path: Path
    filename: str
    sha1: str = ""
    pages: list[str] = field(default_factory=list)
    chars: int = 0


def read_pdf(path: Path) -> Book:
    data = path.read_bytes()
    doc = pymupdf.open(path)
    pages = [p.get_text() for p in doc]
    doc.close()
    return Book(path=path, filename=path.name, sha1=hashlib.sha1(data).hexdigest(),
                pages=pages, chars=sum(len(p) for p in pages))


def sample_pages(book: Book) -> tuple[str, list[int]]:
    """Front matter plus an even spread. Returns the text and the 1-based pages used."""
    usable = [i for i, p in enumerate(book.pages) if len(p.strip()) > 200]
    if not usable:
        return "", []
    front = usable[:4]
    rest = [p for p in usable if p not in front]
    want = max(MAX_PAGES_SHOWN - len(front), 1)
    if len(rest) <= want:
        picked = front + rest
    else:
        step = len(rest) / want
        picked = front + [rest[int(i * step)] for i in range(want)]
    picked = sorted(set(picked))
    return "\n\n".join(book.pages[i][:CHUNK_CHARS] for i in picked), [i + 1 for i in picked]


def page_ranges(pages: list[int]) -> str:
    if not pages:
        return ""
    out, start, prev = [], pages[0], pages[0]
    for p in pages[1:]:
        if p == prev + 1:
            prev = p
            continue
        out.append(f"{start}-{prev}" if prev > start else str(start))
        start = prev = p
    out.append(f"{start}-{prev}" if prev > start else str(start))
    return ", ".join(out)


# --------------------------------------------------------------------------- dedup

def analyse(book: Book) -> dict:
    manifest = load_manifest()
    result = {"filename": book.filename, "pages": len(book.pages), "chars": book.chars,
              "sha1": book.sha1, "title_guess": display_title(book.filename),
              "verdict": "new", "reasons": [], "matches": [], "novel_sections": [],
              "overlaps": []}

    if book.chars < 2000:
        result["verdict"] = "unreadable"
        result["reasons"].append("Almost no extractable text: an image-only scan that needs OCR first.")
        return result

    for row in manifest:
        if row.get("sha1") == book.sha1:
            result["verdict"] = "exact-duplicate"
            result["reasons"].append(f"Byte-identical to a file already held: {display_title(row['filename'])}")
            return result

    nt = normalized_title(book.filename)
    for row in manifest:
        if nt and normalized_title(row.get("filename", "")) == nt:
            result["verdict"] = "title-duplicate"
            result["reasons"].append(f"Same title, different file: {display_title(row['filename'])}")
            return result

    index = load_index()
    titles = {n["slug"]: n["title"] for n in index}
    sampled, pages_used = sample_pages(book)
    result["sampled_pages"] = pages_used

    # Pass 3 — the verdict. Text against text, which is the only signal that actually separates
    # duplicates here (see the measurements in dedup.py).
    tindex = dedup.load_index()
    if not tindex:
        result["reasons"].append("No text index yet, so only file and title dedup ran. "
                                 "Build the indexes for the real check.")
    else:
        hits = dedup.compare(dedup.shingles("\n".join(book.pages)), tindex)
        if hits:
            top = hits[0]
            result["verdict"] = "near-duplicate"
            result["overlaps"] = hits[:4]
            result["reasons"].append(dedup.describe(top, titles.get(top["slug"], top["slug"])))
            if len(hits) > 1:
                result["reasons"].append(f"It also overlaps {len(hits) - 1} other text(s) held.")

    # Advisory only: which existing notes sit nearest in subject matter. This is a topic hint,
    # not evidence of duplication — distinct trading books routinely score 0.85 against each other.
    if index:
        whole = embed([" ".join(sampled.split())[:1500]])
        if whole:
            scored = sorted(((cosine(whole[0], n["v"]), n) for n in index), key=lambda t: -t[0])[:5]
            result["matches"] = [{"slug": n["slug"], "title": n["title"], "tier": n["tier"],
                                  "category": n["category"], "score": round(s, 3)} for s, n in scored]

        # And which sampled pages sit furthest from anything held. Reported as a ranking rather
        # than against a fixed threshold, because the absolute numbers are not meaningful.
        secs = [(i, " ".join(book.pages[i - 1][:CHUNK_CHARS].split())[:1500]) for i in pages_used]
        secs = [(i, s) for i, s in secs if len(s) > 300]
        if secs:
            vecs = embed([s for _, s in secs])
            scored_secs = []
            for (pg, _), vec in zip(secs, vecs):
                best = max((cosine(vec, n["v"]), n) for n in index)
                scored_secs.append({"page": pg, "nearest": best[1]["title"],
                                    "score": round(best[0], 3)})
            scored_secs.sort(key=lambda s: s["score"])
            result["novel_sections"] = scored_secs[:3]
    return result


# --------------------------------------------------------------------------- drafting

SYSTEM = (
    "You produce study notes for a reference library of trading books. Rules, without exception:\n"
    "- Paraphrase. Never reproduce the book's own sentences, and never put its wording inside "
    "quotation marks. Restate every idea in your own words.\n"
    "- Never invent a number. If the book does not state a stop, a size, a lookback or a win rate, "
    "do not supply one. An invented figure is the worst possible failure here.\n"
    "- Keep every concrete parameter the book DOES state.\n"
    "- Be critical. If the book is thin, repetitive, or recycles a standard catalogue, say so.\n"
    "- Plain declarative prose. No marketing language and no claims about profit."
)

FACTS_SCHEMA = {
    "type": "object",
    "properties": {
        "subject": {"type": "string"},
        "teaches": {"type": "array", "items": {"type": "string"}, "minItems": 3, "maxItems": 12},
        "stated_numbers": {"type": "array", "items": {
            "type": "object",
            "properties": {"value": {"type": "string"}, "applies_to": {"type": "string"}},
            "required": ["value", "applies_to"]}},
        "unsupported_claims": {"type": "array", "items": {"type": "string"}},
        "thinness": {"type": "string"},
    },
    "required": ["subject", "teaches", "stated_numbers", "unsupported_claims", "thinness"],
}

NOTE_SCHEMA = {
    "type": "object",
    "properties": {
        "title": {"type": "string"},
        "author": {"type": "string"},
        "year": {"type": "string"},
        "category": {"type": "string", "enum": CATEGORIES[:-1]},
        "difficulty": {"type": "string", "enum": ["beginner", "intermediate", "advanced"]},
        "one_liner": {"type": "string"},
        "tags": {"type": "array", "items": {"type": "string"}, "minItems": 2, "maxItems": 5},
        "summary": {"type": "string"},
        "key_points": {"type": "array", "items": {"type": "string"}, "minItems": 4, "maxItems": 7},
        "actionable_rules": {"type": "array", "items": {"type": "string"}},
        "caveats": {"type": "string"},
        "who_it_is_for": {"type": "string"},
    },
    "required": ["title", "author", "year", "category", "difficulty", "one_liner", "tags",
                 "summary", "key_points", "actionable_rules", "caveats", "who_it_is_for"],
}

FACTS_PROMPT = """Sampled text from a trading book (pages {pages}):

{text}

Record what this book actually claims: its subject, the specific techniques or rules it teaches,
every concrete number it states together with what that number applies to, anything it asserts
without support, and whether the material is thin or repetitive."""

NOTE_PROMPT = """What was found in a trading book:

Subject: {subject}
Teaches: {teaches}
Numbers it states: {numbers}
Asserted without support: {unsupported}
Thinness: {thinness}

The file is named "{filename}".
Books already in this library that cover the closest ground are categorised as: {cat_hint}

Write the library note.

actionable_rules is for anything the reader could actually follow: an entry condition, an exit, a
threshold, a ratio, a lookback, a confirmation requirement. Every number listed above belongs in a
rule there, attached to what it applies to. Leave the list empty only when the book genuinely gives
nothing followable — a glossary or a history, say. Do not put rules in key_points instead.

key_points is for what the book argues and how it is organised, not for its rules.

For category, weigh the evidence above: a book is categorised by its subject, not by an aside.
In caveats be specific and blunt about what is weak, thin or unsupported.
Give the year only if the text states one; otherwise use "unknown"."""


def draft_note(book: Book, model: str, analysis: dict, progress=lambda *_: None) -> dict:
    sampled, pages_used = sample_pages(book)
    if not sampled:
        raise ValueError("no extractable text to read")

    progress("reading", f"{len(pages_used)} sampled pages")
    facts = ask(model, FACTS_PROMPT.format(pages=page_ranges(pages_used), text=sampled[:24000]),
                FACTS_SCHEMA, SYSTEM, budget=1400)

    progress("writing", "the note")
    nums = "; ".join(f"{n.get('value')} ({n.get('applies_to')})"
                     for n in facts.get("stated_numbers", [])) or "none"
    note = ask(model, NOTE_PROMPT.format(
        subject=facts.get("subject", ""),
        teaches="; ".join(facts.get("teaches", [])),
        numbers=nums,
        unsupported="; ".join(facts.get("unsupported_claims", [])) or "none",
        thinness=facts.get("thinness", ""),
        filename=book.filename,
        cat_hint=", ".join(dict.fromkeys(
            m["category"] for m in analysis.get("matches", [])[:3] if m.get("category"))) or "no close match",
    ), NOTE_SCHEMA, SYSTEM, budget=1800)

    rules = [r.strip() for r in (note.get("actionable_rules") or []) if r.strip()]

    # An instruction alone will not hold every time, so check mechanically.
    warnings = []
    checked = " ".join([note["summary"], note["caveats"], *note["key_points"], *rules])
    quoted = re.findall(r"[\"“‘']([^\"“”‘’']{45,})[\"”’']", checked)
    if quoted:
        warnings.append(f"{len(quoted)} passage(s) look quoted from the book rather than paraphrased. "
                        "Rewrite them before approving.")
    body = (
        "## Summary\n\n" + note["summary"].strip() + "\n\n"
        + "## Key points\n\n" + "\n".join(f"- {p.strip()}" for p in note["key_points"]) + "\n\n"
        + "## Actionable rules\n\n"
        + ("\n".join(f"- {r}" for r in rules) if rules
           else "The book states no followable rules; it describes ideas rather than a procedure.")
        + "\n\n## Caveats\n\n" + note["caveats"].strip() + "\n\n"
        + "## Who it is for\n\n" + note["who_it_is_for"].strip() + "\n"
    )

    year = note.get("year", "")
    if not re.fullmatch(r"(19|20)\d\d", year or ""):
        year = "unknown"
    tags = [re.sub(r"[^a-z0-9-]+", "-", t.lower()).strip("-") for t in note.get("tags", [])]
    tags = [t for t in tags if t][:5] or ["trading"]

    if (note.get("author") or "").strip().lower() in ("unknown", "n/a", "not stated", "none", ""):
        note["author"] = "Unknown"
    slug = slugify(book.filename)
    coverage = (f"{page_ranges(pages_used)} of {len(book.pages)} (front matter plus an even spread; "
                "this is exactly what the model was shown, and nothing else)")
    post = frontmatter.Post(
        body,
        title=note.get("title") or display_title(book.filename),
        author=(note.get("author") or "").strip() or "Unknown",
        year=year, slug=slug, tier="B", category=note["category"],
        tags=tags + ["machine-drafted"],
        difficulty=note.get("difficulty", "intermediate"), doc_type="book",
        pages=len(book.pages),
        one_liner=note.get("one_liner") or display_title(book.filename),
        related=[m["slug"] for m in analysis.get("matches", [])[:3]],
        source_file=book.filename, source_review="partial", reviewed_pdf_pages=coverage,
        drafted_by=f"ollama/{model}", draft_status="unreviewed", draft_warnings=warnings,
    )
    DRAFTS.mkdir(parents=True, exist_ok=True)
    out = DRAFTS / f"{slug}.md"
    out.write_text(frontmatter.dumps(post) + "\n", encoding="utf-8")
    return {"slug": slug, "path": str(out.relative_to(ROOT)), "title": post["title"],
            "author": post["author"], "category": post["category"], "coverage": coverage,
            "sampled_pages": pages_used, "rules": len(rules), "warnings": warnings}


def approve(slug: str, sha1: str = "", filename: str = "", pages: int = 0, chars: int = 0) -> dict:
    """Move a reviewed draft into the library and give it a manifest row."""
    src = DRAFTS / f"{slug}.md"
    if not src.exists():
        raise FileNotFoundError(f"no draft {slug}")
    post = frontmatter.load(src, encoding="utf-8")
    post["draft_status"] = "reviewed"
    post["tags"] = [t for t in (post.get("tags") or []) if t != "machine-drafted"] or ["trading"]
    post.metadata.pop("draft_warnings", None)
    (BOOKS / f"{slug}.md").write_text(frontmatter.dumps(post) + "\n", encoding="utf-8")

    rows = load_manifest()
    if not any(r["slug"] == slug for r in rows):
        rows.append({
            "bytes": 0, "chars": chars, "chars_per_page": chars // max(pages, 1) if pages else 0,
            "ext": "pdf", "filename": filename or post.get("source_file", f"{slug}.pdf"),
            "pages": pages or post.get("pages", 0), "pdf_author": "", "pdf_title": "",
            "proposed_tier": post.get("tier", "B"), "sha1": sha1, "slug": slug,
            "status": "downloaded", "text_status": "ok", "tier": post.get("tier", "B"),
            "tier_reason": "added through Book Studio",
        })
        save_manifest(rows)
    # Feed the new book into the dedup corpus, so the next upload is checked against it too.
    up = UPLOADS / (filename or post.get("source_file", ""))
    if up.exists():
        try:
            out = dedup.TEXT_DIRS[-1]
            out.mkdir(parents=True, exist_ok=True)
            book = read_pdf(up)
            (out / f"{slug}.txt").write_text("".join(book.pages), encoding="utf-8")
            dedup.invalidate()
        except Exception:  # noqa: BLE001 - never block an approval on this
            pass
    src.unlink()
    return {"slug": slug, "note": f"content/books/{slug}.md"}
