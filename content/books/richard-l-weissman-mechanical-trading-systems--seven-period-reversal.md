---
title: "Seven-Period Reversal (Full System)"
author: "Richard L. Weissman"
year: 2005
slug: richard-l-weissman-mechanical-trading-systems--seven-period-reversal
tier: A
category: "Trend Following & Mechanical Systems"
tags: [mean-reversion, short-term, day-trading, nondirectional, overbought-oversold, intraday]
difficulty: intermediate
doc_type: system
parent: richard-l-weissman-mechanical-trading-systems
pages: 241
one_liner: "A nondirectional short-term reversal system that fades seven consecutive closes in one direction the moment the eighth bar reverses, with a symmetric 1% profit target and stop."
related: [john-bollinger-bollinger-on-bollinger-band]
source_file: "RICHARD L. WEISSMAN - Mechanical Trading Systems.pdf"
---

## What it is

A short-term, nondirectionally biased mean-reversion system built for liquid, volatile intraday vehicles (the book tests it on the Nasdaq 100 index). Unlike the book's other mean-reversion systems, which fade an oscillator reading, this one fades pure price exhaustion: it waits for a run of six consecutive higher (or lower) closes and then triggers only once the seventh bar breaks that run, on the theory that a market that has moved consistently in one direction for six bars and then stalls is more likely to see a short-term reversion than a continuation. It has no long-term trend filter, so it trades both directions with no directional bias.

## Rules

**Setup condition**
1. Identify a run of six consecutive bars each closing higher than the one before it (for a short setup) or six consecutive bars each closing lower than the one before it (for a long setup).

**Entry**
2. Sell short when, after six consecutive higher closes, the next (seventh) bar closes lower than the prior bar — i.e., the up-run breaks.
3. Buy long when, after six consecutive lower closes, the next (seventh) bar closes higher than the prior bar — i.e., the down-run breaks.
4. No moving-average, RSI, or other trend filter gates the signal — every qualifying reversal pattern is traded regardless of the larger trend context.

**Exit — profit target and stop**
5. Exit a long at entry price plus 1% of entry price (profit target).
6. Exit a long at entry price minus 1% of entry price (fail-safe stop).
7. Exit a short at entry price minus 1% of entry price (profit target).
8. Exit a short at entry price plus 1% of entry price (fail-safe stop).
9. An alternative exit condition (a symmetric seven-bar reversal in the opposite direction) can substitute for or supplement the fixed percentage exits, but the book's tested version uses the fixed 1% target/stop pair.

**Instrument selection**
10. Restrict this system to instruments with enough intraday volatility and liquidity to clear a $75–100 round-turn commission/slippage cost on a 1%-of-value target — the book found only a short list (equity indices, T-bonds, major FX) qualify; most futures and stocks do not generate enough per-trade movement at short-term bar intervals to be profitable after costs.

## Risk

Risk per trade is fixed and symmetric at 1% of entry value on both the stop and the target, so the system's win rate directly determines its expectancy (no built-in profit-to-loss skew). In the book's backtest on the Nasdaq 100 index (day session only, November 1998–January 2004), the system produced $55,696 total net profit over 166 trades, a 48.8% win rate, and a 1.27 profit-to-maximum-drawdown ratio, with an average trade lasting under one day. Compared with a trend-filtered RSI-extremes variant on the same instrument and period, removing the directional bias improved the win rate and shortened average trade duration but reduced the profit-to-maximum-drawdown ratio — the book's general finding that trend-following mean-reversion systems tend to outperform nondirectional ones, at the cost of a lower win rate and longer average holding period.

## Caveats

The system has no trend filter, so it will fade genuine breakouts as readily as exhaustion moves; the book does not report what fraction of losses came from being run over by a strong continuation versus a failed reversion. Performance depends heavily on choosing a sufficiently volatile, liquid instrument — the book shows the same style of system failing outright on instruments or time frames with inadequate per-trade price movement to clear costs, and stop/target percentages that work on one bar interval (e.g., 60-minute) needed to be resized for others. As with the book's other systems, results are backtested on a single vendor's data (CQG) over a specific historical window and may not generalize to markets with different microstructure or volatility regimes.
