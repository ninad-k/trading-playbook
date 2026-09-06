---
author: Jeffrey Owen Katz and Donna L. McCormick
category: Quant, Microstructure & Academic Research
difficulty: advanced
doc_type: book
one_liner: Statistically tests entry families (breakouts, moving averages, oscillators,
  seasonality, cycles, neural nets, genetic rules) and exit families on a 30+ market
  portfolio, ranking which actually beat chance.
pages: 386
related:
- jack-schwager-guide-to-winning-with-automated-trading-systems-course-manual
- george-pruitt-building-winning-trading-systems-with-tradestation
- perry-kaufman-smarter-trading
- richard-l-weissman-mechanical-trading-systems
reviewed_pdf_pages: 4-5, 7, 10, 23, 27, 31, 35, 60, 63-64, 69, 73, 77, 95, 133, 157
  (the test methodology chapters and the per-family results tables for breakouts,
  moving averages, oscillators, cycles and AI models)
slug: mcgraw-hill-encyclopedia-of-trading-strategies
source_file: Mcgraw.Hill.Encyclopedia Of Trading Strategies.pdf
source_review: partial
tags:
- system-testing
- statistical-significance
- moving-averages
- breakouts
- neural-networks
- genetic-algorithms
- exit-strategies
- curve-fitting
tier: A
title: The Encyclopedia of Trading Strategies
year: 1999
---

## Overview

Jeffrey Owen Katz and Donna L. McCormick, both academic researchers and longtime Technical Analysis of Stocks & Commodities contributors, treat trading-system development as an experimental science rather than a chart-reading art. Part I ("Tools of the Trade") covers simulators, optimizers, and the statistics needed to judge whether a backtest result is real. Part II ("The Study of Entries") systematically tests eight families of entry method — breakouts, moving averages, oscillators, seasonality, lunar/solar cycles, cycle-filter banks, neural networks, and genetic algorithms — each held to a fixed, standardized exit so entries can be compared apples-to-apples. Part III ("The Study of Exits") holds entries fixed (random entry) and tests exit refinements: dynamic stops, profit targets, extended time limits, neural and genetic signal exits. Every test runs on a diversified 30+ market futures portfolio with in-sample optimization (1985-1994), out-of-sample verification (1995-1999), transaction costs included, and formal t-test significance reported; full methodology is in the sub-page [[mcgraw-hill-encyclopedia-of-trading-strategies--test-methodology]].

## Core thesis

Most popular technical methods do not survive rigorous, cost-inclusive, out-of-sample testing on a diversified portfolio — and the ones that do survive are not the ones with the best reputations. Moving-average crossovers, oscillator overbought/oversold signals, and cycle-based entries performed at or below random-entry chance out-of-sample; breakout models that once worked decayed toward chance as they became popular; neural networks and genetically evolved rule-based entries — methods with a "terrible reputation" for curve-fitting — were the only families that held a statistically significant edge out-of-sample, when trained on a large, pooled, whole-portfolio sample rather than one market. The authors' explanation is sample size versus free parameters: curve-fitting is a function of how many parameters a model has relative to how much representative data trained it, not a property of the technique itself, so a large neural net or genetic system trained across an entire 30+ market portfolio can outrun its own capacity to merely memorize noise.

## Key concepts

- **Standardized exit** — a fixed stop/profit-target/time-limit exit (in average-true-range units) applied identically to every entry method under test, so results reflect the entry, not exit variation.
- **Dollar volatility equalization** — contracts per market are scaled so every market contributes roughly equal risk/reward, computed from a 200-day average of daily price change times point value.
- **Standard portfolio** — a fixed, diversified set of ~30 futures markets (indices, rates, currencies, energies, metals, livestock, grains, softs) used for every entry-family test.
- **In-sample / out-of-sample split** — parameters are optimized only on 8/1/1985-12/31/1994 data; 1/1/1995-2/1/1999 is reserved purely for verification.
- **Curve-fitting / shrinkage** — the tendency of a model with many free parameters to fit noise in the training sample; quantified with a shrinkage-corrected multiple-correlation formula and cross-checked against out-of-sample decay.
- **Annualized risk-to-reward ratio (ARRR)** — the primary performance statistic, essentially a rescaled t-statistic on daily returns, tied directly to a formal significance test.
- **Walk-forward / genetic optimization** — alternatives to brute-force grid search; genetic algorithms (OptEvolve) are also used directly as an entry- and exit-rule-generation technique.
- **Points of light** — model/order/market combinations profitable and statistically significant in both samples, used to assemble a demonstration multi-system portfolio.

