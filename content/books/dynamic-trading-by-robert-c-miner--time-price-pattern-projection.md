---
title: Dynamic Trading — Time, Price and Pattern Projection Method
author: Robert C. Miner
year: 1997
slug: dynamic-trading-by-robert-c-miner--time-price-pattern-projection
tier: A
category: Fibonacci, Gann & Elliott Wave
tags: [elliott-wave, fibonacci, time-cycles, price-projection, cluster-analysis]
difficulty: advanced
doc_type: system
parent: dynamic-trading-by-robert-c-miner
pages: 505
one_liner: "Project trend-reversal zones in advance by clustering Fibonacci price ratios, Fibonacci time ratios, and a completed Elliott Wave pattern at the same point."
related: [dynamic-trading-by-robert-c-miner, elliott-waves-principle, fischer-robert-fibonacci-applications-and-strategies-for, fibonacci-ratios-with-pattern-recognition]
source_file: "Dynamic.Trading.by.Robert.C..Miner.pdf"
---

## What it is

Miner's core analytical method for anticipating (not merely reacting to) trend changes. Rather than trading a single indicator, the method requires three independent lines of evidence to agree on the same zone before a reversal is treated as high-probability: (1) a recognizable Elliott Wave pattern position (impulse or ABC correction) that is at or near completion, (2) a cluster of Fibonacci price-ratio projections converging on a narrow price zone, and (3) a Fibonacci time-ratio projection (a Time Cycle Ratio) landing on or near the same dates, ideally confirmed by an overlapping Time Rhythm Zone. The method is descriptive/analytical — it identifies where and when to expect a reversal — and is paired separately with the entry-trigger and stop rules used to actually take the trade.

## Rules

**Step 1 — Establish wave position (pattern).** Identify whether the market is in a five-wave impulse sequence or a three-wave (ABC, or complex) correction, using two or three degrees of trend (minor, intermediate, major). Validate against the three Elliott rules: wave 2 cannot retrace past the start of wave 1; wave 3 is never the shortest of waves 1/3/5; wave 4 may not close in wave 1's price range. If no clean count is identifiable (true roughly half the time), do not force one — proceed on price/time projections alone or skip the market.

**Step 2 — Project price.** Compute the standard price-ratio projections for the current wave using the Fibonacci ratio set (.236, .382, .500, .618, .786, 1.00, 1.272, 1.618, 2.000, 2.618, 4.236). Typical target ratios by wave:

| Wave being projected | Ratio and reference |
|---|---|
| Wave 2 | 50%–78.6% retracement of Wave 1 |
| Wave 3 | ≥100% of Wave 1, then 162% or 262% of Wave 1 |
| Wave 4 | 23.6%–50% retracement of Wave 3 (must not enter Wave 1's range) |
| Wave 5 | 62%, 100%, or 162% of Wave 1; or 38%/62% of Waves 1–3; or 127%/162%/200%/262% of Wave 4 |
| Wave C | 62%, 100%, or 162% of Wave A; or 162%, 200%, or 262% of Wave B |

A single projection is weak; a **cluster** of at least two or three independent projections (from different wave comparisons, and ideally from two different wave degrees) landing within a narrow price band is the actionable signal.

**Step 3 — Project time.** Apply the same Fibonacci ratios to time spans instead of price spans:
- **Time Retracement (TR)** — a ratio (commonly 38.2%, 50%, 61.8%, 100%) of the calendar or trading days in one swing, projected forward from the end of the next swing.
- **Alternate Time Projection (ATP)** — the time span of one swing projected by a Fibonacci ratio from the start or end of a different swing (analogous to the price Alternate Price Projection).
- **Time Rhythm Zone (TRZ)** — separately, build a swing-duration history (low-to-low, high-to-low, etc.) for the current major/minor trend direction only (bull swings and bear swings kept in separate samples), drop the shortest and longest 10% of durations, and take the overlap of the two remaining 80% ranges (e.g., low-to-low overlapped with high-to-low for a projected low). This produces a broad probable window; TCR projections falling inside that window are high-probability specific dates.

**Step 4 — Require coincidence.** Treat a reversal as high-probability only when: a price-projection cluster, a time-projection date (or narrow date range, typically 2–4 trading days), and a wave-pattern completion (or invalidation trigger) all fall together. Two of the three factors agreeing is usable; when all three coincide, Miner reports historical hit rates high enough to trade with tight risk.

**Step 5 — Confirm with multiple degrees.** Prefer projections confirmed from both a smaller and a larger wave degree (e.g., the internal five-wave subdivision of wave 5 projecting the same zone as the larger wave 5 itself). When the two degrees don't overlap exactly but are close, favor the smaller-degree target as the more precise one.

## Risk

This is a projection/analysis method, not an entry system by itself; risk is defined operationally by pairing it with one of the daily-bar entry triggers described in the companion "entry strategies" system page (Reversal Day, Signal Day, Snap-Back Reversal Day, etc.), each of which has its own explicit stop placement (typically one tick beyond the signal-day extreme or the last invalidating pivot). The wave count itself supplies a natural "pattern stop-loss": the same price level that would violate an Elliott rule (e.g., wave 2 exceeding the start of wave 1, or wave 4 closing in wave 1's range) is used directly as the stop, so risk and analysis share one source of truth. No fixed percentage-of-equity sizing rule is given; position size is bounded by a pre-set maximum dollar capital-exposure per trade defined in the trader's own plan.

## Caveats

Roughly half the time no clean, three-rule-compliant Elliott Wave count exists, and Miner is explicit that forcing one is worse than having no pattern opinion at all — the method degrades gracefully to price/time-only analysis in that case, but that materially reduces its edge. Time Rhythm Zone projections can rest on small samples (as few as five to seven historical swings in Miner's own examples), so the "80% range" claim carries real statistical uncertainty despite being presented with precision. The projection ratios are stated as typical/frequent, not universal — several examples in the source book show markets terminating well outside the ideal ratio zones, or wave four trading briefly into wave one's range without invalidating the sequence in Miner's own judgment. The method assumes swing (daily/weekly bar) trading; it was not designed or illustrated for sub-daily intraday timeframes.
