---
title: "Volatility-Selective Defensive Straddle Writing"
author: William R. Gallacher
year: 1999
slug: mcgraw-hill-the-options-edge-winning-the-volatility-game-with-options-on-futures--defensive-straddle-writing
tier: A
category: "Options, Futures & Derivatives"
tags: [straddle-writing, volatility, options-on-futures, defensive-hedging, implied-volatility]
difficulty: advanced
doc_type: system
parent: mcgraw-hill-the-options-edge-winning-the-volatility-game-with-options-on-futures
pages: 294
one_liner: "Write at-the-money straddles only when implied volatility exceeds MAD-based market volatility, then hedge the losing side with futures once price closes past strike ± premium."
related: [balsara-nauzer-j-money-management-strategies-for-futures-traders, position-sizing, lawrence-g-mcmillan-profit-with-options]
source_file: "Mcgraw Hill - The Options Edge Winning The Volatility Game With Options On Futures.pdf"
---

## What it is

A systematic, technical (non-fundamental) approach to writing at-the-money straddles on commodity futures options, developed and backtested by William Gallacher across a 1996-98, 15-commodity, 3,781-observation database. The system has two independent layers: a volatility-based filter that decides which straddles are worth writing, and a mechanical defensive hedge that caps losses on straddles that move against the writer. Tested alone, indiscriminate straddle writing is break-even (payout ratio ≈ 1.00); the defensive hedge alone moves the ratio to about 0.90; adding the volatility filter moves it to about 0.88, i.e., an edge of roughly 12% of premium before transaction costs.

## Rules

**Volatility measurement.** Compute the mean absolute deviation (MAD) of daily percentage price changes over a 30-day lookback (fixed in advance, not optimized). Market volatility = 22 × MAD (as a percentage of futures price). Implied volatility for an at-the-money option ≈ 40 × (ATM straddle premium ÷ 2) ÷ (futures price × √(trading days to expiry)).

**Selection filter.** Write a straddle only when implied volatility > market volatility. This filter alone moved the tested payout ratio only modestly, from 0.902 (defended, unfiltered) to 0.884 (defended, filtered) — most of the edge comes from the defensive hedge, not the filter.

**Entry.** Write the at-the-money put and call together at the same strike (a straddle, not a strangle, to capture maximum premium). Enter with a limit order near the true bid-ask midpoint; exit hedges at the market.

**Defensive triggers.** At the moment of writing, set upper trigger = strike + total premium received, lower trigger = strike − total premium received. If the future closes above the upper trigger, buy one futures contract at that close to hedge the losing call; if it closes below the lower trigger, sell one futures contract to hedge the losing put. Protect the hedge itself: close a long futures hedge if the future closes back below the original strike, or a short hedge if it closes back above — locking in a bounded loss and resetting to the pre-hedge state, ready to re-hedge again if needed.

**Exit.** Hold the straddle and any hedge to option expiry unless a hedge-protection trigger fires first.

**Position sizing.** Only write straddles yielding at least $2,500 in premium (below which ~$130 of round-trip commission erodes most of the edge); this excludes most low-premium markets (sugar, cocoa, cattle, corn, gold) unless expiry is distant. Diversify across as many of the 15 tested commodities as possible — independent straddle losses keep aggregate equity variability low enough to finance a large book on comparatively little margin.

## Risk

Per-position risk is open-ended until a trigger fires — futures can gap through a trigger level, so realized loss can exceed the theoretical bound. Portfolio risk is controlled mainly through diversification, not an explicit total-equity stop. Execution costs matter more than in most systems given the thin edge: Gallacher's own accounting takes the 15% gross edge down to ~12% after slippage and ~8% net after commissions. The system has no defined variant for strangles, deep-in-the-money adjustments, or partial scale-outs — it is all-or-nothing straddle-and-hedge.

## Caveats

The defensive-hedge rule was tested on closing prices only, not intraday highs/lows, so the backtest cannot capture same-day whipsaws through both triggers. The $2,500 premium floor and $130 commission reflect late-1990s brokerage pricing and need recalibration. The volatility filter's improvement (0.902 → 0.884) is based on a reduced sample (2,627 of 3,781 observations) that Gallacher flags as suggestive, not statistically strong; a more aggressive filter (implied volatility ≥ 1.5× market volatility) dropped the ratio further to 0.851 but on too small and skewed a sample (315 observations) to trust.
