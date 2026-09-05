---
title: "Short-Term Volatility Based Open Range Breakout System"
author: "John R. Hill, George Pruitt, Lundy Hill"
year: 2000
slug: j-r-hill-g-pruitt-and-l-hill-the-ultimate-trading-guide--volatility-breakout-system
tier: A
category: Day Trading & Scalping
tags: [breakout, volatility, opening-range, mechanical-systems, futures, atr-stop, larry-williams]
difficulty: intermediate
doc_type: system
parent: j-r-hill-g-pruitt-and-l-hill-the-ultimate-trading-guide
pages: 302
one_liner: "A Larry Williams-style opening-range breakout sized off the prior 3-day range, with buy-easier/sell-easier day logic and a 3x-ATR stop trailed to breakeven."
related: [larry-williams-how-to-trade-better, curtis-faith-way-of-the-turtle, turtletrader]
source_file: "J R Hill G Pruitt And L Hill - The Ultimate Trading Guide.pdf"
---

## What it is

A short-term (average holding period under 12 days) mechanical breakout system credited to techniques popularized by Larry Williams. It buys or sells a percentage of the prior three days' high-low range measured from today's open, on the theory that the open sets the tone for the session's likely direction. Because a plain opening-range breakout whipsaws in roughly half its trades, the authors add a "buy easier / sell easier day" filter derived from yesterday's close relative to the close before it, skewing the breakout thresholds asymmetrically toward the statistically favored direction. Risk is capped with an ATR-based stop pulled to breakeven once a defined profit cushion appears, rather than trailed continuously. Backtested one-contract-per-trade on futures, 1/1/1983-8/31/1999, $75 commission/slippage assumed.

## Rules

**Volatility measure**: the highest high minus the lowest low of the past 3 trading days — used to size the breakout distance from today's open.

**Buy-easier / sell-easier determination**: if today's close is less than yesterday's, tomorrow is a "buy easier" day; if greater than or equal, tomorrow is a "sell easier" day.

**On a buy-easier day**: buy stop = open + 50% of the volatility measure; sell stop = open - 100% of the volatility measure.

**On a sell-easier day**: sell stop = open - 50% of the volatility measure; buy stop = open + 100% of the volatility measure.

(The breakout in the statistically favored direction sits at 50% of the recent range from the open; the breakout against it sits at a wider 100%, making a countertrend entry harder to trigger.)

**Initial protective stop**: 3x the 10-day average true range (ATR) from entry.

**Break-even stop**: once open profit reaches 3x the 10-day ATR, move the stop to breakeven rather than trailing it further.

**Stop selection**: use whichever stop is closer to the market — protective, break-even (once active), or the reversal stop implied by the day's opposite breakout level.

**Reversal**: a fill on the opposite breakout stop during the same session reverses the position, per standard two-sided opening-range-breakout order structure.

## Risk

The wide 3x-ATR initial stop is deliberate: since the system wins under half its trades, winners need room to develop while losers stay capped, and a tight stop would simply raise the whipsaw rate in congestive markets. Unlike the book's longer-term moving-average system, this one uses a break-even stop rather than a continuous trail, reflecting its shorter holding period — once 3 ATRs are banked, the trade is managed to avoid giving it back rather than chasing further gains. The buy-easier/sell-easier asymmetry is the system's main edge source; the authors' own bracketing tests (flat 50% or flat 100% breakouts both directions, without the day filter) show materially worse results, confirming the filter carries real weight.

## Caveats

The authors are explicit that the unfiltered breakout idea (without buy-easier/sell-easier logic) shows only a marginal edge that doesn't cover commission and slippage — the asymmetric filter is what makes it tradable in their tests, so dropping that filter shouldn't be expected to reproduce the results. As a short-term, frequently-trading system it's more sensitive to execution costs than the book's longer-term systems; results were tested only through August 1999 and should be re-verified on current data. No explicit market-selection or portfolio guidance is given beyond the book's general diversification principles.
