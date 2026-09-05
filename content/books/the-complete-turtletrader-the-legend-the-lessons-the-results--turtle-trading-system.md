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

A complete, mechanical trend-following system: two price-breakout entry/exit variants (System One and System Two), a volatility-based unit for position sizing and stops, and rules for pyramiding winners and capping portfolio risk. It is market-agnostic — the Turtles traded it unchanged across roughly 20 futures, currency, and interest-rate markets. See [[turtlerules]] for the original written rules and [[curtis-faith-way-of-the-turtle]] for a first-person trading account.

## Rules

**Volatility unit ("N")**: the market's Average True Range — the greatest of (today's high − today's low), (yesterday's close − today's high), (yesterday's close − today's low) — as a 20-day moving average, recalculated daily.

**Entries — System One (S1)**: buy a new 20-day high; short a new 20-day low. Skip the signal if the prior S1 trade (either direction) was a winner, unless that prior trade lost ≥ 2N, in which case take the new signal regardless.

**Entries — System Two (S2)**: buy a new 55-day high; short a new 55-day low. No skip filter. S2 also serves as a fail-safe: if an S1 signal was skipped and the market keeps trending, the S2 breakout re-enters the trade.

**Exits**: whichever comes first of (a) a 2N stop (2 × N behind the position's most recently pyramided entry) or (b) the opposite-direction breakout for the system used to enter — 10-day for S1, 20-day for S2.

**Position size (1 unit)**: account risk = 2% of equity; contract risk = 2N × dollar value per point; contracts per unit = account risk ÷ contract risk, rounded down. Example: $100,000 account, corn N = 7¢ ($50/cent) → contract risk = 7¢×$50×2 = $700; account risk = $2,000; units = 2,000÷700 = 2.67 → trade 2 contracts.

**Pyramiding**: add one unit per 1N favorable move, up to 5 units per market. Stop at ½N on the first unit's first day; from the second unit on, use the standard 2N stop, raising the stop on all units to the newest unit's 2N level each time one is added.

**Portfolio limits**: cap at 4-5 units per market. Reduce combined exposure across highly correlated markets (corn/soybeans, gold/silver) rather than treating each as independent; one approximation used in the book nets correlated long and short groups as: larger group's unit count − (smaller group's unit count ÷ 2).

**Drawdown response**: cut the per-trade risk percentage as equity draws down (matching the money-management overlay in [[forex-misc-money-management-ryan-jones--fixed-ratio-position-sizing]]), restoring it only as equity recovers.

**Order type**: all entries and exits are stop orders triggered by the breakout or stop level — no discretion on whether to take a valid signal.

## Risk

Worst-case single-market loss is bounded by the unit cap and 2N stops: five units × 2% each ≈ 10% of equity before the drawdown-response rule reduces exposure further. Because entries need no confirmation beyond the breakout, the system produces a high rate of small losing trades (documented win rates near 35-40%) offset by a few large trending winners — expectancy, not accuracy, is the basis for profitability. Correlated-market unit limits exist because unhedged exposure to several markets moving together effectively multiplies single-market risk beyond what the per-market 2% figure suggests.

## Caveats

The 20/55/10/20-day parameters are explicitly not sacred — the book quotes Jerry Parker warning that a system sensitive to small parameter changes is not robust, and recommends testing rather than fixating on exact values. The system requires daily recalculation of N and can whipsaw in sideways, low-trend markets; it depends on a small number of large trends per year and specifies no market-selection process beyond diversification and correlation limits. Dollar figures reflect mid-2000s futures pricing and should be recalculated for current contract specifications.
