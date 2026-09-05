---
title: "S&P Day Trade System"
author: "John R. Hill, George Pruitt, Lundy Hill"
year: 2000
slug: j-r-hill-g-pruitt-and-l-hill-the-ultimate-trading-guide--sp-day-trade-system
tier: A
category: Day Trading & Scalping
tags: [day-trading, s-p-500, breakout, counter-trend, mechanical-systems, futures]
difficulty: advanced
doc_type: system
parent: j-r-hill-g-pruitt-and-l-hill-the-ultimate-trading-guide
pages: 302
one_liner: "A same-day S&P 500 futures system combining an opening-range breakout with a counter-trend fade off a 'key of the day' pivot, flat by the close."
related: [larry-williams-how-to-trade-better, curtis-faith-way-of-the-turtle]
source_file: "J R Hill G Pruitt And L Hill - The Ultimate Trading Guide.pdf"
---

## What it is

A day-trading system for S&P 500 futures, presented as the book's most complicated rule set, combining two entry techniques the authors say appear in nearly every top-performing commercial S&P day-trade system Futures Truth has tracked: an opening-range breakout to capture trending days, and a counter-trend retracement entry to capture failed breakouts. All positions close by end of day; only S&P 500 futures are used since few other markets have enough intraday range to cover execution costs day-trading. Backtested one-contract-per-trade, 1/1/1990-2/29/2000, $100 commission/slippage assumed.

## Rules

**Volatility filter (trade permission)**: divide the 10-day average open-to-close range by the 10-day average actual range (high - low). If under 0.5, no trade that day — most movement is happening in the "dead zones" outside the open-to-close core, unfavorable for breakout entries.

**Key of the day**: (High + Low + Close) / 3, per session.

**Buy-easier / sell-easier determination**: if today's close is greater than today's key price, tomorrow is "buy easier"; if less, "sell easier."

**Breakout entries** (volatility measure = 10-day average actual range):
- Buy-easier day: buy stop = open + 30% of the measure; sell stop = open - 60%.
- Sell-easier day: buy stop = open + 60% of the measure; sell stop = open - 30%.

**Counter-trend entries** (using yesterday's actual range and key price, independent of buy/sell-easier classification):
- Buy: triggers once the market first trends down to (yesterday's key - 75% of yesterday's range); a buy stop is then placed at (yesterday's key - 25% of yesterday's range).
- Sell: triggers once the market first trends up to (yesterday's key + 75% of yesterday's range); a sell stop is then placed at (yesterday's key + 25% of yesterday's range).

**Trading window**: no new trades before 10:00am or after 3:30pm Eastern.

**Frequency limit**: one trade per direction per day (up to two signals total — one buy, one sell — never two of the same side).

**Exit**: all positions liquidated at the close; a flat $300 stop per trade. The authors note there is no trailing or breakeven stop in this version, flagged as an area for further refinement.

## Risk

Explicitly higher-risk than the book's other systems: S&P 500 futures can move on the order of $10,000 in a day, margins are correspondingly high, and the authors state these markets "should be out of reach for the average trader." They recommend $20,000-capital traders either trade a small anti-correlated basket instead, or limit themselves to one S&P contract rather than concentrate risk. The fixed $300 stop is blunt relative to the ATR-scaled stops elsewhere in the book, and the lack of a trailing or breakeven mechanism means a trade that moves favorably intraday and reverses can give back the entire gain before the end-of-day exit.

## Caveats

Described by the authors as the most complicated system in the book, and also the narrowest in scope — single-market, single-timeframe, not portfolio-ready. It depends on reliable, low-latency intraday execution and accurate real-time data; the book's broader warnings about data-vendor inconsistencies apply with extra force here. The backtest period (1990-2000) predates the S&P e-mini era and modern market microstructure, so the volatility and range assumptions embedded in the thresholds may need re-calibration for current markets.
