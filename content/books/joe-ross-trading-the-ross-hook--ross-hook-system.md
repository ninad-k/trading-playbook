---
title: "The Ross Hook System"
author: "Joe Ross"
year: unknown
slug: joe-ross-trading-the-ross-hook--ross-hook-system
tier: A
category: Trend Following & Mechanical Systems
tags: [ross-hook, 1-2-3-formation, traders-trick-entry, natural-support-resistance, trend-continuation, joe-ross]
difficulty: intermediate
doc_type: system
parent: joe-ross-trading-the-ross-hook
pages: 180
one_liner: "A complete, codeable spec for Joe Ross's Ross Hook: identify the 1-2-3, define the hook, enter on breakout (or earlier via the TTE), filter with a channel study, and stop at natural support/resistance."
related: [tte, richard-l-weissman-mechanical-trading-systems--two-moving-average-crossover, curtis-faith-way-of-the-turtle]
source_file: "Joe Ross - Trading The Ross Hook.pdf"
---

## What it is

A trend-continuation, price-pattern method built on Joe Ross's "1-2-3" formation: point 1 is where a prior move fails, point 2 is the correction's extreme, point 3 is the breakout that retakes point 1 and (re)establishes the trend. The correction between points 1 and 2 leaves a small "pointy" place — the Ross Hook — and trading that hook's breakout, rather than waiting for the larger 1-2-3 breakout, is the core of the system. It is discretionary/pattern-based, not fully mechanical: filters are layered on the price pattern to decide which hooks to take, but no oscillator generates a signal alone.

## Rules

1. **Trend context.** Only look for hooks inside a defined trend (an emerging move whose extreme has been taken out) or an established trend (whose subsequent correction extreme has also been taken out). A pointy place inside congestion (four-plus non-trending bars) is not a valid hook.
2. **Identify the hook.** Whenever a trend is interrupted by a correction, no matter how slight, it leaves a hook: failure to make a new high (uptrend) or new low (downtrend). A double top followed by a lower high, or double bottom followed by a higher low, also counts. A hook does not require a fresh point 1 — it can form directly off an established trend.
3. **Standard entry.** Buy one tick above the hook's high (long) or sell one tick below its low (short), via a resting stop order.
4. **Early entry (Traders Trick Entry).** Enter instead on the violation of a smaller correcting bar after the hook point, if there is enough room to cover costs before the hook's own breakout, and no more than three correcting bars have formed (double/triple extremes count as one). Full mechanics in [[tte]].
5. **Conservative entry (Slaughterbeck entry).** Wait for a confirming higher low (long) or lower high (short), then enter that bar's breakout.
6. **Filter before entering.** Skip the hook unless: CCI (30-bar) is not already at an extreme (±150 lines) against the trade; Stochastics %K has crossed %D (the level of the cross, "overbought"/"oversold," is irrelevant); and price has been trading predominantly on the correct side of a channel study (Bollinger Bands, a 40-bar Keltner Channel at multiplier 5, or ~39–40 bar moving-average bands at ±0.15%) — do not chase a breakout starting outside the channel.
7. **Skip entirely** when: the market is too volatile around the hook; hooks form too close together (more than roughly one-to-three correction bars suggests exhaustion); the hook is too far from the anticipated level; volume has dried up; or the preceding congestion ran too long. A hook forming just before congestion is the highest-risk case.
8. **Position sizing.** Trade only markets where at least two contracts can be capitalized; a single-contract trader is treated as gambling. No percent-of-equity formula is given in the sampled material.

## Risk

Stops use one or a combination of: a **natural support/resistance stop** (one tick beyond a genuine prior swing point); a **cost-covering stop** (sized so a loss roughly breaks even after costs); a **volatility stop** (derived from recent bar-to-bar volatility rather than a fixed distance); and a **trailing stop** once profitable (trail behind each new correcting bar's extreme — a 50% trailing stop is one variant). In a worked S&P 500 example (40-bar Keltner Channel, multiplier 5, 3-minute chart), partial profit is taken around 40–50 points with the remaining stop moved to breakeven, and Ross says a majority of trades reach 50 points of profit. If the market blasts through 50 points with momentum, the stop can be held back to let the remainder run.

## Caveats

Drawn from sampled OCR pages of a scanned book; only a fraction of the text had recoverable OCR, so some worked-example detail and the full "Don't Take That Hook" chapter set were only partially recovered. No system-wide backtest (win rate, profit factor, drawdown) is given — Ross's evidence is individual worked chart examples, not an aggregated track record. The 1-2-3 formation is treated as prior knowledge from Ross's separate "Law of Charts" material. Content reflects late-1990s charting software and phone/floor-broker order norms; the channel-filter parameters were tuned on S&P 500 futures of that era and may need re-fitting elsewhere.
