---
title: "2-Period ROC"
author: Laurence A. Connors and Linda Bradford Raschke
year: 1995
slug: street-smarts-laurence-connors--2-period-roc
tier: A
category: Swing Trading
tags: [rate-of-change, pivot-point, taylor-trading-technique, overnight-hold]
difficulty: intermediate
doc_type: system
parent: street-smarts-laurence-connors
pages: 145
one_liner: "Calculates a short-term pivot from a 2-period rate of change to decide, by the close each day, whether to carry a long or short position home overnight."
related: []
source_file: "Street Smarts (Laurence Connors).pdf"
---

## What it is

Described by the authors as "Pinball, Part 2," this pattern replaces Momentum Pinball's 1-period rate of change with a 2-period version and derives a daily pivot price rather than an RSI reading, to mechanically answer the question Taylor's original method left ambiguous — whether tomorrow should be a buying day or a selling day. It is meant to be used alongside Taylor's swing-trading framework (buy days find support at the previous day's low and close on the day's high; sell-short days test the previous day's high and reverse), concentrating on a single overnight decision rather than intraday entry and exit management.

## Rules

1. Subtract today's close from the close two days ago (not yesterday) to get the 2-period rate of change: close(day one) minus close(day three, i.e., two sessions back).
2. Add this value to yesterday's closing price (day two) to obtain the short-term pivot number for monitoring today's close.
3. Go home **long** by the close if price is trading above this pivot; go home **short** by the close if price is trading below it. Look to exit the position the next day.
4. If the 2-period rate of change flips from a buy to a sell signal and price closes below the pivot, reverse to short (and vice versa for a flip to a buy signal above the pivot).

## Risk

The source presents this as a discretionary decision aid rather than a standalone system with a defined stop-loss rule of its own — the authors state explicitly they "do not recommend trading this way on a mechanical basis." A worked S&P example shows a fresh signal flip capturing a profitable next-day close in 8 of 11 trades when entered and exited purely on the close-to-close pivot flip, but no formal stop-loss, position size, or risk-per-trade figure is specified in the chapter; risk management is left to Taylor's underlying buy-day/sell-day support-and-resistance levels (the previous day's low for a buy day, the previous day's high for a sell-short day) referenced narratively rather than restated as hard rules here. The authors caution the underlying 2-period rate-of-change oscillator is "noisy" and prone to whipsaw in flat, quiet markets (illustratively, when ADX is below 16) and unreliable in a strongly trending market (ADX above 30 and rising) — meaning the tool should be filtered by a trend-strength reading before being used to time overnight holds.

## Caveats

This chapter's own 8-of-11 track record is a single illustrative example, not a formal backtest, and the authors are explicit that the indicator "gives many false signals in quiet markets and encourages a trader to make too many marginal trades" — a caution aimed specifically at beginners. It is presented as a discretionary overlay on Taylor's method rather than a mechanical trading system in its own right; the authors suggest it becomes a "fine mechanical trading system" only once combined with a longer-term trend indicator, a volatility filter, and a money-management algorithm — none of which are specified in this chapter. The appendix's Moore Research Center statistical studies are cited as showing the underlying short-term momentum function carries a statistically significant edge, but that study covers the raw indicator, not this chapter's specific pivot-based execution rule.
