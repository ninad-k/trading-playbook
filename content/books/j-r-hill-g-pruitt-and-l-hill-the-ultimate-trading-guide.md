---
author: John R. Hill, George Pruitt, Lundy Hill
category: Trend Following & Mechanical Systems
difficulty: intermediate
doc_type: book
one_liner: Futures Truth's founders teach supply/demand chart reading, then walk through
  building, testing, and money-managing mechanical trading systems.
pages: 302
related:
- curtis-faith-way-of-the-turtle
- turtletrader
- george-pruitt-building-winning-trading-systems-with-tradestation
- elder-alexander-trading-for-a-living
- elliott-waves-principle
reviewed_pdf_pages: 3-4, 6-7, 13 (contents, market-stage definitions, the capital
  allocation model and the case-study entry rules)
slug: j-r-hill-g-pruitt-and-l-hill-the-ultimate-trading-guide
source_file: J R Hill G Pruitt And L Hill - The Ultimate Trading Guide.pdf
source_review: partial
tags:
- chart-patterns
- mechanical-systems
- money-management
- backtesting
- swing-trading
- wyckoff
- elliott-wave
- futures
tier: A
title: The Ultimate Trading Guide
year: 2000
---

## Overview

Written by John Hill (founder of Futures Truth, the independent system-tracking service), George Pruitt (its director of research), and Lundy Hill, this book splits into two halves. The first teaches discretionary chart reading based on supply-and-demand "stages of market action" (a Wyckoff-derived framework), short-term bar patterns, trendline/channel trading, swing charts, and an introduction to Drummond Geometry. The second is a manual on building, testing, and money-managing mechanical trading systems, drawing on Futures Truth's database of tracked commercial systems. Nearly every claim is backed by an actual backtest (1983-1999 futures data, $75-100 commission/slippage assumed), unusually concrete about what works versus what merely sounds plausible.

## Core thesis

Markets cycle through four repeating stages: accumulation (bottom), markup (run-up), distribution (top), and markdown (run-down). About 85% of the time a market sits in accumulation or distribution congestion, where only small, quick profits should be taken; the other 15% is the run-up/run-down "thrust" where the real money is made. A trader's job is to locate where price sits in this cycle, buy support/buy zones and sell resistance/sell zones during congestion, and hold for the bigger move once a thrust is confirmed. On the systems side, a mechanical system must originate from a sound supply/demand idea, not a computer's curve-fit search of parameter space; testing validates an idea, it doesn't invent one.

## Key concepts

- **Stages of market action** — accumulation, markup (run-up/thrust), distribution, markdown (run-down); ~85% congestion vs. ~15% trending time.
- **Selling/buying climax** — wide-range bars with an outsized, high-volume final bar marking exhaustion and the start of accumulation (or distribution).
- **Sign of strength / weakness** — a breakout past a prior top (or bottom) by at least one average bar range that holds several bars, confirming the set-up is complete.
- **Terminal shakeout** — a sharp break below the accumulation range that snaps back just as fast (a "V bottom"); traps late shorts.
- **Reaccumulation / redistribution** — congestion after a thrust that usually resolves the same direction it entered.
- **Spring / upthrust** — price probes below (above) a pivot low (high), finds no follow-through, and reverses hard.
- **Three-Day Equilibrium Reverse (3DE)** — a three-bar reversal test using the nine highs/lows/closes of the last three bars and their average.
- **0-2 / 0-4 line** — Elliott-wave-derived trendlines connecting wave pivots, used to time corrective-leg entries.
- **Drummond Geometry / PLdot** — short-term moving-average "dots" plus two-bar termination lines; support/resistance strength is judged by alignment across coordinated time frames.
- **Risk of ruin** — probability of losing all capital, driven by bet size, win rate, and win:loss ratio.
- **Capital Allocation Model** — sizing contracts from equity, mean monthly system return, and a market-risk measure (e.g., 30-day ATR in dollars).
- **Walk-forward / adaptive parameters** — re-testing optimized parameters on unseen data, or floating parameters with volatility, to curb curve-fitting.

## Rules and setups

1. **Support-zone long entry** (Ch 1 case study): buy on a close above 2+ prior closes on a wide-range bar with expanding volume, or a half-range breakout from the open, on the 2nd-3rd pullback into support (not the 4th — zones tend to fail on that test). Stop: one average range below the reaction low. Target: the accumulation "box" width projected up, or 50%/100% of the run-up thrust added to the high.
2. **Trendline and Four-Close System (TL4C)**: trade only with the trend; draw a trendline across the last two pivot highs/lows (2+ rising pivots in the last 20 days); buy on a close above the line where close > open, close > the prior 4 closes, and range > average. Stop below the most recent pivot low, moved to breakeven as a cushion develops.
3. **Simple Moving Average Crossover** (backtested 1983-1999): buy when the 13-day MA of closes crosses above the 39-day MA and yesterday's close exceeds the close 40 days back. Stop = 5x the 20-day ATR, trailed 5 ATRs behind price once 5 ATRs of profit accrue. Full rules: [[j-r-hill-g-pruitt-and-l-hill-the-ultimate-trading-guide--moving-average-crossover-system]].
4. **Short-Term Volatility Based Open Range Breakout** (Larry Williams-style "buy easier/sell easier"): buy/sell stops set at 50%/100% of the 3-day range from the open, the split set by yesterday's close direction. Stop = 3x the 10-day ATR, moved to breakeven after 3 ATRs profit. Full rules: [[j-r-hill-g-pruitt-and-l-hill-the-ultimate-trading-guide--volatility-breakout-system]].
5. **S&P Day Trade System**: an opening-range breakout plus a counter-trend "key of the day" (H+L+C average) fade; trades only when the 10-day open-to-close range is at least half the 10-day ATR; flat by the close; fixed $300 stop. Full rules: [[j-r-hill-g-pruitt-and-l-hill-the-ultimate-trading-guide--sp-day-trade-system]].
6. **Reversal day filter**: a bar trading beyond the prior day's range then closing back inside it isn't tradable alone, but with a 50-day trend filter and an exit on any 60%-of-range opening breakout, it shows a real edge — just not enough to clear costs unfiltered.

