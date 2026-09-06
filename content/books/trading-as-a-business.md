---
author: Charlie Wright
category: Trend Following & Mechanical Systems
difficulty: intermediate
doc_type: book
one_liner: A TradeStation-based framework for building, testing, and money-managing
  mechanical trading strategies, run like a business rather than traded on prediction.
pages: 169
related:
- curtis-faith-way-of-the-turtle
- michael-covel-trend-following
- van-tharp-trading-systems
- money-management-report-van-tharp
- richard-l-weissman-mechanical-trading-systems
- trading-in-the-zone
reviewed_pdf_pages: 4, 23, 26, 31, 36, 40-41 (the entry-rule chapters, order-type
  ranking, T-Bill benchmark and the strategy-evaluation checklist)
slug: trading-as-a-business
source_file: Trading As A Business.pdf
source_review: partial
tags:
- strategy-development
- mechanical-trading
- money-management
- position-sizing
- backtesting
- tradestation
- trend-following
tier: A
title: Trading As A Business
year: unknown
---

## Overview

Charlie Wright argues that consistent trading profit comes from running a small business — designing and executing a rules-based strategy — rather than predicting the market. Built around TradeStation/EasyLanguage historical testing, the book moves from psychological principles through a four-stage trader-education model, a market-type taxonomy (trending, directionless, volatile), a strategy-design method built on "Set-Up" and "Entry," optimization and evaluation methodology, and a cash-management ("ANP Pyramid") position-sizing approach. Every claim is illustrated with real TradeStation code and Performance Summary output (Coca-Cola stock, Swiss Franc and S&P futures), making it unusually concrete and codeable.

## Core thesis

