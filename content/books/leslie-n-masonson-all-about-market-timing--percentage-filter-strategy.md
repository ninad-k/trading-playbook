---
title: Value Line 4% / Nasdaq 6% Percentage Filter Strategy
author: Leslie N. Masonson
year: 2004
slug: leslie-n-masonson-all-about-market-timing--percentage-filter-strategy
tier: A
category: Trend Following & Mechanical Systems
tags: [percentage-filter, market-timing, trend-following, mechanical-systems, whipsaw]
difficulty: intermediate
doc_type: system
parent: leslie-n-masonson-all-about-market-timing
pages: 275
one_liner: "Ned Davis's Value Line 4% filter (buy 4% off a low, sell 4% off a high) and its 6% Nasdaq variant — a percentage-swing trend filter distinct from moving averages."
related: [michael-covel-trend-following, marcel-petro-market-timing]
source_file: "Leslie N Masonson - All About Market Timing.pdf"
---

## What it is

A percentage-swing filter system, originally developed by Ned Davis (Ned Davis Research) roughly 20 years before the book's publication and popularized in Martin Zweig's Winning on Wall Street, that generates buy and sell signals purely from percentage moves off recent swing lows and highs — not from a moving average or the calendar. The base version (VL4%) uses the Value Line Composite Index (VLCI, a geometrically-weighted "median stock" index of about 1,700 companies); a higher-volatility 6% variant (NC6%/NDX6%) applies the identical logic to the more volatile Nasdaq Composite and Nasdaq 100 indexes. Because neither the VLCI nor the Nasdaq indexes are directly tradable, signals are meant to be applied to a correlated index fund or ETF (or, for the VLCI specifically, an approximation via a broad-market fund, since Value Line index futures/options exist but are not recommended for average investors).

## Rules

1. **Core VL4% signal.** Using the weekly Friday closing price of the Value Line Composite Index (or the Value Line Arithmetic Index, VLAI — an equal-weighted alternative introduced in 1988): a **buy signal** triggers when the index closes 4% or more above its most recent swing low (e.g., a rise from 100.00 to 104.00 or higher). A **sell signal** triggers when the index closes 4% or more below its most recent swing high (e.g., a decline from 120.00 to 115.20 or lower).
2. **Execution.** On a buy signal, invest in a correlated index fund, sector fund, or ETF (per the book's Chapters 5–6). On a sell signal, move to cash (money market fund) or, for more aggressive investors, go short via an inverse/bear fund or by shorting the ETF directly (not available in retirement accounts, though bear funds are).
3. **Nasdaq 6% variant (NC6%/NDX6%).** Identical filter logic, applied to the Nasdaq Composite Index (NC6%) or Nasdaq 100 Index (NDX6%) using a wider 6% threshold to account for higher volatility in these indexes. Use **weekly** closing prices only — the book's own daily-interval backtests of this same 6% filter performed far worse (in one 13-year test, a 6% daily filter returned only $15,040 vs. $15.2M+ for the weekly filter over a comparable period) and are explicitly flagged as unusable.
4. **Prefer the arithmetic (equal-weighted) index where available.** Backtests over the same 1992–2002 period found the VLAI (equal-weighted) filter produced 51% more net profit than the otherwise-identical VLCI (geometrically-weighted, "median stock") filter ($123,915 vs. $81,998), and VLAI daily data outperformed VLAI weekly data ($266,792 vs. $123,915) over the same window — the index construction and data frequency both materially affect the filter's results, unlike with the Nasdaq variant where daily data hurt performance.
5. **Parameter is not uniquely optimal at 4%/6% — treat as a tunable band.** Nelson Freeburg tested every 1%–8% threshold combination on the VLCI from 1961–1992 (64 parameter sets); all beat buy-and-hold by at least 2:1. The single best combination found was an asymmetric 4% buy-threshold / 2% sell-threshold (645 VL points vs. 149 for buy-and-hold), narrowly ahead of a symmetric 2%/2% band (588 points) and the standard 4%/4% band (584 points) — meaning the exact threshold is not critical to the strategy working, but a tighter sell-threshold than buy-threshold showed a modest edge.
6. **Leverage variant.** Applying 2:1 leverage (beta of 2.0, e.g., via a leveraged fund) to the VL4% weekly signal roughly doubled the annualized return in the book's Ultra 7 backtest (21.7% vs. 14.23% for the unlevered same-day-execution version) at correspondingly higher risk.
7. **Never selectively skip a signal; use consistent execution timing.** Decide up front whether entries/exits execute on the same day the weekly threshold is confirmed or the next trading day (the book's tests show "next day" execution reduces total gain versus "same day" execution by roughly 1,400 percentage points over multi-decade tests, though it remains far ahead of buy-and-hold either way) and apply that timing consistently.

## Risk

Like the moving-average system in this book, the percentage-filter approach wins on a minority of trades: the original 1966–1988 VL4% backtest had 53 losing trades (average –3.7%) against 48 winning trades (average +11.9%), a roughly 3:1 win/loss ratio that makes the system's profitability dependent on cutting losses short and letting the (less frequent) winners run their full course. The system is vulnerable to extended sideways/range-bound whipsaw periods just like moving averages — a 1992–2002 VLCI weekly backtest lost money over 14 losing trades out of 15 (the 21st through 45th trades in the test), drawing the equity curve below its original starting capital, entirely within a 1980–1180 trading range. Choosing daily vs. weekly data materially changes outcomes and the direction of that change is not consistent across indexes — daily data improved results for the Value Line indexes but sharply worsened results for the Nasdaq indexes — so a trader cannot assume a data-frequency choice that worked for one index will transfer to another.

## Caveats

The Value Line Composite and Arithmetic Indexes are not directly tradable, so every VL4% backtest in the book is a proxy exercise: real-world results depend on how closely an actual index fund/ETF used to implement the signal tracks the underlying Value Line index, which the book does not quantify. All reported backtests exclude dividends and transaction costs, and most exclude taxes; several exclude even a bid/ask-spread estimate. The 6% Nasdaq threshold is described in the text as "arbitrarily" chosen to compensate for higher Nasdaq volatility rather than derived from the same rigorous multi-year parameter sweep Freeburg ran for the Value Line version, so its optimality (unlike the 4% VL threshold) rests on a narrower base of testing. As with the book's other systems, all figures are backtested/theoretical and not represented as achievable by any specific investor in real time.
