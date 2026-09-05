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

A regulatory guideline from the Oesterreichische Nationalbank (Austrian central bank), part of a six-volume series on market risk, helping Austrian banks and supervisors implement the internal-models approach for market-risk capital after the 1998 Banking Act amendment (aligned with Basel's 1996 Capital Accord Amendment). It is a compliance manual, not a strategy document: it defines what a bank's internal Value-at-Risk (VaR) model must contain, how it is validated through backtesting, and how results are reported. Core statutory parameters: a 10-business-day holding period, a one-sided 99% confidence level, at least one year of historical data, and daily backtesting against a rolling 250-day window.

## Key points

- VaR models must use a 10-day holding period; a 1-day VaR can be scaled up by multiplying by the square root of 10, if justified.
- Statutory confidence level for capital purposes is 99% (one-sided).
- Backtesting compares daily VaR forecasts against actual or "hypothetical" (static-portfolio) outcomes; regulators prefer the hypothetical series to isolate model accuracy from intraday trading.
- An "exception" is recorded when realized loss exceeds VaR for the day; exception frequency over 250 days drives a traffic-light classification determining whether approval holds or a capital penalty applies.
- Backtesting must run daily, performed by an independent risk-control function separate from position-taking.
- Institutions must also backtest at the subportfolio level, since aggregation across desks structurally raises the confidence level above 99% for the total book, masking desk-level weaknesses.
- Institutions submit a full model description to the OeNB every three years, plus regular and ad hoc backtesting/stress-testing reports.
- Serial correlation in exceptions (clustering of breaches) is flagged as a weakness to check, since independence is the implicit assumption behind the exception-count test.

## Actionable rules

1. Set VaR holding period to 10 trading days; scale from 1-day VaR by square root of 10 only when justified.
2. Use a 99% one-sided confidence level.
3. Maintain at least one year of historical data to calibrate the model.
4. Backtest daily over a rolling 250-day window and count exceptions.
5. Investigate and correct the model if exceptions indicate VaR is systematically too low per the traffic-light approach.
6. Keep backtesting organizationally separate from trading.

## Caveats

Specific to the Austrian implementation of the Basel market-risk framework as it stood in the late 1990s; exact traffic-light thresholds are referenced but not fully reproduced here, and later Basel II/III revisions superseded parts of this framework. Written for bank risk-control staff, not traders; no entry/exit signals.

## Who it is for

Risk managers and compliance staff running internal VaR models for regulatory capital, or traders wanting to understand how banks validate and are penalized on model accuracy.
