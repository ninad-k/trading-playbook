# Rubinstein on Derivatives: the trader's summary

*A state-price and replication-based path from forwards and options through volatility and dynamic strategies.*

**Mark Rubinstein** · 1999 · Options, Futures & Derivatives · advanced

*Source coverage: partial. PDF pages inspected: 2-8, 29, 49, 70, 90, 111, 131, 151, 172, 192, 233, 254, 274, 294, 315, 335, 356, 376, 396, 417, 437, 458, 478 (every page the scan yields text for; the remaining pages are image-only). These are study notes, not verified trading results.*

## Overview

Rubinstein builds derivatives pricing around payoffs, replication, no-arbitrage, and risk-neutral probabilities. The sequence begins with assets, cash, states, and market organization; advances through forwards, futures, swaps, option combinations, binomial trees, and Black–Scholes; and closes with realized and implied volatility, dynamic asset allocation, portfolio insurance, and simulation. The approach is conceptual but mathematically demanding. Its recurring question is not whether a derivative “looks cheap,” but whether its payoff can be reproduced and therefore assigned a price consistent with other traded claims.

This note is based on the OCR text actually available for selected pages, not a complete reading. Much of the 498-page scan has no extracted text, so the chapter architecture is reliable but some derivations and examples could not be checked line by line.

## Core thesis

Derivative value follows from consistency across attainable state-contingent payoffs. If two portfolios produce the same future cash flows in every state, they should cost the same today; otherwise an arbitrage exists. Market prices of derivatives can also be read in reverse to infer the market's risk-neutral distribution. Rubinstein presents this inverse problem as a central task: learn as much as possible about state prices from a limited menu of traded contracts (PDF p. 29).

## Key concepts

- **State-contingent payoff** — Cash flow specified separately for each possible future state.
- **Replication** — Combining the underlying asset, cash, and derivatives to match another claim's payoff.
- **No-arbitrage** — The consistency condition that equal future payoffs carry equal current values.
- **Risk-neutral probability** — Pricing weights implied by traded assets, distinct from forecasts of actual probabilities.
- **Forward contract** — A bilateral obligation to transact later at a delivery price fixed today.
- **Futures contract** — A standardized forward-like claim settled through daily marking to market (PDF p. 111).
- **Call and put** — Cancellation rights to buy or sell the underlying at a strike price; unlike forwards, exercise is optional (PDF p. 49).
- **Binomial tree** — A discrete state model used to value and hedge contingent claims by backward induction.
- **Delta hedge** — An offsetting position in the underlying chosen to neutralize small price exposure.
- **Implied volatility** — The volatility input that makes a model price equal the observed option price.
- **Realized volatility** — A statistical estimate derived from observed returns.
- **Portfolio insurance** — A dynamic strategy intended to impose a floor or reshape portfolio payoffs.

## Rules and setups

1. Describe the claim as a dated payoff across states before attempting valuation.
2. Search for a portfolio of cash, underlying assets, and traded derivatives that reproduces that payoff. Price the claim from the replicating portfolio when the replication is exact.
3. For forward valuation, include financing, payouts, storage costs, and any convenience yield. Commodity carry differs from financial-asset carry because physical inventory may be costly or beneficial to hold (PDF pp. 131, 396).
4. Treat futures cash flows as daily changes in the futures price; the undiscounted sum of daily settlements equals the terminal spot price minus the initial futures price, per unit of exposure (PDF p. 111).
5. Use binomial valuation by specifying state transitions, valuing terminal payoffs, and stepping backward under risk-neutral weights. Interest-rate trees additionally need to fit the observed term structure; the HJM illustration uses current zero-coupon bond prices and a volatility structure (PDF p. 274).
6. Apply Black–Scholes only with its assumptions visible: no arbitrage, perfect markets, known future riskless and payout returns, known volatility, and no jumps. The text discusses futures and currency options through substitutions, and time-varying deterministic inputs through averages or maturity-matched bond returns (PDF p. 315).
7. When estimating realized volatility from very high-frequency transactions, adjust for microstructure noise. Rubinstein's example shows bid–ask bounce can be comparable to true transaction-return variance and overwhelm the apparent gain from more observations (PDF p. 335).

