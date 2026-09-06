---
author: Pierre Giot & Joachim Grammig
category: Quant, Microstructure & Academic Research
difficulty: advanced
doc_type: paper
one_liner: Discussion paper introducing a Value-at-Risk methodology that prices in
  liquidity risk (price impact of liquidation) for portfolios traded on the Xetra
  automated auction market.
pages: 35
related:
- depth-volatility
- madhavan-market-microstructure-a-survey
- hollifield-miller-sandas-and-slive-liquidity-supply-and-demand-in-limit-order-markets
reviewed_pdf_pages: 1-4 (title, authors and abstract; the body's text extraction is
  corrupted and could not be read)
slug: how-large-is-liquidity-risk-in-an-automated
source_file: How Large Is Liquidity Risk In An Automated.pdf
source_review: partial
tags:
- liquidity-risk
- value-at-risk
- market-microstructure
- limit-order-book
- academic-research
tier: B
title: How Large Is Liquidity Risk in an Automated Auction Market?
year: 2002
---

## Summary

Question: how large is liquidity risk — the extra loss from having to liquidate a position and moving the price against yourself — for stocks and portfolios traded on a pure electronic limit-order market? Data: order-book data from Xetra, the automated auction system used on several European exchanges, supplied by Deutsche Börse AG. Method: the authors extend a standard Value-at-Risk (VaR) framework to explicitly incorporate the price impact of liquidating a position of a given size, producing a "liquidity risk premium" on top of conventional price-risk VaR, and examine how this premium varies with portfolio/position size and the VaR time horizon. Finding (per the abstract): liquidity risk is sensitive to both position size and holding/liquidation horizon, and exhibits an intraday ("diurnal") pattern consistent with market-microstructure theory (i.e., liquidity risk is not constant through the trading day).

## Key points

- Introduces liquidity-adjusted VaR: standard price-risk VaR plus a liquidity risk premium reflecting the price impact of unwinding a position.
- Studied on Xetra, a computerized, order-driven ("automated auction") market with no designated market maker.
- Liquidity risk premiums are computed at both the individual-stock and portfolio level.
- Sensitivity analysis covers two dimensions: how much is being liquidated (portfolio/position size) and over what time horizon (VaR horizon).
- Liquidity risk shows a diurnal (time-of-day) pattern, which the authors interpret through market microstructure theory (i.e., liquidity varies predictably across the trading session, likely thinner near the open/close).
- JEL classification: liquidity, Value-at-Risk, microstructure — positions this as institutional risk-management research, not a trading strategy paper.

## Actionable rules

None given — this is a risk-measurement methodology paper, not a trading system. The practical takeaway for traders and risk managers: standard VaR understates true risk for a position that must be liquidated quickly, and that understatement grows with position size and shrinks (or grows, depending on time-of-day liquidity) with the assumed liquidation horizon — position sizing and stop-out planning should account for expected slippage, not just quoted volatility.

## Caveats

The source PDF's text extraction was corrupted beyond the title, author, and abstract (pages 1–4); the detailed methodology, tables, and specific numeric findings from the body of the paper could not be read and are not represented here beyond what the abstract states. This is a 2002 academic discussion paper reflecting late-1990s/early-2000s Xetra market conditions and may not reflect current European equity market liquidity dynamics.

## Who it is for

Risk managers and quant researchers who need a framework for pricing liquidity risk into VaR for order-driven electronic markets; not a resource for retail trade setups.
