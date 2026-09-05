---
title: "Simple Moving Average Crossover System"
author: "John R. Hill, George Pruitt, Lundy Hill"
year: 2000
slug: j-r-hill-g-pruitt-and-l-hill-the-ultimate-trading-guide--moving-average-crossover-system
tier: A
category: Trend Following & Mechanical Systems
tags: [moving-average, trend-following, mechanical-systems, futures, atr-stop]
difficulty: intermediate
doc_type: system
parent: j-r-hill-g-pruitt-and-l-hill-the-ultimate-trading-guide
pages: 302
one_liner: "A 13/39-day moving-average crossover with a 40-day close filter and a 5x-ATR initial and trailing stop, backtested 1983-1999."
related: [curtis-faith-way-of-the-turtle, turtletrader, macd]
source_file: "J R Hill G Pruitt And L Hill - The Ultimate Trading Guide.pdf"
---

## What it is

A fully mechanical, long-term trend-following system from Chapter 9, the book's "Donchian and moving-average" style example. It buys or sells on a crossover of a 13-day and 39-day simple moving average of closes, gated by a 40-day close filter to avoid signals against the larger trend. Risk is defined entirely by a volatility-scaled stop built from the 20-day average true range (ATR), so both the initial and trailing stop widen or narrow with current volatility rather than a fixed dollar amount. The authors chose 13/39/40/5-ATR as reasonable, un-optimized defaults, and back-tested it one-contract-per-trade across a futures portfolio, 1/1/1983-8/31/1999, $75 commission/slippage assumed per round turn.

## Rules

**Entry (long)**: buy on the open when the 13-day MA of closes crosses from below to above the 39-day MA, and yesterday's close exceeds the close 40 trading days ago.

**Entry (short)**: sell on the open when the 13-day MA crosses from above to below the 39-day MA, and yesterday's close is less than the close 40 trading days ago.

**Initial stop**: calculate the ATR over the past 20 days (true range = max(high, prior close) - min(low, prior close), not simply high - low); set the initial stop at 5x this 20-day ATR from entry.

**Trailing stop**: once the trade is 5 ATRs into profit, trail a stop 5 ATRs behind the high (longs) or low (shorts) of the day that first reached that threshold, recalculating the distance as the 20-day ATR evolves.

**Stop selection**: use whichever stop is closer to the market — the protective stop, the trailing stop (once activated), or the reversal stop implied by the opposite crossover signal.

**Reversal**: if the opposite crossover-plus-filter condition triggers while a position is open, exit and reverse on that signal rather than waiting for a stop to be hit separately.

**Position sizing**: the backtest uses one contract per trade per market; sizing beyond that is left to the Capital Allocation Model (equity x acceptable risk % / current ATR-based market risk).

## Risk

Risk per trade is intentionally wide (5x a 20-day ATR) because the entry is a long-term trend filter — a market crossing two multi-week moving averages is expected to move against the position by more than one or two ATRs before the trend asserts itself, so a tight stop would cause premature whipsaw exits. The trade-off is a lower win rate: this style of system typically wins under 50% of trades, relies on a handful of large winners to offset frequent small losses, and strings together consecutive losers when a market is range-bound (~85% of the time, by the book's own market-stage framework). No fixed profit target is used; profits run until the trailing stop or an opposite signal exits. Because the stop is volatility-scaled, dollar risk varies significantly across markets and over time as ATR expands and contracts.

## Caveats

The 13/39/40/5 parameter set is explicitly a reasonable, un-optimized starting point, not a curve-fit result, so backtested performance is illustrative rather than a forward-edge claim. Results are one-contract-per-market and pre-diversification; the book's own portfolio chapter shows drawdown falls faster than profit when combined with anti-correlated markets and systems, so single-market numbers understate what diversified deployment could achieve. Results are tested only through August 1999 on futures data with $75 commission/slippage assumed — no exchange-fee, margin, or rollover mechanics are discussed in the rule set itself.
