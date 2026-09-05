---
title: "Van Tharp's Four Position-Sizing Models"
author: "Van K. Tharp"
year: 1998
slug: trade-your-way-to-financial-freedom--position-sizing-models
tier: A
category: "Money Management & Position Sizing"
tags: [position-sizing, percent-risk, percent-volatility, money-management, anti-martingale]
difficulty: intermediate
doc_type: system
parent: trade-your-way-to-financial-freedom
pages: 181
one_liner: "Four ways to answer 'how many shares or contracts' from account equity: fixed units per dollar amount, equal value units, percent risk, and percent volatility — demonstrated on identical backtests to isolate the sizing effect."
related: []
source_file: "Trade_Your_Way_to_Financial_Freedom.pdf"
---

## What it is

A comparison of four "anti-martingale" position-sizing algorithms — methods that increase bet size as equity grows, never after a loss — each answering the single question "how much/how many?" from current account equity. Tharp holds entry and exit logic completely constant (a 55-day/21-day channel breakout on 10 commodities, 1981-1991, starting at $1 million, plus a separate 1992-1997 Dow-30 stock test) and varies only the sizing model, producing results from a $32,567 baseline (fixed 100 shares/trade) to $2,109,266 (percent volatility at 0.5%) on identical signals. The lesson: "how much" typically explains more of the variance in real-world trading results than the entry signal itself.

## Rules

**Model 1 — One unit per fixed amount of money**
1. Trade one unit (100 shares, one contract) per fixed dollar amount X of equity (e.g., one contract per $50,000); recompute only when equity crosses the next multiple of X.
2. Never rejects a trade as "too risky," but treats all instruments as equivalent regardless of actual dollar volatility, and a small account must roughly double before adding a unit — near-zero effective sizing at small equity.

**Model 2 — Equal value units (stock/unleveraged traders)**
3. Divide capital into a fixed number of equal-dollar units (e.g., five $10,000 units on $50,000); buy as much of each candidate as one unit affords, rounded down.
4. For futures, cap total dollar value willing to be controlled, divide into units, and only trade an instrument if one unit covers at least one contract.
5. Gives equal portfolio weighting and transparent leverage, but still scales slowly for small accounts and equalizes face value, not actual risk.

**Model 3 — The percent risk model**
6. Per-unit risk ("1R") = dollar distance from entry to protective stop × contract/point value.
7. Fix a percentage of equity to risk per position: under 1% managing others' money, up to ~3% trading your own is comfortable, beyond 3% is "gunslinger" territory.
8. Position size = (equity × risk %) ÷ per-unit dollar risk, rounded down; recompute per signal so total open risk stays capped regardless of instrument volatility.
9. First model to make "1R" mean the same thing across every market, which is what makes R-multiples comparable system-wide.

**Model 4 — The percent volatility model**
10. Measure volatility as average true range over a lookback (Tharp uses 10-20 days); convert to a dollar figure per contract/100 shares.
11. Fix a percentage of equity to expose to one day's normal volatility swing (Tharp's tested range ~0.1% to several percent; 0.5-1.0% suited his breakout system).
12. Position size = (equity × volatility %) ÷ dollar volatility per unit, rounded down; best for tight-stop systems where percent risk would oversize positions.

## Risk

The fixed-amount model broke down entirely below roughly $20,000-$30,000 starting equity, while a $1 million account produced $13.5-30 million at aggressive per-unit-dollar settings. On the 10-commodity futures test, percent risk at 0.10% returned almost nothing (0.7% annualized, negligible drawdown), while 25% risk gave the best reward-to-risk ratio but an 84% max drawdown and margin calls above 10%. On the Dow-30 test (identical signals across all models), percent risk at 1% returned 20.9% annually (14.1% max drawdown) and percent volatility at 0.5% returned 22.9% annually (16.6% max drawdown) — both far ahead of fixed-amount (5.75%) and equal-value (3.86%). Tharp's recommendation: percent risk suits long-term trend followers with wide trailing stops; percent volatility suits tight-stop traders, since it avoids oversizing relative to typical daily price swings.

## Caveats

The specific percentages that "worked" (1% risk, 0.5% volatility) are period- and system-specific, not universal — Tharp says the right percentage depends on your own system's expectancy and stop width. A cited critique (trader Gallacher): a fixed percent risk can correspond to one contract or many depending on stop distance, so two "equal risk" positions can carry very different real exposure. None of the four models accounts for correlation between simultaneously held positions — sizing is computed per instrument independently, so a portfolio of correlated markets (e.g., several currencies at once) can carry more aggregate risk than any single position's calculation suggests.
