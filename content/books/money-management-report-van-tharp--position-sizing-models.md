---
title: "Nine Position-Sizing Models (Equal Units, % Risk, % Volatility, Kelly)"
author: Van K. Tharp
year: 1997
slug: money-management-report-van-tharp--position-sizing-models
tier: A
category: Money Management & Position Sizing
tags: [position-sizing, percent-risk, percent-volatility, kelly-criterion, portfolio-heat]
difficulty: intermediate
doc_type: system
parent: money-management-report-van-tharp
pages: 70
one_liner: "Nine formula-based ways to decide how many units to trade, from units-per-fixed-dollars through percent-risk, portfolio heat, and the Kelly Criterion."
related: [position-sizing, curtis-faith-way-of-the-turtle, balsara-nauzer-j-money-management-strategies-for-futures-traders]
source_file: "Money Management Report - Van Tharp.pdf"
---

## What it is

A menu of nine mutually compatible position-sizing algorithms Van Tharp presents in his Special Report on Money Management, each answering "how many units (shares/contracts) do I trade right now?" as a function of account equity. None of the models specify entries, exits, or stops — they are pure sizing overlays, tested by Tharp against a fixed reference system (a 55-day-high/low breakout entry with a 21-day trailing stop, 10 commodities, 1981-91, $1,000,000 starting equity) so that only the sizing method varies between his illustrative backtest tables. All nine models are anti-martingale: position size grows with equity and shrinks with losses, never the reverse.

## Rules

**Equity basis (choose one before applying any model below).** Core equity = starting cash minus the risk allocation of every currently open position (most conservative). Total equity = cash plus full mark-to-market value of all open positions (most aggressive). Reduced total equity = core equity plus any profit or risk-reduction locked in by a raised stop (middle ground).

**Model 1 — Units per fixed amount of money.** Trade 1 unit per $X of equity (e.g., 1 contract per $50,000). Simplest model; never rejects a signal for being "too risky," but treats all instruments as equal regardless of their actual dollar volatility, and a small account can only add a unit by roughly doubling its equity.

**Model 2 — Equal units / equal leverage.** Divide capital into N equal-dollar units (e.g., five $10,000 units from $50,000). For stocks, buy $10,000 worth of each selected position. For futures, decide a maximum total product value you're willing to control, divide it into N units, and take one contract per unit only if that contract's notional value fits within one unit.

**Model 3 — Percent of margin.** Cap the margin committed to any one new position at a fixed percent of equity (e.g., 5%). Units possible = (allowed margin $) ÷ (margin required per contract), rounded down. Optionally also cap total portfolio margin (e.g., 30% of equity).

**Model 4 — Percent volatility.** Measure the instrument's average true range (ATR) over a lookback (Tharp's example uses a 4-day average) and convert it to a dollar value per contract. Units = (equity × max % volatility allowed, e.g., 2%) ÷ (dollar value of one day's ATR per contract), rounded down. Optionally cap total portfolio volatility exposure (e.g., 5-10% of equity) across all open positions combined.

**Model 5 — Percent risk.** Define risk per contract as (entry price − stop price) × dollar value per point. Units = (equity × max % risk allowed) ÷ (dollar risk per contract), rounded down. Example: $50,000 account, 2.5% risk limit = $1,250; gold risk of $1,000/contract (10-point stop × $100/point) → 1 contract; corn risk of $250/contract (5-cent stop × 5,000 bu) → 5 contracts. General risk-percentage guidance: under 1% per position when trading other people's money; up to about 3% for one's own capital; smaller than these if stops are tighter than the average daily range; larger only if the system's win rate and reward/risk ratio are both well above average.

**Model 6 — Periodic (daily/hourly) money management adjustments.** Re-measure open risk or open volatility on a fixed schedule (daily, hourly) using current (not entry-day) equity and current stop distance, and trim the position back down to the target percentage whenever a favorable move has pushed the notional exposure above the limit — without touching the stop itself, which stays a separate, exit-logic decision.

**Model 7 — Group control.** Cap the combined risk (or volatility, margin, or unit count) allowed across a correlated group of instruments (e.g., all interest-rate futures, all technology stocks) at a fixed percent of equity, so that a single-sector move cannot produce portfolio-wide damage even though each individual position passed its own Model 1-5 limit.

**Model 8 — Portfolio heat.** Set a ceiling on total open risk across the entire portfolio at once (Tharp cites 20-25% as a common professional ceiling, and suggests deriving it as roughly 80% of the system's Kelly-Criterion-implied optimal risk fraction — see Technique below). Divide the heat ceiling by the maximum number of positions you expect to hold simultaneously to back into a workable per-position risk limit.

**Model 9 — Long vs. short netting.** When a sizing model equalizes exposure (Models 2-5, not Model 1), one long position and one offsetting short position in different but relatively uncorrelated markets may be counted together as a single unit of portfolio heat/group risk, since their price risks partially cancel.

**Kelly Criterion (for setting an upper bound on Models 5/8).** Kelly % = W − [(1 − W) ÷ R], where W = historical win rate (as a decimal) and R = average winning trade size ÷ average losing trade size. Example: W = 0.5, R = 2.0 → Kelly % = 0.5 − (0.5 ÷ 2) = 0.25 (25%). Tharp recommends trading at roughly 80% of the raw Kelly value, then dividing that by the maximum expected number of simultaneous positions to get a per-position risk figure (e.g., 80% × 25% = 20%, ÷ 10 expected positions ≈ 2% per position).

**"Market's money" technique (aggressive overlay, not a standalone model).** Risk only a small fixed percent (e.g., 1%) of starting equity, but risk a much larger, near-Kelly-optimal percent (e.g., 4%) of accumulated open profits above starting equity, so that risk capacity scales automatically with unrealized gains while principal stays protected; optionally cut the base risk percentage further (e.g., from 1% to 0.9% to 0.8%) for every additional 5% drawdown below starting equity.

## Risk

Every model here bounds only the sizing decision, not the trade's actual outcome — a stop can still gap through its intended exit price, and Tharp's own tables show that even a well-chosen percent-risk level (e.g., 25% under his reference system) can carry an 84% peak-to-trough drawdown despite producing the best long-run reward-to-risk ratio in the sample. Models 1-3 (fixed units, equal units, percent margin) do not directly account for an instrument's actual price volatility, so they can silently concentrate risk in whichever position happens to be most volatile at the time. Group control (Model 7) and long/short netting (Model 9) depend on correlation assumptions that can break down precisely when they matter most — during broad, correlated market shocks, "independent" positions often move together anyway.

## Caveats

The backtest tables illustrating Models 1, 4, and 5 all use the same single reference system (55/21-day breakout, 10 commodities, 1981-91, $1,000,000 start), so specific breakpoints (e.g., "this system needs at least $100,000 to trade at 1% risk") are properties of that system and dataset, not universal constants — Tharp is explicit that a different system's expectancy and stop size will produce different safe risk percentages. The Optimal-f technique (Ralph Vince's method, mentioned as an alternative to Kelly but not detailed here since Tharp recommends against it) is only briefly critiqued in the source report, not fully specified; readers wanting Optimal-f itself should consult Vince's own work. Dollar figures (margins, contract values) reflect mid-1990s markets and need rescaling for current instruments.
