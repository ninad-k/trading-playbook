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

ACD is Fisher's rules-based intraday-to-swing method for entering trades on confirmed breakouts of an "opening range" (Point A) or on reversal signals beyond that range (Point C), always paired with a pre-defined stop (Point B or Point D respectively). A calculated daily pivot range is layered on top to filter for higher-confidence setups and to tighten stops. Longer holding periods use the same mechanics scaled to a rolling multi-day or multi-week pivot. A separate "macro ACD" daily scoring system (the number line) is used as a trend-bias filter across many sessions.

## Rules

**1. Opening range.** Define the opening range as the high/low band of the first fixed time block of the session (examples in the book: 5 minutes for crude oil/gasoline, 20 minutes for natural gas/S&P futures; longer for slower stocks). This range is the anchor for every other level that day.

**2. Point A (entry trigger).** Pick an "A value" — a tick distance calibrated to the instrument's typical volatility (the book tabulates these per market; e.g., 7–8 ticks for crude oil, 15 ticks for natural gas, 25 ticks for unleaded gasoline). Plot A up = top of opening range + A value, and A down = bottom of opening range − A value. If price trades at or beyond the A up (or A down) level and *stays there for at least half the opening-range time frame*, that A is "confirmed." Only one A can be confirmed per day — a confirmed A up rules out an A down for the rest of that session, and vice versa. On confirmation: go long above a confirmed A up, or short below a confirmed A down.

**3. Point B (stop for an A trade).** The initial stop for a position taken off Point A is the opposite boundary of the opening range (e.g., long above an A up, stop below the low of the opening range).

**4. Daily pivot range.** Calculate from the prior session's high (H), low (L), and close (C): Daily Pivot Price ≈ (High + Low + Close) ÷ 3, with the daily pivot range built as that pivot price plus/minus a differential derived from the same high/low/close (the exact differential formula was not captured in the sampled OCR pages — see Caveats). Price approaching, bouncing off ("pivot range support/resistance"), or "slicing through" this range generates the pivot-based signals below.

**5. A through the pivot (preferred, lower-risk entry).** If a confirmed A up/down also trades through and settles beyond the daily pivot range, treat this as a higher-confidence signal. Tighten the stop from Point B to the far side of the pivot range instead — in the book's worked example this cut risk from 40 ticks (Point B) to 10 ticks (pivot range edge) for the same entry.

**6. Point C and Point D (reversal trade).** Point C is a price level a "C value" of ticks beyond the opening range (C values are instrument-specific and, for commodities, different from A values; for stocks A and C values are equal) — but a C signal is only valid *after* an opposite-direction A has already been confirmed that session (e.g., a C down is only valid following a confirmed A up). A valid C hit signals a sentiment reversal; enter in the direction of C. Point D is the resulting stop: the opposite side of the opening range from the C trade (mirrors Point B's role for A trades). If Point C also trades through the daily pivot range, the same risk-tightening as rule 5 applies (stop to the pivot-range edge instead of Point D).

**7. Failed-A / failed-C setups.** If price approaches an A (or C) level and fails to hold there for the required time before reversing back into the opening range, and this failure occurs at or within the pivot range, treat the pivot range as having "proven" support/resistance — this is a lower-risk entry in the *opposite* direction of the failed A/C, stopped just beyond the pivot range.

**8. Rubber-band trade.** When price stretches toward an A/C target, fails to reach it, and snaps back sharply, fade the move with a tight stop placed at the A/C price level itself and reduced size (book example: 4 ticks of risk for a 126-tick gain). This is an exception-style setup layered on top of the core A/B/C/D rules, not a replacement for them.

**9. Time stop.** If price reaches a target level (pivot range or A/C) but the market fails to develop the anticipated move within a trader-chosen time window, exit regardless of whether the price stop has been hit.

**10. Rolling pivot (multi-day holds).** For positions held several days to weeks, replace the daily pivot range with a rolling pivot built from the highest high and lowest low of the last three (or more) trading days and the most recent close, recalculated each day as the oldest day drops off. Use it as both the entry reference and a trailing stop.

**11. Longer-term pivot (multi-week/seasonal holds).** For position trades, calculate a pivot range from the highest high, lowest low, and closing price of an extended window (the book's examples use the first two calendar weeks of each half-year) using the same pivot formula as rule 4. A/C values for this time frame are scaled up substantially (book example: 200 ticks for natural gas versus 15–20 ticks intraday). This range is then used, unchanged, for the following multi-month period until the next reset window.

**12. Macro ACD / number line (trend filter, not a standalone entry signal).** Score each trading day from −4 to +4 based on which ACD events occurred that day (A up/down confirmed, C up/down confirmed, close location relative to the opening range and pivot). Sum the score over a rolling ~30 trading-day window. Values between −9 and +9 are treated as normal; when the cumulative sum reaches −9, 0, or +9 it signals the market is at a "critical mass" point likely to see a significant, volatility-expanding move — but only if that move develops quickly ("instant gratification rule"); if the expected move stalls, the signal is considered to have failed and should be discarded rather than held for.

## Risk

Every entry rule pairs to a specific, pre-defined price-level stop (Point B, Point D, or the near/far edge of the pivot range) — there is no percent-of-equity formula in the source material; dollar risk per trade is a function of the chosen stop distance and position size, set independently by the trader. Preferring the pivot-range stop over the B/D stop when both are available (rule 5) is the book's primary built-in risk-reduction technique, since it materially shortens stop distance for the same entry. Position size itself is described elsewhere in the parent book as adaptive to trading performance (increased after a hot streak, cut by roughly a third to two-thirds during a slump, reset monthly) rather than fixed — see [[mark-b-fisher-the-logical-trader-applying-a-method-to-the-madness]] for that discussion.

## Caveats

These notes are built from OCR of a sampled subset of pages (front matter plus evenly spaced pages), not the full 137-page text, so some numeric detail is incomplete: the exact "pivot differential" component of the daily pivot range formula (how far the range extends above/below the pivot price) appears in the glossary but the specific tick/fraction rule was on pages not captured in the sample — the pivot price itself (an average of the prior day's high, low, and close) is clear from the text, but readers should verify the differential against the original book (referenced around pp. 37–38 in the index) before coding this system. A/C tick values and opening-range lengths are calibrated to instruments and volatility regimes circa 2000–2001 pit/early-electronic trading and would need revalidation for current markets. No aggregate backtest, win rate, or expectancy figure is given for the system as a whole; all supporting evidence in the source is anecdotal or single-example chart illustrations.
