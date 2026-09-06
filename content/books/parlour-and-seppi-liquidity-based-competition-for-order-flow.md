---
author: Christine A. Parlour, Duane J. Seppi
category: Quant, Microstructure & Academic Research
difficulty: advanced
doc_type: paper
one_liner: Theoretical model of exchange competition showing that neither a pure limit-order
  market nor a hybrid specialist/limit-order market is inherently 'competition-proof'
  for order flow.
pages: 43
related:
- exchange-rules-for-the-frankfurt-stock-exchange
- madhavan-market-microstructure-a-survey
- foucault-kadan-and-kandel-limit-order-book-as-a-market-for-liquidity
- chordia-roll-and-subrahmanyam-market-liquidity-and-trading-activity
- hollifield-miller-sandas-and-slive-liquidity-supply-and-demand-in-limit-order-markets
reviewed_pdf_pages: the model and results sections checked against the note; the paper
  is analytical rather than numeric
slug: parlour-and-seppi-liquidity-based-competition-for-order-flow
source_file: Parlour And Seppi-Liquidity-Based Competition For Order Flow.pdf
source_review: partial
tags:
- market-microstructure
- limit-order-book
- liquidity
- order-preferencing
- specialist-market
- academic-paper
tier: B
title: Liquidity-Based Competition for Order Flow
year: 2003
---

## Summary

Question: when two exchanges compete for the same order flow — a pure limit order market (PLM, like the Paris Bourse or an ECN) versus a hybrid market with both a specialist and a limit book (HM, like the NYSE) — can one market structure dominate and drive the other out, or can both structures coexist? Method: a theoretical, single-period microstructure model (Review of Financial Studies, 2003) in which competitive value traders post limit orders on both exchanges, a passive dealer "crowd" adds liquidity above a cost hurdle, a strategic specialist provides ex post price improvement only in the hybrid market, and an active trader with random order size splits her market order across the two venues to minimize total trading cost. No historical price/volume dataset is used — the paper is entirely analytical/proof-based, with all proofs in an appendix.

## Key points

- Neither the pure limit order market nor the hybrid market is exclusively "competition-proof": multiple equilibria exist depending on liquidity providers' cost heterogeneity, and in some equilibria the hybrid market can actually dominate the pure market.
- "Order preferencing" — the tie-breaking rule used when an order is cost-indifferent between the two venues — is a key determinant of which market structure wins; this validates real-world concerns (e.g., Nasdaq dealer order-direction practices, NYSE regional order routing) that preferencing rules are not neutral.
- Competing exchanges can either increase or decrease aggregate liquidity relative to a single consolidated market, depending on parameters — there is no universal answer that fragmentation is good or bad for liquidity.
- "Best execution" rules that cap the allowable price difference between markets to one tick substantially improve the hybrid market's competitive viability relative to a pure limit order market.
- Limit orders represent ex ante commitments to supply liquidity to future market orders, while a specialist supplies liquidity ex post (after seeing the incoming order) — this timing asymmetry drives most of the paper's results.
- In the hybrid market, the specialist can only trade himself by undercutting both the resting limit book and the dealer crowd (public priority), which limits how much a specialist can capture from order flow.

## Actionable rules

For a trader: this paper offers no entry/exit system. What it implies for practice is that (1) where an instrument is dual/multi-listed or tradable on both a limit-order venue and a hybrid/dealer venue, expected execution quality can depend heavily on order-routing and preferencing rules the trader does not control, so checking a broker's order-routing/best-execution policy matters for cost; (2) posting a limit order on a fragmented market carries a form of "adverse selection" risk from strategic order-splitting by informed/large traders across venues, which the model formalizes as a reason resting limit orders can be thinner than in a single consolidated market.

## Caveats

This is a graduate-level theoretical finance paper full of formal notation (probability distributions, break-even conditions, recursive equilibrium equations) and has no empirical dataset, backtest, or trading signal — it is included here as background on market microstructure and exchange competition, not as source material for a trading rule. Understanding it requires familiarity with market-maker/specialist economics and equilibrium modeling.

## Who it is for

Quant researchers, market-structure analysts, or advanced students who want a rigorous theoretical treatment of why competing trading venues can coexist and how order-routing/preferencing rules affect liquidity — not a fit for traders looking for actionable setups.
