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

**Equity basis.** Core equity = cash minus the risk allocation of every open position (most conservative). Total equity = cash plus full mark-to-market value of open positions (most aggressive). Reduced total equity = core equity plus profit/risk-reduction locked in by a raised stop (middle ground). Pick one before applying any model below.

**1 — Units per fixed money.** Trade 1 unit per $X of equity. Simplest; never rejects a signal, but ignores each instrument's actual volatility and a small account can only add a unit by roughly doubling its equity.

**2 — Equal units / equal leverage.** Divide capital into N equal-dollar units (e.g., five $10,000 units from $50,000); buy that much of each position, or, for futures, take one contract per unit only if its notional value fits within one unit.

**3 — Percent of margin.** Cap margin on any new position at X% of equity. Units = (allowed margin $) ÷ (margin per contract), rounded down. Optionally cap total portfolio margin too (e.g., 30%).

**4 — Percent volatility.** Convert the instrument's average true range (e.g., 4-day average) to a dollar value per contract. Units = (equity × max % volatility, e.g., 2%) ÷ (dollar ATR per contract), rounded down. Optionally cap total portfolio volatility (5-10% of equity).

**5 — Percent risk.** Risk per contract = (entry − stop) × dollar value per point. Units = (equity × max % risk) ÷ (risk per contract), rounded down. Example: $50,000 account, 2.5% limit = $1,250; gold at $1,000/contract risk → 1 contract; corn at $250/contract risk → 5 contracts. Guidance: under 1% trading others' money, up to ~3% on one's own capital, smaller if stops are tighter than the daily range, larger only with an above-average win rate and reward/risk ratio.

**6 — Periodic adjustments.** Re-measure open risk or volatility on a fixed schedule (daily/hourly) using current equity and current stop distance; trim the position back to target whenever a favorable move has pushed exposure above the limit, without moving the stop itself.

**7 — Group control.** Cap combined risk/volatility/margin across a correlated group (e.g., all interest-rate futures) at a fixed % of equity, so one sector's move can't damage the whole portfolio even if each position passed its own Model 1-5 limit.

**8 — Portfolio heat.** Cap total open portfolio risk (20-25% is a common professional ceiling; derive it as ~80% of the Kelly-implied optimal fraction — see below). Divide the heat ceiling by the expected max simultaneous positions to back into a per-position limit.

**9 — Long vs. short netting.** Under an exposure-equalizing model (2-5), one long and one offsetting short in uncorrelated markets may count as a single unit of group/portfolio risk.

**Kelly Criterion** (bounds Models 5/8). Kelly % = W − [(1 − W) ÷ R], where W = win rate (decimal), R = avg win ÷ avg loss. Example: W=0.5, R=2.0 → 0.5 − 0.25 = 25%. Trade ~80% of raw Kelly, divided by expected simultaneous positions (e.g., 80%×25%=20%, ÷10 positions ≈ 2%/position).

**"Market's money" overlay.** Risk a small fixed % (e.g., 1%) of starting equity plus a larger, near-Kelly % (e.g., 4%) of accumulated open profits, so risk capacity grows with unrealized gains while principal stays protected; optionally cut the base % further for every additional 5% drawdown below starting equity.

## Risk

Every model bounds only the sizing decision, not the outcome — a stop can gap through its price, and even a well-chosen risk level (25% in Tharp's reference system) can carry an 84% drawdown despite the best long-run reward/risk ratio in the sample. Models 1-3 ignore actual instrument volatility and can silently concentrate risk in whatever is most volatile. Group control (7) and netting (9) depend on correlation assumptions that break down precisely during broad market shocks, when "independent" positions often move together anyway.

## Caveats

The backtest tables (Models 1, 4, 5) all use one reference system (55/21-day breakout, 10 commodities, 1981-91, $1M start), so specific breakpoints are properties of that system, not universal constants. Optimal-f (Ralph Vince's method) is only briefly critiqued here, not fully specified, since Tharp recommends Kelly instead. Dollar figures reflect mid-1990s markets and need rescaling.
