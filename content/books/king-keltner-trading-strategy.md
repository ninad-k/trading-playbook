---
author: George Pruitt, John R. Hill
category: Trend Following & Mechanical Systems
difficulty: intermediate
doc_type: manual
one_liner: A 1960s Chester Keltner moving-average-band breakout system, modernized
  with a true-range channel and a moving-average liquidation stop.
pages: 4
related:
- dynamic-breakout-ii-strategy
- money-management-in-trading
reviewed_pdf_pages: 1-4
slug: king-keltner-trading-strategy
source_file: King_Keltner_Trading_Strategy.pdf
source_review: full
tags:
- keltner-channel
- moving-average
- true-range
- trend-following
- breakout
- futures
tier: B
title: The King Keltner Trading Strategy
year: 2002
---

## Summary

An excerpt from "Building Winning Trading Systems with TradeStation" documenting a modernized version of Chester Keltner's 1960 moving-average-band system. The original Keltner approach built a channel around a moving average of high/low/close using a moving average of the high-low range; a buy signal fires when price penetrates the upper band and a sell signal when it penetrates the lower band. The King Keltner version substitutes true range (which accounts for gaps) for the simple high-low range, uses 40-day averages for both the centerline and the band width, and adds a direction filter (today's moving average must be rising for a long, falling for a short) before allowing an entry. Positions are liquidated — win or lose — when price returns to the moving average, which serves as both the profit-take and the stop-loss level. A 1982–2002 backtest across 17 futures markets (commission/slippage $75) produced $593,302 total net profit over 3,478 trades, with the authors noting the intentional use of the same two parameters across all markets and win rates under 50% by design (the system is meant to catch a few large trends that outweigh many small failed breakouts).

## Key points

- Core structure: moving average of (High+Low+Close)/3 over 40 days as the centerline; upper/lower bands = centerline ± 40-day average true range.
- True range (vs. simple range) = max(today's high, yesterday's close) − min(today's low, yesterday's close), capturing overnight/weekend gaps that a plain high−low range misses.
- Direction filter: a long is only initiated when today's moving average is greater than yesterday's (rising trend) and price reaches the upper band; a short requires a falling moving average and price reaching the lower band.
- Exit rule: liquidate any open position (long or short, win or lose) when price crosses back to the moving average — the same line serves as both profit-take and stop-loss.
- Backtest (1982–2002, 17 markets, $75 commission/slippage): $593,302 total net profit over 3,478 trades; standout performers were Japanese Yen (+$114,175), Natural Gas (+$100,577), and U.S. Bonds (+$66,275); losers included Wheat (−$16,113), Soybeans (−$15,194), and Live Cattle (−$3,037).
- Win rates across markets ranged roughly 22–39%, explicitly expected to be under 50% — the system's profitability depends on a small number of large trend trades outweighing many smaller failed breakouts.
- The authors deliberately used identical parameters (40/40) across all 17 markets rather than optimizing per market, arguing this improves robustness, though they acknowledge some practitioners would set different parameters per market sector (e.g., one set for currencies, another for meats).
- The system by itself has no bet-sizing/contract-count rule — the authors note it would need a separate money-management overlay to be used as a full portfolio system.

## Actionable rules

1. Compute movAvg = 40-day average of (High+Low+Close); upBand = movAvg + 40-day Average True Range; dnBand = movAvg − 40-day Average True Range.
2. Enter long the next bar at a stop at upBand only if today's movAvg > yesterday's movAvg; enter short the next bar at a stop at dnBand only if today's movAvg < yesterday's movAvg.
3. Exit any open long when price trades at or below movAvg; exit any open short when price trades at or above movAvg (same liquidation point serves as stop and target).
4. Use the same 40/40 parameter pair across all markets traded rather than optimizing per instrument, unless deliberately grouping by market sector (e.g., all currencies together).
5. Expect and accept a sub-50% win rate — do not abandon the system after a string of small losing breakouts, since its edge depends on catching a minority of large trend trades.

## Caveats

Backtest uses static 1982–2002 data with flat $75 commission/slippage and no walk-forward or out-of-sample validation; results are reported per-market only, not as a combined portfolio equity curve, so aggregate drawdown across simultaneously-held positions is not shown. As with any channel-breakout system, its stated main weakness is the failed breakout (price reaching the band as a point of exhaustion rather than trend confirmation), which the moving-average liquidation stop is specifically designed to limit rather than eliminate. No position-sizing or portfolio-level risk rule is provided.

## Who it is for

Systematic futures traders who want a simple, two-parameter trend-following breakout system with an explicit, symmetric exit rule (moving-average liquidation) rather than a discretionary target or trailing-stop scheme.
