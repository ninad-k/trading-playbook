---
title: Fixed Ratio Position Sizing
author: Ryan Jones
year: 1999
slug: forex-misc-money-management-ryan-jones--fixed-ratio-position-sizing
tier: A
category: Money Management & Position Sizing
tags: [fixed-ratio, position-sizing, money-management, delta, drawdown-control, futures]
difficulty: intermediate
doc_type: system
parent: forex-misc-money-management-ryan-jones
pages: 115
one_liner: "The Fixed Ratio delta formula for adding contracts as profit accumulates, with worked comparisons against Fixed Fractional and Optimal f sizing."
related: [balsara-nauzer-j-money-management-strategies-for-futures-traders, position-sizing, curtis-faith-way-of-the-turtle]
source_file: "Forex Misc - Money Management - Ryan Jones.pdf"
---

## What it is

A position-sizing overlay, independent of the entry/exit signal, that decides how many contracts (or shares) to trade next. Unlike Fixed Fractional sizing (risk a constant percentage of equity, or one contract per fixed dollar amount), Fixed Ratio requires an amount of new profit to add the next contract that grows in fixed proportion to the number of contracts already held. This keeps early-stage risk low while letting position size compound faster once the account has built a cushion.

## Rules

**1. Pick a delta.** Delta is the method's only free variable. Rule of thumb: set delta near half the market's expected worst-case per-contract drawdown (an expected $10,000 drawdown suggests roughly a $5,000 delta). Smaller delta = more aggressive (contracts added sooner); larger delta = more conservative.

**2. Compute the next contract-increase level.**
Previous required equity + (current number of contracts × delta) = equity level at which to add the next contract.
Example, delta = $5,000, starting balance $10,000: $10,000 + (1×5,000) = $15,000 to go to 2 contracts; $15,000 + (2×5,000) = $25,000 to go to 3; $25,000 + (3×5,000) = $40,000 to go to 4, and so on. Contracts are reduced by the same schedule in reverse if equity falls back through a level.

**3. Estimate the pace of growth from system statistics.**
Average trades between contract increases ≈ delta ÷ average trade profit. E.g., a $500 average trade with a $5,000 delta implies roughly one new contract every 10 trades, regardless of how many contracts are currently on (the required profit and the average trade both scale by the same factor). Treat this as a liberal estimate — it ignores asymmetrical leverage (a loss needs a proportionally larger gain to recover), so a realistic estimate is roughly 90% of the liberal figure.

**4. Find the profit boundary for any contract count N directly (no table needed).**
Lower boundary (level below which the account drops from N to N−1): [(N×N − N) ÷ 2] × delta.
Upper boundary (level above which the account moves from N to N+1): [(N×N + N) ÷ 2] × delta.
Example, N=10, delta=$5,000: lower = 45 × $5,000 = $225,000; upper = 55 × $5,000 = $275,000.

**5. Size the drawdown response.** Dividing an expected dollar drawdown by delta gives the maximum number of contract levels the account can fall, independent of where in the sequence the drawdown occurs. Example: trading at the 10-contract level with a $5,000 delta and a $10,000-per-contract drawdown → 10,000 ÷ 5,000 = 2 levels, so the floor is 8 contracts, not lower.

**6. Adapting to stocks or multi-lot units.** Because margin requirements are roughly proportional to price (unlike futures, where margin is a small fraction of contract value), the starting account balance must include a margin buffer large enough that required margin never outruns the Fixed Ratio schedule as units are added; recompute the buffer for the chosen unit size (e.g., 10-lot or 100-lot blocks) rather than assuming single-share economics scale directly.

**7. Portfolios of multiple markets.** Assign each market its own delta (roughly half that market's expected drawdown). Combining long and short units across loosely correlated markets lets more total units be carried for the same aggregate risk than trading only long or only correlated markets; total portfolio risk is not the simple sum of each market's exposure once correlation is accounted for.

## Risk

Fixed Ratio's risk profile is set almost entirely by delta: a smaller delta accelerates both compounding and drawdown percentage; a larger delta slows both. Jones's worked comparisons show that against Fixed Fractional methods producing equivalent total profit, Fixed Ratio at a matched delta produces a smaller percentage drawdown, because required equity per contract rises as contracts are added rather than staying constant (one-contract-per-$X) or requiring an ever-smaller marginal profit (Optimal f). The method's edge is largest for small-to-mid accounts; at large fund size, Fixed Fractional sizing can approach true continuous (near-fractional) compounding in a way a small Fixed Ratio account cannot, narrowing or reversing the comparison. Pair Fixed Ratio with the drawdown-response rule from the parent book (cut trading-unit risk 20% per 10% drawdown in equity) rather than relying on delta selection alone to bound losses.

## Caveats

The delta formula assumes a roughly stable relationship between account size and per-contract dollar risk; it does not itself select entries, exits, or stops, and provides no protection against an outsized single loss beyond whatever stop-loss method is used elsewhere. Worked examples use late-1990s futures margins and contract values and need updating for current markets. The comparisons favoring Fixed Ratio use selected, bounded drawdown scenarios rather than a full simulation across many possible trade sequences — treat "always superior to Fixed Fractional" as a claim to verify against your own system's trade distribution, not a proven universal result.
