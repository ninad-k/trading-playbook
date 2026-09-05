---
title: The Encyclopedia of Trading Strategies
author: "Jeffrey Owen Katz and Donna L. McCormick"
year: 1999
slug: mcgraw-hill-encyclopedia-of-trading-strategies
tier: A
category: "Quant, Microstructure & Academic Research"
tags: [system-testing, statistical-significance, moving-averages, breakouts, neural-networks, genetic-algorithms, exit-strategies, curve-fitting]
difficulty: advanced
doc_type: book
pages: 386
one_liner: "Statistically tests entry families (breakouts, moving averages, oscillators, seasonality, cycles, neural nets, genetic rules) and exit families on a 30+ market portfolio, ranking which actually beat chance."
related: [jack-schwager-guide-to-winning-with-automated-trading-systems-course-manual, george-pruitt-building-winning-trading-systems-with-tradestation, perry-kaufman-smarter-trading, richard-l-weissman-mechanical-trading-systems, new-concepts-in-technical-trading-systems-welles-wilder]
source_file: "Mcgraw.Hill.Encyclopedia Of Trading Strategies.pdf"
---

## Overview

Jeffrey Owen Katz and Donna L. McCormick, both with backgrounds in academic research and Technical Analysis of Stocks & Commodities contributions, treat trading-system development as an experimental science rather than a chart-reading art. Part I ("Tools of the Trade") covers simulators, optimizers, and the statistics needed to judge whether a backtest result is real; Part II ("The Study of Entries") systematically tests eight families of entry method — breakouts, moving averages, oscillators, seasonality, lunar/solar cycles, cycle-filter banks, neural networks, and genetic algorithms — each held to a fixed, standardized exit so entry methods can be compared apples-to-apples; Part III ("The Study of Exits") holds entries fixed (random entry) and tests exit refinements — dynamic stops, profit targets, extended time limits, neural and genetic signal exits. Every test runs on a diversified 30+ market futures portfolio with in-sample optimization (1985-1994) followed by out-of-sample verification (1995-1999), transaction costs included, and formal t-test significance reported. The book's full methodology is detailed in the system sub-page [[mcgraw-hill-encyclopedia-of-trading-strategies--test-methodology]].

## Core thesis

Most popular technical methods do not survive rigorous, cost-inclusive, out-of-sample testing on a diversified portfolio — and the ones that do survive are often not the ones with the best reputations. Moving-average crossovers, oscillator overbought/oversold signals, and cycle-based entries performed at or below random-entry chance out-of-sample; breakout models that once worked decayed toward chance as they became popular; while neural networks and genetically evolved rule-based entries — methods with a "terrible reputation" for curve-fitting — were the only families that held up with a statistically significant edge out-of-sample when trained on a large, pooled, whole-portfolio sample rather than a single market. The authors' explanation is sample size versus free parameters: curve-fitting is a function of how many parameters a model has relative to how much (representative) data trained it, not a property of the modeling technique itself, so training a large neural network or genetic system across an entire 30+ market portfolio (rather than one market) can outrun its own capacity to merely memorize noise.

## Key concepts

- **Standardized exit** — a fixed stop/profit-target/time-limit exit (in average-true-range units) applied identically to every entry method under test, so performance differences reflect the entry, not exit variation.
- **Dollar volatility equalization** — position sizes (contracts per market) are scaled so every market contributes roughly equal risk/reward to the portfolio; computed from a 200-day average of daily price change times point value.
- **Standard portfolio** — a fixed, diversified set of ~30 futures markets (indices, rates, currencies, energies, metals, livestock, grains, softs) used for every entry-family test, so results are comparable across chapters.
- **In-sample / out-of-sample split** — parameters are optimized only on 8/1/1985-12/31/1994 data; 1/1/1995-2/1/1999 data is reserved purely for verification and never touched during optimization.
- **Curve-fitting / shrinkage** — the tendency of a model with many free parameters (a large neural net) to fit noise in the training sample; quantified with a shrinkage-corrected multiple-correlation formula and cross-checked against out-of-sample decay.
- **Annualized risk-to-reward ratio (ARRR)** — the book's primary performance statistic, essentially a rescaled t-statistic on daily returns, chosen because it is directly tied to a formal significance test.
- **Walk-forward / genetic optimization** — alternatives to brute-force grid search covered in the optimizer chapter; genetic algorithms (OptEvolve) are also used directly as an entry- and exit-rule-generation technique, not just a parameter search.
- **Money management stop / profit target / time-based exit** — the three components of the standardized exit strategy (MSES/SES), implemented respectively as a stop order, a limit order, and a forced market exit after a maximum holding period.
- **Points of light** — the authors' term for specific model/order/market combinations that were profitable and statistically significant in both in-sample and out-of-sample periods, used to assemble a demonstration multi-system portfolio.

