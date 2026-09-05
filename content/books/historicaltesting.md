---
title: "Historical Testing"
author: Scott Owens
year: 2005
slug: historicaltesting
tier: B
category: Trend Following & Mechanical Systems
tags: [backtesting, curve-fitting, drawdown, forex, system-optimization, risk-assessment]
difficulty: beginner
doc_type: article
pages: 6
one_liner: "FX Engines' Core Concepts brief on using historical (backtest) data to assess a system's risk before trading it live, and the five main ways backtests mislead."
related: [mechanical-trading-systems, richard-l-weissman-mechanical-trading-systems, george-pruitt-building-winning-trading-systems-with-tradestation]
source_file: "historicaltesting.pdf"
---

## Summary

A short "Core Concepts" brief from FX Engines' periodic Forex Report (January 2005, by Scott Owens), pitched at traders of all experience levels. It positions historical (back-)testing as a risk-assessment tool: since a new system has no live track record, a tick-by-tick re-enactment of its trades is the best available substitute. The piece walks through what a good backtest looks like, which metrics matter, and the specific ways backtests can mislead a trader who trusts them uncritically.

## Key points

- A trader's risk profile per trade is driven mainly by position size, volatility, drawdown potential, and recent events; without live experience, historical and live-simulated tests are the closest substitute.
- A good historical test uses multiple years of tick-level data under real trading constraints, replicable by the trader in a live account.
- The most useful backtest metrics are net pips, maximum drawdown, consecutive losses, and success rate — used first to quickly reject bad systems, then to justify deeper study of promising ones.
- Reviewing individual trades (not just summary statistics) surfaces optimization ideas: adjusting a stop, changing the exit signal, or changing the entry schedule.
- Five named pitfalls: curve fitting (over-optimizing to one date range), ignoring trend (testing against-trend systems without checking they hold up), spread differences (test spread narrower than live spread), poor data source (too few or non-gap-free tick data points), over-mechanizing a system that should stay partly discretionary, and platform incompatibility (test platform behaves differently than the live platform).
- After optimization, the recommended sequence is: test many system variants, optimize with awareness of the pitfalls above, then trade live only after live-testing confirms the historical results.

## Actionable rules

1. Build and test a system on multiple years of tick-level (not just daily) data before trading it live.
2. Judge a system first on net pips, max drawdown, consecutive losses, and success rate; only dig into individual trades for systems that pass this first screen.
3. Match the backtest's assumed spread to the spread actually available in live trading — a system tested at a 3-pip spread that trades live at a wider spread will underperform its backtest.
4. Confirm the backtest platform executes identically to the live platform before trusting the results.
5. Run a live (forward) test after optimization and before committing real capital, since live results will deviate from historical ones in some ways regardless of test quality.

## Caveats

Published by a vendor (FX Engines) to promote its own backtesting platform and "Back Test Multiplier" optimization tool; treat the specific product claims as marketing. No concrete numeric thresholds are given for "large" drawdown or "too few" data points — the pitfalls are named conceptually rather than quantified. The content is generic risk-assessment guidance, not a specific tradable system.

## Who it is for

Traders building or evaluating a mechanical system who want a short checklist of backtesting pitfalls before trusting a set of historical results.
