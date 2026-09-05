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

A short-term (average holding period under 12 days), mechanical breakout system credited to techniques popularized by Larry Williams. It buys or sells a percentage of the prior three days' high-low range measured from today's open, on the theory that the opening price sets the tone for the session's likely direction. Because a plain opening-range breakout whipsaws in roughly half its trades (win rate is expected to run under 50%), the authors add a "buy easier / sell easier day" filter derived from yesterday's close relative to the close before it, which skews the breakout thresholds asymmetrically in the statistically favored direction. Risk is capped with an ATR-based stop that is pulled to breakeven once the trade shows a defined profit cushion, rather than trailed continuously. Backtested one-contract-per-trade on futures, 1/1/1983-8/31/1999, $75 commission/slippage assumed.

## Rules

**Volatility measure**: Calculate the highest high and lowest low of the past 3 trading days; the difference between them is the volatility measure used to size the breakout distance from today's open.

**Buy-easier / sell-easier day determination**: If today's close is less than yesterday's close, tomorrow is a "buy easier" day. If today's close is greater than or equal to yesterday's close, tomorrow is a "sell easier" day.

**On a buy-easier day**:
- Buy stop = today's open + (volatility measure / 2) — i.e., 50% of the 3-day range added to the open.
- Sell stop = today's open - volatility measure — i.e., 100% of the 3-day range subtracted from the open.

**On a sell-easier day**:
- Sell stop = today's open - (volatility measure / 2).
- Buy stop = today's open + volatility measure.

(In other words: the breakout in the statistically favored direction is set at 50% of the recent range from the open; the breakout in the opposing direction is set at a wider 100% of the range, making it harder to trigger a countertrend entry.)

**Initial protective stop**: Calculate the 10-day average true range (ATR). Set the initial stop at 3x this 10-day ATR from the entry price.

**Break-even stop**: Once the trade shows an open profit equal to 3x the 10-day ATR, move the stop to breakeven (the original entry price) rather than continuing to trail it further.

**Stop selection**: Use whichever stop is currently closer to the market — the protective stop, the break-even stop (once activated), or the reversal stop implied by the day's opposite breakout level.

**Reversal**: A fill on the opposite breakout stop during the same session reverses the position (stop-and-reverse), consistent with a standard two-sided opening-range-breakout order structure.

## Risk

The wide 3x-ATR initial stop is deliberate: because the system is expected to win less than half its trades, the authors argue winners must be allowed room to develop while losers are capped, and a tight stop on a short-duration breakout system would simply increase the whipsaw rate in congestive (non-trending) markets. Unlike the book's longer-term moving-average system, this one uses a break-even stop rather than a continuously trailed stop, reflecting its shorter average holding period — once 3 ATRs of profit are banked, the trade is managed to avoid giving all of it back rather than chasing further gains with a tightening trail. The buy-easier/sell-easier asymmetry (50% breakout with the pattern vs. 100% against it) is the system's main edge source; the authors' own bracketing tests (removing the buy-easier/sell-easier logic and using flat 50% or flat 100% breakouts in both directions) show materially worse results, confirming the pattern filter carries real weight rather than being decorative.

## Caveats

The authors are explicit that the raw, unfiltered version of this breakout idea (without the buy-easier/sell-easier day logic) shows only a marginal statistical edge that does not cover commission and slippage — the asymmetric filter is what pushes it from "interesting" to tradable in their tests, so a reader who drops that filter should not expect the same results. As a short-term, frequently-trading system, it is more sensitive to execution costs (slippage, fill quality) than the book's longer-term systems; results were only tested through August 1999 and should be re-verified on current data. No explicit market-selection or portfolio guidance is given for this specific system beyond the general diversification principles discussed elsewhere in the book.
