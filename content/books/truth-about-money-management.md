---
title: "The Truth About Money Management"
author: "Murray A. Ruggiero Jr."
year: 2004
slug: truth-about-money-management
tier: B
category: Money Management & Position Sizing
tags: [money-management, position-sizing, optimal-f, kelly-criterion, drawdown, fund-management]
difficulty: intermediate
doc_type: article
pages: 4
one_liner: "Futures Magazine article contrasting individual-trader vs. fund-manager money management goals and walking through percent-risk, percent-volatility, and optimal f position-sizing formulas."
related: [mathematicsmoneymanagement, money-management-report-van-tharp, money-management-risk-control-for-traders]
source_file: "truth_about_money_management.pdf"
---

## Summary

A magazine article arguing that individual traders and professional fund managers should NOT use the same money management approach, because their goals differ: individual traders want to maximize absolute profit while surviving, while fund managers must deliver a superior risk-adjusted (Sharpe Ratio) return to retain client capital. The article then reviews the main quantitative position-sizing frameworks — percent-risked, percent-volatility, and the Kelly/optimal f family — and their practical limitations.

## Key points

- Individual traders can and often should target much larger drawdowns (40-60%, per interviewed trader Sheldon Knight) than fund managers, who typically need drawdowns roughly one-third as large (e.g., ~15%) to keep client money.
- Percent-risked model: LotSize = RiskFraction × Equity / TradeRisk; reduces to the fixed-fractional model if TradeRisk is held constant.
- Percent-volatility model: LotSize = VolatilityFraction × Equity / Volatility (volatility often measured as 10-20 bar average true range).
- Optimal f (Kelly-derived): F = ((B+1)×P - 1)/B, where P = win probability and B = win/loss ratio; popularized for traders by Larry Williams.
- Ralph Vince's refinement uses Holding Period Return (HPR = 1 + f×(-T/BL)) and Terminal Wealth Relative (TWR = product of HPRs) since the Kelly formula breaks down when trade sizes vary.
- Optimal f is highly sensitive to the single largest historical losing trade and to the distribution/sequencing of wins and losses, making it dangerous to trade at or near its calculated value in live markets.
- Professional money managers typically risk just 1-3% of capital per trade (RiskFraction of 0.01-0.03), far below optimal f's often-aggressive output.
- Markets experience "five-sigma" tail events far more often than normal-distribution statistics predict, so money management plans must explicitly plan for them.

## Actionable rules

1. Define your goal first: absolute profit maximization (individual) vs. superior risk-adjusted return relative to competing investments (fund manager) — the money management math should follow from this choice.
2. Risk 1-3% of equity per trade if managing outside capital (professional norm); individual traders may accept more if they have the risk tolerance and capital to rebuild.
3. Use LotSize = RiskFraction × Equity / TradeRisk (percent-risked) or the volatility-based equivalent to scale position size as equity changes, rather than trading a fixed number of contracts.
4. Do not trade at calculated optimal f — it assumes a stable win/loss distribution and rounds awkwardly to whole contracts; treat it as a theoretical ceiling, not a target.
5. Plan explicitly for a five-sigma event (define what you can withstand) as part of the money management plan, since such events occur more often than normal statistics suggest.
6. Set a pre-defined drawdown level (e.g., 40-60% for an aggressive individual account, ~15% for a managed account) at which you stop trading and reevaluate the system.

## Caveats

Written for a general futures-trading audience in a 2004 magazine format; the optimal f / Kelly discussion is a condensed summary rather than a full derivation, and no backtested performance data or specific market examples are given beyond the illustrative arithmetic. Some figures (e.g., historical trader anecdotes) are presented as unverified interview claims.

## Who it is for

Traders and aspiring fund managers who want a quick conceptual overview of position-sizing frameworks (percent-risk, percent-volatility, optimal f) and how professional vs. individual money management goals diverge.
