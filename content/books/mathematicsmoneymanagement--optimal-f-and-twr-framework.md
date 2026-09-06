---
author: Ralph Vince
category: Money Management & Position Sizing
difficulty: advanced
doc_type: system
one_liner: The exact formulas for computing optimal f from a trade history, comparing
  systems by geometric mean, and sizing contracts trade to trade.
pages: 106
parent: mathematicsmoneymanagement
related:
- balsara-nauzer-j-money-management-strategies-for-futures-traders
- kellybetting
slug: mathematicsmoneymanagement--optimal-f-and-twr-framework
source_file: MathematicsMoneyManagement.pdf
tags:
- optimal-f
- kelly-criterion
- twr
- geometric-mean
- position-sizing
- drawdown
tier: A
title: Optimal f and the TWR/Geometric Mean Framework
year: 1992
---

## What it is

A position-sizing procedure, not a trading signal. Given any market system's historical trade-by-trade P&L (computed on a strict 1-unit basis), it finds the single fixed fraction f of the biggest historical loss that maximizes long-run geometric growth of an account under full reinvestment, then converts that fraction into a dollars-per-contract figure usable on the next trade.

## Rules

**1. Prepare the trade stream.** Collect every trade's P&L for one market system (one method, one market, one unit size — e.g., 1 futures contract or 100 shares). Pyramided add-ons are separate market systems. Identify the single largest losing trade in the series (must be negative).

**2. Compute HPR for a candidate f.**
HPR_i = 1 + f × (−Trade_i ÷ Biggest Loss), where Trade_i is signed (losses negative) and Biggest Loss is negative, so −Trade_i/Biggest Loss is positive for losses and negative for wins.

**3. Compute TWR and geometric mean for that f.**
TWR(f) = Π(i=1..N) HPR_i
G(f) = TWR(f)^(1/N), N = number of trades.

**4. Search for optimal f.** Loop f from 0.01 to 1.00 (step 0.01, or use a faster search such as parabolic interpolation). Both TWR(f) and G(f) are smooth, single-peaked curves in f, so the point where TWR stops rising and starts falling is the optimal f. TWR and G peak at the same f — either can be used as the objective.

**5. Convert f to a tradable size.**
Dollars per contract = Biggest Loss ÷ (−optimal f). Example: biggest loss = −$100, optimal f = .25 → $100/.25 = $400 per contract (1 contract for every $400 of equity).
Contracts to trade = floor(current account equity ÷ dollars per contract). Recompute this every day/period as equity changes, not just once.

**6. Geometric Average Trade (GAT), for comparing systems in dollar terms.**
GAT = (G − 1) × (Biggest Loss ÷ −f). This is the system's expected profit per contract per trade under fixed-fractional trading — a fairer comparison across systems than the raw average trade, since it already reflects the effect of fewer contracts held through losers.

**7. Kelly formulas — use only as a sanity check, not as optimal f.**
- Equal-size win/loss: f = 2P − 1 = P − Q (P = win probability, Q = 1 − P).
- Fixed payoff ratio B (win size ÷ loss size), Bernoulli only: f = ((B+1)P − 1) / B = P − Q/B.
- Averaging unequal wins/losses into B understates true optimal f (Vince's example: averaged-Kelly gives f=.16 vs. the correct f=.24 on the same 9-trade sequence) — Kelly is valid strictly for two-outcome, fixed-size distributions, which trading is not.

**8. Multi-system portfolio allocation.** Convert each system's daily $ P&L to a daily HPR relative to its own optimal-f dollar amount: Daily HPR = (Dollars made/lost that day ÷ optimal f in dollars) + 1. For a candidate allocation, Net HPR for a day = Σ(system HPR × its % allocation). Tabulate the mean and population standard deviation of daily net HPRs per candidate; Estimated Geometric Mean EGM = √(AHPR² − SD²) ranks candidates without recomputing full TWRs. The allocation with the highest EGM is the optimal portfolio mix.

**9. Daily rebalancing.** Divide each system's optimal-f dollar amount by its % allocation to get a "contract per total account equity" figure; divide current equity by that figure and floor to the integer for contracts to hold, recalculated daily regardless of profit or loss.

## Risk

Historical drawdown at optimal f is never less than f expressed as a percentage of equity — optimal f = .55 implies at least a 55% equity retracement somewhere in the history. Better systems (higher optimal f) mechanically imply deeper drawdowns; no configuration of optimal f avoids this trade-off. A 5+ year multi-system portfolio traded at full optimal f should still expect 30-95% equity retracements regardless of diversification, since uncorrelated systems still periodically draw down in unison — diversification buffers but does not eliminate this, and can increase it under some correlation structures. Betting beyond optimal f reduces long-run TWR relative to optimal f, and past a large enough f (e.g., f > 0.5 in a 50/50, 2:1 payoff game) the account is a near-certainty to reach zero even though the game still has positive expectancy.

## Caveats

The framework requires a positive-expectancy trade stream to begin with — no money management rescues a negative- or zero-expectancy system. TWR assumes fractional contracts are tradable; real integer-lot trading causes small accounts to diverge from the theoretical curve, converging only as equity grows large relative to one contract's dollar-per-unit requirement. Optimal f assumes the historical biggest loss and trade distribution represent the future — a larger future loss invalidates the calibration. The book gives no formal rule for diluting f below the mathematical optimum, beyond noting the trade-off is geometric, not linear.