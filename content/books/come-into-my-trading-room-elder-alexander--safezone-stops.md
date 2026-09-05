---
title: SafeZone Stops
author: Alexander Elder
year: 2002
slug: come-into-my-trading-room-elder-alexander--safezone-stops
tier: A
category: Trading Psychology & Discipline
tags: [safezone, trailing-stop, volatility, noise-filter, chandelier-exit]
difficulty: intermediate
doc_type: system
parent: come-into-my-trading-room-elder-alexander
pages: 322
one_liner: "Noise-adaptive trailing stop: place the stop a multiple of the average recent penetration below (uptrend) or above (downtrend) the prior bar, moving only in the trend's favor."
related: []
source_file: "Come Into My Trading Room - Elder Alexander.pdf"
---

## What it is

SafeZone is a trailing-stop method Elder developed to place stops tight enough to protect capital but far enough away to avoid being hit by ordinary market "noise" (the countertrend portion of each day's range). It defines noise empirically from recent price behavior rather than using a fixed distance or percentage, and moves only in the direction that reduces risk (never loosens). Elder pairs the same underlying logic with a second method, the Chandelier Exit, for riding stronger trends with wider stops.

## Rules

**Trend filter**: use the slope of a 22-day EMA (or another trend indicator) to determine whether the position is being held in an uptrend or a downtrend; SafeZone is calculated differently for each.

**Uptrend (long) calculation, using daily bars**:
1. For each bar, measure the downside penetration: how far today's low is below yesterday's low (zero if none).
2. Choose a lookback period (start at 10 days; test up to 100 for longer-term averaging) and sum the downside penetrations over that window.
3. Count how many of those bars actually penetrated (had a nonzero value).
4. Average Downside Penetration = sum of penetrations ÷ count of penetrating bars.
5. Multiply yesterday's Average Downside Penetration by a coefficient (start at 2, test up to 3) and subtract the result from yesterday's low to get today's stop.
6. The stop may only move up over time (in the direction of the trade) — if the formula would lower it, hold the stop at its prior level instead.

**Downtrend (short) calculation** mirrors the above using upside penetrations of the previous day's high: Average Upside Penetration × coefficient, added to yesterday's high; the stop may only move down, never up.

**Lookback window discipline**: do not let the lookback period extend back past the most recent significant trend reversal — e.g., if the trend flipped from down to up two weeks ago, cap the lookback at roughly 10 trading days so the noise estimate reflects the current regime, not the prior one.

**Coefficient selection**: 2–3× the average penetration is the starting range Elder recommends; back-test the coefficient on the specific instrument being traded rather than assuming a universal value.

**Chandelier Exit (companion method for strong trends)**: Chandelier = highest high over N days − coefficient × Average True Range(N) for longs (mirror with lowest low + coefficient × ATR for shorts). Elder's example uses N = 22 and coefficient = 3 (formula: `Hhv(hi,22) − 3×ATR(22)`). Because it hangs from the trend's price extreme rather than from the previous bar, it gives up more open profit than SafeZone but tolerates a strong, fast-moving trend without being prematurely stopped out; a trader may take partial profits at a channel line and trail the remainder with the Chandelier Exit.

## Risk

SafeZone stops still have to satisfy the parent book's 2% Rule: the position size must be set so that the distance from entry to the initial SafeZone (or Chandelier) stop, multiplied by shares/contracts, does not exceed 2% of trading equity. SafeZone can also be used as a pre-trade filter: multiply the 22-day EMA of the instrument's SafeZone value by 2 and compare it to 2% of account equity; only trade instruments where that noise-based figure is less than the 2% risk budget (i.e., average noise under roughly 1% of equity), otherwise a logical stop cannot be placed without breaking the risk rule.

## Caveats

Elder states SafeZone is "not a mechanical gadget to replace independent thought" — the lookback period, coefficient, and choice between SafeZone and Chandelier Exit are left to trader judgment and testing, with no single backtested optimum given in the text. The spreadsheet-based calculation (average penetration, coefficient multiplication) requires the trader to program it or track it manually; Elder notes that as of writing, few software packages included SafeZone natively. The Chandelier Exit's wider stop trades off protection of open profit for tolerance of volatility — Elder recommends it mainly for experienced traders riding a strong, established trend, not as a default stop method.
