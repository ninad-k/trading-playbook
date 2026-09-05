---
title: Candlestick Charting Explained
author: Gregory L. Morris
year: 1992
slug: greg-morris-candlestick-charting-explained
tier: A
category: "Candlesticks & Chart Patterns"
tags: [candlestick-patterns, japanese-charting, pattern-recognition, reversal-patterns, continuation-patterns, statistical-testing, indicator-filtering]
difficulty: intermediate
doc_type: book
pages: 155
one_liner: "A candlestick pattern catalogue with precise numeric recognition rules, then a computer test of over 60 patterns' actual success rates across S&P 100 stocks and 41 futures markets."
related: [beyond-candlesticks-steve-nison, big-profit-patterns-using-candlestick-signals-and-gaps-stephen-w-bigalow, candlesticks-fibonacci-and-chart-pattern-trading-tools, john-l-person-swing-trading-using-candlestick-charting-with-pivot-point, candlestick-patterns-for-day-trading]
source_file: "Greg Morris - Candlestick Charting Explained.pdf"
---

## Overview

Gregory L. Morris, creator of the N-Squared charting software, wrote one of the first candlestick books to move past pure visual pattern description into a computer-testable rulebook. The book proceeds in three stages: first, single candle lines (Marubozu, Doji, Spinning Tops, Paper Umbrella) and multi-line reversal and continuation patterns are each given a standardized entry — Japanese name, commentary, a graphic, and precise "Rules of Recognition" written so a programmer could code them; second, a chapter on Sakata's Method traces the historical origin of several key patterns; third, and most distinctively, Morris describes exactly how he coded trend determination and pattern identification for a computer, then reports the actual success/failure statistics of every pattern across the S&P 100 and 41 CSI perpetual futures contracts, followed by a chapter showing how filtering candle signals with conventional oscillators (RSI, stochastics, CCI, MACD, Bollinger %B) improves results. The pattern catalogue and its reliability statistics are detailed further in the system sub-page [[greg-morris-candlestick-charting-explained--pattern-catalogue-and-reliability]].

## Core thesis

