---
title: Automated Trading
author: Scott Owens
year: 2005
slug: coreconcepts-automatedtrading
tier: B
category: Trend Following & Mechanical Systems
tags: [automated-trading, forex, backtesting, execution, systems]
difficulty: intermediate
doc_type: article
pages: 5
one_liner: FX Engines outlines signals, systems, testing, and live execution as the four components of automation.
related: []
source_file: "coreconcepts_automatedtrading.pdf"
source_review: full
reviewed_pdf_pages: "1-5"
---
## Summary

Owens argues that automation can impose consistency on a 24-hour FX market, but only after substantial system-building work. He identifies four components: signals that trigger entry and exit, systems that combine signals with trade management, historical test trading using tick data, and live trading through a dealer (p. 3). The proposed workflow is to use the same tools in testing and live deployment so that execution behavior is comparable. Automation is presented as a way to reduce fatigue, emotional decisions, leverage misuse, and post-loss impulsiveness, while the source also states that the system must be followed exactly once built (pp. 1–3). Platform-selection questions include whether it is hosted or dependent on a home computer, tick-driven, connected to credible dealers, customizable without heavy programming, and transparent about upfront fees (p. 4). The report recommends testing both historical and forward-looking behavior before promotion to live trading (p. 3). It is written by a platform vendor and repeatedly points readers toward FX Engines, so its claims about the need for automation and ideal platforms are marketing arguments rather than comparative evidence (pp. 1, 4–5).

## Key points

- A complete automated workflow spans signal definition, system logic, backtest, forward test, and live execution (p. 3).
- Tick-level data and matching test/live tools matter when slippage and intrabar order are material.
- Hosting, broker dependency, outages, and customization are operational risks alongside strategy risk (p. 4).

## Actionable rules

1. Define signals and combine them into entry, management, and exit logic before testing the complete system (p. 3).
2. Test first on historical tick data and then on a forward-looking live price feed before promotion to live execution (p. 3).
3. Compare candidate platforms for hosting redundancy, tick-driven operation, dealer relationships, customization, and upfront fees (p. 4). These are vendor criteria, not evidence that automation will be profitable.

## Caveats

The brief supplies no independent performance results and is promotional. Automation can execute a bad or overfit strategy faster; “exact” test-to-live equivalence is not guaranteed by a platform’s feature list.

## Who it is for

Traders evaluating the research and operational requirements of FX automation.
