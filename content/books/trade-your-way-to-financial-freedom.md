---
author: Van K. Tharp
category: Money Management & Position Sizing
diagram: position-sizing
diagram_caption: R-multiples and position sizing, the book's central argument.
difficulty: intermediate
doc_type: book
one_liner: Defines trading expectancy and R-multiples, then shows through backtested
  examples that position sizing (not entry signals) drives most of a system's real-world
  return.
pages: 181
related:
- van-tharp-trading-systems
- money-management-report-van-tharp
- curtis-faith-way-of-the-turtle
- george-pruitt-building-winning-trading-systems-with-tradestation
reviewed_pdf_pages: 1-4, 9, 14, 18, 22, 28, 34, 81, 112, 121, 275-290 (the expectancy
  arithmetic, position-sizing models and the system-development chapters)
slug: trade-your-way-to-financial-freedom
source_file: Trade_Your_Way_to_Financial_Freedom.pdf
source_review: partial
tags:
- expectancy
- r-multiples
- position-sizing
- system-development
- trading-psychology
- money-management
tier: A
title: Trade Your Way to Financial Freedom
year: 1998
---

## Overview

Tharp, a trading psychologist and coach, builds this book around a single argument: most traders obsess over entry signals ("being right") while the two factors that actually determine long-run results — a system's expectancy and how positions are sized against account equity — get almost no attention in the trading literature. The book has three parts: Part One diagnoses the psychological biases that distort system development and trading; Part Two walks through building a system conceptually, surveys entry "concepts" (trend following, fundamentals, seasonal tendencies, spreading, arbitrage, neural networks), and develops the expectancy/R-multiple framework; Part Three drills into the mechanical building blocks of any system — setups, entry timing, stops, profit-taking, opportunity/cost factors, and a full chapter on position sizing with four concrete models, demonstrated on the same 20-year futures backtest so the reader can see position sizing alone change a $32,567 result into $2.1 million.

## Core thesis

A trading system's outcome is the product of two largely independent things: expectancy (how much you make per dollar risked, driven by win rate, average win/loss size, and cost of trading) and position sizing (how many units you trade given current equity). Most traders and even most trading books conflate "money management" with stop placement or diversification, but Tharp insists position sizing answers one specific question — "how much?" — throughout a trade, and this variable alone explains most of the variation in real-world results between traders using identical entry signals. A system with positive expectancy can still go broke from bad position sizing, and — his more provocative claim — the specific entry technique matters far less than most traders believe, since even a near-random entry can be profitable wrapped in a sound exit and position-sizing framework.

## Key concepts