## Rules and setups

This is a testing encyclopedia rather than a single strategy, so "rules" are the tested parameter ranges and headline out-of-sample findings for each entry family, all run against the standard portfolio and standardized exit (details in the system sub-page):

1. **Breakouts (Ch. 5)** — close-only and highest-high/lowest-low channel breakouts, look-backs 5-100 in steps of 5, entry at open/limit/stop. Best in-sample look-back was consistently 80 days. Profitable before transaction costs (76% annualized in one test); flipped to a loss once 3-tick slippage and $15/round-turn commission were included. As a family, better than chance out-of-sample (losses under $1,000/trade versus ~$2,000/trade expected at random) but not profitable, except a currencies-only volatility breakout variant (+8.5% annualized, $2,106/trade out-of-sample).
2. **Moving averages (Ch. 6)** — single/dual crossover and slope models, four moving-average types, lengths stepped 1-50. Trend-following variants lost ~$1,500/trade on average (close to the ~$2,100/trade random-entry baseline); counter-trend support/resistance variants were more variable, with a simple-MA support/resistance + stop-order combination profitable in both samples ($227/trade in-sample, $482/trade, 14.8% annualized out-of-sample).
3. **Oscillators (Ch. 7)** — overbought/oversold, signal-line, and divergence models. Worst family tested overall; RSI overbought/oversold was the single worst model, statistically significantly worse than random. The MACD divergence model was the exception, profitable in both samples (6.7%/$1,250 per trade in-sample, 6.1%/$985 per trade out-of-sample with a limit entry).
4. **Seasonality (Ch. 8)** — momentum and crossover models built on same-calendar-date price behavior, with optional Slow %K confirmation/inversion filters. Clearly better than chance; a seasonal crossover-with-confirmation model (entry on stop) was profitable both samples (7.4%/$846 per trade in-sample, 9.5%/$1,677 per trade out-of-sample).
5. **Lunar/solar (Ch. 9), Cycles (Ch. 10)** — lunar momentum/crossover models tied to the lunar month; MESA/filter-bank cycle detection with adaptive periodicity (3-30 bar range) and phase-based entries. Both families performed close to or worse than chance; cycles were the single worst-performing family out-of-sample.
6. **Neural networks (Ch. 11)** — 3- and 4-layer feed-forward nets (e.g., 18-10-1, 18-20-6-1) predicting reversals (Reverse Slow %K) or turning points, trained across the whole portfolio (~88,000 facts). Small networks held up best out-of-sample (average loss $860/trade, versus ~$2,000+/trade random); larger networks showed heavy in-sample curve-fitting (up to 768% annualized in-sample) with mixed but sometimes still-profitable out-of-sample decay.
7. **Genetic algorithms (Ch. 12)** — rule-based entries evolved via OptEvolve over up to 2,500 generations, expressed as human-readable indicator-threshold rules (not a black box). Best out-of-sample performer of every entry family tested: $3,271/trade average profit across all genetic-model tests, with the long-side model returning 64.2% in-sample / 41.0% out-of-sample annualized at one order type.
8. **Exits (Part III, Ch. 13-15)** — fixed stop/target optimum found near 1.5 ATR stop / 4.5 ATR target (maxhold 10 days); dynamic (trailing) ATR-based stops tested against fixed stops; a genetically evolved rule-based signal exit added to the standard exit cut average losing-trade size roughly in half in-sample and reduced it meaningfully out-of-sample, while a neural-network signal exit improved in-sample results but did not hold up out-of-sample.

## Risk and money management

Risk is handled almost entirely through the standardized exit and dollar-volatility equalization rather than a single money-management chapter. Every tested system risks a stop-defined amount per trade (money-management stop expressed in average-true-range units, not a fixed dollar figure, so risk stays comparable across eras and markets), and position size (contracts traded) is scaled per market so each contributes equal dollar volatility to the portfolio rather than an equal number of contracts — this is essential to their finding that a diversified, cost-inclusive, portfolio-level test tells a very different story than single-market anecdotes. The book explicitly avoids compounding/reinvestment in its main tests (constant risk exposure throughout, not constant contract count) specifically so that t-tests on trade profitability remain statistically valid even through periods of negative equity; it notes reinvestment schemes (optimal f, etc.) can be layered on afterward but complicate interpretation of significance tests.

