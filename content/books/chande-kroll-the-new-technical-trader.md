---
author: Tushar S. Chande and Stanley Kroll
category: Indicators
diagram: divergence
diagram_caption: Divergence, the behaviour most of these indicators are built to detect.
difficulty: intermediate
doc_type: book
one_liner: Introduces VIDYA, Qstick, the Chande Momentum Oscillator, StochRSI, Market
  Thrust, and a volatility-based (Chande Kroll) stop, with backtested trading rules
  for each.
pages: 115
related:
- perry-kaufman-smarter-trading
- john-hayden-how-to-use-the-rsi
- wayne-a-thorp-measuring-internal-strength-wilders-rsi-indicator
- money-management-report-van-tharp
reviewed_pdf_pages: 6, 12, 15, 22, 25, 29, 39, 45, 49, 52, 55, 62, 65, 75, 92, 102,
  109 (indicator construction and trading-rule pages for VIDYA, Qstick, CMO/StochRSI,
  Market Thrust and the volatility stop)
slug: chande-kroll-the-new-technical-trader
source_file: Chande Kroll - The New Technical Trader.pdf
source_review: partial
tags:
- momentum
- moving-average
- volatility
- stops
- oscillators
- mechanical-system
tier: A
title: 'The New Technical Trader: Boost Your Profit by Plugging Into the Latest Indicators'
year: 1994
---

## Overview

*The New Technical Trader* is an intermediate-level indicator book: it assumes the reader already knows standard technical analysis and shows that most popular price-based indicators (momentum, RSI, stochastics, CCI, DMI/ADX) are highly correlated with each other and therefore mostly redundant. Chande and Kroll then introduce a set of newer, mostly Chande-designed indicators meant to fix specific weaknesses of the older tools: an adaptive (volatility/momentum-indexed) moving average, a "quantitative candlestick" number in place of pattern reading, new RSI-derived oscillators, a market-breadth improvement on the Arms Index (TRIN), and a volatility-based trailing stop. Each indicator comes with an explicit formula, worked numeric examples, and specific entry/exit trading rules, closing with a fully backtested trading system that combines several of them.

## Core thesis

Because most price-based technical indicators are mathematically similar (the book shows correlation coefficients of 0.77–0.93 between momentum, RSI, stochastics, CMO, and ADX pairs on the same data), stacking multiple "confirming" indicators built the same way adds little real information. The authors argue traders should instead adopt a smaller number of indicators that are genuinely different in construction — adaptive-length averages, candlestick-derived numeric measures, bounded RSI-of-RSI oscillators, and volatility-derived stops — and pair objective price analysis with strict, non-discretionary risk control, since price analysis alone cannot anticipate every market move.

## Key concepts

- **VIDYA (Variable Index Dynamic Average)** — an EMA whose smoothing constant is scaled by a volatility/momentum index (absolute CMO, or r² from linear regression), accelerating in trending markets and flattening in quiet ones: `VIDYA = (0.5 × absCMO) × Close + (1 − 0.5 × absCMO) × VIDYA(prior)`.
- **CMO (Chande Momentum Oscillator)** — net momentum as a fraction of total momentum over n days (book example: 9 days): `CMO = (Su − Sd) / (Su + Sd)`, Su/Sd being summed up-day/down-day changes; ranges −1 to +1 and indexes VIDYA via its absolute value.
- **Qstick** — an n-day moving average of (Close − Open); a numeric substitute for visual candlestick pattern reading, positive when the market closes above its open on average.
- **StochRSI** — a stochastic oscillator applied to RSI instead of price, bounded 0–1, reacting faster at RSI extremes; can stay pinned near 1.0 through a strong uptrend and near 0 through a downtrend.
- **Market Thrust (MT) / Thrust Oscillator (TO)** — a breadth measure from advancing/declining issues and their volumes, an improvement on the Arms Index (TRIN); TO is a bounded (−1 to +1) net-volume variant.
- **Volatility-based (Chande Kroll) stop** — a trailing stop from a 10-day ATR average: preliminary long stop = recent high − multiplier×ATR; actual stop = highest such value over a lookback window (mirrored for shorts); multipliers used range 1.5x (tight) to 4x (loose).
- **MFE/MAE** — Maximum Favorable/Adverse Excursion: post-trade analysis of how far a trade moved for/against the trader before its outcome, used to refine stops and targets.
- **Linear regression trendiness (r²)** — coefficient of determination from a rolling regression, used as a trend-strength filter and as an alternative VIDYA index.
- **Forecast oscillator** — a linear-regression-based next-day price forecast compared to the actual close.

## Rules and setups

1. **VIDYA breakout/band system**: bands = `VIDYA ± 2 × 0.1 × k` (k a volatility constant); close above the upper band = buy signal for next day, close below the lower band = sell signal; once long, a close back below the upper band closes the trade (mirror for shorts).
2. **CMO-driven VIDYA trend system** (fully specified, backtested): buy stop tomorrow, one tick above today's high, when today's and yesterday's closes are both above today's VIDYA (mirror short rule below VIDYA); no separate exit — an opposite signal reverses the position; tested with a flat $1,500 stop.
3. **Qstick trend signal**: 5-day for short-term futures, 20-day daily/30-week or 5-week weekly for longer-term; negative-to-positive zero cross = go long next day, positive-to-negative = go short/close next day. A short/long moving-average-of-Qstick crossover gives the same style of signal.
4. **StochRSI signal**: buy when it rises above 0.80, sell when it falls below 0.20 (treated as trend-confirmation zones, not simple overbought/oversold); reverse if it crosses back through the opposite threshold.
5. **TO long-term signal**: 21-day SMA of TO with a 13-day EMA of that SMA; buy when the SMA falls below −0.3 then crosses back above its EMA, entering on the next close.
6. **TO short-term signal**: 5-day SMA of TO with its own 5-day EMA; buy when the SMA turns up or crosses above its EMA; sell on the reverse cross.
7. **Volatility-based (Chande Kroll) stop**: preliminary long stop = recent high − multiplier×ATR₁₀; actual stop = highest preliminary value over a lookback window (mirror for shorts); the stop only ratchets in the trade's favor. Tighter multipliers (1.5x–2x) exit sooner and whipsaw more; looser (3.5x–4x) hold longer through pullbacks.

