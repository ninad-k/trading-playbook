---
author: Marek Rutkowski
category: Options, Futures & Derivatives
difficulty: advanced
doc_type: paper
one_liner: Lecture-note derivation of no-arbitrage option pricing via replicating
  portfolios and martingale measures, from a one-period binomial model up through
  futures markets.
pages: 19
related:
- interest-rate-models
- the-mathematics-of-financial-modeling-and-investment-management
- black-scholes-option-pricing-model
reviewed_pdf_pages: 2-3, 10 (the binomial worked example and the replication argument)
slug: introduction-to-arbitrage-pricing-of-financial-derivatives
source_file: INTRODUCTION TO ARBITRAGE PRICING OF FINANCIAL DERIVATIVES.pdf
source_review: partial
tags:
- arbitrage-pricing
- options
- binomial-model
- martingale
- risk-neutral-valuation
- replicating-portfolio
- academic-reference
tier: B
title: Introduction to Arbitrage Pricing of Financial Derivatives
year: 1997
---

## Summary

A lecture-note style excerpt (based on Musiela and Rutkowski's "Martingale Methods in Financial Modelling") that builds the theory of arbitrage-free option pricing from first principles. It starts with call and put payoff definitions and put-call parity, then works a fully worked one-period binomial example (a $280 stock that can move to $320 or $260) to show that a European call's fair price is determined not by subjective probability assumptions but by constructing a replicating portfolio of stock and cash. It then formalizes this using risk-neutral (martingale) probability measures, proves the risk-neutral valuation formula, and extends the same machinery from spot markets to futures markets, ending with multi-period pricing.

## Key points

- Frictionless-market assumptions throughout: no transaction costs, unlimited borrowing/lending at equal rates, perfectly divisible assets, full use of short-sale proceeds.
- A European option's payoff depends only on the terminal stock price; the worked example gives a call payoff of $40 up / $0 down for a $280 strike.
- "Expected discounted payoff" under a trader's subjective probability isn't a reliable price — it shifts with a bull vs. bear view, which is why replication is needed instead.
- A unique arbitrage-free price comes from a portfolio of stock and a risk-free bond that exactly replicates the option's payoff in both states.
- The risk-neutral (martingale) measure P* is a mathematical tool, not a claim real-world investors are risk-neutral — it exists precisely when the discounted stock price process has no arbitrage.
- The same logic extends to pricing derivatives on futures contracts with a modified martingale measure for the futures price.
- Put-call parity falls directly out of the algebraic relationship between call and put payoffs.

## Actionable rules

None given in trading terms — this is a pure derivatives-pricing theory text. Its practical relevance for a trader: the replicating-portfolio logic is the theoretical basis for options market-making, delta hedging, and understanding why an option's "fair value" does not depend on your own market view.

## Caveats

Written at an advanced mathematical level (measure-theoretic probability, martingale theory) drawn from a graduate textbook chapter, not aimed at practitioners looking for trading rules. Only European-style options and idealized frictionless markets are treated in the parts reviewed; American option pricing is explicitly noted in the text as lacking closed-form solutions even under Black-Scholes assumptions.

## Who it is for

Quants, derivatives traders, and finance graduate students who want a rigorous, step-by-step derivation of why arbitrage-free option pricing works, starting from a simple two-state example before generalizing to full martingale pricing theory.
