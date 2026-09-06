# Credit Risk Modelling and Credit Derivatives: the trader's summary

*Schönbucher's Bonn PhD dissertation extending the Heath-Jarrow-Morton term-structure framework to defaultable bonds, plus closed-form pricing for the main credit derivative structures.*

**Philipp J. Schönbucher** · 2000 · Quant, Microstructure & Academic Research · advanced

*Source coverage: partial. PDF pages inspected: 1-2 and the structure and pricing chapters checked against the note. These are study notes, not verified trading results.*

## Summary

This is Philipp J. Schönbucher's 2000 doctoral dissertation at the University of Bonn ("Credit Risk Modelling and Credit Derivatives"), later expanded into his well-known textbook of the same subject. The question addressed: how should the term structure of defaultable bond prices, and the market for credit derivatives built on it, be modeled in a way that is both arbitrage-free and flexible enough to price real-world credit derivative structures? The method extends the Heath-Jarrow-Morton (HJM) forward-rate framework — originally built for default-free interest rates — to defaultable bonds, introducing a "multiple defaults" model in which a defaulted bond is restructured and continues trading rather than being liquidated for cash. The main finding is a set of arbitrage-free drift and short-rate restrictions (analogous to the classic HJM drift condition) under which defaultable forward rates, ratings-transition dynamics, and jumps at default can all be modeled consistently, yielding closed-form pricing formulas for the major credit derivative types under both Gaussian-HJM and Cox-Ingersoll-Ross specifications.

## Key points

- Surveys the two dominant modeling traditions: firm's-value models (Merton, Black-Cox — default triggered by asset value hitting a boundary, good for capital-structure questions but generates unrealistically low short-term credit spreads) and intensity models (Jarrow-Turnbull, Duffie-Singleton, Lando — default as the first jump of a point process, better suited to derivative pricing).
- Develops a "multiple defaults" HJM extension in which defaulted debt is restructured rather than liquidated, allowing the defaultable term structure to keep evolving after a credit event.
- Derives the arbitrage-free drift restriction for defaultable forward rates, closely related to the standard HJM restriction, plus the additional requirement that the defaultable short rate never fall below the default-free short rate.
- Extends the model to allow jumps in defaultable forward rates at default, and further to a full ratings-transition framework with stochastic credit-spread dynamics in every rating class (not just a single spread multiplier).
- Catalogs and defines the standard credit derivative structures: asset swap packages, total rate of return swaps (TRORS), default swaps (credit default swaps), credit spread forwards/swaps/options, options on defaultable bonds, basket (first-to-default) default swaps, and credit-linked notes.
- Notes basket/first-to-default default swaps are most useful for small baskets (fewer than six credits); large portfolios are better handled with a loss-level trigger instead.
- Derives closed-form pricing formulas for these instruments under two recovery-model conventions (fractional recovery and equivalent recovery) and two interest-rate/spread dynamics (Gaussian HJM and Cox-Ingersoll-Ross).
- Identifies applications of credit derivatives for market participants: banks managing/freeing credit lines and regulatory capital, traders arbitraging mispriced defaultable bonds or taking a pure view on credit spreads, and investors gaining customized credit exposure via credit-linked notes.

## Actionable rules

None given as trading rules — this is a mathematical pricing-theory dissertation, not a trading system. What a practitioner can take from it: (1) understand what each named credit derivative structure (default swap, TRORS, asset swap, credit spread option, basket swap, credit-linked note) actually isolates — credit risk, market risk, or both — before using it to hedge or speculate; (2) recognize that credit-spread option payoffs and default-swap pricing are tightly linked to the price of an equivalent defaultable floating-rate note, useful for sanity-checking market quotes; (3) treat any credit-derivative pricing model's short-term spread output with skepticism if it is a pure firm's-value model, since those structurally understate near-term default risk.

## Caveats

This is a highly mathematical academic dissertation (stochastic calculus, arbitrage pricing, HJM machinery) aimed at quantitative researchers and derivatives desks, not retail or discretionary traders — most of its content (measure changes, forward-rate SDEs, closed-form derivations) requires graduate-level mathematical finance to follow. Written in 2000, before the 2008 credit crisis exposed serious weaknesses in Gaussian copula and related credit-correlation modeling assumptions used elsewhere in the credit derivatives industry; this dissertation's single-name and basket pricing framework predates those events and the subsequent regulatory overhaul of credit derivatives markets (central clearing, standardized CDS contracts). Notation-heavy; the manuscript includes an extensive symbol glossary that is essential to follow the later chapters.

## Who it is for

Quantitative researchers, credit derivatives desks, or advanced students who need a rigorous, arbitrage-free pricing framework for defaultable bonds and the standard credit derivative structures — not a fit for discretionary or retail traders looking for tradable rules.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: credit-derivatives, credit-risk, default-swaps, term-structure, hjm-model, academic, pricing-models
