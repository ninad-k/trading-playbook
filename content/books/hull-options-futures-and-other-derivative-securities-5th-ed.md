---
author: John C. Hull
category: Options, Futures & Derivatives
difficulty: advanced
doc_type: book
one_liner: 'The standard academic/professional derivatives textbook: pricing theory,
  hedging, the Greeks, binomial and Black-Scholes models, swaps, and risk measurement.'
pages: 756
related:
- fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed
- guy-cohen-the-bible-of-options-strategies
- lawrence-g-mcmillan-profit-with-options
- derivatives-pricing-and-financial-modelling
reviewed_pdf_pages: 5-9, 71, 133, 299, 341, 346, 362 (contents, the margin rules,
  the Greeks chapters and the VaR/regulatory-capital sections)
slug: hull-options-futures-and-other-derivative-securities-5th-ed
source_file: Hull-Options_ Futures And Other Derivative Securities_ 5Th Ed.pdf
source_review: partial
tags:
- options
- futures
- derivatives
- greeks
- black-scholes
- hedging
- put-call-parity
- value-at-risk
tier: A
title: Options, Futures, and Other Derivatives (5th Edition)
year: 2003
---

## Overview

This is John Hull's widely used derivatives textbook — described on its own cover as both "a best-selling college textbook" and "the bible in trading rooms throughout the world." The fifth edition runs to 30 chapters covering futures, forwards, swaps, options mechanics, and pricing theory, with seven chapters new to this edition (hedging with futures, more on numerical procedures, swaps revisited, credit derivatives, real options, insurance/weather/energy derivatives, and derivatives mishaps). It is a rigorous, math-heavy academic text rather than a trading manual, built around a small number of core ideas — no-arbitrage pricing, risk-neutral valuation, and continuous hedging — that it then applies across every derivative type. These notes focus on the parts of the book most relevant to a practitioner: pricing intuition, the Greeks, put-call parity, hedging mechanics, and the logic behind the binomial and Black-Scholes models, rather than the full mathematical derivations or the more specialized later chapters (interest-rate derivatives, swaps, credit derivatives, real options).

## Core thesis

Nearly every derivative can be priced by constructing a hedge — a combination of the underlying asset and cash (or the underlying and the derivative) that eliminates risk over a short interval — and then arguing that a riskless portfolio must earn the risk-free rate, or an arbitrage opportunity would exist. This "no-arbitrage" logic underlies forward/futures pricing, the binomial option-pricing model, and the Black-Scholes-Merton equation alike. A closely related idea, risk-neutral valuation, shows that a derivative can be priced by pretending all investors are risk-neutral, computing the expected payoff under that assumption, and discounting it at the risk-free rate — which gives the same answer as the real, risk-averse world because the risk preferences cancel out of the pricing equation. The book treats hedging (for corporates and portfolio managers) and pricing (for market-makers and quants) as two sides of the same coin: an options market-maker prices a contract by working out the cost of replicating (hedging) it.

## Key concepts

