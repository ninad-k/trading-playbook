---
title: "The New Technical Trader: Boost Your Profit by Plugging Into the Latest Indicators"
author: "Tushar S. Chande and Stanley Kroll"
year: 1994
slug: chande-kroll-the-new-technical-trader
tier: A
category: Indicators
tags: [momentum, moving-average, volatility, stops, oscillators, mechanical-system]
difficulty: intermediate
doc_type: book
pages: 115
one_liner: "Introduces VIDYA, Qstick, the Chande Momentum Oscillator, StochRSI, Market Thrust, and a volatility-based (Chande Kroll) stop, with backtested trading rules for each."
related: [new-concepts-in-technical-trading-systems-welles-wilder, perry-kaufman-smarter-trading, john-hayden-how-to-use-the-rsi, wayne-a-thorp-measuring-internal-strength-wilders-rsi-indicator, money-management-report-van-tharp]
source_file: "Chande Kroll - The New Technical Trader.pdf"
---

## Overview

*The New Technical Trader* is an intermediate-level indicator book: it assumes the reader already knows standard technical analysis and shows that most popular price-based indicators (momentum, RSI, stochastics, CCI, DMI/ADX) are highly correlated with each other and therefore mostly redundant. Chande and Kroll then introduce a set of newer, mostly Chande-designed indicators meant to fix specific weaknesses of the older tools: an adaptive (volatility/momentum-indexed) moving average, a "quantitative candlestick" number in place of pattern reading, new RSI-derived oscillators, a market-breadth improvement on the Arms Index (TRIN), and a volatility-based trailing stop. Each indicator comes with an explicit formula, worked numeric examples, and specific entry/exit trading rules, closing with a fully backtested trading system that combines several of them.

## Core thesis

Because most price-based technical indicators are mathematically similar (the book shows correlation coefficients of 0.77–0.93 between momentum, RSI, stochastics, CMO, and ADX pairs on the same data), stacking multiple "confirming" indicators built the same way adds little real information. The authors argue traders should instead adopt a smaller number of indicators that are genuinely different in construction — adaptive-length averages, candlestick-derived numeric measures, bounded RSI-of-RSI oscillators, and volatility-derived stops — and pair objective price analysis with strict, non-discretionary risk control, since price analysis alone cannot anticipate every market move.

## Key concepts

