---
title: "Black-Scholes Option Pricing Model"
author: Nathan Coelen
year: 2002
slug: black-scholes-option-pricing-model
tier: B
category: Options, Futures & Derivatives
tags: [options-pricing, black-scholes, stochastic-calculus, brownian-motion, derivatives, academic-paper]
difficulty: advanced
doc_type: paper
pages: 19
one_liner: "A step-by-step mathematical derivation of the Black-Scholes PDE and its closed-form solution for a European call option."
related: [introduction-to-arbitrage-pricing-of-financial-derivatives, the-mathematics-of-financial-modeling-and-investment-management]
source_file: "Black-Scholes Option Pricing Model.pdf"
---

## Summary

**Question:** how can a European call option be priced consistently using no-arbitrage arguments? **Method:** the paper builds up the theory piece by piece — arbitrage pricing, hedging and delta, a geometric Brownian motion model for stock prices, Itô calculus (Itô's formula, quadratic variation), then constructs a riskless hedged portfolio (long the option, short ∂V/∂S shares) whose return must equal the risk-free rate. **Finding:** this no-arbitrage condition yields the Black-Scholes PDE, which, solved with the boundary condition C(S,T) = max(S−E, 0) for a European call, gives the closed-form Black-Scholes formula.

## Key points

- Arbitrage pricing theory: two identical assets cannot sell at different prices; any price discrepancy is arbitraged away instantaneously.
- Delta (Δ = ∂V/∂S) measures the option's price sensitivity to the underlying; delta hedging offsets an option position with a proportional stock position.
- Stock price model: dS/S = μdt + σdB, i.e., a deterministic drift (μ) plus a random Brownian-motion term (σdB) — geometric Brownian motion.
- Brownian motion properties used: normal increments, independence of increments, continuous but nowhere-differentiable paths, and quadratic variation equal to t.
- Itô's formula is the stochastic-calculus analogue of the chain rule; it's the key tool for finding dV(S,t) when S follows a stochastic process.
- The hedged portfolio π = V − S·(∂V/∂S) is riskless (no dB term), so dπ = rπdt by no-arbitrage — this substitution produces the Black-Scholes PDE: ∂V/∂t + ½σ²S²∂²V/∂S² + rS∂V/∂S − rV = 0.
- Final formula for a European call: C(S,t) = S·N(d1) − E·e^(−r(T−t))·N(d2), with d1 = [ln(S/E) + (r + ½σ²)(T−t)] / (σ√(T−t)) and d2 = d1 − σ√(T−t).

## Actionable rules

None given — this is a mathematical derivation, not a trading system. Practical takeaway for traders: the five inputs that determine an option's theoretical fair value are the underlying price (S), strike (E), time to expiry (T−t), risk-free rate (r), and volatility (σ) — of which volatility is the only unobservable, making it the key variable options traders estimate and trade around (implied volatility).

## Caveats

Assumes constant volatility and risk-free rate, continuous trading with no transaction costs, log-normal stock price distribution, and no dividends — all of which are known to break down in real markets (volatility smiles/skew, jumps, transaction costs). The paper is a derivation exercise, not a market-tested implementation guide.

## Who it is for

Traders and students who want to understand the mathematical foundation of options pricing (the "why" behind the Black-Scholes formula) rather than just how to plug numbers into a calculator.
