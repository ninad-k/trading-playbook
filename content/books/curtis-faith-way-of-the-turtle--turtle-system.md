---
title: The Original Turtle System (Faith's Account)
author: Curtis M. Faith
year: 2007
slug: curtis-faith-way-of-the-turtle--turtle-system
tier: A
category: Trend Following & Mechanical Systems
tags: [turtle-trading, trend-following, breakout, atr, position-sizing, pyramiding, stops]
difficulty: intermediate
doc_type: system
parent: curtis-faith-way-of-the-turtle
pages: 313
one_liner: "Faith's own reprint of the Turtles' N-based sizing, System 1/System 2 breakout entries, 2N stops, and 1/2N pyramiding, as he traded it."
related: [the-complete-turtletrader-the-legend-the-lessons-the-results--turtle-trading-system, turtlerules, position-sizing]
source_file: "Curtis Faith - Way of the Turtle.pdf"
---

## What it is

The mechanical breakout system taught to the Turtles by Richard Dennis and William Eckhardt, reprinted here from Curtis Faith's own copy of the rules. It combines two Donchian-style breakout entry variants with an ATR-based ("N") volatility unit that drives both position size and stop distance. It is presented as market-agnostic and was traded unchanged across roughly 20 futures markets. Compare [[the-complete-turtletrader-the-legend-the-lessons-the-results--turtle-trading-system]] for a second, independently sourced account of the same rules and [[turtlerules]] for the underlying written rules document.

## Rules

**N (volatility unit).** True range = max(today's high − today's low, today's high − yesterday's close, yesterday's close − today's low). N = (19 × previous N + today's true range) / 20, a 20-day exponential average of true range; seed it with a 20-day simple average of true range.

**Unit size.** Dollar volatility = N × dollars-per-point for the contract. Unit size = (1% of account equity) ÷ dollar volatility, truncated down to a whole number of contracts. Example: $1,000,000 account, heating oil N = 0.0141, $42,000/point → unit size = (0.01 × $1,000,000) ÷ (0.0141 × 42,000) ≈ 16.9 → 16 contracts.

**Entries — System 1 (S1).** Buy 1 unit on a 1-tick breakout above the 20-day high; sell 1 unit short on a 1-tick breakout below the 20-day low. Skip an S1 signal if the prior S1 breakout in that market (taken or not) would have been a winner — defined as reaching a profitable 10-day exit before moving 2N against the position. A skipped S1 signal is replaced by the System 2 (55-day) breakout as a fail-safe entry.

**Entries — System 2 (S2).** Buy 1 unit on a 1-tick breakout above the 55-day high; sell 1 unit short on a 1-tick breakout below the 55-day low. All S2 signals are taken regardless of the outcome of the prior signal. Traders could allocate equity freely between S1 and S2 (all-S2, a 50/50 split, or other mixes).

**Pyramiding.** Add 1 unit each time price moves ½N further in the trade's favor from the previous unit's actual fill price, up to 4 units total in a single market (it was possible to reach the 4-unit maximum in a single fast day).

**Stops.** Initial stop = 2N against the entry (this caps unit risk at roughly 2% of equity, since 1N ≈ 1%). As units are added, raise stops on all existing units by ½N per add, so stops generally converge to 2N below the most recently added unit. An alternative "Whipsaw" variant uses a tighter ½N stop (≈½% risk) and re-enters at the original signal price if stopped out — more trades and a lower win rate, but the book credits it with better results for some Turtles.

**Exits.** S1 positions exit on an opposite 10-day breakout (10-day low for longs, 10-day high for shorts); S2 positions exit on an opposite 20-day breakout. All units in a position exit together at the earlier of the exit-breakout signal or the (adjusted) stop.

**Position limits.** Maximum 4 units in a single market; 6 units total (one direction) across closely correlated markets (e.g. heating oil/crude oil, gold/silver, the currencies as a group); 10 units across loosely correlated markets; 12 units total long or short across the whole portfolio.

**Order handling.** Entries and exits are triggered intraday at the breakout/stop price, not on the close; opening gaps through a signal price are filled at the open. Turtles generally worked orders by hand near the market rather than resting visible stops, and were told to wait for at least a brief stabilization before acting in a fast, gapping market.

## Risk

Per-unit risk is bounded at roughly 2% of equity by the 2N stop, and the 4/6/10/12 unit ladder caps aggregate exposure to any one market or correlated group. Because entries require no confirmation beyond the breakout, most trades lose money (a documented example: exiting winners at 1N and losers at 2N requires twice as many winners as losers just to break even); profitability depends on a small number of large trending winners, so missing or exiting a major trend early can eliminate a year's return. The book documents single-day drawdowns (e.g. the October 1987 rate-cut shock) roughly double what historical backtesting had implied, underscoring that N-based sizing does not protect against gap risk.

## Caveats

Faith's early narrative account (Chapter 3) describes System 2 informally as a 60-day breakout, while the formal reprinted rules used here specify 55 days — use 55 days as the rule. The book also presents several looser, illustrative variants (ATR Channel Breakout, Bollinger Breakout, Donchian Trend) elsewhere as teaching examples; those are not part of the original Turtle rules and are under-specified relative to the system above. Dollar and contract-size examples reflect mid-2000s futures pricing and account sizes and should be recalculated for current markets.
