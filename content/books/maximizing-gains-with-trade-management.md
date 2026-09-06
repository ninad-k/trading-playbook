---
title: "Portfolio-Level Commodity Trading: Maximizing Risk-Adjusted Gains with Trade Management"
author: "Nelson F. Freeburg"
year: 1997
slug: maximizing-gains-with-trade-management
tier: B
category: Money Management & Position Sizing
tags: [trade-management, exits, expectancy, futures]
difficulty: intermediate
doc_type: article
pages: 11
one_liner: "A portfolio backtest shows how per-trade risk, aggregate exposure, and margin caps radically change returns and drawdowns."
related: [choosing-a-trading-system-that-actually-works, david-c-stendahl-money-management-strategies-for-serious-traders]
source_file: "Maximizing Gains With Trade Management.pdf"
source_review: full
reviewed_pdf_pages: "1-11"
---
## Summary

Freeburg’s *Formula Research* article tests how portfolio-level position sizing and exposure limits change a fixed futures system’s historical results. A four-currency example starts with $50,000 and, at one contract per signal, earns $63,087 with an 18.2% compound annual return, 29% drawdown, and a 16-month longest drawdown (p. 3). Risking 5% of equity per trade without an effective aggregate constraint raises profit to $132,000 but also drawdown to 48%. Adding a 20%-of-equity margin cap produces $194,000, 38% annual return, 38% drawdown, and an eight-month longest drawdown (p. 4). The source’s point is that sizing and portfolio constraints can dominate the same entry and exit rules.

## Key points

- The currency system buys after two lower lows and a higher low when the close is above its 28-day simple average and the next open exceeds the close; it trails at the lowest low of ten days, with mirrored short rules (p. 3).
- A second ATR breakout system enters one tick beyond an 84-day extreme and uses the tighter of a dynamic true-range stop and a volatility stop (p. 5).
- The ATR portfolio selected 19 profitable markets from 27 during 1984-1994, then tested 1981-1983 and 1995-April 1997 out of sample. Single lots produced $561,863, 17.4% annual return, 45% drawdown, and 1,032 trades with 46% profitable (p. 6).
- Limiting ATR risk to 3.5% per trade and 11% across open positions raised the reported annual return to 22% and reduced drawdown to 25%; changing the total cap to 12.5% produced 27.6% and 27%, respectively (p. 7).
- Bob Spear’s appended comments dispute some of Freeburg’s software descriptions and warn that selecting only profitable markets risks curve fitting (pp. 10-11).

## Actionable rules

1. Define per-trade risk from a reproducible measure, then round the permitted equity risk down to a whole number of contracts as illustrated on p. 4.
2. Apply an aggregate portfolio constraint in addition to per-trade risk; the examples test total margin or total dollars at risk (pp. 2, 4, 7-9).
3. Evaluate return and drawdown together. In the final test, raising per-trade risk from 1% to 4% increased reported annual return from 17.0% to 49.6% while drawdown rose from under 14% to 40.0% (pp. 8-9).

## Caveats

All performance is hypothetical historical testing, and the article explicitly says it is less dependable than actual results and cannot guarantee future profitability (p. 9). The market-selection step retains only 19 of 27 profitable in-sample markets, a choice Spear flags as possible curve fitting (pp. 6, 11). Large terminal wealth figures assume compounding and executable scaling, and some tested variants suffered drawdowns above 50%.

## Who it is for

System developers studying portfolio sizing, aggregate exposure, compounding, and drawdown tradeoffs.
