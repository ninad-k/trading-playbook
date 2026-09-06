---
author: Lawrence G. McMillan
category: Options, Futures & Derivatives
difficulty: intermediate
doc_type: book
one_liner: 'McMillan''s applied option-strategy text: reading options as sentiment
  indicators, selecting strategies by where implied volatility sits versus its own
  history, and mechanical system trading.'
pages: 286
related:
- guy-cohen-the-bible-of-options-strategies
- fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed
- hull-options-futures-and-other-derivative-securities-5th-ed
- george-m-jabbour-the-option-trader-handbook-strategies-and-trade-adjustments
reviewed_pdf_pages: 4-5, 7, 29 (the volatility-percentile methodology chapters and
  the strategy-selection rules)
slug: lawrence-g-mcmillan-profit-with-options
source_file: LAWRENCE G. McMILLAN - Profit With Options.pdf
source_review: partial
tags:
- options
- implied-volatility
- straddles
- contrary-indicators
- put-call-ratio
- system-trading
- hedging
tier: A
title: Profit With Options
year: 2002
---

## Overview

Lawrence McMillan, author of the reference text *Options as a Strategic Investment* and publisher of an options newsletter and daily fax service, wrote this book (part of the Wiley Trading / Marketplace Books series, structured with review questions like a course text) to teach applied option strategy rather than fresh theory. It works through four uses of options: as direct technical indicators (implied volatility and volume as signals), as contrary sentiment indicators (put-call ratios, $VIX), as inputs to mechanical trading systems, as stock-portfolio insurance, and — the book's centerpiece — as a volatility-trading vehicle, where the strategy chosen (buy or sell premium, and which structure) is driven entirely by where current implied volatility sits relative to its own historical range.

## Core thesis

Option prices (implied volatility) carry two kinds of usable information: sentiment (extreme option buying/selling reveals crowd positioning, useful as a contrarian signal) and value (options are objectively cheap or expensive relative to their own trading history, not relative to some universal "normal" level, since different underlyings trade at structurally different implied volatility levels). A trader who measures where current implied and historical volatility rank against their own multi-month or multi-year range — rather than simply comparing implied to historical — has a real, testable edge for choosing between volatility-buying strategies (straddles, backspreads) and volatility-selling strategies (strangle sales, ratio spreads, credit spreads).

## Key concepts

- **Implied volatility (IV)** — the volatility level an option's market price implies through an option-pricing model; rises as options get more expensive.
- **Historical volatility (HV)** — realized volatility of the underlying computed directly from past price data, typically compared across 10-, 20-, 50-, and 100-day windows.
- **Percentile/decile ranking** — placing today's IV (and HV) reading against the last 200–600+ daily readings for the same underlying to judge "cheap" versus "expensive" objectively.
- **Volatility skew** — the pattern of IV across strikes (forward/positive skew: higher strikes more expensive, typical of commodities; reverse/negative skew: lower strikes more expensive, typical of equity indexes).
- **Contrary indicator** — a sentiment measure (put-call ratio, $VIX) that signals the opposite of what the crowd is doing once it reaches an extreme.
- **Put-call ratio** — daily put volume ÷ call volume for a stock, index, or futures market; smoothed with a moving average and read as a contrarian extreme.
- **Ever probability vs. closing probability** — the (much higher) probability an underlying ever touches a target price before expiration, versus the (lower) probability it closes beyond that price at expiration; computed via Monte Carlo simulation, not the option's delta (which only gives the closing probability).
- **Straddle / strangle** — simultaneous long (or short) call and put, same (straddle) or different (strangle) strikes; the book's primary volatility-buying and volatility-selling vehicles.
- **Backspread / ratio spread** — unequal numbers of long vs. short options at different strikes, used respectively to buy or sell volatility while exploiting a skew.
- **Event-driven straddle** — a straddle bought just before a known binary event (earnings, litigation ruling) to profit from the resulting price gap.

## Rules and setups

Full volatility-based strategy-selection rules (with exact percentile thresholds and follow-up actions) are on the linked system page. In summary:

