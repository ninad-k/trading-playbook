---
title: "Fischer's Fibonacci Price/Time Goal System"
author: Robert Fischer
year: 1993
slug: fischer-robert-fibonacci-applications-and-strategies-for--fibonacci-price-time-goal-system
tier: A
category: Fibonacci, Gann & Elliott Wave
tags: [fibonacci, time-goal-days, corrections, extensions, stop-loss, price-time-analysis]
difficulty: advanced
doc_type: system
parent: fischer-robert-fibonacci-applications-and-strategies-for
pages: 93
one_liner: "Fischer's mechanical substitute for Elliott wave-counting: confirmed swing filters, Fibonacci correction/extension price targets, and Time Goal Days combined into one entry/stop system."
related: []
source_file: "Fischer, Robert - Fibonacci Applications and Strategies for .pdf"
---

## What it is

The book's central tradable method (Chapters 4, 5, 7, and 8): rather than counting Elliott waves to forecast turns, a trade is triggered only when a confirmed price swing reaches a Fibonacci correction or extension level at (or near) an independently calculated Time Goal Day. Price and time are treated as two separate filters that must agree before an entry is taken, with a fixed stop-loss construction ("price square") applied to every trade. The related, more subjective logarithmic-spiral tool (Chapter 9) extends the same price/time idea graphically but is not reduced to a mechanical rule in the book and is not included here.

## Rules

**1. Confirm the swing.** Identify a filter swing using the minimum size for the instrument and timeframe (e.g., 100 basis points daily / 400 weekly for the Swiss franc, Deutsche mark, or Japanese yen; 200 daily / 800 weekly for the British pound). A swing high or low is confirmed only once a counter-move of at least the same filter size occurs in the opposite direction.

**2. Compute the price target.**
- Correction trades: target a retracement of 38%, 50%, or 62% of the confirmed swing; 50-62% retracements are treated as signaling a possible larger trend change, with a profit target of 50% of the total correction amplitude (points A to B).
- Extension trades: multiply the amplitude of an earlier wave by 1.618 (wave 3 target, using wave 1's amplitude) or by 0.618/1.618 (wave 5 target, using wave 1 or wave 3's amplitude) to set the target band.

**3. Compute the Time Goal Day (TGD).** TGD = 1.618 × the number of days (or weeks) between the two most recent confirmed swing highs, or between the two most recent confirmed swing lows. A valid swing high or low should occur at least every 15 days; if the market trends too strongly for that frequency, substitute a smaller filter swing to keep generating TGDs.

**4. Require confluence.** Only take the trade when a Fibonacci price level and a TGD occur together (or within a few bars of each other). If only one condition is met, wait.

**5. Trigger the entry.** Enter short when the close is below the low of the highest day of the move (or when a previous low/support is broken, whichever comes first); enter long on the mirror-image condition. Do not enter merely because a trend-channel line or price target was touched intraday — require a confirming close.

**6. Place the stop (price square).** Measure the horizontal distance of 5 business days (daily chart) or 5 weeks (weekly chart); apply the same distance vertically from the entry to set the stop level. The stop triggers only on a close beyond the square, not an intraday touch.

**7. Re-enter on a fresh trigger.** If stopped out, re-enter only when the same swing/price/time conditions are satisfied again — do not chase or guess a re-entry level.

**8. Very short-term variant (1-2 day hold).** Use a ~400-basis-point swing filter, a minimum 30% correction, breakout-of-previous-high entry, a 0.618 profit target, and a 2-day trailing-low stop instead of the price square.

## Risk

Risk is defined in absolute basis points/full points calibrated per instrument (via the price square), not as a percentage of account equity — the book gives no position-sizing or percent-of-capital rule. The short-term variant substitutes a 2-day trailing stop for the price square. For trades following a large price swing (roughly 10 full points in the Deutsche mark, Swiss franc, or Japanese yen), the book recommends substituting an at-the-money or in-the-money call/put with about three months to expiration for the futures position, converting open-ended stop-out risk into bounded option premium risk.

## Caveats

These rules are reconstructed from OCR-sampled pages of the book (front matter plus evenly spaced pages); the complete worked example combining price and time in Chapter 8, and some of the extension-rule detail in Chapter 5, fall partly outside the sampled pages, so figures given here should be treated as representative rather than exhaustive. No backtested win rate, sample size, or drawdown statistics are provided for the combined system — support is narrated chart examples (Swiss franc, Deutsche mark, Japanese yen, British pound) from the late 1980s/early 1990s. The system requires the trader to first identify filter swings and confirmed highs/lows by eye (or with charting software matching the book's TradeStation-era conventions); this retains a degree of judgment despite the otherwise mechanical price/time/stop rules.
