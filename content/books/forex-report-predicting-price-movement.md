---
title: "The Forex Report: Predicting Price Action"
author: Scott Owens with Omer Lizotte
year: 2004
slug: forex-report-predicting-price-movement
tier: B
category: Forex Mechanics & Macro Drivers
tags: [forex, momentum, breakout, probability, price-action]
difficulty: intermediate
doc_type: article
pages: 25
one_liner: FX Engines tabulates continuation probabilities after 10-, 15-, 20-, 25-, and 50-pip moves in four major pairs.
related: []
source_file: "Forex Report - Predicting Price Movement.pdf"
source_review: full
reviewed_pdf_pages: "1-25"
---
## Summary

This FX Engines data brief estimates how often a move in EURUSD, USDJPY, GBPUSD, or USDCHF continues to larger pip targets. The study uses tick data from January 2000–May 2004, extends daily data through October 2004, and examines 5-, 30-, 60-, 120-, 240-, and 1,440-minute intervals (p. 3). At each interval close, a trigger of 10, 15, 20, 25, or 50 pips in either direction starts a simulated observation; continuation is measured over the next 24 intervals with a fixed 20-pip stop and no spread cost (p. 3). The tables show strong dependence on timeframe and target distance. For a 10-pip EURUSD move, continuation to +80 pips is 32.4% on the 60-minute interval and 68.4% on the daily interval (p. 4). For a 50-pip EURUSD move, continuation to +100 pips is 17.1% on five-minute data and 78.1% on daily data (p. 20). These are conditional historical frequencies, not a complete strategy or expected return.

## Key points

- Longer intervals generally show higher continuation percentages, while farther targets reduce them (pp. 4–23).
- The authors explicitly say the probabilities are a snapshot and may be affected by seasonality and other conditions (p. 2).
- Their suggested use is to backtest fixed exits, breakout entries, and trailing exits at the chosen interval (p. 24).

## Actionable rules

1. Match the currency pair, trigger size, sampling interval, and target exactly when reading a continuation cell; percentages are not interchangeable across tables (pp. 4–23).
2. Follow the authors’ stated research use: backtest fixed exits, breakout entries, and trailing exits at the selected interval (p. 24).
3. Add spread, slippage, an executable trigger, and out-of-sample data before treating the descriptive table as a strategy; the report itself omits these elements (pp. 2, 24–25).

## Caveats

The report gives no sample counts for each cell, does not document data-quality checks, and disclaims accuracy of its prices and probabilities (pp. 2–3, 25). The 20-pip stop and 24-interval horizon create a simulation convention rather than a trading recommendation. Historical continuation can change with regime, liquidity, and execution costs.

## Who it is for

Useful for quantitatively minded FX traders designing hypotheses for breakout and exit research.
