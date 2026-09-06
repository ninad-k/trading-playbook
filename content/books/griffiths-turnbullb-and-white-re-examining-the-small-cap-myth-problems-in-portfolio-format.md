---
author: Mark D. Griffiths, D. Alasdair S. Turnbull, Robert W. White
category: Quant, Microstructure & Academic Research
difficulty: advanced
doc_type: paper
one_liner: Intraday simulation shows small-cap turn-of-the-year outperformance largely
  disappears once real order-book liquidity constraints replace the assumption of
  instant execution.
pages: 21
related:
- supply-demand
- foucault-kadan-and-kandel-limit-order-book-as-a-market-for-liquidity
reviewed_pdf_pages: 1, 5, 8, 12, 17 (the trading-cost methodology and the small-cap-versus-large-cap
  results)
slug: griffiths-turnbullb-and-white-re-examining-the-small-cap-myth-problems-in-portfolio-format
source_file: Griffiths, Turnbullb And White-Re-Examining The Small-Cap Myth Problems
  In Portfolio Formation An.pdf
source_review: partial
tags:
- small-cap
- turn-of-the-year-effect
- liquidity
- portfolio-formation
- transaction-costs
- academic-paper
tier: B
title: 'Re-examining the Small-Cap Myth: Problems in Portfolio Formation and Liquidation'
year: 1999
---

## Summary

Question: are reported excess returns of small-cap stocks at the turn of the tax year actually realizable once real trading constraints are accounted for? Data: complete Toronto Stock Exchange order-flow and quote data, 1984-1994, plus a NYSE replication for 1993-1994, simulating a $10 million market-order purchase and liquidation of small-cap and large-cap decile portfolios around each year-end. Method: an intraday simulation that consumes actual quoted volume at bid/ask prices — rather than assuming unlimited liquidity at closing prices, as standard regression studies do — tracking how long formation and liquidation actually take. Finding: large-cap portfolios outperformed small-cap portfolios by 2.4% (single-day formation) to 6.5% (month-long formation); the small-cap portfolio could not be fully liquidated by the end of any holding period in the sample; this contradicts standard regression-based estimates of the small-firm effect, which assume frictionless, instantaneous trading.

## Key points

- Small-cap portfolio formation typically required 12-13 trading days to invest $10 million (versus under half a day for the large-cap portfolio) due to insufficient quoted ask-side volume.
- In no year could the small-cap portfolio be fully divested by the end of the roughly 4-5 month holding period; unsold shares had to be marked down to one tick below the last bid.
- Large-cap portfolio outperformed small-cap by 2.4% when portfolios were formed on the last trading day of the year, and by 6.5% when formed over the full prior month.
- Regression-based (closing-price) analysis of the same underlying data suggested small-caps outperformed large-caps by roughly 1.4%/day over the 5-day turn-of-the-year window — the opposite conclusion from the simulation, illustrating the gap between paper returns and realizable returns.
- Findings replicate on 1993-1994 NYSE data, suggesting the liquidity problem is not unique to the smaller Toronto market.
- Results held even when returns were computed from the bid-ask midpoint rather than raw transaction prices, ruling out spread costs alone as the explanation.

## Actionable rules

None given — this is an empirical academic study, not a trading system. Practical takeaway: back-tested "edges" that assume instant execution at closing prices can substantially overstate what a real small-cap portfolio strategy would earn once market depth and liquidation time are priced in.

## Caveats

Sample period (1984-1994, plus a 1993-1994 NYSE check) predates modern electronic/algorithmic liquidity provision, so the absolute liquidity constraints found here may be less severe in today's markets, though the general formation/liquidation asymmetry likely still applies to genuinely illiquid names. The study assumes liquidation of unsold shares at one tick below the last bid, which the authors note biases in favor of finding a small-cap premium — i.e., their negative finding is conservative.

## Who it is for

Quant researchers and portfolio managers evaluating whether a small-cap or calendar-anomaly strategy is actually tradable at scale, not just profitable on paper.
