---
author: Michael D. Archer, James L. Bickford
category: Market Structure & Price Action
difficulty: intermediate
doc_type: book
one_liner: A catalog of forex-specific charting techniques (activity, P&F, swing charts,
  Goodman Swing Count) rather than a trading system, heavy on statistics and light
  on money management.
pages: 382
related:
- john-bollinger-bollinger-on-bollinger-band
- michael-covel-trend-following
- miner-robert-high-probability-trading-strategies-entry-to-exit-tactics-for-the-forex-futur
- s-and-c--wyckoff-method
reviewed_pdf_pages: 5, 7-8, 10, 143-144 (contents, the 50 percent principle and Goodman
  swing count chapters, and the Fibonacci retracement rules)
slug: the-forex-chartist-companion
source_file: The_Forex_Chartist_Companion.pdf
source_review: partial
tags:
- point-and-figure
- swing-charts
- chart-patterns
- forex
- fibonacci
- elliott-wave
- price-objectives
tier: A
title: The Forex Chartist Companion
year: 2007
---

## Overview

This is a reference catalog of charting techniques applied specifically to spot currency data, not a single trading system. It compiles and updates three earlier Archer/Bickford works (a forex-charting study, a point-and-figure companion, and a swing-trading companion) into one volume, and adds a fifth section presenting the Goodman Swing Count System (GSCS), a proprietary wave/matrix method taught to co-author Michael Archer by grain trader Charles B. Goodman. The book is built almost entirely around statistical tables generated from a multi-million-tick EUR/USD database and Visual Basic source code (in the appendixes) that readers can use to reproduce the charts themselves.

The five parts are: forex-specific charting (activity, direction, arbitrage, a synthetic "Mundo" composite currency index, and trend-oscillator statistics); point-and-figure (P&F) charting adapted for pip-denominated data; swing charting and Fibonacci-based measured-move forecasting; Western and Japanese reversal charts (Renko, Kagi, three-line break); and the Goodman Swing Count System. There is no chapter on position sizing, drawdown, or trade psychology in any depth — the closest the book comes to money management is a single anecdotal real-time trailing-stop example in the P&F section.

## Core thesis

Standard technical analysis tools were largely designed for equity and futures markets with fixed sessions, ticks, and volume; forex is a 24-hour, decentralized, no-volume market, so charting methods should be re-derived or re-validated against actual currency tick data rather than assumed to transfer unchanged. The authors' method throughout is empirical: define a chart type or pattern, then run it against millions of ticks (mostly EUR/USD, calendar year 2002 or 2000–2005) to produce frequency and continuation-percentage tables, rather than asserting a pattern's reliability from theory alone.

## Key concepts

- **Box size and reversal amount** — the two parameters that drive every reversal chart in the book (P&F and swing charts): box size is the minimum price increment counted (often 1–5 pips), reversal amount is the number of boxes price must retrace before a new column/wave is plotted (commonly 3).
- **Activity** — the authors' forex substitute for volume: a count of price changes (ticks) per interval, since spot forex has no centralized volume data.
- **Mundo** — a synthetic "world currency" index built as a weighted composite of major pairs, used as a beta-like benchmark against which individual pairs can be compared.
- **Point-and-figure (P&F) chart** — price plotted as columns of Xs (advances) and Os (declines), filtering out time and lateral movement; support/resistance appear as repeated highs/lows in adjacent columns.
- **Swing chart** — a companion to P&F that preserves the time axis, plotting waves (diagonal lines) between peaks and valleys using the same box-size/reversal-amount logic.
- **Measured move / 50 percent principle** — the classical premise that a third swing (in the direction of an initial swing) tends to equal the first swing's magnitude, with the retracement between them often near 50 percent; tested statistically rather than assumed.
- **Triangular arbitrage** — a check on three related currency pairs (e.g., EUR/USD, GBP/USD, EUR/GBP) for pricing anomalies versus their theoretical equilibrium ratio; the book argues these are real but too short-lived (seconds to under a minute) for manual trading.
- **Goodman Swing Count System (GSCS)** — Charles Goodman's proprietary extension of the 50 percent rule into nested "matrices" (three-part price swings) with concepts of compensation (a retracement that misses 50 percent must be made up later), carryover, cancellation, and intersection (multiple matrices converging on one price = higher-probability support/resistance).
- **Renko, Kagi, three-line break** — Japanese reversal-chart alternatives to P&F, each filtering noise differently (fixed brick size, line-thickness reversals, and N-line breakout rules respectively).
- **Fibonacci retracement/extension** — used in the swing-charting section (38.2%, 50%, 61.8%) to forecast the size of subsequent waves and, in later chapters, filtered by regression and quartile analysis for third- and fourth-wave forecasts.

