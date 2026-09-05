---
title: "Securities Trading in the Absence of Dealers: Trades and Quotes on the Tokyo Stock Exchange"
author: "Yasushi Hamao, Joel Hasbrouck"
year: 1995
slug: hamao-and-hasbrouck-securities-trading-in-the-absence-of-dealers-trades-and-quotes-on-the
tier: B
category: Quant, Microstructure & Academic Research
tags: [market-microstructure, limit-order-book, tokyo-stock-exchange, liquidity, academic, price-limits]
difficulty: advanced
doc_type: paper
pages: 30
one_liner: "Academic microstructure study finding that Tokyo Stock Exchange's pure limit-order-book system (no dealers) supplies immediacy nearly as well as dealer markets, using warning/special quotes to slow large orders."
related: [madhavan-market-microstructure-a-survey, de-matos-and-fernandes-testing-the-markov-property-with-ultra-high-frequency-financial-dat, hartmann-manna-and-manzanares-the-microstructure-of-the-euro-money-market]
source_file: "Hamao And Hasbrouck-Securities Trading In The Absence Of Dealers - Trades, And Quotes On The Toky.pdf"
---

## Summary

Published in the Review of Financial Studies (1995). Question: can a market with no designated dealers or market makers — where all liquidity comes from public limit orders — supply immediacy comparable to dealer-based markets like the NYSE? Data: intraday trade and quote records for three actively traded Tokyo Stock Exchange (TSE) first-section stocks over the first three months of 1990. Method: descriptive statistics on execution delay and price improvement, plus a dynamic vector autoregression (VAR) of trades and quote revisions to study how the TSE's distinctive "warning quote" / "special quote" mechanism (which pauses and re-displays large orders that would otherwise walk through the book) affects price impact and post-trade quote behavior. Finding: liquidity from public orders alone was good — small orders were blocked from immediate execution less than 5% of the time — and about one-fifth of orders held at an indicative quote received price improvement from competing liquidity suppliers, but orders that were delayed this way had a larger cumulative price impact than orders executed immediately in full.

## Key points

- The TSE prohibits members from placing proprietary limit orders on both sides of the market, structurally preventing de facto dealers from emerging; all liquidity is public.
- Tick sizes are 0.1%-1% of the stock price; trading runs in morning (9:00-11:00) and afternoon (13:00-15:00) sessions, opening each session with a call auction (itayose) before continuous double-auction trading (zaraba).
- Large market orders that would "walk" through the limit-order book are only partially executed; the remainder is converted to a limit order and displayed as an indicative "warning" or "special" quote inviting competing liquidity for up to about a minute (at the saitori's discretion).
- Roughly one-fifth of these indicative quotes get hit by competing liquidity suppliers, delivering price improvement versus letting the order walk the book immediately.
- Small hypothetical buy/sell orders were prevented from immediate execution (due to no acceptable opposing quote) less than 5% of trading time — evidence of good public liquidity supply.
- Orders held at an indicative quote (delayed) show a larger cumulative price impact in the VAR analysis than orders executed immediately at the same size, implying the price-limit mechanism affects market depth, not just transient smoothing.
- Post-trade quotes tend to keep moving in the direction of the initiating trade (positive "continuation"), driven partly by order-flow autocorrelation and partly by cancellation of limit orders that had set the best quote.
- Orders filled at a single price show continuation; orders filled by walking through multiple price levels tend to show reversals afterward, suggesting liquidity is partially restored following large multi-level trades.

## Actionable rules

None given as trading signals — this is an empirical market-structure study, not a strategy source. The transferable insight for a trader is structural: in a pure limit-order-book market (no dealers), a large order that triggers a price-limit pause tends to carry more information (larger subsequent price impact) than one that executes immediately, and roughly 1 in 5 such paused orders will see meaningful price improvement if the trader is willing to wait rather than force immediate execution.

## Caveats

The sample is narrow — three stocks, three months, data from 1990 — and TSE institutional rules (price-limit and warning-quote procedures) have since evolved; the specific mechanics described (saitori discretion, session times) reflect the exchange as it operated at the time of study. It is a technical academic paper requiring familiarity with VAR-based microstructure methodology (Hasbrouck's own prior work) to follow the identification strategy in full.

## Who it is for

Market-microstructure researchers, quant traders studying limit-order-book dynamics, or readers comparing dealer vs. non-dealer market designs — not retail traders looking for a system.
