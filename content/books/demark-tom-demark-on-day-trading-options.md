---
title: DeMark on Day-Trading Options
author: Thomas R. DeMark, Thomas R. DeMark Jr.
year: 1999
slug: demark-tom-demark-on-day-trading-options
tier: A
category: Options, Futures & Derivatives
tags: [options, day-trading, td-sequential, td-combo, market-timing, put-call-ratio, indicators]
difficulty: advanced
doc_type: book
pages: 364
one_liner: "Applies DeMark's TD Sequential/TD Combo timing indicators, plus option-specific tools (TD % F, Dollar-Weighted Options), to buying short-dated, in-the-money calls and puts instead of trading the underlying."
related: [come-into-my-trading-room-elder-alexander--triple-screen, elder-alexander-trading-for-a-living]
source_file: "DeMark,Tom - DeMark on day-trading options.pdf"
---

## Overview

DeMark on Day-Trading Options adapts Thomas DeMark's proprietary market-timing indicators (TD Sequential, TD Combo, TD Lines, TD REI, and others from his earlier work) to the specific mechanics of trading options rather than the underlying stock, futures, or index. The book opens with option basics (pricing, exercising vs. trading, spreads, straddles), moves through mechanics of order placement and option selection, then presents a series of DeMark's own indicators — some built for the underlying asset (TD Sequential, TD Combo, TD Lines, TD REI/TD POQ) and two built directly from option price/volume/open-interest data (TD % F and TD Dollar-Weighted Options). The authors describe these as indicators rather than a mechanical system: rules for identifying when a market is ready to be bought or sold, applied to buying calls or puts, with the trader retaining discretion over exact entries and exits.

## Core thesis

Short-term reversal points in the underlying market can be timed with enough precision to justify buying options — rather than trading the underlying directly — because options cap risk to the premium paid while preserving asymmetric upside, and because DeMark's indicators are explicitly designed to identify exhaustion points (trend reversals) rather than to chase already-established trends. The book's second core claim is that options themselves carry independent, tradable information: option price behavior (TD % F) and the dollar-weighted balance of put versus call activity (TD Dollar-Weighted Options) can each be read as contrarian sentiment indicators, since option traders as a group are described as being wrong about market direction more often than right.

## Key concepts

- **TD Sequential** — a two-phase counting system (Setup, then Countdown) applied to a price series to identify likely trend exhaustion and reversal points, on any timeframe from daily to one-minute bars.
- **Setup phase** — a run of at least 9 consecutive closes each greater than (sell Setup) or less than (buy Setup) the close 4 price bars earlier; a "price flip" (a bar breaking the run) cancels and restarts the count.
- **Countdown phase** — follows a completed Setup; used to identify a further exhaustion point before the market is considered ripe for reversal (the book illustrates a completed Countdown as a "buy-low, sell-high" signal, following an Intersection step after Setup).
- **TD Combo** — a variant counting method (its own Setup and Countdown) presented alongside TD Sequential as an alternative, sometimes more conservative, exhaustion count.
- **TD Setup Trend (TDST)** — support/resistance-like levels derived from the high/low of a completed Setup phase, used to frame subsequent price action.
- **TD Lines / TD Line Gap / TD Line Gap REBO** — trendlines drawn from significant TD points (rather than arbitrary swing highs/lows), with qualifiers required before a breakout is considered valid ("disqualified" breakouts are explicitly filtered out); TD Line Gap REBO adds a retracement-based confirmation level (a percentage, e.g. 38.2%, of the prior day's range added to/subtracted from the current day's open).
- **TD % F** — an indicator built solely from the option's own price series (not the underlying), used to time entries/exits in the option itself.
- **TD Dollar-Weighted Options** — a sentiment indicator using the dollar-weighted value (price × volume, and as a percent of open interest) of puts versus calls, read contrarily since option traders as a group are described as usually wrong about direction.
- **TD REI / TD POQ** — a range-expansion oscillator (TD REI) and a price oscillator qualifier (TD POQ) used to time entries with additional confirmation/disqualification rules, described as "perfecting" raw oscillator signals.
- **Near-term, in-the-money option preference** — the authors' stated preference, for short-term/day trades, is to buy near-term, in-the-money options because they carry little time-value premium and track the underlying's price movement most closely.

## Rules and setups

1. **Buy Setup (TD Sequential)**: a buy Setup begins with a "price flip" — a close less than the close 4 bars earlier, immediately following a bar where the close was greater than (or equal to) the close 4 bars earlier. Count consecutive bars whose close is less than the close 4 bars earlier; a completed buy Setup requires at least 9 such consecutive bars (numbered 1 through 9). Any bar whose close is greater than or equal to the close 4 bars earlier cancels the Setup and restarts the count.
2. **Sell Setup (TD Sequential)**: mirror image — count consecutive bars whose close is greater than the close 4 bars earlier; completed at 9 consecutive bars; canceled by any bar whose close is less than or equal to the close 4 bars earlier.
3. **Setup qualifier for entry**: for a completed buy Setup, the low of the 7th, 8th, or 9th bar of the count must satisfy an additional qualifying condition (per the sampled text) before the signal is used to justify purchase of the underlying asset or the purchase of a call option; the mirror qualifier applies to sell Setups for put purchases.
4. **Countdown and Intersection**: after a completed Setup, the market proceeds through an Intersection step and then a Countdown phase, which the book uses to pinpoint a more precise "buy-low, sell-high" exhaustion point before entry; the specific bar-by-bar Countdown comparison rules were not present in the sampled OCR pages (see Caveats).
5. **TD Line Gap breakout entries**: a low-risk call-buying opportunity occurs when price breaks above a downward-sloping TD Line Gap line, with the qualifier that the current bar's open must itself be in the direction of the breakout (greater than the prior bar's close); mirror for a low-risk put-buying opportunity on a downside break of an upward-sloping TD Line Gap line.
6. **TD Line Gap REBO confirmation**: multiply the prior day's price range by a percentage (the text illustrates 38.2%) and add/subtract it from the current day's open to get a confirming breakout level; a valid low-risk entry occurs at the higher of the TD Line Gap level and the REBO level for calls (mirror, lower of the two, for puts); traders may also split entries between the two levels.
7. **Option selection**: for short-term/day trades, prefer near-term, in-the-money options (small time-value premium, price tracks the underlying closely) over further out-of-the-money or longer-dated contracts; the book explicitly favors outright option buying (calls/puts) over spreads, covered writes, straddles, or other combination strategies for this style of trading.
8. **Letting the option expire**: worthless (out-of-the-money) expiration is presented as an inherent, built-in stop-loss unique to option buying — the trader can simply do nothing and lose only the premium paid, unlike a position in the underlying, which must eventually be offset.

