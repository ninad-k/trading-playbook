---
author: Robert F. Engle and Joe Lange
category: Quant, Microstructure & Academic Research
difficulty: advanced
doc_type: paper
one_liner: Journal of Financial Markets paper introducing VNET, an event-time measure
  of realized market depth, and modeling how volume, transaction count, spread, and
  trading patience predict it on NYSE stocks.
pages: 30
related:
- liquidity-in-forex-markets
- madhavan-market-microstructure-a-survey
- the-interaction-between-the-frequency-of-market-quotes-spread-and-volatility-in-forex
reviewed_pdf_pages: 1, 5, 11 (the VNET definition, the ACD linkage and the 1997 robustness
  check)
slug: engle-and-lange-predicting-vnet-a-model-of-the-dynamics-of-market-depth
source_file: Engle And Lange-Predicting Vnet - A Model Of The Dynamics Of Market Depth.pdf
source_review: partial
tags:
- academic-paper
- market-microstructure
- market-depth
- liquidity
- order-flow
- bid-ask-spread
tier: B
title: 'Predicting VNET: A Model of the Dynamics of Market Depth'
year: 2001
---

## Summary

An academic market-microstructure paper (Journal of Financial Markets, 2001) by Robert F. Engle and Joe Lange introducing VNET, a new intraday statistic for market depth: the net excess volume of buys over sells accumulated over a "price-duration" — the time between one substantial quote-midpoint move and the next. Rather than measuring depth in fixed calendar-time intervals (which produces too many zero/near-zero and noisy observations), the authors measure it in event time keyed to price movement, following the general approach of Cho and Frees (1988). They build a predictive model of VNET using NYSE TORQ data for 17 stocks, then check robustness on a separate, more recent (1997) TAQ dataset.

## Key points

- **VNET**: number of shares bought minus number of shares sold during a "price-duration" (the interval between successive fixed-size moves in the quote midpoint) — a direct, realized-depth analogue to the theoretical "market reaction curve."
- Market depth is distinguished from the bid-ask spread ("tightness"): depth is how much volume can be absorbed at/near a given price before it moves further, not just the gap between best bid and offer.
- VNET is found to vary systematically with total trading volume, the number of transactions within the duration, and volatility (duration length).
- The percentage order imbalance needed to move price declines as total volume traded rises — i.e., in higher-volume periods, a smaller percentage imbalance triggers the same price move.
- A higher number of transactions per price-duration is associated with reduced market depth, consistent with informed traders "flooding" the market after a semi-private information event.
- VNET moves inversely with the bid-ask spread — when the market is tight (narrow spread) it also tends to lack depth, unifying the paper's depth measure with traditional spread-based liquidity measures.
- Unanticipated shocks to the length of a price-duration (labeled PTIME-ERR, derived using Engle and Russell's 1998 ACD/autoregressive conditional duration model) increase realized depth — interpreted as "the value of patience" in large-order execution.
- Robustness check: re-estimating the model on 1997 TAQ data (different volume, volatility, and minimum-tick regime than the original TORQ sample) produced only modestly different parameter estimates, suggesting the relationships are relatively stable over time.

## Actionable rules

None given as trading rules — this is a market-microstructure research paper aimed at institutional execution and risk management, not a retail trading system. Practical implications drawn out in the paper: (1) larger total trading volume in a stock allows a larger nominal imbalance to be absorbed before price moves, useful for sizing large orders; (2) patience in execution (avoiding compressing a large order into a short price-duration) tends to reduce realized price impact; (3) periods of wide bid-ask spread should be expected to coincide with reduced depth, and vice versa.

## Caveats

This is a dense, equation-heavy econometrics paper using NYSE TORQ and TAQ transaction/quote datasets from the 1990s (individual stock symbols like GE, FDX, FNM appear in an appendix regression table); it predates decimalization and modern electronic/HFT market structure, so magnitudes are not directly transferable to today's markets even if the qualitative relationships (volume-depth, spread-depth, patience-depth) likely still hold directionally. No charts or full appendix tables are usable from the extracted text.

## Who it is for

Quant researchers and institutional execution specialists interested in the academic foundations of intraday liquidity/depth measurement, not retail traders looking for entry/exit signals.
