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

The 30-Minute Breakout (30MBO) is Bernstein's successor to his earlier Critical Time of Day (CTOD) system from [[bernstein-jake-the-compleat-day-trader-vol-i]] (see [[bernstein-jake-the-compleat-day-trader-vol-i--ctod-critical-time-of-day]]). Instead of committing only once, at the end of a fixed opening window, the 30MBO re-checks for a breakout at the end of every subsequent half-hour bar of the session: if price closes far enough beyond the first half-hour's high or low, a signal fires. Bernstein reports testing it most successfully on major currencies, stock indices, Treasury bonds, several active European futures (Italian Bond, Bund, DAX, FTSE 100, Notionnel), and, when volume is reasonably large, coffee, heating oil, crude oil, soybeans, and wheat.

## Rules

1. **Mark the opening range.** Record the high and low price of the first 30 minutes of the trading session.
2. **Buy signal.** At the end of any subsequent 30-minute bar, if the closing price of that half-hour is above the first half-hour's high by a predetermined number of ticks, buy at the market. The signal can occur at the end of any half-hour after the first, not only the second half-hour.
3. **Sell signal.** At the end of any subsequent 30-minute bar, if the closing price of that half-hour is below the first half-hour's low by a predetermined number of ticks, sell short at the market — same "any half-hour after the first" timing as the buy signal.
4. **Tick threshold is market-specific.** The exact number of ticks required is calibrated per market (Bernstein references S&P futures statistics discussed in the same chapter); no single universal tick count applies across instruments, and the specific figures did not survive in the sampled OCR pages — this parameter must be derived or sourced separately before the system can be coded for a given market.
5. **Stop-loss.** Use either a predetermined fail-safe ("dead") stop, or exit on the opposite signal (a sell signal reversing a standing long, or vice versa).
6. **Trailing stop.** Once the position has reached a given profit objective, a trailing stop loss can be used to follow the trade (the specific trailing-stop calculation is not detailed further in the sampled pages).
7. **Reversal on opposite signal.** If a stop-out coincides with an opposite-direction breakout signal, liquidate the current position and establish the new, opposite position rather than simply going flat.
8. **End-of-day exit.** Close any still-open position either a few minutes before the session close or via a market-on-close (MOC) order.
9. **Limit-move override.** If a long position moves limit-up in your favor (or a short moves limit-down in your favor) in a market with a daily trading limit, take the profit rather than holding for a further move.
10. **Market filter.** Trade the 30MBO only in active markets — Bernstein notes that market suitability can change over time, and a currently inactive market could later become tradable with this method (or vice versa).

## Risk

Risk per trade is bounded by the stop-loss rule chosen at entry (steps 5-6): either a fixed fail-safe stop or an exit on the opposite breakout signal, later tightened by a trailing stop once the trade shows a defined profit. Because the entry trigger itself (the tick threshold in step 4) is market-specific and not given as a single figure in the sampled pages, the dollar risk per trade cannot be stated generically — it depends on both the calibrated tick threshold for the instrument being traded and the trader's chosen stop distance beyond that. No percent-of-equity position-sizing rule is specified in the sampled pages.

## Caveats

The central missing figure is the tick threshold that defines a valid breakout — Bernstein explicitly says it is "determined by market" and that "the statistics for S&P futures are shown and discussed later in this chapter," but that specific number was not present in the OCR sample used for these notes. Do not substitute an invented value; a trader implementing 30MBO must source this parameter from the original chapter (or from independent testing) before treating the system as fully specified. Likewise, the exact profit objective that triggers the trailing-stop rule (step 6) is referenced but not quantified in the sampled pages. As with the rest of the book, examples and market suitability are calibrated to 1990s futures contracts and trading-hour conventions; a trader applying this to a different instrument or session structure will need to re-derive both the tick threshold and what counts as the session's "first 30 minutes."
