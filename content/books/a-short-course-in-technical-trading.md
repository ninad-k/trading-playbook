---
author: Perry J. Kaufman
category: Trend Following & Mechanical Systems
difficulty: beginner
doc_type: book
one_liner: A graduate-course walkthrough of trend, momentum, and volatility indicators
  with worked spreadsheet formulas, backtest tables, and explicit trading rules.
pages: 339
related:
- elder-alexander-trading-for-a-living
- curtis-faith-way-of-the-turtle
- the-complete-turtletrader-the-legend-the-lessons-the-results
- money-management-report-van-tharp
- street-smarts-laurence-connors
reviewed_pdf_pages: 5, 7-8, 10, 15, 23, 74-77, 84 (the regression-slope and moving-average
  system chapters with their backtest tables)
slug: a-short-course-in-technical-trading
source_file: A Short Course in Technical Trading.PDF
source_review: partial
tags:
- moving-average
- breakout
- momentum
- macd
- stochastic
- rsi
- volatility
- position-sizing
tier: A
title: A Short Course in Technical Trading
year: 2003
---

## Overview

Adapted from a graduate course Kaufman taught at Baruch College, this book builds technical trading from the ground up: charting trends, calculating them mathematically, controlling risk, reading momentum and oscillators, and sizing a portfolio by volatility. Each chapter pairs a concept with an Excel formula, a worked backtest table (often on Microsoft, Enron, AOL, or Amazon data from the late 1990s), and a short set of review questions, closing with informal "trading game" tips drawn from watching students trade paper accounts.

## Core thesis

Markets trend because price runs are not randomly distributed — they show a "fat tail" of longer-than-expected up or down streaks — and any of the standard trend calculations (moving average, exponential smoothing, regression slope, N-day breakout) will profit from that fat tail if applied with discipline. The choice of trend method matters less than consistently controlling risk, sizing positions by volatility, and accepting many small losses in exchange for a few large trend-following profits ("conservation of capital").

## Key concepts

