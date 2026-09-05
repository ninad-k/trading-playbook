---
title: "The Options Course Workbook, 2nd Edition"
author: George A. Fontanills
year: 2005
slug: george-a-fontanills-the-option-course-with-exercise
tier: A
category: "Options, Futures & Derivatives"
tags: [options, workbook, delta-neutral, greeks, ratio-backspread, margin, broker-selection, technical-analysis]
difficulty: beginner
doc_type: course
pages: 237
one_liner: "A 19-chapter study workbook companion to The Options Course: chapter summaries, worked formula problems, and Q&A drills covering options basics through delta-neutral spreads, margin, and broker/tool selection."
related: [fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed, black-scholes-option-pricing-model]
source_file: "GEORGE A. FONTANILLS - The Option Course With Exercise.pdf"
---

## Overview

This is a workbook, not a narrative text: each of its 19 chapters follows a fixed template — a short summary, multiple-choice/fill-in/calculation questions, a "media assignment" pointing to a specific web tool, a vocabulary list, and worked solutions with discussion. It is the companion volume to Fontanills's full "Options Course" textbook, condensing and drilling the same core curriculum (contract mechanics, the Greeks, delta-neutral trading, spread construction) while also covering topics the flagship book treats more lightly: choosing a broker, how an order is processed on an exchange, margin mechanics, interest-rate/bond-market relationships, and screening for "explosive" opportunities. Because the strategy content overlaps substantially with [[fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed]], this page emphasizes the workbook's worked-formula drills and its broker/margin/screening chapters, its most distinct contribution.

## Core thesis

Options mastery is built through repetition and self-testing, not just reading: understanding duration (time to expiration), direction, and magnitude of an anticipated move, and being able to compute a spread's net credit/debit, maximum risk/reward, and breakevens from raw strike/premium inputs, are treated as mechanical skills to drill until automatic. The book repeatedly returns to delta-neutral trading — constructing positions so directional risk nets to zero and profit instead comes from volatility, time decay, or a large enough move in either direction — as the more reliable route to consistent returns than predicting market direction. Around the strategy content, the workbook insists a trader's discipline (paper trading first, defining risk before every trade, preset profit/loss exits, journaling emotions) determines outcomes as much as strategy selection does.

## Key concepts

- **Delta neutral trade** — a position (options/options or options/underlying) constructed so total position delta is at or near zero, removing directional bias; ATM options carry roughly ±50 delta, stock or futures carry a fixed ±100 delta per 100 shares/one contract.
- **Ratio spread** — an uneven number of same-underlying, same-expiration options bought and sold (all puts or all calls); a ratio *call spread* buys a lower-strike call and sells a greater number of higher-strike (OTM) calls, typically in a bearish-to-neutral market.
- **Ratio backspread** — the mirror construction: sell fewer near-the-money options and buy more further-OTM options (1:2 or 2:3 ratios common), aiming for a net credit with unlimited profit beyond the long strikes and bounded risk in between; the book's rule of thumb for a low-volatility market is to use a 0.75+ ratio, buy the lower strike, and sell the higher strike.
- **Volatility skew (forward vs. reverse)** — forward skew: higher-strike options carry higher implied volatility than lower strikes; reverse skew: the opposite. Ratio backspreads are best matched to the skew direction that lets the strategist sell the relatively overpriced strike.
- **Butterfly / condor / iron butterfly** — range-bound, limited-risk structures built from a "body" (short middle strikes) and "wings" (long outer strikes); the long butterfly profits when the underlying settles between the wings at expiration and losses are capped at the net debit paid.
- **Calendar and diagonal spreads** — combining a long-dated and short-dated option (same strike for calendar, different strikes for diagonal) to profit from faster time decay in the near-term short leg.
- **Collar** — long stock plus a protective put financed by a short call, giving limited downside and limited upside.
- **Margin vs. cash trade** — a cash trade requires 100% of the cost up front (options must always be bought this way); a margin trade lets a trader post a percentage (historically 50% for stocks under Federal Reserve/SEC rules) and borrow the rest, which amplifies both gains and losses.
- **Momentum / contrarian screening** — technical, fundamental, and sentiment analysis are presented as three distinct lenses; sentiment tools include the VIX, put/call ratios, and other crowd-psychology gauges used contrarily (extreme bullishness is read as a bearish signal, and vice versa).
- **R/R and probability framing** — every trade evaluation is framed around potential risk, potential reward, probability of success, and time-to-realize-the-return, echoing the book's repeated formula-driven approach to spread evaluation.

