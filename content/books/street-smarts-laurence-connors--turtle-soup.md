---
title: "Turtle Soup"
author: Laurence A. Connors and Linda Bradford Raschke
year: 1995
slug: street-smarts-laurence-connors--turtle-soup
tier: A
category: Swing Trading
tags: [false-breakout, 20-day-breakout, fade-trade, reversal, futures]
difficulty: intermediate
doc_type: system
parent: street-smarts-laurence-connors
pages: 145
one_liner: "Fades a false 20-day breakout the same day it happens, with a re-entry rule if stopped out on day one or two."
related: []
source_file: "Street Smarts (Laurence Connors).pdf"
---

## What it is

A reversal pattern that trades against a failed 20-day price breakout — the same breakout the 1980s Turtles used as a trend-following entry signal. Because a large fraction of 20-day breakouts fail (particularly outside a strong trend), the setup enters in the opposite direction the moment the market falls back inside the prior 20-day range, on the premise that trapped breakout traders will be forced to cover, fueling a sharp reversal. It trades on any market and any timeframe (daily bars through 10-minute bars are shown), and typically produces trades lasting from a few hours to a few days.

## Rules

**For buys (sells are reversed):**
1. Today must make a new 20-day low — the lower, the better.
2. The prior 20-day low being undercut must have occurred at least four trading sessions earlier.
3. Once price falls below that prior 20-day low, place an entry buy stop 5-10 ticks above the prior 20-day low (good for today only). For equities, use roughly 1/8 point instead of ticks.
4. If filled, immediately place a good-till-cancelled protective sell stop one tick under today's low.
5. As the position becomes profitable, trail the stop to lock in gains — some trades last two to three hours, others a few days, so no fixed time exit is used.
6. **Re-entry rule**: if stopped out on day one or day two of the trade, re-enter on a buy stop at the original entry price (day one/day two only); this modestly improves overall profitability.
7. **Range-expansion exit override**: if the market moves parabolically or produces an outsized range-expansion bar in the trade's favor, take full profits immediately rather than trail a stop — this typically marks the last wave of participants entering (a climax), after which there is nobody left to extend the move.

## Risk

Risk per trade is fixed and tight by construction: one tick beyond the current day's extreme at entry, which the source cites as often well under a point (e.g., a 0.40-point risk on one worked S&P example, 1.05-point loss on another). No fixed percentage-of-equity sizing rule is given in this chapter — sizing is left to the book's Chapter 3 money-management rules (enter the full position at once, never add to it). The strategy trades frequently (the authors cite roughly 15-20 trades/month across 30 futures markets) with a low win rate expected on any single 20-day extreme, so the edge depends on a small number of large reversals — occasionally becoming an intermediate- or longer-term trend change — outweighing many small, quickly stopped-out losses.

## Caveats

The authors state explicitly that this is not a mechanical system: trade management (when exactly to trail, tighten, or exit) is subjective and requires judgment, especially around parabolic moves. A significant drawback is the frequency of 20-day highs/lows that simply do not reverse — these produce many small, time-consuming losing trades with no signal in advance that a given level will hold. Because the setup trades directly against a strongly trending market's breakout, entries can occur just before the trend resumes, so the reversal must be watched closely rather than assumed. No independent backtested win rate or drawdown figures are given for Turtle Soup specifically (unlike some other chapters, which cite Moore Research Center studies in the appendix); the evidence offered is a series of annotated historical chart examples (bonds, S&P, copper, equities, currencies, natural gas) from 1994-1995, not a statistical study.
