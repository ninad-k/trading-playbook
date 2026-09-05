---
title: McMillan's Volatility-Based Option Strategy Selection
author: Lawrence G. McMillan
year: 2002
slug: lawrence-g-mcmillan-profit-with-options--volatility-based-strategy-selection
tier: A
category: Options, Futures & Derivatives
tags: [options, implied-volatility, straddles, ratio-spreads, percentile-rank, volatility-trading]
difficulty: intermediate
doc_type: system
parent: lawrence-g-mcmillan-profit-with-options
pages: 286
one_liner: "Rank implied volatility against its own history: buy straddles/backspreads under the 10th percentile, sell strangles/ratio spreads above the 90th, with explicit follow-up rules for both."
related: [lawrence-g-mcmillan-profit-with-options, position-sizing]
source_file: "LAWRENCE G. McMILLAN - Profit With Options.pdf"
---

## What it is

A rule-based method for choosing whether to buy or sell option premium, using each underlying's own historical implied volatility (IV) distribution rather than a universal "cheap/expensive" threshold. Daily IV (and historical volatility, HV) readings are ranked by percentile against 200–600+ past trading days; the percentile — not the raw IV number or a simple IV-vs-HV comparison — determines the strategy: straddle buying, backspreads, strangle selling, or ratio spreads.

## Rules

**Compute composite IV daily.** Blend the individual option IVs for an underlying (weighted by volume and moneyness) into one daily composite reading; keep a running history of at least 200 trading days, ideally 600+.

**Rank by percentile, not raw comparison.** Place today's composite IV against its own historical distribution; separately rank the 10-, 20-, 50-, and 100-day HV readings the same way. A raw "IV higher than HV" reading alone is not sufficient — some underlyings (index options) structurally trade with IV persistently above HV, so only a percentile-versus-own-history reading is trusted.

**Cheap options — buy volatility (IV ≈10th percentile or lower).** Straddle purchase, or a backspread if a favorable skew is also present. Four criteria before entering:
1. Composite IV at or below the 10th percentile, confirmed against current real-time prices.
2. A Monte Carlo calculator shows ≥80% "ever" probability (touching either breakeven at any point before expiration — not the lower "closing" probability, which is just delta) using a conservative low-volatility input.
3. Price history shows the underlying has actually moved the required distance in the required time before.
4. Fundamentals rule out a structural reason IV is low (e.g. a pending cash-tender takeover).
Buy options with at least three months of remaining life.

**Expensive options — sell volatility (IV ≈90th percentile or higher).** Naked strangle/combination sale, or a ratio spread; pick the skew-appropriate variant (positive skew → call ratio spread or put backspread; reverse skew → put ratio spread or call backspread, by whether IV is high or low). Two criteria:
1. IV at or above the 90th percentile.
2. A Monte Carlo calculator shows ≤25% "ever" probability of reaching the short strike (10–15% is safer) using a conservative high-volatility input.
Confine naked selling mainly to index options, or stock options where the news behind the spike is already public. Never sell a naked option priced below about 1.5 points.

**Check the reason before acting.** Before selling elevated IV, rule out an undisclosed catalyst (FDA ruling, lawsuit, takeover rumor) — if one exists, consider an event-driven straddle buy instead. Before buying depressed IV, rule out a structural reason it's low (post-takeover-bid, permanently reduced volatility, a much higher stock price than its volatility history reflects) — not a genuine opportunity despite the cheap percentile.

**Follow-up (straddle buys).** Leave the position alone until a breakeven is approached; close if the straddle loses 60% of its cost. On a profitable breakout, close the losing side, take partial profit (e.g. one-third) on the winning side, trail the rest with a 20-day moving average stop on the underlying.

**Follow-up (naked/strangle sales).** Take defensive action as soon as the underlying reaches the short strike; hold margin sufficient for that scenario from the outset (estimate the option's value at the strike, not just the current OTM margin).

## Risk

Straddle-buying risk is capped at premium paid, tightened by the 60%-of-cost stop; the ≥80% ever-probability criterion is the main edge control, since delta alone understates true breakeven odds. Naked/strangle-selling risk is large or unlimited on a gap; controlled by confining it mainly to index options, requiring ≤25% ever-probability on the short strike, and over-funding margin for a worst-case move. Backspreads/ratio spreads bound risk structurally (a backspread nets a credit so one side is always defined-risk; a ratio spread has a defined max-risk zone) but still carry real loss near the short strikes at expiration.

## Caveats

The method needs a maintained IV/HV database and Monte Carlo software most retail traders must source independently; McMillan's examples lean on his firm's proprietary tools. The 80%/25% thresholds are personal guidelines, not a published backtest — he separately suggests 10–15% may be safer than 25% for naked selling. Straddle buying can produce long flat, decaying stretches ("watching paint dry") even with correct entry criteria; the plan has no time stop beyond the 60%-of-cost loss limit and three-month minimum entry life.
