---
title: The Array Trading System
author: Thomas H. Kee
year: 2010
slug: buy-and-hold-is-dead--array-trading-system
tier: A
category: Trend Following & Mechanical Systems
tags: [support-resistance, market-timing, mechanical-trading, day-trading, swing-trading]
difficulty: intermediate
doc_type: system
parent: buy-and-hold-is-dead
pages: 322
one_liner: "Six named strategies that trade a mechanical buy/short rule against a daily support/resistance array built from three time frames across the Dow, NASDAQ, and S&P."
related: []
source_file: "Buy and Hold Is Dead.pdf"
---

## What it is

A family of six rule-based trading strategies that all share one underlying technical process: build a support/resistance "array" for a market or stock from three time frames (near-term 5-minute/5-day, midterm 30-minute/15-day, long-term daily/6-month), sort the levels around the current price, and trade the same two buy rules and two short rules against whichever level price is closest to. The six strategies differ in instrument, holding period, and stop mechanics, but all end flat/in cash between signals and none uses discretionary sizing.

## Rules

**Core signal logic (all strategies):**
- Buy when support is tested, or when resistance breaks higher.
- Short (or buy an inverse ETF) when resistance is tested, or when support breaks lower.
- A "test" is price coming within a small tolerance of a level: 0.05 points for an individual stock, 3 index points for the NASDAQ, 25 points for the Dow.

**Strategy 1 — Featured Stock of the Day** (day trading, one stock): trade stocks priced $5–$100, liquid, same share count every trade; enter within $0.05 of the array level; stop loss $0.21, profit stop $0.35, trailing profit stop $0.10 (ensure profit-stop minus trailing-stop exceeds the stop loss by ≥$0.10); begin 5 minutes after the open, stop trading 5 minutes before the close; re-enter after a stop up to 3 times (5 max); always flat overnight.

**Strategy 2 — Stock of the Week** (swing trading, one stock, Monday–Friday): start and end each week in cash; exclude stocks reporting earnings or major news that week; same share count every trade; tight stop loss; unlimited same-week re-entries after a stop, but no strategy updates during market hours (updates only overnight); position closed by rule Friday before the close regardless of open profit/loss.

**Strategy 3 — Strategic Plan** (position trading the Dow via ETFs, 1–3 month typical duration): trade only DDM (long 2x Dow) and DXD (short 2x Dow); fixed dollar size per trade (e.g., $50K); enter only on a test of major long-term support/resistance (within 25 Dow points); stop loss 0.5% of position; 10% trailing profit stop; convert DDM↔DXD as price crosses back and forth around the tested level, repeating as needed; never initiate mid-channel; mostly in cash.

**Strategy 4 — Day Trading Strategy** (NASDAQ via QID/QLD, intraday only): begin 5 minutes after open, stop 5 minutes before close; buy QLD on a support test or resistance break, buy QID (short-equivalent) on a resistance test or support break; no fixed-price stop loss — exit immediately if the tested level breaks; "three-point rule" defines an official test (within 3 NASDAQ points); "five-point rule" re-enters in the new direction if price moves 5 points past balance; "one-point rule" exits/reverts to cash if price then reverses 1+ point back through the level; maximum 2 stops per parameter (~9 NASDAQ points, ≈1.5% loss), then that level is retired until a new test occurs; never hold overnight.

**Strategy 5 — Swing Trading Strategy**: identical rule set to Strategy 4 (three-point/five-point/one-point rules, same ~1.5% loss cap per parameter) but positions are expected to be held overnight; uses the swing-trading array (midterm + long-term data points only, wider spreads than the day-trading array).

**Strategy 6 — Lock and Walk Strategy**: identical to Strategy 4's day trading rules but capped at one hour of activity (commonly the first hour); exits automatically at 1–2% gain (user's discretion) or when the hour ends, whichever comes first; otherwise flat.

## Risk

Every strategy fixes size mechanically (same share count or same dollar amount every trade) rather than scaling with conviction, so risk is controlled entirely through the stop rules above, not position sizing. The index strategies (4–6) cap loss at roughly 1.5% of the traded ETF value per support/resistance parameter by limiting re-entries to two attempts, then require a fresh test of a different level before trading resumes — this "retire the level" rule is the primary defense against repeated whipsaw losses in a choppy, non-trending tape. Overnight risk is explicitly priced into the choice of strategy: Strategies 1, 4, and 6 avoid it entirely by closing flat each day; Strategies 2, 3, and 5 accept it as the cost of capturing multi-day moves, and the book warns that a surprise overnight gap can produce a loss larger than the mechanical stop implies — the prescribed response is to take the loss, revert to cash, and only re-enter if the rule-based trigger fires again.

## Caveats

The buy/short and test/break rules are internally consistent but rely entirely on the trader's own subjective trendline placement when building the array (drawing support/resistance lines "by hand" from peaks and troughs) — two traders following the same instructions could produce different levels and therefore different trades. The book does not present an independent, out-of-sample backtest of the six strategies; the worked examples are individual live/simulated trades from the 2008–2009 window, not a multi-year track record, so realized win rates and drawdowns should be treated as illustrative rather than statistically established. Several execution features described (hidden conditional orders, automated trade simulators, correlated stock filters) are tied to the author's own brokerage/service platform and may not be replicable with a generic broker.
