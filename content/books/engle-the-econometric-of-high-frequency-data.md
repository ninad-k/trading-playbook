---
title: "The Econometrics of Ultra-High Frequency Data"
author: "Robert F. Engle"
year: 1996
slug: engle-the-econometric-of-high-frequency-data
tier: B
category: Quant, Microstructure & Academic Research
tags: [high-frequency-data, acd, transaction-duration, volatility]
difficulty: advanced
doc_type: paper
pages: 19
one_liner: "Engle models irregular transaction arrivals with conditional durations and links IBM trade timing to instantaneous quote volatility."
related: [madhavan-market-microstructure-a-survey, mcmillan-and-speight-nonlinear-dynamics-in-high-frequency-intra-day-financial-data]
source_file: "Engle-The Econometric Of High-Frequency Data.pdf"
source_review: full
reviewed_pdf_pages: "1-19"
---
## Summary

Engle defines ultra-high-frequency data as complete transaction records whose observations arrive at random times. Rather than forcing them into fixed calendar intervals, he represents each event by its duration since the previous trade and by “marks” such as price, volume, bid, and ask (pp. 3-6). This framework supports questions about the next event’s arrival rate, its marks, and the interaction between transaction intensity and volatility.

The paper develops a semiparametric hazard estimator around Engle and Russell’s Autoregressive Conditional Duration (ACD) model, then applies it to 15,000 IBM trades. Intraday seasonality is removed before estimating an ACD(1,1). The fitted duration coefficients are .056 and .933, and the standardized durations show little residual serial dependence: the 15-lag Ljung-Box statistic falls from 1,209 for adjusted durations to 17.7 after standardization (pp. 10-11).

Engle next combines ACD timing with a GARCH-style model for midquote returns. Longer trade durations are associated with lower instantaneous volatility, consistent with the Easley-O’Hara “no trade means no news” model rather than the Diamond-Verrecchia “no trade means bad news” prediction. Expected duration has a nonlinear forecasting relation: both very long and very short expected durations imply lower volatility in this sample (pp. 12-17).

## Key points

- Aggregating to fixed intervals discards information and complicates very short-interval analysis (p. 3).
- Duration and marks can be modeled jointly, or separately under stated exogeneity conditions (pp. 4-8).
- The ACD model captures persistent clustering in IBM intertrade durations (pp. 10-11).
- Calendar-time volatility fits slightly better than a plain transaction-time GARCH model, although the difference is small (pp. 16-17).
- Results concern quote volatility conditional on timing, not a directional trading signal.

## Actionable rules

1. Preserve event timestamps and model intertrade durations directly when timing may contain information (pp. 3-6).
2. Remove deterministic time-of-day duration patterns before estimating persistence, as in the IBM application (p. 10).
3. Diagnose standardized durations and volatility residuals for remaining serial dependence before interpreting coefficients (pp. 11, 15-16).

## Caveats

The empirical application uses one 15,000-trade IBM sample and preliminary model specifications. Some duration effects weaken with robust standard errors, and quote discreteness leaves residual mean dependence. The paper does not test returns after costs.

## Who it is for

Market-microstructure researchers and quantitative analysts modeling irregular trades, transaction intensity, and intraday volatility.
