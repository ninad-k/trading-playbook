---
title: "Point-and-Figure Breakout Trading (Full System)"
author: "Michael D. Archer, James L. Bickford"
year: 2007
slug: the-forex-chartist-companion--point-and-figure-breakout-trading
tier: A
category: "Market Structure & Price Action"
tags: [point-and-figure, breakout, chart-patterns, forex, trailing-stop, price-objectives]
difficulty: intermediate
doc_type: system
parent: the-forex-chartist-companion
pages: 382
one_liner: "A pip-denominated point-and-figure system: trade breakouts of trend lines or double/triple top-bottom patterns, size the target with a vertical count, and trail the stop behind the last two columns."
related: [john-bollinger-bollinger-on-bollinger-band, s-and-c--wyckoff-method]
source_file: "The_Forex_Chartist_Companion.pdf"
---

## What it is

A point-and-figure (P&F) trading method adapted from stock-market charting to pip-denominated spot currency data. Price is converted into a column chart of Xs (advances) and Os (declines), which strips out time and lateral "noise" so only meaningful directional moves are plotted. Trades are triggered when price breaks a P&F trend line or takes out the resistance/support formed by a double or triple top/bottom pattern; the target is estimated with a "vertical count" formula, and risk is managed with a manually ratcheted trailing stop rather than a fixed stop-loss distance.

## Rules

**Chart construction**
1. Choose a box size — the minimum price increment counted. One pip is standard for major pairs; use a larger box size (2–5 pips) for wide-spread cross pairs or longer-term analysis.
2. Choose a reversal amount — the number of boxes price must move against the current column before a new column starts. Three boxes is the book's default and most common setting.
3. Plot advances as a column of Xs and declines as a column of Os; a new X (or O) is added to the current column once price moves one box size in that direction, and a new column only starts once price reverses by box size × reversal amount.

**Entry — trend-line breakout**
4. Draw a line along the highest Xs of a downtrend (a declining resistance line) or the lowest Os of an uptrend (a rising support line).
5. Buy when a new column of Xs crosses above the downtrend line; enter at the first X above the high of the prior X column.
6. Sell when a new column of Os crosses below the uptrend line; enter at the first O below the low of the prior O column.

**Entry — double/triple top or bottom breakout**
7. A double top is two X columns whose highs align (forming local resistance); a double bottom is two O columns whose lows align (forming local support). Triple tops/bottoms are the same pattern with three columns.
8. Buy on a new X column that exceeds the aligned resistance high; sell on a new O column that breaks the aligned support low.
9. Do not trade the pattern in isolation — confirm with a trend-line signal or other structure first; the book's own statistics show triple top/bottom "reversal" rates close to a 50/50 baseline.

**Price objective (vertical count)**
10. Count the number of boxes (Xs or Os) in the signal column that produced the breakout.
11. Multiply that count by the reversal amount (typically 3).
12. Multiply the result by the box's pip value (e.g., 0.0001 for a 1-pip box on a 4-decimal pair).
13. For a buy signal, add this value to the low of the signal column's lowest X to get the price objective; for a sell signal, subtract it from the high of the signal column's highest O.
14. Treat the objective as approximate — it may take multiple additional columns (two, four, or more) to be reached, or may not be reached at all.

**Exit / trailing stop**
15. On entry, set the initial stop at the highest X of the prior two X columns (for a long) or the lowest O of the prior two O columns (for a short).
16. As each new column extends the trend, ratchet the stop to the highest X (long) or lowest O (short) of the prior two columns at that point — the stop only ever tightens, never loosens.
17. If the trend stalls (a period of sideways/lateral movement with no new extreme) and a reversal looks imminent, exit manually rather than waiting for the trailing stop to be hit.
18. No fixed stop distance, percent-of-equity risk, or position-sizing rule is specified; sizing and per-trade risk are left entirely to the trader.

## Risk

The source gives no percent-of-equity risk figure, no fixed stop-loss distance, and no position-sizing formula — risk control is entirely the manually ratcheted trailing stop described above. The book's only worked example (a EUR/USD short with a 2-pip box, 2-box reversal) entered at 1.3010 with an initial stop at 1.3024 (14 pips of initial risk), ratcheted the stop to 1.3016 and then 1.2998 as the trade worked, and closed manually at 1.2994 for a 16-pip gain — description of one trade, not a backtested track record. No aggregate win rate, profit factor, or drawdown statistics are given for the breakout-and-trail approach itself; the only performance statistics in the source (reversal and continuation percentages after double/triple tops and bottoms) describe pattern behavior, not the profitability of trading it.

## Caveats

This is a discretionary-mechanical hybrid, not a fully automatable system: the entry and price-objective rules are precise enough to code, but the trailing-stop and pattern-confirmation guidance ("confirm with other signals," "exit manually if a reversal looks imminent") require judgment calls the source does not reduce to fixed thresholds. The statistical backing (reversal/continuation percentages) comes from a single instrument and period — largely EUR/USD tick data from calendar year 2002 — so its applicability to other pairs, box sizes, or eras is untested in the source. The authors themselves note that double/triple top and bottom reversal percentages are close to a 50/50 coin-flip baseline, meaning the pattern alone carries little statistical edge; the edge, if any, comes from combining it with trend-line confirmation and disciplined stop management that the book describes only qualitatively.
