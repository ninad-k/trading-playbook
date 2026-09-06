---
author: Unknown
category: Day Trading & Scalping
difficulty: intermediate
doc_type: manual
one_liner: Free MetaTrader 4 multi-timeframe forex system ('Broom-Hilda') combining
  Woodies CCI, a custom OsMA and moving averages to trade trends, reversals, and scalps
  across paired timeframes.
pages: 6
related:
- forex-trading-machine-ebook
- icwr-forex-trading-strategy
- forex-money-management
reviewed_pdf_pages: 1-6
slug: hilda-system
source_file: Hilda System.pdf
source_review: full
tags:
- forex
- multi-timeframe
- cci
- moving-averages
- trend-following
- scalping
- mt4
- metatrader
tier: B
title: The Broom-Hilda System
year: 2005
---

## Summary

An informal, forum-style write-up (dated around July 2005) distributing a free MetaTrader 4 indicator package nicknamed "Broom-Hilda": three custom indicators (a J_TPO-based "Broom-Hilda" oscillator, SuperWoodies CCI, and a colored OsMA) plus a chart template. The method is a discretionary, multi-timeframe trend-following system that always pairs two chart timeframes (e.g., 5-min with 15-min), reads trend direction off CCI color and moving-average alignment, and times entries off an oscillator/OsMA crossover, with a separate "reversal" setup and a one-chart scalping variant.

## Key points

- Chart setup: 200 SMA (white), 100 WMA (red), 34 WMA (yellow), SuperWoodies CCI (settings 50/0), ColorOsMA (8,12,9), and the Broom-Hilda oscillator (default settings, equivalent to a J_TPO with a lookback of 10).
- Trader always runs exactly two chart timeframes at once, chosen by trading style: 1&5min (scalps), 5&15min (usual intraday, the author's default), 5&30min (extended intraday), 15&60min (1–2 day trades), 30&240min or 60&240min (swing trades), 240min&daily (position trades), daily&weekly (long-term).
- Trend identification: CCI must show a clear, sustained color (roughly six or more bars of one color) on a timeframe to call a trend; if the three moving averages are tangled together ("cabling"), that timeframe is a no-trade zone and the trader shifts to a higher or lower timeframe instead.
- "Broom-Hilda flying her kite" = oscillator above 0.85 (overbought zone); "Broom-Hilda fishing" = oscillator below -0.85 (oversold zone) — these are the setup zones, not the trigger.
- Entry trigger (short example): with CCI red and the oscillator above 0.85, enter when the OsMA closes a bar lower than the prior bar (or, on a faster nested timeframe, when OsMA turns red at the bar close); the mirror-image setup applies to longs.
- Preference is given to trading on the "right side" of the moving averages — e.g., a long should be above the 34 WMA and ideally above the 200 SMA with 30–50 pips of room.
- A separate reversal setup: when the oscillator is at an extreme (kite flying or fishing) at the same moment the OsMA changes color, that flags a potential reversal; only used on 15-minute charts and above, since higher timeframes give larger (and riskier) moves.
- Scalping variant uses a single one-minute chart: go long when the 34 WMA is above the 100 WMA (and vice versa for shorts), without waiting for full kite/fishing extremes.

## Actionable rules

1. Stop-loss sizing by timeframe: roughly 10 pips + spread on 5- and 15-minute charts, 6 pips + spread on 1-minute charts, about 20 pips on 30-minute/1-hour charts; 15-minute trades commonly use a 15–20 pip stop.
2. Exit rule: exit on the strongest timeframe that generated the entry signal (15-min ranks stronger than 5-min, which ranks stronger than 1-min, etc.), using the same OsMA-reversal trigger that generated entry (a higher/lower-than-prior-bar close against your position).
3. Alternative exit: trail the stop behind peaks on the shorter timeframe while the longer timeframe trend persists; if not stopped, still exit on the OsMA-reversal trigger described above.
4. Take partial profit around +15 pips when only the shorter timeframe (not the longer one) confirms the trade, since full alignment across timeframes is what produces 100+ pip trades.
5. Never take a trade "out of sync" — if a higher timeframe is setting up in the opposite direction to a lower-timeframe signal, skip the lower-timeframe trade.

## Caveats

Written informally by an unidentified forum author distributing pirated/rebranded indicators (the text openly says "Broom-Hilda" is a rebrand of the Jurik J_TPO indicator); no author name, publisher, or verification of results is given, and no backtest or track record beyond a handful of anecdotal example trades (with specific July 2005 entry prices) is provided. Language is casual and promotional ("thank you for leeching this"), and reliability of the ~80% figure cited for the reversal setup is unverified/anecdotal. Treat as a discretionary multi-timeframe framework to study, not a proven edge.

## Who it is for

Discretionary forex day/swing traders using MetaTrader who want a concrete, rule-based multi-timeframe trend-following template (paired timeframes, CCI + moving-average trend filter, oscillator-based entries/exits) to study or adapt, understanding it comes from an unverified free-system source.
