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

This is a workbook, not a narrative text: each of its 19 chapters follows a fixed template — a short summary, multiple-choice/calculation questions, a "media assignment" pointing to a web tool, a vocabulary list, and worked solutions. It companions Fontanills's full "Options Course" textbook, drilling the same core curriculum (contract mechanics, the Greeks, delta-neutral trading, spread construction) while also covering topics the flagship book treats more lightly: choosing a broker, how an order is processed on an exchange, margin mechanics, interest-rate/bond relationships, and screening for "explosive" opportunities. Since the strategy content overlaps substantially with [[fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed]], this page emphasizes the workbook's worked-formula drills and broker/margin/screening chapters, its most distinct contribution.

## Core thesis

Options mastery is built through repetition and self-testing, not just reading: understanding duration, direction, and magnitude of an anticipated move, and computing a spread's net credit/debit, maximum risk/reward, and breakevens from raw strike/premium inputs, are treated as mechanical skills to drill until automatic. The book repeatedly returns to delta-neutral trading — constructing positions so directional risk nets to zero and profit comes from volatility, time decay, or a large enough move either way — as more reliable than predicting direction. Around the strategy content, the workbook insists a trader's discipline (paper trading first, defining risk before every trade, preset exits, journaling emotions) determines outcomes as much as strategy selection.

## Key concepts

- **Delta neutral trade** — a position constructed so total position delta is at or near zero, removing directional bias; ATM options carry roughly ±50 delta, stock/futures carry a fixed ±100 delta per 100 shares/one contract.
- **Ratio spread** — an uneven number of same-underlying, same-expiration options bought and sold; a ratio *call spread* buys a lower-strike call and sells more higher-strike (OTM) calls, typically in a bearish-to-neutral market.
- **Ratio backspread** — the mirror construction: sell fewer near-the-money options, buy more further-OTM options (1:2 or 2:3 ratios common), for a net credit with unlimited profit beyond the long strikes and bounded risk in between; low-volatility markets call for a 0.75+ ratio, buying the lower strike and selling the higher.
- **Volatility skew (forward vs. reverse)** — forward: higher strikes carry higher implied volatility than lower strikes; reverse: the opposite. Backspreads are matched to whichever direction lets the strategist sell the relatively overpriced strike.
- **Butterfly / condor** — range-bound, limited-risk structures built from a "body" (short middle strikes) and "wings" (long outer strikes); profits when the underlying settles between the wings, loss capped at the net debit.
- **Calendar and diagonal spreads** — a long-dated and short-dated option (same strike for calendar, different for diagonal) profiting from faster near-term time decay.
- **Collar** — long stock plus a protective put financed by a short call: limited downside, limited upside.
- **Margin vs. cash trade** — a cash trade requires 100% up front (options must always be bought this way); a margin trade posts a percentage (historically 50% for stocks) and borrows the rest, amplifying gains and losses.
- **Momentum / contrarian screening** — technical, fundamental, and sentiment analysis as three lenses; sentiment tools (VIX, put/call ratios) are read contrarily — extreme bullishness signals bearishly.

## Rules and setups

The workbook's most concrete, codeable content is its worked spread-valuation formulas (drilled repeatedly across chapters) and a handful of explicit numeric screening rules:

1. **Ratio call spread valuation.** Net credit = (short premium × short contracts − long premium × long contracts) × 100; maximum reward = [long contracts × (strike difference + net credit)] × 100; maximum risk unlimited beyond the upside breakeven.
2. **Ratio put spread valuation.** Same credit formula; maximum profit = (strike difference + net credit) × 100; maximum risk limited (bounded by the underlying falling to zero).
3. **Ratio backspread valuation.** Net credit/debit = (short premium × short contracts − long premium × long contracts) × 100; maximum profit unlimited (calls) or bounded (puts); maximum risk = [(short contracts × strike difference) − net credit] × 100, occurring only if the underlying settles between strikes at expiration.
4. **Long butterfly/condor valuation.** Net debit = sum of long premiums minus short premium(s), × 100; maximum reward = (strike difference − net debit) × 100, with risk capped at the debit paid; a condor uses two different short strikes (four contracts) instead of one repeated strike.
5. **Ratio backspread market-selection rule.** Never place a backspread in a low-volatility market except with a 0.75-or-higher ratio, buying the lower strike and selling the higher.
6. **Explosive-opportunity screen.** Favor stocks with the greatest percentage rise in volume; price moves beyond 20% up or down (down moves as contrarian rebounds); strong/weak EPS growth and relative strength; or new 52-week highs/lows.
7. **Liquidity/price filters.** Avoid stocks under 300,000 shares/day for short-term trades; "low-priced" means under $20/share; a contrarian setup looks for stocks down 50%+ as rebound candidates.
8. **Account-level guardrails.** Paper trade a new strategy at least three months before going live; never invest all capital in one position; set profit and loss exits before entering.

