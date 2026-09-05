---
title: "Two Moving Average Crossover (Full System)"
author: "Richard L. Weissman"
year: 2005
slug: richard-l-weissman-mechanical-trading-systems--two-moving-average-crossover
tier: A
category: "Trend Following & Mechanical Systems"
tags: [moving-average, trend-following, stop-and-reverse, crossover, diversification]
difficulty: beginner
doc_type: system
parent: richard-l-weissman-mechanical-trading-systems
pages: 241
one_liner: "A 9-day/26-day moving average crossover, always in the market and always reversing, that Weissman calls the simplest and most robust trend-following system in the book."
related: [curtis-faith-way-of-the-turtle, michael-covel-trend-following]
source_file: "RICHARD L. WEISSMAN - Mechanical Trading Systems.pdf"
---

## What it is

The book's baseline long/intermediate-term trend-following system, offered as the simplest workable alternative to a single 200-day moving average. A short-term (9-day) simple moving average is compared to a longer-term (26-day) simple moving average; whichever side the short average is on determines the position. The system is always in the market (stop-and-reverse) and uses no confirmation filter — Weissman presents it as the benchmark against which every added filter, whipsaw-waiting period, or alternate indicator (Ichimoku, three-MA, MACD, DMI) is compared in the book, and notes that in his tests, adding complexity to this system usually made results worse, not better.

## Rules

**Indicators needed**
1. A 9-day simple moving average (SMA) of closing prices.
2. A 26-day simple moving average (SMA) of closing prices.

**Entry / exit (stop-and-reverse — always in the market)**
3. Go long (and exit/cover any existing short) when the 9-day SMA closes above the 26-day SMA.
4. Go short (and exit/cover any existing long) when the 9-day SMA closes below the 26-day SMA.
5. Signals are evaluated on the closing price of each bar; the trade is entered at the next bar's open (Weissman's stated convention for avoiding false intraday triggers).
6. No separate stop-loss, profit target, or time exit is built into the base system — every exit is simply the opposite entry signal.

**Portfolio construction (as tested)**
7. Trade one contract per signal across a diversified portfolio of low/negatively correlated instruments — the book's 10-year backtest used one representative asset from each of: equity index, mid/long-term rates, short-term rates, a European currency, a Asian currency, energy, metals, grains, meats, and food/fiber.
8. Deduct a flat $100 per round-turn trade for slippage and commissions in any backtest of this system.

**Optional refinements (tested separately, not part of the base system)**
9. A whipsaw-waiting-period filter (e.g., Ichimoku's requirement that the longer moving average also be sloping in the crossover's direction) can be added to reduce false signals, but Weissman's own test showed this filter cut the two-MA version's annualized return from 8.48% to 1.26% while nearly quadrupling its maximum drawdown (19.98% to 67.72%) — he presents this as a caution against assuming any filter will help.
10. A percentage-of-value stop-loss (e.g., 3% of the asset's value at entry) can be layered on top of the crossover signal to cut the tail risk of large single-trade losses; Weissman shows this improves profit-to-maximum-drawdown even when it slightly reduces total net profit.

## Risk

No per-trade stop-loss is specified in the base version; risk is defined entirely by how long the market takes to generate an opposite crossover signal. In the book's 10-year (1992–2002) backtested portfolio, assuming $200,000 under management: 8.48% average annualized return on investment, 19.98% maximum peak-to-valley drawdown, 61.18% losing trades, and 10 maximum consecutive losses, with almost two years between some equity peaks. Individual components varied widely — Japanese yen and lean hogs were the strongest contributors (P:MD of 1.97 and 4.26 respectively), while gold and soybeans were net losers over the period. Weissman's general risk-management chapter (not part of this system specifically) recommends capping per-position risk at 1–2% of total account equity and using fixed-fractional position sizing to scale contract count with account equity.

## Caveats

The backtest uses a single data vendor (CQG), a single decade, and a flat $100/round-turn cost assumption that may not generalize to other eras, brokers, or instruments. The system is a stop-and-reverse design, meaning it is always exposed to trend risk with no flat/neutral state — during range-bound periods (Weissman flags equity indices in particular as chronically whipsaw-prone for this design) it will generate a high proportion of losing trades, offset only if a small number of large trending moves compensate. The book explicitly warns against "optimizing" this system by adding filters or by cutting profitable trades short at a fixed target, arguing from its own comparative tests that such changes usually curve-fit to the backtest period and can catastrophically increase drawdown (as with the Ichimoku filter above) or reduce the very outlier trades that supply most of a trend-following system's profit.
