---
author: Jan L. Arps
category: Swing Trading
difficulty: intermediate
doc_type: manual
one_liner: TradeStation/SuperCharts toolkit manual defining a full set of swing-trading
  indicators — Zig-Zag, Fox Wave, Fib channels, Andrews Pitchfork, Price Magnets,
  and three Radar oscillators.
pages: 37
related:
- e-a-s-y-method
- king-keltner-trading-strategy
reviewed_pdf_pages: 2, 13-14, 23 (the indicator construction, ratio settings and the
  support/resistance rules)
slug: jan-l-arps-surfing-the-market-waves-the-swing-trader-s
source_file: Jan L Arps - Surfing The Market Waves - The Swing Trader's.pdf
source_review: partial
tags:
- swing-trading
- elliott-wave
- fibonacci
- andrews-pitchfork
- zig-zag
- support-resistance
- oscillators
tier: B
title: 'Surfing the Market Waves: Jan Arps'' Swing Trader''s Toolkit'
year: 1998
---

## Summary

A user manual for Jan Arps' "Swing Trader's Toolkit," a suite of custom TradeStation/SuperCharts indicators built around the idea that markets move in a fear/greed-driven, five-swing pattern (matching Elliott Wave) governed by both crowd psychology and channel geometry. The manual opens with a conceptual explanation of why markets zigzag rather than trend in straight lines, then documents each tool in the kit: swing-pivot detectors, the Zig-Zag line, pattern-recognition tools (Three-Wave Swing, Arps "Fox" Wave), channel tools (Fibonacci channels, Andrews' Pitchfork, Linear Regression Channel, auto trendlines with DeMark breakout validation), support/resistance tools (daily/weekly/monthly H-L-mid lines, floor-trader pivots, Williams' and DeMark's daily range projections), retracement/extension tools (AutoFib), Price Magnets, and three proprietary oscillators (Radar 1 Sentiment, Radar 2 Acceleration, Radar 3 Overbought/Oversold) plus divergence detectors and an adaptive trailing stop (Pro Stop).

## Key points

- Markets move in a 5-swing fear/greed cycle (initial thrust, pullback, main thrust, secondary reaction, blowoff) matching the classic Elliott Wave pattern; pullbacks in strong trends retrace 35–40%, in weak trends 50–60%, and a pullback beyond 65% signals the trend is likely over.
- Swings can be defined two ways: "Swing Bar Strength" (a pivot high/low must exceed N bars on each side) or "Zig-Zag" reversal amount (a minimum tick or percentage move in the opposite direction), the latter guaranteeing alternating highs and lows.
- Arps "Fox" Wave: a 5-point pattern (P1–P5) where an entry line is drawn through P1–P3 and a target line through P1–P4; a valid setup requires the P1→P2 leg to be longer in time than P3→P4, with price reaching a target near where the P2–P4 timing line intersects the entry line.
- Fibonacci channels plot bands around an 89-bar moving average at 8/13/21/39/55% spacing; price crossing outside the outer band tends to return to the opposite outer boundary.
- Floor Traders' Pivot formulas: Avg = (H+L+C)/3; R2 = Avg+H−L; R1 = 2·Avg−L; S1 = 2·Avg−H; S2 = Avg+L−H (using the prior day's H/L/C).
- Williams' daily range projection: Projected High = (H+L+C)×2/3 − H; Projected Low = (H+L+C)×2/3 − L.
- Standard retracement/extension levels used throughout: 0.236, 0.382, 0.500, 0.618, 0.786, 1.00, 1.272, 1.618, 2.000, 2.618, 4.236 (derived from the Fibonacci sequence).
- Price Magnets project support/resistance zones from prior swing geometry; the manual claims price reaches these zones over 75% of the time, with support/resistance flipping roles if the zone is broken through.
- The Radar 2 oscillator is noted to be highly sensitive and prone to false signals on small swings — the manual recommends filtering its signals with Radar 1 or trading only on Radar 2/price divergences.
- DeMark's trendline-breakout validity test requires at least one of three specific close/open/range conditions relative to the two prior bars before a breakout is treated as genuine rather than a false break.

## Actionable rules

1. Use the Zig-Zag tool first on any chart to calibrate the PCTCHG or TICKCHG sensitivity before applying any other swing-based tool (Fox Wave, AutoFib, Andrews Pitchfork, Linear Regression Channel).
2. Treat a pullback exceeding roughly 65% of the prior thrust swing as a warning that the larger trend may be over, not just a deeper correction.
3. For the Arps Fox Wave setup, require P4 > P3 > P1 (or the mirrored down-wave) and the P1–P2 leg longer in bars than P3–P4 before treating the pattern as valid; enter on a P5 pullback through the P1–P3 entry line with a target at the P1–P4 line extension.
4. Use the adaptive Pro Stop (volatility-based trailing stop, sensitivity input 1.5–5, smaller = tighter) to trail winning swing positions rather than a fixed-dollar stop.
5. Confirm any Auto Trendline breakout against DeMark's three qualifying conditions before acting on it, to filter out false breakouts.
6. Treat divergence between price and any of the Radar oscillators (especially a "Type 2" divergence, which is rarer but more reliable) as a higher-confidence reversal signal than a single-oscillator turn.

## Caveats

This is a proprietary indicator-suite manual (TradeStation/SuperCharts EasyLanguage tools from 1998), not an independent study — none of the tools' win rates or profit factors are backtested or quantified in the text; claims like "75% of the time" for Price Magnets are asserted without supporting statistics. Some tools (e.g., multi-data hourly pivot charts) rely on software workflow specific to now-dated TradeStation/SuperCharts versions.

## Who it is for

Discretionary swing traders already using TradeStation-family charting software who want a structured toolkit of pivot, channel, retracement, and oscillator indicators built around Elliott Wave and Fibonacci concepts, with concrete formulas they could re-implement in another platform.
