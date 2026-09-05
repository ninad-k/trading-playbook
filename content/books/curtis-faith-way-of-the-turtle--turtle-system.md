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

**N (volatility unit).** True range = max(today's high − today's low, today's high − yesterday's close, yesterday's close − today's low). N = (19 × previous N + today's true range) / 20, a 20-day exponential average of true range, seeded with a 20-day simple average.

**Unit size.** Unit = (1% of account equity) ÷ (N × dollars-per-point), truncated down to a whole contract. Example: $1M account, heating oil N = 0.0141, $42,000/point → unit ≈ 16 contracts.

**Entries — System 1 (S1).** Buy 1 unit on a 1-tick breakout above the 20-day high; sell short on a 1-tick breakout below the 20-day low. Skip a signal if the prior S1 breakout in that market would have won (a profitable 10-day exit reached before moving 2N against it); a skipped S1 signal is replaced by the System 2 (55-day) breakout as a fail-safe.

**Entries — System 2 (S2).** Buy/sell on a 1-tick breakout of the 55-day high/low, taken regardless of the prior signal's outcome. Equity could be split freely between S1 and S2.

**Pyramiding.** Add 1 unit each time price moves ½N further in the trade's favor from the previous fill price, up to 4 units per market.

**Stops.** Initial stop = 2N against entry (≈2% of equity, since 1N ≈ 1%). Each add raises stops on existing units by ½N, so stops generally converge to 2N below the newest unit. An alternative "Whipsaw" variant uses a tighter ½N stop (≈½% risk) and re-enters at the original signal price if stopped out — more trades, lower win rate, but credited with better results for some Turtles.

**Exits.** S1 exits on an opposite 10-day breakout; S2 exits on an opposite 20-day breakout. All units in a position exit together at the earlier of the exit breakout or the (adjusted) stop.

**Position limits.** Max 4 units per market; 6 units (one direction) across closely correlated markets (e.g. heating oil/crude, gold/silver, the currencies as a group); 10 across loosely correlated markets; 12 total long or short portfolio-wide.

**Order handling.** Entries/exits trigger intraday at the breakout/stop price, not on the close; gaps through a signal price fill at the open. Turtles worked orders by hand near the market and waited for brief stabilization before acting in a fast, gapping market.

## Risk

Per-unit risk is bounded near 2% of equity by the 2N stop, and the 4/6/10/12 unit ladder caps aggregate exposure to one market or correlated group. Entries require no confirmation beyond the breakout, so most trades lose; profitability depends on a few large trending winners, and exiting a major trend early can erase a year's return. Documented single-day drawdowns (e.g. the October 1987 rate-cut shock) ran roughly double what backtesting implied — N-based sizing does not protect against gap risk.

## Caveats

Faith's narrative chapters describe System 2 informally as a 60-day breakout, while the formally reprinted rules used here specify 55 days — use 55. The book's other systems (ATR Channel Breakout, Bollinger Breakout, Donchian Trend) are separate, under-specified teaching examples, not part of the original rules. Dollar and contract-size examples reflect mid-2000s futures pricing and should be rescaled for current markets.
