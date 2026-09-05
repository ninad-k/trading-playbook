---
title: Bollinger on Bollinger Bands
author: John Bollinger
year: 2002
slug: john-bollinger-bollinger-on-bollinger-band
tier: A
category: Indicators
tags: [bollinger-bands, volatility, percent-b, bandwidth, the-squeeze, pattern-recognition, volume-indicators, mean-reversion]
difficulty: intermediate
doc_type: book
pages: 264
one_liner: "The creator's own manual for Bollinger Bands: construction, the %b and BandWidth indicators, The Squeeze, and three complete trading methods."
related: [alan-farley-the-master-swing-trader, street-smarts-laurence-connors, elder-alexander-trading-for-a-living, candlestick-charting-explained, curtis-faith-way-of-the-turtle]
source_file: "John Bollinger - Bollinger On Bollinger Band.pdf"
---

## Overview

Written by John Bollinger, the inventor of Bollinger Bands, this is the definitive primer on the indicator from its own creator. The book covers construction and parameter selection first, then the two indicators derived directly from the bands (%b and BandWidth), then pattern recognition (M and W tops/bottoms, walking the bands, The Squeeze), and finally three distinct, fully specified trading methods that combine bands with volume indicators. It closes with a 15-point rules summary. The tone is deliberately non-dogmatic: Bollinger repeatedly stresses that defaults (20 periods, 2 standard deviations) are starting points to be tuned, not fixed law, and that band tags are not automatic buy/sell signals.

## Core thesis

Bollinger Bands provide a *relative*, volatility-adaptive definition of "high" and "low" rather than an absolute one — because the bands widen and narrow with recent volatility, a price near the upper band means something different in a calm market than in a volatile one, and the bands adjust automatically. The greatest myth about the bands, Bollinger states directly, is that price should be sold at the upper band and bought at the lower band; in fact price can and does "walk the band" for extended trends. Reliable signals come not from band tags alone but from combining band-relative position (%b) with an independent confirming variable — usually a volume indicator — so that regression-to-the-mean and trend-continuation scenarios can be told apart before acting.

## Key concepts

- **Bollinger Bands** — a simple moving average (default 20 periods) plus/minus a multiple of the moving standard deviation (default 2σ), plotted as upper/lower bands around price.
- **%b** — `(Last − Lower Band) / (Upper Band − Lower Band)`; equals 1.0 at the upper band, 0.5 at the middle band, 0.0 at the lower band; unbounded, so it can exceed 1 or go below 0.
- **BandWidth** — `(Upper Band − Lower Band) / Middle Band`; a normalized measure of how wide the bands are, comparable across securities and time.
- **The Squeeze** — the condition where BandWidth falls to its lowest level in six months, signaling that low volatility is likely to be followed by high volatility (a precondition, not a direction).
- **The Expansion** — the mirror condition: a powerful trend causes the opposite band to turn away from the trend (e.g., the lower band turns down in an uptrend); when that reversal itself reverses, the current leg of the trend is most likely over.
- **Walking the bands** — sustained trends in which price repeatedly tags or rides along one band without reverting to the average; a close outside the band is a continuation signal in this context, not automatically a reversal signal.
- **Head fake** — a short false move opposite a Squeeze's real resolution; the main hazard when trading Method I.
- **Rational Analysis** — Bollinger's term for combining fundamental screening (a buy list / sell list) with technical, band-based timing signals.
- **Normalizing indicators with %b** — plotting Bollinger Bands on an indicator (e.g., RSI, MFI) itself and reading %b of the indicator instead of fixed overbought/oversold levels like 70/30.
- **W-bottoms / M-tops** — reversal patterns where the second low (high) is inside the bands even if it makes a new absolute price low (high), because momentum — and thus the band-relative extreme — is less pronounced on the retest.

## Rules and setups

1. **Construction**: 20-period simple moving average, ±2 standard deviations (population formula) as the default; scale the multiplier with the period — 1.9σ at 10 periods, 2.0σ at 20, 2.1σ at 50 — to hold containment near 88–89% of price action.
2. **%b formula**: `(Last − Lower BB) / (Upper BB − Lower BB)`; use to compare price's position within the bands against an indicator's position within its own bands (e.g., sell if %b(price) > 0.9 and %b(indicator) < 0.3).
3. **BandWidth formula**: `(Upper BB − Lower BB) / Middle BB`; flag a Squeeze when it hits a 6-month low; flag the start of a sustainable trend when BandWidth expands sharply out of a narrow range.
4. **Method I — Volatility Breakout**: wait for a Squeeze (BandWidth at a 6-month low), then buy a close above the upper band / sell short a close below the lower band; exit via Parabolic stop or opposite-band tag (full parameters in the system sub-page).
5. **Method II — Trend Following**: buy when %b > 0.8 **and** 10-period MFI > 80; sell/short when %b < 0.2 and MFI < 20 (system sub-page).
6. **Method III — Reversals**: buy when %b < 0.05 with a positive volume oscillator (non-confirmed lower-band tag); sell/short when %b > 0.95 with a negative oscillator (system sub-page).
7. **Pattern rule for W/M**: an ideal W has its first low outside the lower band and second low inside it (even on a new absolute low); M-tops mirror this but typically take three or more pushes rather than two.

