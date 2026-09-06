---
title: "Multi-dimensional Time Trading"
author: Cynthia Kase
year: 1996
slug: cynthia-kase-multi-dimensional-trading
tier: B
category: Indicators
tags: [multi-timeframe, stochastic, kase, divergence, volatility]
difficulty: advanced
doc_type: article
pages: 3
one_liner: "Explains rolling higher-timeframe permission filters and KaseCD as a companion to the proprietary PeakOscillator."
related: [trading-with-macd-a-lesson-on-divergence, reverse-divergence-and-momentum]
source_file: "Cynthia Kase - Multi-Dimensional Trading.pdf"
source_review: full
reviewed_pdf_pages: "1-3; all rendered pages inspected visually"
---

## Summary

The second article in a series, reprinted from Futures in May 1996, explains two ways Kase combines information across time: a higher-timeframe directional permission filter and KaseCD, an oscillator derived from her PeakOscillator. The intention is to reduce countertrend whipsaws and distinguish changes in the strength of a move. This three-page article is not the full book or a complete implementation specification.

## Key points

- **Permission filter:** use a longer timeframe to screen the direction of shorter-timeframe entries (PDF p. 1).
- **Rolling bars:** instead of waiting for a fixed 45-minute candle to finish, construct a rolling nine-bar window from five-minute candles. Its high and low are the extremes of the window, its open is the oldest bar's open, and its close is the newest close (p. 2).
- **Synthetic stochastic:** feed those rolling OHLC values into a stochastic-style filter, with smoothing to reduce update noise (p. 2).
- **Directional permission:** Kase describes long permission when PK and PD are close together near the upper extreme; when PK is above PD in a neutral region; or when PK is rising strongly from below the lower threshold. Short conditions reverse these relationships (p. 2).
- **KaseCD:** the printed formula smooths the difference between PeakOscillator and its eight-period average over three periods (p. 3).
- **Divergence evidence:** silver charts show cases where KaseCD and PeakOscillator diverge while MACD does not. These selected examples support explanation, not a measured superiority claim (pp. 2-3).

## Actionable rules

1. Treat longer-timeframe permission as a filter on a separate entry setup, rather than an entry by itself. The example applies it to a nine/18-period moving-average crossover (p. 2).
2. For the illustrated rolling window, recompute the nine five-minute bars at each update. This differs from a fixed, clock-aligned 45-minute series (p. 2).
3. If the required PeakOscillator series is available, the stated KaseCD relationship is `average(PeakOscillator - average(PeakOscillator, 8), 3)` (p. 3). The underlying PeakOscillator formula is not supplied here.

## Caveats

Several permission thresholds are examples, including neutral values of 20-80 and differences of 2%-5%; the article says choices depend on indicator length. It does not fully define smoothing, PeakOscillator, stops, sizing or exits. Its square-root-of-time risk discussion is a simplifying argument, not a guarantee that shorter trades are safer. No standalone method sub-page is justified by these incomplete inputs. All three scans were visually inspected.

## Who it is for

Experienced indicator users studying multi-timeframe filters who can distinguish an explanatory article from a reproducible trading system.