- **Fat tail of price runs** — price streaks are less random than a coin flip; there are fewer short runs and more long runs than a normal distribution predicts, which is the statistical reason trend-following works.
- **Time-driven vs. event-driven trend** — a moving average reacts to the passage of time and slows to catch up with price; a breakout only changes on a new high/low "event," so it holds through sideways drift.
- **Conservation of capital** — a trend system takes many small losses (roughly 60-75% of trades lose) and a few large wins; average losing trade and holding time should be much smaller than the average winner.
- **True range** — the largest of (today's high − low), (today's high − yesterday's close), (yesterday's close − today's low); used instead of the simple daily range so gap opens are captured.
- **Front-weighted (exponential) smoothing** — each new price is blended into the trendline by a fixed percentage, giving recent prices more weight than a simple moving average of the same "length."
- **Divergence** — price makes a new high/low but the momentum/MACD/stochastic indicator makes a lower/higher extreme; signals an approaching reversal.
- **Free exposure** — placing an order just ahead of an anticipated breakout so a price gap works in your favor instead of leaving you executed at the crowd's price.
- **Lognormal volatility** — in equities, absolute daily volatility rises roughly in proportion to the natural log of price, so risk (and stop distance) must widen as price rises.
- **Stop close only** — an order type that exits only if the closing price, not the intraday price, breaches the stop level; used to avoid single-tick false breakouts.
- **Two-trend (dual moving average) risk control** — pairing a fast and slow moving average reduces the giveback at trend turns compared with a single slow trend.

## Rules and setups

1. **N-day breakout (three variants).** Rule 1: buy on a new N-day high, sell on a new N-day low (intraday). Rule 2 (more conservative): only act if the close itself makes the new high/low, avoiding one-tick false breaks. Rule 3 (compromise): buy on an N-day high if today's close is also higher than yesterday's close; symmetric for sells. A 20-day or 30-week rolling breakout is the common default; risk equals the width between the resistance and support levels used for entry.
2. **Moving-average trend.** Enter/reverse when the moving average itself turns up or down (compare today's MA value to yesterday's), not merely when price crosses the average. Kaufman's backtests on Microsoft (5-year window) show all periods from 5-200 days roughly profitable except calculation lengths of 20-55 days; profit per trade and profit factor rise steadily as the calculation period lengthens, while win rate stays near 25-35%.
3. **Exponential smoothing equivalence.** A moving average of length N maps to a smoothing percentage of 2/(N+1) (e.g., 20-day MA ≈ 9.5% smoothing, 40-day ≈ 4.9%, 80-day ≈ 2.47%). Trade the smoothed trendline the same way as a moving average: direction of the line, not price vs. line.
4. **Regression slope trend.** Fit a linear regression over a fixed window (Kaufman uses ~125-day/6-month windows); trend is up while the slope is positive, down when negative. Use the *slope value itself*, not price relative to the line.
5. **Two-moving-average risk control.** Use a slow MA (50-200 days) and a fast MA (5-30 days). Buy when both are rising; exit when the fast one turns down (it always turns first). Produces more, smaller trades with a better reward-to-risk ratio than a single slow trend, at the cost of some total profit.
6. **Stop-loss placement.** Never set a stop closer than 1.5x the current daily volatility (true range); place the initial stop below the nearest real support level (for longs). Never lower a stop once raised (raise only, tied to new support levels or a fresh trendline) — with the single explicit exception of an increase in volatility, where the stop may be lowered to the low of the most volatile day.
7. **Volatility-scaled profit/stop targets.** For short-term trades: profit target = entry + (2 × average daily range); stop = entry − (3 × average daily range) for a long. Profit target is deliberately closer than the stop because the nearer order is the one most likely to be hit.
8. **Percentage price bands.** Upper band = 20-day MA × 1.05; lower band = 20-day MA / 1.05 (or × 0.95). Buy near the lower band, sell near the upper band, exit near the middle; works best in slow, sideways markets and fails badly in sustained trends (see [[a-short-course-in-technical-trading--bollinger-band-system]]).
9. **Portfolio position sizing by volatility.** To equalize risk across positions of different price/volatility: solve simultaneously for shares of each instrument so that (shares × instrument's average daily volatility) is equal across the book, subject to a total-capital constraint. Example: $10,000 split between a $100 stock with $3/day volatility and a $25 stock with $1/day volatility solves to 57 and 171 shares respectively.
10. **Exposure discipline.** Do not hold any single position more than about 30% of the time; the less time and less capital exposed, the smaller the damage from an unpredictable price shock (Kaufman cites 9/11 as the canonical example).
11. **Diversification cap.** Real risk reduction from adding uncorrelated markets levels off after three or four positions; more than four adds little further benefit (and in a systemic crisis correlations go to 1 regardless).
12. **Risk per trade (paper-trading game rule).** Never risk more than 20% of capital on one trade; 10% is a better target. Expect roughly 2-3 of every 4 concurrent positions to be profitable if positions are properly diversified.

## Risk and money management

Kaufman treats risk control as inseparable from trend-following: a stop-loss "fights with the trend system" if set too tight relative to the trend's natural noise, so stop distance must scale with volatility (never closer than 1.5x current true range) and with the speed of the trend being traded (slower trend = farther stop). He favors true range over simple daily range so gap opens count toward risk, and recommends multiplying the average true range by a "stop factor" (e.g., 3x) and a smaller "profit factor" (e.g., 2x) for short-term volatility-based exits. For portfolios, position sizes should be set so each holding contributes roughly equal dollar volatility — not equal share counts or equal dollar value, both of which let the highest-volatility name dominate the book's risk. He also stresses that stops do not protect against price shocks (gaps discontinuously through the stop); the only real defenses are smaller position size and shorter average holding time (target under ~30% market exposure).

## Psychology and discipline

The book repeatedly frames trend trading as "conservation of capital": traders must accept a majority of small losing trades as the unavoidable cost of capturing the occasional large winning trend, and must not personalize losses. Kaufman warns against curve-fitting rules to a single chart in hindsight (his own MACD ±2.00 threshold example), against day trading before mastering the basics, against buying on minor support pullbacks (a habit that tends to lose money), and against mistaking a lucky price-shock windfall for skill. He distinguishes a reasoned market "bias" from wishful thinking, and insists a trader must know the exit — both profit target and stop — before entering, and should log the technical reason for every trade rather than a vague hunch.

## Chapter map

- Ch 1 — Timing Is Everything — why systematic, rule-based trading beats discretionary chart-gazing.
- Ch 2 — Charting the Trend — hand-drawn trendlines, support/resistance, redrawing rules.
- Ch 3 — Breakout Trends — sideways ranges, rolling N-day breakout, false breakouts, fat-tail statistics.
- Ch 4 — Calculating the Trend — moving average, exponential smoothing, regression slope, and breakout compared head-to-head with backtest tables.
- Ch 5 — The Trading Game — a paper-trading exercise applying the rules learned so far.
- Ch 6 — Channels and Bands — trend channels, percentage bands, Bollinger bands, regression bands.
- Ch 7 — Event-Driven Trends — swing charting and point-and-figure charting as time-independent trend methods.
- Ch 8 — Controlling the Risk of a Trade — stop-loss placement, stop close only, two-moving-average risk control.
- Ch 9 — One-Day Chart Patterns and Reversals — gaps (common, breakaway, runaway, exhaustion) and reversal bars.
- Ch 10 — Continuation Patterns — flags, pennants, triangles.
- Ch 11 — Top and Bottom Formations — double tops/bottoms, head-and-shoulders, rounded turns.
- Ch 12 — Retracements, Reversals, Fibonacci Numbers, and Gann — classic retracement levels and their limits.
- Ch 13 — Volume, Breadth, and Open Interest — confirming price action with participation data.
- Ch 14 — Momentum and MACD — momentum as speed/acceleration, full MACD calculation, divergence trading.
- Ch 15 — Overbought/Oversold Indicators and Double Smoothing — stochastic (%K/%D/%D-slow) and 14-day RSI, divergence rules.
- Ch 16 — Managing Your Entry and Exit — order types and execution timing.
- Ch 17 — Volatility and Portfolio Management — four volatility measures, lognormal volatility, volatility-based position sizing.
- Ch 18 — Dow Theory — the classical index-confirmation framework revisited for modern markets.

## Strengths and caveats

Every technique is backed by a reproducible spreadsheet formula and a real backtest table (not just a chart picture), which makes this unusually easy to code directly from the text. The examples lean heavily on late-1990s/2000-2001 dot-com-era stocks (Enron, AOL, Amazon, Microsoft) — Enron's collapse and 9/11 both appear as case studies, which dates some illustrations but the mechanics are era-independent. Kaufman is explicit that back-tested parameter windows (e.g., "sell when MACD crosses +2.00") that look great on one chart can be curve-fit and should be treated skeptically; he flags this himself rather than glossing over it. Coverage of pattern-based chapters (candlesticks-adjacent one-day patterns, Fibonacci/Gann, Dow Theory) is comparatively thin (a chapter each) versus the depth given to moving averages, breakouts, and oscillators.

## Who should read it

Beginner-to-intermediate traders who want a self-contained, formula-level introduction to trend and momentum indicators and basic volatility-based position sizing, ideally with a spreadsheet open alongside the text to reproduce the examples.

## Related books in this library

- [[elder-alexander-trading-for-a-living]] — complements Kaufman's indicator mechanics with a fuller psychology and money-management framework (the 2% rule).
- [[curtis-faith-way-of-the-turtle]] and [[the-complete-turtletrader-the-legend-the-lessons-the-results]] — both build on the same N-day breakout / volatility-sizing logic Kaufman introduces, taken to a fully mechanical system.
- [[money-management-report-van-tharp]] — deeper treatment of the position-sizing-by-volatility idea Kaufman sketches in Chapter 17.
- [[street-smarts-laurence-connors]] — a more short-term, pattern-driven counterpart to Kaufman's oscillator chapters (stochastic, RSI).
