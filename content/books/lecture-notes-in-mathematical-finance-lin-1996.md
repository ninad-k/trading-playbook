---
author: X. Sheldon Lin
category: Quant, Microstructure & Academic Research
difficulty: advanced
doc_type: course
one_liner: University graduate-course lecture notes building arbitrage-free asset
  pricing from discrete one-period models up through Ito calculus, Black-Scholes-style
  dynamic hedging, and interest-rate/swap models.
pages: 339
related:
- derivatives-pricing-and-financial-modelling
- introduction-to-arbitrage-pricing-of-financial-derivatives
- 1-the-mathematics-of-financial-derivatives
- black-scholes-option-pricing-model
- hull-options-futures-and-other-derivative-securities-5th-ed
- paul-wilmott-quantitative-finance
reviewed_pdf_pages: the derivation chapters checked against the note; the notes are
  algebraic and state no trading parameters
slug: lecture-notes-in-mathematical-finance-lin-1996
source_file: Lecture Notes In Mathematical Finance (Lin_1996).pdf
source_review: partial
tags:
- arbitrage-pricing
- stochastic-calculus
- option-pricing
- interest-rate-models
- risk-neutral-valuation
- academic-research
tier: B
title: Lecture Notes in Mathematical Finance
year: 1996
---

## Summary

A university lecture-note course (Department of Statistics & Actuarial Science, University of Iowa) building the mathematics of no-arbitrage asset pricing from the ground up in two parts. Part I covers discrete-time finance: one-period market models, trading strategies, no-arbitrage characterization, risk-neutral valuation, discrete-time stochastic processes, lattice/binomial models, and binomial option and interest-rate pricing. Part II covers continuous-time finance: stochastic calculus (Wiener processes, the Ito integral, stochastic differential equations, Ito's lemma, the Feynman-Kac formula, Girsanov's theorem), the dynamic-hedging approach to option pricing, multi-dimensional Ito processes, security-market valuation, digital and barrier options, interest-rate models, and swaps/swaptions, with probability-theory and functional-analysis appendices.

## Key points

- **One-period market model** — a finite state space of possible outcomes, a set of primitive securities with known payoffs in each state, and investor endowments; a "trading strategy" is a portfolio of these securities.
- **No-arbitrage condition** — the foundational assumption throughout the notes: no trading strategy can produce a sure profit with zero net cost; this alone restricts the set of valid prices.
- **Market completeness** — a market is complete if every possible payoff can be replicated by some portfolio of the primitive securities (equivalent to the payoff matrix having full rank); incomplete markets require creating new (derivative) securities to complete them.
- **Risk-neutral probability measure** — under no-arbitrage, there exists a probability measure under which discounted asset prices are martingales; pricing any claim reduces to computing its expected discounted payoff under this measure rather than the real-world probability.
- **Binomial models** — the discrete-time workhorse for pricing options and interest-rate derivatives by building a lattice (tree) of up/down price moves and applying risk-neutral valuation at each node.
- **Ito calculus** — the continuous-time toolkit (Wiener process, Ito integral, Ito's lemma, stochastic differential equations) needed to model continuously-evolving asset prices and derive pricing PDEs.
- **Dynamic hedging / Black-Scholes-style approach** — options are priced by constructing a continuously-rebalanced replicating portfolio in the underlying and a risk-free bond; the same risk-neutral valuation logic from the discrete case reappears via Girsanov's theorem (which formalizes the change from the real-world to the risk-neutral measure).
- **Feynman-Kac formula** — connects the price of a derivative (an expectation under the risk-neutral measure) to the solution of a partial differential equation, the bridge between the probabilistic and PDE approaches to option pricing.
- **Interest-rate models and swaps** — the later chapters extend the same no-arbitrage/risk-neutral machinery to term-structure (interest-rate) models and to pricing swaps and swaptions, plus digital and barrier options as examples of exotic payoffs.

## Actionable rules

None given — this is graduate coursework in the mathematics of arbitrage-free pricing, not a trading system. The conceptual takeaway a trader can use: any consistent options or derivatives price must be expressible as a discounted expectation under some risk-neutral measure; the binomial-tree logic in Part I is the intuitive version of the continuous-time Black-Scholes machinery in Part II.

## Caveats

The source PDF's text layer has systematic ligature-stripping corruption (common character pairs like "ti," "tt," "fi" are dropped or mis-spaced throughout, e.g., "securit y," "Sto c hastic"), which degrades readability of the fine mathematical notation and equations; the table of contents and prose outline used here were reconstructed from the recoverable text and are reliable, but exact formulas and worked numerical examples could not be verified in detail. This is dense, prerequisite-heavy graduate material (real analysis, probability theory, stochastic calculus) with no discussion of practical trading, market frictions, or transaction costs; content predates most 2000s-era volatility-modeling and credit-derivatives developments.

## Who it is for

Graduate students or quant practitioners who want a compact, rigorous course build-up of arbitrage pricing theory from discrete one-period models through continuous-time stochastic calculus and interest-rate derivatives; not intended for discretionary or retail traders.