- **VIDYA (Variable Index Dynamic Average)** — an exponential moving average whose smoothing constant is scaled by a volatility or momentum index (absolute Chande Momentum Oscillator, or the r² from linear regression) so it accelerates in trending/volatile markets and flattens in quiet ones; formula `VIDYA = (0.5 × absCMO) × Close + (1 − 0.5 × absCMO) × VIDYA(prior)`.
- **CMO (Chande Momentum Oscillator)** — net momentum as a fraction of total momentum over n days (the book's worked example uses 9 days): `CMO = (Su − Sd) / (Su + Sd)`, where Su and Sd are the summed up-day and down-day price changes; ranges from −1 to +1, and its absolute value indexes VIDYA.
- **Qstick** — an n-day moving average of (Close − Open), i.e., a numeric summary of candlestick body direction/size in place of visual pattern reading; positive when the market is closing above its open on average.
- **StochRSI** — a stochastic oscillator applied to RSI instead of price, bounded 0–1, designed to react faster at RSI extremes than raw RSI; can stay pinned near 1.0 through a strong uptrend and near 0 through a strong downtrend.
- **Market Thrust (MT) / Thrust Oscillator (TO)** — a stock-market breadth measure built from advancing/declining issues and their volumes (`AI×AV`, `DI×DV`), presented as an improvement on the Arms Index (TRIN); TO is a bounded (−1 to +1) net-volume variant of MT.
- **Volatility-based (Chande Kroll) stop** — a trailing stop built from a 10-day average of the Average True Range (ATR): the preliminary long stop is (recent high − multiplier × ATR), and the actual stop is the highest such preliminary value over a lookback window (mirrored for shorts); multiplier examples given range from 1.5x (tight) to 4x (loose) ATR.
- **Maximum Favorable/Adverse Excursion (MFE/MAE)** — post-trade analysis of how far a trade moved in the trader's favor or against them before its outcome, used to refine stop and target placement after the fact.
- **Linear regression trendiness (r²)** — the coefficient of determination from a rolling linear regression, used both as a standalone trend-strength filter and as an alternative index for VIDYA's smoothing constant.
- **Forecast oscillator** — a linear-regression-based next-day price forecast compared to the actual close, used to gauge forecast quality/trendiness.

## Rules and setups

1. **VIDYA breakout/band system**: build upper/lower bands around VIDYA (`VIDYA ± 2 × 0.1 × k`, where k is a volatility-derived constant); a close above the upper band is a buy signal for the next day, a close below the lower band is a sell signal for the next day; once long, a close back below the upper band closes the trade (and vice versa for shorts).
2. **CMO-driven VIDYA trend system** (fully specified, backtested): go long tomorrow on a buy stop when today's close and yesterday's close are both above today's VIDYA, entering one tick above today's high (mirror rule for shorts: both closes below VIDYA, sell stop one tick below today's low); no separate exit rule is used in the backtest — an opposite entry signal closes/reverses the position; tested with a flat $1,500 initial stop.
3. **Qstick trend signal**: 5-day Qstick for short-term futures, 20-day for daily intermediate-term, 30-week/5-week for weekly charts; when Qstick crosses from negative to positive, go long the next day; from positive to negative, go short (or close longs) the next day. A dual-moving-average version (short vs. long average of Qstick) generates the same style of crossover signal.
4. **StochRSI extreme/reversal signals**: buy when StochRSI rises above 0.80, sell when it falls below 0.20, treating these as trend-confirmation zones rather than simple overbought/oversold levels; reverse the open position if StochRSI then reverses back through the opposite threshold.
5. **Thrust Oscillator (TO) long-term signal**: plot a 21-day SMA of TO with a 13-day EMA of that SMA; buy when the 21-day SMA falls below −0.3 and then crosses back above its own 13-day EMA, entering on the next day's close.
6. **Thrust Oscillator (TO) short-term signal**: plot a 5-day SMA of TO with its own 5-day EMA; buy when the 5-day SMA turns up after a decline or crosses above its EMA; sell when it crosses below its EMA.
7. **Volatility-based (Chande Kroll) stop**: compute a 10-day average of ATR; subtract (multiplier × ATR₁₀) from the recent high for a preliminary long stop, then use the highest of the recent preliminary values as the actual trailing stop (mirror for shorts, using the lowest value and adding the ATR term); the stop can only ratchet in the trade's favor, never retreat. Tighter multipliers (1.5x–2x) exit sooner and whipsaw more in consolidation; looser multipliers (3.5x–4x) hold longer through pullbacks.

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

The book is unusually rigorous for the genre: every indicator is given an explicit formula, a worked numeric calculation, and a stated backtest with real trade counts, win rates, and payoff ratios rather than cherry-picked chart examples — the correlation-table opening (showing r² between popular indicators) is a genuinely useful piece of quantitative skepticism that most trading books skip. The main dated element is the software/data context (SystemWriter Plus, 1983–1993 futures data, "$3,000 black box systems" as a period reference), which doesn't affect the indicator math but marks this clearly as a mid-1990s text; commission/slippage assumptions ($125 per side) are also dated. Because the source is a scanned book with only sampled OCR pages, some supporting detail could not be verified from the text made available: the exact lookback window (highest-high period) feeding the volatility-based stop's preliminary calculation, the full buy-side mirror rule for the CMO-driven VIDYA system (only the sell-side rule was present in the sample), and the complete out-of-sample (1988–1993) backtest results beyond the first five-year block. Treat formulas and rules above as accurate to the sampled pages, and note that some numeric parameters (band multipliers, lookback lengths) are described in the book as adjustable starting points rather than fixed optimal values.

## Who should read it

Best suited to traders already comfortable with standard indicators (RSI, moving averages, stochastics) who want mathematically explicit, backtestable alternatives rather than another qualitative pattern-reading book — the formulas and worked examples make every indicator here directly codeable in a spreadsheet or trading platform. Less useful for discretionary chart readers, beginners without a base in standard technical analysis (the authors explicitly assume this), or anyone looking for psychology/discipline material, which the book does not cover.

## Related books in this library

- [[new-concepts-in-technical-trading-systems-welles-wilder]] — the origin of RSI, ADX/DMI, and ATR, all of which this book directly builds on or compares its new indicators against.
- [[perry-kaufman-smarter-trading]] — another adaptive/volatility-indexed moving-average approach, useful for comparing against VIDYA's design.
- [[john-hayden-how-to-use-the-rsi]] — background on standard RSI, the base indicator StochRSI and CMO are built to improve on.
- [[wayne-a-thorp-measuring-internal-strength-wilders-rsi-indicator]] — further RSI background relevant to the StochRSI and CMO chapters.
- [[money-management-report-van-tharp]] — a useful companion on position sizing, since this book's risk chapter focuses on stop placement rather than sizing formulas.
