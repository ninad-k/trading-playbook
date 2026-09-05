---
title: Best Six Months Seasonal Strategy
author: Leslie N. Masonson
year: 2004
slug: leslie-n-masonson-all-about-market-timing--best-six-months-strategy
tier: A
category: Trend Following & Mechanical Systems
tags: [seasonality, calendar-effects, market-timing, macd, mechanical-systems]
difficulty: beginner
doc_type: system
parent: leslie-n-masonson-all-about-market-timing
pages: 275
one_liner: "Yale Hirsch's calendar system (long November-April, cash May-October) and Sy Harding's MACD-timed refinement, with September-avoidance variants."
related: [marcel-petro-market-timing, joe-ross-trading-spreads-and-seasonals]
source_file: "Leslie N Masonson - All About Market Timing.pdf"
---

## What it is

A pure calendar-timing system developed by Yale Hirsch in 1986 (published annually in the Stock Trader's Almanac) that holds a broad market index only during the historically strongest six months of the year (roughly November through April) and moves to cash for the historically weakest six months (May through October). The book presents three progressively refined variants: the original fixed-calendar version, Sy Harding's Seasonal Timing Strategy (STS) which uses the MACD indicator to move the entry/exit a few weeks earlier or later than the fixed calendar dates, and a September-avoidance variant (Vakkur/Colby) that isolates the single worst month rather than a full six-month block.

## Rules

1. **Base Best Six Months (BSM) rule.** Buy a broad market index fund (S&P 500, Nasdaq Composite, DJIA proxy, or Total Stock Market fund) on November 1 each year. Sell on April 30 of the following year and move proceeds into a money market fund or T-bills. Repeat annually — only two trades per year.
2. **Harding's calendar window (an alternative fixed-date version).** Enter on the last trading day of October; exit on the fourth trading day of May. Backtests in the book show this variant modestly outperforming Hirsch's original November 1/April 30 dates.
3. **MACD-enhanced entry/exit (Harding's STS).** Ignore MACD signals except near the calendar dates. For entry: take the first MACD buy-signal crossover that occurs on or after October 16 (if MACD is already on a buy signal when October 16 arrives, enter immediately; otherwise wait for the crossover). For exit: take the first MACD sell-signal crossover that occurs on or after April 20 (same logic — enter the exit immediately if already on a sell signal, otherwise wait for the cross). Recommended MACD settings from the base moving-average chapter: (12,25,9).
4. **September-avoidance variant (Vakkur).** Sell all positions on the last trading day of August. Stay in cash through September. Buy back on the first trading day of October. Hold through the rest of the year (or combine with rule 1's April 30 exit).
5. **Aggressive September short (Colby).** Instead of moving to cash, sell short on the last trading day of August and cover the short (going long again) on the last trading day of September. A further-refined variant shorts on September 5 (or the next trading day the market is open) and covers on October 27 (or the next open trading day), then goes long.
6. **Never skip a signal.** Take every calendar or MACD-triggered signal in sequence; do not selectively override a signal based on a market opinion, since backtested results assume full compliance.
7. **Stop-loss overlay.** Use a protective stop (the book does not fix an exact percentage for this system specifically but recommends 8–10% elsewhere) in case a given year's buy signal does not work out; simply re-enter on the next year's signal if stopped out.

## Risk

The strategy is invested in the market only about half the calendar year, which the book treats as an automatic ~50% reduction in market-risk exposure versus buy-and-hold, and multiple backtests confirm materially lower standard deviation and drawdown than buy-and-hold over the same period. The main risk is a "bad" favorable-season year: since the rules are calendar/indicator-triggered rather than valuation-based, a November–April period can still produce a loss (the book notes this is "always a possibility" and recommends a stop-loss as the safety valve rather than assuming the seasonal edge holds every single year). The MACD-enhanced version (Harding's STS) depends on correctly implementing and reading a real-time MACD signal — Harding's and Hirsch's own methodologies for computing the "same" MACD signal differ and can produce different entry/exit dates in the same year (in 2003, Hirsch's sell signal triggered April 30 vs. Harding's May 19, with different resulting returns), so results are sensitive to the exact implementation.

## Caveats

All of the multi-decade backtests reported (1950–2001, 1966–1988, 1964–2002) are theoretical: they generally exclude dividends, transaction costs and taxes, and the underlying indexes used in some early tests (e.g., the DJIA before tradable index products like Diamonds existed) were not directly investable at the time, so the reported dollar results assume a tradable proxy existed throughout. The September-avoidance short-selling variant (Colby) requires a brokerage account approved for shorting and is explicitly framed as for "more venturesome investors" rather than the base strategy's typical audience. Because this is fundamentally a calendar-pattern strategy rather than one grounded in a specific causal economic mechanism, its persistence into the future is an empirical bet on seasonal patterns (vacation-driven trading volume, tax-related flows, etc.) continuing to hold, which the book itself flags only qualitatively rather than with a formal significance test.