## Risk and money management

DeMark's stated day-trading stop-loss approach for options is explicitly non-formulaic: for inexpensive options or small positions, the authors report using no fixed stop-loss at all (letting the option's own decay and the trade's small size define the risk); for costly options or larger positions, they use a dollar-amount stop instead of a percentage or technical stop. Beyond this, the primary risk control is structural — buying options rather than the underlying inherently caps the loss on any single trade to the premium paid, and unexercised, out-of-the-money expiration functions as a built-in stop-loss that requires no active exit decision. Additional low-risk exit points are drawn from the technical indicators themselves (a reversal in TD Sequential/TD Combo, or a TD Line/TD REBO breakout in the opposite direction) rather than from a percentage-of-equity risk rule; no explicit position-sizing formula (e.g., a percent-of-account rule) is given in the sampled pages.

## Psychology and discipline

The book frames option traders as a group with a demonstrated contrarian edge available to those who track them: option buyers/sellers as a population are described as wrong about market direction more often than right, which is why a dollar-weighted put/call sentiment reading (TD Dollar-Weighted Options) is used contrarily rather than as a trend-following signal. The authors caution that day trading is exceptionally difficult psychologically and is not suited to every trader, and warn against a specific behavioral trap unique to option day-trading: letting an option's time-value premium erode while stubbornly holding a short-timeframe (one- to five-minute) indicator-driven position that has failed to respond as expected, rather than exiting on the indicator's own terms.

## Chapter map

- Ch 1 — Background: context for combining DeMark's timing work with option trading and day trading.
- Part I (Ch 2–3) — Option Basics and Option Mechanics and Trading: what an option is, pricing, exercising vs. trading vs. letting expire, spreads/straddles/combinations, order placement, and option selection.
- Ch 4 — Tools and Techniques: buying weakness/selling strength, option purchasing rules, rules for buying calls and puts, introduction to the indicators used throughout.
- Ch 5 — Option Indicators TD % F and TD Dollar-Weighted Options: indicators built from the option's own price/volume/open-interest data rather than the underlying.
- Ch 6 — Anticipating the Trend: TD Sequential, TD Combo, and TD Setup Trend: the core Setup/Countdown counting methods, entry rules, stop-loss levels, and profit-taking.
- Ch 7 — Disqualified Breakouts: TD Lines and TD Retracements: qualified/disqualified TD Line breakouts, TD Line Gap and REBO, and several retracement techniques.
- Ch 8 — Perfecting an Oscillator: TD REI and TD POQ: range-expansion oscillator and its qualifier, including disqualified readings.
- Ch 9 — Moving Forward in Reverse: TD Fib Range, TD Exit One, TD REBO Reverse, TD Camouflage, TD Range Projection: supplementary exit/entry refinements.
- Ch 10 — Pulling It All Together: a trading game plan, game-plan summary, other option trading tips, and a conclusion.

## Strengths and caveats

The book gives fully codeable rules for TD Sequential's Setup phase (the exact bar-comparison logic and cancellation conditions), which is unusually precise for a discretionary-leaning indicator book. However, this document was scanned and OCR'd from only a sample of pages, and large stretches — including the detailed Countdown bar-by-bar rules, the explicit TD % F calculation, the Dollar-Weighted Options formula, and the "Option Purchasing Rules"/"Rules for Buying Calls and Puts" sections (pp. 76–80 in the original) — fell in unsampled ranges and could not be verified; the notes above state only what was directly recoverable, and treat the rest as gaps rather than invented detail. As with much of DeMark's published work, indicators are illustrated through chart examples rather than a systematic, quantified backtest, and the book explicitly disclaims being a full "system" with a fixed track record — it presents indicators that leave room for trader discretion. Some option-mechanics content (order-placement conventions, bid/ask spread assumptions) reflects late-1990s market structure that predates decimalization and electronic options markets.

## Who should read it

Active/day traders already comfortable with basic option mechanics who want to apply DeMark's proprietary exhaustion-timing framework (TD Sequential/TD Combo) to option entries and exits, and who are interested in option-specific sentiment tools (TD % F, Dollar-Weighted Options) as a contrarian read on other option traders; not a beginner's introduction to either options or day trading.

## Related books in this library

- [[come-into-my-trading-room-elder-alexander--triple-screen]] — another multi-tool, multi-timeframe timing framework, for readers who want to compare a discretionary counting/exhaustion method (TD Sequential) against a trend/oscillator combination method (Triple Screen).
- [[elder-alexander-trading-for-a-living]] — a broader psychology-and-money-management complement, for structuring the risk discipline this book leaves largely to trader discretion.
