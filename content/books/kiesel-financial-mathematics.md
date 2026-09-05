---
title: "Financial Mathematics"
author: "Rüdiger Kiesel"
year: unknown
slug: kiesel-financial-mathematics
tier: B
category: "Quant, Microstructure & Academic Research"
tags: [arbitrage-theory, derivative-pricing, black-scholes, stochastic-calculus, interest-rate-models, martingale-pricing]
difficulty: advanced
doc_type: course
pages: 142
one_liner: "Graduate-level lecture notes deriving derivative pricing from first principles: arbitrage theory, single- and multi-period market models, Black-Scholes, and interest-rate/HJM models."
related: [bass-financial-mathematics-2003-lecture-notes-series, bass-the-basics-of-financial-mathematics, paul-wilmott-quantitative-finance, hull-options-futures-and-other-derivative-securities-5th-ed, back-to-basics-historical-option-pricing-revisited]
source_file: "Kiesel_ Financial mathematics.pdf"
---

## Summary

A set of graduate/masters-level lecture notes in mathematical finance, building derivative pricing theory from the ground up in four parts: (1) arbitrage theory and single-period market models, (2) financial market theory (expected utility, risk aversion, mean-variance portfolios, CAPM), (3) discrete- and continuous-time pricing models culminating in the Cox-Ross-Rubinstein binomial model and Black-Scholes, and (4) interest-rate theory (term structure, short-rate models, Heath-Jarrow-Morton). Appendices cover the probability and measure-theory background (martingales, filtrations, Radon-Nikodym derivatives) needed to follow the main text rigorously.

## Key points

- **No-arbitrage principle** — the foundation of the entire text: derivative prices are pinned down by the requirement that no risk-free profit be extractable from a combination of the derivative and its underlying.
- **Single-period market model** — the simplest setting for introducing risk-neutral (equivalent martingale) pricing before generalizing to multiple periods.
- **Equivalent martingale measure** — a reweighted probability measure under which discounted asset prices are martingales; its existence is equivalent to no-arbitrage, and its uniqueness is equivalent to market completeness.
- **Cox-Ross-Rubinstein (CRR) binomial model** — a discrete-time model with an explicit up/down price tree, used to derive risk-neutral pricing and hedging mechanically before taking the continuous-time limit.
- **Itô's Lemma and Girsanov's Theorem** — the stochastic-calculus tools used to move from discrete to continuous-time models and to change from the real-world to the risk-neutral measure.
- **Black-Scholes model and the Greeks** — derived as the continuous-time limit of the binomial model; the notes also cover barrier options as an extension.
- **American options** — treated via optional stopping theory and Snell envelopes, i.e., finding the optimal early-exercise policy.
- **Term structure / short-rate models and Heath-Jarrow-Morton (HJM)** — the interest-rate analogue of equity option pricing, covering bond pricing, the term-structure equation, and pricing of swaps and caps.

## Actionable rules

None given — this is pure theory/derivation, not a trading system. Its practical relevance to a trader is foundational: it explains why standard option-pricing and hedging formulas (Black-Scholes deltas, risk-neutral valuation) take the form they do, and under what assumptions (completeness, no-arbitrage, continuous trading) they break down.

## Caveats

Requires graduate-level mathematical background (measure-theoretic probability, stochastic calculus, functional analysis) — not accessible without prior coursework in real analysis and probability theory. As lecture notes rather than a published book, exposition is compressed and proof-heavy with few worked numerical trading examples. No date/edition is given in the extracted text, so currency of references cannot be assessed.

## Who it is for

Graduate students or quantitatively-trained readers who want the rigorous mathematical derivation behind derivative pricing formulas, not practitioners looking for trading rules or intuition-first explanations.
