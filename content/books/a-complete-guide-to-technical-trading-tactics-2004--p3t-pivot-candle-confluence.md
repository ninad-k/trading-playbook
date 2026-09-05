---
title: "P3T: Pivot Point + Candlestick Confluence Trading"
author: "John L. Person"
year: 2004
slug: a-complete-guide-to-technical-trading-tactics-2004--p3t-pivot-candle-confluence
tier: A
category: "Candlesticks & Chart Patterns"
tags: [pivot-points, candlesticks, confluence, commitments-of-traders, futures]
difficulty: intermediate
doc_type: system
parent: a-complete-guide-to-technical-trading-tactics-2004
pages: 287
one_liner: "Person's P3T method: trade calculated daily/weekly/monthly pivot support-resistance targets only when confirmed by a candlestick reversal, an oscillator, or lopsided COT positioning."
related: [a-complete-guide-to-technical-trading-tactics-2004, pivots, camarilla-levels, candlestick-charting-explained]
source_file: "A_Complete_Guide_to_Technical_Trading_Tactics_2004_.pdf"
---

## What it is

P3T ("Person's Pivot Point Trade") is a confluence trading method that combines mathematically calculated support/resistance target levels (classic floor-trader pivot points) with a confirming candlestick reversal pattern, and optionally a confirming oscillator signal or lopsided Commitments of Traders (COT) positioning, before entering a trade. It is not a pure mean-reversion or breakout system on its own — pivot levels are treated as the price zones worth watching, and the candle/oscillator/COT confirmation decides whether to fade the level or to expect it to break.

## Rules

**1. Calculate the pivot levels.** For each time frame you trade (daily, weekly, and monthly, calculated in parallel), take the prior period's high (H), low (L), and close (C):

```
P  = (H + L + C) / 3
R1 = (P × 2) − L
R2 = (P + H) − L
S1 = (P × 2) − H
S2 = (P − H) + L
```

Recalculate daily numbers at the end of each session for the next session, weekly numbers at the end of each week, and monthly numbers at the end of each month. When targets from two different time frames land near the same price, treat that zone as higher-confidence.

**2. Watch for price to reach a target.** The primary levels to act on are R1 and S1 (first resistance/support); R2/S2 are secondary targets used mainly when a market is trending hard enough to blow through R1/S1. As a general rule, only take a trade off the *first* test of a given pivot level in that time frame's cycle — by the second or third test, the edge has typically eroded.

**3. Require a confirming candlestick signal at the level.** Acceptable confirming patterns (see the parent book's candlestick chapter): shooting star, hanging man, bearish engulfing, dark cloud cover, bearish harami / bearish harami cross for a sell at resistance; hammer, bullish engulfing, piercing pattern, bullish harami / bullish harami cross for a buy at support. A doji at the level, especially after an extended run, is itself a caution flag even without a full two-candle reversal pattern.

**4. Add oscillator confirmation where available.** A stochastics or MACD divergence against price at the pivot level (price makes a marginal new high/low while the oscillator fails to) raises confidence further. This is the third leg of Person's "verify, verify, verify" rule — the method wants at least two independent, non-correlated confirmations (pivot target + candle, or pivot target + candle + oscillator) before entry, never a pivot tag in isolation.

**5. Optional sentiment filter — COT.** Before entering, check the CFTC's Commitments of Traders report for the market: a reading is treated as an added warning (favoring a counter-trend P3T entry) when the market is at a price extreme AND large speculators are heavily net long (or short) while commercials are net positioned the other way, particularly when small speculators also hold a historically stretched net position. This is a weekly-resolution filter (data as of Tuesday, released Friday), not an entry trigger by itself.

**6. Entry and stop.** Enter on the confirming candle's close, or on a stop order through the confirming candle's extreme in the trade's direction. Place the initial stop just beyond the pivot level being defended (e.g., a few ticks beyond S1 for a long, beyond R1 for a short) or beyond the confirming candlestick pattern's extreme, whichever is tighter and still technically defensible.

**7. Target and management.** First target is the next pivot level in the sequence (e.g., a short entered at R1 targets the pivot point P, then S1); a stronger trending confirmation (COT lopsidedness, or a break through the first target with continued momentum) can justify holding for R2/S2 (or S2/R2). Trail stops behind newly formed support/resistance as the trade develops rather than using a fixed profit target throughout.

## Risk

The method's stop is technical (tied to the pivot level or the candlestick pattern extreme) rather than a fixed percentage of account equity — position size must be set independently so that the technical stop distance corresponds to an acceptable dollar/percentage risk. Only acting on the first test of a pivot level is itself a risk control: repeated tests of the same level tend to precede an eventual break-through, and trading later tests against the level increases the chance of being run over by the level finally failing. Multi-timeframe confluence (daily + weekly + monthly targets clustering) should be weighted more heavily than a single-timeframe target alone, since Person's own worked examples show noticeably tighter misses (a few points/cents) when multiple time frames agree versus when only one does.

## Caveats

No formal win rate, expectancy, or backtest is given anywhere in the source material — the method is demonstrated through a series of real but individually selected historical chart examples (sugar, cattle, silver, U.S. Dollar Index, crude oil, cotton, S&P futures), each showing the projected pivot target landing close to, but rarely exactly on, the actual high or low. Treat the reported hit rate as illustrative, not statistically validated. The COT layer is weekly-resolution data with a built-in reporting lag (as of the prior Tuesday, released the following Friday), so it functions as a slow-moving positioning backdrop rather than a timing signal, and its behavior can shift materially between the data snapshot and the report's release. The method as described assumes actively traded futures/index markets with meaningful floor/professional participation around round pivot numbers; its reliability on thinly traded instruments or in gapping, news-driven conditions is not addressed by the source text.