## Rules and setups

This is a testing encyclopedia rather than a single strategy, so "rules" are the tested parameter ranges and headline out-of-sample findings for each entry family, all run against the standard portfolio and standardized exit (details in the system sub-page):

1. **Breakouts (Ch. 5)** — channel and highest-high/lowest-low breakouts, look-backs 5-100 by 5, entry at open/limit/stop. Best in-sample look-back was consistently 80 days; profitable before costs (76% annualized) but flipped to a loss once 3-tick slippage and $15/round-turn commission were added. Better than chance out-of-sample (losses under $1,000/trade vs. ~$2,000/trade at random) but not profitable, except a currencies-only volatility-breakout variant (+8.5% annualized, $2,106/trade out-of-sample).
2. **Moving averages (Ch. 6)** — crossover and slope models, four MA types, lengths 1-50. Trend-following variants lost ~$1,500/trade on average (near the ~$2,100/trade random baseline); a simple-MA support/resistance model with a stop order was profitable both samples ($227/trade in-sample, $482/trade / 14.8% annualized out-of-sample).
3. **Oscillators (Ch. 7)** — overbought/oversold, signal-line, divergence models. Worst family overall; RSI overbought/oversold was the single worst model, significantly worse than random. MACD divergence was the exception, profitable both samples (6.7%/$1,250 per trade in-sample, 6.1%/$985 out-of-sample).
4. **Seasonality (Ch. 8)** — calendar-date momentum/crossover models with optional Slow %K confirmation. Clearly better than chance; a crossover-with-confirmation model (entry on stop) was profitable both samples (7.4%/$846 in-sample, 9.5%/$1,677 out-of-sample).
5. **Lunar/solar (Ch. 9), Cycles (Ch. 10)** — lunar-month and MESA/filter-bank cycle models with phase-based entries. Both close to or worse than chance; cycles were the single worst-performing family out-of-sample.
6. **Neural networks (Ch. 11)** — 3-/4-layer feed-forward nets (e.g., 18-10-1, 18-20-6-1) trained across the whole portfolio (~88,000 facts). Small networks held up best out-of-sample (avg. loss $860/trade vs. ~$2,000+ random); larger networks showed heavy in-sample curve-fitting (up to 768% annualized) with mixed out-of-sample decay.
7. **Genetic algorithms (Ch. 12)** — rule-based entries evolved via OptEvolve over up to 2,500 generations, expressed as human-readable rules. Best out-of-sample performer of any family: $3,271/trade average profit, with the long-side model returning 64.2% in-sample / 41.0% out-of-sample annualized.
8. **Exits (Ch. 13-15)** — optimum near a 1.5 ATR stop / 4.5 ATR target (10-day max hold); a genetically evolved rule-based signal exit cut average losing-trade size roughly in half in-sample and held up out-of-sample, while a neural-network signal exit improved in-sample but did not hold up out-of-sample.

## Risk and money management

Risk is handled through the standardized exit and dollar-volatility equalization rather than a dedicated money-management chapter. Every system risks a stop-defined amount per trade (in ATR units, not a fixed dollar figure, so it stays comparable across eras and markets), and position size is scaled per market so each contributes equal dollar volatility rather than an equal contract count — essential to the finding that a diversified, cost-inclusive, portfolio-level test tells a different story than single-market anecdotes. The book avoids compounding in its main tests (constant risk exposure, not constant contract count) so t-tests on trade profitability stay valid through drawdowns; reinvestment schemes (optimal f, etc.) are noted as possible add-ons but are said to complicate significance testing.

