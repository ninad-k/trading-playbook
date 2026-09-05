# Brief for topic-synthesis agents

You are writing one topic page for the Trading Playbook: a synthesis across all book notes in one category. Repo root `D:\Projects\trading-playbook`, Python `.venv/Scripts/python`. Read ONLY the book notes (never the PDFs); the digest script gives you what you need.

## Inputs

```
.venv/Scripts/python scripts/09_topic_digest.py "<Category name>"                 # every page in the category: frontmatter + key sections
.venv/Scripts/python scripts/09_topic_digest.py "<Category>" --max-words 900     # longer excerpts for the important pages
.venv/Scripts/python scripts/09_topic_digest.py --tag "kelly|optimal f"          # find pages in OTHER categories that touch your topic
```

Read a specific page in full when needed: `content/books/<slug>.md`.

## Output: `content/topics/<topic-slug>.md`

Topic slug = category name lower-cased, non-alphanumerics → `-` (e.g. `money-management-position-sizing`, `fibonacci-gann-elliott-wave`, `quant-microstructure-academic-research`).

Frontmatter:
```yaml
---
title: Money Management & Position Sizing
summary: "One sentence: what this topic is and what the library says about it."   # <= 200 chars
books_covered: 41            # number of pages in the category you drew on
---
```

Headings, exactly and in this order:
```
## What it is
## Core principles
## Concrete rules and setups
## Common mistakes
## Best books for this topic
## Open debates
```

- **What it is** (80–150 words): define the topic for a reader who trades but has not studied it.
- **Core principles** (8–15 bullets): the ideas most books agree on. Each bullet ends with citations `[[slug]]` to the 1–4 pages that support it. Prefer principles that are specific, not platitudes.
- **Concrete rules and setups** (numbered, 10–25 items): the actual parameters, formulas, thresholds and setups the books give, one per item, each with its `[[slug]]`. Group by sub-theme with `###` headings if there are more than 12. Where two books give different numbers for the same thing, show both.
- **Common mistakes** (5–10 bullets): errors the books warn about, with `[[slug]]`.
- **Best books for this topic** (ranked list of 5–10): `1. [[slug]] — why, and for whom` — Tier A first unless a Tier B page is clearly better for the purpose.
- **Open debates** (3–8 bullets): where authors disagree (e.g. optimal f vs fixed fractional; indicators vs price action; scaling out vs all-out), stating each side with `[[slug]]`s.

Length 1 200–2 200 words. Paraphrase only. Every `[[slug]]` must be a real filename stem in `content/books/`. Do not invent numbers: if a rule's number is not in the notes, describe it qualitatively. No source URLs or filenames.

When done run `.venv/Scripts/python scripts/05_validate.py` and fix any error mentioning `topics/<your file>` (ignore other errors). Final message: word count, number of distinct pages cited, and any category-level gaps you noticed (books that should exist in this category but are filed elsewhere).
