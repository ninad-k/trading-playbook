# Trading Playbook

**700+ trading books, distilled and indexed.**

Structured study notes from a library of 733 trading and finance PDFs (forex, technical analysis, candlesticks, Elliott/Gann/Fibonacci, day and swing trading, mechanical systems, money management, psychology, options and derivatives, market microstructure research, and investing classics). Every readable document gets a page; major books get deep notes with system sub-pages; 14 topic pages synthesize what the books agree and disagree on; a static site with full-text search ties it together.

> Educational summaries only. Nothing here is financial advice. The notes paraphrase ideas and rules; they do not reproduce the books. Buy the ones you find useful.

## Layout

| Path | What |
|---|---|
| `content/books/<slug>.md` | One markdown page per document (frontmatter + sections). `doc_type: system` pages are sub-pages of a book (`parent:`). |
| `content/topics/<topic>.md` | 14 topic syntheses + glossary |
| `content/paths.md` | Reading paths (beginner / intermediate / advanced / by goal) |
| `data/manifest.json` | Every source file: name, size, pages, text density, tier, duplicate-of, exclusion reason |
| `data/tiers.json` | Tier decisions with reasons |
| `docs/` | Generated static site (GitHub Pages source) |
| `export/medium/` | Generated Medium-ready markdown |
| `scripts/` | Pipeline (numbered in run order) |
| `downloads/` | Raw PDFs and extracted text (git-ignored) |

## Tiers

- **A** — major books: deep notes (overview, thesis, key concepts, rules and setups, risk, psychology, chapter map, caveats, who should read it, related) plus one sub-page per self-contained system.
- **B** — everything else readable: concise page (summary, key points, actionable rules, caveats, who it is for).
- **C** — no page: duplicates, off-topic titles, scanned PDFs without a text layer, corrupt files. Listed in the Index under "Excluded files".

## Build

```bash
python -m venv .venv && .venv/Scripts/pip install -r requirements.txt   # Windows
python scripts/01_fetch.py          # download PDFs (resumable)
python scripts/02_extract.py        # pdfinfo + pdftotext (needs poppler/xpdf on PATH)
python scripts/03_triage.py         # dedupe, flag unreadable, propose tiers -> data/review_sheet.json
python scripts/03_triage.py --apply data/tiers.json   # after review
python scripts/04_chunk.py <slug>   # what the note-writing agents read
python scripts/05_validate.py       # schema + reconciliation
python scripts/06_build_site.py     # -> docs/
python scripts/07_export_medium.py  # -> export/medium/
```

Open `docs/index.html` locally, or serve `docs/`.

## Publish

**GitHub Pages (one-time):** repo *Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `main`, folder `/docs` → Save*. The site appears at `https://ninad-k.github.io/trading-playbook/` within a minute or two of every push.

**Medium:** files in `export/medium/` are ready to paste into a new story (Medium's write API no longer issues tokens). Alternatively use *Medium → Write → Import a story* with the GitHub Pages URL of any page; Medium imports it and sets the canonical link back to the site.

**Notion:** the same content is mirrored as a "Trading Playbook" page tree (Books database + Topics + Index) via the Notion MCP connector; `data/notion_ids.json` maps slugs to Notion page IDs so reruns update instead of duplicating.

## Content rules

- Paraphrase only. No verbatim passages, no chapter reproduction, no quote collections.
- No PDFs are hosted and the public site never links to the source mirror.
- Concrete beats vague: where a book gives numbers (lookbacks, stop distances, risk per trade), the notes keep them.
- Dated material is flagged in *Caveats*.

## License

Code: GPL-3.0 (see `LICENSE`). Notes: CC BY-NC-SA 4.0.
