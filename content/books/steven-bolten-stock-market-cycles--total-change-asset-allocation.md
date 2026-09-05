---
title: "Total Change Asset Allocation and the Time Horizon Duration Bubble Indicator"
author: Steven E. Bolten
year: 2000
slug: steven-bolten-stock-market-cycles--total-change-asset-allocation
parent: steven-bolten-stock-market-cycles
tier: A
category: "Investing, Value & Market History"
doc_type: system
pages: 184
one_liner: "A quarterly stock/bond switching rule based on earnings growth minus interest-rate change, paired with a dividend-discount-model 'years of growth priced in' bubble measure, both backtested by the author."
tags: [asset-allocation, market-timing, dividend-discount-model, sector-rotation, quantitative]
difficulty: advanced
related: [steven-bolten-stock-market-cycles]
source_file: "Steven Bolten - Stock Market Cycles.pdf"
---

## What it is

Two related, quantitative tools from Bolten's dividend-discount framework, reprinted from the author's peer-reviewed papers in Chapter 8: (1) **Total Change**, a quarterly signal for reallocating between equities and long government bonds based on earnings growth versus interest-rate change, backtested by Bolten and Besley over 1967-1987; and (2) **Time Horizon Duration** ("n"), a bubble/trough measure expressing how many years of assumed earnings growth are priced into a stock or index relative to its theoretical no-growth value, applied to historical extremes (1972, 1974, 1983, 1987). Both operationalize the book's claim that prices move on the relative rate of change between earnings and interest rates.

## Rules

**Total Change asset allocation**

1. Each quarter, calculate `Total Change = %ΔE − %Δi`, where %ΔE is the prior quarter's change in trailing/consensus index earnings (original study: S&P 400) and %Δi is the prior quarter's change in the 30-year Treasury yield.
2. **Positive** Total Change (earnings outgrowing rates, or rates falling faster than earnings) → shift weighting **toward equities**.
3. **Negative** Total Change (rates outrunning earnings growth, or earnings falling faster than rates) → shift weighting **toward long bonds**.
4. Reallocation is proportional to the magnitude, not a binary switch; the backtest rebalanced every quarter on the sign/size of the prior reading.
5. Use homogeneous, low-cost, liquid instruments for both legs (index funds/ETFs with switching capability) to keep costs low (~0.25%-0.50%/year estimated).
6. This is a **quarterly, full-cycle strategy**, not for intra-quarter trading; the stated risk is quarter-to-quarter whipsaw in the allocation itself.

**Time Horizon Duration ("n")**

7. Compute the no-growth value: `Sng = E / r` (current earnings E as a perpetuity, discounted at the long Treasury yield r).
8. Compute the gap: `Gap % = (P − Sng) / Sng`.
9. Divide by the consensus earnings growth rate (g) to get years of growth priced in: `n = Gap % ÷ g`.
10. Track n over time; rising n means a longer growth runway is being priced in than historically typical - extreme readings signal bubble risk.
11. Reference points: Q4 1972 n=46.62 (preceded the 1973-74 bear market); Q4 1974 n=17.84; Q3 1983 n=9.84 (fell then recovered as n normalized); Q1 1987 n=20.01, Q2 1987 n=11.54 (crash followed in Q4 1987). Bubble readings have historically clustered in Q3/Q4.
12. Use n as a risk overlay, not a timing trigger - it flags an unusually long assumed growth runway, not a correction date.

## Risk

Reported backtest (1967 Q4-1987 Q4): buy-and-hold S&P 400 = 10.6%/yr; 30-yr Treasuries = 7.8%/yr; T-bills = 6.1%/yr; Total Change reallocation = 12.9%/yr pre-commission; hindsight-optimal switching = 15.7%/yr. The 12.9% outperformed all static benchmarks without hindsight, and estimated expense costs (0.25%-0.50%/yr) would not erode this given only quarterly rebalancing. Risk is quarter-to-quarter allocation whipsaw, not stock-specific volatility, since both legs already eliminate individual-security and default risk. The Time Horizon Duration measure carries no stop-loss or sizing rule - it is a valuation gauge to combine with judgment, not a mechanical trigger.

## Caveats

The Total Change backtest covers one 20-year window with only a two-year out-of-sample extension, predating the low-rate regime of the 1990s-2020s; a strategy premised on tradable swings in bond yields may behave differently near zero rates. It also assumes earnings/yield data are interpretable on a consistent quarterly cadence, more reliable at the index level than for individual securities. The Time Horizon Duration examples are illustrative, not a systematic backtest with defined entry/exit rules - no numeric n threshold is specified as reliably actionable, only that extremes (its highest reading, 46.6, preceded the worst outcome) warrant caution. Treat both as diagnostic overlays for a longer-horizon allocator, not fully specified, risk-managed systems.
