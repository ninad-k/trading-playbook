# The Mathematics of Financial Derivatives: A Student Introduction: the trader's summary

*A student-oriented route from random walks and Black–Scholes PDEs to numerical and path-dependent option valuation.*

**Paul Wilmott, Sam Howison, and Jeff Dewynne** · 1995 · Options, Futures & Derivatives · advanced

*Source coverage: partial. PDF pages inspected: 1-9, 22, 36, 50, 64, 77, 91, 105, 119, 132, 146, 160, 174, 187, 201, 215, 229, 242, 256, 270, 284, 297, 311, 325 (every page the scan yields text for; the remaining pages are image-only). These are study notes, not verified trading results.*

## Summary

Wilmott, Howison, and Dewynne introduce derivative valuation from an applied-mathematics perspective. The organizing tool is the partial differential equation: model a random underlying, remove hedgeable randomness, impose payoff and boundary conditions, then solve analytically or numerically. The book moves from Black–Scholes through finite differences and binomial trees to American, exotic, path-dependent, interest-rate, and convertible claims. Its stated preference is an accurate numerical solution of a realistic model over a closed-form solution obtained by distorting the problem (PDF pp. 6-9).

## Key points

- Asset-price uncertainty is modeled with a continuous-time random walk; Itô's lemma supplies the calculus for functions of that process (PDF p. 36).
- Dynamic hedging converts the pricing problem into a deterministic no-arbitrage relation.
- European values follow from the Black–Scholes PDE plus final and boundary conditions.
- American early exercise creates a free-boundary or complementarity problem.
- Explicit, fully implicit, and Crank–Nicolson finite differences are treated as practical solvers.
- Binomial trees are presented as popular but more limited discrete alternatives.
- General payoff construction redirects risk: a bull call spread buys one call and writes a higher-strike call with the same expiry (PDF p. 50).
- Later chapters extend the framework to barriers, Asians, lookbacks, transaction costs, stochastic rates, and convertibles.

## Actionable rules

1. Specify the contract payoff and all boundary or early-exercise conditions before selecting a solver.
2. Estimate annualized variance from equally spaced returns only with explicit awareness that dataset length and parameter instability remain unresolved in this introductory treatment (PDF p. 36).
3. Use closed form where assumptions fit; otherwise use a stable numerical method on the correct model.
4. For a same-expiry bull call spread, buy strike (E_1) and sell higher strike (E_2); maximum loss is the net premium and upside is capped by the strike gap (PDF p. 50).

## Chapter coverage recovered from the scan

The sampled pages confirm the book's full arc, chapter by chapter: options and their uses including margin for writers (Ch. 1); the random walk, Ito's lemma and the derivation of the Black-Scholes equation with a discussion of implied versus historic volatility, which the text says is plainly not constant over long periods (Ch. 2-3); partial differential equations and the diffusion equation (Ch. 4-5); the Black-Scholes formulae and their Greeks, including the put delta (Ch. 6); variations on the model - dividends, the American option's optimal exercise boundary S_f(t), and an optional analytical treatment of the American call with dividends (Ch. 6-7); finite-difference methods, covering explicit, fully-implicit (with its tridiagonal storage advantage) and Crank-Nicolson schemes (Ch. 8); projected SOR for the linear complementarity problems that American options generate, given as working pseudocode (Ch. 9); binomial methods derived by matching moments (Ch. 10); exotic and path-dependent options, starting from binaries (Ch. 11-13); barrier options, where the contract reverts to a vanilla Black-Scholes call once the barrier is crossed (Ch. 13); Asian options with continuously and discretely sampled arithmetic averages (Ch. 14); lookbacks and options on the running maximum, including the similarity reductions available for certain payoffs (Ch. 15-16); interest-rate models, which the book introduces by explicitly retiring the constant-rate assumption (Ch. 17); and convertible bonds under stochastic rates (Ch. 18). The volume closes with exercises and hints to selected exercises.

## Caveats

This is a mathematics textbook, not a signal system. The OCR is sampled and equations are sometimes corrupted, so this note does not certify implementation details. Models still depend on volatility, transaction-cost, continuity, and hedge assumptions.

## Who it is for

Mathematics, physics, engineering, and quantitative-finance students who know calculus, algebra, and basic probability and want a PDE-centered introduction.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: derivatives, options, black-scholes, pde, numerical-methods
