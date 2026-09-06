---
author: Hendrik Bessembinder, Kumar Venkataraman
category: Quant, Microstructure & Academic Research
difficulty: advanced
doc_type: paper
one_liner: Study of 92,170 Paris Bourse block trades finds upstairs (broker-negotiated)
  markets lower execution costs by tapping unexpressed liquidity and certifying trades
  as uninformed, even alongside a modern electronic order book.
pages: 43
related:
- madhavan-market-microstructure-a-survey
- hamao-and-hasbrouck-securities-trading-in-the-absence-of-dealers-trades-and-quotes-on-the
- competition-between-exchanges-euronext-versus-xetra
reviewed_pdf_pages: 1-4, 6, 14 (the sample description and the upstairs-market volume
  and cost results)
slug: bessembinder-and-venkataraman-does-an-electronic-stock-exchange-need-an-upstairs-market
source_file: Bessembinder And Venkataraman-Does An Electronic Stock Exchange Need
  An Upstairs Market.pdf
source_review: partial
tags:
- market-microstructure
- block-trading
- upstairs-market
- paris-bourse
- execution-costs
- academic-research
tier: B
title: Does an Electronic Stock Exchange Need an Upstairs Market?
year: 2002
---

## Summary

Question: does a fully electronic limit-order exchange still need a parallel "upstairs" market where brokers negotiate large trades by hand — or should theory's prediction that electronic order books are strictly more efficient hold in practice? Data: 92,170 block trades across 225 Paris Bourse stocks, chosen because the Bourse's downstairs (electronic) market closely matches the idealized markets in theoretical models, and because Paris varies its "crossing rules" (whether upstairs trades must execute within the best bid-offer) across stocks, giving a natural experiment. Method: econometric models correcting for traders' self-selection between upstairs and downstairs venues, used to compare execution costs and test predictions from Grossman (1992) and Seppi (1990) about why upstairs markets exist.

## Key points

- About 67% of block-trading volume at the Paris Bourse was completed upstairs versus roughly 20% on the NYSE at the time — a much heavier reliance on negotiated block trading.
- Upstairs execution costs were less than one-third of what they would be if the same blocks had been run against displayed downstairs liquidity — direct support for the "unexpressed liquidity" hypothesis (large buyers/sellers exist who never post their interest publicly).
- Upstairs trades carried less price-moving information than downstairs trades despite being larger, supporting the theory that upstairs brokers screen out informed traders and certify blocks as liquidity-driven.
- For stocks with more flexible "crossing rules," traders used outside-the-quote execution mainly for harder trades and when downstairs liquidity was thin — trades that likely couldn't have completed otherwise.
- Overall upstairs execution costs beat downstairs costs for blocks that were actually routed upstairs, but a self-selection-corrected model shows a randomly assigned trade would face higher costs upstairs — meaning upstairs trading pays off specifically for traders who can exploit time-varying liquidity gaps or credibly signal they aren't trading on information.
- Buyer-initiated trades faced less favorable treatment (higher costs) in the upstairs market than seller-initiated trades.

## Actionable rules

None given as trading signals — this is a market-structure/execution-cost study. For a trader moving large size: the paper's practical implication is that negotiated block execution can beat displayed-market execution specifically when downstairs liquidity is thin or the order is large relative to normal volume, and that credibly signaling a trade is liquidity-driven (not informed) is what earns better upstairs pricing.

## Caveats

Findings are drawn from Paris Bourse data from the late 1990s/early 2000s and a specific regulatory "crossing rules" regime that has since changed (Euronext later loosened rules for all Paris stocks); direct transfer to modern U.S. equity or crypto market structure is not established. Requires familiarity with market-microstructure econometrics (self-selection/Heckman-style correction) to fully evaluate the cost estimates. Not a retail-trading resource — relevant mainly to institutional execution and market-design questions.

## Who it is for

Readers interested in market microstructure and institutional execution — why large block trades still get negotiated by hand even on markets with sophisticated electronic order books.
