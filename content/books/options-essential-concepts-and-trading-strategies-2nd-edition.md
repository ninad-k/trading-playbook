---
author: The Options Institute (Chicago Board Options Exchange)
category: Options, Futures & Derivatives
difficulty: intermediate
doc_type: book
one_liner: CBOE Options Institute textbook covering option fundamentals, the Greeks
  and volatility, a strategy-by-strategy analysis framework, small-investor and institutional
  applications, and floor market-making.
pages: 449
related:
- fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed
- guy-cohen-the-bible-of-options-strategies
- hull-options-futures-and-other-derivative-securities-5th-ed
- lawrence-g-mcmillan-profit-with-options
- mcgraw-hill-stock-options-and-the-new-rules
reviewed_pdf_pages: 4-5, 182 and the strategy-selection chapters checked against the
  note's claims (Greeks definitions, VIX range, strategy-selection framework)
slug: options-essential-concepts-and-trading-strategies-2nd-edition
source_file: Options Essential Concepts and Trading Strategies, 2nd Edition.pdf
source_review: partial
tags:
- options
- greeks
- volatility
- spreads
- covered-call
- market-making
- institutional
tier: A
title: 'Options: Essential Concepts and Trading Strategies'
year: 1995
---

## Overview

A multi-author textbook produced by The Options Institute, the educational division of the Chicago Board Options Exchange (CBOE), with each chapter written by a different CBOE instructor, floor trader, or academic. Second edition (1995) of a reference originally published 1990. The book is organized in three parts — Essential Concepts, Trading Strategies, and Real-Time Applications — moving from option pricing basics through individual strategy selection to institutional portfolio use and how CBOE market makers actually operate. It targets readers already comfortable with equities who want a systematic, non-mathematical grounding in options mechanics and strategy selection, not a quantitative pricing text.

## Core thesis

Options are best understood as tools for expressing a specific market opinion (direction, magnitude, and time frame) combined with a volatility view, and the "right" strategy is the one whose profit/loss profile, break-even, and risk match that opinion — not a universally superior strategy. The book repeatedly frames strategy choice as a structured selection process: form a view on price direction, expected volatility (implied vs. historical), and time horizon, then pick the position (from a basic long call to institutional collars) whose payoff matches all three.

## Key concepts

- **Delta** — dollar change in an option's price for a $1 move in the underlying; calls 0 to 1, puts 0 to −1, rising toward 1 (or −1) as an option moves further in-the-money.
- **Gamma** — the rate of change of delta itself; measures how fast a hedged position can become unhedged, used to judge the stability of a delta-neutral hedge.
- **Vega** — sensitivity of price to a change in implied volatility; market makers trade "vega neutral" by spreading options against each other.
- **Theta** — rate of time decay; in-the-money options retain intrinsic value, while at-/out-of-the-money options lose 100% of premium if unprofitable at expiration.
- **Implied volatility (IV)** — the volatility figure that, plugged into a pricing model, reproduces an option's current market price; distinct from a trader's own "expected volatility" forecast and from historical volatility.
- **Put-call parity** — the fixed pricing relationship linking a call, a put, and the underlying at the same strike/expiration; explains why option prices don't imply a price *direction* on their own.
- **Break-even point** — e.g., long call: strike + premium paid; short put: strike − premium received; central to the opinion/selection/profit/loss/break-even template applied to each strategy.
- **Covered call write** — selling a call against owned stock to collect premium in exchange for capped upside; "systematic writing" extends this into a rolling put-sell/call-sell cycle on assignment.
- **Protective put / collar (fence)** — a put (or a put plus a written call to offset its cost) against long stock to define maximum downside.
- **Vertical spreads (bull/bear)** — same-type, same-expiration options at different strikes, capping both risk and reward versus an outright position.
- **Straddle / strangle / condor** — combinations for a pure volatility view (straddle: same strike; strangle: different strikes; condor: a defined-risk "strangle with clipped wings").
- **VIX** — the CBOE's implied-volatility index, a gauge of market volatility expectations (cited historical range: roughly 8% to over 100% in the prior eight years).
- **Delta/vega/gamma-neutral hedging** — the layered approach market makers use to isolate or eliminate specific risk exposures in a book of positions.

## Rules and setups

The book's core "rules" are a strategy-selection framework rather than a single tradable system with fixed entries/exits/stops — see Strengths and caveats for why no system sub-page was created. Its recurring template, applied across Chapters 4–7:

1. **Form a market opinion** — direction (bullish/bearish/neutral) and, separately, a volatility view.
2. **Match strike selection to conviction** — e.g., higher put strikes for short puts reflect more bullishness; out-of-the-money calls are more bullish and riskier than in-the-money calls since they need a larger move to reach break-even.
3. **Choose the time frame** — weeks to six-months-plus; longer-dated options are more sensitive to IV changes, shorter-dated ones to time decay.
4. **Check the IV level** before entry — matters more for long-premium positions than, say, deep in-the-money covered calls.
5. **Compute break-even, max profit, max loss** from each strategy's fixed formula (e.g., cash-secured short put max loss = strike − premium, at underlying = zero).
6. **Consider frequency of use** — some strategies (liquidating a portfolio) are rare; others (systematic covered-call writing) run continuously.

No stop-loss or position-sizing rule applies across strategies; each strategy's own defined max-loss is its risk boundary (rule 5).

## Risk and money management

Risk is defined structurally (per-strategy max loss from the payoff formula) rather than through account-level sizing rules. For institutions (Chapter 7), the book compares protective strategies (e.g., out-of-the-money puts vs. a collar) across a grid of index price scenarios, selecting by which percent-change profile best matches risk tolerance and cost budget — premium paid is the central trade-off against downside protection obtained. For market makers (Chapter 8), risk management means holding a book delta-, gamma-, and vega-neutral (or deliberately keeping only the wanted exposure) through continuous rehedging as price, time, and IV change.

## Psychology and discipline

Thin in the source material, since this is a mechanics/strategy reference rather than a psychology text. The clearest discipline point: cheaper, further out-of-the-money options look attractive on a percentage-return basis (more contracts for the same outlay), but this "emphasis on quantity" is flagged as a trap — such options need a larger move to break even and lose 100% of premium otherwise, so their apparent leverage overstates real risk-adjusted attractiveness.

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
