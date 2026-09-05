---
title: Candlestick Charting Explained — Pattern Catalogue and Reliability Ranking
author: Gregory L. Morris
year: 1992
slug: greg-morris-candlestick-charting-explained--pattern-catalogue-and-reliability
tier: A
category: "Candlesticks & Chart Patterns"
tags: [candlestick-patterns, pattern-recognition, statistical-testing, indicator-filtering]
difficulty: intermediate
doc_type: system
parent: greg-morris-candlestick-charting-explained
pages: 155
one_liner: "Numeric recognition rules for the classic candlestick catalogue, the trend/success-measurement methodology Morris coded to test them, and the resulting reliability rankings across S&P 100 stocks and 41 futures markets."
related: [greg-morris-candlestick-charting-explained, beyond-candlesticks-steve-nison]
source_file: "Greg Morris - Candlestick Charting Explained.pdf"
---

## What it is

A codeable candlestick pattern-recognition system paired with Morris's own back-tested reliability statistics, rather than a single tradable strategy. It has two layers: (1) precise, numeric recognition rules for the classic reversal and continuation candle patterns, replacing the traditionally subjective "does this look like a Hammer" judgment; and (2) a trend-and-success measurement methodology that lets any of those patterns be objectively scored, plus the actual scores Morris obtained testing over 60 patterns on the S&P 100 (82,000+ days of data) and 41 CSI perpetual futures contracts (49,000+ days), at 3-, 5-, and 7-day prediction intervals. An optional third layer — filtering candle signals through a conventional oscillator's "pre-signal zone" — is included as the book's own recommended enhancement.

## Rules

**A. Identification thresholds (apply before any pattern can be recognized).**
1. **Trend context**: compute a 10-day exponential moving average (EMA) of closing price. Today's close above the EMA = uptrend; below = downtrend. Most patterns require this context to even qualify as a signal.
2. **Long day**: a body (|close − open|) whose size exceeds a minimum threshold relative to recent (5-10 day) price action — Morris offers three interchangeable methods: percent-of-price, percent-of-recent-range, or percent-of-recent-average-body; pick one minimum (e.g., 5% of price) and apply consistently.
3. **Short day**: the mirror of a long day — body size below the same class of threshold.
4. **Doji**: |close − open| less than a small maximum percentage (roughly 1-3%) of the day's high-low range.
5. **Shadow-based subtypes**: classify long lower/upper shadows relative to body length (e.g., a lower shadow ≥2x body = candidate Hammer/Hanging Man territory; ≥3x = Takuri) to distinguish Marubozu, Spinning Top, Dragonfly/Gravestone/Long-Legged Doji subtypes.

