---
title: "Guidelines on Market Risk, Volume 3: Evaluation of Value-at-Risk Models"
author: Oesterreichische Nationalbank
year: 1999
slug: evaluation-of-value-at-risk-models
tier: B
category: Quant, Microstructure & Academic Research
tags: [value-at-risk, backtesting, risk-management, regulation, basel, model-validation, bank-risk]
difficulty: advanced
doc_type: manual
pages: 58
one_liner: "Austrian central bank regulatory guideline specifying how bank-internal VaR models must be built, validated, and backtested for market-risk capital approval."
related: [fallon-w-calculating-value-at-risk, exploring-value-at-risk, hedge-fund-risk-factors-and-value-at-risk-of-credit-trading-strategies, credit-risk-modeling-and-valuation-an-introduction]
source_file: "Evaluation Of Value At Risk-Models.pdf"
---

## Summary

A regulatory guideline published by the Oesterreichische Nationalbank (Austrian central bank) as part of a six-volume series on market risk, written to help Austrian credit institutions and supervisors implement the internal-models approach for market-risk capital requirements following the 1998 Austrian Banking Act amendment (aligned with the Basel Committee's 1996 Amendment to the Capital Accord). It is not a trading strategy document but a compliance manual: it defines what a bank's internal Value-at-Risk (VaR) model must contain, how it must be validated through backtesting, and how results are reported to the supervisor. Core statutory parameters: a 10-business-day holding period, a one-sided 99% confidence level, and at least one year of historical data for the underlying model, with backtesting performed daily against a rolling 250-day window.

## Key points

- Internal VaR models must use a 10-day holding period; a 1-day VaR can be scaled to 10 days by multiplying by the square root of 10, if statistically justified.
- The statutory confidence level for capital-requirement purposes is 99% (one-sided).
- Backtesting compares daily VaR forecasts against actual (or "hypothetical," i.e., static-portfolio) trading outcomes; the regulator prefers the hypothetical P&L series because it isolates model accuracy from intraday trading activity.
- An "exception" is recorded whenever the realized loss exceeds the VaR estimate for that day; the frequency of exceptions over a 250-day window drives the "traffic light" classification (implied green/yellow/red zones) that determines whether the model's regulatory approval is upheld or a capital multiplier penalty applies.
- Backtesting must be performed daily by an independent risk-control function, separate from position-taking.
- Institutions must also backtest at the subportfolio level where feasible, since aggregation across desks structurally raises the confidence level above 99% for the total book, masking desk-level model weaknesses.
- Credit institutions must submit a full system description of their model to the OeNB every three years, plus regular and ad hoc backtesting and stress-testing reports.
- Serial correlation in backtesting exceptions (clustering of breaches) is flagged as a specific weakness the analysis must check for, since independent daily exceptions are the implicit assumption behind the exception-count test.

## Actionable rules

1. Set VaR holding period to 10 trading days for regulatory capital calculations; use the square-root-of-10 scaling from a 1-day VaR only when justified.
2. Use a 99% one-sided confidence level for the VaR estimate.
3. Maintain at least one year of historical data to calibrate the model.
4. Run backtesting daily over a rolling 250-trading-day window and count exceptions (days where actual loss exceeds VaR).
5. Investigate and correct the model if the exception count over 250 days indicates the VaR is systematically too low (too many breaches) per the traffic-light approach.
6. Keep backtesting and model validation organizationally separate from the trading/position-taking function.

## Caveats

This is a compliance/regulatory text specific to the Austrian implementation of the Basel market-risk framework as it stood in the late 1990s; the specific traffic-light thresholds and multiplication factors are referenced but not fully reproduced in the excerpted material, and later Basel II/III revisions (e.g., stressed VaR, expected shortfall under Basel III/FRTB) superseded parts of this framework. It is written for bank risk-control departments and supervisors, not for individual traders, and offers no trading signals or entry/exit rules.

## Who it is for

Risk managers, quants, and compliance staff at institutions running internal VaR models for regulatory capital, or traders wanting to understand how banks validate and are penalized on model accuracy.
