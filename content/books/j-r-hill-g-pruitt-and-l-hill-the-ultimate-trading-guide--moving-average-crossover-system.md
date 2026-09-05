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

A fully mechanical, long-term trend-following system presented in Chapter 9 as the book's example of a "Donchian and moving-average" style approach. It buys or sells on a crossover of a 13-day and 39-day simple moving average of closes, gated by a longer-term 40-day close filter to avoid taking crossover signals against the larger trend. Risk is defined entirely by a volatility-scaled stop built from the 20-day average true range (ATR), so both the initial stop and the trailing stop widen or narrow automatically with current market volatility rather than using a fixed dollar or point amount. The authors chose 13/39/40/5-ATR as reasonable, un-optimized defaults rather than curve-fit parameters, and back-tested it one-contract-per-trade across a futures portfolio from 1/1/1983 to 8/31/1999 with $75 assumed for commission and slippage per round turn.

## Rules

**Entry (long)**: Buy on the open when the 13-day simple moving average of closes crosses from below to above the 39-day simple moving average of closes, AND yesterday's close is greater than the close 40 trading days ago.

**Entry (short)**: Sell on the open when the 13-day moving average crosses from above to below the 39-day moving average, AND yesterday's close is less than the close 40 trading days ago.

**Initial stop**: Calculate the average true range (ATR) over the past 20 days (true range = max(high, prior close) - min(low, prior close), not simply high - low). Set the initial protective stop at 5x this 20-day ATR from the entry price.

**Trailing stop**: Once the trade has moved 5 ATRs into profit (measured against the 20-day ATR calculated at that point), trail a stop 5 ATRs behind the high (for longs) or low (for shorts) of the day that first reached that 5-ATR profit threshold. Recalculate the trailing distance using the current 20-day ATR as it evolves.

**Stop selection**: At any given time, use whichever stop is closer to the market — the original protective stop, the trailing stop (once activated), or the reversal stop implied by the opposite crossover signal.

**Reversal**: If the opposite crossover-plus-filter condition triggers while a position is open, exit and reverse on the same signal (stop-and-reverse), rather than waiting for the trailing/protective stop to be hit separately.

**Position sizing**: The book's backtest uses one contract per trade per market; sizing beyond that is left to the money-management chapter's Capital Allocation Model (equity x acceptable risk % / current ATR-based market risk).

## Risk

Risk per trade is intentionally wide (5x a 20-day ATR) because the entry signal is a long-term trend filter — a market crossing two multi-week moving averages is expected to move against the position by more than one or two ATRs before the trend asserts itself, so a tight stop would simply cause premature whipsaw exits. The trade-off is a lower win rate: the authors note trend-following systems of this style typically win less than 50% of trades, rely on a handful of large winners to offset frequent small losses, and are prone to long strings of consecutive losers when a market is range-bound rather than trending (roughly 85% of the time by the book's own market-stage framework). No fixed profit target is used — profits are allowed to run until the trailing stop or an opposite signal exits the trade. Because the stop is volatility-scaled rather than fixed, position risk in dollar terms will vary significantly across markets and over time as ATR expands and contracts.

## Caveats

The 13/39/40/5 parameter set is explicitly presented as a reasonable, un-optimized starting point, not an optimized or curve-fit result, so backtested performance should be treated as illustrative rather than a claim of forward edge. Results are shown one-contract-per-market and pre-diversification; the book's own portfolio chapter shows drawdown falls faster than profit when this system is combined with anti-correlated markets and systems, so single-market results understate what a diversified deployment could achieve (and single-market drawdown numbers should not be read as portfolio-level risk). As with all the book's trend-following systems, results are only tested through August 1999 on futures data with $75 commission/slippage assumed — no exchange-fee, margin, or contract-rollover mechanics are discussed in the rule set itself.
