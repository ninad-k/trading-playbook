---
title: The Turtle Trading System
author: Michael W. Covel
year: 2007
slug: the-complete-turtletrader-the-legend-the-lessons-the-results--turtle-trading-system
tier: A
category: Trend Following & Mechanical Systems
tags: [turtle-trading, trend-following, breakout, atr, position-sizing, pyramiding, stops]
difficulty: intermediate
doc_type: system
parent: the-complete-turtletrader-the-legend-the-lessons-the-results
pages: 269
one_liner: "The full System One/System Two breakout rules, N-based unit sizing, 2N stops, and five-unit pyramiding taught to Richard Dennis's Turtles."
related: [curtis-faith-way-of-the-turtle, turtlerules, position-sizing]
source_file: "The Complete TurtleTrader - The Legend, the Lessons, the Results.pdf"
---

## What it is

A complete, mechanical trend-following system: two price-breakout entry/exit variants (System One and System Two), a volatility-based unit for position sizing and stops, and rules for pyramiding winners and capping portfolio risk. It is market-agnostic — the Turtles traded it unchanged across roughly 20 futures, currency, and interest-rate markets. See [[turtlerules]] for the original written version of these rules and [[curtis-faith-way-of-the-turtle]] for a first-person account of trading them.

## Rules

**Volatility unit ("N").** N is the market's Average True Range: the greatest of (today's high − today's low), (yesterday's close − today's high), (yesterday's close − today's low), as a 20-day moving average, recalculated daily.

**Entries — System One (S1).** Buy a new 20-trading-day high; sell short a new 20-day low. Skip the signal if the prior S1 trade (in either direction) was a winner — unless that prior trade's loss was ≥ 2N, in which case take the new signal regardless.

**Entries — System Two (S2).** Buy a new 55-trading-day high; sell short a new 55-day low. No skip filter. S2 also serves as a fail-safe: if an S1 signal was skipped and the market keeps trending, the S2 breakout re-enters the trade.

**Exits.** Exit on whichever comes first: (a) a 2N stop — 2 × N behind the position's (most recently pyramided) entry price, or (b) the opposite-direction breakout exit for the system used to enter — a 10-day breakout for S1 positions, a 20-day breakout for S2 positions.

**Position size (1 unit).** Account risk = 2% of current equity. Contract risk = 2N × dollar value per point for that market. Contracts per unit = account risk ÷ contract risk, rounded down to the nearest whole contract. Example: $100,000 account, corn at N = 7¢ (worth $50/cent) → contract risk = 7¢ × $50 × 2 = $700; account risk = $100,000 × 2% = $2,000; units = $2,000 ÷ $700 = 2.67 → trade 2 contracts.

**Pyramiding.** Add one additional unit each time price moves 1N in the trade's favor, up to a maximum of 5 units in a single market. Set the stop at ½N on the first unit's first day; from the second unit onward use the standard 2N stop, and each time a new unit is added, raise the stop on all existing units to the new unit's 2N level.

**Portfolio limits.** Cap at 4-5 units in any one market. Reduce combined exposure across highly correlated markets (e.g., corn and soybeans, gold and silver) rather than treating each as independently risked; a simple approximation used in the book is: total unit risk = larger group's unit count − (smaller group's unit count ÷ 2) when netting correlated long and short positions across a portfolio.

**Drawdown response.** Cut the per-trade risk percentage as account equity draws down (e.g., in 10%-equity-drawdown / 20%-unit-cut steps, matching the money-management overlay in [[forex-misc-money-management-ryan-jones--fixed-ratio-position-sizing]]), and restore it only as equity recovers — never mid-drawdown.

**Order type.** All entries and exits are stop (not limit) orders triggered by the breakout or stop level; no discretion on whether to take a valid signal.

## Risk

Worst-case single-market loss is bounded by the unit cap and 2N stops: five units × 2% each ≈ 10% of equity before the drawdown-response rule reduces exposure further. Because entries require no confirmation beyond the breakout itself, the system produces a high rate of small losing trades (documented win rates near 35-40%) offset by a small number of large trending winners; expectancy, not accuracy, is the basis for its profitability. Correlated-market unit limits exist because unhedged exposure to several markets that move together effectively multiplies single-market risk beyond what the per-market 2% figure suggests.

## Caveats

The 20/55/10/20-day parameters are explicitly not sacred — the book quotes Jerry Parker warning that a system whose results are sensitive to small changes in a parameter like breakout length is not robust, and recommends testing rather than fixating on the exact values. The system requires daily recalculation of N and can generate frequent whipsaw losses in sideways, low-trend markets; it depends on a small number of large trends per year for its edge and does not specify a market-selection process beyond diversification and correlation limits. Dollar figures and contract values in the worked examples reflect mid-2000s futures pricing and should be recalculated for current contract specifications.
