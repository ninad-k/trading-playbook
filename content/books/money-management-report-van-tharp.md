---
title: Special Report on Money Management
author: Van K. Tharp
year: 1997
slug: money-management-report-van-tharp
tier: A
category: Money Management & Position Sizing
tags: [position-sizing, money-management, kelly-criterion, optimal-f, portfolio-heat, drawdown, expectancy]
difficulty: intermediate
doc_type: course
pages: 70
one_liner: "A two-part course update defining nine position-sizing models — from units-per-fixed-dollars through percent-risk and portfolio heat — each illustrated on the same 55/21-day breakout system."
related: [van-tharp-trading-systems, position-sizing, balsara-nauzer-j-money-management-strategies-for-futures-traders, jack-schwager-stock-market-wizards, curtis-faith-way-of-the-turtle]
source_file: "Money Management Report - Van Tharp.pdf"
---

## Overview

This is a two-part IITM course update (Parts I and II bound together) in which Van Tharp isolates "money management" — narrowly and deliberately defined as the part of a trading system that answers "how many units" or "how much" to trade — from entries, exits, and stop placement. He argues this is the single most misunderstood and most decisive component of trading performance, citing a Brinson/Singer/Beebower pension-fund study attributing 91.5% of returns to asset allocation rather than security selection or timing. The report catalogs nine position-sizing models, three ways of calculating account equity to feed them, and then a set of more aggressive "maximum profit" techniques (leveraging a high reward-to-risk system, optimal f, the Kelly Criterion, and "playing the market's money"). Every model is illustrated with worked numerical examples and, for several, with backtest tables from the same 55-day-entry/21-day-exit channel breakout system traded across ten commodities from 1981-91.

## Core thesis

Position sizing, not entry signal quality, is what separates traders who survive and compound capital from traders who blow up — even with a positive-expectancy system. Tharp's opening illustration (Ralph Vince's forty-PhD computer game, a 60%-win-rate game better than any casino odds, in which 38 of 40 players still lost money) is meant to show that oversized bets destroy even a mathematically favorable game. His practical framework is anti-martingale: position size should increase as equity grows and decrease (or stop) after losses, never the reverse. He is equally insistent that money management must be treated as a separate module from stop-loss placement — a "money management stop" that exits at a fixed dollar loss is not money management at all, because it doesn't answer "how many units."

## Key concepts

- **Money management (Tharp's definition)** — strictly, the algorithm that determines "how many" units or "how much" capital to commit to a position; excludes entries, exits, and stop placement.
- **Core equity, total equity, reduced total equity** — three ways to compute the account balance a sizing model is applied to: core equity subtracts each open position's allocated risk from starting equity; total equity is cash plus full mark-to-market value of open positions; reduced total equity is core equity plus any locked-in profit from a raised stop. Total equity is the most aggressive of the three, core equity the most conservative.
- **Anti-martingale vs. martingale** — anti-martingale systems (bet size rises after wins) are the only kind Tharp endorses; martingale systems (bet size rises after losses, e.g., doubling after each loss) are mathematically doomed by long losing streaks and broker/exchange bet limits.
- **Reward-to-risk ratio (money-manager sense)** — compounded annual return divided by peak-to-trough drawdown; Tharp's example shows two trading records with identical entry/exit logic but ratios of 0.114 versus 8.5, purely from different position sizing.
- **Portfolio heat** — the total risk exposure of an entire portfolio at once (a term Tharp credits to Ed Seykota and Dave Druz); most experienced traders cap it around 20-25%.
- **Optimal f** — Ralph Vince's fixed-fraction sizing method that maximizes long-run geometric growth, calculated as a divisor of the system's single largest historical loss; Tharp criticizes it for assuming the worst loss has already occurred and for requiring complex iterative computation.
- **Kelly Criterion** — Tharp's preferred alternative to optimal f for estimating a maximum sustainable bet fraction, using only win rate and the win/loss size ratio.
- **Expectancy** — (probability of winning × average win) − (probability of losing × average loss); the foundation Tharp says must be maximized before position sizing is layered on top.
- **Playing the market's money** — sizing rule that risks a small, fixed percentage of starting capital but a much larger, near-optimal percentage of accumulated open profits, so risk-taking capacity grows automatically with unrealized gains while principal stays protected.
- **Drawdown recovery asymmetry** — the nonlinear fact that a 20% loss needs a 25% gain to recover, a 50% loss needs 100%, and losses beyond 50% require improbably large gains, which is Tharp's core argument for controlling position size in the first place.

## Rules and setups

The nine numbered position-sizing models — units per fixed amount of money, equal units/equal leverage, percent of margin, percent volatility, percent risk, periodic adjustments, group control, portfolio heat, and long-vs-short netting — are documented with full worked formulas on the companion page [[money-management-report-van-tharp--position-sizing-models]]. This is a money management report, not an entry/exit system: Tharp explicitly declines to specify entries or stops, instead applying every sizing model to the same externally sourced 55-day-breakout/21-day-trailing-stop system purely as a consistent test bed, so there are no proprietary entry rules to report here beyond that reference system's brief description.

## Risk and money management

This is the entire subject of the report, so risk concepts and money management models are one and the same; see Key Concepts and the companion system page for the specific formulas. Tharp's general guidance on how much to risk per position: institutional/other-people's-money managers should stay under 1% per position; individual traders risking their own capital can reasonably go up to 3% before crossing into "gunslinger" territory; and systems using very tight stops (smaller than the average daily range) need correspondingly smaller risk percentages or should switch to a volatility-based model instead of a risk-based one. He recommends deriving a portfolio heat ceiling from roughly 80% of the system's Kelly-derived optimal percentage, and then dividing that ceiling by the maximum expected number of simultaneous open positions to back into a reasonable per-position risk limit.

## Psychology and discipline

Tharp treats undersized and oversized betting as mirror-image psychological failures rather than purely technical errors: the Vince PhD-game losers succumbed to the gambler's fallacy (assuming a losing streak makes a win "due") and escalated bet size for emotional reasons, not mathematical ones. He also frames the client-relations dimension of money management psychologically — a money manager who has an genuinely excellent year of trading can still be perceived by clients as having "lost" a large percentage if equity merely pulled back from an interim peak, illustrating that psychological framing of drawdown, not just its objective size, drives investor (and trader) behavior. He closes Part II with an explicit warning that the more aggressive "maximum profit" techniques (leveraging, optimal f, playing the market's money) are dangerous without strong personal discipline and adequate capitalization, and can accelerate ruin as easily as they accelerate gains if a trader abandons the plan mid-drawdown.

