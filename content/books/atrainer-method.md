---
title: "ATrainer Method"
author: Unknown
year: unknown
slug: atrainer-method
tier: B
category: Trend Following & Mechanical Systems
tags: [moving-average-envelope, dmi, forex, breakout, discretionary-system, eur-usd]
difficulty: intermediate
doc_type: manual
pages: 3
one_liner: "A forum-posted breakout system combining a 1-period MA, a standard-deviation-based moving-average envelope, and DMI (+DI/-DI) crossovers, tuned for 20-pip EUR/USD gains."
related: [bollinger-band, macd, six-forces-of-forex, wayne-a-thorp-measuring-internal-strength-wilders-rsi-indicator]
source_file: "Atrainer Method.pdf"
---

## Summary

A trading-forum write-up describing a self-developed system that replaces a conventional slow moving average with a moving-average (MA) envelope calibrated to roughly a 0.5 standard-deviation width (matched visually against a 0.5 Bollinger Band at pivot points, then the Bollinger is discarded), paired with a 1-period MA of price as the "fast" line and DMI +DI/-DI crossovers as a confirming oscillator. The author trades it with discretion rather than as a pure mechanical system, primarily to catch ~20 pip moves in EUR/USD on a 30-minute chart.

## Key points

- The "fast MA" is simply price plotted as a 1-period moving average (no lag), which the author found filters noise better than expected despite being unsmoothed.
- The "slow" component is not a moving average but an MA envelope, sized to roughly a 0.5 standard deviation — calibrated by overlaying a 0.5-setting Bollinger Band, matching envelope width to Bollinger width at major pivots, then dropping the Bollinger.
- The envelope's key property (unlike a Bollinger Band) is that it narrows during strong breakouts (giving price room to run outside it) and holds steady width during consolidation, rather than widening on breakouts and squeezing in consolidation like a Bollinger Band.
- DMI is used only for its +DI/-DI crossover; the author explicitly does not use the ADX line.
- Highest-probability signal: an MA-envelope cross confirmed by a simultaneous +DI/-DI crossover.
- Lower-probability continuation signal: a re-entry into the envelope followed by a new breakout, with DMI still favoring the same direction; trendlines drawn on the DMI lines are used for early exits near tops/bottoms.
- A signal is treated as false if price closes back inside the envelope and DMI recrosses within two bars of the signal.
- Author's own settings: 10-period MA envelope at a 0.04 shift and a 10-bar DMI on a 30-minute EUR/USD chart; a 20-period envelope is offered as a more conservative variant.

## Actionable rules

1. Plot price as a 1-period MA (fast line) alongside an MA envelope calibrated to ~0.5 standard deviation width (found by matching against a 0.5 Bollinger Band at pivots, then removing the Bollinger).
2. Add a DMI with a 10-bar period; use only the +DI/-DI cross, ignore ADX.
3. Primary entry: MA-envelope breakout confirmed by a simultaneous +DI over -DI (or vice versa) crossover.
4. Secondary/continuation entry: re-entry into the envelope followed by a fresh breakout while DMI still favors the same direction; lower probability than the primary signal.
5. Exit/false-signal rule: if price closes back inside the envelope and DMI recrosses within 2 bars, treat the original signal as false.
6. Author's tested settings: 10-period MA envelope, 0.04 shift, 10-bar DMI, 30-minute EUR/USD chart, targeting ~20 pip gains.

## Caveats

Posted with the explicit admission that the author lacks backtesting capability and "can't optimize" the 0.5 standard-deviation parameter — it is a heuristic, not a validated setting. The author states the system is traded "with a large amount of discretion," and the entry rules for the two-bar false-signal filter and trendline-based DMI exits are described loosely rather than as precise, codeable rules. No track record, win rate, or drawdown data is given. Author identity and publication date are unknown (informal forum/PDF repost).

## Who it is for

Discretionary forex traders interested in an alternative to Bollinger Bands for envelope-based breakout trading, willing to backtest and formalize the loosely specified rules themselves.
