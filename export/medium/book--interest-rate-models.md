# Interest-Rate Models: the trader's summary

*Encyclopedia article surveying arbitrage-free term-structure models from Vasicek through Heath-Jarrow-Morton and Markov-functional approaches.*

**Andrew J.G. Cairns** · 2004 · Quant, Microstructure & Academic Research · advanced

*Source coverage: partial. PDF pages inspected: 8, 19 (the model taxonomy and references; the paper is algebraic rather than numeric). These are study notes, not verified trading results.*

## Summary

An academic reference article (prepared for the Encyclopaedia of Actuarial Science) that surveys, in historical sequence, the main continuous-time, arbitrage-free models for the full term structure of interest rates. It starts by defining precise notation for zero-coupon bond prices, spot rates, forward rates, and the instantaneous risk-free rate, then works through short-rate models (Vasicek, Cox-Ingersoll-Ross, Ho-Lee, Hull-White), the Heath-Jarrow-Morton (HJM) framework for modeling the entire forward-rate curve, the Flesaker-Hughston/Potential approach using state-price deflators, and finally Markov-functional models, which are presented as a unifying framework that many earlier models fit into.

## Key points

- Distinguishes precisely between yield-to-maturity, the spot-rate curve, instantaneous forward rates, and the par-yield curve — a common source of confusion the article explicitly calls out.
- The Vasicek (1977) model was the first major arbitrage-free short-rate model and derives a Black-Scholes-type PDE for bond prices; it and the CIR model are both "time-homogeneous, equilibrium" short-rate models.
- Short-rate models (Vasicek, CIR, Ho-Lee, Hull-White) price contingent claims as functions of a low-dimensional Markov state variable, making them computationally tractable.
- The HJM framework instead models the dynamics of the entire forward-rate curve directly, offering more flexibility to fit the observed initial curve exactly but at greater computational cost.
- The Flesaker-Hughston (Potential) approach reformulates pricing using positive state-price deflators, guaranteeing positive interest rates by construction.
- Markov-functional models are presented as a general class requiring only that the model be describable through a low-dimensional Markov process, which many named models (Vasicek, CIR, Ho-Lee, Hull-White) already satisfy.
- The article restricts itself to default-free government debt; credit risk is explicitly left to a separate reference.

## Actionable rules

None given — this is a pure modeling/pricing-theory reference for fixed-income derivatives, not a trading rulebook. Its practical value for a trader is understanding which term-structure model family (equilibrium short-rate vs. HJM vs. Markov-functional) underlies a given interest-rate derivative's pricing or a hedging desk's risk system.

## Caveats

Densely mathematical (stochastic calculus, PDEs, measure theory) and written for an actuarial/quant audience; not accessible without a graduate-level quantitative finance background. It focuses purely on model theory and offers no empirical calibration results, backtests, or practical parameter values, so it cannot be used directly to build a live pricing model without substantial additional work.

## Who it is for

Quants and fixed-income derivatives specialists who need a concise, historically organized map of term-structure model families (Vasicek, CIR, Hull-White, HJM, Markov-functional) before diving into a specific model's full derivation.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: interest-rate-models, term-structure, vasicek, cir, hull-white, hjm, fixed-income, academic-reference
