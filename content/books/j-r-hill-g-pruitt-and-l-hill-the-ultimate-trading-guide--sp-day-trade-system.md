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

A day-trading system for S&P 500 futures, presented as the book's most complicated rule set, combining two entry techniques that the authors say appear in nearly every top-performing commercial S&P day-trade system they have tracked at Futures Truth: an opening-range breakout to capture trending days, and a counter-trend retracement entry to capture failed breakouts. All positions are closed by the end of the day; only S&P 500 futures are used because the authors argue few other markets have enough intraday range to cover execution costs on a day-trade basis. Backtested one-contract-per-trade, 1/1/1990-2/29/2000, $100 commission/slippage assumed.

## Rules

**Volatility filter (trade permission)**: Calculate the average actual range (high - low) for the past 10 days, and the average open-to-close range for the past 10 days. Divide the open-to-close average by the actual-range average. If this ratio is less than 0.5, no trade is taken that day (most of the day's movement is happening outside the open-to-close "core," in the dead zones between open/low and high/close, which is unfavorable for open-range breakout entries).

**Key of the day**: (High + Low + Close) / 3, calculated for each session.

**Buy-easier / sell-easier day determination**: If today's close is greater than today's key price, tomorrow is a "buy easier" day. If today's close is less than today's key price, tomorrow is a "sell easier" day.

**Breakout entries** (volatility measure = 10-day average actual range):
- Buy-easier day: buy stop = open + 30% of the volatility measure; sell stop = open - 60% of the volatility measure.
- Sell-easier day: buy stop = open + 60% of the volatility measure; sell stop = open - 30% of the volatility measure.

**Counter-trend (retracement) entries**, using yesterday's actual range and yesterday's key price (independent of the buy-easier/sell-easier classification):
- Counter-trend buy: triggers only after the market first trends down to (yesterday's key price - 75% of yesterday's actual range); once that point is touched, a buy stop is placed at (yesterday's key price - 25% of yesterday's actual range).
- Counter-trend sell: triggers only after the market first trends up to (yesterday's key price + 75% of yesterday's actual range); once touched, a sell stop is placed at (yesterday's key price + 25% of yesterday's actual range).

**Trading window**: No new trades before 10:00am or after 3:30pm Eastern.

**Trade frequency limit**: Only one trade per direction per day (i.e., up to two signals in a day — one buy and one sell — but never two buys or two sells).

**Exit**: All positions are liquidated at the close of the same session. A flat $300 money-management stop is used per trade; the authors note there is no trailing stop or breakeven stop in this version, and flag that as an area for further refinement.

## Risk

The system is explicitly higher-risk than the book's other systems: S&P 500 futures can move on the order of $10,000 in a day, margin requirements are correspondingly high, and the authors state plainly that these markets "should be out of reach for the average trader." They recommend traders with roughly $20,000 in capital either trade a small basket of anti-correlated markets instead, or limit themselves to one S&P contract rather than concentrating risk. The fixed $300 stop is a blunt instrument relative to the ATR-scaled stops used elsewhere in the book, and the lack of any trailing or breakeven mechanism means a trade that moves favorably intraday and then reverses can give back the entire gain before the end-of-day exit.

## Caveats

This is described by the authors themselves as the most complicated system in the book, and it is also the narrowest in scope — a single-market, single-timeframe day-trading system rather than a portfolio-ready approach. It depends on reliable, low-latency intraday execution and accurate real-time price data; the authors' broader discussion of data-vendor inconsistencies (opening/closing price discrepancies, bid/ask handling differences) applies with extra force to a system this execution-sensitive. Backtest period (1990-2000) predates the S&P e-mini era and modern market microstructure (electronic order books, HFT-driven intraday volatility patterns), so the volatility and range assumptions embedded in the rule thresholds may not transfer cleanly to current markets without re-calibration.
