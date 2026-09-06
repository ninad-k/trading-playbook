# Financial Time Series Toolbox for MATLAB: User's Guide: the trader's summary

*MATLAB toolbox reference for building and analyzing financial time series objects, with worked examples computing MACD, Williams %R, RSI, and On-Balance Volume.*

**The MathWorks, Inc.** · 2004 · Indicators · intermediate

*Source coverage: partial. PDF pages inspected: 2-3, 11-14 (the function reference and the worked indicator examples). These are study notes, not verified trading results.*

## Summary

The official MathWorks user's guide (Version 2, 2004) for the Financial Time Series Toolbox, an add-on for MATLAB. It documents the `fints` financial time series object (dates, frequency, and one or more data series), the functions for building, indexing, transforming, and visualizing it, a chapter of worked technical-analysis examples, a point-and-click GUI, and a full alphabetical function reference. It is a software manual, not a trading strategy source, but its Technical Analysis chapter is directly relevant to traders who want to compute standard indicators programmatically.

## Key points

- A financial time series object (`fints`) is built from a `fints(dates, data)` constructor or from a text file via `ascii2fts`; it always carries `desc`, `freq`, and `dates` fields plus one or more named data series (defaulting to `series1`, `series2`, ...).
- Frequency must be set explicitly (e.g., `fts.freq = 'daily'`) before most operations will run correctly.
- Built-in technical analysis functions are grouped into oscillators (accumulation/distribution oscillator, Chaikin oscillator, `macd`, stochastic oscillator, acceleration, momentum), stochastics (Chaikin volatility, fast/slow stochastics, `willpctr` for Williams %R), indexes (negative/positive volume index, `rsindex` for RSI), and indicators (accumulation/distribution line, `bollinger` bands, highest high, lowest low, median/typical/weighted price, `onbalvol`, price/volume rate of change).
- `rsindex` (RSI) defaults to a 14-period lookback, matching the standard textbook convention; the period is configurable via a second argument.
- `macd` requires a series named `Close` (case-insensitive) by default and returns both the MACD line and a 9-period signal line.
- `willpctr` (Williams %R) is conventionally read against the -20/-80 overbought/oversold levels; `rsindex` against the 30/70 levels.
- `onbalvol` (On-Balance Volume) requires both `Close` and `Volume` series present in the object.
- `fillts` interpolates missing values in a time series (e.g., filling gaps from holidays) using several interpolation methods.
- The toolbox includes frequency-conversion functions (e.g., `todaily`) to align series of different native frequencies (e.g., weekly economic data against daily price data) before analysis such as regression.
- A worked demo program shows constructing a dividend-adjusted "spot price" series, a return series, and regressing returns against an explanatory index — a template for simple factor-style analysis.
- A GUI (`ftsgui`) provides menu-driven access to the same load, fill, frequency-conversion, technical-analysis, and charting functions without writing code, including a candlestick plot and an interactive zoomable chart tool (`chartfts`).

## Actionable rules

None given — this is a software reference manual, not a trading system. The closest actionable content: the toolbox's default indicator parameters (14-period RSI, 9-period MACD signal line, -20/-80 Williams %R bands, 30/70 RSI bands) match conventional technical-analysis defaults and can be used as starting points for programmatic indicator calculation.

## Caveats

This is MATLAB software documentation from 2004 (Financial Time Series Toolbox, since superseded/renamed within MATLAB's Financial Toolbox family), not a trading book — most of its content (object construction syntax, GUI menus, file I/O) is programming reference with no trading-relevance beyond the indicator formulas and default parameters used. Requires a MATLAB license and the toolbox itself to be useful; the discussion here paraphrases the documented indicator conventions only.

## Who it is for

Traders or analysts with MATLAB access who want to compute standard technical indicators (MACD, RSI, Williams %R, OBV, Bollinger Bands) programmatically against historical price data rather than relying on charting-software defaults.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: matlab, technical-indicators, macd, rsi, williams-pctr, on-balance-volume, data-tools, quant
