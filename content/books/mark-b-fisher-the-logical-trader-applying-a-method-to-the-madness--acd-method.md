---
title: "The ACD Method"
author: "Mark B. Fisher"
year: 2002
slug: mark-b-fisher-the-logical-trader-applying-a-method-to-the-madness--acd-method
tier: A
category: "Day Trading & Scalping"
tags: [acd-method, pivot-points, opening-range, futures, number-line]
difficulty: intermediate
doc_type: system
parent: mark-b-fisher-the-logical-trader-applying-a-method-to-the-madness
pages: 137
one_liner: "Fisher's full ACD ruleset: opening-range breakout entries (A/B), pivot-range confirmation, C/D reversal signals, rolling and longer-term pivots, and a macro number-line trend filter."
related: [mark-b-fisher-the-logical-trader-applying-a-method-to-the-madness, pivots, automated-intraday-open-pivot-setup, forex-intraday-pivots-trading-system-complete-system]
source_file: "Mark B Fisher, - The Logical Trader. Applying A Method To The Madness.pdf"
---

## What it is

ACD is Fisher's rules-based method for entering trades on confirmed breakouts of the day's "opening range" (Point A) or on reversal signals beyond it (Point C), each paired with a pre-defined stop (Point B or D). A calculated pivot range filters for higher-confidence setups and tightens stops. The same mechanics scale to a rolling multi-day or multi-week pivot for longer holds, and a separate daily "number line" score acts as a trend-bias filter.

## Rules

1. **Opening range**: the high/low of the session's first fixed time block (5 min for crude oil/gasoline, 20 min for natural gas/S&P futures in the book's examples). Anchors every other level that day.
2. **Point A (entry)**: an "A value" is a tick distance calibrated per instrument (e.g., 7–8 ticks crude oil, 15 ticks natural gas). A up = opening-range high + A value; A down = opening-range low − A value. Price must hold at/beyond that level for at least half the opening-range time frame to "confirm." Only one A can confirm per day. Go long on a confirmed A up, short on a confirmed A down.
3. **Point B (stop)**: opposite boundary of the opening range from the A entry.
4. **Daily pivot range**: from the prior session's high/low/close, Pivot Price ≈ (High + Low + Close) ÷ 3, with the range built as that price ± a differential (exact differential formula not captured in the sampled OCR — see Caveats).
5. **A through the pivot**: if a confirmed A also clears the pivot range, tighten the stop to the pivot range's far edge instead of Point B (book example: cuts risk from 40 to 10 ticks).
6. **Point C / Point D (reversal)**: Point C is a "C value" of ticks beyond the opening range, valid only after an opposite A already confirmed that session. A C hit signals a sentiment reversal; enter in its direction, stop at Point D (opposite side of the opening range). If C also clears the pivot range, tighten the stop to the pivot edge as in rule 5.
7. **Failed A/C at the pivot**: if price fails to hold an A or C level and reverses back through the pivot range, treat the pivot as proven support/resistance and enter opposite the failed A/C, stopped just beyond the pivot.
8. **Rubber-band trade**: fade a failed approach to an A/C target that snaps back, stop at the A/C price, reduced size.
9. **Time stop**: exit if an anticipated move fails to develop within a set window after a target is reached, regardless of the price stop.
10. **Rolling pivot** (multi-day holds): rebuild the pivot from the high/low/close of the last 3+ trading days, rolling daily; use as entry reference and trailing stop.
11. **Longer-term pivot** (multi-week/seasonal): same formula (rule 4) over an extended window (e.g., first two weeks of each half-year); A/C values scaled up (e.g., 200 ticks vs. 15–20 intraday for natural gas); range held fixed until the next reset window.
12. **Number line (trend filter)**: score each day −4 to +4 by which A/C events occurred and where it closed; sum over a rolling ~30-day window. A cumulative reading of −9, 0, or +9 signals a likely volatility-expanding move — valid only if it develops quickly (the "instant gratification rule"); otherwise discard the signal.

## Risk

Every entry maps to a specific price-level stop (B, D, or a pivot-range edge) — no percent-of-equity formula is given; dollar risk is stop distance × position size, set by the trader. Preferring the pivot-range stop over B/D (rule 5) is the method's main built-in risk reducer. Position size itself is adaptive to recent performance (increased after a hot streak, cut roughly a third to two-thirds during a slump, reset monthly) — see the parent book note.

## Caveats

Built from OCR of a sampled subset of pages, not the full text: the daily pivot's differential component (how far the range extends beyond the pivot price) is named in the glossary but its exact tick/fraction rule fell on unsampled pages — verify against the original before coding. A/C tick values reflect 2000–2001 pit/early-electronic markets and need revalidation today. No aggregate backtest, win rate, or expectancy is given; evidence is anecdotal and example-based.
