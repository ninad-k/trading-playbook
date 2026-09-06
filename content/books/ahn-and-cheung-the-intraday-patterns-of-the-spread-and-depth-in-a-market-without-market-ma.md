---
author: Hee-Joon Ahn and Yan-Leung Cheung
category: Quant, Microstructure & Academic Research
difficulty: advanced
doc_type: paper
one_liner: Empirical study of 471 Hong Kong stocks finding U-shaped intraday/intraweek
  spreads and reverse-U-shaped depth, proving these patterns arise from limit-order
  traders alone, without any specialist market maker.
pages: 18
related:
- admati-and-pfleiderer-a-theory-of-intraday-patterns-volume-and-price-variability
- sarin-and-saudagaran-testing-for-micro-structure-effects-of-international-dual-listings-us
reviewed_pdf_pages: 7-9, 16-17 (the descriptive statistics and the spread/depth correlation
  tables)
slug: ahn-and-cheung-the-intraday-patterns-of-the-spread-and-depth-in-a-market-without-market-ma
source_file: Ahn And Cheung-The Intraday Patterns Of The Spread And Depth In A Market
  Without Market Makers - .pdf
source_review: partial
tags:
- market-microstructure
- bid-ask-spread
- market-depth
- limit-order-book
- liquidity
- adverse-selection
- academic-paper
tier: B
title: 'The Intraday Patterns of the Spread and Depth in a Market Without Market Makers:
  The Stock Exchange of Hong Kong'
year: 1999
---

## Summary

Published in the Pacific-Basin Finance Journal (1999), this paper asks whether the well-documented U-shaped intraday spread and reverse-U-shaped depth patterns on the NYSE are caused by specialist market-making behavior, or arise naturally from limit-order trading alone. The Stock Exchange of Hong Kong (SEHK) is used as a clean test case: a purely order-driven market with no market makers or floor specialists, only limit orders matched by an automated system. Using six months of trade and quote data (Oct 1996-Mar 1997) on 471 common stocks, the authors compute intraday/intraweek patterns of spreads, depth, and trading activity, with dummy-variable regressions controlling for firm size, day of week, and time of day.

## Key points

- Both quoted and effective spreads show a U-shape: highest in the first half-hour (quoted 2.05%, effective 1.29%), declining through the day, then rising again in the last half-hour (quoted 1.71%, effective 1.26%).
- Market depth shows the mirror-image reverse-U-shape: lowest at the open, rising to a peak just before the last half-hour, then dropping.
- Trading volume is also U-shaped intraday, concentrated at the open and close.
- Intraweek: spreads are narrowest Tuesday/Wednesday and widest Friday (quoted) or Monday (effective); depth is lowest at the start/end of the week — consistent with NYSE findings.
- Spread and depth are negatively correlated stock-by-stock in every half-hour interval (average -0.123), strongest at the open and close — evidence limit-order traders trade off price against quantity.
- Average percentage quoted spread 1.73% (vs. ~0.6% cited for NYSE at the time), decreasing monotonically with firm size and stock price.
- Findings replicate Lee, Mucklow & Ready's (1993) NYSE result that wide spreads pair with small depths — but here with zero specialist participation, challenging the assumption that specialists cause the U-shape.
- Interpretation: informed trading concentrates around the open/close, so liquidity providers widen spreads and shrink displayed size to protect against adverse selection at those times.

## Actionable rules

1. Expect the widest effective spreads and thinnest displayed depth at the market open and in the final trading interval — treat these windows as the highest-adverse-selection-risk times to post or take liquidity, on any order-driven (non-market-maker) exchange, not just NYSE-style markets.
2. When gauging true liquidity, look at spread and depth together, not spread alone — a narrow spread paired with thin depth is not necessarily "liquid."
3. Expect wider spreads and thinner depth around the beginning (Monday) and end (Friday) of the trading week versus midweek.
4. Smaller-capitalization, lower-priced stocks carry structurally wider percentage spreads and thinner depth than large caps — factor this into execution-cost estimates when sizing orders in an order-driven market.

## Caveats

This is a pure academic microstructure study (no trading system, no P&L). Findings are specific to the SEHK's institutional structure in 1996-97 (a limit-order-only automated matching system, tick-size schedule from HK$0.001 to HK$2.50, a midday lunch break) and to the sample's price/liquidity filters (stocks priced HK$0.25-100, ≥60 listing days); the tick-size regime and market structure of most exchanges (including the SEHK itself) have since changed materially, and the paper does not test whether the pattern holds under decimalized, high-frequency modern markets.

## Who it is for

Quant researchers and market-microstructure students studying bid-ask spread and depth dynamics, and execution traders who want empirical grounding for avoiding the open/close in illiquid, order-driven markets.
