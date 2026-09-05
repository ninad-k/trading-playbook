---
title: "N-Day Rolling Breakout System"
author: Perry J. Kaufman
year: 2003
slug: a-short-course-in-technical-trading--n-day-breakout-system
tier: A
category: Trend Following & Mechanical Systems
tags: [breakout, trend-following, rolling-highs-lows, event-driven]
difficulty: beginner
doc_type: system
parent: a-short-course-in-technical-trading
pages: 339
one_liner: "Buy the highest high and sell the lowest low of the past N days, computed fresh every day, with three progressively stricter confirmation rules."
related: []
source_file: "A Short Course in Technical Trading.PDF"
---

## What it is

An event-driven trend system that replaces hand-drawn support/resistance lines with a rolling calculation: every day, find the highest high and lowest low over the previous N days (not including today). A new high triggers a buy (or reverses a short); a new low triggers a sell (or reverses a long). Because it only reacts to genuine new highs/lows rather than the passage of time, it holds through sideways drift better than a moving average and gives fewer false signals at trend turns, at the cost of larger risk per trade and larger profit per trade. Kaufman presents this as one of four equivalent trend calculations (with moving average, exponential smoothing, and regression slope) and shows it has the highest win-rate and profit-factor characteristics among them when back-tested across a 5-200 day range of N.

## Rules

Pick a lookback length N (common defaults: 20 days for daily charts, 30 weeks for weekly charts). Three entry variants, in increasing order of conservatism:

1. **Rule 1 (basic).** Buy when today's high exceeds the highest high of the prior N days. Sell/short when today's low drops below the lowest low of the prior N days. Intraday penetration triggers the signal.
2. **Rule 2 (close-confirmed).** Same levels, but only act if today's *close* is beyond the N-day high/low, not merely the intraday high/low. Avoids one-tick false breakouts but can leave you out of a market that is moving steadily higher/lower without ever closing at a new extreme.
3. **Rule 3 (compromise, Kaufman's preferred).** Buy if there is a new N-day high AND today's close is higher than yesterday's close. Sell if there is a new N-day low AND today's close is lower than yesterday's close. Avoids most false breakouts while still confirming genuine momentum.

Mechanics:
- Recalculate the N-day high/low window every day, dropping the oldest day and adding the newest (a true "rolling" window, not a fixed chart range).
- The system is always in the market: a sell signal for a long position simultaneously opens a new short (stop-and-reverse), unless you choose to flatten instead.
- To anticipate the breakout and capture "free exposure," place the entry order slightly ahead of the exact N-day high/low level rather than exactly at it, since a genuine breakout often gaps through the level on a rush of clustered orders.
- Place entries/exits calculated from the close just before the market closes, not the next morning, so the order is in ahead of any gap-open reaction to the breakout.

Spreadsheet formula (10-day example, columns: B=high, C=low, D=close):
```
E11 = MAX(B1:B10)                 ' 10-day high through previous day
F11 = MIN(C1:C10)                 ' 10-day low through previous day
G11 = IF(B11>E11 AND D11>D10, 1, IF(C11<F11 AND D11<D10, -1, G10))   ' trend/position
```

## Risk

- Initial risk on a breakout trade equals the distance between the resistance level (N-day high) and the support level (N-day low) used for entry — this is inherent to the method and widens automatically in volatile markets, narrows in quiet ones.
- Because risk expands with volatility, position size should shrink accordingly rather than using a fixed share count; Kaufman's volatility-based position sizing (equalizing dollar volatility across positions) applies directly.
- Backtests on Microsoft (5-year window, calculation periods 5-200 days) show the breakout method has roughly half the number of trades of a moving average of comparable speed, a substantially higher average profit per trade (up to 5x), a slightly larger maximum drawdown at short lookbacks, and a win rate that climbs toward 40%+ at longer lookbacks versus ~25-35% for moving averages.
- A stop-loss can be layered on top of the natural breakout exit, but should never be tighter than 1.5x the current daily true range, or the trade should simply be closed outright instead of using an artificially close stop.
- Longer N reduces whipsaws but increases the risk taken per trade and the time a losing position is held before the opposite breakout triggers an exit.

## Caveats

Kaufman is explicit that the rolling breakout is not inherently "better" than manually drawn trendlines — it has the same profit/risk character, but is far more practical to compute across many markets and to backtest. It remains partly time-dependent: as the rolling window advances, quieter markets produce closer highs/lows and therefore more frequent, smaller-risk signals, so it is not a purely event-driven method in the way swing charting or point-and-figure charting are. The book does not give a single "best" N — its own tests show profitability is choppy across calculation lengths in the 20-55 day range and improves at both shorter and longer extremes, which is itself a caution against over-fitting a specific N to one instrument's history. As with all the book's examples, backtests are shown on individual dot-com-era stocks (Microsoft, Enron) over short multi-year windows, not on a broad, out-of-sample universe.
