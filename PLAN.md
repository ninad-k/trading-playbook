# Trading Playbook: continuation plan

## Name and purpose

**Trading Playbook** — *Trading books, explained and connected.* Keep the existing name and stable slugs. The library provides original study notes, source-page references, method sub-pages, topic syntheses, and searchable static HTML. Suggested repository name: `trading-playbook`.

## Current verified state — 6 September 2026

| Item | Count |
| --- | ---: |
| Saved source PDFs | 733 |
| Main notes | 582 |
| Major / concise notes | 128 / 454 |
| Method sub-pages | 151 |
| Topic syntheses / glossary | 13 / 1 |
| Reading paths | 1 (`content/paths.md`) |
| Missing eligible notes | 0 |
| Notes with recorded source coverage | 582 of 582 |
| Full / partial source review | 228 / 354 |
| Duplicate / off-topic / damaged PDFs | 106 / 41 / 4 |

See [the completion report](data/resume_completion.md) for the new-book index and [the source inventory](docs/coverage.html) for every PDF. The source directory could not be freshly verified; these counts refer to the saved local collection.

Every note now records which PDF pages were actually read. "Full" means the document's entire extractable text was reviewed; "partial" names the specific pages inspected and, where relevant, says why the rest could not be — most often because the scan is image-only outside a sampled set of pages. This does not mean every page of every book has been read; it means the claim each note makes about its own coverage is now explicit and checkable. Four damaged files remain unavailable. A damaged alternative copy of The Logical Trader points to an available canonical note.

## Work completed

- Resumed existing notes and preserved unrelated working-tree changes.
- Added 148 source-grounded notes, including 17 titles recovered from legacy scan exclusions.
- Used lower-cost drafting agents followed by stronger source review; corrected unsupported rules, attribution, numerical relationships, and PDF-page citations.
- Recovered image-only PDFs with OCR, including an inverted Investment Science scan. Retained exact page coverage and original extraction backups locally.
- Reconciled the manifest, tiers and exclusions. Duplicate landing pages retain canonical navigation; no filler summaries stand in for unreadable documents.
- Rebuilt the A–Z, author, subject and systems indexes; included the existing 14 topic/glossary files.
- Added a filterable source-coverage page. Search covers every complete note and supports category, tier, difficulty and type filters. Content hashes prevent old browser caches hiding new search entries.
- Wrote the 13 topic syntheses, the glossary and `content/paths.md` (three level-based and eight goal-based reading routes, 89 linked notes).
- **Completed the retrospective source-coverage pass.** All 434 previously unrecorded notes were reviewed against their extracted PDF text and now carry `source_review` and `reviewed_pdf_pages`. Short documents received full readings; long books received targeted verification of their numeric and rule claims against the source pages. About a dozen factual errors were found and fixed along the way — among them a misattributed position-sizing study, an invented pyramiding sequence, a wrong spike threshold in the Barry Rudd notes, a %b formula missing its ×100, an unsupported 90% claim in the Ross Hook notes, and a profit-taking rule credited to the wrong author in Market Masters.
- **Deepened the partial readings.** The proprietary-method courses (The Fractal's Edge in both editions, Forex Trading Machine, The Penny Stock Trading System, Profit From Prices, FC Power Trading) and the equation-heavy texts (Investment Science, Rubinstein on Derivatives, The Mathematics of Financial Derivatives, Jaeckel's Monte Carlo Methods) were re-read and their notes materially expanded. Eight further partials were confirmed to be at the limit of their scans — the PDFs are image-only outside a sampled set of pages — and their coverage strings now say so.
- **Editorial pass on the syntheses.** Thirteen major notes added since the syntheses were written were uncited; all four affected topic pages now incorporate them, and every A-tier note in the library is cited by its topic synthesis.
- Regenerated 596 editable Medium drafts against the updated notes, so every draft now carries an accurate source-coverage label. Draft links already point at `https://ninad-k.github.io/trading-playbook/`, which matches the configured `origin` remote, so no re-export is needed before publishing.
- Verified all 733 note files structurally, 851 generated HTML pages, 36,156 local links, 747 search entries and all 733 PDF inventory records.

