---
title: "Limit Order Book as a Market for Liquidity"
author: "Thierry Foucault, Ohad Kadan, Eugene Kandel"
year: 2003
slug: foucault-kadan-and-kandel-limit-order-book-as-a-market-for-liquidity
tier: B
category: Quant, Microstructure & Academic Research
tags: [limit-order-book, market-microstructure, liquidity, bid-ask-spread, market-resiliency, academic-paper]
difficulty: advanced
doc_type: paper
pages: 65
one_liner: "Theoretical model shows market resiliency after liquidity shocks rises with the share of patient traders and falls with order arrival rate and tick size."
related: [foucault-and-kadan-limit-order-book-as-a-market-for-liquidity, chordia-roll-and-subrahmanyam-market-liquidity-and-trading-activity, hollifield-miller-sandas-and-slive-liquidity-supply-and-demand-in-limit-order-markets, madhavan-market-microstructure-a-survey]
source_file: "Foucault, Kadan And Kandel-Limit Order Book As A Market For Liquidity.pdf"
---

## Summary

Question: how does traders' impatience shape order choice, spread dynamics, and how quickly a limit order market recovers after a liquidity shock? Method: a dynamic equilibrium model of an order-driven market where liquidity traders arrive sequentially, are randomly patient or impatient, and choose between market and limit orders to minimize execution cost. Finding: patient traders supply liquidity to impatient traders; market "resiliency" (the probability the spread reverts to its competitive level before the next trade) rises with the share of patient traders and falls with the order arrival rate; and reducing the minimum tick size can paradoxically widen average spreads by letting limit orders sit less aggressively.

## Key points

- Liquidity has three dimensions (Harris, 1990): tight (small spread), deep (large size), resilient (spread reverts quickly) — this paper's focus is resiliency, the least-studied of the three.
- Traders must trade for exogenous reasons and are randomly patient or impatient; only the trade-off between waiting cost and immediacy cost drives order choice.
- Patient traders bid more aggressively (tighter limit prices) when expected waiting time is longer — i.e. when patient traders are scarce or arrivals are frequent.
- Resiliency is maximal only when all traders share the same patience level; heterogeneity leaves a meaningful chance the spread stays wide until the next trade.
- Markets dominated by impatient traders show spreads skewed wide and are less resilient.
- A smaller tick size can reduce resiliency and increase the average spread where impatient traders dominate, because it lets patient traders shade their limit prices by less.
- Predicts a positive correlation between trading frequency and spread, controlling for arrival rate, and predicts spreads and trading frequency rise while limit-order aggressiveness falls over the trading day.

## Actionable rules

None given — this is a theoretical microstructure model, not a trading system. Practical read for traders: expect wider, less resilient spreads around news events or the close, when urgency-driven order flow dominates, and don't assume a smaller tick size automatically means tighter realized spreads, particularly in less liquid names.

## Caveats

Highly mathematical equilibrium model with simplifying assumptions (a discrete K-tick price grid, only two patience types; the paper shows its baseline results survive relaxing the assumption that buyers and sellers strictly alternate). Several predictions, including the intraday decline in limit-order aggressiveness, are explicitly flagged by the authors as untested against real data at the time of writing.

## Who it is for

Quant researchers and advanced traders interested in why bid-ask spreads widen after order flow shocks and how tick size and order-arrival intensity affect market resiliency.
