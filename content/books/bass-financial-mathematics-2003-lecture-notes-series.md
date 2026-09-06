---
author: Richard F. Bass
category: Quant, Microstructure & Academic Research
difficulty: advanced
doc_type: paper
one_liner: 'A graduate math course deriving option pricing from first principles:
  probability, binomial trees, Brownian motion, Ito calculus, and the Black-Scholes
  formula.'
pages: 70
related:
- black-scholes-option-pricing-model
- hull-options-futures-and-other-derivative-securities-5th-ed
- back-to-basics-historical-option-pricing-revisited
- fi-lecture16-exotic-options-credit-derivatives
reviewed_pdf_pages: the derivation sections checked against the note; the notes are
  algebraic rather than numeric
slug: bass-financial-mathematics-2003-lecture-notes-series
source_file: Bass_Financial Mathematics (2003)(Lecture Notes Series).pdf
source_review: partial
tags:
- option-pricing
- black-scholes
- binomial-model
- stochastic-calculus
- martingales
- arbitrage
- term-structure
tier: B
title: Financial Mathematics (Lecture Notes)
year: 2003
---

## Summary

University of Connecticut lecture notes (Spring 2003) for a graduate course in mathematical finance. Question addressed: how should a European option be priced today given uncertain future stock movement? Method: build up the mathematics rigorously — measure-theoretic probability, conditional expectation, martingales — then apply it first to the one-step and multi-step binomial asset-pricing model, and finally to the continuous-time model (Brownian motion, stochastic integrals, Ito's formula, Girsanov's theorem) to derive the Black-Scholes formula. Finding: option price is pinned down uniquely by a no-arbitrage replication argument, not by predicting whether the stock will rise or fall — the price depends on volatility but is independent of the stock's expected return (drift).

## Key points

- The no-arbitrage principle ("no free lunch") is the single engine driving every pricing result in the notes: if two portfolios have identical payoffs, they must have the same price today, or a riskless profit is possible.
- In the one-step binomial model, a replicating portfolio of Δ shares of stock plus a bond position exactly reproduces an option's payoff; the option's fair value is the cost of building that portfolio, independent of the real-world up/down probabilities.
- The multi-step binomial model extends this by backward induction through the tree; American options add early-exercise decisions at each node.
- Under the risk-neutral measure, the discounted stock price is a martingale — the mathematical device that makes "fair pricing" tractable.
- Continuous-time results (Brownian motion, Ito's formula, stochastic differential equations) are the tools used to move from the discrete binomial tree to a continuous stock-price model (geometric Brownian motion).
- The Black-Scholes formula for a European call, W0 = xΦ(g) − Ke^(−rt)Φ(h), falls out of the martingale-representation and risk-neutral-pricing machinery; the formula depends on volatility σ but not on the stock's expected drift μ.
- Later sections extend the framework to American puts, term-structure (interest rate) models, foreign exchange options, and options on dividend-paying stocks.

## Actionable rules

None given — this is a theoretical derivation, not a trading rulebook. The practical takeaways for a trader: (1) an option's "fair" price is anchored to volatility and the risk-free rate, not to a view on which direction the underlying will move; (2) hedging (delta-replication) is the mechanism markets use to keep option prices arbitrage-free, which is why implied volatility, not directional forecasts, is the primary lever option traders quote and trade.

## Caveats

This is dense graduate-level mathematics (measure theory, stochastic calculus) with no discussion of real-world frictions — transaction costs, discrete hedging, bid-ask spreads, or the volatility smile that violates the model's constant-volatility assumption. It is a derivation of the theoretical foundation underlying options pricing, not a practitioner's guide; readers wanting applied option strategy or risk management should look elsewhere in this library.

## Who it is for

Quantitatively trained readers (or those willing to work through it) who want to understand the mathematical derivation behind Black-Scholes and binomial option pricing, rather than just the resulting formulas.