## Rules and setups

The workbook's most concrete, codeable content is its worked spread-valuation formulas (drilled repeatedly across chapters) and a handful of explicit numeric screening rules:

1. **Ratio call spread valuation.** Net credit = (short premium × short contracts − long premium × long contracts) × 100. Maximum reward = [long contracts × (strike difference + net credit)] × 100, realized if short options expire worthless and the long option is closed near the short strike. Maximum risk is unlimited beyond the upside breakeven.
2. **Ratio put spread valuation.** Same credit formula; maximum profit = (strike difference + net credit) × 100; maximum risk is limited (bounded by the underlying falling to zero).
3. **Call/put ratio backspread valuation.** Net credit/debit = (short premium × short contracts − long premium × long contracts) × 100. Maximum profit is unlimited (call backspread, upside) or large-but-bounded-by-zero (put backspread, downside); maximum risk = [(short contracts × strike difference) − net credit] × 100, occurring only if the underlying settles between the strikes at expiration.
4. **Long butterfly valuation.** Net debit = (sum of long premiums − 2 × short premium) × 100. Maximum reward = (difference between the short and outer strike − net debit) × 100; maximum risk is capped at the net debit paid; breakevens are the outer strikes adjusted by the net debit.
5. **Long condor valuation.** Same debit-based structure as the butterfly but with two different short strikes instead of one repeated short strike, so four separate contracts are involved.
6. **Ratio backspread market-selection rule.** Never place a ratio backspread in a low-volatility market unless following three specific rules: use a 0.75-or-higher ratio, buy the lower strike, sell the higher strike.
7. **Explosive-opportunity screen (six criteria).** Favor stocks showing (a) the greatest percentage rise in volume, (b) price increases greater than 20%, (c) price decreases greater than 20% (contrarian rebound candidates), (d) strong or weak EPS growth (for buying or selling respectively), (e) strong or weak relative strength, and (f) new 52-week highs or lows.
8. **Liquidity/price filters.** Avoid stocks trading under 300,000 shares daily for short-term trading; a "low-priced" market for options purposes trades under $20 a share; a contrarian setup looks for stocks down 50% or more (on the Price Percentage Losers list) as rebound candidates.
9. **Momentum threshold.** A single-day price move of 20% or more (up or down) is treated as a momentum signal; 60- and 90-day lookbacks are the book's stated windows for longer-term momentum.
10. **Account-level guardrails (echoed from the parent Options Course).** Paper trade any new strategy for at least three months before trading it live; never invest all trading capital in one position; set profit and loss exit points before entering a trade.

## Risk and money management

The workbook's margin chapter gives concrete, if dated, figures: stock margin accounts historically allow traders to borrow up to 50% of a position's cash value (per SEC/clearing-firm rules at the time of writing); a margin call requires depositing additional funds within roughly one business day or having the position liquidated; naked (uncovered) option writing carries the highest margin requirements of any strategy discussed, while multi-leg, risk-defined combinations generally reduce margin versus their naked equivalents. Each stock option point of premium is worth $100 per contract. The book frames risk management primarily through position construction (limited-risk spreads, defined breakevens) rather than a fixed percent-of-account rule, though its "Mastering the Market" chapter stresses matching trade size and risk to available time, capital, and personal risk tolerance, and treats a favorable reward-to-risk ratio with a high win probability as the baseline test for whether a trade is worth taking.

## Psychology and discipline