## Chapter map

- Part I, Forward & "Managing Other People's Money" — drawdown mechanics, the reward-to-risk ratio, and the Vince PhD-game illustration.
- Part I, "Money Management Defined" — Tharp's narrow definition, martingale vs. anti-martingale, and Market Wizards quotes on risk sizing.
- Part I, "Money Management Models," Models 1-4 — units per fixed amount of money, equal units/equal leverage, percent of margin, percent volatility, each with backtest tables on the 55/21 breakout system.
- Part II, Models 5-9 — percent risk, periodic (daily/hourly) adjustments, group control, portfolio heat, and long-vs-short netting.
- Part II, "Designing a High Reward-Risk System" — a six-step checklist for combining expectancy, sizing model choice, and multiple non-correlated systems.
- Part II, "How to Produce Maximum Profits," Techniques 1-4 — leveraging a proven high-ratio system, optimal f and the Kelly Criterion, "playing the market's money," and creative pyramid money management.

## Strengths and caveats

The report's clarity and worked numerical examples (each model applied to identical data) make the trade-offs between models unusually easy to compare, and the drawdown-recovery table is a genuinely useful, portable reference. Caveats: nearly all the backtest illustrations use one reference system (a 1981-91, ten-commodity, 55/21-day channel breakout) tested with a $1,000,000 starting account, so the specific percentage breakpoints (e.g., "the system breaks down below one contract per $20,000") do not transfer directly to other systems, timeframes, or account sizes — Tharp says as much repeatedly. Some tables in the source scan are visually garbled (OCR/formatting artifacts), though the surrounding worked examples make the underlying numbers recoverable. The report predates modern electronic execution and covers only futures/stock examples of the era (contract sizes, margins circa mid-1990s), so dollar figures need rescaling.

## Who should read it

Traders and system developers who already have a positive-expectancy entry method and need a rigorous framework for deciding position size — especially anyone currently sizing positions with an ad hoc "one contract per X dollars" rule and wanting to see, numerically, why that approach caps a small account's growth.

## Related books in this library

- [[van-tharp-trading-systems]] — Tharp's broader framework for what a "trading system" and full trading business plan consist of, of which this report's position-sizing models are one component.
- [[position-sizing]] — a focused treatment of position-sizing effects on trader performance that pairs directly with this report's model catalog.
- [[balsara-nauzer-j-money-management-strategies-for-futures-traders]] — an academic, futures-specific treatment of the same percent-risk and optimal-f territory.
- [[jack-schwager-stock-market-wizards]] — source of several of the risk-management quotes (Kovner, Hite, Dennis) Tharp cites directly in this report.
- [[curtis-faith-way-of-the-turtle]] — a real-world application of percent-risk (N-based) position sizing, useful as a worked example of Model 5 in practice.
