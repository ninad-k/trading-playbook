---
title: The Bible of Options Strategies
author: Guy Cohen
year: 2005
slug: guy-cohen-the-bible-of-options-strategies
tier: A
category: Options, Futures & Derivatives
tags: [options, spreads, straddles-strangles, iron-condors, synthetics, greeks, income-strategies, taxation]
difficulty: intermediate
doc_type: book
pages: 401
one_liner: "A 58-strategy options reference giving construction, Greeks, risk/reward, and exit rules for every strategy from a long call to iron condors and synthetics."
related: [fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed, lawrence-g-mcmillan-profit-with-options, george-m-jabbour-the-option-trader-handbook-strategies-and-trade-adjustments, hull-options-futures-and-other-derivative-securities-5th-ed, the-equity-options-strategy-guide]
source_file: "Guy Cohen The Bible of Options Strategies.pdf"
---

## Overview

This is a reference encyclopedia, not a narrative trading book. Cohen documents 58 options strategies grouped into seven families (the four basic positions, income strategies, vertical spreads, volatility strategies, sideways strategies, leveraged strategies, and synthetic strategies), plus a closing chapter on U.S. options taxation. Every strategy gets identical treatment: a proficiency rating, a market-outlook/volatility tag, a description with a diagram, step-by-step construction and exit rules, a "Context" block (outlook, rationale, net position, time-decay effect, holding period, stock/option-selection filters), a max-risk/max-reward/breakeven formula, a five-Greeks risk-profile diagram, advantages/disadvantages, and a worked numeric example. The book assumes the reader already knows what a call and a put are and wants a construction manual, not options theory.

## Core thesis

Every one of the 58 strategies is a variation on four building blocks (long call, short call, long put, short put) combined in different ratios, strikes, and expirations to produce a specific risk/reward shape suited to a specific market view (bullish, bearish, sideways) and volatility expectation (rising or falling). Choosing a strategy is a mechanical matching exercise: define the market outlook and volatility view first, then pick the strategy family whose risk profile fits, then apply Cohen's fixed selection filters (liquidity minimums, strike distance, days to expiration) to the specific trade.

## Key concepts

- **Proficiency rating** — each strategy is tagged novice/intermediate/advanced/expert by complexity and risk, not just mechanics (a naked short call is simple to place but rated advanced for its uncapped risk).
- **Net debit vs. net credit trade** — whether combined premiums paid exceed premiums received; sets the max-risk formula and whether time decay helps or hurts the position.
- **ITM / ATM / OTM** — in-, at-, and out-of-the-money strikes relative to the stock price; the book's primary strike-selection language.
- **The Greeks (five-pack)** — delta, gamma, theta, vega, rho shown as a labeled risk-profile diagram for every strategy.
- **Vertical spread** — two same-type, same-expiration options at different strikes (bull/bear call/put spreads); max risk and reward are both fixed by the strike gap.
- **Calendar and diagonal spreads** — a longer-dated option paired with a shorter-dated one, same strike (calendar) or different strikes (diagonal); the diagonal's deep-ITM long leg avoids the calendar's "right but still lose" risk shape.
- **Ratio spread / backspread** — unequal long/short option counts (2:1 or 3:2) trading a cheaper entry for uncapped risk (ratio spread) or uncapped reward with capped risk (backspread).
- **Butterfly / condor** — three- or four-strike, capped-risk, capped-reward structures; a condor separates the two middle strikes of a butterfly, widening the profit zone at a lower peak payout.
- **Iron butterfly / iron condor** — the same payoff shapes built by mixing puts and calls instead of one option type.
- **Synthetic position** — reproducing stock, straddle, or futures payoffs using only options, mainly for margin, tax, or execution reasons.
- **Collar** — long stock plus a protective long put financed by a covered short call; a long-dated, low-risk, low-return "insured" stock position.
- **"Steps In" / "Steps Out"** — Cohen's fixed template: the technical entry condition, and a trading-plan-driven exit rule.

## Rules and setups

Selection filters Cohen applies to nearly every strategy: minimum stock liquidity of 500,000 average daily volume; minimum option open interest of 100 (preferably 500); strikes and expirations chosen from a short list of standardized offsets rather than optimized per-trade.

Representative construction and risk/reward rules by family (all use the maximum-risk/reward formulas exactly as printed):

| Strategy | Legs | Max risk | Max reward | Typical holding period |
|---|---|---|---|---|
| Long call | Buy 1 call | Premium paid | Uncapped | 3+ months (avoid last month) |
| Covered call | Long stock + short 1 call | Stock cost − premium | (Strike − stock cost) + premium | Monthly, roll each expiration |
| Bull put spread | Short higher-strike put + long lower-strike put | Strike difference − net credit | Net credit | ≤1 month |
| Calendar call | Long far-dated call + short near-dated call, same strike | Net debit paid | Long call's residual value at short expiration − net debit | Long leg 6+ months, short leg ~1 month |
| Diagonal call | Long far-dated deep-ITM call + short near-dated OTM call | Net debit paid | Value at short strike − net debit | Long leg 6+ months, short leg ~1 month |
| Straddle / strangle (long) | Long 1 call + 1 put, same (straddle) or different (strangle) strikes | Combined premium | Uncapped | Before an expected volatility event |
| Long call/put condor | 4 strikes, buy outer 2, sell inner 2 | Net debit | Strike gap − net debit | ≤1 month, equidistant strikes |
| Call ratio backspread | Sell 1–2 lower-strike calls, buy 2–3 higher-strike calls (ratio ≤0.67 short:long) | Capped | Uncapped | High-volatility, directional |
| Long iron butterfly | Buy low put, sell mid put, sell mid call, buy high call | Net debit (or bounded) | Capped, often opened for a credit | ≤1 month |
| Collar | Long stock + long ATM/OTM put + short OTM call | Capped by put strike | Capped by call strike | 12–18 months, held near-to-expiration |

