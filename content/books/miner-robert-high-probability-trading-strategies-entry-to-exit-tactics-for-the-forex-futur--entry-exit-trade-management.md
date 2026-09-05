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

The execution layer used once the setup filter (see [[miner-robert-high-probability-trading-strategies-entry-to-exit-tactics-for-the-forex-futur--dual-time-frame-momentum-setup]]) qualifies a market: two objective entry/stop techniques, a position-size formula, and a two-unit trade-management plan governing stop adjustments through the exit. Both entries require price to move in the anticipated direction first — Miner never buys or sells at a fixed target.

## Rules

**Entry 1 — Trailing One-Bar (Tr-1BH/L).** Once the setup filter qualifies a direction, place a buy-stop (long) one tick above the last completed bar's high, or sell-stop (short) one tick below its low; trail forward bar by bar until filled. Initial stop, once filled: one tick beyond the swing high/low made prior to entry. If the opposing momentum reversal occurs, or price reaches OB/OS, before the trail is taken out, the setup is voided.

**Entry 2 — Swing Entry (SE).** Same qualifying conditions, but the trigger is a break of the most recent swing high/low, one tick beyond it; stop one tick beyond the prior swing low/high. Wider risk than Tr-1BH/L but a higher stated win rate. If per-contract risk is too large, drop to a smaller time frame for entry (shrinks the stop) or use an unleveraged proxy.

**Position size.** Max capital exposure = 3% of equity per trade; 6% max across all open trades. Capital-exposure-per-unit = |entry − initial stop| × multiplier. Max position size = floor(3% of equity ÷ exposure-per-unit); never size above this. Stop trading for the rest of the month at a 10% closed-trade drawdown.

**Two-unit structure.** Split every trade into a short-term (ST) and a long-term (LT) unit at entry, managed independently.

**ST unit.** Assume the move is only a minor correction. Trail the stop to Tr-1BL/H once price reaches the 61.8% retracement of the move, or a second momentum reversal occurs against the position — whichever comes first. Locks in a small profit even if the larger-trend thesis is wrong.

**LT unit.** Hold with a wide stop while the trend develops, moving it only at logical pattern points (e.g. below/above the most recent completed wave extreme) — never by a fixed dollar/percent amount or schedule. Once higher-TF momentum reaches OB/OS, or a Fibonacci price target zone is reached, tighten to a Tr-1BL/H trail to protect late-stage gains.

**Exit philosophy.** Never exit at a fixed target — let the trailing stop take the position out, since trends routinely exceed projections. Mid-trade changes must follow the same momentum/pattern/price/time evidence used to enter, never an arbitrary reaction to open profit.

## Risk

Realized risk per trade is bounded by the 3%/6% sizing rule at entry, but open-trade risk shifts constantly as the LT stop is widened with the trend then tightened late — unlike a static-stop system. The known failure mode is a sharp reversal right after the LT stop was widened "to give the trend room"; the book acknowledges this without giving drawdown or win-rate figures for the plan as a whole.

## Caveats

Both entries can produce no fill if price never triggers the trail/swing level — acceptable by design, but a mechanical build needs an explicit signal-expiry rule beyond the source's loose "voided if the opposing reversal comes first." LT-unit stop placement ("a logical pattern point") is illustrated by example, not a single formula, so it carries more discretion than the ST rule or the sizing formula.
