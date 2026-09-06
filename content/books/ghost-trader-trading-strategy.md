---
author: George Pruitt, John R. Hill
category: Trend Following & Mechanical Systems
difficulty: advanced
doc_type: article
one_liner: Excerpt from Building Winning Trading Systems with TradeStation showing
  a template that only issues a real trade signal after a simulated 'ghost' trade
  on the same rules has lost.
pages: 4
related: []
reviewed_pdf_pages: 1-4
slug: ghost-trader-trading-strategy
source_file: Ghost_Trader_Trading_Strategy.pdf
source_review: full
tags:
- tradestation-easylanguage
- mechanical-system
- moving-average
- rsi
- trade-filtering
- backtesting
tier: B
title: The Ghost Trader Trading Strategy
year: 2002
---

## Summary

This excerpt from Pruitt and Hill's TradeStation programming book presents the "Ghost Trader" as a coding template, not a complete standalone strategy. The premise: some traders believe a loss is more likely followed by a win, so the system keeps a hidden ("ghost") record of every hypothetical trade a base EMA/RSI system would take, and only fires a real order when the last simulated-or-real trade on that logic was a loser. The article walks through the EasyLanguage code for tracking simulated positions and gating real signals on prior outcome.

## Key points

- **Base long entry** — 9-period EMA of closes above the 19-period EMA of highs, and 9-period RSI of closes crossing below 70, triggers a buy-stop at today's high for tomorrow.
- **Base short entry** — mirror condition: 9 EMA of closes below 19 EMA of lows, RSI crossing above 30, triggers a sell-stop at today's low.
- **Exit** — longs exit on a break of the lowest low of the past 20 days; shorts exit on a break of the highest high of 20 days.
- **Ghost-tracking** — variables `myPosition`, `myEntryPrice`, `myProfit` simulate every trade the base logic would generate, whether or not a real order was placed.
- **Gating rule** — a real order fires only when `myProfit < 0`, i.e., the last tracked simulated-or-real trade was a loss.
- **Illustrative result** — over a 2000-2002 sample, filtering to "only trade after a loser" produced fewer trades but a better net result than taking every signal, in the authors' own example.

## Actionable rules

1. Track a simulated position/P&L using the base EMA(9)/EMA(19)/RSI(9) entries and 20-day-breakout exits on every bar, regardless of whether a real trade is taken.
2. Only submit a real buy-stop/sell-stop when the base rules trigger AND the last closed simulated-or-real trade was a loss.
3. Exit real positions using the same 20-day high/low breakout used for the simulated trades.
4. Account for gap opens with `MaxList`/`MinList` between the stop price and the actual open when recording simulated entry/exit prices.

## Caveats

This is a coding template to illustrate a trade-filtering technique, not a validated system — one illustrative backtest window is shown, with no out-of-sample testing, no risk/sizing rules, and no proof that "trade only after a loss" holds statistically beyond the example given.

## Who it is for

TradeStation/EasyLanguage programmers wanting a worked example of trade-outcome-dependent filtering logic layered on a base mechanical system, not traders looking for a ready-to-use strategy.