Discipline themes recur at both ends of the book: Chapter 1 opens with "start small, paper trade, define your risk before every trade," and the closing chapters return to the same points with more force. Fear and greed are named as the primary saboteurs of a trading plan; the workbook's prescribed defense is deciding entry, profit-exit, and loss-exit points in advance of every trade so that in-the-moment emotion has less room to override the plan. A trading journal — tracking not just trade mechanics but the trader's emotional state during each position — is recommended as a tool for self-diagnosis. The final chapter lists discipline, persistence, patience, independent thinking, contrarian thinking, self-honesty, and decisive execution as the seven traits the author considers necessary for long-term trading success.

## Chapter map

- Ch 1 — Options Trading: A Primer — duration/direction/magnitude framework, starting small, paper trading.
- Ch 2 — The Big Picture — market structure orientation.
- Ch 3 — Option Basics — contract mechanics, terminology, American vs. European style.
- Ch 4 — Basic Trading Strategies — long calls/puts, covered and naked positions.
- Ch 5 — Introducing Vertical Spreads — ratio call/put spreads and ratio backspreads with full valuation drills.
- Ch 6 — Demystifying Delta — delta neutral construction basics.
- Ch 7 — The Other Greeks — gamma, theta, vega.
- Ch 8 — Straddles, Strangles, and Synthetics — nondirectional delta-neutral structures.
- Ch 9 — Advanced Delta Neutral Strategies — ratio spreads/backspreads and volatility skew in depth.
- Ch 10 — Trading Techniques for Range-Bound Markets — butterflies, condors, iron butterflies, calendars, diagonals, collars.
- Ch 11 — Increasing Your Profits with Adjustments — rebalancing a position back to delta neutral as the underlying moves.
- Ch 12 — Choosing the Right Broker — broker types, licensing, evaluation criteria.
- Ch 13 — Processing Your Trade — exchange order flow, order types, market makers/specialists.
- Ch 14 — Margin and Risk — margin mechanics, leverage, naked-writing risk.
- Ch 15 — A Short Course in Economic Analyses — interest rates, bond prices, and stock market relationships.
- Ch 16 — Mastering the Market — risk tolerance, exits, avoiding emotional trading.
- Ch 17 — How to Spot Explosive Opportunities — fundamental/technical/sentiment screening rules.
- Ch 18 — Tools of the Trade — charting and research tools, avoiding "analysis paralysis."
- Ch 19 — Final Summary — trading-matrix strategy selection and closing psychology discussion.

## Strengths and caveats

The worked numeric examples (spread valuations with full solved formulas) are genuinely useful as a self-check for anyone learning to compute credit, max risk/reward, and breakevens by hand — more drill-focused than most options texts. The broker-selection, order-processing, and margin chapters give concrete process detail that many strategy-focused options books skip entirely. Caveats: the book is a 2005 workbook built around a 2004-era brokerage and exchange landscape — payment-for-order-flow practices, the specific list of U.S. options exchanges, and stated margin percentages (50%) may have shifted since publication, and readers should verify current rules with a broker rather than treat the figures as current. Much of the delta-neutral/Greeks content substantially duplicates [[fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed]] at a shallower level of depth, so a reader who already owns that book gains comparatively little new strategy content here beyond the exercises themselves. As with any workbook tied to "free" web tools (CBOE calculator, Optionetics rankers), some of the specific referenced tools and URLs may no longer exist or function as described.

## Who should read it

Beginner-to-intermediate options traders who want a self-paced, drill-based way to internalize spread mechanics and valuation formulas, or anyone using it explicitly as a companion/workbook alongside the full Options Course textbook. Less useful as a standalone strategy reference for a trader who wants deep coverage of any single technique — for that, the parent Options Course book is the more complete source.

## Related books in this library

- [[fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed]] — the full textbook this workbook drills; read that book for depth on any strategy summarized here, and this one for the accompanying practice problems and the broker/margin/screening chapters it covers more thoroughly.
- [[black-scholes-option-pricing-model]] — background on the option-pricing math underlying the delta/Greeks calculations this workbook has readers compute by hand.
