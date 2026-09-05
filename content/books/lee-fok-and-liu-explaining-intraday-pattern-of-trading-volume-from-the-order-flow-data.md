---
title: "Explaining Intraday Pattern of Trading Volume from the Order Flow Data"
author: "Yi-Tsung Lee, Robert C.W. Fok, Yu-Jane Liu"
year: 2001
slug: lee-fok-and-liu-explaining-intraday-pattern-of-trading-volume-from-the-order-flow-data
tier: B
category: Quant, Microstructure & Academic Research
tags: [order-flow, trading-volume, intraday-patterns, market-microstructure, information-asymmetry, academic-paper]
difficulty: advanced
doc_type: paper
pages: 32
one_liner: "Taiwan Stock Exchange order-book data shows a J-shaped (not U-shaped) intraday volume pattern, driven more by liquidity flow than informed trading."
related: [supply-demand, foucault-kadan-and-kandel-limit-order-book-as-a-market-for-liquidity, the-interaction-between-the-frequency-of-market-quotes-spread-and-volatility-in-forex]
source_file: "Lee, Fok And Liu - Explaining Intraday Pattern Of Trading Volume From The Order Flow Data.pdf"
---

## Summary

Question: why does trading volume spike at the market open and close, and how does informed vs. uninformed traders' order placement drive that pattern? Data: the complete limit order book for the 30 most-traded stocks on the Taiwan Stock Exchange (TWSE), March-May 1995, covering 46% of total market value; TWSE is an agency call-auction market with price-time priority and no dealer/specialist. Method: classifies orders by size (large = informed, small = uninformed) and by whether they execute immediately ("real" orders) or sit away from the market ("waiting" orders), then regresses volume on informed/uninformed and real/waiting order flow across 31 intraday intervals. Finding: contrary to the classic U-shaped pattern found on the NYSE/Toronto, TWSE volume follows a J-shape (heaviest near the close); both informed and uninformed investors place the most orders at the open and close, but real orders are J-shaped while waiting orders are reverse-J-shaped; and uninformed (liquidity) order flow has a slightly larger effect on volume than informed order flow.

## Key points

- TWSE call-auction structure: the open call accumulates orders from 8:30-9:00am; subsequent calls execute roughly every minute; no dealer/specialist intermediary.
- Volume is J-shaped, not U-shaped: the largest orders are placed at the open, but only moderate executed volume results, because traders place conservative/away-from-market orders then.
- Orders are split into "real" (executable at submission) and "waiting" (priced away from the market) to separate genuine trading intent from price-priority positioning.
- Real orders (informed and uninformed alike) show a J-shaped pattern matching volume; waiting orders show a reverse-J pattern, shrinking as the session progresses and uncertainty resolves.
- Regression coefficients for both informed and uninformed order flow are significant in every interval tested; the uninformed (liquidity) coefficient is consistently larger.
- Results hold across six alternative size/price thresholds used to define informed/uninformed and real/waiting orders.

## Actionable rules

None given — this is an academic microstructure study, not a trading system. Practical read for traders: on markets with this order-book structure, visible order-book depth at the open can overstate likely executed volume (much of it is exploratory "waiting" order flow), and liquidity-driven flow — not just informed trading — is the larger driver of volume spikes at the open and close.

## Caveats

Findings are specific to the Taiwan Stock Exchange's call-auction, no-dealer market structure in 1995 and may not generalize to continuous double-auction or dealer markets (the U-shaped pattern found elsewhere is explicitly contrasted). The informed/uninformed classification is a size-based proxy (e.g., orders over 20 lots vs. under 5-20 lots), not a direct measure of who possesses private information.

## Who it is for

Researchers and quant traders interested in how order-book composition (informed vs. uninformed, real vs. waiting orders) explains intraday volume patterns, particularly in auction-market structures outside the US.
