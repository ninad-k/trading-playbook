# Manual Trader — build plan

Four pieces of work, in dependency order. Stage 0 is mine (scaffolding must exist before anything is
written into it); stages 1–3 are split across Sonnet 5 agents working on separate files.

---

## The seven new sources

All seven extract as clean text. No OCR needed.

| Book | Pages | Text | What it carries |
|---|---:|---:|---|
| The Institutional Order Flow & AMT Playbook | 235 | 724k | Microstructure, auction market theory, TPO, volume profile, footprint/delta, VWAP, DOM, algo detection, inventory & internals. Ten chapters, each with a summary checklist. |
| Charts Don't Lie | 48 | 65k | Beginner's route through candlesticks, chart patterns and discipline. 55 patterns. |
| IQ Trader — The Ultimate Trading Playbook | 75 | 44k | Charts, patterns, indicators. |
| The Complete Trading Mastery Playbook | 62 | 45k | Chart types, Fibonacci tooling, applied workflow. |
| The Intraday Trader's Guide | 58 | 37k | 13 candle signals, 14 chart patterns, MA/MACD/RSI/ADX, intraday application. |
| IQ Trader Candlestick Book | 57 | 17k | Candlestick catalogue. |
| CandleCraft — The Advanced Candlestick Guide | 30 | 21k | Basic → reversal → continuation → complex candlesticks. |

The Institutional Order Flow book is by a distance the most substantial and is the only source in the
whole library — including the 733 existing PDFs — that covers order flow and auction market theory at
depth. It carries the advanced end of the curriculum on its own.

### One thing to settle before I put your name on anything

Four of the seven carry someone else's byline in the file itself:

- **CandleCraft** — *"PRESENT BY :- VIKAS (FOUNDER OF MERROR TRADER)"*, with "IQ TRADER" substituted
  at a second spot in the same document.
- **IQ Trader Candlestick Book**, **IQ Trader's Ultimate Trading Playbook**, **The Intraday Trader's
  Guide** — all branded "IQ Trader", and two are titled "English of…" / "English Edition", which reads
  like a translation of an existing Hindi ebook rather than an original.

**Charts Don't Lie** and **The Institutional Order Flow & AMT Playbook** carry no third-party byline and
read as original work.

I am not going to attribute another person's book to you on a public site. So, unless you tell me
otherwise, the plan below does this:

- **Concepts from all seven** feed the Manual Trader course. Techniques and facts aren't anyone's
  property, and every word of the course is newly written.
- **Author credit** — you are credited as author of the Trading Playbook itself: the library, the
  syntheses, the course. That is accurate regardless of who wrote the source ebooks.
- **The four IQ Trader / CandleCraft books** get library notes attributed to the byline printed in the
  file, not to you.
- Tell me you hold the rights to those four and I will change their attribution in one pass.

---

## Stage 0 — Scaffolding *(me, before agents start)*

1. `content/manual/NN-slug.md` — new content type, its own frontmatter schema (`stage`, `title`,
   `goal`, `builds_on`, `prereq_skills`, `practice`, `self_check`).
2. `templates/manual.html` — a lesson template with **previous / next** links and a stage rail, so the
   course reads as a sequence rather than a pile of pages. This is what makes it a course and not the
   rest of the site.
3. `docs/manual/` output, a "Manual Trader" entry at the top of the sidebar, and a course landing page.
4. Validator support in `05_validate.py`, link and build checks, search indexing.
5. Six new schematic diagrams the course needs and the library does not yet have: volume profile
   shape, VWAP with deviation bands, the footprint/delta grid, order-book depth imbalance, the
   auction-rotation cycle, and an expectancy/R-distribution chart.

## Stage 1 — The course *(three Sonnet 5 agents, separate files)*

Nine stages, written as continuous teaching prose. Each one states what you will be able to do by the
end, teaches it, works an example, gives one practice drill, and ends with a self-check that gates the
next stage. No link dumps, no "see also" lists, no "read book X" — the reading list already exists
elsewhere on the site and is deliberately not the point here.

| # | Stage | Builds the skill of |
|---|---|---|
| 1 | What a chart actually is | Reading price and time honestly; choosing a timeframe for a reason |
| 2 | The candle and the sequence | Reading one bar, then three, without pattern-matching from a catalogue |
| 3 | Structure | Swings, trend, ranges, support and resistance as inventory rather than lines |
| 4 | Patterns as structure in motion | Recognising the classical set — and knowing when each is just a range |
| 5 | Indicators, and what they actually compute | MA, RSI, MACD, ADX, Bollinger, divergence; why stacking them fails |
| 6 | The trade | Entry, stop, target, R, position size, expectancy. First stage where money is at risk |
| 7 | The session | Opening range, VWAP, gaps, session rotations, the shape of an intraday day |
| 8 | Where price comes from | Matching engine, auction market theory, volume profile, footprint, DOM |
| 9 | Your own playbook | Regime → location → trigger; journaling, review, and the discipline loop |

Stages 1–3 → agent A · 4–6 → agent B · 7–9 → agent C. Each agent owns its own files and nothing else.

Stage 8 is where the Institutional Order Flow book does its work, and stage 9 is where the course
stops teaching setups and starts teaching the process that decides which setups you keep.

## Stage 2 — Library notes for the seven books *(one Sonnet 5 agent)*

Seven notes in the existing house format, with real page-level source coverage — the same standard the
other 582 are held to. Categories: Candlesticks & Chart Patterns (3), Day Trading & Scalping (2),
Quant/Microstructure (1, the Institutional book), Market Structure (1). The Institutional book warrants
Tier A with method sub-pages for volume profile, footprint and VWAP.

## Stage 3 — Attribution, and cleaning the sources *(me)*

1. **Author.** "Ninad K" as author of the Trading Playbook, on every page footer and in the metadata,
   with the About page rewritten to explain the idea in your voice: why a library of 733 trading books
   read end to end is worth more than any one of them, and what the course is for.
2. **Strip the source filenames.** Raw PDF filenames are currently visible on **52 pages** — things
   like `241FOREX_2.pdf`, `(Ebooks) Finance- Mba In Finance.pdf`, `.pdf - Linked File.pdf`. They look
   like a warez folder listing and they tell a reader nothing. Every one is replaced with the clean
   book title. There are no external download links anywhere in the notes — I checked; that part is
   already clean.

---

## Verification

Validator, full rebuild, link check across all pages, and a read-through of the course as a first-time
visitor would take it — stage 1 to stage 9, following only the next links, confirming each stage stands
on what came before and nothing forward-references.
