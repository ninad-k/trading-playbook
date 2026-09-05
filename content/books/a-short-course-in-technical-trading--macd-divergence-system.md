---
title: "MACD Crossover and Divergence System"
author: Perry J. Kaufman
year: 2003
slug: a-short-course-in-technical-trading--macd-divergence-system
tier: A
category: Indicators
tags: [macd, momentum, divergence, oscillator, exponential-smoothing]
difficulty: intermediate
doc_type: system
parent: a-short-course-in-technical-trading
pages: 339
one_liner: "Fully specified MACD (40/20/9) with a signal-line crossover trend rule and a three-part scaled-exit divergence rule."
related: []
source_file: "A Short Course in Technical Trading.PDF"
---

## What it is

The moving average convergence-divergence (MACD) indicator, built as the difference between a fast and slow exponentially smoothed trendline, further smoothed into a "signal line." Kaufman presents it two ways: as a basic trend-following crossover system, and — more effectively — as a divergence detector that anticipates tops and bottoms when price makes a new extreme but the MACD does not confirm it.

## Rules

**Calculation (Kaufman's worked example, 40/20/9):**
1. Convert calculation periods to smoothing percentages using `2 / (N + 1)`: slow period 40 days → 0.0243 (2.43%); fast period 20 days → 0.0476 (4.76%).
2. Calculate a slow exponentially smoothed trendline using the 2.43% smoothing constant.
3. Calculate a fast exponentially smoothed trendline using the 4.76% smoothing constant.
4. **MACD line = fast trendline − slow trendline.** (Positive and rising when the market is moving up quickly.)
5. **Signal line** = 9-day exponential smoothing of the MACD line (smoothing constant ≈ 0.10, i.e., 2/(9+1)).
6. **Histogram** = MACD line − signal line; used to visualize relative strength/weakness of the MACD versus its own signal line.

**Trend crossover rules:**
- Buy when the MACD line crosses above the signal line.
- Sell when the MACD line crosses below the signal line.
- Raw crossovers generate frequent false signals; Kaufman recommends filtering by only acting on crossovers that follow the MACD reaching a threshold extreme relevant to the instrument's own historical range (he explicitly warns against picking a threshold like ±2.00 after the fact purely because it worked on one chart — that is curve-fitting).

**Divergence rules (the stronger use of the indicator):**
1. Identify two consecutive rising price swing highs (bearish case) or two consecutive falling swing lows (bullish case).
2. Compare the MACD line's value at each of the two price extremes. Bearish divergence: price makes a higher high while the MACD makes a lower peak. Bullish divergence: price makes a lower low while the MACD makes a higher trough.
3. **Anticipating entry (bearish example) — scale into the trade in three parts:**
   - Sell the first third as soon as price makes a new high on materially weaker MACD than the prior high.
   - Sell the second third when the MACD comes back within 15-20% of its previous peak value.
   - Sell the final third on the actual signal-line crossover (the latest, most conservative confirmation — but typically the worst fill price).
4. **Exit the divergence trade** when the MACD returns to zero (treat this as the natural "prices have returned from overbought/oversold to neutral" exit) — do not expect price to run from overbought straight through to oversold.
5. **Invalidate/stop the trade** if the MACD rallies back above its previous peak (bearish case) or falls back below its previous trough (bullish case) — this means the divergence pattern has failed, and the position should be closed for a loss.
6. **Combine with trend for the best case:** hold a divergence-driven short only if the underlying trend also turns down by the time MACD reaches zero; then continue riding it as a trend trade rather than closing at the neutral point.

## Risk

- Because divergence trades are entered before confirmation (steps 1-2 of the scale-in), they carry meaningfully more risk than the pure crossover rule; that risk is explicitly compensated for by scaling in over three tranches rather than committing full size on the first weak signal.
- The MACD itself has no fixed numeric overbought/oversold threshold — Kaufman shows that a level like ±2.00 that fits one chart can be entirely wrong on another with a different volatility profile (peaks as high as ±10 are shown on a different instrument), so any absolute threshold must be recalibrated per instrument using a long history, not fitted from a single chart.
- Divergence is stronger and more tradable when the angle between rising price and falling MACD (or vice versa) is pronounced; shallow, nearly parallel divergences are lower-confidence and should be sized down or skipped. A specific quantified filter given for the related stochastic divergence (structurally identical logic) requires the second oscillator peak to be at least 5-15% lower than the first.
- A basic uncompensated MACD crossover system, run with no filter, is explicitly shown to generate large gains at real turning points but also "a lot of other crossings that generated losses" — it should not be traded as a standalone system without the extreme-threshold or divergence filters above.

## Caveats

Kaufman is unusually candid that the ±2.00 MACD threshold used in his own worked example is an after-the-fact fit to that specific chart and would be "fitting the data" if presented as a general rule — treat any single fixed numeric MACD threshold with skepticism and re-derive it from the instrument's own historical MACD range instead. The MACD's calculation periods (40/20/9 here) are illustrative rather than asserted optimal; the book does not provide a parameter sweep or backtest table for MACD/divergence performance the way it does for the single-trend and breakout methods, so expected win rate, drawdown, and trade frequency are not quantified for this system.
