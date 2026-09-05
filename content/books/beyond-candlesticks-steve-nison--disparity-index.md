---
title: "The Disparity Index"
author: "Steve Nison"
year: 1994
slug: beyond-candlesticks-steve-nison--disparity-index
tier: A
category: Indicators
tags: [disparity-index, moving-averages, overbought-oversold, divergence, japanese-charting]
difficulty: intermediate
doc_type: system
parent: beyond-candlesticks-steve-nison
pages: 276
one_liner: "A percentage-distance-from-moving-average oscillator used by Japanese traders to gauge overbought/oversold conditions, trend, and divergence."
related: [macd, trading-hill-arthur-introduction-to-candlesticks]
source_file: "Beyond_Candlesticks__Steve_Nison_.pdf"
---

## What it is

The disparity index (also called the disparity ratio) is a Japanese moving-average oscillator expressing today's close as a percentage distance above or below a chosen moving average — functionally a percent-from-moving-average indicator, and mathematically identical to the related "divergence index" (close / moving average, as a ratio around 100% instead of a percentage around 0). Common moving-average lengths from Japanese practice: 5-, 9-, or 25-day for shorter-term traders; 13-week, 26-week, or 75-/200-day for longer-term traders. As with all the book's techniques, the exact period and overbought/oversold threshold are market-dependent, calibrated per instrument rather than fixed.

## Rules

**Formula**: Disparity Index (%) = ((Close - Moving Average) / Moving Average) x 100. A reading of 0 means the close equals the moving average; negative means the close is that percentage below it (e.g., -25% on a 13-week index means 25% under the 13-week MA); positive means that percentage above (+12% on a 200-day index means 12% over the 200-day MA).

**Overbought/oversold**: choose a threshold pair specific to the instrument (Nison's worked examples use roughly ±10% and ±15% depending on the stock). A reading at or beyond the upper threshold flags overbought, vulnerable to a pullback or consolidation; at or beyond the lower threshold flags oversold, vulnerable to a bounce. An oversold reading resolves one of two ways: a sharp bounce, or extended sideways "box action" that walks the index back toward zero without price reversing.

**Trend confirmation**: between extremes, use the index's own direction as confirmation — rising confirms an uptrend, falling confirms a downtrend, distinct from the overbought/oversold reading itself.

**Divergence**: a new price high with a lower disparity-index peak than its prior high is bearish divergence; a new price low with a higher disparity-index low is bullish divergence.

**Combining with candlesticks**: Nison's central use is confirmation, not a standalone signal — a bullish candle pattern at an oversold disparity reading is a stronger buy signal than the same pattern at neutral (mirrored for bearish patterns at overbought); one worked example treats a strong bullish-looking candle at an overbought reading as a warning not to buy despite its shape.

**Divergence index (equivalent form)**: Divergence (%) = (Close / Moving Average) x 100 — a 102% reading is identical to a +2% disparity reading, 97% identical to -3%. All disparity techniques transfer directly, just rescaled around 100 instead of 0.

## Risk

The disparity index carries no inherent stop-loss or sizing rule — Nison treats it strictly as a confirmation/context layer for candlestick entries, not a standalone entry/exit system. Because thresholds are calibrated per market, one instrument's threshold won't necessarily transfer to another; higher-volatility markets need wider bands to avoid false signals. Like any indicator reading, "overbought" can persist through an extended strong trend — Nison's own example notes that once a market is no longer oversold via sideways "box action" rather than a reversal, it stays vulnerable to renewed downside without a fresh sell signal from the index itself.

## Caveats

The threshold values given (e.g., ±10%, ±15%) are illustrative, drawn from specific worked chart examples, not universal cutoffs — Nison says explicitly to expect different disparity zones on different markets and to experiment rather than adopt one fixed number. A cited statistical study (Nikkei divergence index, 1980s) gives 95%-confidence divergence ranges by MA length (e.g., 200-day divergence 102-110% in a rising market, 90-99% falling), but this is specific to that index and period, offered as an example of the method rather than a portable rule.
