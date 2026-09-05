---
title: "Momentum Pinball"
author: Laurence A. Connors and Linda Bradford Raschke
year: 1995
slug: street-smarts-laurence-connors--momentum-pinball
tier: A
category: Swing Trading
tags: [rsi, rate-of-change, overnight-hold, first-hour-breakout, taylor-trading-technique]
difficulty: intermediate
doc_type: system
parent: street-smarts-laurence-connors
pages: 145
one_liner: "Uses a 3-period RSI of the 1-period rate of change (the LBR/RSI) to flag overbought/oversold exhaustion, entering on a first-hour range breakout and typically holding one to two days."
related: []
source_file: "Street Smarts (Laurence Connors).pdf"
---

## What it is

A short-horizon (one-to-two-day) directional-bias tool built to remove the ambiguity in George Douglass Taylor's manual buy-day/sell-day classification. It applies a 3-period RSI to a 1-period rate of change (today's close minus yesterday's close) — the authors label this composite the "LBR/RSI" — to flag exhaustion, then requires the market to confirm direction by breaking the first hour's trading range before entering, avoiding trades that never get confirmation.

## Rules

**Buy setup:**
1. Plot a 3-period RSI of the 1-period rate of change (net daily price change) — the LBR/RSI.
2. Day one: the LBR/RSI closes below 30.
3. Day two: place a buy stop above the high of the first hour's trading range.
4. Once filled, place a resting protective sell stop at the low of the first hour's range (the market "should not" return to this point).
5. If stopped out, the trade may be re-entered on a buy stop at the original price — rare, but profitable when it occurs.
6. If the trade closes with a profit on day two, carry it home overnight; exit on morning follow-through the next day (day three), by the close at the latest.

**Sell setup (reverse of buys):** day one LBR/RSI closes above 70; place a sell stop below the low of the first hour's range; protective buy stop at the high of the first hour's range; same overnight-hold and next-day-exit logic.

## Risk

Initial risk is bounded by the first hour's trading range — the protective stop sits at the opposite extreme of that range from the entry, so risk scales with early-session volatility rather than a fixed amount. The source explicitly cautions that markets with too narrow an average daily range produce a first-hour range too small to be worth trading (shown as a marginal example on IBM), so instrument selection (adequate daily range) is itself a risk-management input. No fixed percent-of-equity position size is given; the book's general rule (enter the full position at once, tighten stops as the trade becomes profitable) applies. The intended holding period is strictly one to two days — the authors repeatedly warn "do not overstay your welcome" — which limits both risk exposure and expected reward per trade.

## Caveats

Entries depend on the market confirming direction via the first-hour breakout; several worked examples show a valid LBR/RSI signal that never triggers because price fails to break the first-hour range, meaning the signal alone is not tradable without that confirmation. The authors note this pattern overlaps somewhat with the 80-20's setup (both exploit short-term exhaustion) but the two "test out independently" with different entry mechanics, implying no formal combined-edge study was done. No independent backtested win rate or drawdown is cited for Momentum Pinball itself in this chapter (the appendix's Moore Research statistical studies are cited primarily for other setups); the evidence given is a run of annotated S&P, IBM, and orange juice chart examples from 1995.
