---
title: "The One-Minute Commodity Trader"
author: Larry Williams
year: 2005
slug: williams-larry-trade-stocks-and-commodities-with-the-insiders--one-minute-commodity-trader
tier: A
category: Trend Following & Mechanical Systems
tags: [cot-report, commercials, trend-filter, futures, moving-average, sentiment]
difficulty: intermediate
doc_type: system
parent: williams-larry-trade-stocks-and-commodities-with-the-insiders
pages: 224
one_liner: "A weekly futures system combining a 52-week moving-average trend filter with a 6-month COT Index of commercial hedger positioning."
related: [turtletrader, dynamic-breakout-ii-strategy]
source_file: "Williams Larry - Trade Stocks and Commodities With the Insiders.pdf"
---

## What it is

A weekly, chart-based futures system from Chapter 13 that filters out the false or premature signals produced by the raw COT Index (see the parent page) by requiring agreement between price trend and commercial hedger positioning. Commercials must hedge continuously as part of their business, so they are sometimes "early," but when their positioning extreme lines up with an already-established price trend, setups are markedly cleaner than COT extremes alone. Williams calls it "one-minute" because, once a chart carries the moving average and COT Index, scanning it for a valid setup takes well under a minute per market per week.

## Rules

**Universe:** any actively traded futures market with a CFTC COT report (illustrated on bonds, gold, orange juice, wheat, British pound, Swiss franc, S&P 500).

**Timeframe:** weekly bars, evaluated once a week.

**Step 1 — Trend direction:** compute a 52-week simple moving average of price. Uptrend if this week's 52-week MA is higher than last week's; downtrend if lower.

**Step 2 — 6-month COT Index for commercials:**
```
COT Index = [(This week's commercial net position − lowest in past 6 months) /
             (highest in past 6 months − lowest in past 6 months)] × 100
```
Same normalization as the standard 3-year COT Index, but with a 6-month lookback, making it more responsive.

**Step 3 — Entry:** long when trend is up AND the 6-month COT Index is above roughly 80% (or buy calls); short when trend is down AND the index is below roughly 20% (or buy puts). No trade when trend and COT Index disagree — these are the premature signals the trend filter removes.

**Step 4 — Exit/stop:** trail at the lowest low of the last 17 trading days for longs (highest high for shorts), excluding inside days. After a stop-out, re-enter with the trend at the highest high of the last 13 days (lowest low for shorts) if the COT extreme hasn't reversed. No fixed profit target; Williams notes trends rarely run past ~15 weeks without a significant correction, offered as a caution rather than a time-stop rule.

**Frequency:** qualifying setups are infrequent (e.g., only 7 signals in orange juice over 2000-2004) — a low-frequency, selective filter, not a weekly signal in every market.

## Risk

No fixed percent-of-equity figure is given; risk runs entirely through the 17-day trailing stop, sized by whatever dollar loss the trader has decided is acceptable. The book's own test (Table 13.1, five markets, 2000-2004, "52-week MA rising AND 6-month COT Index > 80%," no exit rule specified) reported 54-71% win rates and positive profit in all five markets (British pound, bonds, Swiss franc, S&P 500, gold) — a small, in-sample illustration, not a walk-forward backtest, and it tests only the long side. Diversification across uncorrelated futures markets is implied by the examples but never stated as an explicit sizing rule.

## Caveats

The 80%/20% thresholds and 17-day/13-day stop parameters are stated as fixed numbers but not shown to be optimized or robustness-tested — they read as working defaults. The only backtest covers a short five-year window on a handful of markets and only the long side, so the reported win rates should not be treated as a validated edge. The 6-month lookback is more reactive than the parent book's 3-year standard but also more prone to distortion by short-term seasonal hedging patterns, a risk the book doesn't address. The system also depends on pre-2009 CFTC legacy categories; post-2009 disaggregated reporting (separating swap dealers and managed money from commercials) can change what "commercial" positioning means in financialized markets like stock indexes and currencies.
