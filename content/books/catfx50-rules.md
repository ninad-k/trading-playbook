---
title: "CatFX50 Rules"
author: "Unknown"
year: 2007
slug: catfx50-rules
tier: B
category: Day Trading & Scalping
tags: [forex, ema, stochastic, pivot-points, scalping, eurusd, gbpusd]
difficulty: intermediate
doc_type: manual
pages: 4
one_liner: "A four-level EMA50/EMA120-plus-stochastic forex scalping system on the 30-minute chart for EURUSD, USDCHF and GBPUSD, with a 34-pip stop."
related: [5-13-62, camarilla-levels, 9-forex-systems, king-keltner-trading-strategy]
source_file: "CatFX50 rules.pdf"
---

## Summary

"CatFX50" is a short rules sheet (a recap/cheat-sheet, not a full manual) for a discretionary forex system built on a 30-minute chart. It combines an EMA50/EMA120 trend filter with a custom histogram-stepped stochastic indicator ("Hist_Step_MA_Stoch") and an auxiliary "aNina" indicator, offering four increasingly aggressive/riskier signal levels for entries plus a set of optional confirming tools (Fibonacci pivots, additional moving averages, Camarilla pivot levels).

## Key points

- Core tools: EMA50 and EMA120 on the chart, a "Hist_Step_MA_Stoch" indicator (2000-bar lookback, ±0.04 step filters), and an "aNina_v1" indicator (9000-bar lookback).
- Traded pairs: EUR/USD, USD/CHF, and GBP/USD; timeframe is the 30-minute chart; trading window is restricted to 08:00–18:00 CET.
- Level 1 (standard) signal: buy when price crosses above EMA50 and a new bar opens above it, with Hist_StepMA_Stoch confirming green (mirror for sells with red).
- Levels 2–4 are progressively riskier: Level 2 allows one bar to dip below EMA50 before resuming; Level 3 allows the stochastic to briefly flip color without a full cross; Level 4 is a breakout of a recent high/low after consolidation, needing a clear "indication of strength" or risking a trap.
- A signal more than 20 pips from EMA50 is flagged as riskier.
- Check correlated pairs (EUR/GBP, USD/CHF, US Dollar Index) before entering, to avoid conflicting exposure across pairs.
- Optional confirming tools: FiboPiv_v2 (Fibonacci pivots), a triple moving average (50/14/2000/2), SDX-TZBreakout, and Camarilla pivot levels (L3–L5, H3–H5).

## Actionable rules

1. Only trade EUR/USD, USD/CHF, or GBP/USD, and only within the 08:00–18:00 CET window.
2. Standard (Level 1) long entry: price crosses above EMA50 and the new bar opens above it, with Hist_StepMA_Stoch green; mirror for shorts (cross below, open below, indicator red).
3. Prefer signals where price and indicator crossings occur simultaneously; treat entries more than 20 pips from EMA50 as higher risk.
4. Do not trade a pair on another pair's signal — wait for each pair's own confirmed setup, and check EUR/GBP, USD/CHF, and the US Dollar Index for conflicting signals first.
5. Use a fixed stop loss of 34 pips.
6. Levels 2–4 (dip-and-resume, brief stochastic flip, and consolidation breakout) require the same indicator confirmation as Level 1 but are explicitly labeled riskier — the text advises caution ("take care") on Level 4 in particular.

## Caveats

This is a bare rules recap, not a full manual — it assumes the reader already has the custom indicators (Hist_Step_MA_Stoch, aNina) installed and understood; no chart images, backtest results, or win-rate statistics are included in this text. The system explicitly disclaims itself: "not a Holy Grail nor a money machine." Several proprietary/custom indicator names cannot be verified as standard or reproducible without the original indicator files.

## Who it is for

Intermediate forex scalpers/day traders already comfortable with custom MetaTrader-style indicators who want a simple EMA-plus-stochastic entry checklist across three major pairs.
