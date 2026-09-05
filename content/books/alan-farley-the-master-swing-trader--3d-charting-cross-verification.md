---
title: 3D Charting and Cross-Verification
author: Alan S. Farley
year: 2000
slug: alan-farley-the-master-swing-trader--3d-charting-cross-verification
tier: A
category: Swing Trading
tags: [swing-trading, cross-verification, multi-timeframe, bollinger-bands, moving-averages]
difficulty: intermediate
doc_type: system
parent: alan-farley-the-master-swing-trader
pages: 377
one_liner: "A multi-time-frame confluence method: only trade where several independent S/R signals converge across three related chart windows."
related: [john-bollinger-bollinger-on-bollinger-band, come-into-my-trading-room-elder-alexander]
source_file: "Alan Farley - The Master Swing Trader.pdf"
---

## What it is

3D charting and cross-verification (CV) are Farley's core trade-selection method, used underneath every one of his named setups. Instead of relying on a single indicator or pattern, the trader watches three related time frames simultaneously (one above and one below the intended holding period) and only acts when independent support/resistance signals — a prior high or low, a Fibonacci retracement, a moving average, a trendline, a Bollinger Band extreme — line up at the same price. Convergence of unrelated signals ("cross-verification") is treated as evidence that many market participants will react at that level, raising the odds of a clean reaction.

## Rules

**Time-frame stack** (pick one row matching holding period):

| Trader type | Holding period | 3D chart combination |
|---|---|---|
| Scalper | seconds–minutes | 1-min / 5-min / 15-min |
| Day trader | minutes–hours | 1-min / 5-min / 60-min |
| Position trader | hours–days | 60-min / daily / weekly |
| Investor | days–weeks | daily / weekly / monthly |

1. Build the "charting landscape" on the primary time frame: horizontal S/R (prior highs/lows), trendlines, Fibonacci grid (38%/50%/62%) drawn over the relevant swing, moving average ribbon (20-50-200 daily, or 5-8-13 with 2 std-dev Bollinger Bands intraday), and candlestick reversal patterns.
2. Look for price zones where 2 or more of these independently derived levels intersect. Farley calls 4+ overlapping signals at one price "CV×4" — the highest-probability setups.
3. Confirm on the time frame *above* the primary chart that no larger-scale S/R will block the trade before it can reach a reasonable profit target.
4. Confirm on the time frame *below* the primary chart (or via candlestick shadows / Finger Finder analysis) for a precise, low-risk entry trigger once price reaches the CV zone.
5. Define the profit target (PT) as the distance from entry to the next opposing S/R barrier, and the failure target (FT) as the distance to the level that proves the setup wrong. Only take trades where PT is roughly 3× FT before slippage (discount to ~2.5:1 after).
6. Use log (percentage) charts for low-priced or fast-moving stocks; use linear (arithmetic) charts for higher-priced or slower-moving stocks — trendlines and channel widths behave differently on each.
7. Treat lower-pane indicators (RSI, MACD, Stochastics) as confirmation only, not the primary signal; ignore one once experience shows the price pattern tells a more reliable story.

## Risk

CV does not itself size positions — it filters entries. Combine it with Farley's general risk rules: never enter without a pre-defined FT; keep per-trade loss within personal risk tolerance (position size derived from the FT distance); require ~3:1 reward:risk before slippage; and prefer discretionary, trailing S/R-based exits (e.g., an 8-bar or 13-bar MA violation on the 5-8-13 grid) over fixed stops when the position can be actively watched. Because CV is discretionary, risk is concentrated in mis-identifying which levels are "real" S/R — Farley recommends favoring setups with fewer, cleaner intervening obstacles between entry and target over crowded charts with many marginal levels.

## Caveats

Cross-verification is a qualitative confluence heuristic, not a mechanical, backtestable rule — how many levels must converge, and how close counts as "the same price," is left to trader judgment. It also assumes the trader can reliably draw correct trendlines, Fibonacci grids, and S/R zones, which is itself a skill with no objective scoring in the text. The method predates modern high-frequency/algorithmic market structure, and Farley's specific MA/Bollinger settings (20-50-200, 5-8-13) are heuristic defaults rather than optimized parameters — the book presents no systematic backtest of the CV framework itself, only illustrative chart examples.