## Psychology and discipline

The book has almost no discretionary-psychology content — its argument is that mechanical, fully specified systems remove emotion (fear, greed, second-guessing) from entries, exits, and stops, and that testing itself must be scientifically disciplined: parameters fixed before testing, the in/out-of-sample wall never violated, skepticism toward any result that hasn't survived a fresh sample. Katz's own origin story — an early discretionary S&P/OEX signal service undermined by his own second-guessing and undisciplined exits — motivates the book's central rule: if it can't be coded and back-tested, it shouldn't be traded.

## Chapter map

- Ch 1-4 (Part I) — Data, Simulators, Optimizers, Statistics — infrastructure and statistical toolkit (t-tests, shrinkage, curve-fitting tradeoffs).
- Ch 5 — Breakout Models — channel and volatility breakouts, order-type and filter variations.
- Ch 6 — Moving-Average Models — trend-following and counter-trend crossover/slope/support-resistance variants.
- Ch 7 — Oscillator-Based Entries — overbought/oversold, signal-line, divergence models.
- Ch 8 — Seasonality — calendar-date momentum and crossover models with confirmation/inversion filters.
- Ch 9 — Lunar and Solar Rhythms — lunar-cycle and sunspot-activity entry models.
- Ch 10 — Cycle-Based Entries — MESA and filter-bank cycle detection and phase-timed entries.
- Ch 11 — Neural Networks — feed-forward nets for reversal and turning-point prediction.
- Ch 12 — Genetic Algorithms — evolved, human-readable rule-based entry models.
- Ch 13-15 (Part III) — Standard Exit, Improvements on the Standard Exit, AI Exits — fixed/dynamic stops, targets, time limits, neural/genetic signal exits vs. random entries.
- Conclusion — portfolio-wide ranking of every entry family plus an assembled "points of light" multi-system portfolio.

## Strengths and caveats

The methodology is the book's real value: a fixed standard portfolio, dollar-volatility equalization, an unchanging exit while entries are compared, formal in/out-of-sample separation, costs included by default, and t-test significance for every headline number — rigor rarely seen in retail-facing trading books. The main dating issue is the data window itself (1985-1999 futures markets, 1990s bid-ask/tick-size conventions), so absolute figures and even relative rankings may not transfer unchanged to today's markets. The neural-network and genetic-algorithm code uses period C/TradeStation idioms requiring the authors' own C-Trader Toolkit to reproduce exactly. Some conclusions (cycles worse than chance) contradict optimistic claims made for the same techniques elsewhere — a useful check on hype, but a reader invested in cycles or oscillators will find this book unsparing.

## Who should read it

System developers and quantitative traders who want a template for testing their own entry/exit ideas rigorously — the standard-portfolio, standardized-exit, in/out-of-sample methodology is directly reusable regardless of which specific systems one trades. Less useful for discretionary traders looking for chart-pattern guidance, and requires comfort with basic inferential statistics (t-tests, significance, shrinkage) to get full value from the results tables.

## Related books in this library

- [[jack-schwager-guide-to-winning-with-automated-trading-systems-course-manual]] — a parallel treatment of building and testing mechanical systems, useful alongside this book's statistical rigor.
- [[george-pruitt-building-winning-trading-systems-with-tradestation]] — implements many similar entry/exit ideas directly in TradeStation code, complementing this book's C-based examples.
- [[perry-kaufman-smarter-trading]] — covers adaptive moving averages and other techniques this book tests statistically, from a design rather than testing perspective.
- [[richard-l-weissman-mechanical-trading-systems]] — shares the philosophy that psychology-driven pitfalls are best solved with fully mechanical, tested systems.
- **New Concepts in Technical Trading Systems** (no library summary: corrupt) — source of the directional movement index the Encyclopedia references as a candidate trend/no-trend filter for breakout systems.
