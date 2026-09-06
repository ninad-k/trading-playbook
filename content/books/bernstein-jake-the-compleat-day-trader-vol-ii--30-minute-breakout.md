---
title: "The 30-Minute Breakout (30MBO)"
author: Jake Bernstein
year: 1998
slug: bernstein-jake-the-compleat-day-trader-vol-ii--30-minute-breakout
tier: A
category: Day Trading & Scalping
tags: [breakout, opening-range, futures, day-trading, trailing-stop, 30-minute-breakout]
difficulty: intermediate
doc_type: system
parent: bernstein-jake-the-compleat-day-trader-vol-ii
pages: 260
one_liner: "Bernstein's flagship Volume II system: buy or sell any half-hour close that exceeds the first 30 minutes' range by a market-specific tick threshold, exiting on a stop, a reversing signal, or the close."
related: [bernstein-jake-the-compleat-day-trader-vol-ii, bernstein-jake-the-compleat-day-trader-vol-i, turtlerules, curtis-faith-way-of-the-turtle]
source_file: "Bernstein, Jake - The Compleat Day Trader Vol II.pdf"
---

## What it is

The 30-Minute Breakout (30MBO) is Bernstein's successor to his earlier Critical Time of Day (CTOD) system from [[bernstein-jake-the-compleat-day-trader-vol-i]] (see [[bernstein-jake-the-compleat-day-trader-vol-i--ctod-critical-time-of-day]]). Instead of committing only once at the end of a fixed opening window, it re-checks for a breakout at the end of every subsequent half-hour bar: if price closes far enough beyond the first half-hour's high or low, a signal fires. Bernstein reports testing it most successfully on major currencies, stock indices, Treasury bonds, several active European futures (Italian Bond, Bund, DAX, FTSE 100, Notionnel), and, when volume is large, coffee, heating oil, crude oil, soybeans, and wheat.

## Rules

1. **Mark the opening range.** Record the high and low price of the first 30 minutes of the session.
2. **Buy signal.** At the end of any subsequent 30-minute bar, if that half-hour's close is above the first half-hour's high by a predetermined number of ticks, buy at the market — the signal can occur at the end of any half-hour after the first, not only the second.
3. **Sell signal.** Mirror-image: a half-hour close below the first half-hour's low by the tick threshold triggers a market sell short, with the same "any half-hour after the first" timing.
4. **Tick threshold is market-specific.** The exact number of ticks is calibrated per market (Bernstein references S&P statistics discussed in the same chapter); no universal tick count applies across instruments, and the specific figures did not survive the sampled OCR pages — this parameter must be sourced separately before the system can be coded for a given market.
5. **Stop-loss.** Use either a predetermined fail-safe ("dead") stop, or exit on the opposite signal (a sell reversing a standing long, or vice versa).
6. **Trailing stop.** Once the position reaches a given profit objective, a trailing stop can follow the trade (the exact calculation is not detailed in the sample).
7. **Reversal on opposite signal.** If a stop-out coincides with an opposite-direction breakout signal, liquidate and establish the new, opposite position rather than simply going flat.
8. **End-of-day exit.** Close any open position a few minutes before the close, or via a market-on-close (MOC) order.
9. **Limit-move override.** If a position moves the daily limit in your favor, take the profit rather than hold for more.
10. **Market filter.** Trade only active markets — suitability can shift over time, so a currently inactive market could later become tradable (or vice versa).

## Risk

Risk per trade is bounded by the stop-loss rule chosen at entry (steps 5-6): a fixed fail-safe stop or an exit on the opposite breakout signal, tightened by a trailing stop once the trade shows a defined profit. Because the entry trigger itself (the tick threshold in step 4) is market-specific and not given as a single figure in the sample, dollar risk per trade cannot be stated generically — it depends on the calibrated tick threshold plus the trader's chosen stop distance beyond that. No percent-of-equity sizing rule is specified.

## Caveats

The central missing figure is the tick threshold that defines a valid breakout — Bernstein says it is "determined by market" and that S&P statistics are "discussed later in this chapter," but that number was not present in the OCR sample used for these notes. Do not substitute an invented value; implementing 30MBO requires sourcing this parameter from the original chapter or independent testing. Likewise, the exact profit objective triggering the trailing stop (step 6) is referenced but not quantified in the sample. As with the rest of the book, examples are calibrated to 1990s futures contracts and trading-hour conventions; applying this to a different instrument or session requires re-deriving both the tick threshold and what counts as the session's "first 30 minutes."
