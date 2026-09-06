---
author: George A. Fontanills
category: Options, Futures & Derivatives
diagram: option-payoffs
diagram_caption: The payoff shapes the course builds on.
difficulty: intermediate
doc_type: book
one_liner: 'Full options curriculum built around delta-neutral trading: Greeks, straddles/strangles,
  ratio backspreads, and range-bound spreads, each with numbered entry/adjustment/exit
  road maps.'
pages: 592
related:
- black-scholes-option-pricing-model
- using-options-to-buy-stocks-build-wealth-with-little-risk-and-no-capital
- introduction-to-arbitrage-pricing-of-financial-derivatives
reviewed_pdf_pages: 4, 7-8, 503-511 (contents, the Greeks chapters and the strategy-review
  appendix with its risk/reward formulas)
slug: fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed
source_file: Fontanills - The Options Course - High Profit And Low Stress Trading
  Methods, 2nd Ed.pdf
source_review: partial
tags:
- options
- delta-neutral
- greeks
- spreads
- volatility
- ratio-backspread
- straddle
- money-management
tier: A
title: 'The Options Course: High Profit & Low Stress Trading Methods'
year: 2005
---

## Overview

Fontanills, co-founder of Optionetics, wrote this as a soup-to-nuts options curriculum: contract mechanics, the Greeks, and a large catalog of strategies, organized around a central idea — delta-neutral trading — rather than around directional forecasting. The 2nd edition (2005) walks from basic calls/puts through vertical spreads, straddles/strangles, ratio backspreads, and range-bound (premium-selling) structures, then covers order execution, margin, macro analysis, and stock-screening technique. It reads as a course text: each strategy gets a definition, a worked numeric example, a risk graph description, and — usefully — a numbered "road map" of guidelines for entering, monitoring, and exiting the position.

## Core thesis

Directional forecasting is a low-edge game; a trader's real edge comes from mispriced volatility and structuring trades so that the position's delta (directional exposure) starts at or near zero. A delta-neutral trader combines options (and sometimes stock/futures) in ratios that offset directional risk, profits from time decay or volatility change instead of correct market-direction guessing, and mechanically rebalances ("adjusts") the position back toward zero delta as the underlying moves. Consistent profitability is process-driven: use option pricing math (the Greeks) to quantify risk before placing a trade, follow a fixed set of entry/exit rules, and treat volatility — not price direction — as the primary variable to trade.

## Key concepts

- **Delta** — sensitivity of an option's price to a $1 move in the underlying; also interpreted as the option's approximate probability of expiring in-the-money. ATM options ≈ ±50 delta; 100 shares of stock or one futures contract = ±100 delta (fixed, non-adjustable).
- **Gamma** — the rate of change of delta per $1 move in the underlying ("the delta of the delta"); largest for at-the-money options and grows as expiration nears.
- **Theta** — daily time decay of an option's premium, expressed as a negative number; largest for ATM options close to expiration.
- **Vega** — sensitivity of an option's price to a 1-point change in implied volatility; largest for options far from expiration.
- **Delta neutral trading** — combining long/short options (and stock/futures) so the position's net delta is zero, removing directional bias and isolating profit to volatility and time.
- **Implied volatility (IV) vs. statistical/historical volatility (SV)** — IV is the market's priced-in expectation of future movement (from an option's market price via a pricing model); SV is the annualized standard deviation of past price changes. Comparing IV to SV signals whether options are cheap or expensive.
- **Volatility skew** — a time skew (front-month IV differs sharply from back-month IV) or a price skew (forward: higher strikes carry higher IV; reverse: lower strikes carry higher IV), each favoring different spread structures.
- **Straddle/strangle** — buying (or selling) a call and put at the same (straddle) or different (strangle) strikes and the same expiration to trade an expected volatility change rather than direction.
- **Ratio backspread** — selling fewer near-the-money options and buying more further-dated/further-out options in a ratio (e.g., 1×2, 2×3) that can be placed for a net credit or near-zero debit, capping risk in the middle and leaving unlimited profit potential in the anticipated direction.
- **Adjustment** — buying/selling stock or options mid-trade to bring a position's delta back to zero and lock in partial profit as the underlying moves.
- **Vertical, calendar, and diagonal spreads** — combining options at different strikes (vertical), same strike/different expirations (calendar), or both (diagonal) to define risk and exploit time decay or skew.
- **Butterfly, condor, and iron condor/butterfly** — limited-risk, limited-reward structures (a body plus wings) built to profit when the underlying stays within a range through expiration.
- **Collar** — long stock plus a protective put and a covered call, financing downside protection with capped upside.