- **Forward vs. futures contract** — a forward is a private, customized OTC agreement to buy/sell at a future date; a futures contract is the same idea standardized and exchange-traded with daily marking-to-market.
- **Cost of carry / no-arbitrage forward pricing** — a forward price is pinned down by the spot price plus the net cost of financing and holding the asset (interest less any income/yield); any deviation creates a riskless arbitrage.
- **Hedging with futures** — using a futures position to offset exposure in the underlying; the minimum-variance hedge ratio sizes the futures leg when the hedge is imperfect (basis risk).
- **Put-call parity** — for European options on the same stock and strike, `c + Ke^{-rT} = p + S0` (call price plus present value of the strike equals put price plus stock price); it lets a trader infer one option's fair price from the other's, and violations (net of transaction costs) are the classic options arbitrage.
- **Six factors that move an option's value** — current stock price, strike price, time to expiration, volatility, the risk-free rate, and expected dividends; a call generally rises with stock price, time, volatility, and rates, and falls with strike and dividends (a put moves in mirror fashion on most of these).
- **The Greeks** — sensitivities of an option's price to each input: **Delta** (∂price/∂stock price; for a European call on a dividend-yield-paying stock, delta = e^{-qT}N(d1)), **Gamma** (rate of change of delta), **Theta** (time decay), **Vega** (sensitivity to volatility), **Rho** (sensitivity to interest rates).
- **Delta hedging** — offsetting an option position with a position in the underlying sized by delta so the combined position is (instantaneously) insensitive to small price moves; because delta changes as price and time move, a delta-hedge must be rebalanced continuously (dynamic hedging), and cannot be "set and forget."
- **Risk-neutral valuation** — pricing a derivative by discounting its expected payoff under an assumed world where all assets earn the risk-free rate; produces correct prices in the real world too, because risk preferences drop out of the no-arbitrage argument.
- **Binomial tree model** — models the underlying as moving up or down by fixed factors (u, d) over discrete steps; the option is priced by replicating its payoff with a position in the stock and a risk-free bond (or, equivalently, using risk-neutral probabilities), and refining the tree (more, shorter steps) converges toward the Black-Scholes price.
- **Black-Scholes-Merton model** — the continuous-time limit of the same replication logic: a continuously-rebalanced riskless hedge between the option and the stock must earn the risk-free rate, which yields a partial differential equation with closed-form solutions for European calls and puts.
- **Value at Risk (VaR)** — a single number summarizing portfolio risk: the loss over N days that will not be exceeded with X% confidence; bank regulators use N = 10 days, X = 99%, and require capital of at least 3× that VaR figure.

## Rules and setups

This is a pricing/hedging textbook, not a trading-signal book, so it has no entries, exits, or position-sizing rules in the trading-playbook sense. The closest things to operational "rules" it lays out are option-margin formulas and the seven Black-Scholes assumptions, both stated precisely enough to apply directly:

1. **Naked written call margin** (per contract, ×100 shares): the greater of (a) 100% of the sale proceeds + 20% of the stock price − any out-of-the-money amount, or (b) 100% of proceeds + 10% of the stock price. The 20% is replaced by 15% for a broad-based stock index option.
2. **Naked written put margin**: the greater of (a) 100% of proceeds + 20% of stock price − any out-of-the-money amount, or (b) 100% of proceeds + 10% of the strike price.
3. **Black-Scholes-Merton assumptions** (the conditions under which the pricing formula is exact): stock price follows a constant-volatility lognormal process; short selling with full use of proceeds is allowed; no transaction costs or taxes and infinitely divisible securities; no dividends during the derivative's life; no riskless arbitrage opportunities exist; trading is continuous; the risk-free rate is constant and the same for all maturities. The book notes several of these (constant volatility/rates, no dividends) are later relaxed in more advanced chapters.
4. **VaR capital rule**: regulatory market-risk capital ≈ k × (10-day, 99% VaR), with multiplier k set by regulators at a minimum of 3.0.

## Risk and money management

The book's risk content is about measuring and hedging risk rather than sizing trades. Chapter 14 covers the Greeks individually and then in combination (a "delta-gamma-vega" analysis), warning that a portfolio can be delta-neutral while still carrying large gamma or vega risk — e.g., a delta-neutral position with large negative gamma is exposed to big losses from a large price move in either direction, because delta neutrality only protects against small moves. Chapter 16 introduces Value at Risk as the practical, single-number way large institutions and regulators summarize aggregate risk across hundreds of market variables, using historical-simulation or model-building approaches. The book also flags that simple hedging schemes can fail badly in practice — the discussion of portfolio insurance notes it did not work well during the October 19, 1987 crash, because the assumption of continuous, frictionless rebalancing broke down in a fast, gapping market.

## Psychology and discipline

Not a focus of the book; this is a quantitative/technical text aimed at pricing and hedging, not trader behavior. The closest material is procedural discipline around hedge rebalancing: because delta (and the other Greeks) change continuously with price and time, a hedger who fails to rebalance frequently enough will drift away from a riskless position, which the book frames as an execution/discipline problem as much as a modeling one.

## Chapter map

