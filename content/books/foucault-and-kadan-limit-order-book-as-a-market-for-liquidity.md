---
title: "Limit Order Book as a Market for Liquidity"
author: "Thierry Foucault, Ohad Kadan, Eugene Kandel"
year: 2001
slug: foucault-and-kadan-limit-order-book-as-a-market-for-liquidity
tier: B
category: Quant, Microstructure & Academic Research
tags: [market-microstructure, limit-order-book, liquidity, tick-size, bid-ask-spread, academic]
difficulty: advanced
doc_type: paper
pages: 59
one_liner: "A dynamic microstructure model showing how the mix of patient vs. impatient traders, tick size, and order arrival rate jointly determine spreads and limit-order execution time."
related: [foucault-kadan-and-kandel-limit-order-book-as-a-market-for-liquidity, chordia-roll-and-subrahmanyam-market-liquidity-and-trading-activity, hollifield-miller-sandas-and-slive-liquidity-supply-and-demand-in-limit-order-markets, parlour-and-seppi-liquidity-based-competition-for-order-flow, credit-derivatives]
source_file: "Foucault And Kadan-Limit Order Book As A Market For Liquidity.pdf"
---

## Summary

This CEPR working paper (July 2001) by Foucault, Kadan, and Kandel asks: in a pure order-driven market with no designated market-maker, how do trader impatience, tick size, and order arrival rate jointly determine bid-ask spreads and the time it takes a limit order to execute? The model has liquidity traders arriving sequentially, each forced to buy or sell one unit, choosing between an immediate market order or a price-improving limit order that trades off a better price against a waiting cost. Traders differ only in how costly waiting is to them (patient vs. impatient), and the paper solves for the equilibrium mix of order types this population produces. The main finding is that the ratio of patient to impatient traders is the central driver of book dynamics: a higher proportion of patient traders means fiercer competition among liquidity suppliers, more aggressive (tighter) quoting to shorten wait times, and a spread distribution skewed toward small spreads — while several comparative-statics results run counter to naive intuition (e.g., a smaller tick size can widen average spreads, and slower order arrival can narrow them).

## Key points

- Model setup: buyers and sellers arrive one at a time and must trade; each chooses a "j-limit order" (j = 0 is a market order, j > 0 improves the price by j ticks but delays execution) to maximize expected profit net of a waiting cost that is linear in expected time-to-execution.
- Traders split into two types by waiting cost: patient (low cost, natural liquidity suppliers) and impatient (high cost, natural liquidity demanders); the population proportion of each is a key model parameter.
- Three distinct equilibrium types emerge depending on (i) the patient traders' relative impatience, (ii) the proportion of patient to impatient traders, and (iii) the tick size.
- A larger proportion of patient traders intensifies competition among liquidity suppliers, shortens expected time-to-execution, and skews the spread distribution toward smaller spreads.
- Traders frequently find it optimal to undercut or outbid the best quote by more than one tick — more likely when patient traders are relatively numerous, waiting costs are high, or tick size is small.
- Counterintuitive result: a smaller tick size can widen average spreads, because it lets liquidity suppliers post less competitive prices when competition among them is weak (more price points to hide behind).
- Counterintuitive result: a slower order arrival rate can narrow average spreads — slower arrivals lengthen expected time-to-execution, which pushes liquidity suppliers to quote more aggressively when the spread is wide.
- Extends the base model to include a designated market-maker/liquidity provider (as required on some exchanges, e.g., the Paris Bourse for small/mid-cap stocks) and shows this intervention forces patient traders to quote more aggressively, narrowing spreads — a rationale for market-maker obligations in less liquid names.
- Model predictions are consistent with prior empirical findings that expected limit-order time-to-execution increases with the distance between the limit price and the mid-quote (cited against Lo, MacKinlay, and Zhang's econometric estimates).

## Actionable rules

None given as trading rules — this is a theoretical microstructure model, not a trading strategy. What a practitioner can take from it: (1) expect tighter, more competitive spreads in names/venues with a higher proportion of patient (institutional, long-horizon) participants; (2) don't assume a smaller minimum tick automatically narrows spreads — it can widen them if liquidity competition is weak; (3) in illiquid names, a designated market-maker/liquidity-provider obligation should be expected to compress spreads by forcing more aggressive quoting from other liquidity suppliers.

## Caveats

Highly stylized theoretical model (discrete time, single security, exogenously fixed price bounds A and B, traders who must trade with no outside option) built for analytical tractability, not a description of any specific real market's exact mechanics — its value is in the comparative-statics intuition (tick size, patience mix, arrival rate effects on spreads), not literal numeric predictions. Academic working-paper prose with dense notation; requires comfort with basic game-theoretic/equilibrium reasoning. This working-paper (CEPR) version may differ in detail from the paper's eventual published Review of Financial Studies version by the same three authors.

## Who it is for

Market microstructure researchers, quant traders, or exchange/market-design practitioners who want a rigorous model of how trader impatience and tick size shape limit order book dynamics — not for traders seeking discretionary or systematic entry/exit rules.