No one can reliably predict where or when the market will move; profitable trading instead comes from designing, backtesting, and mechanically executing a rules-based strategy with disciplined risk and cash management, then trusting the strategy (not personal judgment) to determine when to be long, short, or flat. Because a market must keep moving to survive (Steidlmayer's market-facilitation idea), a trend-following strategy that stays in the market cheaply during quiet periods will eventually catch the big move that produces most of its profit — so the trader's real job is minimizing losses and drawdown while waiting, not calling tops and bottoms.

## Key concepts

- **Four stages of trader education** — discretionary trader (intuition, hot tips, no rules) → technical trader (indicators applied inconsistently, "indicator fascination") → strategy trader (backtested, quantifiable rules) → complete strategy trader (rules plus disciplined cash management).
- **Market facilitation** — Peter Steidlmayer's idea that markets must keep moving to attract participants or they die; used to argue that a losing streak in a trend strategy cannot continue indefinitely.
- **Three market types** — trending (sustained directional moves), directionless (small sideways chop), volatile (sharp price jumps); each favors a different strategy style, and the same instrument can look like a different type depending on the chart's time frame.
- **Set-Up** — the condition(s) that make a trader aware a trade may be coming (e.g., a moving-average crossover, ADX trending, RSI overbought/oversold); a set-up alone does not trigger a trade.
- **Entry** — the separate technique that actually triggers the trade once a set-up is active; combining a set-up with a purpose-built entry is presented as the core innovation that turns a mediocre indicator into a workable strategy.
- **Entry Rule #1 and #2** — (1) price must confirm the set-up's direction before entry; (2) the entry must guarantee the strategy will catch every move it was designed for (no reliance on a pattern, like a key reversal, that might simply never occur).
- **MAXID / ROMID** — Maximum Intra-day Drawdown, treated as the trader's actual "investment" in a strategy, and Return On MAXID, the corresponding return-on-investment metric (margin is deliberately excluded from the investment figure).
- **ANP (Accumulated Net Profit) Pyramid** — a position-sizing method that risks a fixed percentage of a strategy's accumulated open profit (not original capital) per additional contract, so size grows and shrinks with profits while personal starting capital is never risked beyond one contract.
- **Contribution / fixed costs** — treating trading like a small business's income statement: variable costs (slippage, commission) reduce contribution, which must in turn cover fixed costs (data, software, office) before counting as profit.
- **Risk premium over T-Bills** — Wright's personal benchmark that a strategy must beat the 90-day T-Bill rate by a multiple (roughly 2× for stocks, 4× for futures) to justify the added risk of trading it.

## Rules and setups

The book teaches a *process* for building a strategy, not one fixed system. Core rules (fully detailed, with worked numbers, in the companion system page [[trading-as-a-business--set-up-and-entry-with-anp-pyramid]]):

1. **Entry must satisfy two rules** — price must move in the set-up's direction before entry (a bare market order fails unless conditioned); the entry must guarantee the strategy catches every move of the type it targets, rejecting any entry a strong trend could bypass entirely (e.g., a key reversal that never forms).
2. **Preferred order types, ranked** — stop orders (best) > Stop-Close-Only > conditioned market orders > limit orders (rejected outright: not guaranteed to fill and require price to move against the set-up).
3. **Failsafe entries** — add a secondary breakout trigger (e.g., a new 50-bar high/low) whenever the primary entry could fail to fire during an unusually strong trend.
4. **Money-management stop sizing** — set a per-contract stop by optimizing a range of distances and picking the level maximizing both Net Profit and ROMID; a stop hit much more than ~10% of the time is too tight.
5. **Strategy evaluation checklist** — beat the T-Bill rate by roughly 2× (stocks) or 4× (futures); require at least ~25–30 historical trades; verify the combined strategy beats each component (set-up alone, entry alone); treat drawdown exceeding ~2× the historical worst as a red flag.
6. **Largest-trade sanity check** — the largest winning trade should be no more than ~50% of gross profit or ~25% of net profit, or the strategy is fragile despite good aggregate statistics.

## Risk and money management

Wright treats money management, not the indicator or set-up, as the book's central differentiator. The mechanism (Chapter 9): fix a per-contract money-management stop by optimization; capitalize the account to at least 3× the strategy's historical MAXID plus margin before trading even one contract; trade one contract with personal capital; once Accumulated Net Profit (ANP) crosses a threshold set by a chosen risk percentage (his examples test 10–60% of ANP), add contracts funded only by that accumulated profit; drop back to one contract whenever ANP falls back toward zero. In his worked Swiss Franc example, moving from a flat one-contract strategy to the ANP Pyramid (20–50% of ANP, $4,000 stop) turned a strategy netting ~$90,000 over 15 years into one netting $300,000–$3.4 million, with correspondingly larger MAXID as the risk percentage rises — an explicit growth-versus-drawdown trade-off. Full mechanics and formulas are in [[trading-as-a-business--set-up-and-entry-with-anp-pyramid]].

## Psychology and discipline

Discipline is framed as doing the opposite of "human nature": buying high and exiting higher, selling low and exiting lower (since the 95% of traders who lose money are, by definition, doing what feels natural). Wright's central psychological rules: accept losses as an unavoidable cost of doing business (many top traders lose money on more than half their trades); do all analysis before the market opens and concentrate purely on execution during market hours; never fight the market or hold an opinion that overrides the strategy's signal; give a strategy a realistic time horizon based on its own historical loss streaks rather than judging it after a week or month; and always remain in position for trend strategies so the (unpredictable) big move is never missed while waiting.

## Chapter map

- Ch 1 — The Principles of Successful Trading — don't predict, don't fight the market, accept losses, use historical statistics, buy high/sell low.
- Ch 2 — The Path to Successful Trading — the four-stage trader-education model (discretionary → technical → strategy → complete strategy trader).
- Ch 3 — Markets, Strategies & Time Frames — the three market types and matching strategy styles and time frames.
- Ch 4 — Profile of a Winning Strategy — the Set-Up/Entry framework, the two entry rules, and the four order types, via a worked Coca-Cola example.
- Ch 5 — The Art of Strategy Design – In Theory — matching market type and time frame to the trader's own psychology.
- Ch 6 — The Art of Strategy Design – In Practice — a full worked example building a volatility-expansion strategy from an "up key reversal" pattern.
- Ch 7 — Optimization, The Double-Edged Sword — the case for cautious optimization/backtesting over "soft" predictive techniques (Elliott Wave, Gann, Market Profile).
- Ch 8 — The Science of Strategy Evaluation — MAXID/ROMID, the T-Bill risk-premium benchmark, and statistical criteria for judging a strategy.
- Ch 9 — Trading as a Business — cost accounting and the ANP Pyramid position-sizing method, via a Swiss Franc example.

## Strengths and caveats

The book's strength is unusual concreteness: every concept is shown as runnable EasyLanguage code with a real Performance Summary, and the ANP Pyramid and money-management-stop optimization are fully specified and codeable. It is explicitly TradeStation-centric — terminology (MAXID, ROMID, ANP, SPF/PS tables) and even the entry-order taxonomy assume that platform, and later editions of TradeStation or other platforms may not expose identical order types. The historical examples (Coca-Cola 1970–1997, Swiss Franc 1982–1997) predate decimalization, electronic execution, and modern slippage/liquidity conditions; the flat per-trade slippage/commission assumptions ($0–$100, 15–35 cents/share) are dated. The book is also a strong advocate for optimization as a legitimate practice and dismisses "soft" predictive methods (Elliott Wave, Gann, Market Profile) somewhat polemically, without engaging seriously with curve-fitting critiques beyond asserting that all investment analysis relies on historical data. No author biography, publisher, or copyright date is present in the source file, so the year above is left unknown.

## Who should read it

Traders who already have basic charting/indicator literacy and want a structured, TradeStation-flavored process for turning an idea into a backtested, risk-managed mechanical strategy — particularly the Set-Up/Entry design method and the ANP Pyramid position-sizing approach. Less useful for discretionary or pattern-based traders (Elliott Wave, Gann, candlestick) since the book explicitly argues against those approaches in favor of quantified, backtested rules.

## Related books in this library

- [[curtis-faith-way-of-the-turtle]] — another fully mechanical trend-following system with an explicit, business-like position-sizing framework.
- [[michael-covel-trend-following]] — broader survey of the trend-following philosophy this book's market-facilitation argument sits within.
- [[van-tharp-trading-systems]] — a complementary framework for evaluating whether a trading system fits the trader's own psychology and objectives.
- [[money-management-report-van-tharp]] — alternative position-sizing models to compare against the ANP Pyramid.
- [[richard-l-weissman-mechanical-trading-systems]] — a similar mechanical-systems-development approach with additional statistical validation methods.
