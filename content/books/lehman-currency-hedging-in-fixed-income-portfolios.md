---
author: Lev Dynkin, Tony Gould
category: Forex Mechanics & Macro Drivers
difficulty: advanced
doc_type: article
one_liner: Lehman Brothers research note on how FX forward hedges change a bond portfolio's
  duration and create tracking error versus hedged benchmarks.
pages: 8
related:
- interest-rate-models
- day-trading-the-currency-market
- wiley-currency-strategy-a-practitioner-s-guide-to-currency-trading-hedging-and-forecasting
reviewed_pdf_pages: 6-9 (the hedging-mechanics sections and the index weight/return
  tables)
slug: lehman-currency-hedging-in-fixed-income-portfolios
source_file: Lehman Currency Hedging in Fixed Income Portfolios.pdf
source_review: partial
tags:
- currency-hedging
- fixed-income
- forward-contracts
- duration
- tracking-error
- index-replication
- institutional
tier: B
title: Currency Hedging in Fixed Income Portfolios
year: 2003
---

## Summary

An institutional research note explaining that hedging currency exposure in a bond portfolio with FX forwards is never perfectly clean: forwards cannot fully eliminate currency volatility because bond values fluctuate between hedge resets, and using forwards also alters the portfolio's interest-rate exposure. It works through the covered-interest-arbitrage relationship that prices forwards, shows how a currency hedge swaps local interest-rate duration for base-currency duration, and discusses the tracking error created when hedge timing or tenor differs from the monthly reset used in Lehman Brothers' own bond indices.

## Key points

- Forward rates are set by covered interest arbitrage (worked example: borrow euros at 2%, invest dollars at 1%, sell forward at $/€1.08 versus spot 1.10, capturing a 0.87 euro profit on 100 euros).
- Formula: Hedged yield ≈ Bond yield + (Base currency rate − Local currency rate).
- Formula: Hedged bond duration ≈ Bond duration − tenor of the hedge, offset by an equivalent rise in base-currency duration.
- Because the hedge is sized once per month against an expected future value, intra-month market moves leave a position over- or under-hedged; a 3-month hedge with no adjustment cost a euro investor 0.11% over Q2 2003.
- Currency volatility has limited effect on overall hedged-index volatility, and fully eliminating currency risk can actually raise portfolio risk by removing a diversifying return source.
- Longer-tenor hedges (up to six months) trade increased tracking error for potentially higher carry and lower transaction costs from less frequent rolling.
- Currency moves shift hedged-index country weights (the euro's 5.4% May 2003 rise lifted the Global Aggregate's euro weight by 1.5%), requiring periodic rebalancing.

## Actionable rules

1. Hedging a foreign bond with a forward gives up local-currency rate exposure for base-currency exposure of roughly the hedge's tenor.
2. To replicate a monthly-reset hedged index intra-month, sell forward the expected month-end value of local bonds computed at month start, not the current market value.
3. Weigh a longer hedge tenor (up to ~6 months) against a shorter one: potentially higher carry and lower costs versus greater tracking error and duration mismatch.
4. Rebalance hedged-portfolio country weights periodically to offset currency-driven drift versus the benchmark.

## Caveats

Written for institutional bond-index managers benchmarked against Lehman Brothers (later Barclays/Bloomberg) hedged indices; the numeric examples (2003 rates, index composition) are dated. Not directly applicable to discretionary FX or futures traders — this is portfolio-construction and index-tracking guidance, not a directional strategy.

## Who it is for

Fixed-income portfolio managers and quants managing currency-hedged bond portfolios against benchmark indices, or anyone who wants to understand the duration and tracking-error mechanics of FX forward hedging.
