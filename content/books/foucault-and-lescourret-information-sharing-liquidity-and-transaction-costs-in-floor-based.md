---
title: "Information Sharing, Liquidity and Transaction Costs in Floor-Based Trading Systems"
author: "Thierry Foucault and Laurence Lescourret"
year: 2001
slug: foucault-and-lescourret-information-sharing-liquidity-and-transaction-costs-in-floor-based
tier: B
category: "Quant, Microstructure & Academic Research"
tags: [market-microstructure, floor-trading, information-sharing, liquidity, bid-ask-spread, academic-paper]
difficulty: advanced
doc_type: paper
pages: 43
one_liner: "Theoretical model of floor brokers pooling fundamental and order-flow information, showing it improves price discovery and cuts liquidity traders' costs but can raise or lower market depth."
related: [madhavan-market-microstructure-a-survey, liquidity-in-forex-markets, hartmann-manna-and-manzanares-the-microstructure-of-the-euro-money-market]
source_file: "Foucault And Lescourret-Information Sharing, Liquidity And Transaction Costs In Floor-Based Tradi.pdf"
---

## Summary

Question: does information sharing between two floor brokers with different information types (one holding fundamental/payoff information on a security, the other holding information about incoming liquidity/order flow) help or hurt floor-based markets? Method: a theoretical microstructure model (in the tradition of Kyle 1985) in which "dual-capacity" floor brokers can pool private information before trading against a competitive market maker and other, non-informed speculators. Finding: under identifiable parameter conditions, the two informed brokers are jointly better off sharing information; when they do, price discovery improves, return volatility falls, and the aggregate expected trading costs borne by liquidity traders decrease — but the effect on quoted market depth and bid-ask spreads is ambiguous (it can go either way depending on parameter values).

## Key points

- Floor-based markets (NYSE, Frankfurt, AMEX, CBOT/CBOE-style open outcry) allow person-to-person contact that lets brokers share information — something anonymous electronic limit-order systems cannot easily replicate.
- Two types of floor information sharing are distinguished: (1) floor brokers with market-makers (mitigates adverse selection, per Benveniste, Marcus & Wilhelm 1992) and (2) floor brokers with other floor brokers (the paper's focus).
- The model separates "fundamental" speculators (who know the security's payoff) from a broker who instead observes non-fundamental information (client order flow / liquidity demand).
- When information sharing occurs, it increases competition among the counterparties serving the informed broker's clients, so a smaller share of that broker's client orders must be executed against the market maker.
- Proposition: expected trading costs borne by liquidity traders overall are always lower when the two brokers share information versus when they do not.
- Because the trading game is zero-sum, the aggregate reduction in liquidity traders' costs and the increase in the two sharing speculators' profits come at the expense of the other (non-sharing) speculators in the market.
- With only a single fundamental speculator (N=1), there is no parameter combination under which information sharing is optimal for the two brokers — sharing requires competition among multiple fundamental speculators to make sense.
- Information sharing makes prices more informative and less volatile, and its effect on the bid-ask spread and quoted depth depends on the relative variance of fundamental versus liquidity-driven order flow.

## Actionable rules

None given — this is a theoretical market-microstructure model, not a trading system. What a trader/market participant can take from it: floor/pit-style markets with informal broker-to-broker information sharing can produce tighter effective trading costs for liquidity-driven orders than a naive comparison of quoted spreads alone would suggest, and that advantage is a structural feature of person-to-person floor trading that anonymous electronic order books do not automatically replicate.

## Caveats

Purely theoretical/mathematical (a Kyle-style linear-equilibrium model) with no empirical dataset — conclusions are model-dependent and the appendix proofs use notation that OCRs with garbled symbols in places. The paper is explicitly about floor-based/open-outcry markets, which have been largely displaced by electronic trading since it was written (2001); its practical relevance today is mainly historical/academic. The authors themselves flag that whether floor-sharing benefits outweigh floor trading's other costs (higher operating costs, less transparency) is left for future research.

## Who it is for

Readers interested in market microstructure theory — why floor/pit markets historically retained an edge in certain conditions, and how information sharing among market participants affects price discovery, volatility, and liquidity costs. Not for traders looking for an executable strategy.
