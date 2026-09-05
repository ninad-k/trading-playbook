---
title: Inside Day Breakout Play
author: Kathy Lien
year: 2006
slug: day-trading-the-currency-market--inside-day-breakout
tier: A
category: Day Trading & Scalping
tags: [forex, day-trading, breakout, volatility, inside-day, candlestick]
difficulty: intermediate
doc_type: system
parent: day-trading-the-currency-market
pages: 259
one_liner: "A volatility-contraction breakout strategy: after two or more consecutive inside days, buy or sell the break of the most recent inside day's range with a stop-and-reverse order on the other side."
related: [day-trading-the-currency-market, icwr-forex-trading-strategy]
source_file: "Day Trading the Currency Market.pdf"
---

## What it is

An inside day is a trading session whose high and low are both contained within the prior session's high and low. Two or more consecutive inside days indicate contracting volatility, which the strategy treats as a precursor to a volatility expansion (breakout). The play is a pure price-action/candlestick setup requiring no indicators, though technical context (triangle formations, Fibonacci/moving-average confluence, MACD) can be used to bias the expected breakout direction. It works on daily charts (the primary use case) or hourly charts, and is most effective ahead of major economic releases or the London/U.S. market opens, and in tighter-range pairs (EUR/GBP, USD/CAD, EUR/CHF, EUR/CAD, AUD/CAD) where false breakouts are less frequent.

## Rules

**Setup condition**: identify a currency pair where the daily range has been contained within the prior day's range for at least two consecutive days (multiple inside days strengthen the signal).

**Long setup**:
1. Place a buy order 10 pips above the high of the most recent inside day.
2. Simultaneously place a stop-and-reverse order for two lots at least 10 pips below the low of the nearest inside day (this converts a failed long breakout directly into a short position).
3. Take profit when price reaches double the amount risked, or begin trailing the stop at that point.
4. False-breakout protection: if the stop-and-reverse order triggers, place a new stop at least 10 pips above the high of the nearest inside day, and protect any profit beyond the amount risked with a trailing stop.

**Short setup** (mirror image):
1. Place a sell order 10 pips below the low of the most recent inside day.
2. Simultaneously place a stop-and-reverse order for two lots at least 10 pips above the high of the nearest inside day.
3. Take profit at double the amount risked, or trail the stop from that point.
4. False-breakout protection: if the stop-and-reverse order triggers, place a new stop at least 10 pips below the low of the nearest inside day.

**Directional bias (optimization)**: favor the breakout direction suggested by the developing chart pattern — e.g., inside days contracting toward the top of a range (ascending triangle) favor an upside breakout; contracting toward the bottom (descending triangle) favor a downside breakout. Significant support/resistance (Fibonacci levels, moving averages) beneath the inside-day zone raises the odds of an upside breakout or a false downside break.

## Risk

Because entries and initial stops are set relative to the (often wide) daily inside-day range rather than a fixed pip count, risk per trade is generally higher than the other strategies in the book — the source text explicitly notes "the risk is generally pretty high if done on daily charts." The stop-and-reverse structure means a failed breakout automatically flips the position rather than simply exiting, which limits whipsaw cost but doubles position exposure at the reversal point. Profit potential following a genuine breakout tends to be large, and these breakouts are described as frequent precursors to sustained trend moves, which is why trailing stops (rather than fixed targets) are recommended for the aggressive portion of the trade.

## Caveats

Worked examples (EUR/GBP, NZD/USD, EUR/CAD) include at least one case where the initial breakout failed and the stop-and-reverse triggered before the eventual trend materialized — illustrating that false breakouts are a real, not hypothetical, risk even with the reversal safeguard. The rule for how many pips constitute "at least two" inside days versus a stronger multi-day contraction is left to judgment rather than a strict count threshold. As with the book's other setups, the examples are a small hand-picked sample from 2004–2005 data, not a systematic backtest.
