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

1. **Opening range**: high/low of the session's first fixed time block (5 min crude oil/gasoline, 20 min natural gas/S&P in the book's examples). Anchors every other level that day.
2. **Point A (entry)**: an "A value" is a per-instrument tick distance (e.g., 7–8 ticks crude oil, 15 ticks natural gas). A up = range high + A value; A down = range low − A value. Price must hold at/beyond it for at least half the opening-range time frame to "confirm." Only one A confirms per day. Go long on a confirmed A up, short on a confirmed A down.
3. **Point B (stop)**: opposite boundary of the opening range from the A entry.
4. **Daily pivot range**: from the prior session's high/low/close, Pivot Price ≈ (High + Low + Close) ÷ 3, range built as that price ± a differential (exact differential formula fell outside the sampled OCR pages — see Caveats).
5. **A through the pivot**: if a confirmed A also clears the pivot range, tighten the stop to the pivot's far edge instead of Point B (book example: 40 ticks → 10 ticks of risk).
6. **Point C / D (reversal)**: Point C is a "C value" of ticks beyond the opening range, valid only after an opposite A already confirmed that session; a C hit signals reversal — enter in its direction, stop at Point D (opposite opening-range side). If C also clears the pivot, tighten to the pivot edge as in rule 5.
7. **Failed A/C at the pivot**: if price fails to hold an A/C level and reverses back through the pivot range, enter opposite the failed A/C, stopped just beyond the pivot.
8. **Rubber-band trade**: fade a failed approach to an A/C target that snaps back; stop at the A/C price, reduced size.
9. **Time stop**: exit if the anticipated move fails to develop within a set window after a target is reached.
10. **Rolling pivot** (multi-day holds): rebuild the pivot from the high/low/close of the last 3+ trading days, rolling daily; use as entry reference and trailing stop.
11. **Longer-term pivot** (seasonal): same formula (rule 4) over an extended window (e.g., first two weeks of each half-year); A/C values scaled up (e.g., 200 vs. 15–20 ticks for natural gas); held fixed until the next reset.
12. **Number line (trend filter)**: score each day −4 to +4 by which A/C events occurred and close location; sum over a rolling ~30-day window. A cumulative −9, 0, or +9 signals a likely volatility-expanding move, valid only if it develops quickly ("instant gratification rule"); otherwise discard.

## Risk

Every entry maps to a price-level stop (B, D, or a pivot-range edge) — no percent-of-equity formula is given; dollar risk is stop distance × position size, set by the trader. Preferring the pivot-range stop over B/D (rule 5) is the method's main built-in risk reducer. Position size is otherwise adaptive to recent performance (larger after a hot streak, cut a third to two-thirds during a slump, reset monthly) — see the parent book note.

## Caveats

Built from OCR of a sampled subset of pages, not the full text: the pivot's differential component (how far the range extends beyond the pivot price) is named in the glossary but its exact rule fell on unsampled pages — verify against the original before coding. A/C tick values reflect 2000–2001 pit/early-electronic markets and need revalidation today. No aggregate backtest, win rate, or expectancy is given; evidence is anecdotal and example-based.
