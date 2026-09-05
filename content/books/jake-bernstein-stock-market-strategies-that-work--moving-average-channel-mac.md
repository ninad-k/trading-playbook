---
title: "Moving Average Channel (MAC)"
author: "Jacob Bernstein and Elliott Bernstein"
year: 2002
slug: jake-bernstein-stock-market-strategies-that-work--moving-average-channel-mac
tier: A
category: Trend Following & Mechanical Systems
tags: [moving-average-channel, trend-following, support-resistance, breakout, stop-loss]
difficulty: intermediate
doc_type: system
parent: jake-bernstein-stock-market-strategies-that-work
pages: 208
one_liner: "Bernstein's own trend/support-resistance tool: a 10-day MA of highs and 8-day MA of lows forms a channel used to define trend, time entries at support/resistance, and set stops."
related: [jake-bernstein-stock-market-strategies-that-work, turtlerules, curtis-faith-way-of-the-turtle]
source_file: "Jake Bernstein - Stock Market Strategies That Work.pdf"
---

## What it is

The Moving Average Channel (MAC) is the Bernsteins' own construction ("our own creation"): a moving average of daily highs and a separate moving average of daily lows, plotted together as a channel. Unlike a moving average of closes, it is designed to locate objective support and resistance — lows tend to act as support in an uptrend, highs as resistance in a downtrend. The same fixed lengths (10-day high MA, 8-day low MA) are used on every stock, "do not change from stock to stock." It borrows from Donchian's 1950s channel work but uses two separately-lengthed moving averages rather than one rolling high/low.

## Rules

1. **Construct the channel.** Plot a 10-day SMA of daily highs (upper band/resistance) and an 8-day SMA of daily lows (lower band/support), using these lengths regardless of instrument.
2. **Determine the trend.** Uptrend confirmed once two or more consecutive bars close completely above the channel top; downtrend once two or more close completely below the bottom; otherwise treat as sideways.
3. **Entry.** In a confirmed uptrend, buy at the MAC low as price retraces down to it. In a confirmed downtrend, sell short at the MAC high as price rallies up to it. Do not fade the breakout itself — it defines which side of the market to trade from.
4. **Continuation signal.** Five or more consecutive bars entirely outside one side of the channel warns of an unusually strong move still to come — argues for holding the position longer, not a new entry trigger.
5. **Exit/stop-loss (choose one).** Conservative: a 10 percent closing-basis stop from entry. Aggressive: exit on the mirror-image two-bar signal (two closes below the channel exits a long; two closes above exits a short).
6. **Trailing stop.** Once a position shows a reasonable profit, trail a stop below the lowest low of the last three bars (longs) or above the highest high of the last three bars (shorts).
7. **Channel surfing (range-bound variant).** In a sideways market, buy at the MAC low and take profit at the MAC high (mirror for shorts), repeating as price oscillates; caps profit per trade versus riding a trend, but suits choppy conditions.
8. **Optional scaling.** Consider multiple partial positions on entry so different exit techniques (fixed stop, two-bar exit, trailing stop) can apply to different portions of the same trade, at the cost of higher initial risk.

## Risk

Risk per trade is bounded by whichever exit rule is chosen at entry (10 percent stop, or the two-bar opposite-side exit); size the position so this stop distance equals an acceptable dollar loss. The trailing stop only activates once a position is already profitable, so it doesn't define initial risk. Channel surfing carries lower risk and reward per trade than trading the primary breakout. No percent-of-equity risk rule is specified — the dollar stop is left to individual risk tolerance and account size.

## Caveats

The book calls the MAC a "technique" and "trading method," not a fully mechanical system, warning it is "adjustable to the needs of the trader" and won't work identically for everyone — some discretion (entry price within the band, choice of exit method, when to trail) is expected rather than eliminated. No backtested win rate, average trade, or drawdown statistics are given across a systematic universe; the book's examples (Citrix, IBM, Juniper, Broadcom, Boeing, Microsoft, the Dow, and others) are illustrative single-instrument chart walkthroughs from 2001, not an aggregated performance study. As a lagging, moving-average-based method it will give back profit at trend reversals and can whipsaw in choppy markets, which is why channel surfing is offered as a separate variant for that regime.
