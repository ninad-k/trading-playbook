---
author: Joe Ross
category: Options, Futures & Derivatives
difficulty: intermediate
doc_type: book
one_liner: Joe Ross's course on constructing and filtering futures spreads and seasonal
  trades, using fundamentals, a defined time window, chart patterns, and Bollinger
  Band/RSI confirmation.
pages: 161
related:
- joe-ross-trading-the-ross-hook
- tte
- richard-l-weissman-mechanical-trading-systems
reviewed_pdf_pages: 2, 5-9, 14, 19, 30, 90, 140 (contents, spread construction and
  ratio worked examples, the technical-filter chapter and the cattle seasonal spread
  results)
slug: joe-ross-trading-spreads-and-seasonals
source_file: Joe Ross - Trading Spreads And Seasonals.pdf
source_review: partial
tags:
- spreads
- seasonality
- futures
- intermarket-spread
- intramarket-spread
- filtering
- bollinger-bands
- rsi
- joe-ross
tier: A
title: Trading Spreads and Seasonals
year: unknown
---

## Overview

A two-part course: the first half (roughly chapters 1–15) covers futures spreads — what they are, why and where to use them, how to construct and chart them, and how to filter and time entries/exits with fundamentals, chart patterns, Bollinger Bands, and RSI; the second half (chapters 16 onward) applies the same filtering framework to outright seasonal futures trades. Ross's own Ross Hook pattern from [[joe-ross-trading-the-ross-hook]] is used throughout as the chart-pattern entry/exit signal for both spreads and outright seasonal positions. The book is built around worked examples in named markets (grains, cattle, metals, currencies, financials) with real contract months and dollar figures, plus decision-table backtests for specific seasonal spreads.

## Core thesis

Seasonal tendencies in futures — driven by recurring annual supply/demand rhythms (harvest timing, weather cycles, gestation periods, tax-driven capital flows) — persist over decades and are underused by modern traders, who Ross argues have shifted to indicator- and system-driven trading and largely abandoned fundamentals-based seasonal analysis. Spreads (the price difference between two related contracts) express this seasonality with less absolute volatility and lower margin than outright futures, because a spread is effectively a hedged position most of the time. Neither seasonality nor any single technical band or oscillator is sufficient alone: Ross's method layers (1) a fundamental/seasonal rationale, (2) a defined calendar time window in which the trade has historically worked, and (3) a technical trigger (chart pattern, Bollinger Bands, RSI) to time entry and exit within that window.

## Key concepts

- **Spread** — the price differential between two related futures contracts (intramarket: two delivery months of the same commodity; intermarket: two related commodities), computed by subtracting the closing price of the contract you are short from the closing price of the contract you are long.
- **Legging in / legging out** — putting on or taking off the two sides of a spread at different times rather than simultaneously; Ross avoids this in his listed "no-leg" markets (Orange Juice, Heating Oil, Unleaded Gas, Copper, Coffee, Cotton, Live Hogs, T-Bills, Feeder Cattle) and prefers to enter/exit as a single spread order.
- **Exchange-recognized spread** — a spread combination the exchange itself margins as a unit (lower initial/maintenance margin than the two legs held separately), such as the MOB, NOB, or TED spread.
- **Seasonal window** — a defined, historically-derived date range (e.g., a 20-day bracketed window) during which a specific seasonal spread or outright trade has tended to move in a particular direction.
- **Optimized entry/exit date** — the single best-performing historical date for entering or exiting a seasonal trade, computed after the fact; Ross repeatedly shows this is inferior in practice to a chart-pattern-based entry/exit taken inside the seasonal window.
- **Ledge** — a short sideways congestion (up to about ten bars) where two matching highs and two matching lows can be connected with a ruler; Ross enters only on a genuine breakout through the Ledge's high or low, never on a gap past it.
- **Trend definition rule** — an emerging trend requires four consecutive closes beyond the open (or three plus a gap-confirmed open) in one direction; the breakout of that emerging trend's extreme makes it a "defined" trend, and the breakout of the following correction's extreme makes it an "established" trend. A correction lasting more than three bars becomes congestion or a new trend.
- **Bollinger Bands on the spread line** — applied directly to the spread's own price series (not the outright futures) using two standard deviations, which Ross notes contains roughly 95%+ of the spread line's movement; used only in combination with a chart pattern or oscillator, never alone.
- **RSI divergence on spreads** — used as a momentum confirmation: in choppy/sideways spreads, buy when price diverges lower while RSI is rising, and sell when price diverges higher while RSI is falling.

