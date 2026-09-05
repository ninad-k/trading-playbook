---
title: "The Fibonacci-Candlestick-Chart-Pattern Confluence Method"
author: "Robert Fischer, Jens Fischer"
year: 2003
slug: candlesticks-fibonacci-and-chart-pattern-trading-tools--confluence-method
tier: A
category: "Fibonacci, Gann & Elliott Wave"
doc_type: system
parent: candlesticks-fibonacci-and-chart-pattern-trading-tools
pages: 273
one_liner: "Trade a 61.8% Fibonacci retracement only when a candlestick reversal pattern or a 3-point chart pattern confirms it, instead of entering on the retracement level alone."
related: [fischer-robert-fibonacci-applications-and-strategies-for, elliott-waves-principle, greg-morris-candlestick-charting-explained]
source_file: "Candlesticks Fibonacci and Chart Pattern Trading Tools.pdf"
---

## What it is

A countertrend, swing-timeframe entry method that requires two independent signals to align before entering: (1) price has retraced a defined Fibonacci percentage of the prior swing, and (2) either a candlestick reversal pattern or a completed 3-point chart pattern confirms the reversal at that level. The book demonstrates it is a materially better filter than trading the Fibonacci level alone, using matched before/after trade logs on the same S&P 500 window (Dec 2001-Apr 2002).

## Rules

**1. Define the swing and correction level.**
- Identify the prior impulse swing (peak-to-valley or valley-to-peak) using a minimum swing size calibrated per instrument (30 basis points was used for the S&P 500 example; must be found by testing historical data — too small over-generates signals, too large yields none).
- Working correction levels, derived from the PHI series (1.000, 0.618, 1.618): 38.2% (= 0.618 ÷ 1.618), 50.0%, and 61.8% (= 1.000 ÷ 1.618). The book's default and most-tested level is 61.8%, chosen because 38.2% enters too early (more false signals) and waiting past 61.8% risks missing the move entirely.

**2. Do not enter on the retracement level alone.** Stand-alone entry the instant price reaches 61.8% of the prior swing produced a losing trade log in the book's own test (9 trades, mostly stopped out) — used deliberately as the baseline this method improves on.

**3. Entry trigger — candlestick confirmation variant.**
- Wait for the 61.8% (or, per Additional Fibonacci Correction Levels, 38.2%/50.0% with the same logic) retracement level to be reached.
- Enter only when a recognizable candlestick reversal pattern completes at/near that level: hammer, bullish/bearish belt-hold, bullish/bearish engulfing, harami/harami cross, doji, piercing pattern/dark-cloud cover, or morning/evening star.
- Stop-loss at the prior swing high (for shorts) or swing low (for longs).
- Once in profit, trail with a 3-day high/low trailing stop.

**4. Entry trigger — 3-point chart pattern confirmation variant.**
- Same swing size and 61.8% retracement level as above.
- Entry on a 1-day high/low "backward look" once the correction level is reached, filtered by watching for 3-point patterns (double top/bottom, triple top/bottom, head and shoulders) that would otherwise have triggered a losing stand-alone entry — the book's re-examination of its own baseline trade log shows specific losing signals that a double top, double bottom, triple bottom, quadruple top, or triple top would have flagged in advance.
- Stop-loss at the previous swing high/low; re-entry (a "re-sell short" / "re-buy long") is permitted after being stopped out if the pattern re-forms.
- 3-day high/low trailing stop once in profit, same as the candlestick variant.

**5. Optional third confirmation — PHI-ellipse or trend channel.** For the most conservative entries, require the price move to also break the outer line of a PHI-ellipse or a parallel trend channel drawn around the same swing (a "double confirmation"). This gives up some profit potential (later entry) in exchange for avoiding losing trades in strongly trending conditions.

**6. Calibrate per instrument.** Swing size must be re-derived for each product from its own volatility (the book's examples: 30 bp for the S&P 500 index; different price-unit swing sizes for Microsoft and Allianz, which trade at very different absolute price levels). Smaller swing size produces more, smaller trades; larger swing size produces fewer, larger trades or none at all.

## Risk

Stop-loss is always placed at the swing extreme that defined the correction (prior swing high for a short, prior swing low for a long) — a level determined by market structure, not a fixed percentage or dollar amount. Once profitable, both confirmation variants use a 3-day high/low trailing stop to lock in gains rather than a static profit target. The book does not specify position sizing or percent-of-equity risk per trade; risk control in this method is entirely about signal filtering (fewer, better-confirmed entries) and stop placement, not capital allocation. In the book's own comparative test, adding candlestick confirmation reduced trade count from 9 to 7 and reduced (but did not eliminate) stop-outs; adding 3-point-pattern confirmation with a re-entry rule produced 9 trades but with a better win/loss mix than the unconfirmed baseline.

## Caveats

Tested only on a handful of instruments (S&P 500, Microsoft, Allianz) over short windows (roughly 4-12 months each) — not a large-sample statistical validation. Swing size, the single most consequential parameter, has no formula and must be hand-calibrated per instrument from historical data. Candlestick pattern recognition and 3-point pattern identification both retain a discretionary, chart-reading component that resists full mechanization. The method assumes retracements will occur within a bounded, identifiable swing structure; in a strongly trending market with shallow corrections, the 61.8% level may never be reached, and the book's own trending-market example (Microsoft) shows far fewer trades than the sideways-market example (Allianz).
