---
title: "241 Forex: Trading Systems Built to Change and Adapt to the Trader"
author: Carl (241Forex.com)
year: 2006
slug: 241forex
tier: B
category: Forex Mechanics & Macro Drivers
tags: [forex, swing-trading, intraday, weekly-pivots, position-sizing, trend-following]
difficulty: intermediate
doc_type: manual
pages: 21
one_liner: "Two rule-based forex systems (weekly Swing Trade Equation and daily Intraday Trade Equation) with three risk tiers of entries, stops, and pip targets."
related: [big-ben-breakout, forex-intraday-pivots-trading-system-complete-system]
source_file: "241FOREX.pdf"
---

## Summary

A short forex trading manual presenting two mechanical systems built from prior weekly or daily OHLC data entered into a spreadsheet formula, generating long/short trigger prices. The Swing Trade Equation uses three prior weeks of data to trigger one trade per week, with exits/stops scaled to three trader risk profiles. The Intraday Trade Equation uses the prior day's OHLC to trigger at most one trade per day, closed out same-day.

## Key points

- **Currency pairs used** — EUR/USD, EUR/CHF, EUR/GBP, USD/CHF, USD/CAD, GBP/USD; EUR/USD recommended as most consistently volatile.
- **Swing system trend filter** — only take a long/short if the last three weekly closes are in ascending/descending order (last week > 2 weeks ago > 3 weeks ago, or the reverse).
- **Three trader risk tiers** — Trader 1 (new, smallest size, safety stop), Trader 2 (moderate), Trader 3 (aggressive, largest target/stop, allows averaging in).
- **Safety stop** — for Trader 1 (swing) and Trader 2/3 optionally: if price moves 20 pips (Trader 1) or more in favor then returns to entry, exit flat to protect capital.
- **Intraday trigger-value filter** — only take the intraday trade if the calculated trigger value falls between .0065 and .0150 (USD/JPY: between .15 and .35); whichever side (long/short) has the larger valid trigger value is taken.
- **Best trading hours** — EUR/USD: London and New York hours; GBP/USD: late Tokyo into London/New York; no new intraday entries after the 4:00 p.m. EST New York close.

## Actionable rules

1. Swing system entry: long only if last week's close > 2-weeks-ago close > 3-weeks-ago close (mirror for short); one trade per week, only in the "trade week."
2. Swing exits (profit targets): Trader 3 = 200+ pips; Trader 2 = 110 pips; Trader 1 = 75 pips.
3. Swing stops: Trader 3 = 75 pips; Trader 2 = 35 pips; Trader 1 = 25 pips, plus a 20-pip safety stop (exit flat if price retraces to entry after a 20-pip favorable move).
4. Swing averaging-in (Trader 2/3 only): Trader 3 adds 2 contracts if trade moves 50 pips against entry, then sets stop at −75 pips on the whole position; Trader 2 adds 2 contracts at −20 pips against entry, sets stop at −40 pips on the whole position.
5. Intraday entry: take the first (only) daily trigger that falls within the trigger-value band (.0065–.0150, or .15–.35 for USD/JPY); target 25 pips, stop 15 pips, with a 10-pip safety stop.
6. No new intraday trades after 4:00 p.m. EST (New York close).

## Caveats

The system's exact entry/trigger-price formula depends on a proprietary spreadsheet not reproduced in the manual (only a partial description and example numbers are given), so the rules above are not fully codable without that spreadsheet. No backtest statistics, win rate, or sample results are provided — only the mechanical rules themselves. Written circa 2005-2006; broker margin, spread, and liquidity conditions referenced are dated.

## Who it is for

Retail forex traders wanting a simple, mechanical trend-following weekly system plus a companion intraday breakout-style system, with built-in risk tiers for different account sizes and experience levels.
