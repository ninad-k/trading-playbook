---
title: The Fader
author: Kathy Lien
year: 2006
slug: day-trading-the-currency-market--the-fader
tier: A
category: Day Trading & Scalping
tags: [forex, day-trading, fade, false-breakout, adx, range-bound]
difficulty: intermediate
doc_type: system
parent: day-trading-the-currency-market
pages: 259
one_liner: "A contra-trend hourly-chart strategy for weak-trend (ADX under 35) markets: fade a break of the previous day's high or low once price snaps back through the opposite side of that day's range."
related: [day-trading-the-currency-market, day-trading-the-currency-market--waiting-for-the-real-deal]
source_file: "Day Trading the Currency Market.pdf"
---

## What it is

The Fader is described as a variation of "Waiting for the Real Deal," generalized beyond GBP/USD to any pair, and built around the observation that breakouts at significant levels are frequently tested and rejected (false breakouts) rather than sustained, especially in weakening-trend conditions. It uses the daily chart to confirm the market is range-bound or losing trend momentum (ADX filter) and the hourly chart to time the entry once a false break has been confirmed by a reversal back through the prior day's range.

## Rules

**Long setup**:
1. Locate a currency pair whose 14-period ADX is below 35, ideally trending downward (confirming a weakening trend).
2. Wait for the market to break below the previous day's low by at least 15 pips.
3. Place an entry order to buy 15 pips above the previous day's high (i.e., wait for a reversal back through and beyond the opposite side of the range).
4. Once filled, place the initial stop no more than 30 pips away from entry.
5. Take profit when price moves 60 pips in your favor (double the 30-pip risk).

**Short setup** (mirror image):
1. Locate a currency pair whose 14-period ADX is below 35, ideally trending downward.
2. Wait for a move above the previous day's high by at least 15 pips.
3. Place an entry order to sell 15 pips below the previous day's low.
4. Once filled, place the initial protective stop no more than 30 pips above the entry.
5. Take profit when the position runs 60 pips in your favor.

**Optimization**: works best absent major scheduled economic data (e.g., avoid trading around the U.S. non-farm payrolls release), since a breakout coinciding with a real catalyst is more likely to be genuine and should not be faded; most effective on less volatile, narrower-range pairs.

## Risk

Fixed 30-pip initial risk against a fixed 60-pip target gives a built-in 2:1 reward-to-risk ratio on every trade taken under this rule set. Because the strategy explicitly fades price after it has already broken a key level (the previous day's high or low) in one direction, a genuine trend continuation after the fade entry is the primary risk scenario — the ADX<35 filter is the main defense against entering this trade in a strongly trending market.

## Caveats

Worked examples (EUR/USD, GBP/USD hourly charts) show successful fades but are again a small, hand-selected illustrative sample rather than a backtested win rate. The strategy explicitly should not be used around major data releases, which narrows the opportunity set and requires the trader to track an economic calendar. Because entries require price to first break one side of the range by 15 pips and then break the other side by another 15 pips, the strategy depends on a fairly wide intraday range being available intraday — it may not trigger at all in very quiet markets.
