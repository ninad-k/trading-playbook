---
title: "The Ross Hook System"
author: "Joe Ross"
year: unknown
slug: joe-ross-trading-the-ross-hook--ross-hook-system
tier: A
category: Trend Following & Mechanical Systems
parent: joe-ross-trading-the-ross-hook
pages: 180
one_liner: "A complete, codeable spec for Joe Ross's Ross Hook: identify the 1-2-3, define the hook, enter on breakout (or earlier via the TTE), filter with a channel study, and stop at natural support/resistance."
related: [tte, richard-l-weissman-mechanical-trading-systems--two-moving-average-crossover, curtis-faith-way-of-the-turtle]
source_file: "Joe Ross - Trading The Ross Hook.pdf"
doc_type: system
---

## What it is

A trend-continuation, price-pattern trading method built on Joe Ross's "1-2-3" formation. Point 1 is where a prior move fails to continue; point 2 is the extreme of the correction that follows; point 3 is the breakout that retakes the point-1 level and (re)establishes the trend. The correction between points 1 and 2 leaves behind a small "pointy" place on the chart — the Ross Hook — and trading the breakout of that hook, rather than waiting for the larger 1-2-3 breakout, is the core of the system. The method is discretionary/pattern-based rather than fully mechanical: technical filters are layered on top of the price pattern to decide which hooks are worth taking, but no oscillator or study generates a signal on its own.

## Rules

**1. Establish trend context.** Only look for hooks inside a defined trend (an emerging move whose extreme has been taken out) or an established trend (a defined trend whose subsequent correction has also been taken out). A "pointy" place that forms inside congestion (four or more non-trending bars) is not a valid hook and must be ignored.

**2. Identify the hook.** Formal definition: whenever a market trend is interrupted by a correction, no matter how slight, it leaves behind a Ross Hook.
- In an uptrend: failure of price to make a new high constitutes a hook at that point. A double top (two consecutive equal highs) followed by a lower high also counts.
- In a downtrend: failure of price to make a new low constitutes a hook. A double bottom followed by a higher low also counts.
- A hook does not require a prior "point 1" — it can form directly off an established trend without a fresh 1-2-3 needing to be redrawn each time.

**3. Entry — standard breakout.** Buy one tick above the highest high of the hook (long case), or sell one tick below the lowest low of the hook (short case). Use a resting (stop) order at that level.

**4. Entry — early alternative (Traders Trick Entry).** Instead of waiting for the hook's own breakout, enter on the violation of a smaller "correcting bar" that forms after the hook point (bars making lower highs, for a long setup, without necessarily making lower lows). Conditions: (a) there must be enough room between the earlier entry and the hook's own breakout level to cover trading costs and bank some profit; (b) no more than three correcting bars are allowed before the setup is abandoned (a double/triple extreme among them counts as one bar); (c) the underlying 1-2-3/hook must have formed at the end of a trend, not inside consolidation. Full entry mechanics are in [[tte]].

**5. Entry — conservative alternative (Slaughterbeck entry).** Wait instead for confirmation — a higher low after the hook (long case) or a lower high (short case) — and enter on the breakout of that confirming bar. Slower and lower-risk than both the standard breakout and the TTE.

**6. Filter before entering.** Skip a hook unless a secondary study confirms it:
- CCI (30-bar) should not already be at an extreme (±150 reference lines) against the trade direction.
- Stochastics: only the %K/%D crossover matters, not "overbought"/"oversold" readings — a market can stay pinned at an extreme for long stretches while trending.
- Channel filters (Bollinger Bands, or a 40-bar Keltner Channel with a multiplier of 5, or ~39–40 bar moving-average bands at roughly ±0.15%): only take the hook breakout if price has been trading predominantly on the correct side of the channel; do not chase a breakout that starts outside the channel against the recent range.

**7. Situations to skip entirely.** Do not take the hook when: the market is too volatile immediately around the hook; hooks are forming too close together (a healthy trend move should show roughly one to three bars of correction before resuming — more suggests exhaustion); the hook is too far from the level being anticipated; volume has dried up; or the preceding congestion has run an unusually long time. A hook that forms just before congestion begins is specifically flagged as the highest-risk case, since the last hook in a series often marks the start of a reversal or an extended sideways period rather than a continuation.

**8. Position sizing.** Trade only markets where at least two contracts can be capitalized; a single-contract trader is, in Ross's framing, effectively gambling rather than trading a business. No specific percent-of-equity risk formula is given in the sampled material.

## Risk

Stops are placed using one (or a combination) of four techniques rather than a fixed percentage:
- **Natural support/resistance stop** — one tick beyond the nearest genuine prior swing point, so the stop is only hit on a real structural violation.
- **Cost-covering stop** — sized so a losing trade approximately breaks even once commissions are netted against the small profit cushion built into the entry ("free trade" framing).
- **Volatility stop** — derived from a rolling study of the market's own recent bar-to-bar volatility rather than a fixed tick distance.
- **Trailing stop** — once profitable, trail behind each new correcting bar's extreme; Ross discusses both a "50% trailing stop" (giving back roughly half of open profit) and harder full/small profit-lock variants.
On a worked S&P 500 intraday example (40-bar Keltner Channel, multiplier 5, 3-minute chart), partial profit is taken around 40–50 points with the remaining stop moved to breakeven; about 90% of the time no further stop management is needed once that point is reached.

## Caveats

These notes are drawn from sampled OCR pages of a scanned book; only a fraction of the text (front matter plus evenly spaced pages) had recoverable OCR, so some worked-example detail and the full "Don't Take That Hook" chapter set were only partially recovered. No system-wide backtest (win rate, profit factor, drawdown) is given for the Ross Hook itself in the sampled material — Ross's evidence is a series of individual worked chart examples, not an aggregated track record. The 1-2-3 formation this system depends on is treated as prior knowledge from Ross's separate "Law of Charts" material rather than fully re-derived here. Content reflects late-1990s charting software and order-execution norms (phone/floor-broker orders); the underlying price-pattern logic is timeframe- and instrument-agnostic, but the specific channel-filter parameters (Keltner multiplier, moving-average band width) were tuned on S&P 500 futures of that era and may need re-fitting elsewhere.
