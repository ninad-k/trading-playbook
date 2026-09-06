---
author: Larry Williams
category: Trend Following & Mechanical Systems
difficulty: intermediate
doc_type: book
one_liner: Builds a COT Index from the CFTC's Commitments of Traders report to gauge
  commercial hedgers' relative bullishness, and combines it with a trend filter into
  a complete trading method.
pages: 224
related:
- turtletrader
- van-tharp-trading-systems
- dynamic-breakout-ii-strategy
reviewed_pdf_pages: 3, 5, 7, 20, 22 (contents, the COT report structure, and the Public/Commercial
  index threshold rules)
slug: williams-larry-trade-stocks-and-commodities-with-the-insiders
source_file: Williams Larry - Trade Stocks and Commodities With the Insiders.pdf
source_review: partial
tags:
- cot-report
- commitments-of-traders
- commercials
- contrarian
- futures
- sentiment
- trend-filter
- smart-money
tier: A
title: 'Trade Stocks and Commodities with the Insiders: Secrets of the COT Report'
year: 2005
---

## Overview

Larry Williams (2005, Wiley Trading Series) builds a trading approach around the CFTC's weekly Commitments of Traders (COT) report, which discloses how much of the open interest in each futures market is held by "commercials" (hedgers using futures for their underlying business), large speculators, and small speculators. Williams argues commercials, as professionals hedging real production or inventory, are consistently on the right side of major turns, while the small-speculator "public" is consistently wrong. The book develops a normalized index of commercial and public positioning, shows how to read it across dozens of futures markets, and ends with a codified system — "The One-Minute Commodity Trader" — combining the index with a trend filter.

## Core thesis

Futures markets are a zero-sum transfer of wealth between three CFTC-tracked groups: commercials, large speculators, and small speculators. Commercials have structural information advantages (order flow, inventories, physical supply/demand) and are net right at extremes; the public is net wrong, driven by emotion. Because raw net-long/short numbers aren't comparable across time or market size, Williams normalizes each week's net position against its own three-year (or six-month) range to produce a 0-100% "COT Index" — how bullish current positioning is *relative to that group's own recent history*, not an absolute direction. Readings above roughly 80% (commercials) or 75% (public, inverted) mark extremes worth acting on; mid-range readings aren't tradable alone. Positioning extremes are not timing tools — they need a trend filter to become actionable, the basis of the system sub-page.

## Key concepts

- **Commitments of Traders (COT) report** — weekly CFTC disclosure of long/short/spread positions by category (commercial, large speculator, small speculator/"public") in each reportable futures market.
- **Commercials** — hedgers using futures to manage real business risk (producers, processors, merchants); treated as the "smart money" whose positioning contains information.
- **Public / small speculators** — non-reporting traders below CFTC size thresholds; treated as a contrarian indicator because they are structurally net wrong at extremes.
- **Large traders** — reporting speculators above CFTC size thresholds; discussed as a third group whose behavior is less reliably predictive than the commercials'.
- **COT Index** — the current week's net position normalized against the highest and lowest net position of a lookback window (3 years standard, 6 months for the One-Minute system), scaled 0-100%.
- **Open interest (OI)** — total outstanding futures contracts; used both raw and as a ratio (commercial position as % of total OI) to gauge how dominant commercials are in a given market.
- **Proxy index** — a COT-index-like measure built from price/volume/OI behavior for markets without COT reporting (e.g., pork bellies, some indexes, foreign markets).
- **WILLCO** — Williams' index built from the net difference in commercial positioning expressed as a stochastic-style oscillator, used similarly to the COT Index.
- **Preframing** — Williams' psychological technique of mentally rehearsing drawdowns in advance so real losing streaks don't trigger panic exits.
- **Trend filter** — a simple directional gate (e.g., a rising/falling multi-week moving average) used to decide whether to act only on COT buy signals (uptrend) or only on COT sell signals (downtrend).

## Rules and setups

**Public Index, Rule 1:** sell short when the public index is extremely bullish (roughly above 75%); buy long when extremely bearish (roughly below 25%).

**Public Index, Rule 2:** do the opposite of the public as a group — sellers signal buy, buyers signal sell.

**Commercial COT Index thresholds:** above 80% (3-year lookback) marks unusually heavy commercial buying and favors rallies; below 20% marks unusually heavy selling and favors declines. Williams stresses the index shows *what*, not *when* — it needs a trend filter (see the system sub-page, [[williams-larry-trade-stocks-and-commodities-with-the-insiders--one-minute-commodity-trader]]).

**COT Index formula:**
```
COT Index = [(This week's net position − Lowest net position in lookback) /
             (Highest net position in lookback − Lowest net position in lookback)] × 100
```
Standard lookback: 3 years. Faster variant used in the One-Minute system: 6 months.

**Open-interest ratio rule:** a commercial position exceeding roughly 55-60% of total open interest is treated as an extreme worth noting alongside the COT Index reading.

