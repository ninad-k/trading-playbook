---
title: "Options: Essential Concepts and Trading Strategies"
author: "The Options Institute (Chicago Board Options Exchange)"
year: 1995
slug: options-essential-concepts-and-trading-strategies-2nd-edition
tier: A
category: "Options, Futures & Derivatives"
tags: [options, greeks, volatility, spreads, covered-call, market-making, institutional]
difficulty: intermediate
doc_type: book
pages: 449
one_liner: "CBOE Options Institute textbook covering option fundamentals, the Greeks and volatility, a strategy-by-strategy analysis framework, small-investor and institutional applications, and floor market-making."
related: [fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed, guy-cohen-the-bible-of-options-strategies, hull-options-futures-and-other-derivative-securities-5th-ed, lawrence-g-mcmillan-profit-with-options, mcgraw-hill-stock-options-and-the-new-rules]
source_file: "Options Essential Concepts and Trading Strategies, 2nd Edition.pdf"
---

## Overview

A multi-author textbook produced by The Options Institute, the educational division of the Chicago Board Options Exchange (CBOE), with each chapter written by a different CBOE instructor, floor trader, or academic. Second edition (1995) of a reference originally published 1990. The book is organized in three parts — Essential Concepts, Trading Strategies, and Real-Time Applications — moving from option pricing basics through individual strategy selection to institutional portfolio use and how CBOE market makers actually operate. It targets readers already comfortable with equities who want a systematic, non-mathematical grounding in options mechanics and strategy selection, not a quantitative pricing text.

## Core thesis

Options are best understood as tools for expressing a specific market opinion (direction, magnitude, and time frame) combined with a volatility view, and the "right" strategy is the one whose profit/loss profile, break-even, and risk match that opinion — not a universally superior strategy. The book repeatedly frames strategy choice as a structured selection process: form a view on price direction, expected volatility (implied vs. historical), and time horizon, then pick the position (from a basic long call to institutional collars) whose payoff matches all three.

## Key concepts

- **Delta** — the dollar change in an option's price for a $1 move in the underlying; calls have positive delta (0 to 1), puts have negative delta (0 to −1), and delta rises toward 1 (or −1) as an option moves further in-the-money.
- **Gamma** — the rate of change of delta itself as the underlying moves; measures how fast a hedged position can become unhedged, and is used by market makers to judge the stability of a delta-neutral hedge.
- **Vega** — sensitivity of an option's price to a change in implied volatility; a market maker can trade "vega neutral" to hedge out volatility exposure by spreading options against each other.
- **Theta** — the rate of time decay; in-the-money options retain intrinsic value, while at-the-money/out-of-the-money options lose 100% of premium if unprofitable at expiration.
- **Implied volatility (IV)** — the volatility figure that, plugged into a pricing model, reproduces an option's current market price; distinct from "expected volatility," which is a trader's own forecast, and from historical volatility.
- **Put-call parity** — the fixed pricing relationship linking a call, a put, and the underlying at the same strike/expiration; the book uses it to explain why option prices don't imply a price *direction* on their own.
- **Break-even point** — for a long call: strike + premium paid; for a short put: strike − premium received; central to the "opinion / selection / profit / loss / break-even" template the book applies to each strategy.
- **Covered call write** — selling a call against stock already owned, to collect premium in exchange for capping upside; "systematic writing" extends this into a rolling put-sell/call-sell cycle on assignment.
- **Protective put / collar (fence)** — buying a put (or a put plus selling a call to offset its cost) against a long stock position to define maximum downside.
- **Vertical spreads (bull/bear)** — buying and selling options of the same type and expiration at different strikes to cap both risk and reward relative to an outright long/short option.
- **Straddle / strangle / condor** — combinations for expressing a pure volatility view (straddle: same strike calls+puts; strangle: different strikes; condor: a "strangle with clipped wings," i.e., a defined-risk version).
- **VIX** — the CBOE's implied-volatility index, introduced in the book as a gauge of overall market volatility expectations (historical range cited: roughly 8% to over 100% across the prior eight years as of writing).
- **Delta-neutral / vega-neutral / gamma-neutral hedging** — the layered hedging approach professional market makers use to isolate (or eliminate) specific risk exposures in a book of option positions.

## Rules and setups

The book's core "rules" are a strategy-selection framework rather than a single tradable system with fixed entries/exits/stops — see Strengths and caveats for why no system sub-page was created for it. Its recurring, reusable template for evaluating any strategy (applied consistently across Chapters 4–7) is:

1. **Form a market opinion** — direction (bullish/bearish/neutral) and, separately, a volatility view (rising/falling/stable implied volatility).
2. **Match strike selection to conviction** — e.g., higher put strikes for short puts reflect a more bullish opinion; out-of-the-money calls are a more bullish (and more leveraged, more risky) bet than in-the-money calls because they need a larger underlying move to reach break-even.
3. **Choose the time frame** — from short-dated (weeks) tactical positions to six-month-plus strategic ones; longer-dated options are more sensitive to changes in implied volatility, shorter-dated options to time decay.
4. **Check the implied volatility level** before entry — the book stresses IV level matters more for some strategies (e.g., long premium positions) than others (e.g., deep in-the-money covered calls).
5. **Compute break-even, max profit, max loss** using each strategy's fixed formula (e.g., short put break-even = strike − premium received; max loss for a cash-secured short put = strike − premium, occurring if the underlying goes to zero).
6. **Consider expected frequency of use** — some strategies (e.g., liquidating an entire portfolio) are appropriate rarely; others (e.g., systematic covered-call writing) are meant to be run continuously.

