"""Shared helpers for the trading-playbook pipeline."""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DOWNLOADS = ROOT / "downloads"
PDF_DIR = DOWNLOADS / "pdf"
TXT_DIR = DOWNLOADS / "txt"
CONTENT = ROOT / "content"
BOOKS = CONTENT / "books"
TOPICS = CONTENT / "topics"
DOCS = ROOT / "docs"
MANIFEST = DATA / "manifest.json"

BASE_URL = "https://dl.fxf1.com/files/books/english/"

CATEGORIES = [
    "Market Structure & Price Action",
    "Candlesticks & Chart Patterns",
    "Indicators",
    "Fibonacci, Gann & Elliott Wave",
    "Trend Following & Mechanical Systems",
    "Day Trading & Scalping",
    "Swing Trading",
    "Forex Mechanics & Macro Drivers",
    "Options, Futures & Derivatives",
    "Money Management & Position Sizing",
    "Trading Psychology & Discipline",
    "Quant, Microstructure & Academic Research",
    "Investing, Value & Market History",
    "Glossary",
]

_STOP_PREFIXES = re.compile(
    r"^(\(?e?books?\)?|\(?trading\)?|\[.*?\]|mcgraw[- .]hill|john wiley( sons)?|wiley)[\s\-.,:]*",
    re.I,
)


def slugify(name: str) -> str:
    """Filename -> stable ascii slug (no extension)."""
    stem = re.sub(r"\.(pdf)$", "", name, flags=re.I)
    stem = unicodedata.normalize("NFKD", stem).encode("ascii", "ignore").decode()
    stem = re.sub(r"[^A-Za-z0-9]+", "-", stem).strip("-").lower()
    stem = re.sub(r"-{2,}", "-", stem)
    return stem[:90].strip("-") or "file"


def normalized_title(name: str) -> str:
    """Loose title key for duplicate detection."""
    stem = re.sub(r"\.(pdf)$", "", name, flags=re.I)
    stem = re.sub(r"_\d$", "", stem)  # trailing _2
    stem = re.sub(r"\(\d+\)$", "", stem)
    stem = _STOP_PREFIXES.sub("", stem)
    stem = unicodedata.normalize("NFKD", stem).encode("ascii", "ignore").decode().lower()
    stem = re.sub(r"[^a-z0-9]+", " ", stem)
    words = [w for w in stem.split() if w not in {"the", "a", "an", "of", "and", "by", "for", "to", "in", "ebook", "pdf"}]
    return " ".join(words)


def load_manifest() -> list[dict]:
    if MANIFEST.exists():
        return json.loads(MANIFEST.read_text(encoding="utf-8"))
    return []


def save_manifest(rows: list[dict]) -> None:
    DATA.mkdir(exist_ok=True)
    rows = sorted(rows, key=lambda r: r["filename"].lower())
    MANIFEST.write_text(json.dumps(rows, indent=1, ensure_ascii=False), encoding="utf-8")