## Risk and money management

The margin chapter gives concrete, if dated, figures: stock margin accounts historically allow borrowing up to 50% of a position's cash value; a margin call requires depositing funds within roughly one business day or the position is liquidated; naked option writing carries the highest margin requirement of any strategy discussed, while multi-leg, risk-defined combinations generally reduce margin versus their naked equivalents. Each stock option point of premium is worth $100/contract. Risk is framed mainly through position construction (limited-risk spreads, defined breakevens) rather than a fixed percent-of-account rule, though "Mastering the Market" stresses matching trade size to available time, capital, and risk tolerance, and treats a favorable reward-to-risk ratio with high win probability as the baseline test for a trade.

## Psychology and discipline

Discipline themes recur at both ends of the book: Chapter 1 opens with "start small, paper trade, define your risk before every trade," and the closing chapters return to the same points with more force. Fear and greed are named the primary saboteurs of a trading plan; the prescribed defense is deciding entry, profit-exit, and loss-exit points in advance so in-the-moment emotion has less room to override the plan. A trading journal — tracking not just trade mechanics but emotional state during each position — is recommended for self-diagnosis. The final chapter lists discipline, persistence, patience, independent thinking, contrarian thinking, self-honesty, and decisive execution as the seven traits the author considers necessary for long-term success.

## Chapter map

- Ch 1 — Options Trading: A Primer — duration/direction/magnitude framework, starting small.
- Ch 2 — The Big Picture — market structure orientation.
- Ch 3 — Option Basics — contract mechanics, terminology, American vs. European style.
- Ch 4 — Basic Trading Strategies — long calls/puts, covered and naked positions.
- Ch 5 — Introducing Vertical Spreads — ratio call/put spreads and backspreads, with valuation drills.
- Ch 6 — Demystifying Delta — delta-neutral construction basics.
- Ch 7 — The Other Greeks — gamma, theta, vega.
- Ch 8 — Straddles, Strangles, and Synthetics — nondirectional delta-neutral structures.
- Ch 9 — Advanced Delta Neutral Strategies — ratio spreads/backspreads and volatility skew in depth.
- Ch 10 — Range-Bound Markets — butterflies, condors, iron butterflies, calendars, diagonals, collars.
- Ch 11 — Adjustments — rebalancing a position back to delta neutral as the underlying moves.
- Ch 12 — Choosing the Right Broker — broker types, licensing, evaluation criteria.
- Ch 13 — Processing Your Trade — exchange order flow, order types, market makers/specialists.
- Ch 14 — Margin and Risk — margin mechanics, leverage, naked-writing risk.
- Ch 15 — Economic Analyses — interest rates, bond prices, and stock market relationships.
- Ch 16 — Mastering the Market — risk tolerance, exits, avoiding emotional trading.
- Ch 17 — Spotting Explosive Opportunities — fundamental/technical/sentiment screening rules.
- Ch 18 — Tools of the Trade — charting and research tools, avoiding "analysis paralysis."
- Ch 19 — Final Summary — trading-matrix strategy selection and closing psychology discussion.

## Strengths and caveats

The worked numeric examples (full solved formulas for spread valuations) are a genuinely useful self-check for anyone learning to compute credit, max risk/reward, and breakevens by hand — more drill-focused than most options texts. The broker-selection, order-processing, and margin chapters give concrete process detail many strategy-focused options books skip. Caveats: this is a 2005 workbook built around a 2004-era brokerage and exchange landscape — payment-for-order-flow practices, the exchange list, and the stated 50% margin figure may have shifted since; verify current rules with a broker rather than trust the figures as current. Much of the delta-neutral/Greeks content substantially duplicates [[fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed]] at shallower depth, so a reader who already owns that book gains little new strategy content beyond the exercises. Some referenced "free" web tools (CBOE calculator, Optionetics rankers) may no longer exist or work as described.

## Who should read it

Beginner-to-intermediate options traders who want a self-paced, drill-based way to internalize spread mechanics and valuation formulas, or anyone using it as a companion workbook alongside the full Options Course textbook. Less useful as a standalone strategy reference for depth on any single technique — for that, the parent book is the more complete source.

## Related books in this library

- [[fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed]] — the full textbook this workbook drills; read that book for depth on any strategy summarized here, and this one for the accompanying practice problems and the broker/margin/screening chapters it covers more thoroughly.
- [[black-scholes-option-pricing-model]] — background on the option-pricing math underlying the delta/Greeks calculations this workbook has readers compute by hand.
