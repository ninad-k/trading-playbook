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

A rule-based method for choosing whether to buy or sell option premium, using each underlying's own historical implied volatility (IV) distribution rather than a universal "cheap/expensive" threshold. Daily IV readings (and historical volatility, HV) are ranked by percentile against 200–600+ past trading days; the percentile — not the raw IV number, and not a simple IV-vs-HV comparison — determines the strategy. The same percentile framework selects among straddle buying, backspreads, strangle selling, and ratio spreads.

## Rules

**Compute composite IV daily.** Blend the individual option IVs for an underlying (weighted by volume and moneyness) into one daily composite reading; keep a running history of at least 200 trading days (ideally 600+, i.e. roughly a year or more).

**Rank by percentile, not raw comparison.** Place today's composite IV against the historical distribution (deciles or percentiles). Separately rank the 10-, 20-, 50-, and 100-day HV readings the same way. A raw "IV higher than HV" reading is not sufficient by itself — some underlyings (e.g. index options) structurally trade with IV persistently above HV, so only a percentile-versus-own-history reading is trusted.

**Cheap options — buy volatility (IV in roughly the 10th percentile or lower).** Preferred structures: straddle purchase, or a backspread if a favorable volatility skew is also present. Apply four straddle-buying criteria before entering:
1. Composite IV at or below the 10th percentile of its own history, confirmed against current real-time option prices.
2. A Monte Carlo probability calculator shows at least an 80% "ever" probability (probability the underlying touches either breakeven at any point before expiration — not the lower "closing" probability, which is just the option's delta) using a conservative (low) volatility input.
3. The underlying's own price history shows it has actually made moves of the required size within the required time window before.
4. Fundamentals are checked to rule out a structural reason IV is low (e.g. a pending cash-tender takeover that removes price uncertainty) rather than a true mispricing.
Buy options with at least three months of remaining life to blunt early time decay.

**Expensive options — sell volatility (IV at roughly the 90th percentile or higher).** Preferred structures: naked strangle/combination sale (sell an OTM call and an OTM put) or a ratio spread (buy one option, sell more further out); apply a skew-appropriate variant (positive skew → call ratio spread or put backspread; negative/reverse skew → put ratio spread or call backspread, chosen by whether IV is high or low). Two criteria before selling naked:
1. IV at or above the 90th percentile of its own history.
2. A Monte Carlo probability calculator shows a 25% or lower "ever" probability of the underlying reaching the short strike before expiration (10–15% is safer), using a conservative (high) volatility input.
Confine naked selling mainly to index options (no single-name takeover/earnings gap risk) or to stock options where the news driving the IV spike is already public and understood. Never sell a naked option trading below about 1.5 points — it can't be covered cheaply on a further decline.

**Check the reason before acting.** Before selling elevated IV, rule out an undisclosed corporate event (FDA ruling, lawsuit, takeover rumor) — if a known catalyst explains the spike, treat it as a potential event-driven straddle buy instead of a volatility sale. Before buying depressed IV, rule out a structural reason it's low (post-takeover-bid, permanently reduced company volatility, or a stock now trading at a much higher price than its volatility history reflects) — these are not genuine buying opportunities even though the percentile looks cheap.

**Follow-up (straddle buys).** Leave the position alone until a breakeven is approached; risk 60% of the initial straddle cost as a stop-out level (close if the straddle loses 60% of its value). On a profitable breakout, close the losing side, take partial profit (e.g. one-third) on the winning side, and trail the remainder with a 20-day moving average stop on the underlying.

**Follow-up (naked/strangle sales).** Take defensive action as soon as the underlying trades to the short strike; hold margin sufficient for that scenario from the outset (estimate the option's value if the underlying reaches the strike, not just the current out-of-the-money margin) so a forced adjustment is never margin-driven.

## Risk

Straddle-buying risk is capped at the premium paid (managed down further by the 60%-of-cost stop); the "ever" probability criterion (≥80%) is the primary edge control, since closing-probability/delta alone understates true breakeven odds. Naked/strangle-selling risk is large or theoretically unlimited on a gap move; it is controlled by confining the strategy mainly to broad index options, requiring a low (≤25%) "ever" probability of the short strike being touched, and over-funding margin for a worst-case move to the strike. Backspreads and ratio spreads bound the risk profile structurally (a backspread is entered for a net credit so one side always has defined risk; a ratio spread has a defined maximum-risk zone between strikes) but both still carry real loss potential near the short strikes at expiration.

## Caveats

The percentile method requires a maintained historical IV/HV database (200–600+ daily readings per underlying) and Monte Carlo probability software that most retail traders must source independently; McMillan's own worked examples rely on his firm's proprietary tools and website data. The "ever probability ≥ 80%" and "≤ 25%" thresholds are stated as McMillan's personal guidelines, not derived from a published backtest, and he separately suggests 10–15% may be safer than 25% for naked selling — treat the numbers as a starting framework, not a proven optimum. Straddle buying can produce long stretches of flat, decaying premium ("watching paint dry") even when the entry criteria were correctly met; the plan has no time-based stop beyond the 60%-of-cost loss limit and the three-month minimum remaining life at entry.
