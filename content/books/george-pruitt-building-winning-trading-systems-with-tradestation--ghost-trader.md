---
title: "The Ghost Trader Trading Strategy (Full System)"
author: "George Pruitt, John R. Hill"
year: 2003
slug: george-pruitt-building-winning-trading-systems-with-tradestation--ghost-trader
tier: A
category: "Trend Following & Mechanical Systems"
tags: [trade-filtering, moving-average, rsi, simulated-trading, tradestation-easylanguage]
difficulty: advanced
doc_type: system
parent: george-pruitt-building-winning-trading-systems-with-tradestation
pages: 406
one_liner: "A trade-filtering template that runs a base EMA/RSI system as a hidden paper-trade simulation and only fires a real order when the most recent simulated-or-real trade on that logic was a loser."
related: []
source_file: "George Pruitt-Building_Winning_Trading_Systems_With_Tradestation.pdf"
---

## What it is

A coding template, more than a finished strategy, demonstrating how to make a system's real trade signals depend on the outcome of the prior trade. Some traders believe a loss is more likely to be followed by a win (or vice versa); testing this historically is awkward because "skip the next trade if the last one was a winner" requires tracking hypothetical trades never actually taken. Ghost Trader solves this by running a "ghost" (simulated/paper) copy of a base EMA/RSI system on every bar — tracking a shadow position, entry price, and realized P&L as if every signal had been traded — and only submitting a real order when the most recently closed trade in that shadow record (real or simulated) was a loser.

## Rules

**Base entry/exit logic (the underlying system being filtered)**
1. Long entry: 9-period exponential moving average of closes greater than the 19-period EMA of highs, and the 9-period RSI of closes crossing below 70 → buy stop at today's high, filled next bar.
2. Short entry: 9-period EMA of closes less than the 19-period EMA of lows, and the 9-period RSI of closes crossing above 30 → sell stop at today's low, filled next bar.
3. Exit: a long is liquidated when price breaks the lowest low of the past 20 days; a short is liquidated when price breaks the highest high of the past 20 days.

**Ghost (simulated) tracking — runs every bar regardless of whether a real trade is taken**
4. Maintain `myPosition` (0/1/−1), `myEntryPrice`, and `myProfit` as ordinary variables, not real orders.
5. When yesterday's data would have generated a long signal (condition 1, evaluated one bar back) and today's high confirms the stop would have filled: set `myPosition = 1` and `myEntryPrice` = the greater of today's open or yesterday's high (accounts for a gap-open fill).
6. When a simulated long's 20-day-low exit would have triggered: set `myProfit` = exit price − `myEntryPrice`, and reset `myPosition = 0`. Mirror logic applies to simulated shorts (using the 20-day-high exit and `myEntryPrice` − exit price for `myProfit`).
7. This shadow bookkeeping runs continuously and independently of whether the real system below is currently in a position.

**Real trade-gating logic**
8. Submit a real buy stop at today's high (next bar) only if the base long-entry condition fires AND `myProfit < 0` (the last tracked simulated-or-real trade was a loser).
9. Submit a real sell stop at today's low (next bar) only if the base short-entry condition fires AND `myProfit < 0`.
10. Exit real positions using the identical 20-day high/low breakout rule used for the simulated trades (rule 3).
11. The template is explicitly extensible — the authors note it can be adapted to require two (or more) consecutive simulated losers before re-enabling real trades, or to gate on winners instead of losers if that is the hypothesis being tested.

## Risk

No position sizing, stop-loss distance, or account-level risk rule is specified — Ghost Trader is a filtering layer bolted onto a base system's existing entries and 20-day breakout exits, inheriting that base system's risk profile entirely. In the authors' illustrative 2000-2002 comparison on a single instrument, taking every base signal produced a mix of wins and losses across roughly a dozen trades; filtering to "only trade after a loser" produced fewer total trades but a higher realized net result in that sample (several of the base system's losers were the ones skipped, while its winners were largely preserved).

## Caveats

The authors are explicit this is a coding demonstration of a trade-filtering technique, not a validated system: the "losses cluster and reverse" premise is asserted, not statistically tested, and the one illustrative backtest window is far too short (and un-replicated across markets) to generalize from. EasyLanguage has no built-in way to identify which entry rule triggered a position, so the shadow-tracking code must reconstruct gap-open fills and exits manually — a source of subtle bugs if adapted carelessly. Because the base system's entry and exit are not otherwise validated here, any performance gain from the "trade only after a loss" filter is confounded with the base system's own edge or lack of one.
