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

The mechanical trend-following system Richard Dennis and William Eckhardt taught the Turtles in December 1983, released directly by an Original Turtle. A volatility-normalized, dual channel-breakout system: two Donchian-style entries (20-day and 55-day breakouts), a single volatility unit (N) driving both position size and stops, and rule-based pyramiding and exits, traded unchanged across roughly two dozen liquid U.S. futures markets. This page is the canonical rule set that [[curtis-faith-way-of-the-turtle--turtle-system]] and [[the-complete-turtletrader-the-legend-the-lessons-the-results--turtle-trading-system]] independently corroborate.

## Rules

**Markets.** Liquid U.S. futures only: T-bond, T-note, Eurodollar, T-bill, currencies (Swiss franc, Deutschmark, British pound, French franc, yen, Canadian dollar), S&P 500, coffee, cocoa, sugar, cotton, gold, silver, copper, crude oil, heating oil, unleaded gas. Grains and meats excluded. Once a trader opted out of a market, they stayed out consistently.

**N (volatility unit).** True Range = max(H−L, H−PDC, PDC−L). N = (19 × previous N + today's TR) / 20 — a 20-day EMA of true range, seeded with a 20-day simple average.

**Unit size.** Dollar volatility = N × dollars-per-point. Unit = (1% of equity) ÷ dollar volatility, truncated to whole contracts. Example: $1M account, heating oil N=0.0141, $42,000/point → unit ≈ 16.88 → 16 contracts. Recomputed weekly.

**Entries — System 1 (20-day breakout).** Buy/sell 1 unit on a 1-tick breakout of the 20-day high/low, intraday. Skip the signal if the last S1 breakout in that market (either direction) would have won — a profitable 10-day exit reached before moving 2N against it. A skipped signal is replaced by the 55-day (System 2) breakout as failsafe.

**Entries — System 2 (55-day breakout).** Buy/sell on a 1-tick breakout of the 55-day high/low; every signal taken regardless of the prior trade's outcome. Equity may be split freely between S1 and S2.

**Adding units.** Add 1 unit each ½N of favorable movement from the previous fill, up to 4 units/market — possibly all 4 in one day. Example (crude oil, N=1.20, entry 28.30): adds at 28.90, 29.50, 30.10.

**Stops.** Initial stop = 2N against entry (≈2% equity). Each add raises earlier units' stops by ½N, so stops normally converge to 2N below the newest unit. Stops were mental price levels, not resting broker orders; once hit, exit without exception.

**Whipsaw alternative.** Tighter ½N stop (≈0.5% risk), re-entering at the original signal price if stopped out — more trades, lower win rate, reported better net results for some Turtles; worst-case 4-unit risk still ≤2%.

**Exits.** S1 positions exit fully on a 10-day opposite breakout; S2 on a 20-day opposite breakout — whichever comes first with the stop, and intraday like entries.

**Position/correlation limits.** Max 4 units/market; 6 units one-direction across closely correlated markets (e.g. heating oil/crude, gold/silver, Swiss franc/Deutschmark, T-bill/Eurodollar); 10 across loosely correlated markets (e.g. gold/copper); 12 total long or short portfolio-wide.

**Execution tactics.** Prefer limit orders near the market over market orders. In fast markets, wait for stabilization before entering. On simultaneous correlated signals, take one contract-month per market, buying the strongest and selling the weakest in the group. Roll contracts a few weeks before expiration unless the near month is notably stronger.

## Risk

Per-unit risk is capped near 2% of equity by the 2N stop; the 4/6/10/12 ladder caps aggregate exposure. Notional account equity was cut 20% for every 10% drawdown, so sizing shrinks automatically in losing periods. The edge depends on a low win rate offset by rare large trend winners — exiting early or slow-rolling adds hurts returns even though it "feels" safer. Gap risk is real: the October 1987 rate-cut shock cost Turtles loaded in rate futures 20–40% of equity in a day despite the unit limits.

## Caveats

Real slippage and gap risk (scheduled events especially) run higher than the formulas imply. Dollar-volatility examples use early-2000s contract sizes and need rescaling. No formal backtest or win-rate data is given — only the anecdotal 80% average annual return across Turtles as a group, masking wide dispersion between individuals on the same rules. The S1 "skip on a winner" rule and 55-day failsafe are easy to misimplement; use the exact logic above, not a paraphrase.