## Rules and setups

1. **Market selection for spreads**: Ross restricts spread trading to a defined list of liquid markets (currencies, energies, grains, financial instruments, meats, metals, softs) and explicitly avoids outright spread trades in Orange Juice and Cotton, and avoids or refuses to leg into Lumber, Value Line, Canadian Dollar, and Pork Bellies.
2. **Constructing a spread chart**: subtract the closing price of the short-side contract from the closing price of the long-side contract for each bar to build the spread line; a rising line means the spread favors the long side.
3. **Spread ratio**: when the two legs are not naturally 1:1 in dollar value (e.g., Gold vs. Silver), multiply one side's contract count to match dollar-value risk — Ross's worked example uses 2 short Silver contracts against 1 long Gold contract.
4. **Fundamentals filter**: before entering a seasonal spread, check weather, crop/production conditions, and relative price moves of both legs over the proposed window; reject the trade if the two legs' fundamentals are moving the "wrong way" relative to the expected seasonal differential (a worked Corn/Wheat example shows the trade skipped for exactly this reason).
5. **Time-window filter**: only take the trade within its historically defined seasonal window (bracketed date range, often about 20 days); a signal outside that window is not treated as a seasonal trade.
6. **Entry signal within the window**: use a chart pattern breakout (commonly the Ross Hook / 1-2-3's number-2 point) or an RSI-crosses-50%-with-price-above-its-moving-average combination as the trigger, not a mechanical "enter on date X" rule.
7. **Exit preference**: exit via chart pattern (a new opposing signal or hook) rather than a fixed "optimized" calendar exit date; Ross's own comparison shows the chart-pattern exit outperforming the optimized-date exit in a worked April/August Live Cattle example ($1,525 gross gain vs. $625).
8. **Named seasonal spread example**: long April Live Cattle / short August Live Cattle, entered around the third Friday in March, historically about 93% accurate and profitable 14 of 15 years in Ross's sample; a second Cattle example (long October Live Cattle / short February Live Cattle) is put on in the last week of June with an optimized exit around the first week of August.
9. **Ledge/breakout entry (non-seasonal spreads and outright trades)**: mark a Ledge (matching highs/lows over up to ten bars), enter only on a clean breakout through the marked level, and skip the trade if price gaps past the entry rather than trading through it.
10. **Bollinger Band signal on the spread line**: treat a sharp move outside the bands after a period of band-tightening as confirmation of trend continuation (not exhaustion); treat a sharp move outside the bands immediately followed by a retracement back inside as a sign of exhaustion instead.
11. **Filter combination rule**: never rely on Bollinger Bands (or any band study) alone — pair them with either a chart pattern or a non-correlated oscillator (Ross specifically warns against pairing Bollinger Bands with CCI, since both measure price deviation and are multicollinear).

## Risk and money management

Spreads are framed as an inherent risk-reduction tool rather than a source of leverage: because a spread position is effectively hedged, it carries lower exchange margin requirements and lower volatility than the equivalent outright futures position, and Ross describes using a spread specifically to hedge an existing outright position ahead of a scheduled fundamental report (a worked Crude Oil / API-report example). No explicit percent-of-equity position-sizing formula is given in the sampled pages; risk control is expressed instead through market selection (avoiding thin/treacherous markets), the no-legging rule for volatile spread pairs, and entering only within a confirmed seasonal window with a chart-pattern trigger rather than trading the calendar blindly. The one quantified backtest sampled (an April/August Live Cattle decision table) shows year-by-year worst-equity and best-equity swings alongside win-rate and average profit-per-trade statistics, used as the model for how Ross expects a seasonal spread to be vetted before being traded live.

## Psychology and discipline

Little dedicated psychology material was recovered in the sampled pages; the book's discipline content is procedural rather than emotional — favoring rules-based fundamentals/window/pattern filtering over "black box" mechanical signals, and repeatedly demonstrating (via the optimized-date-vs-pattern-exit comparisons) that a trader who mechanically chases a historically optimal date will underperform one who waits for the market's own chart-pattern confirmation within the window.

## Chapter map

- Ch 1–2 — What is a Spread? / Why Use Spreads?: definitions, suitable markets, legging in/out, advantages (lower margin, lower volatility, insensitivity to outright trend direction).
- Ch 3 — How to Trade Spreads to Reduce Risk: using a spread to hedge an existing outright futures position (worked Crude Oil/API report example).
- Ch 4–7 — Seasonal Spread Trade Selection, Filtering Process (Fundamentals, Time Window, Entry/Exit Signals): the core three-layer filter.
- Ch 8–9 — Seasonal Spread Examples; Non-Seasonal Spreads: worked currency and Cattle/Cattle spread cases.
- Ch 10–12 — Fractional Spreads, Conversions, Using Spreads to Reduce Volatility.
- Ch 13–15 — Trading Spreads Using Technical Indicators; Technical Filtering; Seasonal Spread Trading with Bollinger Bands and RSI.
- Ch 16–19 — Introducing Seasonals / What is a Seasonal? / Seasonal Futures Market Selection / Seasonal Futures Trade Selection: shifting the same framework to outright seasonal futures.
- Ch 20–22 — Outright Seasonal Futures: Checking Fundamentals; Time Window; Trading with Chart Patterns and Bollinger Bands.
- Ch 23–27 — Thinking and Trading Go Together; Beware of Stop Running; Carrying Charge Spreads; Converting Daytrades to Spreads; Wrap-Up.
- Appendices — Chart patterns for outright seasonal futures; decision tables (backtested seasonal spread statistics); resources.

## Strengths and caveats

This book is from a scanned copy with OCR run only on a sample of pages (front matter plus evenly spaced pages), so these notes reflect what was recoverable; entire chapters in the seasonal-futures half of the book (roughly chapters 16–27, corresponding to the later printed-page range) fell in the unsampled gaps and are represented here only by their table-of-contents titles rather than worked content. Within what was recovered, the book's strength is showing real backtested decision tables (year-by-year win rate, best/worst equity, average profit) for at least one named spread rather than asserting seasonality without evidence — a rarer feature than in most seasonality books. The repeated finding that pattern-based exits beat "optimized" calendar-date exits is a useful, falsifiable claim rather than vague seasonal folklore. Caveats: seasonal relationships (crop cycles, old-style carrying-charge markets, pre-2000s spread margining) can shift with changes in production geography, ethanol/biofuel demand, or exchange margin rules, and the book does not address this risk of seasonal decay; some fundamentals discussion (calling brokers for CBOT/CME printed spread yearbooks, phone-based order entry) is dated.

## Who should read it

Futures traders already comfortable with outright positions who want a structured way to reduce volatility and use recurring calendar effects, and who are willing to combine fundamentals research, a defined seasonal window, and a chart-pattern trigger rather than trade a seasonal calendar mechanically.

## Related books in this library

- [[joe-ross-trading-the-ross-hook]] — the Ross Hook pattern used throughout this book as the chart-pattern entry/exit trigger for spreads and seasonal trades.
- [[tte]] — Ross's Traders Trick Entry, applicable to the same hook-based entries referenced here.
- [[richard-l-weissman-mechanical-trading-systems]] — for contrast, a fully mechanical, backtested systems approach versus this book's fundamentals-plus-pattern discretionary filtering.