**B. Representative pattern rules (full catalogue covers ~60 patterns; these anchor the family).**
6. **Hammer (bullish, downtrend) / Hanging Man (bearish, uptrend)**: small real body at the extreme (top) of the day's range; lower shadow ≥2x body length (any color body); upper shadow ≤5-10% of the day's range; require next-day confirmation (higher close for Hammer, lower open + black body for Hanging Man).
7. **Bullish/Bearish Engulfing**: a trend must be in force; day 2's real body fully engulfs day 1's real body (neither top nor bottom of day 1 may exceed day 2's, though one edge may tie); day 1's color matches the prior trend, day 2's is opposite; ≥30% overlap beyond day 1's body strengthens the signal.
8. **Piercing Line (bullish) / Dark Cloud Cover (bearish)**: day 1 is a long body in the trend direction; day 2 opens beyond day 1's extreme (below day 1's low for Piercing, above day 1's high for Dark Cloud Cover) and closes within, and past the midpoint of, day 1's body — this 50% threshold is rigid; less penetration reclassifies the pair as a continuation pattern (On Neck/In Neck/Thrusting Line) instead.
9. **Three White Soldiers (bullish) / Three Black Crows (bearish)**: three consecutive long bodies of the same color, each closing progressively higher (Soldiers) or lower (Crows), each ideally opening within the prior day's body and closing near its own extreme.
10. **Star family (Morning Star, Evening Star, Doji Star)**: a long body in the trend direction, followed by a small body (or Doji, for a Doji Star) that gaps away from it, followed — for Morning/Evening Star — by a third day closing well into the first day's body in the opposite direction.

**C. Measuring success/failure (the testable core of the system).**
11. **Two baselines**: for each day the trend is known (close vs. 10-day EMA), classify the outcome at a chosen future point as Reverse Current Trend or Continue Current Trend. Because trends persist more often than not, "Continue" is the higher base rate and "Reverse" the lower one.
12. **Prediction interval**: choose how many days ahead to score the outcome (Morris tests 3, 5, and 7; results are reported to be broadly similar for any interval from 1-10 days). At that interval, if price is still on the pattern's predicted side of the trend line, score a success.
13. **Scoring a reversal pattern**: compare its success rate against the Reverse Current Trend base rate — a reversal pattern only adds value if it beats this (inherently sub-50%) baseline.
14. **Scoring a continuation pattern**: compare its success rate against the (higher) Continue Current Trend base rate — a continuation pattern must beat the odds of the trend persisting anyway to be considered valuable; this is why some continuation patterns show high raw success but a negative ranking score.
15. **Discount low-frequency patterns**: any pattern occurring only once or twice in the test sample should be treated as statistically meaningless regardless of its reported success rate; check a pattern's ranking stability across multiple prediction intervals (3/5/7-day) before trusting it — a pattern that jumps around in rank across intervals is unreliable, one that moves steadily in one direction has a horizon preference, and one that stays stable across all intervals is the most dependable signal.

**D. Optional enhancement — indicator filtering.**
16. Choose a bounded oscillator (RSI 14 with 30/70 or 35/65 thresholds; stochastic %D 14 with 20/80 thresholds; CCI 14 with ±100 thresholds; or a zero-line/self-smoothing crossover indicator like MACD, rate of change, or Bollinger %B). Define its "pre-signal area": for a threshold oscillator, the zone beyond the threshold before the reversing cross; for a zero-line oscillator, the zone after crossing zero and before crossing its own smoothing.
17. Only act on a bullish candle pattern while the chosen oscillator sits in its buy pre-signal zone, and only act on a bearish candle pattern while it sits in its sell pre-signal zone; ignore candle signals that fire outside the relevant zone. In Morris's 100-stock 1989-1992 test this cut trade count by more than half (37.1 to 13.7 trades on average) while raising average gain per trade (0.40% unfiltered to 0.60% filtered), though results were mixed pattern-by-pattern (e.g., the price detrend oscillator and linear trend indicator filters underperformed their own unfiltered indicator in the worked single-stock example).

## Risk

No stop-loss, position sizing, or profit target is specified anywhere in this system — Morris's test harness is deliberately simplistic ("always in the market": buy, sell, sell-short, cover) purely to compare candle-only, indicator-only, and filtered signals on equal footing, and he states explicitly that commissions and slippage are excluded from every reported percentage. Risk control here is entirely about avoiding false confidence in an untested or low-frequency pattern: require the trend-context check before accepting any pattern, discount patterns with few occurrences, and prefer patterns whose ranking is stable across multiple prediction intervals rather than the single best-ranked pattern at one interval, which may be an artifact of that specific horizon and sample.

## Caveats

All reliability statistics come from one dataset and era (S&P 100 constituents 1989-1992ish for the ranking tables' underlying data window referenced elsewhere in the book, and CSI perpetual futures contracts of similar vintage) and have not been shown to hold out-of-sample in later or different markets. The "successful" designation is binary and direction-only (did price end up on the predicted side of trend at the prediction interval) — it carries no magnitude, so a barely-positive outcome counts the same as a large favorable move, and the book's own tables show several 100%-success patterns that occurred only once, which Morris himself flags as not meaningful. Thresholds for long/short/Doji classification are given as ranges ("5% is often used," "1 to 3% seems to work quite well") rather than fixed constants, so two implementations using different thresholds will identify a different — sometimes substantially different — set of pattern occurrences from the same price data. The filtering enhancement's results were also pattern- and indicator-specific in Morris's own examples (some indicator filters clearly helped, at least one clearly hurt), so the filtering rule should be validated per indicator and market rather than assumed universally beneficial.
