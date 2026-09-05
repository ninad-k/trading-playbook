---
title: "The King Keltner Trading Strategy (Full System)"
author: "George Pruitt, John R. Hill"
year: 2003
slug: george-pruitt-building-winning-trading-systems-with-tradestation--king-keltner
tier: A
category: "Trend Following & Mechanical Systems"
tags: [keltner-channel, moving-average, true-range, trend-following, breakout, futures]
difficulty: intermediate
doc_type: system
parent: george-pruitt-building-winning-trading-systems-with-tradestation
pages: 406
one_liner: "A modernized 1960s Chester Keltner moving-average-band breakout: buy/sell on a true-range band penetration in the direction of the moving average's slope, liquidate at the moving average itself."
related: [dynamic-breakout-ii-strategy]
source_file: "George Pruitt-Building_Winning_Trading_Systems_With_Tradestation.pdf"
---

## What it is

A long-term trend-following channel breakout built around Chester Keltner's 1960 moving-average-band concept, updated by Pruitt and Hill with true range (instead of simple high-low range) and a trend-direction filter. A 40-day moving average of the typical price forms the centerline; bands are placed a 40-day average true range above and below it. A position is taken only when price penetrates the band in the direction the moving average is already sloping, and every open position — winner or loser — is liquidated when price returns to the moving average, which serves as both the profit-take and the stop-loss level. The same two parameters (40, 40) are used unchanged across all markets traded.

## Rules

**Indicators needed**
1. `movAvgVal` = 40-day simple moving average of (High + Low + Close).
2. `upBand` = movAvgVal + 40-day Average True Range.
3. `dnBand` = movAvgVal − 40-day Average True Range.
4. True range (for the ATR calculation) = max(today's high, yesterday's close) − min(today's low, yesterday's close), which captures gap moves that a plain high-low range misses.

**Entry**
5. Go long on a stop at `upBand`, entered on the next bar, only if today's `movAvgVal` is greater than yesterday's `movAvgVal` (moving average is rising).
6. Go short on a stop at `dnBand`, entered on the next bar, only if today's `movAvgVal` is less than yesterday's `movAvgVal` (moving average is falling).
7. No other filter, volume condition, or seasonal rule gates entry — the direction-of-slope check is the only trend confirmation used.

**Exit**
8. `liquidPoint` = the same 40-day moving average of (High + Low + Close), recalculated daily.
9. If long, exit (sell) on a stop at `liquidPoint` whenever price trades at or below it.
10. If short, exit (buy to cover) on a stop at `liquidPoint` whenever price trades at or above it.
11. This single liquidation level serves as both the protective stop and the profit-taking exit — there is no separate target or trailing-stop mechanism.

**Parameters and portfolio use**
12. Use identical 40/40 parameters across every market traded rather than optimizing per instrument; the authors argue this is the more robust test of whether the underlying principle (moving-average-band breakout with true-range width) is real, though they concede sector-level grouping (all currencies together, for instance) is a defensible compromise.
13. Expect and accept a sub-50% win rate by design — the system is built to catch a minority of large trending moves that outweigh a majority of small failed breakouts, not to be "right" most of the time.

## Risk

No account-level position sizing or percent-of-equity cap is given — the authors say it "could be the foundation for an entire portfolio-based trading platform" but needs a money-management overlay (e.g., their separate Money Manager template) before being traded as a full program. Per-trade risk is unbounded until the moving-average liquidation point is hit, so effective stop distance floats with the current 40-day ATR. In the authors' 1982-2002, 17-market backtest ($75 commission/slippage), the system made $593,302 net over 3,478 trades, win rates roughly 22-39% by market. Best: Japanese Yen (+$114,175), U.S. Bonds (+$66,275), Swiss Franc (+$56,963); worst: Wheat (−$16,113), Soybeans (−$15,194), Live Cattle (−$3,037) — grains and meats underperformed throughout.

## Caveats

The backtest uses flat $75 commission/slippage over a fixed window with no walk-forward or out-of-sample test, and results are per-market only, not a combined portfolio curve, so aggregate drawdown across simultaneous positions is never shown. Its principal known weakness, as with any channel-breakout system, is the failed breakout — price reaching the band as exhaustion rather than trend confirmation — which the moving-average exit limits but does not eliminate. Underperformance in grains and meats is acknowledged but unresolved.
