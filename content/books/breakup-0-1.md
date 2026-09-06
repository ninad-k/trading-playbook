---
author: Unknown
category: Trend Following & Mechanical Systems
difficulty: beginner
doc_type: manual
one_liner: 'One-page indicator-stack setup: three EMAs, a 20 SMA, stochastic and Parabolic
  SAR combined to filter and time trend trades.'
pages: 1
related:
- dynamic-breakout-ii-strategy
- channeltrading
reviewed_pdf_pages: '1'
slug: breakup-0-1
source_file: Breakup 0.1.pdf
source_review: full
tags:
- ema
- moving-averages
- stochastic
- parabolic-sar
- trend-filter
- indicator-stack
tier: B
title: Breakup
year: unknown
---

## Summary

A single-page trading setup describing how to stack four indicator types on one chart (30-minute or higher timeframe) to define trend direction, filter entries, and time trade triggers. It is a checklist rather than a book: four ordered steps with no discussion of history, statistics, or backtest results.

## Key points

- **Triple EMA stack** — 50-period (green), 100-period (red), and 200-period (light blue) EMA; trade only when they are stacked in order with visible space between them, forming an "open fan."
- **20-period SMA** — plotted in dark blue; price should trade from below it (for longs) or above it (for shorts), giving room for the move; it should be moving the same direction as the EMAs and generally stacked near the 50 EMA.
- **Stochastic filter (14,3,3)** — only trade up when stochastic is above 20 and rising; only trade down when stochastic is below 80 and falling.
- **Parabolic SAR trigger** — enter in the direction of the EMA stack and stochastic signal on the first SAR dot appearing on the desired side of price.
- **Daily stochastic cross-check** — for extra caution, confirm the same 14,3,3 stochastic reading on the daily chart aligns with the intended trade direction.
- **Timeframe** — intended for charts of 30 minutes or higher; higher timeframes preferred.

## Actionable rules

1. Trade only when the 50/100/200 EMAs are stacked in trend order with visible separation ("open fan" shape).
2. Long trigger: EMAs stacked bullishly, 14,3,3 stochastic above 20 and rising, price above the 20 SMA, first Parabolic SAR dot appears below price.
3. Short trigger: EMAs stacked bearishly, 14,3,3 stochastic below 80 and falling, price below the 20 SMA, first Parabolic SAR dot appears above price.
4. Optional filter: check the daily 14,3,3 stochastic is aligned with the trade direction before entering.
5. No explicit stop-loss or position-sizing rule is given beyond a general statement to use "good money management."

## Caveats

This is a one-page checklist with no supporting statistics, no exit rule, no defined stop-loss distance, and no position-sizing formula ("good money management" is asserted, not defined). Source and author are unknown; treat as a starting template to be backtested and completed, not a stand-alone system.

## Who it is for

Traders who already understand EMAs, stochastics, and Parabolic SAR and want a compact, ready-to-plot indicator-confluence checklist for trend trades on intraday-to-swing timeframes.
