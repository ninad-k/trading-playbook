---
title: "Using Bollinger Bands"
author: "John Bollinger"
year: 1992
slug: trading-bollinger-john-bollinger-bands-done
tier: A
category: Indicators
tags: [bollinger-bands, volatility, percent-b, bandwidth, trading-bands, mean-reversion]
difficulty: intermediate
doc_type: article
pages: 11
one_liner: "Bollinger's original 1992 Stocks & Commodities article introducing Bollinger Bands, %b, and BandWidth — the condensed source of his later full book."
related: [john-bollinger-bollinger-on-bollinger-band, candlestick-charting-explained]
source_file: "[Trading] Bollinger_ John - Bollinger Bands (Done).pdf"
---

## Overview

This is John Bollinger's original 1992 article for *Stocks & Commodities* magazine ("Using Bollinger Bands"), an 11-page piece that predates and condenses the material he later expanded into the full book *Bollinger on Bollinger Bands* (2002), already covered in this library at [[john-bollinger-bollinger-on-bollinger-band]]. It traces trading-band history from J.M. Hurst's hand-drawn cycle envelopes through Marc Chaikin's percentage-based Bomar Bands to Bollinger's own standard-deviation-based construction, then introduces the %b and BandWidth indicators and the core rule that band tags are not standalone buy/sell signals.

## Core thesis

Trading bands answer whether a price is high or low on a *relative* basis, not an absolute one — and Bollinger Bands do this better than fixed-percentage or fixed-point envelopes because band width is set by a volatility measure (standard deviation) that automatically widens and narrows with the market itself. A tag of the upper or lower band is not, by itself, a sell or buy signal; it only becomes actionable when compared against the behavior of an independent, non-colinear indicator (something derived from a different data source than closing price alone).

## Key concepts

- **Bollinger Bands** — a simple moving average (20-period default) plus/minus two standard deviations, calculated from the same closing-price data as the average.
- **Envelope history** — Hurst's hand-drawn cyclical envelopes; the 1970s fixed-percentage shift (e.g., a 21-day average shifted ±4%); Chaikin's Bomar Bands, which set width to contain a fixed 85% of the past year's data.
- **%b** — `(Last − Lower Band) / (Upper Band − Lower Band)`, using George Lane's stochastics formula applied to the bands; 100 at the upper band, 0 at the lower band, and unbounded beyond either.
- **Band width (BandWidth)** — the width of the bands expressed as a percent of the moving average; a sharp narrowing (e.g., under 2% for the S&P 500 in this article) precedes a volatility expansion.
- **Multicollinearity avoidance** — Bollinger's rule against combining indicators derived from the same underlying data (e.g., RSI + MACD + rate of change, all from closing price); he recommends pairing bands with one indicator each from price (RSI), volume+price (on-balance volume), and range+volume (money flow).
- **Parameter scaling** — as the moving average period lengthens, the standard deviation multiplier should increase (1.5σ at 10 periods, 2σ at 20 periods, 2.5σ at 50 periods).

## Rules and setups

1. **Construction**: 20-day simple moving average ± 2 standard deviations as the default for stocks; use 10-day/1.5σ for a shorter-term view and 50-day/2.5σ for a longer-term view.
2. **No standalone band-tag signal**: a tag of the upper band with a confirming (non-diverging) indicator reading is a continuation signal, not a sell signal; a tag with a diverging indicator reading is the sell signal.
3. **W-bottom / M-top price-only signal**: a low (high) outside the bands followed by a second low (high) inside the bands, regardless of the second point's price relative to the first, constitutes a buy (sell) signal from price action within the bands alone.
4. **%b + indicator divergence entry**: e.g., price makes a new low with %b around −20 while RSI reads 35, then a shallower low with %b only to 10 while RSI holds above 40 (does not make a new low) — the non-confirmed second low is a buy signal.
5. **BandWidth squeeze**: a sharp drop in BandWidth (the article cites sub-2% readings for the S&P 500) flags an imminent volatility expansion, though not its direction.

## Risk and money management

The article gives no position-sizing or stop-loss framework; it is purely a signal-construction piece. The only risk-relevant guidance is indirect: avoid over-trusting any single confirming indicator by choosing confirmations that are not mathematically colinear with each other or with the bands (Bollinger explicitly warns that the Commodity Channel Index, an early popular choice, was found to be too colinear with the bands themselves).

## Psychology and discipline

Limited coverage given the article's length; the closest guidance is Bollinger's framing that trading bands should prompt questions rather than issue verdicts — "asking the market what is happening is always a better approach than telling the market what to do" — an early statement of the same anti-false-certainty stance he develops at length in the full book.

## Chapter map

Not applicable — this is an 11-page magazine article with informal section breaks: envelope/trading-band history; Bollinger's own construction method and parameter selection; "answering the questions" (relative vs. absolute price); introducing %b and BandWidth; avoiding multicollinearity among confirming indicators.

## Strengths and caveats

**This document substantially overlaps with [[john-bollinger-bollinger-on-bollinger-band]]** already in this library: it is Bollinger's own earlier (1992) statement of the same construction formula, the same %b and BandWidth indicators, and the same core "bands are relative, not absolute" thesis that the full 2002 book expands into three complete trading methods (Volatility Breakout, Trend Following, Reversals) with worked multi-market parameter testing. Everything of substance here is a subset of that book's Parts I-II and the confirmation-indicator logic in Part IV; readers should treat this article as historical context (Bollinger's original public introduction of the indicator) rather than a separate source of trading rules. As a magazine piece, it is also necessarily brief: no worked full trading system, no backtest, and pre-Squeeze-terminology (the formal "Squeeze" and "Method I/II/III" system names introduced in the later book do not appear here).

## Who should read it

Only worth reading directly for someone specifically interested in the historical origin of Bollinger Bands or in seeing Bollinger's own earliest public formulation of %b and BandWidth. Anyone wanting Bollinger's actual trading rules should go straight to [[john-bollinger-bollinger-on-bollinger-band]], which contains everything in this article plus the fully specified trading methods.

## Related books in this library

- [[john-bollinger-bollinger-on-bollinger-band]] — the full-length, later book by the same author that supersedes this article; contains the same construction and indicators plus three complete trading methods.
- [[candlestick-charting-explained]] — a natural companion for reading the price bars that interact with the bands.
