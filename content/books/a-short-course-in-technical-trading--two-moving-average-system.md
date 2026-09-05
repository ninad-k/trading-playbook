---
title: "Two-Moving-Average Trend System"
author: Perry J. Kaufman
year: 2003
slug: a-short-course-in-technical-trading--two-moving-average-system
tier: A
category: Trend Following & Mechanical Systems
tags: [moving-average, trend-following, dual-ma, crossover, risk-control]
difficulty: beginner
doc_type: system
parent: a-short-course-in-technical-trading
pages: 339
one_liner: "Pair a slow and fast moving average; stay long only while both trend up, exit the instant the fast one turns down."
related: []
source_file: "A Short Course in Technical Trading.PDF"
---

## What it is

A trend-following system built from two moving averages of different speeds, used specifically to fix the biggest weakness of a single-moving-average trend system: giving back a large fraction of open profit before the slow trendline finally turns. Instead of trading the crossover of price against a moving average, the position is defined by the *direction* of each moving average line itself. Kaufman demonstrates this on Amazon (October 1998-April 1999) with an 80-day slow average and a 10-day fast average: the two-trend version produced $62/share across several smaller, controlled trades versus a single 80-day trend that still held an open (unrealized, unprotected) profit of $78/share at the same point — a larger number on paper, but one exposed to giving back a large share of it before the slow line ever turns.

## Rules

1. Choose a long (slow) moving-average calculation period, typically 50-200 days, and a short (fast) calculation period, typically 5-30 days.
2. Compute the direction of each average daily: an average is "up" if today's value is greater than yesterday's value, "down" if less (this is the trend-direction rule used throughout the book — direction of the line, not price relative to the line).
3. **Entry (long):** buy when both the fast and the slow moving averages are trending up.
4. **Entry (short):** sell/short when both are trending down.
5. **Exit:** close the position the moment the fast moving average turns against the position — it will always turn before the slow one, since it reacts faster to new prices.
6. After an exit, wait for both averages to realign in the same direction again before re-entering; this produces a series of smaller trades rather than one long trade held to the final slow-trend reversal.

Spreadsheet mechanics are the same as a single moving average, computed twice at two different lengths:
```
MA_fast(t) = AVERAGE(prices over fast period)
MA_slow(t) = AVERAGE(prices over slow period)
Direction_fast = IF(MA_fast(t) > MA_fast(t-1), "up", "down")
Direction_slow = IF(MA_slow(t) > MA_slow(t-1), "up", "down")
Position = "long" if both "up"; "short" if both "down"; otherwise flat/prior position per exit rule
```

## Risk

- Risk is governed by the speed of the *fast* average: a shorter fast-average calculation period produces a smaller risk per trade (tighter exit reaction) but more total trades and more whipsaws in choppy markets.
- The two-trend approach trades reward-to-risk for total profit: Kaufman's Amazon example shows total realized profit was lower than the single slow-trend's open (unrealized) profit, but with a materially better ratio of profit to risk taken and without the large drawdown the single-trend approach would have suffered if it had held to the final reversal.
- As with any moving-average trend method, stops should not be set inside the normal noise of the fast average; Kaufman's general rule of never placing a stop closer than 1.5x current daily volatility still applies as an overlay.
- Because the fast average both enters and exits the trade, its whipsaw rate directly determines commission/slippage drag — very short fast periods (well under 10 days) should be checked against realistic trade frequency before committing capital.

## Caveats

The book only demonstrates this system on a single instrument (Amazon) over roughly six months — no multi-market, multi-period backtest table is given for the two-average version, unlike the single-moving-average, breakout, and stochastic sections, which do include quantified tables. The specific period pair (80/10) is illustrative, not asserted to be optimal; Kaufman does not test a range of fast/slow combinations the way he does for the single-trend and breakout methods elsewhere in the book. As with all moving-average methods in this text, the system remains time-driven rather than event-driven, so it will still lag at the very start of a new trend and can still whipsaw in a sideways, low-volatility market where neither average develops sustained direction.
