---
title: Paul Wilmott Introduces Quantitative Finance
author: Paul Wilmott
year: 2001
slug: paul-wilmott-quantitative-finance
tier: A
category: Quant, Microstructure & Academic Research
tags: [quantitative-finance, derivatives, options, no-arbitrage, black-scholes, technical-analysis, market-microstructure]
difficulty: intermediate
doc_type: book
pages: 72
one_liner: "A gentle, discursive intro to quant finance: products and no-arbitrage, option jargon and payoff diagrams, then a skeptical tour of technical analysis and market microstructure."
related: [rubinstein-mark-rubinstein-on-derivatives, hull-options-futures-and-other-derivative-securities-5th-ed, black-scholes-option-pricing-model, chart-formations]
source_file: "Paul Wilmott-Quantitative Finance.pdf"
---

## Overview

This is Wilmott's introductory quant-finance text, aimed at readers who know little or no finance mathematics. The sampled pages cover its first three chapters: an introduction to financial products and the time value of money, a chapter on derivatives (option definitions, payoff diagrams, put-call parity, basic strategies), and a chapter that surveys traditional technical analysis and market microstructure modeling from a skeptical, probabilistic point of view. Wilmott uses Bloomberg screens, The Wall Street Journal listings, and a simple coin-tossing spreadsheet exercise to build intuition before introducing any formal mathematics. The tone throughout is conversational and pedagogical — sidebars ("Time Out...") walk through symbols and concepts step by step for readers intimidated by notation.

## Core thesis

Prices are best modeled probabilistically, not treated as deterministically predictable. Wilmott's opening move is to simulate a stock-like path by repeatedly multiplying a starting value by 1.01 (up) or 0.99 (down) on a coin flip — a multiplicative (lognormal/geometric) random walk, distinct from an additive (arithmetic/Normal) one. He is explicit that this is a modeling choice, not a claim that markets are literally unpredictable: manipulation and structural effects exist, but a probabilistic model is the practical foundation for pricing derivatives. The book's other organizing idea is no-arbitrage: prices of related instruments (spot vs. forward, call vs. put) must satisfy consistency relationships or riskless profit would be available; this idea does the heavy lifting throughout, well before any stochastic calculus is introduced.

## Key concepts

- **No-arbitrage / "no free lunch"** — if two portfolios have identical payoffs in every future state, they must have the same price today, or a riskless profit is available. Used to derive the forward price and put-call parity without probability assumptions.
- **Lognormal (geometric) vs. Normal (arithmetic) random walk** — multiplying by a random factor each period versus adding a random amount; the multiplicative version keeps prices positive and is Wilmott's default toy model.
- **Cum-dividend / ex-dividend** — the stock's price drops around the ex-dividend date to offset the dividend the new buyer will not receive.
- **Forward price relation** — F = S(t)·e^{r(T−t)} for a non-dividend asset, derived by hedging a forward against the underlying and cash rather than by forecasting; extended to F = S(t)·e^{(r+s−c)(T−t)} for commodities (storage cost s, convenience yield c), F = S(t)·e^{(r−r_f)(T−t)} for FX, and F = S(t)·e^{(r−q)(T−t)} for index futures with dividend yield q.
- **Backwardation / contango** — futures price below vs. above the no-arbitrage spot-plus-carry level.
- **Payoff vs. profit diagrams** — payoff = contract value at expiry as a function of the underlying (e.g., max(S−E,0) for a call); profit diagrams net out the premium paid, shifting the break-even point.
- **Intrinsic value vs. time value** — intrinsic value is what the option would be worth if it expired today at the current level; time value is anything above that, driven by uncertainty until expiry.
- **Put-call parity** — C − P = S − E·e^{−r(T−t)}, a model-independent relationship from a hedged portfolio of long call/short put replicating a forward.
- **Gearing (leverage)** — an out-of-the-money option can produce a far higher percentage return than owning the underlying outright if the move is large enough, at the cost of a higher chance of the option expiring worthless.
- **Straddle / strangle** — combinations (long call + long put, same or different strikes) used to speculate on volatility direction rather than price direction.
- **Efficiency of markets vs. technical analysis** — Wilmott repeatedly flags that classic charting concepts (support/resistance, Elliott wave, Gann) lack a rigorous statistical foundation even though they are widely used.

## Rules and setups

