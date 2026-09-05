---
title: "Trade Adjustment Playbook: Rolling, Collars, Ratio Spreads, and Repairs"
author: George M. Jabbour and Philip H. Budwick
year: 2004
slug: george-m-jabbour-the-option-trader-handbook-strategies-and-trade-adjustments--trade-adjustment-playbook
tier: A
category: Options, Futures & Derivatives
difficulty: intermediate
doc_type: system
parent: george-m-jabbour-the-option-trader-handbook-strategies-and-trade-adjustments
pages: 355
tags: [options, adjustments, rolling, collars, ratio-spreads, repair-strategies, hedging]
one_liner: "A rules-based menu for adjusting an existing stock or option position — roll it, collar it, convert it to a ratio spread, or repair it back toward breakeven — chosen by where the underlying is relative to the original entry."
related: []
source_file: "GEORGE M. JABBOUR - The Option Trader Handbook - Strategies And Trade Adjustments.pdf"
---

## What it is

A decision framework for what to do to an *already open* stock or option position as the underlying moves, rather than a method for picking new trades. The book treats four adjustment families as reusable primitives that recur across every chapter (long stock, short stock, calls, puts, spreads, combinations): (1) **rolling** a leg to a different strike/expiration, (2) **collaring** a position with a covered call plus protective put, (3) **converting** a directional position into a **ratio spread** by selling additional out-of-the-money options against it, and (4) **repairing** a losing position with a ratio spread structured for zero cost or a net credit. Which one to apply depends on where the underlying is relative to entry and what the trader now expects (continuation, reversal, or range-bound drift) rather than a fixed schedule.

## Rules

**When to roll**
1. Roll a profitable long option (call or put) to a further out-of-the-money strike when it has gained significantly and you expect continuation: sell the original option, use part of the profit to buy the new farther strike, and bank the remainder as a locked-in gain (call/put replacement).
2. Roll a losing directional position (protective put, long call/put) into a vertical spread (bear put spread, bull call spread) when you still expect a move but want to lower the cost basis: sell an option against the existing long at a strike beyond where you expect the move to stop.
3. Roll a vertical spread down (or up) a strike when the underlying has moved through it and a partial retracement is expected: close the original long leg, open a new long leg closer to the current price, and fund the difference by adding a short leg at (or near) the original strike — this creates a "Christmas tree" (short calls at two different strikes) if the original short leg is kept open rather than closed.

**When to convert to a ratio spread**
4. Convert a long call/put or a vertical spread into a ratio spread (sell 1 extra option per existing long, i.e. move from a 1:1 to a 1:2 structure) when the underlying has moved favorably and you now expect sideways-to-slightly-reversing action rather than continued strong movement.
5. Size the ratio at 1:2 as the default and 1:3 only when conviction that the stock will stop near the short strike is high; avoid 1:4 or higher except when an existing unrealized gain in the position provides a buffer against the added naked exposure — even then, treat it as high-risk.
6. Set the short strike of the ratio spread at the price level you expect the underlying to be trading at, at expiration — that strike is both the adjustment's maximum-profit point and, beyond it, where naked risk begins.
7. Calculate the new (upside or downside) breakeven point after adding the ratio before committing to it: breakeven = short strike ± (spread width + net credit, or − net debit), adjusted for which side the naked risk sits on.

**When to collar**
8. Add a collar (sell an out-of-the-money covered call, buy an out-of-the-money protective put, same expiration) to a stock position at entry or after a gain, sizing strikes so the trade opens near zero cost or for a small net credit.
9. Use a "profit collar" once a long stock position shows an unrealized gain: sell a call above the current price and buy a put below it to lock in a minimum guaranteed profit (the put's intrinsic value plus/minus the collar's net credit/debit) while retaining limited further upside to the call strike.
10. For a more conservative ("upward-bias") collar, buy an at-the-money put instead of an out-of-the-money one; this raises the net debit but reduces maximum risk and raises the minimum guaranteed outcome.
11. Never close only the put side of a collar while a stock is still held and the short call remains open uncovered — closing the put and leaving the call naked reintroduces unlimited risk and margin exposure that the collar was built to remove.

**When to repair**
12. Apply a repair ratio spread to a losing long stock or long call position only when a partial (not necessarily full) recovery is expected: buy one option near the current price and sell two (or more, up to ~1:3) options at a higher strike set at the expected recovery target.
13. Require the repair spread to open for a net credit or at worst a very small net debit — a repair that requires meaningful new capital is not fulfilling its purpose (reducing the breakeven without adding risk).
14. Ensure every short leg in a repair spread is fully covered by the long option or the underlying shares; a repair adjustment should never introduce a naked leg, since that adds risk to a position that is already underwater.
15. If the underlying continues falling below the repair spread's long strike, expect the repair to stop helping — the position then behaves close to the unadjusted original, offset only by the small credit collected at inception.

**Exit / follow-through**
16. At expiration of any adjustment (collar, ratio spread, repair), reassess: if the underlying sits between the strikes, the hedge/adjustment expires and original directional risk returns — decide explicitly whether to roll into a new adjustment, close the position, or let it run unhedged.
17. Recalculate maximum risk, maximum reward, and both breakeven points every time a new leg is added or removed; do not adjust based on a stale risk profile from before the change.

## Risk

Every adjustment shifts, rather than eliminates, risk: rolling and repair spreads reduce breakeven but typically cap upside (via a short strike) and can introduce naked exposure beyond that strike if the ratio exceeds 1:1; collars cap both loss and gain by construction, so the "cost" of downside protection is forfeited upside beyond the call strike. Ratio spreads and ratio writes carry a margin requirement on their naked leg(s), and that leg's risk is theoretically unlimited (calls) or limited-but-large (puts, capped at the strike) if the underlying makes a large move beyond the new breakeven. Repair spreads structured for a net credit have no additional capital at risk beyond the original position, but they also provide little to no incremental downside protection — they only improve outcomes in the range between the original loss level and the new upside breakeven. Every adjustment's profit/loss figures in the source assume the position is held to expiration and exclude commissions and bid/ask slippage, which understates the true cost of adjustments involving multiple simultaneous leg trades.

## Caveats

The framework is a menu of mechanically sound techniques, not a decision algorithm — the book does not give quantitative thresholds (e.g., "roll when down X%" or "collar when up Y%") for when to trigger each adjustment type; the choice is left to the trader's directional judgment on where the underlying is headed next, which is the same forecasting problem the adjustment was meant to sidestep. No backtested win-rate, expectancy, or comparative performance data is given for any adjustment path versus simply closing the position; every example is a single hypothetical illustrative case (EBAY, YHOO, COST) rather than a statistical study. The "repair" framing can also encourage loss aversion — turning a stock repair into a de facto reason to avoid realizing a loss — which the book's own risk-management chapter (Chapter 1) cautions against elsewhere ("trade freeze").