## Risk and money management

This is a valuation text, not a discretionary trading manual. Risk is handled through payoff design, hedging parameters, diversification across states, and explicit model assumptions. The practical discipline is to identify exposures before trading: directional payoff, financing, payout or carry, volatility, path dependence, and liquidity. A model price is conditional on inputs and market structure; it does not remove gap, parameter, transaction-cost, or execution risk.

## Psychology and discipline

Psychology is largely outside the book's scope. Its substitute is analytical discipline: separate actual probabilities from pricing probabilities, refuse inconsistent cash-flow comparisons, and avoid treating a formula as valid after its assumptions fail. The chapters on volatility reinforce humility about estimation error.

## Chapter map

- Ch 1 — Assets, Derivatives and Markets — State payoffs, asset classes, contracts, and trading venues.
- Ch 2 — Forwards and Futures — Carry pricing, replication, futures hedging, and swaps.
- Ch 3 — Introduction to Options — Basic and combined positions, valuation, and replication.
- Ch 4 — The Binomial Option Pricing Model — Single- and multi-period trees, hedging, extensions, and bond options.
- Ch 5 — The Black–Scholes Formula — Derivation, hedge sensitivities, and extensions.
- Ch 6 — Volatility — Realized estimation and volatility inferred from options.
- Ch 7 — Dynamic Strategies — Asset allocation, portfolio insurance, and simulation.

## Further material from the remaining readable pages

- **Swap valuation by replication** — an interest-rate swap is valued by asking what portfolio replicates it: a long fixed-rate bond plus a short floating-rate bond, or the equivalent alternative decomposition (p. 151).
- **Payoff diagrams and standard-option tables** — the protective put (asset plus put) and the other elementary combinations are presented as profit diagrams with a worked parameter set, alongside sample option values for S=100, t=1, r=1.15, d=1.00 and volatility 0.30 (pp. 172, 192).
- **Greeks from the tree** — theta and the other sensitivities are read directly off the binomial lattice rather than from closed-form derivatives (p. 254).
- **Portfolio insurance algebra** — the insured payoff max(K, alpha x S*) is rewritten as K + max(0, alpha x S* - K), i.e. cash plus a call, which is how the replicating strategy is derived; a strategy that dominated the underlying portfolio is ruled out by arbitrage (p. 356).
- **Market price of risk** — defined on the binomial tree as the common ratio of expected excess return to standard deviation across all default-free securities at every node (p. 417).
- **Riskless return** — short-term US Treasury bills are used as the archetypal zero-coupon, default-free security proxying the riskless rate (p. 437).
- The book closes with an annotated bibliography and an applications bibliography that summarise the primary literature paper by paper (pp. 458, 478).

## Strengths and caveats

The state-payoff perspective unifies instruments that are often taught separately, and the progression from replication to implied distributions is unusually coherent. The book also flags model limitations rather than presenting Black–Scholes as an oracle. Some institutional details are dated: the scan describes floor exchanges, fractional stock spreads, and late-1990s market organization (PDF pp. 70, 335). More seriously, this source is sampled OCR: equations and symbols are often damaged, and most pages are blank in extracted text. Readers should use the original for any implementation or derivation.

## Who should read it

Advanced students, derivatives traders, risk managers, and quantitative analysts who want a conceptual bridge between payoff engineering and formal pricing. It assumes comfort with algebra, probability, and option terminology.

## Related books in this library

- [The Mathematics of Financial Derivatives: A Student Introduction](https://ninad-k.github.io/trading-playbook/books/1-the-mathematics-of-financial-derivatives.html) — Develops the same pricing domain through stochastic calculus, PDEs, and numerical methods.
- [How to Trade the New Single Stock Futures](https://ninad-k.github.io/trading-playbook/books/jake-bernstein-how-to-trade-the-new-single-stock-futures.html) — Applies futures mechanics to a specific retail instrument rather than general valuation theory.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: derivatives, options, futures, volatility, arbitrage, hedging
