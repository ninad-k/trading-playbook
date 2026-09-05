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

The disparity index (also called the disparity ratio) is a Japanese moving-average oscillator that expresses today's closing price as a percentage distance above or below a chosen moving average. It is functionally equivalent to a percent-from-moving-average indicator, and Nison notes it is mathematically the same information as the related "divergence index" (current price / moving average, expressed as a ratio around 100% rather than a percentage around 0). Common moving-average lengths cited from Japanese practice are 5-, 9-, or 25-day for shorter-term traders, and 13-week, 26-week, or 75-/200-day for longer-term traders — but, as with all the book's techniques, the exact period and the overbought/oversold threshold are market-dependent and left to be calibrated per instrument rather than fixed.

## Rules

**Formula**: Disparity Index (%) = ((Close - Moving Average) / Moving Average) x 100.

- A reading of 0 means today's close equals the chosen moving average.
- A negative reading means the close is that percentage below the moving average (e.g., -25% on a 13-week disparity index means price is 25% under the 13-week MA).
- A positive reading means the close is that percentage above the moving average (e.g., +12% on a 200-day disparity index means price is 12% over the 200-day MA).

**Overbought/oversold use**: Choose a threshold pair specific to the instrument (Nison's worked examples use roughly +10%/-10% and +15%/-15% depending on the stock). A reading at or beyond the upper threshold flags an overbought market vulnerable to a pullback or sideways consolidation; a reading at or beyond the lower threshold flags an oversold market vulnerable to a bounce. An oversold reading is resolved one of two ways: a sharp bounce, or extended sideways "box action" that lets the index walk back toward zero without price actually reversing.

**Trend confirmation**: Between overbought and oversold extremes, use the index's own direction as a trend confirmation tool — a rising disparity index (moving from an oversold reading toward an overbought one) confirms an uptrend in price; a falling disparity index confirms a downtrend. This is distinct from the overbought/oversold reading itself.

**Divergence**: Plot the peaks (or troughs) of the disparity index against the peaks (or troughs) of price. If price makes a new high but the disparity index makes a lower high than its prior peak, that is bearish (negative) divergence. The mirror — a new price low with a higher disparity-index low — is bullish divergence.

**Combining with candlesticks**: Nison's central trading use is confirmation, not a standalone signal — a bullish candle pattern (hammer, morning star, bullish harami) occurring while the disparity index is at an oversold reading is treated as a stronger buy signal than the same candle pattern appearing at a neutral reading; the same logic applies to bearish candle patterns at overbought readings, and Nison gives a worked example where a strong-looking bullish candle at an overbought disparity reading is treated as a warning not to buy, despite the bullish-looking candle shape.

**Divergence index (equivalent form)**: Divergence (%) = (Close / Moving Average) x 100. A reading of 102% is identical information to a +2% disparity reading; a reading of 97% is identical to a -3% disparity reading. All disparity-index techniques transfer directly to the divergence index, just rescaled around 100 instead of 0.

## Risk

The disparity index carries no inherent stop-loss or position-sizing rule of its own — Nison treats it strictly as a confirmation and context layer for candlestick entries, not an entry/exit system in its own right. Because thresholds are calibrated per market (the book shows different overbought/oversold cutoffs on different stocks), a threshold tuned to one instrument's typical volatility will not necessarily transfer to another; a market with structurally higher volatility will require wider overbought/oversold bands to avoid constant false signals. As with any pure indicator-based reading, an "overbought" market can remain overbought (and continue rising) for an extended period in a strong trend — Nison's own worked example notes that once a market is no longer oversold via "box action" sideways drift rather than a reversal, it becomes vulnerable to renewed downside without the index itself giving a fresh sell signal.

## Caveats

The book gives illustrative threshold values (e.g., ±10%, ±15%) drawn from specific worked chart examples, not universal cutoffs — Nison states explicitly that a reader should expect different disparity zones on different markets and should experiment rather than adopt a single fixed number. A single statistical study cited in the book (Nikkei divergence index, 1980s) gives 95%-confidence divergence ranges by moving-average length (e.g., 200-day divergence 102-110% in a rising market, 90-99% in a falling market), but this is specific to that index and time period and is presented as an example of the method rather than a portable rule.
