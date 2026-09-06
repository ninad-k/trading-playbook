---
title: "The Predictive Power of Stock Market Indicators"
author: "Ben Branch"
year: 1976
slug: ben-branch-the-predictive-power-of-stock-market-indicator
tier: B
category: Quant, Microstructure & Academic Research
tags: [market-indicators, forecasting, regression, investor-sentiment]
difficulty: advanced
doc_type: paper
pages: 18
one_liner: "Branch tests ten sentiment, informed-opinion, liquidity, and monetary indicators against future S&P 500 changes from 1960 through 1974."
related: [position-sizing, cot]
source_file: "Ben Branch - The Predictive Power Of Stock Market Indicator.pdf"
source_review: full
reviewed_pdf_pages: "1-18"
---
## Summary

Branch tests whether several broad-market indicators jointly forecast subsequent S&P 500 percentage changes over one, three, six, nine, and twelve months. The ten variables cover odd-lot and floor-trader short selling, the market P/E ratio, Barron’s confidence index, specialist short sales, secondary distributions, mutual-fund cash, the Treasury-bill rate, money-supply growth, and inflation (pp. 3-10). The main 1960-1974 regressions find the mutual-fund cash position and Treasury-bill rate most consistently useful. Several other variables work in some horizons, while money-supply growth does not (pp. 10-13, 18).

A split-period exercise estimates coefficients on 1960-1967 and compares predictions with 1968-1974 outcomes. Predicted and actual changes correlate from .278 at one month to .577 at three months, with reported significance at 1% or better (pp. 15-17). Branch still warns that this does not show an indicator trading rule can beat buy-and-hold after transaction costs (p. 17).

## Key points

- Joint regressions explain more variation than any single indicator in the full sample (p. 13).
- Forecast fit is modest at one month and generally stronger at longer horizons (p. 13).
- Mutual-fund cash and the bill rate are the only variables described as consistent across adjustment periods and subsamples (pp. 15-18).
- Several relationships change between 1960-1967 and 1968-1974, highlighting instability (pp. 15-16).
- Longer-horizon regressions have strongly autocorrelated errors because forecast windows overlap (p. 13).

## Actionable rules

1. Do not convert a significant coefficient directly into a trading signal; first specify the rule and compare it with buy-and-hold after costs (p. 17).
2. Validate indicator models in a later period rather than judging only in-sample fit, as the paper does with its 1960-1967/1968-1974 split (pp. 15-17).
3. Prefer stable relationships across horizons and subsamples, and reject improvements obtained by repeatedly changing lags or functional forms without fresh validation (p. 18).

## Caveats

The data end in 1974 and several indicators depend on historical market institutions. Overlapping returns complicate inference, coefficient stability is mixed, and the study does not implement an investable strategy.

## Who it is for

Researchers evaluating market-timing indicators, regression stability, and the gap between predictability and tradable performance.
