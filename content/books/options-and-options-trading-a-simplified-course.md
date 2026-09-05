---
title: "Options and Options Trading: A Simplified Course"
author: Robert W. Ward
year: 2004
slug: options-and-options-trading-a-simplified-course
tier: A
category: Options, Futures & Derivatives
tags: [options, black-scholes, binomial-model, greeks, delta-hedging, volatility, probability, derivatives]
difficulty: beginner
doc_type: book
pages: 405
one_liner: "Builds option pricing from coin-toss probability up through the Black-Scholes formula, then argues no strategy is an automatic winner and the real edge is order flow, customer business, and reading volatility."
related: [black-scholes-option-pricing-model, fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed, hull-options-futures-and-other-derivative-securities-5th-ed]
source_file: "Options And Options Trading A Simplified Course.pdf"
---

## Overview

Ward, a former head trader in gold and foreign exchange derivatives, wrote this as a from-scratch derivatives primer aimed at readers with no math background. Part One builds intuition using coin-toss probability (binomial trees, Pascal's triangle, frequency distributions) and applies it to a running IBM stock-option example. Part Two extends that groundwork into "the Formula," walking through a skeleton option-pricing model up to Black-Scholes itself, including volatility and the model's known weaknesses. Part Three turns to trading: a primer on risk and hedging, the Greeks, how professional trading desks actually make money (mostly from customers, not forecasting), converting puts into calls and back, a survey of the most common option strategies, and a closing chapter of "market insights and edges." Each chapter ends with a key-concepts review and practice questions (answers in a back-of-book answer key), reflecting its origin as a course text rather than a strategy manual.

## Core thesis

Option pricing is not black magic — it is built from the same probability logic as counting the outcomes of coin tosses, and once a reader accepts that, the Black-Scholes formula becomes a transparent (if imperfect) codification of intuitive ideas rather than an opaque black box. But understanding the pricing math is not the same as having a trading edge. The book's second, more cynical thesis (Part Three) is that no option strategy is inherently profitable — under fair pricing all strategies break even before costs — and that professional traders' real profits come from customer order flow, bid/ask spreads, information advantages, and off-market pricing of private deals, not from clever formulas or "mispriced" options. For a self-directed trader, the only legitimate edges are a genuinely better-than-average opinion about future volatility and price direction, and discipline about costs.

## Key concepts

- **Binomial tree / coin-toss model** — the number of paths to each outcome of N coin tosses (2^N total paths, N+1 outcomes) mirrors the logic behind the Cox-Ross-Rubinstein binomial option model; frequency counts follow Pascal's triangle (1-4-6-4-1 pattern for four tosses).
- **Moneyness** — at-the-money (strike = spot), in-the-money (exercising now nets a profit), out-of-the-money (exercising now would lose money); illustrated with a $100 IBM stock and a ladder of strikes from $80–$120.
- **Cash, forward, and futures markets** — three venues for the same underlying that trade in line with each other except around delivery frictions; futures are standardized/exchange-traded (fungible, liquid), forwards are bespoke dealer-to-client contracts (invitation-only, less liquid).
- **Spot-to-forward pricing (S·e^rT)** — the forward price is the spot price compounded at the risk-free rate to the delivery date; this is why an at-the-money call costs more than an at-the-money put of the same strike and tenor (the forward, not the spot, is the "fair" reference price).
- **Delta** — the option's rate of price change relative to a $1 move in the underlying (0.00–1.00 for calls), also called the hedge ratio; interpreted loosely as an approximate probability of finishing in-the-money.
- **Gamma** — the rate of change of delta (the "delta of the delta" / the option's "acceleration"); the source of the mismatch between a static hedge and a moving underlying.
- **Theta** — the option's time decay, measured typically per day or per week of remaining life.
- **Vega (kappa)** — the option's sensitivity to a percentage-point change in implied volatility.
- **Rho** — sensitivity to interest rates (rho 1) and, separately, to dividends (rho 2, described as much harder to hedge).
- **Delta neutral** — a position built so component deltas net to zero, removing first-order directional exposure; the book argues this is far less automatically profitable than academic theory suggests once real-world costs are included.
- **Implied vs. statistical (historical) volatility** — implied volatility is backed out of an option's market price via a pricing model; statistical volatility is computed from realized past price changes; the book frames forecasting the gap between them as the central skill in options.
- **CPL.PCS (put-call-long / put-call-short)** — mnemonic ("Corporal Paces") for the two synthetic-equivalence formulas: Call − Put = Long, and Put − Call = Short, used to convert between puts, calls, and stock.
- **Mispriced options** — the book argues genuine, persistent option mispricing is effectively undetectable in practice ("phantoms"); apparent edges are usually relative (cross-strike/cross-maturity) rather than absolute.

## Rules and setups

This is a pricing-theory and market-structure course, not a signal-based trading system — it gives no entries, stops, or position-sizing formulas for directional trading. Its actionable content is a set of mechanical construction/conversion rules and a strategy-selection map:

1. **Conversion mechanics (CPL.PCS).** To build a synthetic call: buy the put and buy the equivalent long stock (Call = Put + Long). To build a synthetic put: buy the call and sell the equivalent stock short (Put = Call + Short).
2. **Conversion validity conditions.** For a conversion or reverse conversion to be a true (near risk-free) hedge: (a) put and call strikes must match exactly; (b) expirations must match exactly; (c) the stock leg must be executed in the market that corresponds to the option type (spot stock for spot options, futures for futures options); (d) share count must offset precisely (1 option contract = 100 shares); (e) all legs must be placed simultaneously at prevailing prices — "lifting a leg" (executing legs sequentially) adds uncompensated risk.
3. **Pit-trader rule of thumb for conversions.** Whatever you do with the put, do the same with the stock (buy the put → buy the stock as the offset; sell the put → sell the stock).
4. **Strategy-to-market-view map** (Ch. 21, non-numeric but concrete): covered write / buy-write for a flat-to-mildly-bullish view; vertical (bull/bear) spreads for a directional view with defined risk; horizontal/calendar spreads to trade time and volatility term structure; ratio writes (e.g., buy 1 ATM call, sell 3 OTM calls) when expecting volatility to fall sharply; back spreads (the reverse ratio) when expecting volatility to rise sharply; long straddle/strangle (same-strike vs. different-strike puts+calls) when expecting a large move or volatility spike; short straddle/strangle for an expected quiet, range-bound market; synthetic long/short (call+put combinations) to replicate stock exposure without holding shares; conversion/reverse conversion to flatten three-legged exposure to near zero.
5. **Worked straddle example (numbers from the book).** With IBM at $100, the $100 straddle (call $3.50 + put $3.50 = $7.00) breaks even at $93 and $107 by January expiry; the $95/$105 strangle costs $3.40 combined and breaks even at $91.60 and $108.40 — cheaper premium for a wider required move, illustrating the straddle-vs.-strangle cost/breakeven tradeoff.
6. **General execution discipline.** Never leg into or out of a multi-leg position; treat mispricing claims skeptically — an "edge" must come from a demonstrably better forecast of future volatility or direction, not from an assumed pricing error.

## Risk and money management

The book frames risk management almost entirely through the Greeks rather than through position-sizing percentages: a trader should know a portfolio's aggregate delta (directional exposure), gamma (how fast delta will move against the trader as price moves), theta (daily cost of holding the position), vega (exposure to a volatility shift), and rho/rho-2 (interest-rate and dividend exposure), and should hedge each dimension deliberately rather than assume a position is safe because it "looks" balanced. It explicitly warns that "there are no perfect hedges" — every open position, however offset, retains residual risk (basis risk, gamma risk between rebalances, dividend risk) that can surface violently in a large, seemingly well-hedged portfolio. On delta-neutral trading specifically, the author disputes the Black-Scholes textbook claim that continuous delta hedging is riskless and only earns the risk-free rate: in the real world, borrowing costs exceed the risk-free rate, commissions and bid/ask spreads are nonzero, liquidity is finite, and continuous rebalancing is impossible, so the average delta-neutral trader loses money to these frictions unless the original position carried a built-in mispricing edge. No percentage-of-capital risk limits, stop-loss rules, or position-sizing formulas are given anywhere in the book — risk is managed by measuring and offsetting Greek exposures, not by capping dollar loss per trade.

## Psychology and discipline

Psychology is addressed less as trader self-management and more as a market-structure observation: prices are set by emotional humans, not the unemotional statistical models used to value options, so fear and greed create measurable phenomena (volatility skew, panics near popular strangle breakevens) that a disciplined trader can study and exploit. The book explicitly warns against two behavioral traps: (1) treating a good run of profitability as proof of skill, which tempts traders and management to raise position size right before "the inevitable bad turn," and (2) listening to confident media commentators and forecasters, since being average in one's opinions guarantees an average (or worse, cost-adjusted negative) return. Its practical psychological prescription, borrowed from a Wayne Gretzky anecdote ("skate to where the puck is going to be"), is to develop a documented, testable view of how sentiment and volatility are likely to shift — through patient, structured observation — rather than reacting to where the market already is.

## Chapter map

- Ch 1 — What a derivative is: options, forwards, futures defined; moneyness; cash/forward/futures market structure.
- Ch 2–3 — Binomials, coin tosses, Pascal's triangle: the combinatorial basis for option pricing models.
- Ch 4–5 — Distributions, probabilities, odds, and payoffs: frequency vs. probability distributions, expected payoff logic.
- Ch 6–8 — Writing a first option; strike prices and summation notation; deriving the "fair price" of an option from expected payoff.
- Ch 9 — Applying the framework to a real instrument: an IBM stock option worked example.
- Ch 10–11 — A statistics crash course; comparing Dow Jones price behavior to coin-toss randomness.
- Ch 12 — Converting spot prices to forward prices (S·e^rT).
- Ch 13–14 — Building a "skeleton" option formula and arriving at Black-Scholes.
- Ch 15–16 — Volatility's role in the formula; the pros and cons (assumptions and failure modes) of Black-Scholes.
- Ch 17–18 — A primer on risk and hedging; finding and hedging option risk via the Greeks (delta, gamma, theta, vega, rho).
- Ch 19 — How professional traders actually make money: bid/ask spreads, order flow, customer markups, scalping, spreading, arbitrage, off-market private deal pricing.
- Ch 20 — Converting puts and calls (CPL.PCS synthetic-equivalence formulas and pit-trading conversion mechanics).
- Ch 21 — The most common option strategies (covered writes, vertical/horizontal/diagonal/ratio spreads, straddles/strangles, synthetics, conversions) mapped to market views.
- Ch 22 — Market insights and edges: why no strategy is an automatic winner, why claimed mispricings are rarely real, and why volatility forecasting is the central skill.

## Strengths and caveats

The book's genuine strength is pedagogical sequencing: it is unusually careful about building intuition for probability and pricing from first principles before introducing any formula, which makes it a strong on-ramp for a reader with no quantitative background. The tradeoff is that roughly two-thirds of the book (Parts One and Two) is pricing theory and probability education rather than trading material, so a reader looking for concrete setups will find comparatively little until Part Three, and even there the content is a strategy catalog and a set of qualitative market observations rather than a testable rule set. Some content is dated: references to open-outcry pits, "SOES," and 2001–2003-era market examples reflect early-2000s market structure that has since moved almost entirely to electronic execution. The book's central claim that professional profits come overwhelmingly from customer flow and market-making rather than forecasting is a useful corrective to retail strategy-selling books, but it also means the book offers little to a reader whose only realistic account type is a retail brokerage account without access to order flow or private deal pricing.

## Who should read it

Best suited to a complete beginner who wants to understand where option pricing formulas come from before using them, or an intermediate trader who has learned to run Black-Scholes as a "black box" and wants the underlying logic explained in plain language. Less useful for a trader who already understands the Greeks and wants concrete, numbered entry/exit/sizing rules for a specific strategy — for that, a strategy-specific book with defined systems is a better fit.

## Related books in this library

- [[black-scholes-option-pricing-model]] — the formal derivation of the same Black-Scholes formula this book approaches intuitively through coin-toss probability.
- [[fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed]] — picks up where this book's Greeks chapter leaves off, with numbered entry/adjustment/exit road maps for delta-neutral strategies this book only surveys conceptually.
- [[hull-options-futures-and-other-derivative-securities-5th-ed]] — the rigorous academic derivative-pricing text this book is a simplified, narrative on-ramp to.
