---
title: Triple Screen Trading System
author: Alexander Elder
year: 2002
slug: come-into-my-trading-room-elder-alexander--triple-screen
tier: A
category: Trading Psychology & Discipline
tags: [triple-screen, multi-timeframe, trend-following, oscillators, force-index]
difficulty: intermediate
doc_type: system
parent: come-into-my-trading-room-elder-alexander
pages: 322
one_liner: "Three-timeframe method: trend-following indicators on a long-term chart pick direction, oscillators on the intermediate chart time entries, and a third screen places the order."
related: []
source_file: "Come Into My Trading Room - Elder Alexander.pdf"
---

## What it is

Triple Screen resolves conflicts between trend-following indicators and oscillators, and between different chart timeframes, by imposing a strict sequence: analyze a long-term chart for direction (strategic decision), an intermediate chart for timing (tactical decision), and use a third method to place the actual entry order. It was originally developed by Elder in the mid-1980s and updated in this book with newer indicator choices (weekly EMA slope in place of weekly MACD-Histogram slope as the primary Screen One signal, and Force Index as a Screen Two option).

## Rules

**Choosing timeframes**: pick a favorite ("intermediate") timeframe — e.g., daily. Multiply its length by 5 to get the "long-term" timeframe — e.g., weekly. A day-trader using a 10-minute intermediate chart would use an hourly long-term chart; a long-term investor using weekly as intermediate would use monthly as long-term.

**Screen One (strategic, long-term chart)**: apply a trend-following indicator. Elder's current preference is the slope of a 26-week EMA (roughly half a year): rising EMA → trade long or stand aside only; falling EMA → trade short or stand aside only. Also plot weekly MACD-Histogram; when its slope agrees with the EMA, treat the trend as stronger and size up; a divergence between weekly MACD-Histogram and price overrides the EMA signal.

**Screen Two (tactical, intermediate chart)**: only take oscillator signals in the direction of the Screen One trend.
- When the weekly trend is up, wait for a daily oscillator to dip and reverse up: for conservative traders, wait for daily MACD-Histogram to fall below zero and tick up, or Stochastic to reach its lower reference line; for active traders, wait for the 2-day EMA of Force Index to fall below zero.
- When the weekly trend is down, wait for the mirror-image sell signal (daily MACD-Histogram ticks down from above zero or Stochastic reaches its upper reference line; or the 2-day EMA of Force Index rallies above zero).
- An oscillator signal against the weekly trend may be used to take profits on an existing position but never to open a new counter-trend trade.

**Screen Three (entry placement)**: two options.
1. Without live data — when the first two screens agree bullish, place a buy order at the previous day's high (or one tick above), good for one day, to catch an upside breakout in the direction of the long-term trend; mirror with a sell order at the previous day's low (or a tick below) for bearish setups. Alternatively, buy a pullback to the rising daily EMA, or use the SafeZone indicator to estimate how far price is likely to dip below the previous low and place the order there.
2. With live/intraday data — enter on an opening-range breakout (e.g., above the high of the first 15–30 minutes for longs) or apply the same technique on an intraday chart; exits should still be governed by the weekly/daily analysis that generated the trade, not by intraday noise.

**Stop and target placement (Screen Two)**: set the stop before entering; it may never risk more than 2% of account equity (see the 2%/6% Rules in the parent book). Profit targets: exit on the daily chart hitting its upper (long) or lower (short) channel line, or exit when the weekly EMA turns flat/reverses for a longer-term-oriented trader, or use the 2-day EMA of Force Index turning against the position for a short-term exit.

## Risk

Every Triple Screen trade must pass the 2% Rule before being placed: if a logical stop derived from Screen Two would risk more than 2% of equity, skip the trade rather than widening the stop. Because entries are always taken with the long-term trend, stops sit on the countertrend side of recent noise (use SafeZone to gauge noise distance). Pyramiding additional entries in the same direction is allowed as long as each addition is sized under the 2% limit and total open risk stays under the 6% monthly ceiling.

## Caveats

Triple Screen is explicitly described by Elder as "a method of trading rather than a mechanical system" — indicator choice, parameter lengths, and the exact multiplier for the long-term timeframe are left to the trader to test on their own market, and the book does not present a systematic backtest of the approach. The original 1986 version used weekly MACD-Histogram slope as the primary Screen One signal; this book substitutes the 26-week EMA slope as the author's current preference, so readers of Elder's earlier Trading for a Living will see a parameter change. Works best on trending markets; Elder gives no explicit rule for filtering out range-bound conditions before applying Screen One.