**Stop-loss/holding rules (Ch. 12), general-purpose:** trail longs at the lowest low of the last 17 trading days (highest high of 17 days for shorts, excluding inside days); after a stop-out, re-enter with the trend at the highest high of the last 13 days (lowest low for shorts); size stops by dollar risk, not chart features; few trends run past ~15 weeks without a significant correction.

**Gold-specific spread rule:** subtract a 3-week from a 21-week moving average of the gold/US-dollar-index spread; a reading above roughly 30% signals gold overbought vs. the dollar, favoring a decline within about six months — a positioning signal, not a short-term timing tool. Williams also cites his own 1973 seasonal research: gold tends to rally into July and top by December.

## Risk and money management

Williams treats stops as the central risk-management tool: their sole job is capping dollar loss, sized by the maximum acceptable loss rather than by chart geometry. He states plainly that stops cannot turn a losing system into a winning one — they only prevent catastrophic single-trade losses (he references his own history of margin calls before adopting disciplined stops). No fixed percent-of-equity risk-per-trade figure is given; position-sizing guidance is qualitative — avoid "plunging" (over-sized positions), his own worst historical habit. The COT Index is framed as a trade-selection filter, not a sizing input, and COT signals (especially from the public side) can be premature or wrong in isolation, which is why the culminating system layers a trend filter on top rather than trading the index alone.

## Psychology and discipline

A recurring theme is that most traders lose because of psychology, not signal quality: the public buys at emotionally exciting highs and sells at capitulation lows because risking money is emotional, most participants don't know "the rules of the game," and emotion overrides logic — precisely why public positioning is usable as a contrarian indicator. Williams introduces "preframing" — deciding in advance, at the start of each year, that a difficult drawdown period will occur, so it doesn't provoke a panic exit when it does. He warns against two failure modes: perpetual bearishness sold to a public that wants its fears confirmed, and "Cosmic Trader" belief systems (he singles out W. D. Gann-style narrative trading) that claim to explain all past price action while forecasting no better than chance. His takeaway: systems and rules are necessary to survive, but judgment is still required to recognize when a rule no longer applies.

## Chapter map

- Ch 1-3 — Meet Your New Investment Partner; Watching/Understanding the Commercials: introduces the COT report and CFTC reporting categories.
- Ch 4 — The COT Index: the normalized 3-year index and its 80%/20% levels.
- Ch 5 — For Every Insider There Is an Outsider: the Public Index and its two contrarian rules.
- Ch 6 — Large Traders: why this category is less predictive than commercials.
- Ch 7-9 — Volume and Open Interest chapters: OI-based extensions of the index; conventional OI "wisdom" tested and largely debunked.
- Ch 10 — A Unified Theory of COT Data: WILLCO and OI-as-percent-of-total constructs.
- Ch 11 — Using Commercials for Stocks: equity application and a proxy for non-COT markets.
- Ch 12 — Pointers and Thoughts on Trading: stop-loss philosophy, holding winners, preframing.
- Ch 13 — The One-Minute Commodity Trader: the trend + 6-month COT Index system (see sub-page); gold spread and seasonal notes.
- Ch 14-15 — Charts; Putting Theory to Work: chart-reading commentary and worked examples.

## Strengths and caveats

The COT Index's core logic — normalize positioning against its own recent range rather than reading absolute net-long/short figures — is a genuinely useful methodological point, presented with real historical charts across many markets. But most evidence in the book is anecdotal (chart examples chosen to illustrate a point) rather than a systematic backtest; the one quantified test given (Table 13.1: a handful of markets, 2000-2004) is small and short and should not be read as a validated edge. The book predates the CFTC's later disaggregated report categories (producer/merchant vs. swap dealer vs. managed money), which materially change how "commercial" positioning should be read in financialized markets post-2009. Williams is candid that no perfect system exists and his rules are meant to be overridden by judgment — honest, but it limits how mechanically the "system" can be coded and back-tested faithfully.

## Who should read it

Futures and commodity traders who want a sentiment/positioning layer to add to an existing trend-following or swing approach, and readers already familiar with Williams' other trend and pattern work who want the COT-specific piece of his toolkit. Less suited to pure equity traders (the stock-market application in Ch. 11 is a brief add-on) or to anyone wanting a fully mechanical, rigorously backtested system rather than a discretionary framework with illustrative examples.

## Related books in this library

- [[turtletrader]] — another trend-following futures framework; useful contrast between price-only trend rules and Williams' trend-plus-positioning approach.
- [[van-tharp-trading-systems]] — a general framework for defining and evaluating a trading system's components, applicable to formalizing the One-Minute Commodity Trader method.
- [[dynamic-breakout-ii-strategy]] — an alternative mechanical trend-filter (adaptive Donchian breakout) that could substitute for the 52-week moving-average filter used here.
