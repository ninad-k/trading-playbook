---
title: "The 4x1 Strategy and Median Grid"
author: Dirk du Toit
year: 2004
slug: the-bird-watching-lion-country--4x1-median-grid
parent: the-bird-watching-lion-country
tier: A
category: "Forex Mechanics & Macro Drivers"
doc_type: system
pages: 236
one_liner: "Du Toit's core forex day-trading method: one currency, low gearing with multiple staggered entries, one direction only, entered within a self-drawn support/resistance grid divided into four quadrants."
tags: [forex, median-grid, gearing, cost-averaging, day-trading, trend-following]
difficulty: intermediate
related: [the-bird-watching-lion-country, day-trading-the-currency-market]
source_file: "The Bird Watching Lion Country.pdf"
---

## What it is

The 4x1 Strategy is Dirk du Toit's discretionary forex day-trading method, named for its four constraints: one currency, one lot (low gearing), one direction, one-percent profit edge. Median Trading is the methodology used to deploy it: a manually-drawn horizontal support/resistance grid ("comfort zone") on a single currency pair, split into four price quadrants, that gives the trader a fixed reference point for judging whether the current price is relatively high or low. The two are combined - the 4x1 rules for what/how much/which direction to trade are executed using the median grid's quadrants to decide where to enter and add to positions. The method is built around the premise that FX prices oscillate around a median band most of the time and periodically "overshoot" to test the grid's extremes, and that low leverage combined with multiple staggered entries (cost averaging) beats a single precisely-timed entry with tight stops.

## Rules

**Instrument and direction**
1. Trade one currency pair at a time (author trades EUR/USD, occasionally GBP/USD); avoid non-USD cross pairs due to thinner liquidity and less transparent fundamentals.
2. Establish a medium/long-term fundamental trend view for that pair (the "one-way play") and trade exclusively in that direction - no counter-trend shorts in an uptrend, no counter-trend longs in a downtrend.

**Building the median grid**
3. Use a 60-minute chart with roughly 3-4 weeks of price history.
4. Identify the clearest support level (bottom) and resistance level (top) and draw horizontal lines at each; typical grid width is ~300-400 pips on EUR/USD and ~400-500 pips on GBP/USD (roughly 2.5-3% of the underlying price).
5. Identify the median band: the price zone (roughly 20-40 pips wide) in the middle of the grid where price action is most concentrated ("busy" middle, "quiet" extremes).
6. Divide the grid into four equal quadrants (Q1 = bottom, through Q4 = top).

**Entries (in an established uptrend)**
7. Treat Q1 and Q2 (bottom half) as the primary buying zone - highest-probability, lowest-risk entries.
8. Treat Q3 (just above median) as a valid continuation-buy zone but with reduced position size/gearing.
9. Treat Q4 (top quadrant) as high-risk: only trade it for a confirmed breakout attempt, and expect prices there to be quickly reclaimed by the median more often than not.
10. Enter using price levels, not pinpoint timing: a valid entry zone is a 20-40 pip range near a quadrant's boundary; do not attempt to time the exact turning point, since intraday moves are treated as effectively random noise around the fundamental direction.
11. Use multiple staggered entries rather than one large entry: as price dips further into lower quadrants, add further entries at each new level (cost averaging), broadening the position like a base-up pyramid.

**Sizing**
12. Cap gearing at roughly 2:1-3:1 per individual entry (position size ÷ account margin).
13. Allow total exposure across all simultaneous entries in a grid to run higher (worked examples reach 10:1-15:1) but only as a result of multiple small entries added over time, never as a single large position.
14. Reduce gearing as price rises deeper into the upper quadrants (higher risk zone); increase willingness to add size in lower quadrants.

**Exits**
15. Take profit once an "acceptable" gain exists - benchmark roughly 30-40 pips (~1% of capital at 3:1 gearing per entry) - rather than trying to maximize every move; treat this as a repeatable daily/per-trade target, not a ceiling.
16. Allow profitable entries to run through periods of adverse movement (including dipping temporarily out-of-the-money) as long as the original directional/fundamental setup is unchanged.
17. Exit for loss when the fundamental setup that justified the original entry no longer holds - not simply because the position is temporarily underwater or because of a fixed pip distance.
18. On a confirmed break of the grid's extreme against the trade, expect a new grid to form roughly 300-400 points further out; either wait for the new range to establish before re-entering, or scale out immediately.

## Risk

Gearing discipline substitutes for tight stop-losses as the primary risk control: the author's own worked comparison shows a 20:1-geared position with 30-pip stops wiped out by a cumulative 175-pip adverse move, versus a 1:1-geared position that would require a 2,500-pip move for the same loss. Set a maximum tolerable account drawdown before trading (example: 25%) but begin actively managing (scaling out, reducing gearing, or hedging) well before reaching it (example: start asking "when do I act" at 10% drawdown, act by 5%). If stops are used, place them beyond a genuine support/resistance level, never at a fixed tight distance (30-40 pips from entry is explicitly called too tight for normal FX volatility) - the goal is a stop that is unlikely ever to be triggered, not a mechanical exit. Avoid opening or holding tight positions immediately around scheduled high-impact data releases. Hedging (an offsetting position in the same pair) is available as an advanced, discretionary damage-control tool but is not recommended for novices.

## Caveats

This is a discretionary system, not a mechanical one: grid placement (where exactly to draw support/resistance and the median), what counts as an "acceptable" profit, and whether the "fundamental setup" is still valid are all left to trader judgment and are not reducible to a fixed formula as presented in the book. The author states at the time of writing that he has not rigorously backtested or automated the method and flags (without resolving) the risk of curve-fitting in his own ongoing automation efforts. Specific pip widths and leverage assumptions reflect mid-2000s EUR/USD and GBP/USD volatility and retail leverage norms and should be recalibrated (e.g., as a percentage of current price/ATR) rather than applied as fixed pip counts in other regimes or instruments.
