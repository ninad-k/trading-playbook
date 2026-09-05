---
title: "The Ultimate Trading Guide"
author: "John R. Hill, George Pruitt, Lundy Hill"
year: 2000
slug: j-r-hill-g-pruitt-and-l-hill-the-ultimate-trading-guide
tier: A
category: Trend Following & Mechanical Systems
tags: [chart-patterns, mechanical-systems, money-management, backtesting, swing-trading, wyckoff, elliott-wave, futures]
difficulty: intermediate
doc_type: book
pages: 302
one_liner: "Futures Truth's founders teach supply/demand chart reading, then walk through building, testing, and money-managing mechanical trading systems."
related: [curtis-faith-way-of-the-turtle, turtletrader, george-pruitt-building-winning-trading-systems-with-tradestation, elder-alexander-trading-for-a-living, elliott-waves-principle]
source_file: "J R Hill G Pruitt And L Hill - The Ultimate Trading Guide.pdf"
---

## Overview

Written by John Hill (founder of Futures Truth, the independent system-tracking service), George Pruitt (its director of research), and Lundy Hill, this book splits into two halves. The first teaches discretionary chart reading based on supply-and-demand "stages of market action" (a Wyckoff-derived framework), short-term bar patterns, trendline and channel trading, swing charts, and an introduction to Drummond Geometry. The second half is a manual on building, testing, and money-managing mechanical trading systems, drawing on Futures Truth's database of tracked commercial systems. Nearly every claim is backed by an actual backtest (1983-1999 futures data, $75-100 commission/slippage assumed), which makes the book unusually concrete about what works and what merely sounds plausible.

## Core thesis

Markets cycle through four repeating stages: accumulation (bottom), markup (run-up), distribution (top), and markdown (run-down). About 85-86% of the time a market sits in accumulation or distribution congestion, where only small, quick profits should be taken; the other 15% is the run-up/run-down "thrust" phase where the real money is made. A trader's job is to locate where price sits in this cycle, buy in support/buy zones and sell in resistance/sell zones during congestion, and hold for the bigger move once a thrust is confirmed. On the systems side, the authors argue that a mechanical system must originate from a sound supply/demand idea, not from a computer's curve-fit search of parameter space; testing exists to validate an idea, not to invent one.

## Key concepts

- **Stages of market action** — accumulation, markup (run-up/thrust), distribution, markdown (run-down); each averages ~85% congestion vs. ~15% trending time.
- **Selling/buying climax** — a cluster of wide-range bars with an outsized final bar and a volume spike that marks exhaustion and starts accumulation (or distribution).
- **Sign of strength / sign of weakness** — a breakout that exceeds a prior top (or falls below a prior bottom) by at least one average bar range and holds for several bars, confirming the set-up is complete.
- **Terminal shakeout** — a sharp break below the whole accumulation range that snaps back just as fast (a "V bottom"); traps late shorts.
- **Reaccumulation / redistribution** — congestion after a thrust that usually resolves in the same direction it entered, per Newton's-law-style trend persistence.
- **Spring / upthrust** — price probes below (above) a pivot low (high), finds no follow-through supply/demand, and reverses hard.
- **Three-Day Equilibrium Reverse (3DE)** — a three-bar reversal test using the nine highs/lows/closes of the last three bars and their average.
- **0-2 line / 0-4 line** — Elliott-wave-derived trendlines connecting wave pivots, used to time entries on corrective legs.
- **Drummond Geometry / PLdot** — short-term moving-average "dots" plus two-bar termination lines; support/resistance is judged strong or weak by whether it lines up across coordinated time frames (e.g., daily inside weekly inside monthly).
- **Risk of ruin** — the statistical probability of losing all trading capital, driven by bet size (risk per trade), win rate, and win:loss ratio.
- **Capital Allocation Model** — sizing contracts from equity, mean monthly system return, and a market-risk measure (e.g., 30-day average true range in dollars).
- **Walk-forward / adaptive parameters** — re-testing optimized parameters on unseen data, or letting parameters float with volatility (e.g., channel length scaled to 30-day standard deviation, floored/capped) to reduce curve-fitting.

## Rules and setups

