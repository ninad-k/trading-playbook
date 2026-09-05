---
title: Miner's Entry, Position Size, and Two-Unit Trade Management Plan
author: Robert C. Miner
year: 2009
slug: miner-robert-high-probability-trading-strategies-entry-to-exit-tactics-for-the-forex-futur--entry-exit-trade-management
tier: A
category: Fibonacci, Gann & Elliott Wave
tags: [entry-triggers, stop-loss, position-sizing, trade-management, risk-management]
difficulty: advanced
doc_type: system
parent: miner-robert-high-probability-trading-strategies-entry-to-exit-tactics-for-the-forex-futur
pages: 290
one_liner: "Two objective entry triggers, a 3%/6% position-sizing formula, and a two-unit stop-trailing plan that manages every trade from fill to exit."
related: [miner-robert-high-probability-trading-strategies-entry-to-exit-tactics-for-the-forex-futur--dual-time-frame-momentum-setup, dynamic-trading-by-robert-c-miner--entry-triggers-and-stops, position-sizing]
source_file: "Miner Robert - High Probability Trading Strategies Entry to Exit Tactics for the Forex, Futures, and Stock Markets.pdf"
---

## What it is

The execution layer used once the setup filter (see [[miner-robert-high-probability-trading-strategies-entry-to-exit-tactics-for-the-forex-futur--dual-time-frame-momentum-setup]]) qualifies a market for a trade: two objective entry/stop techniques, a mechanical maximum-position-size formula, and a two-unit trade-management plan that governs stop adjustments through the exit. Both entry techniques require the market to move in the anticipated direction before a trade is placed — Miner never buys or sells at a fixed target price.

## Rules

**Entry Strategy 1 — Trailing One-Bar entry (Tr-1BH/L).** Once the setup filter qualifies a direction, place a buy-stop (long) one tick above the high of the last completed bar, or a sell-stop (short) one tick below the low of the last completed bar; trail this stop forward bar by bar until filled. Once filled, the initial protective stop is one tick beyond the swing high/low made prior to entry. If the opposing momentum reversal occurs, or price reaches the OB/OS zone, before the trailing bar is taken out, the setup is voided — no trade.

**Entry Strategy 2 — Swing Entry (SE).** Same qualifying conditions as Strategy 1, but the trigger is a break of the most recent swing high (long) or swing low (short), one tick beyond it; initial stop is one tick beyond the swing low/high made prior to entry. Wider capital exposure than Tr-1BH/L but a higher stated win rate. If per-contract risk is too large for the account, drop to the next smaller time frame for entry (usually shrinks the stop) or use an unleveraged proxy instrument.

**Maximum position size.** Maximum capital exposure = 3% of available account equity per trade; 6% max across all open trades simultaneously. Capital-exposure-per-unit = |entry price − initial stop price| × contract/share multiplier. Maximum position size = floor(3% of equity ÷ capital-exposure-per-unit). If sizing to more than this maximum, do not take the trade. Stop trading for the remainder of the month if closed-trade losses reach a 10% account drawdown.

**Two-unit structure.** Every trade is split into at least two units at entry (e.g. 1 contract each, or any consistent split): a short-term (ST) unit and a long-term (LT) unit, each independently managed.

**ST unit management.** Assume the trade may be only a minor correction, not a full trend. Trail the stop to the Tr-1BL/H (one tick beyond the prior completed bar) once either (a) price reaches the 61.8% retracement of the move being traded, or (b) a second momentum reversal occurs against the position on the entry time frame — whichever comes first. This locks in a small profit even if the larger-trend thesis is wrong.

**LT unit management.** Hold with a wide stop while the trend develops, moving the stop only at logical pattern points (e.g. below/above the most recent completed wave low/high once a new extreme confirms it) — never by a fixed dollar or percentage amount, and never on a fixed time schedule. Once the higher time frame momentum reaches its OB/OS zone, or price reaches a computed Fibonacci price target zone, tighten the stop to a Tr-1BL/H trail (or the daily 1BL/H after a second confirming momentum reversal) to protect the trend's late-stage gains.

**Exit philosophy.** Never exit at a fixed profit target — let the market take the position out via the trailing stop, since trends routinely exceed projected targets. Any change to the trade-management plan mid-trade must follow from the same momentum/pattern/price/time evidence used to enter, not from an arbitrary reaction to open profit.

## Risk

Total realized risk per trade is bounded by the 3%/6% sizing rule at entry, but because stops are trailed rather than fixed, open-trade risk changes constantly as the LT unit's stop is moved outward with the trend before being tightened late in the move — a materially different risk profile from a static-stop system. The plan's known failure mode is a market that reverses sharply right after the LT stop has been widened to "give the trend room," which the book acknowledges but does not size numerically (no historical drawdown or win-rate figures are given for the plan as a whole).

## Caveats

Both entry techniques can produce no fill at all if price never triggers the trailing bar or swing level — the book treats this as acceptable (a passed opportunity, not a loss) but a mechanical implementation needs an explicit signal-expiry rule, which the source material only states loosely ("if the opposing momentum reversal occurs first, the setup is voided"). LT-unit stop placement ("a logical pattern point") is described by example rather than by a single formula, so it carries more discretion than the ST-unit rule or the position-sizing formula.