- Ch 1 — Introduction — exchange-traded and OTC markets, forwards, futures, options, types of traders.
- Ch 2 — Mechanics of futures markets — contract specification, margin, delivery, regulation.
- Ch 3 — Determination of forward and futures prices — cost of carry, no-arbitrage pricing.
- Ch 4 — Hedging strategies using futures — basis risk, minimum-variance hedge ratio, stock index hedges.
- Ch 5 — Interest rate markets — zero rates, bond pricing, duration-based hedging.
- Ch 6 — Swaps — mechanics and valuation of interest-rate and currency swaps.
- Ch 7 — Mechanics of options markets — contract specification, margins, taxation.
- Ch 8 — Properties of stock options — bounds on option prices, put-call parity, early exercise, dividends.
- Ch 9 — Trading strategies involving options — spreads, combinations, and other payoff structures.
- Ch 10 — Introduction to binomial trees — one- and two-step trees, risk-neutral valuation, delta.
- Ch 11 — A model of the behavior of stock prices — the Markov property, Itô's lemma, the lognormal property.
- Ch 12 — The Black-Scholes model — derivation, closed-form formulas, implied volatility, dividends.
- Ch 13 — Options on stock indices, currencies, and futures — extending the pricing formulas.
- Ch 14 — The Greek letters — delta, gamma, theta, vega, rho, and dynamic hedging.
- Ch 15 — Volatility smiles — empirical departures from the Black-Scholes constant-volatility assumption.
- Ch 16 — Value at risk — the VaR measure and its use in bank capital requirements.
- Ch 17–19 — (not captured in the sampled pages; per the book's own structure these cover further interest-rate/numerical topics before Ch 20).
- Ch 20 — More on models and numerical procedures — additional numerical pricing methods.
- Ch 21 — Martingales and measures — the mathematical machinery behind risk-neutral pricing.
- Ch 22–24, 26 — (not captured in the sampled pages).
- Ch 25 — Swaps revisited — nonstandard swap products.
- Ch 27 — Credit derivatives — how credit default products work and are valued, including convertible debentures.
- Ch 28 — Real options — applying options theory to capital investment appraisal.
- Ch 29 — Insurance, weather, and energy derivatives — non-traditional derivatives and risk management.
- Ch 30 — Derivatives, mishaps, and what we can learn from them — case studies in derivatives losses.

## Strengths and caveats

This is a graduate-level finance textbook, not a retail trading guide — it assumes calculus/probability fluency and is written for pricing and risk-managing derivatives, not for generating trading signals. Being a 5th edition from the early 2000s, it predates some post-2008 developments in derivatives regulation, OIS/SOFR discounting, and the post-crisis overhaul of credit-derivatives and swap-valuation practice found in later editions; a reader using it for current market conventions (e.g., interest-rate benchmark reform, central clearing) should cross-check against a newer edition or current material. The empirical put-call-parity research it cites (Bhattacharya; Klemkosky and Resnick) is from the late 1970s options market, illustrating the ideas historically rather than describing current market microstructure.

## Who should read it

Traders and analysts who want the underlying pricing logic behind options and futures rather than a strategy cookbook: how delta-hedging and no-arbitrage arguments produce option prices, why the Greeks matter for managing an options book, and how institutions quantify aggregate portfolio risk via VaR. Less suited to a reader looking only for concrete options trading strategies or setups — pair it with a strategy-focused options book for that.

## Related books in this library

- [[fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed]] — practitioner-oriented options strategy counterpart to Hull's pricing theory.
- [[guy-cohen-the-bible-of-options-strategies]] — a strategy reference to pair with Hull's Greeks and payoff-diagram material.
- [[lawrence-g-mcmillan-profit-with-options]] — applies option pricing concepts to concrete trading strategies.
- [[derivatives-pricing-and-financial-modelling]] — another pricing-theory-focused derivatives text for cross-reference.

## Caveats

These notes are based on OCR of a sampled subset of pages (front matter plus evenly spaced pages) of a 756-page scanned textbook; the great majority of pages were not machine-readable, so the chapter map beyond Chapter 16 and several later chapters (17–19, 22–24, 26) is reconstructed from the table of contents, the book's own "new chapters" summary, and scattered running headers rather than from a full read of those chapters' content. Formulas and figures presented here (put-call parity, delta, VaR parameters, margin rules, Black-Scholes assumptions) were confirmed directly in the sampled OCR text.