1. **Support-zone long entry (Chapter 1 case study)**: buy on a close above two-plus prior closes on a wide-range bar (range > 10-day average range) with expanding volume, OR on a half-range breakout from the open (50% of prior day's range added to the open), on the 2nd-3rd pullback into the support zone (not the 4th — zones tend to fail on the fourth test). Stop: one average range below the reaction low, or one entry-bar-range below the entry bar's low; move up once breathing room appears, and exit if the market doesn't respond within ~3 bars. Target: the width of the accumulation "box" projected up, or 50%/100% of the run-up thrust added to the high.
2. **Trendline and Four-Close System (TL4C)**: trade only with the trend; draw a trendline across the last two pivot highs (lows for a sell) with 2+ rising pivot lows in the last 20 days; buy on a close above the line where close > open, close > each of the prior 4 closes, and range > average range. Stop below the most recent pivot low, moved to breakeven once a half-range cushion develops.
3. **Simple Moving Average Crossover** (fully mechanical, backtested 1983-1999): buy on the open when the 13-day MA of closes crosses above the 39-day MA and yesterday's close > the close 40 days ago (mirror for shorts). Initial stop = 5x the 20-day average true range (ATR); trail the stop 5 ATRs behind price once 5 ATRs of profit accrue; reverse on the opposite signal. (Full rules and standalone page: [[j-r-hill-g-pruitt-and-l-hill-the-ultimate-trading-guide--moving-average-crossover-system]].)
4. **Short-Term Volatility Based Open Range Breakout** (Larry Williams-style "buy easier/sell easier" day system): buy stop/sell stop set as a percentage of the 3-day high-low range from the day's open, with the percentage split 50/100 depending on whether yesterday's close was down (buy easier) or up (sell easier). Stop = 3x the 10-day ATR, moved to breakeven after 3 ATRs profit. (Full rules: [[j-r-hill-g-pruitt-and-l-hill-the-ultimate-trading-guide--volatility-breakout-system]].)
5. **S&P Day Trade System**: combines an opening-range breakout with a counter-trend "key of the day" (average of H+L+C) fade; only trades when the 10-day average open-to-close range is at least 50% of the 10-day average true range; flat by end of day; fixed $300 money-management stop; no trades before 10:00am or after 3:30pm ET. (Full rules: [[j-r-hill-g-pruitt-and-l-hill-the-ultimate-trading-guide--sp-day-trade-system]].)
6. **Reversal day filter**: a bar that trades beyond the prior day's range then closes back inside it (a one-day sentiment flip) is not tradable alone, but combined with a trend filter (yesterday's close vs. the close 50 days back) and an exit on any 60%-of-prior-range opening breakout, it shows a statistical edge — just not enough to clear commission and slippage without added filters.

## Risk and money management

The authors treat money management as the majority of the trading decision (they estimate 75% of the decision process is sizing/risk, only 25% is signal generation). Risk of ruin is framed with worked examples: on $20,000 capital, betting $5,000/trade with a 45% chance of loss per trade gives roughly a 4% chance of ruin on four straight losers, versus 0.17% at $2,500/trade — cut the bet size and ruin risk falls fast. Their longer-run ruin formula, PR = ((1-TA)/(1+TA))^IU (TA = trading advantage = win% - loss%, IU = initial number of trading units = capital / bet size), shows probability of eventual ruin at 10% edge and 4 units near 45%, versus under 2% at 20 units — the clearest single takeaway is "don't bet the farm." The **Capital Allocation Model** sizes contracts as: number of contracts = (equity x acceptable risk %) / current market risk (e.g., 30-day ATR in dollars); expected monthly return then scales with contract count. A worked bond example: $100,000 capital, $1,125 average 30-day-ATR risk per contract, risking 5% of equity per trade ($5,000) yields 4 contracts and a ~48%/year expected return at the historical $1,000/month per-contract average — the same system risking only 3% nets fewer contracts, lower return, but shallower expected drawdown. Diversification is treated as the free lunch: combining anti-correlated markets and anti-correlated systems raises the ratio of profit to maximum drawdown faster than it raises drawdown itself.

For performance evaluation, beyond net profit the authors flag: maximum drawdown, average drawdown, longest flat period, profit-to-loss ratio, average trade, most consecutive losses, Sharpe ratio, percent winning months, and long vs. short profit split (a system that only wins on one side is a red flag for regime dependence). Chapter 12's turnkey portfolios illustrate scale: a $10,000 account can realistically trade only 1-2 markets on one system, while $300,000 supports five systems across a dozen-plus markets with total drawdown far below the naive sum of individual-market drawdowns.

