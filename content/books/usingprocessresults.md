---
title: "Using ProcessResults.xls"
author: "Unknown"
year: unknown
slug: usingprocessresults
tier: B
category: Trading Psychology & Discipline
tags: [mt4, trade-journal, reporting, performance-analysis]
difficulty: intermediate
doc_type: manual
pages: 3
one_liner: "A terse MT4 workflow exports closed-position history and consolidates account and currency-pair results in a spreadsheet."
related: [choosing-a-trading-system-that-actually-works, personal-trading-behaviour]
source_file: "UsingProcessResults.pdf"
source_review: full
reviewed_pdf_pages: "1-3"
---
## Summary

This operational note documents a workflow using the MT4 Expert Advisor GetHistory.mq4 and ProcessResults.xls. GetHistory extracts closed-position history; the spreadsheet creates account worksheets and a combined date-based summary (p. 1). Setup requires specifying the history-file path, one symbol per worksheet, and an output worksheet name, then running “Calculate Summary.” The source warns that the EA updates once per minute rather than every tick, extracts only closed positions, and depends on the account-history range selected by the user (p. 3). It is a reporting tool for demo or live accounts, not a strategy or performance guarantee.

## Key points

- MT4 history settings control what the export contains (pp. 1, 3).
- One currency pair is entered per worksheet and symbols omit the slash, e.g. EURUSD (p. 3).
- Blank rows stop processing further setup rows (p. 3).
- Rerunning can create or overwrite worksheets, so copies are needed to preserve snapshots (p. 3).
- Error handling is limited and paths must be exact.

## Actionable rules

1. Set the intended MT4 account-history range before extraction (pp. 1, 3).
2. Enter the file path, symbol, and destination worksheet in the startup sheet, then calculate the summary (p. 1).
3. Keep a copy of a worksheet before rerunning if historical snapshots must be preserved (p. 3).

## Caveats

The document is software procedure documentation for historical MT4 files. It does not analyze expectancy, open positions, tick-level behavior, or current platform compatibility.

## Who it is for

MT4 users building a basic closed-trade performance log across accounts and pairs.