- **Expectancy** — average amount you can expect to win (or lose) per dollar risked, over many trades: `Expectancy = (probability of winning × average win) − (probability of losing × average loss)`, computed per unit risked, not per trade.
- **R-multiple** — a trade's profit or loss expressed as a multiple of its initial risk (R = dollar distance from entry to initial stop); a $1,500 gain on a $500 risk is a 3R trade, letting systems and markets be compared on a common scale.
- **Reliability (hit rate)** — percentage of winning trades; Tharp repeatedly shows this is the variable traders fixate on, though far less important than the size of wins relative to losses.
- **Opportunity factor** — how often a system gets to trade; a lower-expectancy system trading far more often can out-earn a higher-expectancy system that trades rarely.
- **Position sizing** — the part of a system that determines "how much" at any point in a trade, as a function of current equity; distinct from stop placement, diversification, or risk avoidance.
- **Anti-martingale vs. martingale** — anti-martingale increases bet size as equity grows (the only category Tharp endorses); martingale increases bet size after losses (doubling down), which he shows mathematically leads to ruin.
- **The Snow Fight metaphor** — equity is a wall of snow; winning trades are white snowballs that build it, losing trades are black snowballs that erode it, and position sizing determines how many snowballs hit the wall at once.
- **Judgmental biases** — a catalogued set of psychological distortions (gambler's fallacy, need to be right, recency bias) that corrupt system development and live trading.
- **The Holy Grail** — Tharp's framing device: there is no perfect system out there; the real Holy Grail is the trader's own psychology and discipline in applying expectancy and position sizing consistently.
- **Setups vs. filters vs. entry signals** — a layered structure: a market filter determines whether conditions suit the system, a setup narrows to specific pre-conditions, and the entry signal is the precise trigger.

## Rules and setups

Tharp's 12-step system-development framework (Chapter 4) is the book's master checklist, not a fixed rule set: (1) take a self-inventory of your objectives and constraints; (2) gather market information with an open mind; (3) determine your objectives explicitly; (4) fix your trading time frame; (5) study the best historical moves in that time frame for common traits; (6) define the concept behind those moves in objective, measurable terms; (7) add stops and transaction costs; (8) add profit-taking exits and calculate expectancy; (9) look specifically for huge-R-multiple trades (10R or larger); (10) optimize via position sizing, not entry tweaking; (11) identify how the system can be improved; (12) do worst-case-scenario mental rehearsal before trading live. Two numeric examples recur through the expectancy chapter: a marble-drawing game with a 60% win rate but only a 20-cent expectancy per dollar risked, versus a second game with a 36% win rate but a 78-cent expectancy — proof that win rate alone is a poor guide to system quality. The book gives no single "buy here, sell here" entry rule of its own; entry concepts (trend following, fundamentals, seasonality, spreading, arbitrage, neural networks) are surveyed in Chapter 5 as raw material for a trader's own concept, not prescribed as the book's system.

## Risk and money management

Position sizing gets its own dedicated treatment, covered in the [[trade-your-way-to-financial-freedom--position-sizing-models]] sub-page: four models (one-unit-per-fixed-amount, equal value units, percent risk, percent volatility), each demonstrated on an identical channel breakout system across the same backtest so the reader can isolate the position-sizing effect from the entry/exit logic. Tharp gives explicit risk-tolerance guidance: traders managing other people's money should risk under 1% of equity per position; trading your own capital, up to about 3% is comfortable, and beyond 3% is "gunslinger" territory requiring conscious acceptance of the added risk. He also tabulates recovery math to make small-account fragility concrete: a 20% drawdown needs a 25% gain to recover, a 40% drawdown needs 66.7%, and a 50% drawdown needs a full 100% gain — the basis for his warning that accounts under roughly $50,000 face structurally worse odds regardless of system quality.

## Psychology and discipline

Part One (Chapters 1-3) is a full unit on the psychological side of system development: judgmental biases that distort backtesting and live trading, the gambler's fallacy (believing a losing streak makes a win "due"), and the observation that Ralph Vince's famous study had 95% of a room of PhDs lose money playing a positive-expectancy game purely through poor bet sizing driven by psychology. Tharp frames "being right" as a trap — a system can be right 90% of the time and still have negative expectancy if the rare losses are large enough (worked example: 90% win rate, $275 average win, 10% loss rate, $2,700 average loss, yields a negative $22.50 expectancy). Setting explicit objectives before building a system (Chapter 3, including an interview with trader Tom Basso) is treated as inseparable from psychology — a system built without clear personal objectives cannot be followed with discipline because it was never really the trader's own.

## Chapter map

- Ch 1 — The Legend of the Holy Grail — reframes the "perfect system" myth around psychology.
- Ch 2 — Judgmental Biases — biases affecting system development, testing, and live trading.
- Ch 3 — Setting Your Objectives — with an interview with trader Tom Basso.
- Ch 4 — Steps to Developing a System — the 12-step framework.
- Ch 5 — Selecting a Concept That Works — trend following, fundamentals, seasonality, spreading, arbitrage, neural networks.
- Ch 6 — Understanding Expectancy — the Snow Fight metaphor, expectancy formula, R-multiples.
- Ch 7 — Using Setups — the four phases of entry, filters vs. setups.
- Ch 8 — Entry or Market Timing — beating random entry, common entry techniques.
- Ch 9 — Know When to Fold 'Em — what a stop does, using a stop that makes sense.
- Ch 10 — How to Take Profits — profit-taking exit design, simplicity vs. multiple exits.
- Ch 11 — The Opportunity and Cost Factors — trading frequency and cost in system evaluation.
- Ch 12 — What Do You Mean Position Sizing? — the four position-sizing models (see system sub-page).

## Strengths and caveats

The expectancy/R-multiple framework and the four-model position-sizing demonstration (same signals, wildly different results purely from sizing) are the book's lasting contributions and are widely cited in later trading literature. The backtests are dated — a 1981-1991 futures test and a 1992-1997 Dow-30 stock test, using era-specific software (Athena) and cost assumptions — and no walk-forward or out-of-sample validation is shown. The book is conceptual and framework-heavy rather than a source of concrete entry/exit rules; readers wanting a tradable system must supply their own from Chapter 5's survey of concepts. Some psychological material (biases, objective-setting) can feel repetitive alongside Tharp's later books and seminars.

## Who should read it

Traders and system developers who already have (or are developing) an entry method and want to understand why results diverge from backtested expectations — the gap is often position sizing, not the entry signal. Also valuable for anyone who has never separated "how good is my edge" (expectancy) from "how much should I bet" (position sizing).

## Related books in this library

- [[van-tharp-trading-systems]] — a shorter Tharp article covering the same trading-system-as-business-plan territory at a higher level; this book fully develops the expectancy and position-sizing concepts it references.
- [[money-management-report-van-tharp]] — Tharp's dedicated money-management report, a natural next read after this book's position-sizing chapter.
- [[curtis-faith-way-of-the-turtle]] — a fully disclosed trend-following system whose percent-risk-based sizing can be evaluated directly against Tharp's four models.
- [[george-pruitt-building-winning-trading-systems-with-tradestation]] — supplies complete entry/exit systems of the kind Tharp's Chapter 5 surveys only conceptually.