## Risk and money management

The book devotes a full chapter to risk control, built primarily around the volatility-based stop described above, used two ways: as an intermediate-term trailing stop, or (for short-term traders) as a tighter re-entry trigger after being stopped out on the looser version. The fully backtested CMO-driven VIDYA system used a flat $1,500 initial stop with no separate profit target (opposite signals close and reverse the trade), plus $125 added to losses and subtracted from gains in testing to model slippage and commissions. Reported ten-year, cross-market backtest results (System Writer Plus, roughly 1983–1993, split into two five-year blocks) targeted a 30–45% win rate and a payoff ratio (average winner ÷ average loser) above 2.50; the first five-year Swiss franc block returned a 36% win rate, a 3.37 payoff ratio over 33 trades, an average losing trade cut off in 13 days, and an average winning trade held 79 days, with average trade profit above $700. Maximum Favorable/Adverse Excursion (MFE/MAE) analysis is recommended as a follow-up step to refine stop placement per market once a system's basic edge is confirmed.

## Psychology and discipline

The book is almost entirely mechanical/quantitative and does not treat trading psychology as a subject in its own right; its implicit discipline argument is that mathematically well-defined, testable rules (explicit formulas, stated lookback periods, and out-of-sample backtest splits) remove the ambiguity and second-guessing that come from discretionary pattern reading, particularly the candlestick-pattern reading Qstick is explicitly designed to replace with a single number.

## Chapter map

- Ch 1 — An Abundance of Indicators — shows the high correlation between popular price indicators (momentum, RSI, stochastics, CMO, ADX) and previews the book's new indicators.
- Ch 2 — Linear Regression Analysis — trend quantification, r²-based trendiness, and a next-day forecast oscillator.
- Ch 3 — The Variable Index Dynamic Average — VIDYA construction (CMO-indexed and r²-indexed variants), bands, and breakout rules.
- Ch 4 — Qstick: The Quantitative Candlestick — Qstick construction, zero-cross and dual-average trading strategies, a 1987-crash case study.
- Ch 5 — New Momentum Oscillators — the Chande Momentum Oscillator and the Stochastic RSI Oscillator, with construction and trading rules.
- Ch 6 — Market Thrust and Thrust Oscillator — a breadth/volume improvement on the Arms Index (TRIN), with short- and long-term trading rules.
- Ch 7 — Controlling Risk: The Key to Profitability — the volatility-based (Chande Kroll) trailing stop, trade templates, and MFE/MAE analysis.
- Ch 8 — How to Use This Book — a fully specified, backtested CMO-driven VIDYA trading system combining several of the book's indicators.

## Strengths and caveats

The book is unusually rigorous for the genre: every indicator gets an explicit formula, a worked numeric calculation, and a stated backtest with real trade counts, win rates, and payoff ratios rather than cherry-picked chart examples — the opening correlation table (r² between popular indicators) is a genuinely useful piece of quantitative skepticism most trading books skip. The main dated element is the software/data context (System Writer Plus, 1983–1993 futures data), which doesn't affect the indicator math but marks this as a mid-1990s text; commission/slippage assumptions ($125 per side) are also dated. Because the source is a scanned book with only sampled OCR pages, some detail could not be verified: the exact lookback window feeding the volatility-stop's preliminary calculation, the full buy-side mirror rule for the CMO-driven VIDYA system (only the sell side was present in the sample), and the complete out-of-sample (1988–1993) backtest results beyond the first five-year block. Treat rules above as accurate to the sampled pages; some numeric parameters (band multipliers, lookback lengths) are described as adjustable starting points, not fixed optimal values.

## Who should read it

Best suited to traders already comfortable with standard indicators (RSI, moving averages, stochastics) who want mathematically explicit, backtestable alternatives to qualitative pattern reading — the formulas and worked examples make every indicator directly codeable. Less useful for discretionary chart readers, beginners without a technical-analysis base (the authors assume this), or anyone looking for psychology/discipline material, which the book does not cover.

## Related books in this library

- **New Concepts in Technical Trading Systems** (no library summary: corrupt) — the origin of RSI, ADX/DMI, and ATR, all of which this book directly builds on or compares its new indicators against.
- [[perry-kaufman-smarter-trading]] — another adaptive/volatility-indexed moving-average approach, useful for comparing against VIDYA's design.
- [[john-hayden-how-to-use-the-rsi]] — background on standard RSI, the base indicator StochRSI and CMO are built to improve on.
- [[wayne-a-thorp-measuring-internal-strength-wilders-rsi-indicator]] — further RSI background relevant to the StochRSI and CMO chapters.
- [[money-management-report-van-tharp]] — a useful companion on position sizing, since this book's risk chapter focuses on stop placement rather than sizing formulas.
