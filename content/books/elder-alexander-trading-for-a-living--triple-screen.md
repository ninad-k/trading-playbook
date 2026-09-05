---
title: Triple Screen Trading System (Original)
author: Alexander Elder
year: 1993
slug: elder-alexander-trading-for-a-living--triple-screen
tier: A
category: Trading Psychology & Discipline
tags: [triple-screen, multi-timeframe, trend-following, oscillators, macd-histogram]
difficulty: intermediate
doc_type: system
parent: elder-alexander-trading-for-a-living
pages: 312
one_liner: "Elder's original 1993 multi-timeframe method: weekly MACD-Histogram slope sets direction, a daily oscillator times entries, intraday trailing stops execute."
related: [come-into-my-trading-room-elder-alexander--triple-screen]
source_file: "Elder Alexander - Trading For A Living.pdf"
---

## What it is

Triple Screen is Elder's method for resolving the conflict between trend-following indicators (good in trends, bad in ranges) and oscillators (good for timing, bad at riding trends) by applying them to two different timeframes in a fixed sequence, plus a third, order-placement "screen." This is the system's original 1993 presentation: a weekly chart sets strategic direction, a daily chart times the entry against a short-term pullback, and an intraday trailing-stop technique places the actual order. Elder's own later revision, described in [[come-into-my-trading-room-elder-alexander--triple-screen]], updates the Screen One indicator and adds an explicit risk-sizing rule (the 2% Rule tie-in) and alternate order-placement options; treat that later page as an update to this one, not a contradiction.

## Rules

**Screen One (weekly chart, strategic)**: plot a trend-following indicator on the weekly chart. In this original version, Elder's primary signal is the slope of weekly MACD-Histogram: a rising slope identifies an uptrend (trade long or stand aside only); a falling slope identifies a downtrend (trade short or stand aside only).

**Screen Two (daily chart, tactical)**: only take a daily oscillator signal that goes *against* the current short-term daily move but *with* the weekly trend — i.e., use a dip in a daily oscillator during a weekly uptrend to prepare a long entry, and a rally in a daily oscillator during a weekly downtrend to prepare a short entry. Summary table:

| Weekly trend | Daily trend (oscillator) | Action | Order type |
|---|---|---|---|
| Up | Up | Stand aside | None |
| Up | Down | Go long | Trailing buy-stop |
| Down | Down | Stand aside | None |
| Down | Up | Go short | Trailing sell-stop |

**Screen Three (intraday, entry)**: no separate chart or indicator is required — this is an order-placement technique.
- Long setup (weekly up, daily down): place a buy-stop order one tick above the high of the latest daily bar. If not filled, lower the buy-stop the next day to one tick above that day's high, and continue lowering it daily until either filled or the weekly indicator reverses and cancels the buy signal.
- Short setup (weekly down, daily up): place a sell-stop order one tick below the latest daily bar's low. If not filled, raise the sell-stop the next day to one tick below that day's low, continuing daily until filled or the weekly signal reverses.
- The technique is designed to catch an intraday breakout that resumes the weekly trend direction, entering only once the market actually starts to move back in that direction rather than trying to pick the exact bottom or top of the daily pullback.

**Stop placement on entry**: place the initial stop at the extreme of the past two days' range (i.e., beyond the recent two-day high for a short, or below the recent two-day low for a long).

## Risk

The system provides no built-in position-sizing formula in this original edition; Elder's general money-management chapter (see the parent book's Risk and money management section) applies the 2% Rule — never risk more than 2% of account equity, including commissions and slippage, on the trade defined by the Screen Three entry and its two-day-range stop. As in the later Triple Screen revision, an oscillator signal running counter to the weekly trend should be read only as a signal to take profits on an existing position, never as a basis for a new counter-trend entry. Because entries always trail price (buy-stops above, sell-stops below), a trader risks missing fast, gapping moves that never trigger the trailing order; conversely, the daily re-adjustment of the trailing stop keeps the entry price close to the actual breakout point rather than chasing whatever level Screen Two first signaled.

## Caveats

The original text gives no explicit rule for filtering range-bound weekly markets before applying Screen One, and Elder does not present a systematic backtest of the approach — only worked chart examples. The specific Screen One indicator in this 1993 edition (weekly MACD-Histogram slope) was replaced by Elder himself in his 2002 sequel with a 26-week EMA slope as his stated current preference; readers should use the later book's version if they want Elder's most current parameters, and treat this page as documenting the system's original form. This file's source book was OCR'd from a sampled subset of pages; the Screen Three description above comes from the sampled pages around p.258, but the fuller Screen One/Two discussion in the surrounding, unsampled chapter text was not directly readable, so some phrasing follows the equivalent passage in Elder's own later book rather than being read verbatim here.