## Rules and setups

The book's most concrete, mechanical rules are in the P&F section (Part II):

1. **Parameters**: choose a box size (1 pip is standard for major pairs; larger for wide-spread crosses or longer-term analysis) and a reversal amount (3 boxes is the book's default).
2. **Trend-line signal**: draw a line along the extreme highs of a downtrend or extreme lows of an uptrend; when a downtrend line is crossed by a new column of Xs, it is a buy signal (entry at the first X above the prior X-column high); when an uptrend line is crossed by a new column of Os, it is a sell signal (entry at the first O below the prior O-column low).
3. **Double top/bottom**: two X columns with matching highs (double top) or two O columns with matching lows (double bottom) mark local resistance/support; a buy signal fires if price exceeds the resistance, a sell signal if price breaks the support.
4. **Triple top/bottom**: the same pattern extended to three columns; the book's own tests found "reversal" percentages after these patterns close to the 50/50 baseline, so it recommends confirming with trend lines and other signals rather than trading the pattern alone.
5. **Price objective (vertical count)**: count the number of boxes in the signal column, multiply by the reversal amount (3), multiply by the box's pip value, and add (buy) or subtract (sell) the result from the breakout price to get a target.
6. **Trailing stop**: no fixed percentage or pip distance is prescribed; the book's real-time example sets the initial stop at the highest X (for a short) or lowest O (for a long) of the prior two columns, then ratchets it forward as new columns form, manually exiting when the trend stalls.
7. **Confirmation**: the authors repeatedly recommend not acting on any single P&F signal (trend line, double/triple top or bottom) alone, and suggest paper trading first.

The Goodman Swing Count System's core rule ("The Rule") is that a 50 percent retracement of a swing is a point of decision, not a certainty: if the retracement over- or undershoots 50 percent, the shortfall/excess ("compensation") carries over and must be resolved in a later swing within the same price matrix; where two or three matrices' measured-move points converge ("intersection"), that price is a higher-confidence support/resistance level. No fixed stop, target, or position-sizing rule is given for GSCS — the authors describe it as closer to a discretionary wave-counting discipline (like Elliott Wave, which the book explicitly positions itself against) than a mechanical system.

## Risk and money management

The book gives essentially no risk or money-management guidance. There is no discussion of percent-of-equity risk, stop-loss distance as a fixed pip or percentage rule, leverage limits, or position sizing anywhere in the main text; "money management" appears once in the index, referring to a single paragraph noting that GSCS also touches on "psychological and money management elements of trading" without elaborating. The only concrete risk mechanic shown is the ad hoc trailing-stop example in the real-time P&F charting chapter (Chapter 20), which the authors themselves describe as pattern-specific rather than a universal rule.

## Psychology and discipline

Psychology is addressed briefly and indirectly. The real-time P&F charting chapter urges traders to keep every completed chart (wins and losses alike), review them after a delay of about two weeks, and look for common factors distinguishing winning setups from losing ones — an early, informal version of trade journaling. The same chapter warns against becoming absorbed in the mechanics of charting at the expense of watching the market itself, advising traders to stop charting and manage the position directly if price moves violently. Beyond this, the book does not address trading psychology, discipline, or behavioral biases in any depth.

## Chapter map

- Part I (Ch 1–10) — Forex-specific charting: tick/spread charts, activity charts, direction charts, forex-vs-futures pip differentials, triangular arbitrage, the Mundo composite index, range charts, absolute and two-dimensional momentum, and moving-trend (linear regression) oscillators.
- Part II (Ch 11–20) — Point-and-figure charting: history, the P&F algorithm (box size, reversal amount), trend lines, double and triple tops/bottoms with statistical signal tables, triangle patterns, pattern-frequency tables by box size, breakout analysis, vertical/horizontal count price objectives, and a real-time P&F trading walkthrough.
- Part III (Ch 21–31) — Forex swing charting: a Fibonacci primer, the swing-reversal algorithm, the measured move and 50 percent principle tested statistically, third- and fourth-Elliott-wave forecasting via regression, cycle-frequency tables, bull/bear cycle studies, and swing volatility/velocity properties.
- Part IV (Ch 32–33) — Other reversal charts: Western (geometric, trend-outline, pivot) and Japanese (Renko, Kagi, three-line break) charting methods.
- Part V (Ch 34–38) — Goodman Swing Count System: its history and origin with Charles B. Goodman, ordinal principles (the 50 percent rule, recursive/self-similar price matrices), cardinal principles (price surge, multilevel matrices, compensation, carryover, cancellation, intersection), Goodman versus Elliott wave theory, and a worked chart-notation case study.
- Appendixes — world currency codes, exchange rates, global banking hours, extensive monthly/daily/time-of-day/day-of-week reference charts, comparative statistics, and Visual Basic 6.0 source code for the P&F and swing algorithms.

## Strengths and caveats

The book's strength is methodological rigor within its narrow scope: nearly every charting claim is backed by a frequency or continuation-percentage table computed from a large tick database, and the authors are candid when results are unimpressive (e.g., noting that double/triple top and bottom reversal percentages are close to a 50/50 coin flip). The Visual Basic source code in the appendixes lets a reader actually reproduce the P&F and swing algorithms rather than take the charts on faith.

The central caveat is that this is a charting reference, not a trading system book — there are no position-sizing rules, no stop-loss percentages, no backtested equity curves, and essentially no discussion of trading psychology. The statistical tables are drawn overwhelmingly from a single instrument and time window (EUR/USD, 2002, or 2000–2005 for some studies), so their generalizability to other pairs or eras is untested within the book itself. The Goodman Swing Count System, despite being labeled a "system," is presented as a discretionary, wave-counting framework similar in spirit to Elliott Wave (which the authors explicitly critique) rather than a mechanical ruleset; the authors concede it is only "probably" programmable and that a full automation would go against the originator's intent. Some content (tick-chart rendering, streaming-data mechanics) is tied to mid-2000s retail forex platform behavior and 2002–2005 market data.

## Who should read it

Useful for forex traders who want a deeper, more quantitative treatment of point-and-figure and swing charting adapted specifically to pip-based currency data, or who want to understand the Goodman Swing Count System's wave/matrix vocabulary. Not useful as a standalone source for a complete trading plan — readers need a separate source for entries' risk control, position sizing, and psychology; pair this book with a money-management or systems-focused text.

## Related books in this library

- [[john-bollinger-bollinger-on-bollinger-band]] — another chart-pattern-driven approach with its own statistical validation, useful contrast in rigor and scope.
- **New Concepts in Technical Trading Systems** (no library summary: corrupt) — classical technical indicators (RSI, ATR) referenced in passing here as an alternative to the book's own trend oscillators.
- [[michael-covel-trend-following]] — supplies the systematic money-management and psychology content this book omits.
- [[miner-robert-high-probability-trading-strategies-entry-to-exit-tactics-for-the-forex-futur]] — a Fibonacci/Elliott-oriented forex and futures method that overlaps with this book's swing-chart Fibonacci chapters.
- [[s-and-c--wyckoff-method]] — another pattern/price-structure school (accumulation, distribution, support/resistance) that complements the P&F chapter's support/resistance framing.