## Psychology and discipline

The book is light on psychology relative to the technical and systems content, but returns repeatedly to a few behavioral rules: don't chase a market making new highs/lows (enter on your terms, on a pullback, not at the extreme); "learn to love small losses" because a winner is always the next trade; liquidate the moment a trade "doesn't act right" rather than hoping it turns around; and don't try to catch 90% of every move — small, repeated chunks compound better than swinging for home runs. The authors are candid that roughly 80% of traders lose money and that technology (fast data, cheap software) has not changed that ratio — only execution cost has improved. They also warn against "rainbow merchants" (system vendors selling curve-fit hindsight) and against over-optimizing: a system's logic additions must be universal across markets and conditions, not tuned per-market (e.g., "don't trade soybeans on Tuesdays" is curve-fitting; "skip trades after abnormally high volatility" is not).

## Chapter map

- Ch 1 — The Set-Ups or the Big Picture — Wyckoff-style stages of market action, buy/sell zones, a five-trade GM case study.
- Ch 2 — Practical Applications of the Elliott Wave Theory — a trading-oriented condensation of Elliott wave counts and targets.
- Ch 3 — Bar Charts and Their Forecasting Ability — inside/outside/reversal days, three-day equilibrium reverse, gap and opening-range statistics.
- Ch 4 — Channel and Trendline Trading — 0-2/0-4 lines, the TL4C system, trend channel trading.
- Ch 5 — Swing Trading — swing charts, support/resistance zone mechanics, time-and-price projections.
- Ch 6 — Patterns — 19 named entry/exit bar patterns (springs, upthrusts, dynamite triangle, narrow/wide range, two-day flip, etc.) plus Keltner/Bollinger channel trading.
- Ch 7 — Drummond Geometry and the PLdot — multi-time-frame support/resistance coordination.
- Ch 8 — Introduction to Mechanical Trading Systems — why (and why not) to buy a system.
- Ch 9 — Where to Start — data issues, indicator backtests (stochastics, RSI, MACD, CCI, Bollinger, moving averages, Donchian), and full rules for the MA crossover, volatility breakout, and S&P day trade systems.
- Ch 10 — Historical Testing: A Blessing or a Curse — curve-fitting, walk-forward testing, adaptive parameters, performance statistics.
- Ch 11 — Money Management — risk of ruin, the Capital Allocation Model, stop/target placement.
- Ch 12 — Turnkey Systems and Portfolios — five model portfolios from $10,000 to $300,000.
- Ch 13 — Top Ten Systems of All Time — profiles of ten commercial vendor systems Futures Truth tracked (contact info and general approach, not disclosed rules).

## Strengths and caveats

The book's biggest strength is that almost every technique is backtested with stated commission/slippage and test-period dates rather than asserted on faith — rare among pattern-trading books. The weakness is dated infrastructure discussion (continuous-contract data vendors, 1999-era software) and Chapter 13's "Top Ten Systems," which is really a directory of commercial vendors with contact numbers and no disclosed rules — not usable as written. Some discretionary techniques (0-2/0-4 lines, Drummond Geometry) are explicitly described by the authors themselves as resistant to mechanical coding and dependent on chart-reading judgment, so readers wanting pure mechanical rules should focus on Chapter 9's three fully-specified systems. The heavy reliance on 1983-1999 futures data means results should be treated as a starting point for re-testing, not a live edge.

## Who should read it

Futures and stock traders who want to combine discretionary Wyckoff-style chart reading with a rigorous, testable approach to system design and position sizing. Best suited to readers already comfortable with bar charts who want concrete, numbered rules (not vague pattern recognition) and a realistic treatment of money management and risk of ruin. Less useful for pure discretionary or pure fundamental traders.

## Related books in this library

- [[curtis-faith-way-of-the-turtle]] — another mechanical trend-following system built and tested the way Futures Truth evaluates vendor systems.
- [[turtletrader]] — complements the book's Donchian-breakout discussion with the original rules it's based on.
- [[george-pruitt-building-winning-trading-systems-with-tradestation]] — co-author George Pruitt's dedicated guide to coding and testing systems in EasyLanguage.
- [[elder-alexander-trading-for-a-living]] — a psychology- and money-management-forward counterpart to this book's more mechanical, backtest-driven approach.
- [[elliott-waves-principle]] — the source theory behind Chapter 2's trading-oriented Elliott wave condensation.
