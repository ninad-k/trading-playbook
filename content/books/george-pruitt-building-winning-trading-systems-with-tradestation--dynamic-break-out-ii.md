---
title: "The Dynamic Break Out II Strategy (Full System)"
author: "George Pruitt, John R. Hill"
year: 2003
slug: george-pruitt-building-winning-trading-systems-with-tradestation--dynamic-break-out-ii
tier: A
category: "Trend Following & Mechanical Systems"
tags: [donchian-channel, volatility, adaptive-parameters, bollinger-bands, trend-following, seasonality]
difficulty: intermediate
doc_type: system
parent: george-pruitt-building-winning-trading-systems-with-tradestation
pages: 406
one_liner: "A Donchian channel breakout whose look-back length adapts daily to changes in 30-day price volatility, filtered by an adaptive Bollinger Band and exited on an adaptive moving-average trailing stop."
related: [dynamic-breakout-ii-strategy]
source_file: "George Pruitt-Building_Winning_Trading_Systems_With_Tradestation.pdf"
---

## What it is

An upgraded version of George Pruitt's original 1996 Dynamic Break Out system (published in Futures Magazine), built on a standard Donchian channel breakout — buy on a new N-day high, sell on a new N-day low — but where N is not fixed. Instead, an "adaptive engine" changes the look-back length every day based on the percentage change in 30-day standard deviation of closing prices: rising volatility (associated with market indecision) widens the look-back, making entries harder to trigger; falling volatility (associated with a trending market) narrows the look-back, making entries easier. Version II adds an adaptive Bollinger Band filter on top of the raw breakout, and replaces the original's flat $1,500 money-management stop with a dynamic trailing stop set at the moving average of closes over the same adaptive window.

## Rules

**Adaptive look-back engine**
1. Initialize `lookBackDays = 20` on the first bar.
2. Each subsequent day: `todayVolatility` = 30-day standard deviation of closes; `yesterdayVolatility` = the same calculation one bar back.
3. `deltaVolatility = (todayVolatility − yesterdayVolatility) / todayVolatility`.
4. `lookBackDays = lookBackDays × (1 + deltaVolatility)`, rounded to the nearest whole number.
5. Clip `lookBackDays` to the range [20, 60] — the floor and ceiling the authors found necessary through testing, since values outside this band produced unacceptable results.

**Bollinger filter and breakout levels (recomputed daily using the current `lookBackDays`)**
6. `upBand` = Bollinger Band of closes over `lookBackDays`, +2.0 standard deviations.
7. `dnBand` = Bollinger Band of closes over `lookBackDays`, −2.0 standard deviations.
8. `buyPoint` = highest high over `lookBackDays`; `sellPoint` = lowest low over `lookBackDays`.

**Entry**
9. Go long on a stop at `buyPoint`, next bar, only if today's close is above `upBand`.
10. Go short on a stop at `sellPoint`, next bar, only if today's close is below `dnBand`.
11. Both the raw N-day breakout AND the Bollinger Band condition must agree before a signal fires — the band filter is what distinguishes Version II from the original 1996 system.

**Exit**
12. `longLiqPoint` = `shortLiqPoint` = moving average of closes over the current (adaptive) `lookBackDays`.
13. Exit a long (sell) on a stop at this liquidation point whenever price trades at or below it.
14. Exit a short (buy to cover) on a stop at this liquidation point whenever price trades at or above it.
15. This replaces the original Dynamic Break Out's flat $1,500 money-management stop entirely — the exit level is now volatility-adaptive, like the entry.

**Parameters**
16. Look-back floor/ceiling = 20/60 days; Bollinger width = 2.0 standard deviations; volatility measurement window = 30 days. All held constant across every market traded.

## Risk

No account-level position sizing is specified. In the 1982-2002, 17-market backtest ($75 commission/slippage), the system made $452,504 net over 1,820 trades — fewer than King Keltner, Bollinger Bandit, or Thermostat, since the adaptive filter is more selective. Best: Japanese Yen (+$118,200), U.S. Bonds (+$67,094), Swiss Franc (+$57,338); worst: Copper (−$25,175), Live Cattle (−$17,397), Soybeans (−$9,681), Wheat (−$14,831). Two follow-up experiments on the soybean weakness both failed: fading every signal still lost money (−$1,681 net over 128 trades, 64% win rate, but losses outweighed wins), and a March-July-long/July-February-short seasonal filter also lost money (−$4,363 net, 36% win rate, 1996-2002).

## Caveats

Same backtest limitations as the rest of the book: flat $75 commission/slippage, fixed window, no walk-forward validation, per-market rather than portfolio-level reporting. The authors are candid that trend-following systems generally can't capture grain markets' cyclical, seasonality-driven behavior, and that neither a naive fade nor a seasonal filter fixed it in their own tests — readers shouldn't assume a similarly simple patch exists. The 20/60-day bounds on the adaptive engine were chosen empirically ("through optimization... look-back lengths that fell beyond these boundaries did not generate acceptable expectations") rather than derived from theory, itself a mild form of the curve-fitting the book otherwise argues against.
