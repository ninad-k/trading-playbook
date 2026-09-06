---
author: Yasushi Hamao, Joel Hasbrouck
category: Quant, Microstructure & Academic Research
difficulty: advanced
doc_type: paper
one_liner: Academic microstructure study finding that Tokyo Stock Exchange's pure
  limit-order-book system (no dealers) supplies immediacy nearly as well as dealer
  markets, using warning/special quotes to slow large orders.
pages: 30
related:
- madhavan-market-microstructure-a-survey
- de-matos-and-fernandes-testing-the-markov-property-with-ultra-high-frequency-financial-dat
- hartmann-manna-and-manzanares-the-microstructure-of-the-euro-money-market
reviewed_pdf_pages: 1-2, 4 (the market description, tick-size rules and sample period)
slug: hamao-and-hasbrouck-securities-trading-in-the-absence-of-dealers-trades-and-quotes-on-the
source_file: Hamao And Hasbrouck-Securities Trading In The Absence Of Dealers - Trades,
  And Quotes On The Toky.pdf
source_review: partial
tags:
- market-microstructure
- limit-order-book
- tokyo-stock-exchange
- liquidity
- academic
- price-limits
tier: B
title: 'Securities Trading in the Absence of Dealers: Trades and Quotes on the Tokyo
  Stock Exchange'
year: 1995
---

## Summary

Published in the Review of Financial Studies (1995). Question: can a market with no dealers or market makers — where all liquidity comes from public limit orders — supply immediacy comparable to dealer-based markets like the NYSE? Data: intraday trade and quote records for three actively traded Tokyo Stock Exchange (TSE) stocks over the first three months of 1990. Method: descriptive statistics on execution delay and price improvement, plus a dynamic VAR of trades and quote revisions to study how the TSE's "warning"/"special" quote mechanism (pausing and re-displaying large orders that would otherwise walk through the book) affects price impact. Finding: public-order liquidity was good — small orders were blocked from immediate execution less than 5% of the time — and about one-fifth of paused orders received price improvement, but delayed orders had a larger cumulative price impact than orders executed immediately in full.

## Key points

- TSE prohibits members from placing proprietary limit orders on both sides of the market, structurally preventing de facto dealers from emerging.
- Tick sizes run 0.1%-1% of price; sessions open with a call auction (itayose) before continuous double-auction trading (zaraba).
- Large orders that would walk through the book are only partially executed; the remainder becomes a "warning" or "special" indicative quote inviting competing liquidity for up to about a minute.
- Roughly one-fifth of these indicative quotes get hit by competing liquidity, delivering price improvement.
- Small hypothetical orders were blocked from immediate execution less than 5% of trading time — good public liquidity supply.
- Delayed (paused) orders show larger cumulative price impact in the VAR analysis than immediately executed orders of the same size, implying the mechanism affects market depth, not just transient smoothing.
- Post-trade quotes tend to keep moving in the initiating trade's direction, from order-flow autocorrelation and cancellation of limit orders that set the best quote.
- Single-price fills show continuation; multi-level fills tend to show reversals afterward, suggesting liquidity partially restores after large trades.

## Actionable rules

None given as trading signals — an empirical microstructure study. Transferable insight: in a pure limit-order-book market, a large order that triggers a price-limit pause tends to carry more information (larger subsequent impact) than one executing immediately, and roughly 1 in 5 paused orders see meaningful price improvement for a patient trader.

## Caveats

Narrow sample — three stocks, three months, 1990 data — and TSE rules have since evolved. Technical academic paper requiring familiarity with VAR-based microstructure methodology.

## Who it is for

Market-microstructure researchers and quants studying limit-order-book dynamics, not retail traders seeking a system.
