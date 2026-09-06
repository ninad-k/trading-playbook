---
author: David G. Luenberger
category: Quant, Microstructure & Academic Research
difficulty: advanced
doc_type: book
one_liner: A mathematical survey connecting present value, portfolio choice, equilibrium
  pricing, hedging, and derivatives.
pages: 510
related:
- fixed-income-securities
- derivatives-pricing-and-financial-modelling
reviewed_pdf_pages: 3-13, 37, 62, 87, 112, 137, 162, 187, 212, 237, 262, 286, 311,
  336, 361, 386, 411, 436, 461, 486 (every page the scan yields text for; the remaining
  pages are image-only)
slug: investment-science
source_file: Investment science.pdf
source_review: partial
tags:
- investment-analysis
- fixed-income
- portfolio-theory
- derivatives
- mathematical-finance
tier: B
title: Investment Science
year: 1998
---

## Summary

David G. Luenberger presents investment analysis as a sequence of reusable mathematical principles. The contents begin with deterministic cash flows, interest, fixed-income valuation, duration, immunization, and the term structure. They then move to mean-variance portfolios, CAPM, factor and arbitrage-pricing models, utility and risk-neutral pricing, followed by forwards, futures, swaps, asset dynamics, options, and more general investment problems (pp. 7-10).

The emphasis is on deriving practical solutions from a small set of ideas rather than cataloging products. The book assumes comfort with mathematical deduction roughly at an undergraduate engineering, mathematics, or science level, while requiring only elementary portions of calculus (pp. 11-13). Sampled chapters show how the same discipline links portfolio construction, no-arbitrage valuation, and contingent claims.

## Key points

- The organization progresses from present-value arithmetic to uncertainty, equilibrium, and derivatives (pp. 7-10).
- Mean-variance analysis frames portfolio choice through expected return, covariance, feasible sets, and efficient portfolios (pp. 8, 187).
- CAPM is presented both as an equilibrium model and as a basis for performance evaluation and project choice (pp. 8-9).
- Log-optimal pricing expresses a security's price through its payoff and the return on the log-optimal portfolio (p. 262).
- Forward pricing follows from a replicating cash-flow argument and the exclusion of arbitrage (p. 286).
- Option valuation uses risk-neutral expected cash flows and backward recursion; options can reduce or amplify portfolio risk depending on use (p. 361).
- **Present value as an equivalent single payment** — a cash-flow stream's present value is defined as the payment today that is equivalent to the whole stream, with future value its mirror image (p. 37).
- **Immunization is only local** — a duration-matched bond portfolio is immunised against parallel shifts in the spot-rate curve, and the text is explicit that other procedures are needed for non-parallel moves (p. 112).
- **Asian options** — Chapter 13 covers averaging options in two forms: the average price used as the strike, giving a payoff of max(S_T − S_avg, 0), and the average substituted for the final price, giving max(S_avg − K, 0) (p. 386).
- **Optimal growth** — Chapter 15 develops log-optimal (growth-optimal) portfolios by taking logarithms of the compounded wealth relative, so that maximising expected log return maximises long-run growth (p. 436).
- **General multiperiod valuation** — Chapter 16 shows that a security's price equals the discounted risk-neutral expected value of all its future cash flows, generalised to any number of underlying assets (pp. 461, 486).

## Actionable rules

1. Match the model to the cash-flow problem: discount deterministic streams first, then introduce covariance, utility, or contingent-claim machinery only when uncertainty requires it (pp. 7-10).
2. When testing a forward price, construct the spot purchase, financing, carrying costs, and delivery cash flows. A zero-cost strategy with a certain positive terminal payoff exposes an inconsistent price, subject to the ability to short and borrow (p. 286).
3. Price a European option in a lattice by taking its terminal payoff under risk-neutral probabilities, discounting at the risk-free rate, and working backward node by node (p. 361).

## Caveats

This note is based on every page the 510-page scan yields extractable text for — roughly 28 sampled pages. The scan is image-only elsewhere, so intervening derivations could not be read. Exercises and many derivations were not reviewed continuously. The models rely on assumptions such as frictionless trading, available financing, and specified return dynamics; they are analytical tools rather than direct trading signals.

## Who it is for

Technically trained readers seeking a unified foundation for portfolio analysis, fixed income, and derivatives.