## Risk and money management

The book does not prescribe a position-sizing or percent-risk framework; risk control is handled entirely through exit technique. Two exits recur throughout: a Welles Wilder Parabolic stop (tightening progressively from just outside the entry range) for a shorter, more conservative trade, or a tag of the opposite band as a wider target that lets trades run through corrections. Bollinger favors adjusting Squeeze-length and bandwidth parameters (tighter and shorter for short-term traders) to fit personal risk tolerance, repeating that no single parameter set is "correct" for all traders or securities — testing on your own universe is required.

## Psychology and discipline

Bollinger frames the biggest error as false certainty: treating a band tag as an automatic signal rather than a piece of relative information that needs indicator confirmation. He explicitly warns against believing in "continuous advice" — the idea that any indicator or system delivers a running verdict on what to do at every moment — and argues investors should instead wait for a limited number of discrete, well-defined setups per year rather than trading continuously. He also cautions against over-optimizing systems to fit historical parameters exactly, noting that Bollinger Band construction rules have proven robust precisely because small parameter changes don't materially change results — a mark of a durable approach versus a curve-fit one.

## Chapter map

- Part I (Ch 1–5) — Introduction, raw materials (chart types), time frames, why continuous advice fails, "be your own master" (customize everything).
- Part II (Ch 6–9) — History of trading bands/envelopes (LeDoux, Keltner, Donchian, Bomar Bands), Construction, Bollinger Band Indicators (%b, BandWidth), Statistics (why containment isn't exactly 95%, regression to the mean).
- Part III (Ch 10–16) — Pattern Recognition, Five-Point Patterns (price filters, point-and-figure, Bollinger Boxes), W-Type Bottoms, M-Type Tops, Walking the Bands, The Squeeze, Method I: Volatility Breakout.
- Part IV (Ch 17–20) — Bollinger Bands and Indicators (confirmation logic), Volume Indicators (AD, Intraday Intensity, MFI, Volume-Weighted MACD), Method II: Trend Following, Method III: Reversals.
- Part V (Ch 21–22) — Normalizing Indicators (bands on RSI/MFI/stochastics), Day Trading applications.
- Part VI — 15 Basic Rules, Wrapping Up, Endnotes, Glossary, Bibliography.

## Strengths and caveats

The book is unusually rigorous for a Tier-A trading title: formulas are given explicitly, parameter choices are backed by an actual multi-market test (IBM, S&P 500, Nikkei 225, gold, DM/USD, NASDAQ Composite over 8–10 years) rather than asserted, and the author is candid about statistical limitations — stock returns are non-normal with fat tails, containment is closer to 88–89% than the "expected" 95%, and regression to the mean is weaker than commonly assumed. The three methods are given as complete, testable rule sets rather than vague heuristics. Caveats: some material (day trading chapter, point-and-figure/Bollinger Boxes discussion) reflects early-2000s market structure and technology; volume-indicator reliability depends on well-specified bars, which the book itself flags as a problem intraday; and, as with any indicator book, no forward-looking backtest across modern markets is provided — the parameter table is a starting point the reader must validate.

## Who should read it

Ideal for intermediate technical traders who already read basic charts and want a rigorous, formula-complete treatment of one specific indicator family, including exact entry/exit logic for three distinct trading styles (breakout, trend-following, mean-reversion). Less useful as a first book on technical analysis generally, since it assumes familiarity with moving averages, oscillators, and volume indicators, and it is narrowly scoped to Bollinger Bands rather than broader system design or money management.

## Related books in this library

- [[alan-farley-the-master-swing-trader]] — uses Bollinger Bands (20-2 and 5-8-13 setups) as one input to a broader multi-time-frame swing framework.
- [[street-smarts-laurence-connors]] — another source of concrete, testable short-term setups that pairs well with Bollinger's confirmation-based methods.
- [[elder-alexander-trading-for-a-living]] — a broader psychology-plus-indicators framework (Triple Screen) that complements Bollinger's narrower, deeper indicator focus.
- [[candlestick-charting-explained]] — a natural companion for reading the price bars that interact with the bands in pattern recognition.
- [[curtis-faith-way-of-the-turtle]] — a contrasting fully mechanical, volatility-based breakout system (ATR-driven rather than band-driven) useful for comparing volatility-breakout philosophies.
