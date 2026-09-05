# Brief for note-writing agents

You are writing study notes for the Trading Playbook site. Repo root: `D:\Projects\trading-playbook`. Python: `.venv/Scripts/python`. Read documents ONLY through `scripts/04_chunk.py` (never open PDFs). Write ONLY the files you are assigned under `content/books/`.

## How to read a document

```
.venv/Scripts/python scripts/04_chunk.py <slug>                    # overview: stats, TOC, intro, 12 spaced windows
.venv/Scripts/python scripts/04_chunk.py <slug> --windows 20       # more coverage for long books
.venv/Scripts/python scripts/04_chunk.py <slug> --pages 40-55      # exact pages (1-based)
.venv/Scripts/python scripts/04_chunk.py <slug> --full             # short docs (< ~60 pages): read everything (capped 18k words)
.venv/Scripts/python scripts/04_chunk.py <slug> --grep "stop|risk per trade|position siz"   # find the numbers
```

For Tier A: overview first, then target chapters that carry the rules (use `--grep` for "rule", "entry", "exit", "stop", "%", "risk"), then read 2–4 page ranges in full. Budget about 40–60k tokens of reading per book. For Tier B: `--full` when under ~60 pages, otherwise overview + one or two ranges.

## Output file: `content/books/<slug>.md`

Frontmatter (all keys required; YAML; quote strings with colons):

```yaml
---
title: Trading for a Living            # proper title, not the filename
author: Alexander Elder                 # "Unknown" if truly unknown; "Various" for anthologies
year: 1993                              # integer or unknown
slug: trading-for-a-living              # MUST equal the assigned slug / filename
tier: A                                 # as assigned
category: Trading Psychology & Discipline   # exactly one from the list below
tags: [psychology, indicators, money-management, triple-screen]   # 3–8 lowercase kebab tags
difficulty: intermediate                # beginner | intermediate | advanced
doc_type: book                          # book | course | article | paper | manual | system
pages: 289                              # from the chunk header
one_liner: "Three pillars: psychology, method, money management; introduces the Triple Screen system."   # <= 160 chars, specific
related: [come-into-my-trading-room, trading-in-the-zone]   # 0–5 slugs from the provided slug list only
source_file: "Elder Alexander - Trading For A Living.pdf"   # exact filename from the assignment
---
```

Categories (copy exactly): `Market Structure & Price Action` · `Candlesticks & Chart Patterns` · `Indicators` · `Fibonacci, Gann & Elliott Wave` · `Trend Following & Mechanical Systems` · `Day Trading & Scalping` · `Swing Trading` · `Forex Mechanics & Macro Drivers` · `Options, Futures & Derivatives` · `Money Management & Position Sizing` · `Trading Psychology & Discipline` · `Quant, Microstructure & Academic Research` · `Investing, Value & Market History`

### Tier A body (900–1500 words). Use these exact `##` headings in this order:

```
## Overview
## Core thesis
## Key concepts
## Rules and setups
## Risk and money management
## Psychology and discipline
## Chapter map
## Strengths and caveats
## Who should read it
## Related books in this library
```

- **Key concepts**: a bullet list `**Term** — one or two line definition`. 6–15 terms.
- **Rules and setups**: numbered, concrete. Entry, exit, stop, sizing, timeframe, filters, with the book's actual numbers (e.g. "13-day EMA", "2% of equity", "close below the 20-day low"). If the book has none, say so in one line.
- **Chapter map**: `Ch N — title — one line on what it covers`. Parts/sections if no chapters. Keep it to 5–25 lines; group chapters if there are more than 25.
- **Strengths and caveats**: dated content (pit trading, commissions, pre-decimal), curve-fit or unproven claims, contradictions with other well-known authors.
- **Related books in this library**: 2–5 bullets `[[slug]] — why`. Only slugs from the provided list.

### System sub-pages (Tier A only, when the book contains a distinct, self-contained tradable method)

File `content/books/<slug>--<system-kebab>.md`, `doc_type: system`, add `parent: <slug>`, `tier` same as parent, `source_file` same as parent, `pages` same as parent. Headings, exactly:

```
## What it is
## Rules
## Risk
## Caveats
```

Rules must be complete enough that a reader could code them. 250–600 words. Examples: Triple Screen, Turtle system, Ross Hook, Bollinger Squeeze, 2-period RSI, Market Profile, LSS 3-day cycle, Camarilla pivots. Do not create system pages for generic advice.

### Tier B body (250–450 words), headings exactly:

```
## Summary
## Key points
## Actionable rules
## Caveats
## Who it is for
```

Key points: 5–10 bullets. Actionable rules: numbered, with the document's numbers; "None given" if none. For academic papers: Summary = question + data + method + finding; Key points = results; Actionable rules = what a trader can take from it.

## Writing rules

1. Paraphrase only. Never copy sentences or passages. No quotes section. At most one short quoted phrase (under 12 words) per page if it is a named rule.
2. Concise and concrete. No filler ("this fascinating book…"), no restating the heading, no marketing language.
3. Keep the book's numbers. Prefer tables for parameter sets.
4. Do not invent. If the text is partial or unclear, say what is missing in Caveats.
5. Never mention the source URL, mirror, or download. Never reference the PDF filename in the body.
6. Use `[[slug]]` for cross-references (only slugs from the provided list).
7. If a document is actually a duplicate, off-topic, or unreadable, do NOT write a page; report it in your final message with the reason.
8. After writing your files run `.venv/Scripts/python scripts/05_validate.py` and fix any error mentioning your slugs (ignore errors about other slugs).

Final message: a table `slug | title | category | doc_type | words | system pages created | problems`.
