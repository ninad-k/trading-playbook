---
title: "The Bollinger Bandit Trading Strategy (Full System)"
author: "George Pruitt, John R. Hill"
year: 2003
slug: george-pruitt-building-winning-trading-systems-with-tradestation--bollinger-bandit
tier: A
category: "Trend Following & Mechanical Systems"
tags: [bollinger-bands, standard-deviation, trend-following, breakout, trailing-stop, futures]
difficulty: intermediate
doc_type: system
parent: george-pruitt-building-winning-trading-systems-with-tradestation
pages: 406
one_liner: "A Bollinger Band breakout system with a trend filter and a decaying trailing stop that tightens the longer a trade is held, up to a floor of 10 days."
related: [dynamic-breakout-ii-strategy, king-keltner-trading-strategy]
source_file: "George Pruitt-Building_Winning_Trading_Systems_With_Tradestation.pdf"
---

## What it is

A "first cousin" of the King Keltner system that trades breakouts of a 50-day Bollinger Band (a moving average of closes plus/minus 1.25 standard deviations) rather than a true-range channel. Unlike King Keltner's flat moving-average exit, Bollinger Bandit uses a shrinking trailing stop: the moving-average look-back used for the exit starts at 50 days and decrements by one day for every day the trade stays open, down to a floor of 10 days — so the exit tightens the longer a position runs, giving back less of a large profit than a static exit would. A 30-day rate-of-change filter (today's close vs. the close 30 days ago) confirms the position is only taken in the direction of an existing trend.

## Rules

**Indicators needed**
1. `upBand` = 50-day moving average of closes + (50-day standard deviation of closes × 1.25).
2. `dnBand` = 50-day moving average of closes − (50-day standard deviation of closes × 1.25).
3. `rocCalc` = today's close − close 30 days ago (a simple rate-of-change / trend filter).
4. `liqDays`, a counter initialized to 50 whenever flat, that decrements by 1 for every additional day a trade stays open.

**Entry**
5. Go long on a stop at `upBand`, next bar, only if `rocCalc` is positive (today's close is above the close 30 days ago — an uptrend confirmation).
6. Go short on a stop at `dnBand`, next bar, only if `rocCalc` is negative (close is below the close 30 days ago — a downtrend confirmation).
7. The potential band penetration is necessary but not sufficient — the 30-day rate-of-change trend filter must also agree with the direction of the breakout before a position is opened.

**Exit / trailing stop**
8. While flat, reset `liqDays` to 50.
9. On each day a position is held, decrement `liqDays` by 1, with a floor of 10 (i.e., `liqDays = MaxList(liqDays − 1, 10)`) — the exit moving-average length shortens as the trade ages, tracking price more closely over time and locking in more of an open profit.
10. Compute the liquidation point as the moving average of closes over the current (shrinking) `liqDays` length.
11. Exit a long (sell) on a stop at this liquidation point only if it is currently below `upBand` — this condition prevents the system from immediately re-entering the same long it just exited.
12. Exit a short (buy to cover) on a stop at the liquidation point only if it is currently above `dnBand`, for the symmetric reason.

**Parameters**
13. Use 50 days for the Bollinger Band length, 1.25 standard deviations for band width, 30 days for the rate-of-change filter, and a 10-day floor on the trailing-stop length — unchanged across every market traded.

## Risk

No account-level position sizing is specified; the authors' own testing found the shrinking trailing stop "only marginally increased profit and decreased drawdown" versus a flat exit, but argue it adds comfort because risk visibly tightens as a trade ages. In the 1982-2002, 17-market backtest ($75 commission/slippage), net profit was $537,822 over 3,092 trades. Best: Japanese Yen (+$121,938), Natural Gas (+$85,898); worst: Wheat (−$20,038), Live Cattle (−$16,868), Soybeans (−$15,925) — the same grain/meat weakness as the book's other trend systems. The authors note it is highly correlated with King Keltner (profitable and unprofitable in the same markets), so trading both together adds little diversification.

## Caveats

Backtest assumptions match the rest of the book: flat $75 commission/slippage, a fixed window, no walk-forward test, per-market rather than portfolio-level reporting. Because the exit look-back shrinks over time, a trade stalled near breakeven for many days can be exited by an increasingly short, more reactive moving average even without a sharp adverse move — a subtlety the source doesn't address. The authors concede the trailing-stop refinement's edge over a flat exit is marginal, so the real edge is the same Bollinger Band breakout-plus-trend-filter logic as its Keltner-based sibling, not the exit mechanism.