## Rules and setups

The book gives strategy-specific numeric "road maps" (14-step guideline lists per spread) rather than one universal rule set; the most portable, codeable rules:

1. **Delta neutral entry.** Build the trade so opening deltas net to zero: e.g., long 200 shares (+200 delta) offset by 4 long ATM puts or 4 short ATM calls (4 × ∓50 = ∓200).
2. **Delta-based adjustment trigger.** Monitor the combined position delta continuously; when it drifts to a predetermined threshold (the book uses ±100 as the default), buy or sell stock/options to bring it back to zero. This can be pre-calculated at the start of the day and set as standing orders.
3. **Straddle/strangle timeframe.** Use options with 30–90+ days to expiration (author prefers ~90); avoid short-dated straddles because non-linear time decay erodes them too fast. Exit straddles well before expiration — 30+ days out — rather than holding to expiry.
4. **Ratio backspread construction.** Sell the near strike, buy a larger number of the farther strike (same expiration), using ratios that are multiples of 1:2 or 2:3; avoid ratios above 0.67 unless trading a slow market (then 0.75+ is acceptable but carries more risk). Prefer options with 90+ days to expiration; favor medium-priced underlyings ($25–$75) with a reverse skew (call backspread) or forward skew (put backspread) so the short leg is relatively overpriced.
5. **Ratio backspread exit.** Close if the short leg has ≤¼ point of time value remaining (assignment risk); take profit on part of the position once gains reach ~50%+ and hold the remainder "for free"; close the whole spread inside the breakevens with 30 days or less left unless conviction is high; let the position expire worthless if price is beyond the favorable breakeven.
6. **Range-bound spreads (butterfly/condor/calendar/diagonal).** Enter when expecting the underlying to stay between the breakevens; use options with ≤45 days to expiration for butterflies; place as a single multi-leg limit order (never leg in/out); plan the exit before entry (let expire worthless outside the profit zone, or close near the short strike for maximum profit).
7. **General exit discipline.** Exit most premium trades ~30 days before expiration unless the position's profit depends on a short option expiring worthless.
8. **Screening rule ("Five Minute Success Formula").** Look for stocks moving ≥30% intraday on volume >300,000 shares (ideally >1 million), confirm the move has an identifiable news catalyst, verify liquid options exist, and size the trade to cost <$100 per position if possible.
9. **Reward/risk filter.** Only take trades with a reward-to-risk ratio greater than 2:1; buy options when volatility is low, sell when volatility is high; never leg into or out of a multi-leg spread.

## Risk and money management

The book states explicit account-level risk caps in its "Rules for Trading Success": risk no more than 5% of total trading capital on any single trade, and no more than 50% of the account across all open positions at any one time. Individual strategies carry their own defined maximum risk (usually the net debit paid, or a calculable capped amount for credit spreads/backspreads); undefined-risk strategies (naked short calls, uncovered ratio spreads beyond the credit zone) are flagged as needing a margin check with the broker. A supplemental trailing-stop-style rule appears in the stock-screening section: exit a position if the underlying breaks 20% off a new high (long trades) or 20% off a new low (short trades). The author also recommends targeting an ~75% win rate as a benchmark for a "good" trade selection process, and reviewing all closed trades every six months to identify recurring mistakes.

