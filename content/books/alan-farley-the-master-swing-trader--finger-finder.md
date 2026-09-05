---
title: Finger Finder
author: Alan S. Farley
year: 2000
slug: alan-farley-the-master-swing-trader--finger-finder
tier: A
category: Swing Trading
tags: [swing-trading, candlesticks, reversal, bollinger-bands]
difficulty: intermediate
doc_type: system
parent: alan-farley-the-master-swing-trader
pages: 377
one_liner: "Use single-bar hammer, doji, and harami candlesticks at key S/R as a window into hidden reversals in the time frame below the chart."
related: [candlestick-charting-explained]
source_file: "Alan Farley - The Master Swing Trader.pdf"
---

## What it is

Finger Finder reads single-bar candlestick patterns — hammers, dojis, and haramis — as evidence of a reversal that occurred in the time frame beneath the chart being viewed. A long shadow ("finger") that reaches through support/resistance and then closes back inside it shows that price briefly traded through a level, triggered stops, and reversed before the bar closed — information a plain price bar hides. Location relative to major S/R and Bollinger Bands, not the candle shape alone, drives the setup's predictive power.

## Rules

1. **Pattern definition**: open-to-close real body must be one-third or less of the bar's total high-low range (captures dojis and hammers) — filter out "spinning tops" (body near the middle of the range, low predictive value) unless the pattern also qualifies as a harami (real body fits entirely within the prior bar's open-close range, and the prior bar's range exceeds the one before it).
2. **Doji**: open and close nearly identical. **Hammer**: less strict — real body under one-third of total range, positioned at one extreme. **Harami**: candle equivalent of an inside day; can extend beyond the prior bar's high/low as long as the real body stays inside it.
3. **Location filter**: fingers are only significant at high volume or near major S/R; ignore them when buried in congestion. Best signals strike through or against a Bollinger Band extreme or the center band, with shadows piercing the band while the real body stays inside.
4. **Directional read**: a reversal finger opposing the recent trend, with a shadow that exceeds the average bar range for that stock, signals reversal; a finger with its real body pointing in the direction of an already-moving trend ("fish hammer") signals continuation instead.
5. **Aggressive entry**: sell short at a doji/hammer top or go long at a doji/hammer bottom, with a stop just outside the signal bar's shadow.
6. **Defensive entry**: wait for a violation of the real body (not just the shadow) in the intended direction, or wait 3–5 bars for a double-top/bottom test of the finger extreme before entering.
7. **Hidden 100 application** (documented sub-case): valid when the signal candle's shadow doesn't exceed 62% retracement of the price swing it terminates and the smaller time frame shows a clean V-bottom/V-top; entry looks for price to complete the retracement toward 100% after the 62% violation.
8. **2B Finger application**: shadow reaches past an intermediate high/low but the real body closes back inside S/R, with the same-time-frame chart pattern confirming a reversal within 2–4 bars — treat as a small-scale 2B reversal.

## Risk

Stop loss for aggressive entries sits just outside the signal bar's high/low shadow — any violation of the shadow negates the reversal read. For the Hidden 100 case, Farley places the stop under the apex of a subsequent consolidation pattern (e.g., a small triangle) that forms after the signal. Because holding periods are short (fingers typically resolve within 2–3 bars), use tight, bar-based stops rather than wide percentage stops.

## Caveats

Reliable mainly in liquid, high-volume names — thin or low-priced stocks generate meaningless single-bar patterns from noise and wide spreads. The setup is explicitly described as relying more on visual judgment than mathematics ("the skilled eye does a better job... than any mathematics"), so it resists precise backtesting. Ignore candle extremes on very short (1-minute) intraday charts, where bad ticks distort shadow length.
