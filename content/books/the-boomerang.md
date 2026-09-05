---
title: "The Boomerang: NipThePips' Trading Method"
author: "NipThePips"
year: 2008
slug: the-boomerang
tier: B
category: Forex Mechanics & Macro Drivers
tags: [forex, breakout, martingale, reverse-and-reset, compounding, gbpusd, gbpjpy]
difficulty: intermediate
doc_type: system
pages: 14
one_liner: "A GBP/USD or GBP/JPY H4 breakout system that flips direction and widens its take-profit target after each 5-pip stop-out, aiming to eventually catch the real move."
related: [forex-misc-money-management-ryan-jones, money-management-risk-control-for-traders]
source_file: "The Boomerang.pdf"
---

## Summary

A forex forum-style trading method combining a directional H4 breakout filter with a martingale-like reverse-and-reset entry sequence. The stated goal is small, compounding profits (5-10 pips per trade) with the possibility of catching larger trending moves via a scaled-out trailing-stop structure, applied specifically to GBP/USD or GBP/JPY.

## Key points

- Chart setup: H4 chart with an 18-period EMA (applied to close) as the main trend filter, plus an H1 chart purely for monitoring the trade after entry; an Excel workbook is used to calculate entry, take-profit, and stop-loss levels for each new trade in the sequence.
- Long entry filter: price must open above the 18 EMA on the H4 chart and above the previous H4 bar's median price (the 50% retracement of that bar's range, found via a Fibonacci extension tool); short entry is the mirror condition.
- Re-entry rule: a new trade may also be taken opposite to the previous stopped-out trade, regardless of the EMA/median filter, as part of the reverse-and-reset sequence.
- Reverse-and-reset mechanic: each trade uses a fixed 5-pip stop; if stopped out, the next trade reverses direction at that stop price, with the take-profit target increased by the size of the prior loss plus the original 10-pip goal (so a second attempt targets 15 pips, and so on) — intended to eventually recoup losses and profit once a real breakout hits.
- Profit-taking / trailing scale-out once a trade reaches its initial 10-pip target: exit 50% of the position at +10 pips, then trail the remainder in tranches — 20% at a 10-pip trail, 20% at a 15-pip trail, 10% at a 20-25 pip trail — to let a genuine trending move run.
- Compounding position-sizing example: increase position size by one lot for every full increment of the original starting capital gained (e.g., starting at $6,000 trading 1 lot, add a lot at $12,000, $18,000, etc.), assuming a conservative 5 net pips/day average.
- The author's own worked spreadsheet example shows this compounding approach turning $6,000 into close to $1,000,000 over roughly three trading years (220 trading days/year) under those assumptions.
- The author reports only one severe "wipe-out" (all reversal attempts failing in sequence) during testing of an earlier version of the method, describing it as very rare.

## Actionable rules

1. Initial stop loss: 5 pips on every trade in the sequence.
2. Initial take-profit: 10 pips on the first trade of a sequence.
3. On stop-out, reverse direction immediately and increase the take-profit target by the prior loss plus the original 10-pip goal (e.g., 15 pips on the second attempt).
4. Entry filter for a fresh (non-reversal) sequence: price above (below) both the 18 EMA and the previous H4 bar's median for longs (shorts).
5. Scale-out once +10 pips is reached: close 50% of the position immediately; trail 20% at 10 pips, 20% at 15 pips, and 10% at 20-25 pips.
6. Position sizing: increase size by one lot per full multiple of starting capital gained, assuming steady small daily gains.
7. Take initial capital out of the account once it has doubled (stated as a personal risk-management tip, not a formal rule).

## Caveats

The reverse-and-reset mechanic is structurally a martingale-style approach (escalating recovery target after a loss rather than escalating stake, but same recovery logic) and the author acknowledges a "very rare" but real risk of a full wipe-out where the sequence never catches the move; no worst-case drawdown or maximum sequence length is quantified. The headline compounding result ($6,000 to ~$1M in three years) rests on an idealized assumption of a steady 5 net pips/day with no losing streaks factored into the compounding table, and is presented via the author's own spreadsheet rather than an independently verified track record. The system is narrowly scoped to two GBP pairs and H4 entries with no discussion of spread, slippage, or broker execution quality, which matter disproportionately for a 5-pip stop.

## Who it is for

Forex traders interested in a mechanical breakout-with-recovery approach for GBP/USD or GBP/JPY who are comfortable with martingale-style risk (escalating profit targets after a loss) and want a concrete position-sizing and trailing-stop framework to pair with it.