## Psychology and discipline

The book has almost no discretionary-psychology content — its entire argument is that mechanical, fully specified systems remove emotion (fear, greed, second-guessing) from entries, exits, and stop placement, and that testing itself must be conducted with scientific discipline: pre-registered test parameters, in-sample/out-of-sample separation never violated, and skepticism toward any result that has not survived a fresh sample. The authors' own origin story (Katz's early discretionary S&P/OEX signal service, undermined by his own second-guessing and undisciplined exits) is used to motivate the book's central discipline: if a rule can't be coded and back-tested, it shouldn't be traded.

## Chapter map

- Ch 1-4 (Part I) — Data, Simulators, Optimizers, Statistics: infrastructure and the statistical toolkit (t-tests, shrinkage correction, sample-size/curve-fitting tradeoffs) used throughout the rest of the book.
- Ch 5 — Breakout Models — channel and volatility breakouts, order-type and filter variations.
- Ch 6 — Moving-Average Models — trend-following and counter-trend crossover/slope/support-resistance variants.
- Ch 7 — Oscillator-Based Entries — overbought/oversold, signal-line, divergence models.
- Ch 8 — Seasonality — calendar-date momentum and crossover models with confirmation/inversion filters.
- Ch 9 — Lunar and Solar Rhythms — lunar-cycle and sunspot-activity entry models.
- Ch 10 — Cycle-Based Entries — MESA and filter-bank cycle detection and phase-timed entries.
- Ch 11 — Neural Networks — feed-forward nets for reversal and turning-point prediction.
- Ch 12 — Genetic Algorithms — evolved, human-readable rule-based entry models.
- Ch 13-15 (Part III) — The Standard Exit Strategy, Improvements on the Standard Exit, Adding AI to Exits: fixed/dynamic stops, profit targets, time limits, and neural/genetic signal exits, tested against random entries.
- Conclusion — portfolio-wide ranking of every entry family, plus an assembled multi-system "points of light" portfolio combining the best model/market pairings found.

## Strengths and caveats

The methodology is the book's real value: a fixed standard portfolio, dollar-volatility equalization, an unchanging standardized exit while entries are compared, formal in-sample/out-of-sample separation, transaction costs included by default, and t-test significance reported for every headline number — a rigor rarely seen in retail-facing trading books. The main dating issue is the data window itself (1985-1999, primarily pre-2000 futures markets with 1990s bid-ask/tick-size conventions), so absolute dollar figures and even relative rankings (e.g., breakout decay, oscillator weakness) reflect that era's liquidity and participant mix and may not transfer unchanged to today's markets. The neural-network and genetic-algorithm code is written in period C/TradeStation idioms requiring the authors' own C-Trader Toolkit to reproduce exactly. Some conclusions (e.g., cycles performing worse than chance) contradict the optimistic claims made for the same techniques in other technical-analysis literature — a useful check on hype, though it also means a reader who has invested in a specific indicator family (cycles, oscillators) will find this book unsparing.

## Who should read it

System developers and quantitative traders who want a template for testing their own entry/exit ideas rigorously — the standard-portfolio, standardized-exit, in/out-of-sample methodology is directly reusable regardless of which specific systems one trades. Less useful for discretionary traders looking for chart-pattern guidance, and requires comfort with basic inferential statistics (t-tests, significance, shrinkage) to get full value from the results tables.

## Related books in this library

- [[jack-schwager-guide-to-winning-with-automated-trading-systems-course-manual]] — a parallel treatment of building and testing mechanical systems, useful alongside this book's statistical rigor.
- [[george-pruitt-building-winning-trading-systems-with-tradestation]] — implements many similar entry/exit ideas directly in TradeStation code, complementing this book's C-based examples.
- [[perry-kaufman-smarter-trading]] — covers adaptive moving averages and other techniques this book tests statistically, from a design rather than testing perspective.
- [[richard-l-weissman-mechanical-trading-systems]] — shares the philosophy that psychology-driven pitfalls are best solved with fully mechanical, tested systems.
- [[new-concepts-in-technical-trading-systems-welles-wilder]] — source of the directional movement index the Encyclopedia references as a candidate trend/no-trend filter for breakout systems.