Cohen's worked example compares ratio constructions directly: a 2:1 call ratio backspread costing $0.10 net debit outperformed a 3:2 version netting a $2.30 credit but pushing the upper breakeven further out — his rule is to compare upper breakeven and max risk across ratios rather than default to whichever nets a credit.

## Risk and money management

Every strategy carries an explicit max-risk/max-reward/breakeven formula in terms of premiums and strike differences, not percent-of-equity sizing — the book gives no position-sizing or portfolio-level risk rule, leaving that to the reader's own trading plan, which Cohen references constantly but never specifies. Exits are strategy-specific: capped-risk positions (butterflies, condors, verticals) are typically held to expiration or unwound by reversing all legs; uncapped-risk positions (naked calls, short straddles/strangles, ratio spreads, ladders) need a hard stop-loss on the underlying since Cohen gives no other exit trigger. For credit and calendar-type income trades, time decay is the source of profit, so holding periods stay short (one month or less) to maximize theta while limiting uncapped-risk exposure to the same short window.

## Psychology and discipline

The book is procedural, not psychological — there is no dedicated chapter on trading psychology. The discipline message is indirect: every "Steps Out" section defers to "the rules defined in your Trading Plan," implying pre-committed rather than improvised entries and exits, and the proficiency-rating system itself warns novices and intermediates away from uncapped-risk strategies regardless of how simple their mechanics look. Cohen also repeatedly flags the "false economy" of short-dated long options or long-dated short options, using time-decay math as a check against intuitively appealing but mathematically poor structures.

## Chapter map

- Ch 1 — The Four Basic Options Strategies — long call, short call, long put, short put, with full Greeks and worked examples.
- Ch 2 — Income Strategies — covered call, naked put, bull put/bear call spreads, iron butterfly/condor, covered straddle/strangle, calendar and diagonal calls/puts, covered put.
- Ch 3 — Vertical Spreads — bull call, bear put, and call/put ladders (unbalanced verticals with uncapped risk or reward).
- Ch 4 — Volatility Strategies — straddle, strangle, strip, strap, guts, and short butterfly/condor variants (profit from a big move).
- Ch 5 — Sideways Strategies — short straddle/strangle/guts, long butterflies/condors, modified butterflies (profit from range-bound action).
- Ch 6 — Leveraged Strategies — call/put ratio backspreads and ratio spreads.
- Ch 7 — Synthetic Strategies — collar, synthetic call/put, synthetic straddles, synthetic futures, combos, and the box.
- Ch 8 — Taxation for Stock and Options Traders — U.S. capital-gains rules, wash sales, constructive sales, option holding-period and exercise tax treatment.
- Appendix A — Strategy Table — one-line construction/benefit/disadvantage summary for all 58 strategies (source of the "awkward to adjust" caveat on every butterfly/condor).
- Appendix B — Glossary.

## Strengths and caveats

The construction, risk/reward, and Greeks presentation is unusually consistent across all 58 strategies, making the book genuinely usable as a lookup reference rather than a cover-to-cover read. The taxation chapter is U.S.-only and uses pre-2008 rates (15%/35% long/short capital gains), dated and not reliable for current tax law. The book gives no portfolio-level risk framework, no position-sizing rule, and little on implied-volatility modeling — its Greeks diagrams are qualitative shapes, not a pricing tutorial, so readers needing options-pricing math (Black-Scholes, volatility skew) need a companion text. Butterflies and condors are repeatedly flagged by Cohen himself as "awkward to adjust," meaning the book's own stance is that these are hold-to-expiration trades, not actively managed positions.

## Who should read it

Traders who already understand call/put mechanics and want a single-volume construction manual for any of the 58 named strategies — how to build it, what it costs, its Greeks, and how to exit it. Less useful for traders wanting pricing theory, implied-volatility analysis, dynamic adjustment tactics, or portfolio-level risk management.

## Related books in this library

- [[fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed]] — another broad options-strategy course, useful for cross-checking construction rules and adding volatility-trading theory Cohen omits.
- [[lawrence-g-mcmillan-profit-with-options]] — deeper treatment of position adjustment and dynamic management, the gap this book's own "awkward to adjust" caveats point to.
- [[george-m-jabbour-the-option-trader-handbook-strategies-and-trade-adjustments]] — focused specifically on adjusting existing option positions, complementing this book's static construction-only approach.
- [[hull-options-futures-and-other-derivative-securities-5th-ed]] — the options-pricing and Greeks-mechanics theory this book assumes but never derives.
- [[the-equity-options-strategy-guide]] — a shorter, complementary strategy reference for cross-checking risk/reward formulas on the same core strategy set.
