---
title: "Calculating Value-at-Risk"
author: "William Fallon"
year: 1996
slug: fallon-w-calculating-value-at-risk
tier: B
category: Quant, Microstructure & Academic Research
tags: [value-at-risk, garch, options-greeks, delta-normal, gamma-normal, risk-management, portfolio-risk]
difficulty: advanced
doc_type: paper
pages: 39
one_liner: "Wharton working paper comparing six VaR models, finding second-order (gamma) approximations paired with multivariate GARCH beat the first-order delta models used by most practitioners."
related: [kalman-filter-for-arbitrage-identification-in-high-frequency-data]
source_file: "Fallon_ W - Calculating Value-At-Risk.pdf"
---

## Summary

Question: which combination of portfolio-function approximation and state-variable model produces the most accurate Value-at-Risk (VaR)? Data: 26 years (1969–1994) of weekly equity prices (Dow Chemical, Exxon, Union Carbide, Coca-Cola, S&P 500) plus a hypothetical five-option portfolio. Method: reviews four existing VaR models (Garbade's delta-normal, J.P. Morgan's RiskMetrics, Hsieh's delta-GARCH, Wilson's gamma-normal), then introduces a new gamma-normal model and a "gamma-GARCH" model, testing all six out-of-sample over a 13.5-year holdout by counting VaR breach frequency. Finding: first-order "delta" approximations perform poorly whenever a portfolio has gamma (convexity) risk — mean absolute pricing error was roughly three times worse for delta than gamma models — and gamma-GARCH most closely matched target breach frequency among all six.

## Key points

- VaR is a one-sided confidence bound on portfolio losses over a fixed horizon.
- Every model combines two choices: portfolio approximation (delta vs. gamma) and state-variable model (unconditional normal, exponentially-weighted "RiskMetrics," or GARCH).
- Delta-only models ignore gamma, which the Black-Scholes PDE says should matter whenever options are present.
- Delta's error was consistently biased with the sign of gamma — for the (positive-gamma) options tested, delta VaR was always too conservative.
- Both methods performed poorly for deep out-of-the-money, near-expiry options, but gamma's error stayed under 0.5% MAPE there versus over 100% for delta.
- No single state-variable model was unambiguously best; GARCH was only marginally favored on an efficiency-regression (R²) test.
- Gamma-GARCH best matched actual VaR breach frequency out-of-sample in two of three confidence levels tested.
- Flags an incentive-design risk: VaR systems ignoring gamma can be "gamed" by traders taking convexity risk that doesn't register in measured VaR.

## Actionable rules

None as position-sizing rules — this is a risk-measurement methodology paper, not a trading system. Takeaways: (1) delta-only VaR materially understates risk for option portfolios with real gamma exposure; (2) GARCH-style time-varying volatility improves risk forecasts over flat historical volatility; (3) validate VaR by out-of-sample breach frequency, not in-sample fit.

## Caveats

A 1996 academic paper using data through 1994 and a hypothetical, author-chosen five-option test portfolio — illustrative of methodology, not a real-portfolio claim. The state-variable comparison is explicitly called "inconclusive" by the authors; only the delta-vs-gamma result is unambiguous. No transaction costs or liquidity risk addressed.

## Who it is for

Risk managers and derivatives traders who want to understand why naive delta-based VaR misstates risk for options portfolios, and why gamma and GARCH approaches were already demonstrably more accurate by the mid-1990s.
