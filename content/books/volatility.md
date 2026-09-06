---
author: Guy Bower
category: Options, Futures & Derivatives
difficulty: beginner
doc_type: article
one_liner: CDM Trading primer distinguishing historical from implied volatility and
  outlining basic strategies for trading high vs. low volatility with options.
pages: 4
related:
- using-volatility-in-option-tradingpart-1
- volatility-part-2
- mcgraw-hill-the-options-edge-winning-the-volatility-game-with-options-on-futures
reviewed_pdf_pages: 1-2 (the volatility definitions and the worked option-pricing
  example)
slug: volatility
source_file: Volatility.pdf
source_review: partial
tags:
- options
- volatility
- implied-volatility
- historical-volatility
- theta
- strangle
- ratio-spread
tier: B
title: Volatility
year: unknown
---

## Summary

A short educational piece from CDM Trading (Guy Bower) introducing option volatility for beginners. It distinguishes historical volatility (the standard deviation of the underlying's price changes over a chosen lookback) from implied volatility (the volatility figure an option's market price implies when run backward through a pricing model such as Black-Scholes). It then covers how to judge whether options are cheap or expensive and sketches basic strategies for high- and low-volatility environments.

## Key points

- Historical volatility is computed from the standard deviation of daily percentage price changes over a chosen period (e.g., 30 days); shorter windows reveal extremes, longer windows give an average.
- Implied volatility is backed out of an option's market price using a pricing model, holding the other four inputs (futures price, strike, rate, expiration) as known.
- Worked example: S&P 500 futures at 1,100, a 1,120 call trading at 20.70 with 30 days to expiry prices out to about 40% implied volatility versus a 30% theoretical value of 16.50.
- Options should be judged cheap/expensive both against their own past IV levels and against the underlying's historical volatility.
- Selling strategies for high IV: short volatility positions such as a naked strangle (sell OTM put and call) or a ratio spread (buy near-the-money, sell two or more further OTM).
- Buying strategies for low IV: near-the-money long option or straddle-like structure with plenty of time to expiration, since time decay is offset by the underlying's ongoing movement.
- Short volatility positions tend to show small steady gains punctuated by sudden losses on sharp moves; long volatility positions tend to slowly bleed value before gaining suddenly.
- Deciding whether to hold a long volatility position often comes down to whether IV has returned to "normal" levels.

## Actionable rules

1. Compare current implied volatility to (a) its own recent history and (b) the underlying's historical volatility before entering a volatility trade; the best opportunities occur when both flag the same direction (cheap or expensive).
2. When selling volatility, prefer out-of-the-money strikes (naked strangle or ratio spread) to give the underlying room to move and to reduce the odds of costly adjustments.
3. When buying volatility, buy near-the-money options with ample time to expiration rather than far OTM or near-dated contracts.
4. Hold a mix of long- and short-volatility positions in a portfolio given their opposite risk/reward and psychological profiles.
5. Close (or rebalance) a long volatility position once volatility has normalized; keep an adjusted position open if it has not.

## Caveats

Extremely brief and introductory; gives no numeric thresholds for what counts as "high" or "low" IV, no position-sizing guidance, and the worked example uses one illustrative option-pricing scenario rather than backtested results. Includes a standard risk disclaimer noting it is not personalized advice.

## Who it is for

Traders new to options who need a plain-language first pass at historical vs. implied volatility before moving to more technical volatility-trading material.
