# Arbitrage Pricing Theory: the trader's summary

*A factor-model primer derives expected returns as a linear function of systematic exposures and factor risk premia.*

**D. N. Tambakis** · Quant, Microstructure & Academic Research · advanced

*Source coverage: full. PDF pages inspected: 1-11. These are study notes, not verified trading results.*

## Summary

The article explains Arbitrage Pricing Theory (APT) as a multi-factor model. Asset return is written as an intercept plus factor loadings times common factors and an idiosyncratic error; with sufficiently diversified portfolios, unsystematic risk averages out (pp. 3-5). No-arbitrage equilibrium then implies expected return is a linear combination of factor loadings and factor risk premia. Factors may be macroeconomic variables, firm characteristics, or portfolio returns, while selecting them remains a judgmental empirical task (pp. 4, 7-8). The article describes a two-stage estimation procedure: time-series regressions estimate betas, then cross-sectional regressions estimate risk premia (pp. 8-10).

## Key points

- Only systematic exposure is priced in the idealized diversified equilibrium (pp. 3-5).
- Short selling and access to proceeds are important assumptions for the arbitrage portfolio (p. 3).
- Relevant factors can include interest rates, inflation, production, size, and sector or market returns (pp. 4, 7-8).
- Adding factors raises fit but can create estimation and error-covariance problems (p. 10).
- APT risk premia need not have the simple positive interpretation of CAPM market beta (p. 10).

## Actionable rules

1. Define candidate systematic factors and estimate each asset’s loading with a time-series regression (pp. 7-9).
2. Estimate factor premia in a cross-sectional regression only after accounting for beta-estimation uncertainty (pp. 8-10).
3. Test whether residual covariance is small enough for diversification to reduce idiosyncratic risk (pp. 3, 9-10).

## Caveats

APT does not identify a unique factor set automatically. Factor selection, short-sale access, homogeneous expectations, and stable relationships are strong assumptions. This article gives a framework for expected returns, not a standalone trading signal.

## Who it is for

Quantitative investors and students building multi-factor valuation or portfolio models.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: arbitrage-pricing, factor-models, risk-premia, portfolio-theory
