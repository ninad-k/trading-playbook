---
title: "Delta-Neutral Straddle & Adjustment System"
author: George A. Fontanills
year: 2005
slug: fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed--delta-neutral-straddles-and-adjustments
tier: A
category: Options, Futures & Derivatives
tags: [options, delta-neutral, straddle, strangle, greeks, volatility, adjustments]
difficulty: intermediate
doc_type: system
parent: fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed
pages: 592
related: []
one_liner: "Trade an at-the-money straddle for a volatility/news catalyst, then mechanically rebalance the position back to zero delta whenever it drifts about 100 deltas off-center."
source_file: "Fontanills - The Options Course - High Profit And Low Stress Trading Methods, 2nd Ed.pdf"
---

## What it is

A non-directional options method built around the long straddle (buy an at-the-money call and an at-the-money put, same strike and expiration) or strangle (same idea, different strikes), entered so the position starts with a net delta of zero. Because ATM options have roughly ±50 delta and one option contract represents 100 shares of exposure, one long call plus one long put nets to ~0 delta at entry. The trade does not bet on direction; it bets that the underlying will move enough (or that implied volatility will rise enough) to overcome the combined time decay (theta) of both legs before expiration. As the underlying price moves, the position's net delta drifts away from zero — the trader then "adjusts" (buys or sells stock, or sells some of the winning-side options) to bring delta back toward neutral, banking a piece of the move each time. This adjustment process, repeated over the trade's life, is the core profit engine, distinct from simply holding the straddle to expiration.

## Rules

**Entry**
1. Look for a stock with low current implied volatility (IV) relative to its own historical range, ideally with a known catalyst ahead — an earnings release is the most reliable and predictable trigger (four scheduled dates per year per company).
2. Use options with 30–90+ days to expiration (the book leans toward the long end, ~90 days) so time decay doesn't outrun the volatility/price move. Avoid short-dated straddles — non-linear time decay erodes them fastest in the final weeks.
3. Buy one ATM call and one ATM put, same strike and expiration (straddle), or slightly different strikes (strangle) if a lower net debit is preferred. Confirm the position opens at (or very near) delta neutral: long call delta (+50) + long put delta (−50) ≈ 0.
4. Alternative entry: combine stock with options instead of two option legs — e.g., long 100 shares (+100 delta) hedged with 2 long ATM puts (2 × −50 = −100 delta) for a synthetic straddle-like profile.
5. Confirm sufficient option liquidity (tight bid/ask) since the strategy depends on adjusting multiple times over the trade's life; wide spreads and per-trade commissions erode the edge.

**Adjustment (the core of the system)**
6. Track the position's net delta continuously (or via end-of-day recalculation). Three trigger types, used interchangeably or combined:
   - **Delta-based (the default):** when net position delta reaches a predetermined magnitude — the book's standard is ±100 — rebalance immediately by buying/selling stock or by selling some of the in-the-money-side options.
   - **Time-based:** rebalance to neutral on a fixed schedule (e.g., end of each day or week) regardless of the delta reading.
   - **Event-based:** rebalance just ahead of a known volatility event (e.g., before an earnings release) to lock in the pre-announcement volatility run-up.
7. To adjust with options: if the underlying rallied, sell some of the now-higher-delta calls (take profit on the winning side) to bring delta back down; if it fell, sell some puts. This recycles capital into new positions but incurs commissions and bid/ask slippage.
8. To adjust with stock: if delta has drifted positive (long-biased), sell shares; if negative, buy shares. Every 100 shares traded offsets 100 deltas — the simplest, lowest-slippage way to rebalance, and the book's preferred method once account size supports it.
9. Delta-based adjustment can be pre-calculated at the start of the trading day: solve for the exact underlying price at which position delta will hit ±100, and place a standing stock order at that level so the adjustment executes automatically without intraday monitoring.
10. Each adjustment that captures profit on the winning leg effectively "restarts" part of the spread at a new, more favorable price — the mechanism by which the trade earns money beyond the initial volatility move.

**Exit**
11. Close (or stop adjusting and let expire) 30 or more days before expiration as a general rule, since gamma/theta both accelerate sharply in the final month and the reward-to-risk of continuing to hold deteriorates.
12. If the anticipated catalyst (e.g., earnings) has already occurred and volatility has reverted to its pre-announcement level, exit — waiting longer risks giving back gains to time decay as the "excess" volatility used to price the straddle high has already been captured or lost.
13. If the position never gets going (underlying stays pinned near the strike, IV doesn't rise), treat the eroding theta as the defined risk and exit before it consumes more than the acceptable loss for the trade — the straddle's maximum loss is the total premium paid for both legs.

## Risk

Maximum loss on the basic long straddle/strangle is capped at the combined premium paid for the call and put (the net debit), realized if the underlying finishes exactly at the strike at expiration with no adjustments made. Because the position carries negative theta on both legs simultaneously, the passive risk is time decay: an underlying that fails to move (or whose IV doesn't rise) bleeds value daily, faster as expiration approaches. Delta neutrality does not eliminate this — it only removes *directional* risk, not volatility/time risk. Adjusting with options rather than stock adds transaction-cost risk (commissions plus bid/ask spread, cited as $10–$30 minimum per option trade in the source, versus near-zero cost per stock trade), which can offset the benefit of frequent rebalancing on small accounts. Account-level sizing follows the book's general risk caps: no more than 5% of trading capital on one trade, no more than 50% deployed at once.

## Caveats

The book presents adjustment as mechanically simple but glosses over how noisy and expensive frequent options-based rebalancing can be in practice — bid/ask slippage on each adjustment is acknowledged but not modeled into the numeric examples, which tend to show clean, idealized outcomes. The ±100-delta trigger is offered as a default rather than derived from optimization; no backtested win-rate or expectancy data is given for the straddle-adjustment system as a whole, only for isolated example trades. The strategy also assumes options liquid enough to adjust repeatedly without moving the market, which is not true of thinly traded underlyings.
