---
title: "Volatility-Selective Defensive Straddle Writing"
author: William R. Gallacher
year: 1999
slug: mcgraw-hill-the-options-edge-winning-the-volatility-game-with-options-on-futures--defensive-straddle-writing
tier: A
category: "Options, Futures & Derivatives"
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

**Volatility measurement.** Compute the mean absolute deviation (MAD) of daily percentage price changes over a 30-day lookback (the choice of 30 was fixed in advance, not optimized). Market volatility = 22 × MAD (as a percentage of futures price). Compute the option's implied volatility either by iterating the pricing formula or, for at-the-money options, via the shortcut: implied volatility ≈ 40 × (ATM straddle premium ÷ 2) ÷ (futures price × √(trading days to expiry)).

**Selection filter.** Write a straddle only when implied volatility > market volatility (i.e., the option looks overvalued relative to recent price behavior). Skip straddles where implied volatility ≤ market volatility. In the tested database this filter alone improved the payout ratio only modestly, from 0.902 (defended, unfiltered) to 0.884 (defended, filtered) — most of the edge comes from the defensive hedge below, not the filter.

**Entry.** Write the at-the-money put and call together (a straddle, not a strangle) at the same strike, since the straddle captures the maximum available premium. Use limit orders priced at the estimated true midpoint between bid and ask when entering; market orders are acceptable on exit.

**Defensive trigger (long side).** At the moment of writing, set an upper trigger = strike price + total straddle premium received, and a lower trigger = strike price − total straddle premium received. If the underlying future closes above the upper trigger, buy one futures contract at that closing price to hedge the losing call. If it closes below the lower trigger, sell one futures contract at that closing price to hedge the losing put.

**Defensive trigger (protecting the hedge).** A long futures hedge (protecting a written call) is itself closed out if the future subsequently closes back below the original straddle strike price; a short futures hedge (protecting a written put) is closed out if the future closes back above the original strike. This locks in a fixed, bounded loss on the futures leg and returns the trader to the pre-hedge state, ready to re-hedge again if necessary (rare, but it happens).

**Exit.** Hold both the straddle and any hedge to option expiry unless the hedge-protection rule above triggers first. At expiry, one side of the straddle is exercised against the writer and offset with futures if not already covered.

**Position sizing / selectivity filters.** Only write straddles yielding at least $2,500 in total premium (the level below which ~$130 of round-trip commission per straddle erodes most of the edge); this rules out most straddles in low-priced/low-volatility markets (sugar, cocoa, cattle, corn, gold) unless time-to-expiry is long. Diversify across as many of the 15 tested commodities as possible — independent straddles across uncorrelated markets is what keeps aggregate equity variability low enough to finance a large notional book on comparatively little margin.

## Risk

Per-position risk is open-ended until the defensive trigger fires (the futures market can gap through the trigger level, especially around scheduled news, so realized loss can exceed the theoretical 2× premium bound implied by the trigger design). Aggregate portfolio risk is controlled mainly through diversification rather than any explicit stop-loss cap on total equity: the book relies on the low correlation of straddle losses across 15 independent commodities to keep simultaneous drawdowns unlikely, not on a portfolio heat limit. Execution costs matter more than in most systems because the edge is thin: Gallacher's own accounting knocks the pre-cost 15% gross edge down to about 12% after bid-ask slippage and to roughly 8% net after commissions, meaning a system that looks solidly profitable gross can be marginal or negative if traded in small size or with high per-trade costs. The strategy is not defined for out-of-the-money strangles, deep-in-the-money adjustments, or partial position scale-outs — it is an all-or-nothing straddle-and-hedge design.

## Caveats

The defensive-hedge rule was tested using daily closing prices only (not intraday highs/lows), so the backtest cannot capture intraday stop-outs or same-day whipsaws through both triggers; Gallacher argues this makes the test conservative but acknowledges it as a real limitation. The $2,500 premium floor and $130 commission estimate reflect late-1990s retail futures-option brokerage pricing and should be recalibrated for current commission structures before being used as a hard rule. The volatility-selectivity filter's improvement (0.902 → 0.884) is based on a reduced sample (2,627 of the original 3,781 observations) and Gallacher himself flags the result as directionally suggestive rather than statistically strong; a further, more aggressive filter (implied volatility ≥ 1.5× market volatility) dropped the ratio further to 0.851 but on a sample too small (315 observations, concentrated in a few commodities) to be considered reliable.