No single stop-loss or position-sizing rule applies across strategies — each strategy's own defined max-loss (from its option/spread structure) functions as its risk boundary, per rule 5 above.

## Risk and money management

Risk in this book is defined structurally (per-strategy max loss, computed from the option payoff formula) rather than through account-level position sizing rules. For institutional applications (Chapter 7), the book illustrates comparing multiple protective strategies (e.g., buying out-of-the-money puts as portfolio insurance vs. a collar) side by side across a grid of index price scenarios, selecting based on which strategy's percent-change profile best matches the portfolio manager's risk tolerance and cost budget — cost of insurance (premium paid) is treated as the central trade-off against the amount of downside protection obtained. For market makers (Chapter 8), risk management means holding a book delta-, gamma-, and vega-neutral (or deliberately taking on only the specific exposure wanted) through continuous rehedging as the underlying price, time, and implied volatility all change.

## Psychology and discipline

The book is a mechanics/strategy reference, not a psychology-focused text, so this section is thin in the source material. The clearest discipline-adjacent point is a caution to option buyers: cheaper, further out-of-the-money options look attractive on a percentage-return basis (a trader can buy more contracts for the same dollar outlay) but this "emphasis on quantity" reasoning is flagged as a trap — such options require a larger move to reach break-even and lose 100% of premium if that move doesn't happen, so their apparent leverage advantage overstates their real risk-adjusted attractiveness.

## Chapter map

- Ch 1 — History of Options — origins of options trading, pre-CBOE OTC put/call dealer market, 1930s regulatory history.
- Ch 2 — Fundamentals of Options — option definitions, delta, put-call parity, basic position payoffs.
- Ch 3 — Volatility Explained — historical vs. implied vs. expected volatility, how implied volatility is derived from option price.
- Ch 4 — Option Strategies: Analysis and Selection — the opinion/selection/profit/loss/break-even framework applied across basic long/short calls and puts.
- Ch 5 — New Product Strategies — strategies using newer listed products of the time (index options, LEAPS), including the VIX.
- Ch 6 — Option Strategies for the Small Investor — covered call writing, systematic writing, protective puts, collars/fences for individual investors.
- Ch 7 — Institutional Uses of Options — portfolio-level hedging comparisons (selling the portfolio, protective puts, collars) for institutional risk management.
- Ch 8 — The Business of Market Making — how CBOE floor market makers price and hedge (delta/gamma/vega-neutral trading), and why floor trading is not "in competition" with off-floor traders.
- Ch 9 — Using Option Market Information to Make Stock Market Decisions — put-call ratio, option premium level, and implied volatility (VIX) as market-sentiment indicators.
- Ch 10 — Institutional Case Studies — two worked cases: portfolio-manager use of options for risk management, and an investment trust seeking trustee approval for derivatives use.

## Strengths and caveats

The book's strength is its consistent, reusable strategy-analysis template (opinion, strike selection, time frame, IV level, break-even/profit/loss) applied across a wide range of strategies from basic to institutional, making it easy to compare strategies on the same footing. Its dated elements: it predates decimalized option pricing (quotes shown in fractions, e.g., "4 1/4," "1 15/16"), references now-superseded product/market structure details (e.g., early VIX history, pre-portfolio-margin capital treatment), and several named strategies (e.g., large-scale portfolio insurance case studies) reflect mid-1990s institutional practice. Because the strategy-selection guidance in Chapter 4 and Chapter 7 is a decision framework (compare opinion/time frame/IV level across strategies) rather than a fully specified tradable system with concrete entry triggers, position sizing, and stop rules, no system sub-page was created for it per this library's criteria — see the parent brief's note that system pages require a complete, codeable ruleset.

## Who should read it

Traders and investors who already understand basic equities and want a structured, non-mathematical reference for how each standard option strategy's risk/reward is built, how to select a strategy that matches a market view, and how professional market makers and institutions actually use and hedge options.

## Related books in this library

- [[fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed]] — another broad options-strategy reference, useful for cross-checking strategy definitions and risk profiles.
- [[guy-cohen-the-bible-of-options-strategies]] — a strategy-by-strategy options reference to compare against this book's opinion/selection framework.
- [[hull-options-futures-and-other-derivative-securities-5th-ed]] — the standard quantitative derivatives text, useful as the mathematical complement to this book's non-mathematical treatment of the Greeks and volatility.
- [[lawrence-g-mcmillan-profit-with-options]] — a practitioner-oriented options strategy book for comparing selection criteria and real-world position management.
- [[mcgraw-hill-stock-options-and-the-new-rules]] — another options strategy reference for cross-referencing strategy mechanics.
