---
title: "Wiggle Breakout System"
author: Barry Rudd
year: 1998
slug: barry-rudd-stock-patterns-for-day-trading-and-swing-trading--wiggle-breakout-system
tier: A
category: Day Trading & Scalping
tags: [breakout, consolidation, trailing-stop, wiggle, stop-loss, tape-reading]
difficulty: intermediate
doc_type: system
parent: barry-rudd-stock-patterns-for-day-trading-and-swing-trading
pages: 196
one_liner: "Rudd's core method: buy or sell the breakout of a tight multi-bar consolidation on the 5-minute chart, then manage the trade with a fixed 1/4-point stop that converts to a stock-specific 'wiggle' trailing stop."
related: [barry-rudd-stock-patterns-for-day-trading-and-swing-trading, turtlerules, curtis-faith-way-of-the-turtle]
source_file: "Barry Rudd - Stock Patterns For Day Trading And Swing Trading.pdf"
---

## What it is

A discretionary-but-rule-bounded intraday breakout method built on two ideas: trade the break of a tight, multi-bar price consolidation on a 5-minute chart, then give the position room to breathe using the stock's own historical average pullback size — its "standard wiggle" — rather than an arbitrary fixed profit target. The same consolidation-then-breakout logic is applied to daily bars for multi-day swing trades.

## Rules

1. **Screen the stock.** Average daily volume of at least 100,000 shares; market-maker bid/ask spread of about 1/8 point (occasionally 1/4); at least 4+ market makers quoting at each price level.
2. **Measure the standard wiggle.** Review at least 5 days of the stock's 5-minute bar chart and estimate its average pullback size on trending days — typically 5/8 to 3/4 point in the book's examples, updated periodically.
3. **Wait for consolidation.** Identify several 5-minute bars trading tightly against a price level (the day's high, low, or a prior level); the longer and tighter, the higher-probability the setup.
4. **Enter on the breakout.** Buy above the consolidation's upper boundary, sell short below its lower boundary. Prefer the day's first breakout; take a later one on the same stock only if the broader trend is intact and the day's range still leaves room versus the stock's average.
5. **Pre-trade filter.** Use bid-side (ask-side, for shorts) depth to estimate the exit price on an immediate reversal; pass if that loss would exceed about 1/4 point (sometimes 3/8).
6. **Set the initial stop.** 1/4 point from the actual fill price (sometimes 3/8), not from the breakout level.
7. **Convert to a trailing stop.** Once open profit plus the initial stop equals roughly 3/8 point, trail the stop by the standard wiggle amount from step 2.
8. **Exit ("wiggled out")** the moment price retraces beyond the standard wiggle amount from its most favorable point — the primary exit in place of a fixed target.
9. **Override with a direct profit-take** when a fast spike of roughly 1 point or more stalls within 5-10 minutes of the breakout, price approaches daily support/resistance, or a strong move occurs on day one of a multi-day setup.
10. **Swing variant.** Apply the same trigger to daily bars for 2-to-5+-day trades; the sample gives no distinct stop/wiggle size for this timeframe — treat it as the intraday rules scaled up until better data is available.

## Risk

Risk per trade is fixed at entry (about 1/4, occasionally 3/8, point from the fill price) and checked against the pre-trade depth filter (rule 5) before the trade is taken at all. No percent-of-equity sizing rule exists in the source — position size is left to the trader, with only a 500-share beginner recommendation to limit the cost of learning each stock's fill behavior. Overnight/swing risk is flagged qualitatively: a 10-20+ point adverse gap is a risk to check for (news, earnings, economic releases) before holding past the close, with no explicit dollar or percent cap given.

## Caveats

The stop and wiggle sizes (1/4, 3/8, 5/8-3/4 point) are fractional, pre-decimalization figures calibrated to mostly tech-sector Nasdaq stocks of the late 1990s; they don't translate directly to cents or percentages on a modern instrument without re-deriving a "standard wiggle" from current data. The bid-depth filter and screen-reading process assume Nasdaq market-maker-style quote transparency later changed by decimalization and order-handling reforms. No backtested win rate, average trade, or drawdown statistic is given for the system — its support is illustrative chart examples, not systematic testing. The swing variant is named but lacks its own numeric stop/target rules in the sample, so treat it as adapted rather than fully specified.
