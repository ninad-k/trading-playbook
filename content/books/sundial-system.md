---
title: "The Knife (Sundial System)"
author: "Charles \"Diallist\" (James16 trading forum)"
year: unknown
slug: sundial-system
tier: B
category: Forex Mechanics & Macro Drivers
tags: [forex, momentum, moving-averages, fibonacci, position-sizing, trend-following, mechanical-system]
difficulty: intermediate
doc_type: manual
pages: 43
one_liner: "Forex momentum system (nicknamed 'the Knife') combining weekly moving-average momentum for trend and 4-hour moving-average slope changes for entries, with Fibonacci profit targets."
related: [forex-money-management, bill-poulos-the-truth-about-fibonacci-trading, van-tharp-the-flow-of-the-markets]
source_file: "Sundial System.pdf"
---

## Summary

A forum tutorial teaching a discretionary-mechanical forex trading system nicknamed "the Knife," derived from a model built by an informal group called the Vegas Team. It combines a weekly chart (to determine trend and momentum strength via two moving averages) with a 4-hour chart (to trigger entries via a moving-average slope change) and uses Fibonacci-number pip targets scaled to each currency pair's volatility. The author states the system is about 90% mechanical and 10% discretionary, and repeatedly stresses demo-trading for at least three months before going live.

## Key points

- Weekly chart setup: 21-period EMA and 5-period SMA, both on median price (H+L)/2; the distance between them measures momentum strength, not crossover timing.
- Trend rule: increasing distance between the two weekly moving averages bar-to-bar confirms the current trend; a decrease in that distance signals a trend change (occasionally an increase signals a change instead — treated as an exception case).
- 4-hour chart setup: 55-period SMA on median price and 8-period SMA on close; a change in the 8 SMA's slope (not a moving-average crossover) triggers entries, and only in the direction of the weekly trend.
- Two signal types: Primary (full position size) when the slope change occurs further from the 55 SMA, and Secondary (half position size) when closer — Secondary signals are considered less reliable.
- Three "risk models" set profit targets as Fibonacci pip distances from the 4-hour 55 SMA, chosen by currency volatility: Low volatility 89 & 144 pips, Medium 144 & 233 pips, High 233 & 377 pips.
- Position exits are staged in thirds: one-third of the position closed at the first Fibonacci target, one-third at the second target, and the final third left to run until the 8 SMA's slope reverses.
- A filter is applied on the weekly chart when momentum exceeds 500 pips: a valid trend-change signal then requires either a 10+ pip decrease in momentum or two consecutive bars of any decrease, to avoid false reversals in strongly trending markets.
- The author cites a Vegas Team manual backtest (Jan 2004–Jun 2005, six USD pairs) using deliberately conservative assumptions (ignoring trades under 100 pips, measuring exits off the lagging 8 SMA rather than price, and doubling recorded losses) as evidence of profitability, without giving a verifiable win rate or return figure.

## Actionable rules

1. Position size must be a multiple of 3 lots so it can be split evenly across the two Fibonacci take-profit exits and the trailing final third.
2. Risk 1× your normal per-trade risk percentage (e.g. 2–3% of equity) on a Primary signal, and half that (e.g. 1–1.5%) on a Secondary signal.
3. Stops are set from recent technical levels (most often the last swing high/low), or alternatively from a "neutral line" method the text references but does not fully define in the excerpted material.
4. Choose the risk model (89/144, 144/233, or 233/377 pips) to match the traded pair's typical volatility (example given: risk model 2 for GBP/USD, risk model 1 for USD/JPY), and generally pick the largest model whose second target still gets hit in strong trends.
5. Only take 4-hour entries in the direction confirmed by the weekly momentum trend; do not trade the moving-average crossover itself as a signal.
6. Demo-trade the system for a minimum of three months before committing real capital.

## Caveats

This is an informal forum-style write-up (undated, author identified only by forum handle "Diallist"/"Charles"), not a peer-reviewed or published book — the described backtest is a single, non-independently-verified claim from an anonymous "Vegas Team" and includes no drawdown, Sharpe, or out-of-sample data. Several referenced elements (the "neutral line" stop method, the full weekly filter exceptions, and the 4-hour entry filter) are described as covered "in the system description thread" but are not fully detailed in the material read here, so a reader would need the original forum thread to code the system completely. Treat the profit claims (up to 20,000–25,000 pips/year cited by one team member) as unverified marketing, not evidence.

## Who it is for

Forex traders comfortable with multi-timeframe technical analysis (moving averages, Fibonacci levels) who want a rules-based trend/momentum framework and are willing to demo-test extensively before risking capital; not for traders wanting a fully specified, backtest-verifiable system out of the box.
