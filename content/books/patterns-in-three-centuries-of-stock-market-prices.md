---
title: Patterns in Three Centuries of Stock Market Prices
author: William N. Goetzmann
year: 1993
slug: patterns-in-three-centuries-of-stock-market-prices
tier: B
category: Quant, Microstructure & Academic Research
tags: [market-history, mean-reversion, long-horizon, bootstrapping, stock-returns]
difficulty: advanced
doc_type: paper
pages: 23
one_liner: Three centuries of London and New York prices suggest horizon-dependent persistence and reversion, but not a demonstrated trading edge.
related: []
source_file: "Patterns In Three Centuries Of Stock Market Prices.pdf"
source_review: full
reviewed_pdf_pages: "1-23"
---

## Summary

Goetzmann tests long-horizon dependence in annual capital-appreciation series for London from 1700–1989 and New York from 1790–1989. He applies nonoverlapping 1–10-year autoregressions and rescaled-range statistics, using ordinary and variance-stratified bootstraps. Raw London returns show long-horizon persistence; deviations from rolling 20-year means show shorter-horizon reversion in both markets (PDF pp. 10–21). Results depend on the statistic and specification, and the paper does not establish a profitable trading strategy.

## Key points

- The London series contains 290 years with 2.1% geometric annual capital appreciation and 15.7% annual standard deviation. New York has 197 years, 3.9% appreciation, and 18.4% standard deviation (PDF p. 10).
- Both indices splice historical sources. Survivorship, infrequent trading, price averaging, changing breadth, missing dividends, and structural economic change can bias means, variances, and dependence estimates (PDF pp. 4–8).
- For raw London returns, horizons beyond five years appear persistent, but only the eight-year coefficient exceeds the 95th percentile under the variance-stratified bootstrap (PDF p. 15).
- After subtracting the rolling 20-year mean, London coefficients turn negative; four- through seven-year horizons are individually significant (PDF pp. 12, 15).
- New York coefficients are negative across horizons, yet the joint autoregression test does not reject temporal independence at conventional levels (PDF pp. 20–21).
- Joint rescaled-range tests for demeaned London and New York reject independence at 95%, combining low two- to four-year statistics with high eight-year statistics (PDF pp. 20–21).
- The evidence cannot distinguish changing expected returns, dividend policy, index composition, or speculative bubbles (PDF pp. 21–22).

## Actionable rules

1. Test a horizon family jointly; do not select a single significant lag after examining many horizons (PDF pp. 14–15, 20–21).
2. Preserve changing variance when resampling long historical series; the paper compares i.i.d. and variance-stratified bootstraps (PDF pp. 11–15).
3. State whether “mean reversion” refers to raw returns or deviations from a specified rolling mean, because they produce different conclusions (PDF pp. 12, 15, 21).
4. Before treating the pattern as tradable, test total investor returns, trading rules, and costs; capital appreciation alone is insufficient (PDF p. 22).

## Caveats

Longer history increases sample size while adding nonstationarity and measurement problems. Individual-horizon results are stronger than several joint tests. The author says an efficiency test would require total returns and perhaps a horizon longer than one lifespan (PDF p. 22).

## Who it is for

Researchers evaluating long-run dependence, historical indices, and mean-reversion claims.