Candlestick patterns encode short-term (one-to-ten-day) trader psychology at trend turning points, and while they were traditionally read subjectively, they can be given objective, numeric recognition rules and then tested like any other technical signal — and when tested, most individual patterns are only marginally reliable on their own (roughly half succeed by Morris's own ranking criteria), continuation patterns are held to a stricter bar than reversal patterns because trends already tend to continue, and a small number of patterns (occurring only once or twice in the data) cannot be judged statistically at all. The practical payoff is that filtering candle signals with a conventional overbought/oversold indicator's "pre-signal area" consistently improves results versus using either candles or the indicator alone, by reducing trade count and raising average gain per trade.

## Key concepts

- **Long day / short day** — a candlestick body (open-to-close range) that is large or small relative to the most recent 5-10 days; the threshold is contextual, not fixed, though a numeric percentage-of-price or percentage-of-range minimum can be set.
- **Marubozu** — a long body with no shadow at one or both ends; White Marubozu is a strong bullish line, Black Marubozu a strong bearish line, and Closing/Opening Marubozu variants have only one shadow missing.
- **Doji** — a day where open and close are equal or nearly so (within a small percentage of the day's range); subtypes include Long-Legged, Gravestone (open/close at the low), and Dragonfly (open/close at the high) Doji.
- **Trend determination** — Morris's chosen method is a 10-day exponential moving average of closing price; a close above it defines an uptrend, below it a downtrend, and this trend context is required before most patterns can even be classified as valid signals.
- **Reverse Current Trend / Continue Current Trend** — the book's two baseline "success" benchmarks: a reversal pattern is compared against the base rate of trend reversal (which is inherently below 50% since trends tend to persist), while a continuation pattern is compared against the (higher) base rate of trend continuation, making continuation patterns hold a tougher bar to add value.
- **Prediction interval** — the number of days after a pattern's completion used to score it as a success or failure; the book tests 3-, 5-, and 7-day intervals and finds many patterns' rankings shift materially across them.
- **Ranking score** — a pattern's success rate measured relative to its appropriate baseline (Reverse or Continue Current Trend), not raw success percentage; this is why some continuation patterns show high raw success but a negative ranking score.
- **Filtering / pre-signal area** — the zone an oscillator (RSI, %K/%D stochastic, CCI, MACD, %B) occupies before it actually fires its own buy/sell signal; a candle pattern occurring while the relevant indicator is in its pre-signal area is treated as a higher-confidence "filtered" signal.
- **Sakata's Method** — the historical trading approach attributed to the 18th-century rice trader Munehisa Homma, credited as the origin of several classic multi-day patterns (Three White Soldiers, Three Black Crows, and related formations).

## Rules and setups

The book's tradable content is a large pattern catalogue plus a statistically tested filtering overlay (both detailed in [[greg-morris-candlestick-charting-explained--pattern-catalogue-and-reliability]]); representative numeric rules include:

1. **Hammer / Hanging Man**: small real body at the top of the day's range; long lower shadow at least twice (up to three times) the body's length; little to no upper shadow (no more than 5-10% of the high-low range); confirmation required via a higher close the following day. A lower shadow of 3x the body or more reclassifies it as the more bullish Takuri line.
2. **Engulfing Pattern**: a trend must be underway; the second day's real body must completely engulf the first day's real body (both top and bottom cannot be equal to the first day's, though one may be); first day's color matches the prior trend, second day's color is opposite; penetration of at least 30% beyond the first day's body strengthens the signal.
3. **Piercing Line / Dark Cloud Cover**: both are two-day patterns requiring a long body on day one in the direction of the trend; day two must open beyond day one's extreme (below the low for Piercing, above the high for Dark Cloud Cover) and close within — and on the favorable side of — the midpoint of day one's body. There is no flexibility on the 50%-penetration requirement; less penetration reclassifies the pair as a weaker continuation pattern (On Neck, In Neck, Thrusting Line for Piercing's family).
4. **Doji-based signals**: a Doji is only significant when it appears after a run of non-Doji days in an established trend (an isolated Doji after other Doji is not meaningful); a Doji following a long day in the trend direction forms a Star pattern, one of the strongest reversal signals in the catalogue.
5. **Candlestick filtering rule**: define a "pre-signal area" for a chosen oscillator (e.g., RSI 14 with 30/70 or 35/65 thresholds, stochastic %D 14 with 20/80 thresholds); only act on a candle pattern signal when the oscillator is currently within its buy (for bullish patterns) or sell (for bearish patterns) pre-signal zone. In the book's 100-stock test (1989-1992), unfiltered candle-pattern trading averaged 0.40%/trade over 37.1 trades; %D alone averaged 0.02%/trade over 30.1 trades; filtered candles averaged 0.60%/trade over just 13.7 trades — a 50%+ reduction in trade count paired with materially higher average gain.

## Risk and money management

The book gives no explicit stop-loss, position-sizing, or profit-target rules — its statistics (percentage gain per trade, win/loss counts) are always-in-the-market comparisons (buy, sell, sell-short, cover) used purely to compare candle-only, indicator-only, and filtered-candle trading, not a deployable money-management system. Morris explicitly cautions that his simple test calculations exclude commissions and slippage, and that "an average gain of 0.6% would quickly disappear" once real trading costs are included — the relative comparison between methods, not the absolute return figures, is what he asks readers to trust. Position sizing, stops, and portfolio-level risk control are left entirely to the reader to layer on top of whatever entry signal (filtered or unfiltered) is chosen.

## Psychology and discipline

Each pattern's write-up centers on a "Scenarios and Psychology" section explaining the sentiment shift the candle sequence is thought to represent (e.g., a Hanging Man's long lower shadow revealing that sellers briefly took control at the top of an uptrend, unsettling holders even though the close recovered). Morris opens the book with a broader discussion of eyewitness/observational bias (borrowed from the study of crime-scene testimony) to argue that raw pattern recognition is inherently colored by the observer's expectations, which is his stated motivation for reducing patterns to objective, numeric recognition rules that a computer — not a chart-reader's eye — can apply consistently. Discipline in this book means trusting the tested statistical ranking and the filtering overlay over a trader's instinct about which pattern "looks" strong on a chart.

## Chapter map

- Ch 1 — Introduction — observational bias in pattern reading; case for objective, computer-codable rules.
- Ch 2 — Candlestick Lines — single-day constructs: Marubozu, Spinning Tops, Doji variants, Paper Umbrella, Star.
- Ch 3 — Reversal Candle Patterns — the large catalogue of reversal formations (Hammer/Hanging Man, Engulfing, Piercing Line/Dark Cloud Cover, Harami, Three Black Crows/White Soldiers, Morning/Evening Star, and related variants), each with recognition rules and pattern-flexibility notes.
- Ch 4 — Continuation Candle Patterns — Tasuki Gap, On Neck/In Neck/Thrusting Line, Rising/Falling Three Methods, and related continuation formations.
- Ch 5 — Sakata's Method and Candle Formations — historical origin of key multi-day patterns via the Homma family's rice-trading approach.
- Ch 6 — The Philosophy Behind Candle Pattern Identification — trend-determination method (10-day EMA), numeric thresholds for long/short/Doji days, and data/frequency statistics (Table 6-1).
- Ch 7 — Reliability of Pattern Recognition — the statistical test methodology (Reverse/Continue Current Trend baselines, prediction intervals) and full ranking tables for stocks and futures.
- Ch 8 — Candlestick Filtering — combining candle signals with RSI, stochastics, CCI, MACD, Bollinger %B, and other oscillators' pre-signal zones; worked comparative results; introduces CandlePower (volume-integrated) charting.

## Strengths and caveats

The book's central strength — reducing subjective pattern reading to explicit, numeric rules and then actually testing them — is rare in candlestick literature, most of which stays purely descriptive. Morris is unusually candid about limitations: he flags patterns that occurred only once or twice in the test data as statistically meaningless despite showing 100% success, notes that rankings shift substantially across 3/5/7-day prediction intervals (meaning many patterns are not robust to the exact horizon chosen), and explicitly warns that his percentage-gain figures ignore commissions and slippage. The test data (S&P 100 stocks 1989-1992, CSI perpetual futures) is dated and pre-decimalization; tick-based thresholds (e.g., Doji percentage-of-range cutoffs) may need rescaling for modern minimum price increments and different volatility regimes. The book also does not test combining multiple patterns or holding periods beyond a single prediction interval, and its "always in the market" testing convention (used purely for comparison) does not reflect how a real discretionary or systematic trader would size or exit positions.

## Who should read it

Traders and system developers who want candlestick patterns defined precisely enough to code, plus a sense — grounded in actual test statistics rather than folklore — of which patterns are more or less reliable and at which forecast horizons. Less useful as a first introduction to candlestick reading for a purely discretionary chart-watcher (Nison's more narrative treatments serve that purpose better), and the filtering chapter assumes basic familiarity with RSI, stochastics, and similar oscillators.

## Related books in this library

- [[beyond-candlesticks-steve-nison]] — the more narrative, historically detailed treatment of Japanese candlestick technique that this book's numeric-rules approach complements.
- [[big-profit-patterns-using-candlestick-signals-and-gaps-stephen-w-bigalow]] — a practitioner-oriented candlestick pattern guide covering similar formations from a discretionary-trading angle.
- [[candlesticks-fibonacci-and-chart-pattern-trading-tools]] — combines candlestick signals with other chart-pattern tools, similar in spirit to this book's filtering chapter.
- [[john-l-person-swing-trading-using-candlestick-charting-with-pivot-point]] — applies candlestick patterns within a swing-trading framework, a practical extension of the entry signals catalogued here.
- [[candlestick-patterns-for-day-trading]] — adapts candlestick pattern recognition to a shorter, intraday timeframe than this book's daily-bar focus.
