---
title: The Turtle Trading System (Original Rules)
author: Curtis Faith
year: 2003
slug: turtlerules--turtle-system
tier: A
category: Trend Following & Mechanical Systems
tags: [turtle-trading, trend-following, breakout, atr, position-sizing, pyramiding, stops]
difficulty: intermediate
doc_type: system
parent: turtlerules
pages: 37
one_liner: "The master reference for the Turtle system: N-based unit sizing, System 1 (20-day) and System 2 (55-day) breakout entries, 2N stops, ½N unit-adding, and 10/20-day breakout exits."
related: [curtis-faith-way-of-the-turtle--turtle-system, the-complete-turtletrader-the-legend-the-lessons-the-results--turtle-trading-system, position-sizing]
source_file: "turtlerules.pdf"
---

## What it is

The complete mechanical trend-following system Richard Dennis and William Eckhardt taught the Turtles in December 1983, as released directly by an Original Turtle. It is a volatility-normalized, dual channel-breakout system: two Donchian-style entry variants (a 20-day and a 55-day breakout), a single volatility unit (N) that drives both position size and stop distance, and rule-based pyramiding and exits. It was traded unchanged across roughly two dozen liquid U.S. futures markets. This page is the canonical rule set that [[curtis-faith-way-of-the-turtle--turtle-system]] and [[the-complete-turtletrader-the-legend-the-lessons-the-results--turtle-trading-system]] both independently corroborate.

## Rules

**Markets.** Liquid U.S. futures only: 30-year T-bond, 10-year T-note, Eurodollar, 90-day T-bill, currencies (Swiss franc, Deutschmark, British pound, French franc, Japanese yen, Canadian dollar), S&P 500, coffee, cocoa, sugar, cotton, gold, silver, copper, crude oil, heating oil, unleaded gas. Grains and meats were excluded (position limits and floor-trading integrity, respectively). Once a trader opted out of a market, they had to stay out of it consistently.

**N (volatility unit).** True Range = max(H−L, H−PDC, PDC−L), where H/L are today's high/low and PDC is the previous day's close. N = (19 × previous N + today's TR) / 20 — a 20-day exponential moving average of true range, seeded with a 20-day simple average of TR.

**Dollar volatility and unit size.** Dollar volatility = N × dollars-per-point of the contract. Unit = (1% of account equity) ÷ dollar volatility, truncated down to whole contracts. Example: $1,000,000 account, heating oil N = 0.0141, $42,000/point → unit = ($1,000,000 × 0.01) / (0.0141 × 42,000) ≈ 16.88, truncated to 16 contracts. Unit size was recomputed weekly.

**Entries — System 1 (S1), 20-day breakout.** Buy 1 unit on a 1-tick breakout above the preceding 20-day high; sell short on a 1-tick breakout below the preceding 20-day low, traded intraday (not at the close). A System 1 signal is skipped if the last S1 breakout taken in that market (regardless of direction) would have been a winner — defined as reaching a profitable 10-day exit before moving 2N against the position. If a signal is skipped this way, the System 2 (55-day) breakout in that market becomes the failsafe entry, so a major move is never missed entirely.

**Entries — System 2 (S2), 55-day breakout.** Buy/sell on a 1-tick breakout of the preceding 55-day high/low. Every S2 signal is taken regardless of whether the prior S2 trade won or lost. Equity could be split freely between S1 and S2 (e.g. 100% S2, or a 50/50 split).

**Adding units (pyramiding).** After the initial unit, add one further unit each time price moves ½N in the trade's favor from the previous fill price, up to a maximum of 4 units per market. If the market moves fast enough, all 4 units could be added in a single day. Example (crude oil, N=1.20, 55-day breakout at 28.30): units added at 28.30, 28.90, 29.50, 30.10.

**Stops.** Initial protective stop = 2N against the entry price (≈2% of equity, since 1N ≈ 1%). As each new unit is added, stops on the earlier units are raised by ½N, so in the normal case all units in a position end up stopped at 2N below (above) the most recently added unit — though gaps or fast-market fills can leave stops uneven. Stops were mental/manual price levels, not resting orders with the broker, to avoid revealing size; once the price traded there, the position was exited without exception.

**Alternate "Whipsaw" stop.** A tighter ½N stop (≈0.5% risk per unit) with re-entry at the original signal price if stopped out. Produces more trades and a lower win rate but was reported to improve net results for some Turtles; it also avoids having to move earlier units' stops as new units are added, since worst-case total risk across 4 units never exceeds 2%.

**Exits.** System 1 positions exit entirely on a 10-day price breakout against the position; System 2 positions exit entirely on a 20-day price breakout against the position. All units making up a position exit together at the earlier of this breakout exit or the (adjusted) stop. Exits, like entries, are taken intraday as soon as the exit price trades, not at the close.

**Position/correlation limits.** Max 4 units in any single market; max 6 units (one direction) across closely correlated markets (e.g. heating oil & crude oil, gold & silver, Swiss franc & Deutschmark, T-bill & Eurodollar); max 10 units across loosely correlated markets (e.g. gold & copper); max 12 units total in one direction (long or short) across the whole portfolio — so a trader could theoretically hold 12 long and 12 short simultaneously.

**Execution tactics.** Prefer limit orders near the market over market orders to reduce slippage from the bid/ask "bounce." In fast markets, wait for at least a temporary stabilization before entering rather than chasing with a market order. When several correlated markets signal simultaneously, take only one contract-month per market (the most liquid), buying the strongest market and selling the weakest within a correlated group rather than taking every signal at once. Roll expiring contracts into the next month a few weeks before expiration unless the nearer month is trading noticeably stronger than the deferred month.

## Risk

Per-unit risk is capped near 2% of equity by the 2N initial stop; the 4/6/10/12 correlation ladder caps aggregate single-market and portfolio exposure. Account size itself was notional and dynamically resized: a 20% cut to notional equity for every 10% drawdown from the year's starting equity, so position sizing (and risk) automatically shrinks in losing periods. The system's edge depends on a low win rate (most 20/55-day breakouts fail to become trends) offset by a small number of large trending winners — exiting a winning trend early, or skipping/slow-rolling unit adds, materially damages long-run returns even though it "feels" safer. Extraordinary gap risk is explicitly acknowledged: the October 1987 crash's overnight Fed rate cut cost Turtles loaded long in interest-rate futures 20–40% of account equity in a single day despite the unit-limit rules.

## Caveats

The rules assume broker execution close to signal prices; real slippage and gap risk (especially around scheduled economic events) were higher than the formulas imply, as the 1987 example shows. N and dollar-volatility examples use early-2000s contract sizes and prices and need rescaling for current markets. The document provides no formal backtest, Sharpe ratio, or win-rate statistics — only anecdote and the claim of an 80% average annual compound return across the original Turtles as a group, which masks wide dispersion between individual traders using the identical rule set. The 20-day S1 "skip on a winner" rule and 55-day failsafe are easy to implement incorrectly; get the exact skip/failsafe logic from this page rather than a paraphrase.
