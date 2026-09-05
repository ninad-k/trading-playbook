---
title: The Basics of Financial Mathematics
author: Richard F. Bass
year: 2003
slug: bass-the-basics-of-financial-mathematics
tier: B
category: Quant, Microstructure & Academic Research
tags: [options-pricing, black-scholes, binomial-model, brownian-motion, martingales, stochastic-calculus, risk-neutral-pricing]
difficulty: advanced
doc_type: course
pages: 105
one_liner: "University lecture notes deriving option pricing rigorously: elementary probability, the binomial asset pricing model, Brownian motion/stochastic calculus, and the Black-Scholes formula via the risk-neutral measure."
related: [black-scholes-option-pricing-model]
source_file: "Bass - The Basics of Financial Mathematics.pdf"
---

## Summary

These are University of Connecticut course notes (Spring 2003) by mathematician Richard Bass, teaching the mathematics behind derivatives pricing rather than any trading strategy. The question addressed throughout: given a model of how a stock price moves, what is the fair (arbitrage-free) price of an option on it, and how does one replicate/hedge it? The notes build up in stages: elementary probability (sigma-fields, conditional expectation, martingales), the discrete-time binomial asset-pricing model (one-step, multi-step, American options), continuous-time tools (Brownian motion, stochastic integrals, Ito's formula, Girsanov's theorem), the continuous-time model culminating in Black-Scholes and the Fundamental Theorem of Asset Pricing, and finally term-structure/interest-rate models. The finding repeated in both settings: under "no arbitrage," a risk-neutral probability measure exists under which the discounted asset price is a martingale, and any option's price equals its expected payoff under that measure.

## Key points

- One-step binomial model: with up-factor u, down-factor d, and risk-free rate r, the no-arbitrage option price is V0 = [1/(1+r)] × E[V1] under risk-neutral probabilities p = (1+r-d)/(u-d) and q = (u-1-r)/(u-d) — not the real-world up/down probabilities.
- Hedge ratio (delta): Δ0 = (V1^u − V1^d)/(uS0 − dS0), i.e., replicate the option's payoff by holding Δ0 shares plus a bank position.
- Multi-step binomial model: under the risk-neutral measure, the discounted stock price (1+r)^(-k)S_k is a martingale, generalizing the one-step result to any number of steps.
- Continuous-time model (geometric Brownian motion, drift removed via Girsanov's theorem) yields the closed-form Black-Scholes formula: W0 = xΦ(g) − Ke^(−rT)Φ(h), with g = [ln(x/K) + (r+σ²/2)T]/(σ√T) and h = g − σ√T.
- Key qualitative result: the Black-Scholes price depends on volatility σ but is completely independent of the stock's real-world expected return μ.
- Fundamental Theorem of Finance: a market is arbitrage-free iff a probability measure exists under which discounted asset prices are martingales; it is "complete" if every payoff can be replicated by trading the underlying and the bank account.
- Later sections extend the framework to American options, martingale representation, explicit hedging strategies, and term-structure/interest-rate models.

## Actionable rules

None given as trading rules. This is a pure derivation of pricing theory, not a strategy manual — its "rules" are mathematical (the u/d/p/q and delta-hedging formulas and the Black-Scholes closed form above), not entry/exit/sizing rules a trader would apply directly.

## Caveats

This is graduate-level applied mathematics (measure-theoretic probability, stochastic calculus), not a practitioner guide — it assumes calculus/probability background and offers no worked numerical trading examples or market-data calibration. All models assume frictionless markets (no transaction costs, unlimited borrowing/short-selling), which the notes themselves flag as unrealistic. It is a foundational-theory reference for why option-pricing formulas take the form they do, not for building a trading system.

## Who it is for

Quantitative traders, derivatives desk analysts, and finance students who want the rigorous mathematical derivation behind binomial option pricing and the Black-Scholes formula, as a foundation before or alongside practitioner texts like Hull.
