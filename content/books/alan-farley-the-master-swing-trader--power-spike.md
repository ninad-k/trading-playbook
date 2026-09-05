---
title: Power Spike
author: Alan S. Farley
year: 2000
slug: alan-farley-the-master-swing-trader--power-spike
tier: A
category: Swing Trading
tags: [swing-trading, volume-analysis, breakout, reversal]
difficulty: intermediate
doc_type: system
parent: alan-farley-the-master-swing-trader
pages: 377
one_liner: "Trade breakouts, breakdowns, reversals, or swing pivots confirmed by volume spiking to defined multiples of the 50-day volume moving average."
related: []
source_file: "Alan Farley - The Master Swing Trader.pdf"
---

## What it is

Power Spike is a volume-driven setup: it identifies emotional, high-participation events (measured against a 50-day volume moving average, VMA) and classifies the price context they occur in — breakout, breakdown, reversal, or pivot — before choosing a strategy. It is a daily-chart-only tool (Farley considers intraday volume too noisy and time-biased for reliable signals in most stocks) and explicitly excludes merger/acquisition-driven volume spikes.

## Rules

1. **Signal threshold (single bar)**: volume equal to or exceeding 3× the 50-day VMA. **Multi-day threshold**: volume equal to or exceeding 2× the 50-day VMA for two consecutive days. A tighter/higher-conviction variant raises these to 5× (single bar) and 3× (two days).
2. **Exhaustion warning**: volume prints of 5–6× the 50-day VMA often mark the start of a "short-circuited" phase — the active trend flatlines afterward into a series of inside days and narrow-range bars; stand aside rather than chasing continuation.
3. **Classify the pattern before trading**: breakout/breakdown from a base (enter on pullback, or use a tight arbitrary stop if price moves too fast for a pullback), reversal after an extended trend (shift to the next-lower time frame and trade the resulting reversal pattern), or swing pivot (price oscillates across the spike level for an extended period — use a "1-2 pierce" strategy: let price pierce and test the pivot axis once, then enter on the next test in the direction of the swing back through center).
4. **Location matters**: spikes at old highs/lows (past battle zones) carry more long-term directional significance than spikes in open territory, because they force a decision between trapped holders and new entrants.
5. **Data hygiene**: exclude secondary offerings, large single-holder transactions, and unadjusted stock-split data, all of which create false volume spikes with no crowd-psychology content.
6. **Breakdown Spike application** (documented sub-case): requires an obvious support level that has persisted for months, breaking down on a high-volume event, followed by continued decline at a milder angle — the setup works because heavy prior selling has already exhausted at-risk holders, so the stock "falls from its own weight."

## Risk

Because power spike trades split into several distinct sub-strategies (breakout/breakdown, reversal, pivot), stop placement follows the sub-strategy: a tight stop beyond the base or S/R level for breakout/breakdown trades, a stop beyond the smaller-time-frame reversal pattern for reversal trades, and a stop just beyond the pivot axis extreme for pivot trades. Farley flags pivot-spike strategies as the most complex of the three and suggests most traders should avoid them.

## Caveats

The VMA-multiple thresholds (3x/2x, 5x/3x) are Farley's own heuristics, adjustable "according to personal interest," not empirically optimized values. The method explicitly should not be applied to intraday charts for most stocks because first/last-hour volume can represent 60%+ of the session's total, distorting relative-spike readings; it's usable intraday only in the most liquid, index-like names. Requires manual exclusion of corporate-action-driven volume (secondaries, block trades, splits), which demands fundamental awareness beyond the chart itself.
