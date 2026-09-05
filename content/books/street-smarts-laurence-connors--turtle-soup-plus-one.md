---
title: "Turtle Soup Plus One"
author: Laurence A. Connors and Linda Bradford Raschke
year: 1995
slug: street-smarts-laurence-connors--turtle-soup-plus-one
tier: A
category: Swing Trading
tags: [false-breakout, 20-day-breakout, fade-trade, reversal, futures]
difficulty: intermediate
doc_type: system
parent: street-smarts-laurence-connors
pages: 145
one_liner: "Trades a 20-day breakout that reverses on the day after the breakout, using an overnight setup identified the evening before."
related: []
source_file: "Street Smarts (Laurence Connors).pdf"
---

## What it is

A near-identical sibling of Turtle Soup that waits one extra day: instead of fading a false breakout on the same session it occurs, this pattern waits for the market to make a new 20-day extreme with a confirming close, then trades the reversal the following day. Because the setup and confirmation both happen by the prior close, the trader can identify the trade the evening before and place a resting order ahead of time, rather than watching for an intraday reversal — the authors call this the easier of the two Turtle Soup patterns to monitor.

## Rules

**For buys (sells are reversed):**
1. The market makes a new 20-day low, with the prior 20-bar low having occurred at least three trading sessions earlier; day one's close must be at or below that prior 20-bar low (a close-based confirmation, unlike Turtle Soup's intraday-only trigger).
2. The next day (day two), place an entry buy stop at the earlier 20-day low. If not filled on day two, the trade is cancelled — the setup does not carry forward to day three.
3. If filled, place a protective sell stop one tick under the lower of the day-one or day-two low.
4. Take partial profits within two to six bars and trail a stop on the remaining position.

## Risk

Risk is defined the same way as Turtle Soup — one tick beyond the lower of the two setup-day extremes — but because entry occurs on day two rather than intraday on the breakout day, the initial risk distance can be somewhat wider if the market gapped or moved further before triggering. As with Turtle Soup, no fixed percentage-of-equity sizing is specified; the book's general money-management rules (full position at entry, immediate hard stop, scale out into strength) apply. The pattern works identically across timeframes — the source shows both daily-bar examples (bonds, soybeans, S&P, equities) and 10-minute intraday examples using the same "previous 20-bar high/low minus/plus one tick" entry logic.

## Caveats

The authors note the underlying mechanism is likely that a second day of breakout activity draws in the last, most reluctant momentum traders — including those who only act on a closing breakout — making the eventual reversal larger when it comes, but this is offered as a plausible explanation, not a proven one. As with Turtle Soup, the chief drawback is the number of 20-bar highs/lows that do not reverse the following day, producing frequent small losses. No separate backtested statistics are given for this variant; it is presented as evolving directly from Turtle Soup and sharing its general reliability and risk profile, illustrated again purely through annotated historical chart examples (1994-1995 bonds, soybeans, S&P, Delta Air Lines, Texas Instruments) rather than a formal study.