1. **Rank, don't just compare**: measure both IV and HV against their own multi-month/year percentile history before concluding options are cheap or expensive — a raw IV-vs-HV gap alone is misleading (e.g. OEX structurally trades at higher IV than its HV).
2. **Cheap options (IV in the ~10th percentile or lower)**: favor straddle buying or backspreads (buy volatility), subject to the four straddle-buying criteria in the system page.
3. **Expensive options (IV in the ~90th percentile or higher)**: favor strangle/combination sales or ratio spreads (sell volatility) — confined mainly to index options or stocks where the news causing the spike is already known.
4. **Contrary sentiment**: read extreme put-call ratios and $VIX spikes as reversal signals — buy when the crowd is extremely bearish (high put-call ratio, IV spike into a decline), sell/fade when extremely bullish.
5. **System trading**: any mechanical system needs explicit, pre-defined entry rules, exit rules, and a stop sized to the market's volatility (not an arbitrary dollar amount) — and the discipline to follow the system through its worst historical drawdown without overriding it.

## Risk and money management

Naked option selling (strangles, naked puts) carries theoretically large or unlimited loss and is explicitly discouraged on individual stocks (gap risk from takeovers, earnings, litigation) — McMillan confines volatility-selling largely to broad index options, where single-name gap risk doesn't apply. Backspreads are structured to collect a net credit at initiation so there is always some profit potential on the "wrong" side even if the anticipated move doesn't happen. For system trading, stops must be volatility-scaled (e.g. a point stop sized to the market's typical daily range) rather than fixed, and a system's historical maximum drawdown must be survivable on the capital actually allocated to it. Margin for naked index option sales should be over-allowed beyond the exchange minimum, sized to what would be required if the underlying moved to the strike, not just the current out-of-the-money margin.

## Psychology and discipline

McMillan's most repeated caution is skepticism about why options are cheap or expensive before trading the number: expensive options with no visible news may reflect insider information about a pending takeover or earnings surprise, and cheap options after a cash-tender bid are cheap for a legitimate structural reason (the stock won't move), not a mispricing to exploit. He also warns that straddle buying is often "watching paint dry" — long stretches with no move — and that traders abandon a statistically sound strategy out of boredom or impatience before it has a chance to pay off. For system trading, the chapter is explicit that the hardest part is not designing rules but obeying them exactly through a live drawdown, since emotional overrides are what turn a profitable system into a losing one.

## Chapter map

- Ch 1 — Introduction — option terminology, pricing components, historical vs. implied volatility basics.
- Ch 2 — Options as Direct Indicators — reading price and volume in the options market itself as a signal (insider-activity screening, event-driven straddles).
- Ch 3 — Options as Contrary Indicators — put-call ratios, $VIX, and implied volatility as contrarian sentiment gauges.
- Ch 4 — System Trading — choosing/building a mechanical system, drawdown tolerance, worked short-term and intermediate-term system examples.
- Ch 5 — Protecting a Stock Portfolio — protective puts, collars, and other portfolio-insurance structures.
- Ch 6 — Trading Volatility — volatility skew, call/put backspreads and ratio spreads for exploiting it.
- Ch 7 — Buy Low and Sell High—Volatility, That Is — the percentile method, straddle-buying criteria, and naked-option-selling criteria (this book's core system).

## Strengths and caveats

The book's percentile-based, quantified approach to "cheap vs. expensive" options is more rigorous and more actionable than most volatility-trading writing, and its Monte Carlo "ever vs. closing probability" distinction is a genuinely useful correction to naive delta-as-probability reasoning. It assumes access to historical IV/HV databases and option-evaluation or Monte Carlo software (McMillan points readers to his own firm's website and paid tools) that a self-directed reader must source elsewhere today. Several worked examples use 1990s option chains, index levels, and margin rules that are dated; the underlying percentile method still applies. As with most option-selling literature, the naked-selling chapters understate tail risk relative to what live trading experience (and the book's own acknowledgment of "eight standard deviation" daily moves) would suggest.

## Who should read it

Traders who already understand basic option mechanics (calls, puts, strike, expiration, delta) and want a systematic framework for choosing between buying and selling volatility, plus a primer on reading options-market sentiment as a contrarian signal. Less useful as a first options book — it assumes the reader can price and evaluate options already, unlike a pure strategy-mechanics primer.

## Related books in this library

- [[guy-cohen-the-bible-of-options-strategies]] — a broader catalogue of option structures for readers who need the mechanics McMillan assumes as background.
- [[fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed]] — another applied options strategy text covering similar ground for comparison.
- [[hull-options-futures-and-other-derivative-securities-5th-ed]] — the standard academic reference for the option-pricing theory McMillan applies but doesn't derive.
- [[george-m-jabbour-the-option-trader-handbook-strategies-and-trade-adjustments]] — practical follow-up on adjusting option positions once established, a topic this book only touches on.
