---
author: Lester
category: Forex Mechanics & Macro Drivers
difficulty: intermediate
doc_type: manual
one_liner: A forum thread compiling one forex trader's WMA5/WMA20 crossover system
  for EUR/USD, GBP/USD and USD/CHF on 30-minute charts, with a pip-filter entry and
  multi-lot scale-out exits.
pages: 7
related:
- fx10
reviewed_pdf_pages: 1-7
slug: bunny-cross-system
source_file: BUNNY CROSS SYSTEM.pdf
source_review: full
tags:
- forex
- moving-average-cross
- wma
- scalping
- trailing-stop
- scaling-out
- eur-usd
tier: B
title: Bunny Cross System
year: unknown
---

## Summary

This is a transcribed forum thread (attributed to a poster "Lester"), not a formal book — one trader's rules and Q&A responses for a 30-minute-chart forex system built on a 5-period and 20-period weighted moving average (WMA) crossover, traded mainly on EUR/USD, GBP/USD and USD/CHF. Core idea: wait for WMA5 to cross WMA20, then enter only once price moves a further fixed pip "filter" beyond the crossed level (20 pips EUR/USD, 30 pips others) to avoid whipsaws from an incomplete cross. Risk is capped at the level of the original cross (the initial stop), managed with a step-ladder trailing stop and optional multi-lot scale-out.

## Key points

- **Entry filter**: enter only once price is 20 pips beyond the WMA5/WMA20 cross (EUR/USD) or 30 pips (GBP/USD, USD/CHF); this buffer is the main defense against whipsaws.
- **Initial stop**: set at the level of the moving-average cross itself, so it scales with how far price traveled before the filter triggered entry.
- **Trailing-stop ladder**: breakeven at 10 pips profit, lock 10 at 30 pips, lock 30 at 30-50 pips, lock 50 at 50-100 pips, then lock 100 and trail by 10.
- **"Dead cross" filter**: ignore a crossover where the two averages are moving in opposite directions; only trade crosses where both move the same direction.
- **WMA100 filter**: only take crosses in the direction of the WMA100 (long above it, short below); avoid crosses that lead straight into it.
- **"Mr Sheen" re-entry**: after a 30+ pip retrace off a strong move, re-enter on a 5-minute-chart breakout bounce off WMA20/WMA100 in the original trend direction, with a tight stop.
- **Scaling out**: enter 2-3 lots at once, take partial profit on the first lot at a fixed target (e.g. 50 pips), and move remaining stops to breakeven.
- **Ranging-market warning**: more than two crosses on one pair in a day signals a range and calls for caution on new signals.

## Actionable rules

1. Enter when price closes 20 pips (EUR/USD) or 30 pips (other pairs) beyond a confirmed WMA5/WMA20 cross on the 30-minute chart.
2. Only treat the cross as valid if both WMAs move in the same direction (reject "dead crosses").
3. Set the initial stop at the cross level; trail per the ladder (breakeven at 10 pips, then lock 10/30/50/100 as profit milestones hit).
4. Filter all crosses by WMA100: longs only above it, shorts only below it.
5. Skip new signals after more than two same-day crosses on a pair.
6. On a 30+ pip retracement, re-enter on a 5-minute breakout bounce off WMA20/WMA100 ("Mr Sheen") with a tight 10-20 pip stop.

## Caveats

This is an informal forum compilation, not a vetted publication — rules and pip values shift slightly across the thread as contributors refine them, and the win-rate claim (~90%) is self-reported with no verifiable backtest. No author surname, date, or independent track record is available; treat every numeric parameter as personal preference, not an optimized setting.

## Who it is for

Discretionary forex swing/day-traders comfortable with moving-average crossover systems who want a fully worked example of pip filters, multi-lot scaling, and trailing-stop management on 30-minute major-pair charts.
