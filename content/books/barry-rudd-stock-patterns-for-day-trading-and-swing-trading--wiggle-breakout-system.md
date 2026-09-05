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

A discretionary-but-rule-bounded intraday breakout method built around two ideas: (1) trade the break of a tight, multi-bar price consolidation on a 5-minute chart, and (2) once in the trade, give it room to breathe using the stock's own historical average pullback size — its "standard wiggle" — rather than an arbitrary or fixed profit target. The same consolidation-then-breakout logic is applied to daily bars for multi-day swing trades, and to very tight, short compressions for the scalping variant.

## Rules

1. **Screen the stock.** Average daily volume of at least 100,000 shares; market-maker bid/ask spread of about 1/8 point (occasionally 1/4); at least 4+ market makers quoting at each price level.
2. **Measure the standard wiggle.** Before trading a name, review at least 5 days of its 5-minute bar chart and estimate the average pullback size on trending days — typically 5/8 to 3/4 point in the book's examples, though this varies by stock and should be updated periodically.
3. **Wait for consolidation.** Identify a period of several 5-minute bars trading tightly against a price level (the day's high, low, or a prior level). The longer and tighter this consolidation, the higher-probability the setup.
4. **Enter on the breakout.** Buy when price breaks above the consolidation's upper boundary; sell short when it breaks below the lower boundary. The first breakout of the day is preferred; a later breakout on the same stock is only taken if the broader market trend is still intact and the day's range leaves room versus the stock's average daily range.
5. **Pre-trade filter.** Before entering, use bid-side (or ask-side, for shorts) depth to estimate the probable exit price if the market reverses immediately after the fill. Pass on the setup if that immediate loss would exceed about 1/4 point (sometimes 3/8).
6. **Set the initial stop.** Place a stop 1/4 point from the actual fill price (sometimes 3/8 point) — not from the breakout level.
7. **Convert to a trailing stop.** Once open profit plus the initial 1/4-point stop equals roughly 3/8 point of profit, begin trailing the stop by the stock's standard wiggle amount from step 2.
8. **Exit ("wiggled out").** Close the trade the moment price retraces beyond the standard wiggle amount from its most favorable point — this is the primary exit mechanism in place of a fixed target.
9. **Override with a direct profit-take** instead of trailing when: a fast price spike of about 3/4 point or more occurs within 5-10 minutes of the breakout and then stalls; price approaches a daily support/resistance level; or a strong move occurs on day one of a multi-day setup.
10. **Swing variant.** Apply the same consolidation/breakout trigger to daily bars for trades intended to last 2 to 5+ days; the sampled pages do not specify a distinct stop or wiggle size for this timeframe — treat it as the intraday rules applied one timeframe up until better data is available.

## Risk

Risk per trade is fixed at entry (about 1/4, occasionally 3/8, point from the fill price) and is checked against the pre-trade bid/ask-depth filter (rule 5) before the trade is taken at all. There is no percent-of-equity sizing rule in the source — position size (shares per trade) is left to the trader, with the book only recommending 500-share clips for beginners to limit the cost of learning each stock's fill behavior. Overnight/swing risk is flagged separately and qualitatively: a 10-20+ point adverse gap against a held position is called out as a risk to check for (pending news, earnings, economic releases) before holding past the close, but no explicit dollar or percent cap on overnight exposure is given.

## Caveats

The stop and wiggle sizes (1/4, 3/8, 5/8-3/4 point) are fractional, pre-decimalization figures calibrated to individual, mostly tech-sector Nasdaq stocks of the late 1990s; they do not translate directly to cents or percentages on a modern, decimalized instrument without the trader re-deriving a "standard wiggle" from current data. The pre-trade bid-depth filter and the "big 4" screen-reading process assume Nasdaq market-maker-style quote transparency that was substantially changed by decimalization and order-handling reforms in the early 2000s. No backtested win rate, average trade, or drawdown statistic is given for the system as a whole — its support in the source is illustrative chart examples rather than systematic testing. The swing-trade variant is stated by name and holding period but is not accompanied by its own numeric stop/target rules in the sampled pages, so it should be treated as adapted rather than as fully specified.
