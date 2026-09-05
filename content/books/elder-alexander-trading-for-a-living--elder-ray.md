---
title: Elder-ray (Bull Power / Bear Power)
author: Alexander Elder
year: 1993
slug: elder-alexander-trading-for-a-living--elder-ray
tier: A
category: Indicators
tags: [elder-ray, bull-power, bear-power, divergence, ema, oscillator]
difficulty: intermediate
doc_type: system
parent: elder-alexander-trading-for-a-living
pages: 312
one_liner: "Two histograms — Bull Power and Bear Power — built off a 13-day EMA, used to spot divergences that mark trend turns."
related: [come-into-my-trading-room-elder-alexander]
source_file: "Elder Alexander - Trading For A Living.pdf"
---

## What it is

Elder-ray is Elder's own indicator pair, named after X-rays, meant to "see through" a price bar and reveal the relative strength of bulls and bears within it. It is built on a 13-day exponential moving average (EMA) of closing price, taken as the market's running consensus of fair value. Bull Power measures how far the day's high manages to push above that average; Bear Power measures how far the day's low is pushed below it. The two are plotted as histograms above and below a zero line, alongside the 13-day EMA on the price chart.

## Rules

**Calculation**: 
- 13-day EMA of closing price, plotted on the price chart.
- Bull Power = day's High − 13-day EMA.
- Bear Power = day's Low − 13-day EMA.

Bull Power is positive when the day's high closes above the EMA (bulls able to lift price above consensus value) and can turn negative in a strong downtrend when even the day's high fails to reach the EMA. Bear Power is negative when the day's low closes below the EMA (bears able to push price under consensus value) and can turn positive in a strong uptrend when even the day's low stays above the EMA.

**Trend confirmation filter**: use the slope of the 13-day EMA itself as the primary trend read; only act on Elder-ray signals in the direction confirmed by the EMA's slope (rising EMA favors long signals, falling EMA favors short signals).

**Bullish divergence (buy signal)**: price makes a new low, but Bear Power's low on that bar is more shallow (less negative) than Bear Power's low on the prior price low. Confirm the signal once the 13-day EMA turns up.

**Bearish divergence (short signal)**: price makes a new high (or matches the prior high), but Bull Power's peak on that bar is lower than its peak on the prior price high. Confirm the signal once the 13-day EMA turns down.

**Pyramiding/re-entry signal within an established trend**: in a downtrend, when Bull Power ticks up into positive territory and then turns back down, place an order to sell short below the low of that last bar (an entry to add to or re-enter a short position in the direction of the confirmed downtrend). Mirror the logic for uptrends using Bear Power ticking down into negative territory and then turning back up, to add to or re-enter longs.

## Risk

No dedicated position-sizing rule is given for Elder-ray specifically; treat it as a timing/entry filter used alongside the parent book's general 2% Rule (risk no more than 2% of account equity per trade, inclusive of costs) for sizing whatever entry the divergence or re-entry signal generates. Because Elder-ray is a divergence-based indicator, its signals are inherently lagging confirmations rather than leading predictions — the divergence is only visible after the second low or high has printed, and the 13-day EMA slope confirmation adds further lag before a trade is taken.

## Caveats

Elder-ray is proprietary to Elder; the book illustrates it with annotated chart examples (a COMEX gold chart showing a bearish divergence in June–July and a bullish divergence in September) rather than a systematic, quantified backtest, so its historical hit rate and expectancy are not established in the text. The indicator depends entirely on the 13-day EMA period Elder selected for this book; no sensitivity testing of that parameter is presented. This page is based on the sampled OCR pages around p.240 (the worked chart example and divergence rules) of a scan where most page ranges were not sampled; the exact formula lines (Bull Power = High − EMA, Bear Power = Low − EMA) are stated in the source's figure/caption text and are consistent with the same indicator as documented in Elder's later book, [[come-into-my-trading-room-elder-alexander]].