## Psychology and discipline

Psychology gets comparatively little dedicated space versus the mechanics, but a few threads recur: delta neutral trading is framed explicitly as a way to reduce the emotional strain of forecasting direction, since profits depend on volatility/time rather than being "right" about where price goes. The book stresses acting mechanically on adjustment triggers rather than hoping a losing directional bias will reverse — "every delta neutral trader knows the feeling of having a weight lifted... the moment he does the right thing." Traders are told to write every order down in a trading journal before calling the broker, to place multi-leg spreads as a single order to avoid leg-risk, and to periodically review losing trades for behavioral patterns rather than blaming the market.

## Chapter map

- Ch 1–3 — Options primer, market big picture, and contract basics (calls, puts, exercise/assignment).
- Ch 4 — Basic directional strategies (long/short stock, calls, puts, covered calls, protective puts) with breakeven/risk formulas for each.
- Ch 5 — Vertical spreads (bull call, bear put, bull put, bear call) with net-debit/net-credit mechanics.
- Ch 6 — Delta: definition, hedge-ratio use, and its relationship to volatility.
- Ch 7 — The other Greeks: gamma, theta, vega, and their interaction as expiration nears.
- Ch 8 — Straddles, strangles, and synthetics: full delta-neutral mechanics and volatility-driven entries.
- Ch 9 — Advanced delta-neutral strategies: call/put ratio backspreads with the seven backspread rules and 14-step road maps.
- Ch 10 — Range-bound techniques: butterflies, condors, iron butterflies/condors, calendars, diagonals, and collars, each with a road map.
- Ch 11 — Adjustments: fixed vs. variable delta, adjusting with options vs. stock, and delta-/time-/event-based adjustment triggers.
- Ch 12–13 — Choosing a broker and trade-processing mechanics (order types, ECNs, SOES).
- Ch 14 — Margin and risk (broker-specific; the book advises checking current requirements directly).
- Ch 15–17 — Macro/economic analysis, "mastering the market" (top-down vs. bottom-up selection, expected-value framing), and finding explosive opportunities (news/volume screens).
- Ch 18–19 — Trading tools/software and a final summary.
- Appendices — Trading resources, Greek/strategy reference tables, one-page "strategy review" cards per spread, and the Five-Minute Success Formula / Rules for Trading Success checklists.

## Strengths and caveats

The strategy road maps are unusually concrete for a retail options book — each spread comes with formulas for maximum risk, maximum reward, and breakeven, plus a numbered entry-to-exit checklist, which makes the material easy to turn into rules a system could check. The weaknesses are dated infrastructure references (floor trading, SOES, Island ECN, pre-decimalization spread mechanics in the order-routing chapter) that no longer describe modern electronic markets, and a promotional undertone pointing toward the author's Optionetics platform and seminars. Some claims read as optimistic in hindsight — a 75% win-rate target and reward/risk-ratio framing understate how option-selling strategies concentrate risk in tail moves, and volatility-skew explanations are simplified relative to how professional market-making desks actually model skew. The margin and regulatory content (Reg T, SOES rules) reflects mid-2000s rules and should not be relied on for current requirements.

## Who should read it

Suitable for a trader who already understands basic call/put mechanics and wants a structured bridge into spread trading and Greek-based risk management, particularly anyone interested in non-directional (delta-neutral) strategies. Less useful as a first exposure to options (the pacing assumes some background) or as a source for current execution/margin mechanics.

## Related books in this library

- [[black-scholes-option-pricing-model]] — the mathematical derivation behind the pricing model this book applies practically (Greeks, IV) without deriving.
- [[introduction-to-arbitrage-pricing-of-financial-derivatives]] — the no-arbitrage / replicating-portfolio theory underlying the option pricing this book treats as a given software output.
- [[using-options-to-buy-stocks-build-wealth-with-little-risk-and-no-capital]] — a narrower, single-strategy premium-selling method (short LEAP puts) that shares this book's volatility-selling logic.