## Remaining work, in order

1. **Publish to GitHub Pages.** The destination is settled: `origin` is `github.com/ninad-k/trading-playbook`, which is exactly the `https://ninad-k.github.io/trading-playbook/` base already hard-coded in `scripts/07_export_medium.py` and `scripts/08_notion_payload.py`, so no regeneration is needed. Nothing is deployed yet: local `main` is 37 commits ahead of the remote, whose only commit is the initial one, and `docs/` (855 files, 20 MB) has never been committed — it is untracked rather than ignored. Publishing takes two steps, and the URL 404s until both are done: (a) commit and push `main`; (b) in repository settings enable Pages with Source *Deploy from a branch*, branch `main`, folder `/docs`. The source mirror `downloads/` (2.0 GB of PDFs) is git-ignored and must stay that way. Durable edits belong in Markdown or templates, not in `docs/`.
2. **Mirror to Medium and Notion.** Post selected Medium drafts — choose specific posts rather than treating 596 generated drafts as ready to publish. Verify the intended Notion parent/database before syncing; existing local state records only one previously synced book. Preserve page IDs and nest method pages beneath their parents. No remote publication or Notion synchronisation has been performed.
3. **Optional: extend coverage on the general-finance primers.** Ten of the partial notes are ordinary full-text books (financial-statement, valuation and stock-market primers, the single-stock-futures and no-bull-investing titles, the Paulos memoir) whose notes are concise Tier B summaries. Their scans are complete, so deeper reading is possible; it was judged lower value than the proprietary and equation-heavy titles and deliberately left undone.
4. **Optional: re-OCR the sampled scans.** Roughly a dozen PDFs — among them Investment Science, Rubinstein on Derivatives, Glenn Neely's Elliott Wave text, Prechter's Major Works, and the Day Trading University and FC Power courses — yield text on only 25 to 32 of their pages. Their notes are as complete as the current extraction allows. A fresh OCR pass over the image-only pages is the only way to improve them.
5. **Replace damaged sources if obtained.** Keep a documented unavailable status until a legitimate readable replacement is available. Do not infer book content from a filename.

## Content and review rules

- Paraphrase and attribute; do not reproduce chapters or host source PDFs.
- Short documents: read all meaningful pages. Longer books: record the exact sampled or complete chapter ranges and label partial coverage honestly.
- Do not invent missing entries, stops, sizing, indicator parameters or performance figures.
- Clearly identify editorial implications when a source provides research or concepts instead of a trading procedure.
- Schema and link checks verify structure, not financial correctness or profitability.
- Agents own separate note files. One coordinator applies exclusions, canonical links, exports and builds after source-review handoff.

## Rebuild and review commands

Run from the repository root with the existing environment:

```powershell
.venv/Scripts/python scripts/09_resume_inventory.py
.venv/Scripts/python scripts/04_chunk.py <slug> --pages <first-last>
.venv/Scripts/python scripts/05_validate.py
.venv/Scripts/python scripts/06_build_site.py
.venv/Scripts/python scripts/12_check_site.py
.venv/Scripts/python scripts/07_export_medium.py --all-books --site <actual-public-base-URL>
.venv/Scripts/python scripts/08_notion_payload.py <slug>
.venv/Scripts/python scripts/13_completion_report.py
```

`scripts/10_recover_scans.py` accepts explicit recovery-job JSON and skips completed jobs. Tesseract jobs use PyMuPDF with the official English model stored in `downloads/tessdata/eng.traineddata`; rotated scans can specify a render rotation. `scripts/11_reconcile_notes.py` previews saved review decisions; `--apply` updates metadata and canonical references. Inspect decisions before applying new ones.

The live manifest, completion report and coverage page supersede older batch-file counts.
