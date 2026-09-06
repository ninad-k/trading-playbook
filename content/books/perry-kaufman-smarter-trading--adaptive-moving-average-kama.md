---
author: Perry J. Kaufman
category: Trend Following & Mechanical Systems
difficulty: intermediate
doc_type: system
one_liner: A trendline that automatically speeds up in trending markets and slows
  down in noisy/sideways markets, driven by an Efficiency Ratio measuring net direction
  versus total price movement.
pages: 257
parent: perry-kaufman-smarter-trading
related:
- perry-kaufman-smarter-trading
- richard-l-weissman-mechanical-trading-systems
slug: perry-kaufman-smarter-trading--adaptive-moving-average-kama
source_file: Perry Kaufman - Smarter Trading.pdf
tags:
- kama
- adaptive-moving-average
- efficiency-ratio
- trend-following
- moving-average
- exponential-smoothing
tier: A
title: The Adaptive Moving Average (KAMA)
year: 1995
---

## What it is

The Adaptive Moving Average (AMA), widely known outside this book as KAMA (Kaufman's Adaptive Moving Average), is an exponential moving average whose smoothing constant is not fixed but recalculated on every bar from a measure of trend "efficiency." When the market is moving cleanly in one direction, the smoothing constant rises toward a fast setting so the trendline tracks price closely; when the market is choppy/sideways, the smoothing constant falls toward a slow setting so the trendline flattens and resists whipsaws. The trend signal itself is simply the direction the AMA line is moving — no separate price-crossing rule is used.

## Rules

**Step 1 — Efficiency Ratio (ER).** Choose a lookback period (Kaufman's own TradeStation-style code example uses period = 10 days):
- `signal` = |close − close[period periods ago]| (net directional price change over the period)
- `noise` = sum of |close − close[1 bar ago]| over every bar in the period (total path length traveled, including back-and-forth movement)
- `ER = signal / noise`

ER ranges from 0 (pure noise — no net progress despite lots of movement) to 1 (perfectly directional — every bar moved the same way).

**Step 2 — Smoothing constant (SC).** Map ER onto a smoothing constant bounded by a fastest and slowest exponential-average speed:
- Fastest constant: `fastest = 2/(2+1) = 0.6667` (equivalent to a 2-period EMA)
- Slowest constant: `slowest = 2/(30+1) = 0.0645` (equivalent to a 30-period EMA)
- `SC = [ER × (fastest − slowest) + slowest]²` — the squaring (applied after the linear interpolation) makes the constant fall toward the slow end quickly and rise toward the fast end more gradually, so the AMA is conservative about speeding up but decisive about slowing down.

**Step 3 — The AMA line itself**, computed like a standard exponential moving average but with the period-by-period recalculated SC in place of a fixed constant:
`AMA[today] = AMA[yesterday] + SC × (close[today] − AMA[yesterday])`

**Basic trading rule** — Kaufman's stated system: buy when the AMA line turns up; sell (go short, or exit long) when the AMA line turns down. Signals are based on the direction of the trendline itself, not on price crossing the line, because the formula already limits how much the line can move bar to bar.

**Filter for false signals** — because a flat/sideways AMA can still wiggle slightly, Kaufman's own code example (TradeTrac/EasyLanguage-style, reproduced from the book) adds a noise filter before acting on a direction change:
- Compute `dama = AMA − AMA[1 bar ago]`, and also the two- and three-bar-back differences `dama2`, `dama3`.
- Compute `sdama` = standard deviation of `dama` over a lookback (book's example: 20 bars) multiplied by a filter constant (book's example: 0.10).
- Only signal a new long when `dama ≥ 0` **and** at least one of `dama`, `dama2`, `dama3` exceeds `sdama` (the line has moved up by more than the filtered noise threshold recently).
- Only signal a new short symmetrically, when `dama < 0` and at least one of the three back-differences is more negative than `−sdama`.
- Period (10), filter (0.10), and sdays (20) are treated as optimizable coefficients in Kaufman's own code, not fixed constants.

**Parameter defaults given in the text**: ER lookback = 10 days; fastest EMA equivalent = 2 days; slowest EMA equivalent = 30 days; noise-filter lookback = 20 days; filter multiplier = 0.10.

## Risk

Kaufman presents the AMA as a trend-following trendline only — a basic system, not a complete trading strategy. He explicitly separates it from entry/exit refinements, profit-taking, and stop-loss logic, which he treats as independent ("lateral") components to be designed and tested separately rather than folded into the AMA formula itself. No specific stop-loss size or position-sizing rule is given for AMA specifically; the book's general risk-control guidance (Chapter 6/10 in the parent book) — normalize to a fixed maximum drawdown, prefer deleveraging over reliance on tight stops, and size positions from a measured combination of drawdown and equity-change standard deviation — applies to AMA as it would to any trend system. Because AMA is fundamentally a trend-following method, it carries the standard trend-following risk profile: frequent small losses during transitions between trending and choppy regimes (mitigated, not eliminated, by the noise filter above), and full exposure to a sharp reversal immediately after the smoothing constant has sped up into a fast-tracking state.

## Caveats

This description is drawn from the sampled OCR pages of the book (roughly pages 133–156 of a 257-page book whose text was OCR'd only for a spaced sample of pages); some surrounding explanatory text — for example, the fuller "Testing the AMA" results section and additional discussion of "Programming the Adaptive Moving Average" — falls on pages that were not part of the OCR sample and so is not reflected here. The formula and defaults above are reconstructed directly from Kaufman's own reproduced source code (Box 8-4 in the book) and are consistent with the standard published KAMA formula used elsewhere in the industry. The squaring step in the smoothing-constant calculation is a specific design choice by Kaufman (biasing the line toward caution) rather than a mathematical necessity of the efficiency-ratio concept — a linear (unsquared) mapping is a documented variant used by other implementations. As with any trend method, KAMA's speed still lags at the very start of a new trend and can whip back and forth during a slow transition from a trending to a choppy regime before the Efficiency Ratio fully registers the change.