---
author: Tom DeMark and Rocke DeMark
category: Indicators
difficulty: advanced
doc_type: article
one_liner: Currency Trader magazine article explaining Tom DeMark's TD Sequential
  indicator (TD Setup and TD Countdown) for timing trend exhaustion in forex.
pages: 6
related:
- demark-tom-demark-on-day-trading-options
- divergence
- macd
- chart-patterns-tutorial
reviewed_pdf_pages: 1-6
slug: td-sequential
source_file: TD_Sequential.pdf
source_review: full
tags:
- td-sequential
- countertrend
- trend-exhaustion
- forex
- demark
- setup-countdown
tier: B
title: Countertrend Forex Trading with TD Sequential
year: 2005
---

## Summary

A January 2005 Currency Trader magazine article by Tom DeMark and Rocke DeMark introducing TD Sequential, a countertrend timing tool built from two components: TD Setup (a momentum count comparing today's close to the close four bars earlier) and TD Countdown (a trend-exhaustion count comparing today's close to the high/low two bars earlier). The article argues markets only trend 25-30% of the time, so an objective tool for spotting trend exhaustion — buying weakness and selling strength — has an edge over pure trend-following, illustrated with GBP/USD, EUR/USD, and AUD/NZD daily charts.

## Key points

- **TD Price Flip** — the required "initialization" bar before a Setup can begin: the close immediately before Setup bar 1 must cross relative to the close four bars earlier in the opposite direction of the impending Setup.
- **Buy Setup** — 9 consecutive closes each less than the close 4 bars earlier; interruption at any point resets the count to zero.
- **Sell Setup** — 9 consecutive closes each greater than the close 4 bars earlier.
- **Setup "perfection"** — a buy Setup is perfected when the low of bar 8, bar 9, or a later bar is below the lows of both Setup bars 6 and 7 (mirrored for a sell Setup using highs).
- **TD Countdown** — begins once a 9-bar Setup completes; counts (non-consecutively) bars where the close is ≤ the low two bars earlier (buy) or ≥ the high two bars earlier (sell), until 13 valid Countdown bars accumulate.
- **Countdown 13 qualifier** — for a buy Countdown, the low of bar 13 must be ≤ the close of Countdown bar 8 (mirrored for sell).
- **Countdown cancellation** — a buy Countdown is cancelled if price closes above the entire Setup's high range, or if a contradictory sell Setup completes first.
- **Recycling** — if selling intensifies enough to extend a buy Setup past 18 consecutive closes before Countdown completes, the Countdown process restarts ("recycles").
- On daily charts, completed Countdown "13"s coincide with a market top or bottom roughly 4-5 times per year; shorter timeframes produce more frequent signals.

## Actionable rules

1. Confirm a TD Price Flip before starting to count a Setup.
2. Count 9 consecutive closes vs. the close 4 bars earlier to complete a Setup (buy: less than; sell: greater than); the count resets on any interruption.
3. Require Setup "perfection" (bar 8/9/later low or high beyond Setup bars 6-7) before treating the Setup as a reliable signal.
4. After Setup completes, count Countdown bars (close vs. high/low 2 bars earlier) to 13, applying the bar-8 qualifier, to time the actual entry against the trend.
5. Cancel and restart if a contradictory Setup forms before Countdown 13, or if price closes beyond the full Setup range.

## Caveats

This is a 6-page magazine article, not the full TD Sequential methodology from DeMark's books — some edge cases (e.g., full recycling rules, TD Combo, exact tie-breaking conventions) are referenced but not fully specified here. TD Sequential, TD Setup, TD Countdown, and TD Price Flip are registered trademarks, and the rules as counted by different charting platforms can vary slightly from DeMark's proprietary implementation.

## Who it is for

Traders wanting an objective, rule-based countertrend timing tool to identify probable trend-exhaustion points, particularly in forex; requires care to implement the counting rules exactly, and works best alongside other confirmation rather than as a standalone system.
