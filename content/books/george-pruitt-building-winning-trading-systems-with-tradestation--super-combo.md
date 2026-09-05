---
title: "The Super Combo Day Trading Strategy (Full System)"
author: "George Pruitt, John R. Hill"
year: 2003
slug: george-pruitt-building-winning-trading-systems-with-tradestation--super-combo
tier: A
category: "Day Trading & Scalping"
tags: [day-trading, open-range-breakout, failed-breakout, stock-indices, multi-timeframe, tradestation-easylanguage]
difficulty: advanced
doc_type: system
parent: george-pruitt-building-winning-trading-systems-with-tradestation
pages: 406
one_liner: "An intraday stock-index system combining an open-range breakout with failed-breakout reversal logic on 5-minute bars, using daily-bar statistics to set the day's trigger levels."
related: []
source_file: "George Pruitt-Building_Winning_Trading_Systems_With_Tradestation.pdf"
---

## What it is

A day-trading system for stock indices combining two entry concepts the authors say dominate the best-performing day systems tracked by Futures Truth: an open-range breakout (buying/selling a thrust away from the open) and failed-breakout logic (reversing when an initial breakout doesn't hold). It runs on two simultaneous data streams — daily bars to calculate the day's trigger levels, 5-minute bars to place and manage orders — and is presented as a "kitchen sink" template demonstrating TradeStation's multi-timeframe capability as much as a finished edge. No trade is taken in the first 30 minutes, and at most one long and one short attempt are taken per day.

## Rules

**Daily-bar calculations (computed once per day, using the prior day's data)**
1. `averageRange` = 10-day average of (daily High − Low).
2. `averageOCRange` = 10-day average of |Open − Close|.
3. Tradeable-day filter: only trade today if yesterday's |Open − Close| was less than 85% of `averageOCRange` — a small-range bar (SRB) yesterday is treated as a precondition for today's setup; if yesterday was a wide-range bar, skip the day.
4. Classify today as a "buy easier day" if yesterday's close ≤ the close two days ago, else a "sell easier day."
5. On a buy-easier day: `buyBOPoint` = today's open + 30% of `averageRange`; `sellBOPoint` = today's open − 60% of `averageRange`.
6. On a sell-easier day: `sellBOPoint` = today's open − 30% of `averageRange`; `buyBOPoint` = today's open + 60% of `averageRange`.
7. `longBreakPt` = yesterday's high + 25% of `averageRange` (confirms an upside breakout has "achieved" enough follow-through); `shortBreakPt` = yesterday's low − 25% of `averageRange`.
8. `longFBOPoint` = yesterday's low + 25% of `averageRange` (failed-breakout buy level); `shortFBOPoint` = yesterday's high − 25% of `averageRange` (failed-breakout sell level).

**Intraday entries (5-minute bars, using the daily levels above)**
9. Skip the first 30 minutes (first six 5-minute bars).
10. If no long/short taken yet today and time is before 2:30pm CT: buy stop at `buyBOPoint`, sell stop at `sellBOPoint` (initial breakout entries).
11. Failed-breakout entries: if intraday high exceeds `longBreakPt` and no short taken yet, sell short at `shortFBOPoint` (betting the upside thrust fails); mirror for the downside (intraday low below `shortBreakPt` → buy at `longFBOPoint`).
12. Stop-reversal failed breakout: if a long is stopped out, ≥4 bars have passed since entry, and it's before noon CT, allow a short reversal at the long's liquidation point (mirror for a stopped-out short) — catches failures too fast for the intraday-high/low trigger.
13. At most one long and one short attempt per day; once both sides have been tried, stop looking for new entries.

**Exit / trade management**
14. Initial protective stop = entry price minus 25% of `averageRange` or 3.00 full points, whichever is greater (a 3-point floor applies when 25% of range is smaller).
15. If entered via a stop-reversal failed breakout (rule 12), use 15% of `averageRange` instead of 25% for the protective stop, reflecting the entry's higher uncertainty.
16. Move the stop to breakeven once open profit reaches 50% of `averageRange`.
17. After 2:30pm CT, trail the stop to the low (longs) or high (shorts) of the prior three 5-minute bars, anticipating the tendency for moves to fade late in the session.
18. Exit all open positions at the close (no overnight holds).

## Risk

No percent-of-equity position sizing is given; risk per trade is set by the protective-stop distance (25% or 15% of the 10-day average daily range, floored at 3 points). In a 2001-2002 S&P backtest ($100 commission/slippage), the system made $27,175 net over 155 trades (38% win rate, average win $2,148 vs. average loss $1,037, 2.07 win/loss ratio, $13,725 max intraday drawdown). A longer 1986-2002 test (via the authors' Excalibur software) showed $188,913 total profit over 2,129 trades, 42.4% win rate, 1.3 profit-to-loss ratio, and 24% time-in-market — consistent with a selective approach rather than one constantly positioned.

## Caveats

Presented explicitly as "the kitchen sink day trader" — a demonstration of technique (multi-data-stream programming, modular trade-management state machines) more than a polished strategy; the authors did no optimization before publishing results. The trade-management logic is the most complex in the book, with interacting special cases (tracking which entry type triggered a position to pick the right stop percentage) that are easy to mis-implement. Backtests use only a few years of intraday data on a single instrument (S&P/stock indices), so the 17-market, 20-year validation applied elsewhere in the book does not apply here.
