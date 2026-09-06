# Derivatives Pricing and Financial Modelling: Tutorial 10: the trader's summary

*An unsolved tutorial connecting short-rate models, HJM dynamics, bond-option pricing and coupon-bond volatility.*

**Andrew Cairns** · Options, Futures & Derivatives · advanced

*Source coverage: full. PDF pages inspected: 1-3. These are study notes, not verified trading results.*

## Summary

This three-page university tutorial contains seven advanced interest-rate modelling exercises. It moves from Ho-Lee and Hull-White short-rate models to the Heath-Jarrow-Morton framework, probability-measure changes and coupon-bond volatility. It is useful as a study checklist for readers who already know stochastic calculus and derivatives pricing. It contains questions and model inputs, not worked solutions or trading recommendations (PDF pp. 1-3).

## Key points

- The first problem connects an integrated Brownian motion with discount-bond pricing and fitting an initial forward curve in Ho-Lee (p. 1).
- The second explores Hull-White mean reversion while holding a long-run variance constraint fixed (p. 1).
- The third asks for a bond-option price and the minimum information required to calculate it (pp. 1-2).
- HJM exercises distinguish no-arbitrage conditions from whether a useful finite-dimensional Markov representation exists (p. 2).
- Another exercise contrasts real-world and risk-neutral dynamics and asks when Gaussian forward rates and lognormal discount-bond prices follow (p. 3).
- The final problem moves from zero-coupon dynamics to a continuously coupon-paying bond, asking how its volatility varies with maturity (p. 3).

## Actionable rules

1. No trading entry, exit, stop or sizing rules are supplied. Use the numbered questions to identify gaps in model understanding rather than as a signal system.
2. For the concrete Hull-White exercise, the supplied inputs include mean reversion 0.24, volatility 0.02, a forward curve `0.06 + 0.01 exp(-0.2t)`, and a three-month option on a ten-year, £100 face-value zero-coupon bond with a £53.50 strike (p. 1). These are problem inputs; no numerical option price is provided.
3. Before comparing solutions, preserve the stated measure, volatility specification, maturity convention and payoff. Changing any of them changes the question being answered (pp. 1-3).

## Caveats

This note summarizes the scope of the exercises and does not supply or verify their solutions. Some displayed mathematics extracts poorly, so the original typesetting is needed for exact derivations. The assumptions are mathematical modelling choices rather than empirical guarantees. Publication year is not stated. The source is trading-related educational material despite its lack of exposition.

## Who it is for

Advanced students revising interest-rate derivatives after reading a full pricing text.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: interest-rates, ho-lee, hull-white, hjm, bond-options