## Risk and money management

The authors treat money management as the majority of the trading decision — 75% sizing/risk, 25% signal generation, by their own estimate. Risk of ruin is framed with worked examples: on $20,000 capital, betting $5,000/trade with a 45% per-trade loss chance gives roughly a 4% chance of ruin on four straight losers, versus 0.17% at $2,500/trade. Their long-run ruin formula, PR = ((1-TA)/(1+TA))^IU (TA = win% - loss%, IU = capital / bet size), shows eventual-ruin probability near 45% at a 10% edge and 4 units, versus under 2% at 20 units: "don't bet the farm." The **Capital Allocation Model** sizes contracts as (equity x acceptable risk %) / market risk (e.g., 30-day ATR in dollars); a worked bond example — $100,000 capital, $1,125 ATR-risk per contract, 5% risked — yields 4 contracts and a ~48%/year expected return at a $1,000/month per-contract average. Diversification is the free lunch: anti-correlated markets and systems raise the profit-to-drawdown ratio faster than they raise drawdown.

Beyond net profit, the authors flag drawdown (max and average), longest flat period, profit-to-loss ratio, average trade, most consecutive losses, Sharpe ratio, percent winning months, and long-vs-short split (winning only on one side flags regime dependence). Chapter 12's model portfolios show scale: $10,000 trades 1-2 markets on one system; $300,000 supports five systems across a dozen-plus markets with drawdown far below the sum of individual-market drawdowns.

## Psychology and discipline

The book is light on psychology relative to its technical content, but repeats a few behavioral rules: don't chase a market at new highs/lows — enter on a pullback, on your terms; "learn to love small losses"; liquidate the moment a trade "doesn't act right"; and don't try to catch 90% of every move — small, repeated chunks compound better than home runs. The authors note roughly 80% of traders lose money and technology hasn't changed that, only execution cost has. They warn against "rainbow merchants" (vendors selling curve-fit hindsight) and against over-optimizing: added logic must be universal across markets, not tuned per-market ("don't trade soybeans on Tuesdays" is curve-fitting; "skip trades after abnormally high volatility" is not).

## Chapter map

- Ch 1 — The Set-Ups or the Big Picture — stages of market action, buy/sell zones, a five-trade GM case study.
- Ch 2 — Elliott Wave Theory — a trading-oriented condensation of wave counts and targets.
- Ch 3 — Bar Charts and Their Forecasting Ability — inside/outside/reversal days, 3-day equilibrium reverse, gaps.
- Ch 4 — Channel and Trendline Trading — 0-2/0-4 lines, the TL4C system, trend channel trading.
- Ch 5 — Swing Trading — swing charts, support/resistance mechanics, time-and-price projections.
- Ch 6 — Patterns — 19 named bar patterns plus Keltner/Bollinger channel trading.
- Ch 7 — Drummond Geometry and the PLdot — multi-time-frame support/resistance coordination.
- Ch 8 — Introduction to Mechanical Trading Systems — why (and why not) to buy a system.
- Ch 9 — Where to Start — indicator backtests plus the MA crossover, volatility breakout, and S&P day trade rules.
- Ch 10 — Historical Testing: A Blessing or a Curse — curve-fitting, walk-forward testing, adaptive parameters.
- Ch 11 — Money Management — risk of ruin, the Capital Allocation Model, stop/target placement.
- Ch 12 — Turnkey Systems and Portfolios — five model portfolios from $10,000 to $300,000.
- Ch 13 — Top Ten Systems of All Time — ten commercial vendor profiles (contacts, not disclosed rules).

## Strengths and caveats

The book's biggest strength is that almost every technique is backtested with stated commission/slippage and test-period dates rather than asserted on faith — rare among pattern-trading books. The weakness is dated infrastructure discussion (continuous-contract data vendors, 1999-era software) and Chapter 13's "Top Ten Systems," a directory of commercial vendors with contact numbers and no disclosed rules. Some discretionary techniques (0-2/0-4 lines, Drummond Geometry) are explicitly flagged by the authors as resistant to mechanical coding, so readers wanting pure rules should focus on Chapter 9's three fully-specified systems. The heavy reliance on 1983-1999 futures data means results are a starting point for re-testing, not a live edge.

## Who should read it

Futures and stock traders who want to combine discretionary Wyckoff-style chart reading with a rigorous, testable approach to system design and position sizing. Best suited to readers comfortable with bar charts who want concrete, numbered rules and a realistic treatment of money management and risk of ruin. Less useful for pure discretionary or fundamental traders.

## Related books in this library

- [[curtis-faith-way-of-the-turtle]] — another mechanical trend-following system built and tested the way Futures Truth evaluates vendor systems.
- [[turtletrader]] — the original Donchian-breakout rules this book's channel discussion draws on.
- [[george-pruitt-building-winning-trading-systems-with-tradestation]] — co-author George Pruitt's dedicated guide to coding and testing systems.
- [[elder-alexander-trading-for-a-living]] — a psychology- and money-management-forward counterpart to this book's mechanical, backtest-driven approach.
- [[elliott-waves-principle]] — the source theory behind Chapter 2's trading-oriented condensation.
