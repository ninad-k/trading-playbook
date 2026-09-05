---
title: "Critical Time of Day (CTOD)"
author: Jake Bernstein
year: 1995
slug: bernstein-jake-the-compleat-day-trader-vol-i--ctod-critical-time-of-day
tier: A
category: Day Trading & Scalping
tags: [opening-range-breakout, trailing-stop, futures, day-trading, ctod]
difficulty: intermediate
doc_type: system
parent: bernstein-jake-the-compleat-day-trader-vol-i
pages: 242
one_liner: "Bernstein's opening-range breakout system: trade the break of the first two hours' 5-minute closing-price range, with a 5-minute-close trailing stop that ratchets in hourly."
related: [bernstein-jake-the-compleat-day-trader-vol-i, bernstein-jake-the-compleat-day-trader-vol-ii, turtlerules]
source_file: "Bernstein, Jake - The Compleat Day Trader Vol I.pdf"
---

## What it is

CTOD is an intraday opening-range breakout system: it defines a trading range from the first two hours of the session using 5-minute closing (not high/low) prices, then trades the break of that range in either direction, confirmed on a 5-minute closing basis rather than an intraday tick touch. It targets active, liquid markets — Bernstein names currencies, stock indices, and Treasury bonds — and is Bernstein's earlier alternative to the newer breakout methods he developed later (see [[bernstein-jake-the-compleat-day-trader-vol-ii]] for the 30-Minute Breakout).

## Rules

1. **Build the range.** Track 5-minute closing prices for the first 2 hours of the trading session. The highest of these closes becomes the buying breakout level; the lowest becomes the selling breakout level.
2. **Buy signal.** Once a 5-minute close prints above the highest 5-minute closing level of the first 2 hours, buy at the market.
3. **Sell signal.** Once a 5-minute close prints below the lowest 5-minute closing level of the first 2 hours, sell short at the market.
4. **Initial stop-loss.** On a long entry, use a 5-minute closing stop below the lowest closing 5-minute plot of the first 2 hours (the mirror-image level of the sell signal). On a short entry, use a 5-minute closing stop above the highest closing 5-minute plot of the first 2 hours.
5. **Trailing stop.** As the trade runs, trail the stop using a 5-minute-close basis: for a long, exit on a 5-minute close below the lowest 5-minute close of the previous completed hour; for a short, exit on a 5-minute close above the highest 5-minute close of the previous completed hour. The stop ratchets in with each new hour that completes.
6. **Alternative stop.** In place of the 5-minute-close trailing stop, a fixed money-management stop or a stop derived from another indicator in the book (e.g., a moving average or oscillator) may be substituted.
7. **Exit.** Close the position by the end of the trading day if not already stopped out, or exit when the trailing/alternative stop is hit, whichever comes first.
8. **Parameter experimentation.** Bernstein suggests testing alternative range windows (e.g., 1 hour or 1.5 hours) rather than the standard 2 hours, since different markets may respond better to a shorter or longer opening-range window.

## Risk

Risk per trade is bounded by the distance from entry to the opposite-side 5-minute closing stop in step 4, set by the width of the first two hours' closing range rather than a fixed dollar or percent figure — a wider morning range means wider initial risk. No percent-of-equity sizing rule is given; the trader sizes the position so the range-derived stop distance matches an acceptable dollar loss. The hourly-ratcheting trailing stop (step 5) is the system's primary mechanism for protecting profit once the trade is working, not a separate profit target.

## Caveats

The 2-hour window is a default, not a fixed requirement — Bernstein invites testing 1-hour or 1.5-hour variants, so "2 hours" should be read as a starting parameter, not an optimized constant. No win rate, average trade, or drawdown statistic for CTOD specifically survives the sampled OCR pages (unlike some of the book's other systems, which do include performance tables); its support here is the rule description and qualitative tips, not a backtest. The system assumes an actively-traded instrument with meaningful intraday range in the first two hours — Bernstein notes it works best in currencies, stock indices, and Treasury bonds, and cautions that market suitability can shift over time.
