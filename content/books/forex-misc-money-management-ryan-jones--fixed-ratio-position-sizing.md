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

**1. Pick a delta**, the only free variable. Rule of thumb: roughly half the expected worst-case per-contract drawdown (a $10,000 drawdown suggests a $5,000 delta). Smaller delta = more aggressive; larger = more conservative.

**2. Contract-increase level**: previous required equity + (contracts held × delta) = level to add the next contract. Example, delta $5,000, start $10,000: $10,000+(1×5,000)=$15,000 → 2 contracts; $15,000+(2×5,000)=$25,000 → 3; $25,000+(3×5,000)=$40,000 → 4. Contracts drop by the same schedule in reverse if equity falls back through a level.

**3. Estimate the pace of growth**: average trades between increases ≈ delta ÷ average trade profit. A $500 average trade with a $5,000 delta implies roughly one new contract every 10 trades at any contract count — a liberal estimate, since it ignores asymmetrical leverage; a realistic figure is closer to 90% of it.

**4. Profit boundary for contract count N**: lower (drop to N−1) = [(N×N − N) ÷ 2] × delta; upper (move to N+1) = [(N×N + N) ÷ 2] × delta. Example, N=10, delta=$5,000: lower = 45×5,000 = $225,000; upper = 55×5,000 = $275,000.

**5. Drawdown response sizing**: expected dollar drawdown ÷ delta = maximum contract levels the account can fall, regardless of where in the sequence it strikes. At 10 contracts, $5,000 delta, $10,000 drawdown → 2 levels, floor of 8 contracts.

**6. Stocks or multi-lot units**: margin is roughly proportional to price (unlike futures, where it's a small fraction of contract value), so the starting balance needs a margin buffer large enough that required margin never outruns the schedule as units are added; recompute for the chosen unit size (10-lot, 100-lot).

**7. Portfolios**: assign each market its own delta (roughly half its expected drawdown). Combining long and short units across loosely correlated markets carries more total units for the same aggregate risk than an all-long or highly correlated book.

## Risk

Fixed Ratio's risk profile is set almost entirely by delta: smaller accelerates both compounding and drawdown percentage; larger slows both. Against Fixed Fractional methods producing equivalent total profit, a matched delta produces a smaller percentage drawdown, because required equity per contract rises as contracts are added rather than staying constant (one-contract-per-$X) or shrinking (Optimal f). The edge is largest for small-to-mid accounts; at large fund size, Fixed Fractional can approach true continuous compounding in a way a small Fixed Ratio account cannot. Pair Fixed Ratio with the parent book's drawdown-response rule (cut trading-unit risk 20% per 10% equity drawdown) rather than relying on delta alone.

## Caveats

The formula assumes a roughly stable relationship between account size and per-contract dollar risk; it does not select entries, exits, or stops, and gives no protection against an outsized single loss beyond whatever stop method is used elsewhere. Worked examples use late-1990s futures margins and need updating for current markets. Comparisons favoring Fixed Ratio use selected, bounded drawdown scenarios rather than a full simulation across trade sequences — verify "superior to Fixed Fractional" against your own system rather than treating it as a universal result.
