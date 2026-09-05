---
title: "Modeling High-Frequency FX Data Dynamics"
author: "Oscar Jorda and Massimiliano Marcellino"
year: 2002
slug: jorda-and-marcellino-modeling-high-frequency-fx-data-dynamics
tier: B
category: "Quant, Microstructure & Academic Research"
tags: [academic-paper, market-microstructure, high-frequency-data, fx, bid-ask-spread, poisson-model, volatility, tick-data]
difficulty: advanced
doc_type: paper
pages: 32
one_liner: "Academic paper showing that non-normality and volatility clustering in FX data can be artifacts of time aggregation, and introduces a Poisson-based 'ACI' model of quote-arrival intensity and spreads."
related: [asset-pricing-with-speculative-trading, hrishikesh-d-vinod-preparing-for-the-worst]
source_file: "Jorda And Marcellino-Modeling High-Frequency Fx Data Dynamics.pdf"
---

## Summary

An academic microstructure paper on the spot FX market (question: how much of the "stylized facts" of high-frequency financial data — non-normality, leptokurtosis, conditional heteroskedasticity — is a real feature of the market versus an artifact of aggregating irregularly-arriving tick data into fixed calendar-time intervals?). Method: the authors derive analytically and confirm via Monte Carlo simulation that fixed-interval time aggregation of an irregularly-timed data-generating process can itself produce these "stylized facts" even when they are absent from the underlying process. They then propose a new autoregressive conditional intensity (ACI) model — a Poisson-regression-based approach that keeps the analysis in calendar time while modeling the random intensity of quote arrivals — and apply it to interdealer FX quote data to study whether high-activity periods carry more or less information than low-activity periods, using the bid-ask spread as a proxy for information content.

## Key points

- Time aggregation of irregularly-spaced, high-frequency data can mechanically generate non-normality, fat tails, and volatility clustering, independent of the true underlying process.
- The ACI(1,1) model conditions the Poisson intensity of quote arrivals (per half-hour interval) on its own past values and on lagged bid-ask spreads, with seasonal (time-of-day, day-of-week, holiday) terms.
- Empirically, the ACI model dramatically outperforms a simple seasonal-dummy Poisson model in fit and residual autocorrelation (Ljung-Box statistics).
- Average FX quote intensity in the sample runs around 120 quotes per half-hour in a regular business day.
- Spread dynamics show two distinct peaks as a function of quote intensity: one at very low activity (consistent with dealer inventory-rebalancing noise, per Lyons 2001) and one around 140 quotes/half-hour (consistent with an information-signal-extraction effect, per Easley & O'Hara 1992) — i.e., the relationship between activity and informativeness is non-monotonic, not simply "more activity = more/less information" in one direction.
- Autoregressive persistence of the spread varies substantially (from high persistence to negative correlation and back) as trading intensity changes.
- No evidence of ARCH effects in the model residuals once the intensity-dependent dynamics are accounted for, suggesting explicit variance modeling may be secondary once time-deformation is handled.

## Actionable rules

None given as trading rules — this is a market-microstructure econometrics paper, not a trading system. What a trader can take from it:

1. Apparent "fat tails" or volatility clustering in a fixed-interval (e.g., 1-minute, 1-hour) FX price series may partly reflect the sampling/aggregation scheme itself, not just genuine regime shifts — be cautious drawing risk conclusions from calendar-time-aggregated tick data without accounting for tick intensity.
2. Bid-ask spreads (a proxy for cost/liquidity) behave non-monotonically with trading intensity: both very quiet and moderately busy periods can carry wider or more "informative" spreads than mid-range activity, so "more volume = tighter/wider spread" is not a safe blanket assumption.
3. Time-of-day/day-of-week seasonality in quote intensity is substantial and should be filtered out before comparing spread or volatility behavior across sessions.

## Caveats

Highly technical: assumes familiarity with point processes, Poisson regression, and time-series econometrics. Uses early-2000s interdealer FX quote data (not trade data), so findings about spread/intensity dynamics may not carry over unchanged to modern electronic FX markets with different microstructure. The authors themselves caution that the informativeness result "has to be guarded due to the limitations that these data impose."

## Who it is for

Quant researchers and market-microstructure specialists studying high-frequency FX data properties; not intended for discretionary or systematic retail traders looking for signals.