The book gives no complete, codeable trading system — it is a finance-theory primer, not a trading manual. It does document mechanics practitioners use:
1. **Coin-toss price simulation**: start at 100, multiply by 1.01 on a head or 0.99 on a tail each period (p = 0.5 default) to generate a toy lognormal path — used purely as a teaching device, not a forecasting tool.
2. **Support and resistance, moving averages, oscillators, candlesticks, point-and-figure charts** — described as commonly used technical tools (Section 3.2), presented descriptively rather than endorsed with specific entry/exit numbers.
3. **Elliott wave / Fibonacci** — five up-wave / three down-wave pattern; peak ratios "supposed" to run near 1.618 and 2.618, which Wilmott explicitly flags as coincidental with the Fibonacci sequence's limiting ratio rather than causal ("unfortunately... people extrapolate wildly from this").
4. **Volume and open interest** — rising price with high volume signals trend strength; rising price with low volume can signal an impending reversal; rising open interest during a trend signals the trend is being reinforced by new positions rather than short-covering.

## Risk and money management

Not a focus of the sampled chapters. The book's closest treatment is structural: it explains gearing/leverage quantitatively (an example compares a 9.6% return on outright stock ownership to a 28% return on a call option for the same underlying move) and flags that the leverage cutting in favor of the option buyer on a big move cuts against a naked option seller symmetrically. No stop-loss, position-sizing, or capital-allocation rules are given in the sampled pages; if later chapters (options Greeks, hedging, risk-neutral valuation — outside the 72-page sample) address this more systematically, it is not visible here.

## Psychology and discipline

Largely absent from the sampled material; this is a technical primer, not a psychology-of-trading book. The one recurring behavioral note is a warning about survivorship bias in market-prediction claims: "we've all done it," Wilmott writes of confident post-hoc predictions, "though it's nothing to be proud of" — people who called a move loudly are remembered, while the many wrong calls are quietly forgotten.

## Chapter map

- Ch 1 — Products and markets: equities, commodities, exchange rates, forwards and futures — instrument definitions, dividends, stock splits, fixed and floating interest rates, the time value of money, and the no-arbitrage derivation of the forward price.
- Ch 2 — Derivatives — call/put definitions and jargon, payoff and profit diagrams, writing vs. buying options, speculation and gearing, put-call parity, straddles/strangles/combinations, binary options, LEAPS/FLEX.
- Ch 3 — Predicting the markets? — technical analysis survey (charting, moving averages, oscillators, candlesticks, point-and-figure, Elliott wave, Fibonacci, Gann), volume and open interest, and an introduction to market microstructure modeling (producers, speculators, market makers).

## Strengths and caveats

The book's Bloomberg screenshots, quoted option prices, and newspaper listings are all dated late 1999/early 2000 (pre-decimalization US options quotes in fractions, not decimals), which dates the material but does not undermine the theory. Wilmott is unusually candid about the limits of technical analysis and chart-pattern folklore for a book that still describes them at length — he presents Elliott wave and Gann analysis descriptively while explicitly questioning their statistical grounding ("Gann charts... need I say more?"), a useful model of how to discuss popular-but-unproven methods without either dismissing or endorsing them uncritically. The sampled 72 pages only reach the end of the technical-analysis/microstructure section of Chapter 3; the book's more mathematically demanding later material (stochastic calculus, the Black-Scholes derivation, the Greeks, exotic options) that presumably follows is not represented in this sample.

## Who should read it

Traders and analysts who want the conceptual scaffolding behind options and forwards (no-arbitrage reasoning, payoff diagrams, put-call parity) explained in plain language before tackling denser texts. Less useful for a reader who already knows options mechanics and wants either trading rules or the full mathematical derivation of pricing models — for the latter, this text is explicitly a stepping stone to Wilmott's more advanced books.

## Related books in this library

- [[rubinstein-mark-rubinstein-on-derivatives]] — covers the same no-arbitrage and payoff-diagram territory in more depth, plus the binomial model and Black-Scholes derivation this sample doesn't reach.
- [[hull-options-futures-and-other-derivative-securities-5th-ed]] — the standard, more comprehensive derivatives textbook Wilmott himself cites as one of "the best books on options."
- [[black-scholes-option-pricing-model]] — a focused treatment of the pricing model this introductory text sets up but does not derive in the sampled chapters.
- [[chart-formations]] — a deeper dive into the chart patterns Wilmott surveys briefly and skeptically in Chapter 3.
