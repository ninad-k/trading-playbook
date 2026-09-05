---
title: "The Profitunity / Alligator System"
author: Bill Williams
year: 1998
slug: bill-williams-new-trading-dimensions-how-to-profit-from-chaos-in-stocks-bonds-and-commodit--profitunity-alligator-system
tier: A
category: Trend Following & Mechanical Systems
tags: [chaos-theory, alligator, fractals, awesome-oscillator, mechanical-system]
difficulty: intermediate
doc_type: system
parent: bill-williams-new-trading-dimensions-how-to-profit-from-chaos-in-stocks-bonds-and-commodit
pages: 102
one_liner: "A five-indicator, Alligator-gated trend system: enter on a fractal breakout, add on with AO/AC/Zone/Balance Line signals, exit on a tiered stop hierarchy."
related: [bill-williams-trading-chaos, elliott-waves-principle]
source_file: "Bill Williams - New Trading Dimensions - How To Profit From Chaos In Stocks, Bonds, And Commodities.pdf"
---

## What it is

A fully mechanical trend-following system ("Profitunity") for any market or timeframe. Five indicators ("dimensions") generate entries — Fractal, Awesome Oscillator (AO), Accelerator/Decelerator (AC), Zone, and Balance Line — but none is tradable until price first breaks out of a three-line moving-average envelope called the Alligator, which also sets the allowed trade direction. Once triggered, the system adds on aggressively to every same-direction signal from any of the five dimensions, aiming to capture 3–5x the size of the underlying trend move, then exits on a ranked stop hierarchy.

## Rules

**Indicator construction**
- Alligator: Jaw (blue) = 13-bar smoothed moving average (SMMA) of bar midpoint `(H+L)/2`, plotted 8 bars forward. Teeth (red) = 8-bar SMMA, plotted 5 bars forward. Lips (green) = 5-bar SMMA, plotted 3 bars forward.
- Fractal: a 5-bar pattern where the middle bar's high is higher than the 2 bars on each side (buy fractal), or the middle bar's low is lower than the 2 bars on each side (sell fractal).
- AO: `SMA(5, midpoint) − SMA(34, midpoint)`, plotted as a colour-coded histogram (green if higher than prior bar, red if lower).
- AC: a 5-bar SMA of the difference between AO and a 5-bar SMA of AO; also colour-coded green/red.
- Zone: Green when both AO and AC bars are green; Red when both are red; Gray when they disagree.
- Balance Line: for entry purposes, use the Blue Alligator line itself as the reference "Balance Line."

**Entry sequence**
1. Wait for the Alligator's three lines to intertwine ("sleeping") — a signal the market is range-bound and a trend has not yet started.
2. First entry only on a fractal whose middle-bar high/low is outside (above/below) the Alligator's mouth. Place a buy stop 1 tick above a buy fractal's high, or a sell stop 1 tick below a sell fractal's low. A fractal on the wrong side of the Teeth (red line) is invalid and must be ignored.
3. Once the first fractal is hit, go aggressive: take every subsequent same-direction signal from any dimension, filtered only by remaining outside the Alligator's mouth ("do not feed the Alligator" — never buy below the mouth or sell above it).
   - AO: Saucer (3-bar colour reversal on one side of zero), zero-line Cross, or Twin Peaks (second peak shallower than the first, same side of zero). Stop 1 tick beyond the corresponding price bar.
   - AC: 2 same-colour bars off a peak/trough if AC has already crossed zero in the trade's favour; 3 bars required if AC is still on the opposite side of zero. Crossing zero is not itself a signal, only a bar-count reducer.
   - Zone: while in Green (long) or Red (short) Zone, add on the close of every consecutive same-colour bar; stop adding new Zone-based positions after 5 consecutive same-colour bars (other-dimension signals can still be taken).
   - Balance Line: from a base bar (current bar or most recent opposite extreme), 1 new high/low if moving away from the Balance Line, 2 if moving toward it; double the requirement again if the current bar is in the unfavourable zone (buying while Red, selling while Green).
4. A signal not filled before the indicator reverses colour is cancelled. Always take the most recently formed, nearest signal in a given direction — earlier signals are superseded.

## Risk

No fixed percentage or dollar risk rule is given in the source; the book explicitly rejects "never risk over 2% of equity" as an ungrounded, non-market-derived rule. Risk control is entirely stop-placement based:
- Initial stop: placed just inside the Alligator's Teeth (red line) immediately after the first fractal-breakout entry, as a stop-close-only (not intrabar) order.
- Losses from this first, low-conviction breakout are treated as an accepted cost of early positioning ("low-rent district" trades) — no target win rate or max-loss-per-trade figure is stated.
- No position-sizing formula (fixed fractional, volatility-based, or otherwise) is provided; examples in the book use a flat 1 contract or 100 shares per signal for illustration only.

## Caveats

The exit and add-on rules are precise enough to code, but several pieces this system is known for elsewhere are missing from this particular book: the Market Facilitation Index (MFI) is mentioned only as "closely approximated by AO" and is not defined or given entry/exit rules here (see the earlier *Trading Chaos* for that). No money-management or position-sizing rule is supplied, so this cannot be run as a complete system without importing risk rules from elsewhere (e.g. [[money-management-report-van-tharp]]). Reported results in the book are a small number of hand-picked 3-month chart examples, not a systematic backtest, so the stated "3–5x the trend move" and "~10% per month" targets should be treated as illustrative rather than statistically validated. The system also assumes markets trend 15–30% of the time and produces frequent whipsaw losses ("low-rent district" trades) during the remainder, which the book does not quantify.
