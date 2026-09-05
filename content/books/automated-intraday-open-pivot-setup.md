---
title: "Automated Intraday Open Pivot Setup"
author: "Jeff Reimer"
year: 2005
slug: automated-intraday-open-pivot-setup
tier: B
category: Day Trading & Scalping
tags: [forex, pivot-points, intraday, spreadsheet-system, money-management, gbpusd]
difficulty: beginner
doc_type: manual
pages: 9
one_liner: "A spreadsheet-driven forex system that compares the daily pivot point to the previous session's open to pick direction, then trades a fixed 20-pip limit/20-pip stop, best tested on GBP/USD."
related: [pivots, camarilla-levels, forex-intraday-pivots-trading-system-complete-system, forex-money-management]
source_file: "Automated_Intraday_Open_Pivot_Setup.pdf"
---

## Summary

Jeff Reimer describes a short, mechanical intraday forex system built around a spreadsheet ("trade sheet") that calculates a pivot point from the prior session's open/high/low/close and compares it to the previous open to set direction, then requires a second confirming calculation before entering. The whole daily process — record OHLC, run the calculator, place one order at the new session's open — is designed to take under two minutes.

## Key points

- Direction rule: pivot above the previous open → long bias; pivot below → short bias.
- Confirmation: for a long bias, (Previous High − Previous Open) must exceed the profit goal plus spread; for a short bias, (Previous Low − Previous Open) must exceed goal plus spread. Only then is a trade taken.
- The author's own testing of 16 limit/stop combinations found 20 pips each way most efficient.
- Backtested over three years of GBP/USD data (CMS), the 20/20 setup reportedly achieved 83.17% accuracy.
- Session close/open time must match the trader's preferred market (author trades Asian/Sydney off a 17:00 EST close); other sessions require recalculating OHLC at their own local close.
- Position sizing example: 1 mini-lot (10K) per $250 of balance at 200:1 leverage — called "high by most standards" by the author himself.
- A hypothetical compounding table (starting at $250, reaching millions within a year if lot size scales with balance) is explicitly flagged as hypothetical.
- The Asian session reportedly dips ~20 points from the open before reversing toward the forecast direction, motivating a discretionary entry 15–25 points beyond the open rather than immediately at the open.

## Actionable rules

1. At the session close, record open, high, low, close for the pair being traded.
2. Calculate the pivot point; compare it to the previous open to set direction.
3. Confirm only if (High − Open) [long] or (Low − Open) [short] exceeds the profit goal plus spread; otherwise skip the session.
4. Enter at the new session's open, or wait for price to move 15–25 points against the open first, per the session's typical pattern.
5. Set both limit and stop at 20 pips from entry (the author's tested optimum).
6. Cross-check against a standard indicator (e.g., MACD) or a higher timeframe before entering.
7. Size positions at roughly 1 mini-lot per $250 of equity at 200:1 leverage (the author's own — aggressive — practice); readers are told to set their own comfortable risk level.

## Caveats

Self-published, with a liability disclaimer; the 83.17% accuracy and multi-million-dollar compounding projection come solely from the author's own backtest and are not independently verified. The position sizing shown (200:1 leverage, full balance re-compounded into lot size) is extremely aggressive. The system requires manual entry into an accompanying spreadsheet not included in this text.

## Who it is for

Part-time forex traders wanting a very short daily routine for one intraday session, comfortable with an aggressive, single-pair (GBP/USD-tested), fixed-pip approach and setting their own risk parameters around it.
