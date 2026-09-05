---
title: TD Sequential for Options
author: Thomas R. DeMark, Thomas R. DeMark Jr.
year: 1999
slug: demark-tom-demark-on-day-trading-options--td-sequential-options
tier: A
category: Options, Futures & Derivatives
tags: [td-sequential, option-buying, exhaustion, setup, countdown, in-the-money]
difficulty: advanced
doc_type: system
parent: demark-tom-demark-on-day-trading-options
pages: 364
one_liner: "DeMark's Setup/Countdown bar-counting method for timing trend exhaustion, applied to buying near-term in-the-money calls or puts instead of trading the underlying directly."
related: []
source_file: "DeMark,Tom - DeMark on day-trading options.pdf"
---

## What it is

TD Sequential is DeMark's proprietary bar-counting method for identifying when a trend is likely exhausted and due to reverse. In this book it is applied not to trade the underlying stock, futures contract, or index directly, but to time the purchase of a short-dated, in-the-money call (on a completed buy signal) or put (on a completed sell signal), so that risk is capped to the option premium while the trader still captures the anticipated reversal. It works identically on any bar interval — daily charts down to one-minute intraday bars — which is what makes it usable for day trading.

## Rules

**Step 1 — Price flip (initiates a Setup)**: a buy Setup begins when a bar's close is less than the close 4 bars earlier, immediately after a prior bar whose close was greater than or equal to the close 4 bars earlier (the reverse — a close greater than the close 4 bars earlier, following a prior close less than or equal to the close 4 bars earlier — initiates a sell Setup).

**Step 2 — Setup count**: from the price-flip bar (numbered 1), count consecutive bars whose close continues to satisfy the same condition: less than the close 4 bars earlier for a buy Setup, greater than the close 4 bars earlier for a sell Setup. A completed Setup requires at least 9 such consecutive bars, numbered 1 through 9 on the chart.

**Step 3 — Cancellation**: if, before reaching a count of 9, a bar's close breaks the run (for a buy Setup: a close greater than or equal to the close 4 bars earlier; for a sell Setup: a close less than or equal to the close 4 bars earlier), the count is canceled and erased, and a new Setup phase must begin from the next qualifying price flip. A Setup can also be nullified after completion if a subsequent Setup's true range is fully contained within (or a recent Setup recycles within) a prior Setup's range — in that case the completed count stays on the chart but does not proceed to Countdown.

**Step 4 — Entry qualifier**: before acting on a completed buy Setup, the low of the 7th, 8th, or 9th bar of the count must satisfy an additional qualifying condition before it is used to justify a purchase (of the underlying, or of a call option); the mirror condition (using the highs of bars 7–9) applies to a completed sell Setup before buying a put. (The book's precise statement of this qualifying condition was not present in the sampled OCR pages — see Caveats.)

**Step 5 — Intersection and Countdown**: once a Setup is complete and not nullified, the method moves to an Intersection step and then a Countdown phase — a further, separate bar count used to pinpoint a more precise "buy-low, sell-high" exhaustion point beyond the Setup signal alone, before the actual entry is taken. TD Combo is presented as an alternate Setup/Countdown variant that can be run alongside TD Sequential for comparison or confirmation.

**Step 6 — Option selection at entry**: on a qualified buy signal, buy a near-term, in-the-money call (small time-value premium, price tracks the underlying closely); on a qualified sell signal, buy a near-term, in-the-money put. The book's stated preference is to buy options outright rather than use spreads, covered writes, or straddles for this style of trade.

## Risk

Risk is capped structurally by using options rather than the underlying: the maximum loss on any single entry is the premium paid. Beyond that, the book's day-trading stop-loss discipline is explicitly non-formulaic — no fixed stop for inexpensive options or small positions (the position is simply allowed to run to expiration or an opposing indicator signal), and a dollar-amount stop (not a percentage or technical level) for costly options or larger positions. Additional low-risk exits are drawn from the indicators themselves — an opposing TD Sequential/TD Combo signal, or a break of a TD Line/TD REBO level in the other direction — rather than from a stated percent-of-equity risk rule. Unexercised, out-of-the-money expiration is treated as an inherent, no-action stop-loss unique to option buying.

## Caveats

The Setup-phase rules above (price flip, 9-bar count, cancellation, and the existence of a 7th/8th/9th-bar qualifier) are drawn directly from sampled OCR text. The exact bar-by-bar comparison rules for the Countdown phase (commonly a 13-count in DeMark's published work generally) were not present in the sampled pages of this scan and are not stated here to avoid inventing detail; treat Countdown as "a further exhaustion count following Setup" until verified against the original text or another DeMark source. The book presents TD Sequential as an indicator requiring trader judgment, not a fully mechanical system with a published, quantified track record — DeMark explicitly frames it that way in the foreword. Because this scan's text came from a sampled subset of pages, the qualifier condition in Step 4 and the exact Countdown mechanics should be treated as incomplete rather than definitive.
