---
author: George Pruitt, John R. Hill
category: Trend Following & Mechanical Systems
difficulty: intermediate
doc_type: manual
one_liner: A Donchian-style breakout system that adapts its look-back length daily
  to market volatility, adding a Bollinger Band filter and dynamic trailing stop.
pages: 8
related:
- king-keltner-trading-strategy
- money-management-in-trading
reviewed_pdf_pages: 1-8
slug: dynamic-breakout-ii-strategy
source_file: Dynamic_Breakout_II_Strategy.pdf
source_review: full
tags:
- breakout
- donchian-channel
- volatility
- adaptive-parameters
- bollinger-bands
- trend-following
- seasonality
tier: B
title: The Dynamic Break Out II Strategy
year: 2002
---

## Summary

An excerpt from "Building Winning Trading Systems with TradeStation" describing an upgraded version of George Pruitt's 1996 Dynamic Break Out system for Futures Magazine. The core idea is a Donchian channel breakout (buy on a new N-day high, sell on a new N-day low) where N ("look-back days") is not fixed but adapts daily based on the percentage change in 30-day standard deviation of closing prices: rising volatility widens the look-back (making entry harder, since indecisive/choppy markets shouldn't trigger trades easily), falling volatility narrows it (making entry easier in a trending market). The look-back is bounded between 20 and 60 days. Version II adds an adaptive Bollinger Band filter on top of the breakout (yesterday's close must also be outside the band before a new signal fires) and replaces the original's flat $1,500 stop with a dynamic trailing stop set at the moving average of closing prices over the same adaptive look-back window. A 1982–2002 backtest across 17 futures markets (commissions/slippage $75) produced $452,504 total net profit and 1,820 trades; performance in grain markets (soybeans, wheat, corn) was poor or negative, which the authors attribute to seasonal/cyclical behavior that a pure trend-following breakout can't capture — illustrated with a soybean "fade" experiment and a March–July/July–February seasonal long/short filter.

## Key points

- Base logic: Donchian breakout — buy on a new N-day high, sell on a new N-day low, but N changes daily via an adaptive volatility engine instead of staying fixed.
- Look-back bounds: 20 days minimum, 60 days maximum, starting at 20 on bar 1.
- Volatility input: 30-day standard deviation of closing prices; % change from yesterday's to today's volatility is applied directly as the % change to the look-back length.
- Bollinger Band filter (added in version II): band width = length-adaptive moving average of closes ± 2.0 standard deviations over the same adaptive look-back; a long requires yesterday's close above the upper band AND today's high ≥ the N-day high; short is the mirror condition.
- Exit/stop: dynamic trailing stop = simple moving average of closes over the current adaptive look-back (replacing the original system's flat $1,500 money-management stop).
- Backtest (1982–2002, 17 futures markets, $75 commission/slippage): total net profit $452,504 over 1,820 trades; strongest results in currencies (Japanese Yen +$118,200, Swiss Franc +$57,338, Deutsche Mark +$49,088) and bonds; weakest/negative in grains (Copper −$25,175, Soybeans −$9,681, Live Cattle −$17,397, Wheat −$14,831).
- A "fade" experiment (reversing every signal) on soybeans still lost money overall (−$1,681 net over 128 trades, 64% win rate but poor average win/loss ratio), suggesting the grain underperformance isn't simply solved by trading the opposite side.
- A seasonal filter tested on soybeans (long only March 1–July 1, short only July 2–February 28, based on cyclical/seasonal analysis) also lost money in a 1996–2002 test (−$4,363 net, 36% win rate), showing seasonality alone didn't fix the grain-market problem either.

## Actionable rules

1. Initialize look-back length to 20 days; each day, compute deltaVolatility = (today's 30-day StdDev of closes − yesterday's) ÷ today's 30-day StdDev, then lookBackDays = lookBackDays × (1 + deltaVolatility), clipped to [20, 60].
2. Compute upBand/dnBand as a Bollinger Band (± 2.0 std dev) of closes over the current look-back length.
3. Enter long the next bar at a stop equal to the N-day highest high, but only if yesterday's close was above the upper Bollinger Band; enter short at the N-day lowest low only if yesterday's close was below the lower band.
4. Exit a long when price trades at or below the moving average of closes over the current look-back (liquidation point); exit a short at or above the same moving average.
5. Treat this as a long-term trend-following system requiring diversification across multiple markets — the authors explicitly note it needs heavy capitalization and can go years without profit in any single market.

## Caveats

Backtest uses static $75 commission/slippage assumptions and a fixed 1982–2002 window without out-of-sample validation or walk-forward testing; results are shown per-market rather than as a portfolio equity curve, so combined drawdown and correlation effects across the 17 markets are not demonstrated. The system reliably underperforms in grain/agricultural markets per the authors' own admission, and neither the fade nor the seasonal-filter fix tested in the source resolved this. As with most channel breakout systems, it is vulnerable to failed breakouts in choppy, low-trend regimes.

## Who it is for

Systematic futures traders comfortable coding TradeStation EasyLanguage strategies who want a volatility-adaptive alternative to a fixed-parameter Donchian channel system, applied across a diversified basket of markets rather than any single instrument.
