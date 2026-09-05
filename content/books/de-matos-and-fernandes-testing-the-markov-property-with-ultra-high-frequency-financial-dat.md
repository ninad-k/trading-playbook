---
title: Testing the Markov Property with Ultra-High Frequency Financial Data
author: "Joao Amaro de Matos, Marcelo Fernandes"
year: 2001
slug: de-matos-and-fernandes-testing-the-markov-property-with-ultra-high-frequency-financial-dat
tier: B
category: Quant, Microstructure & Academic Research
tags: [market-microstructure, bid-ask-spread, markov-process, nonparametric-testing, academic, nyse, ultra-high-frequency]
difficulty: advanced
doc_type: paper
pages: 24
one_liner: "Academic paper developing a nonparametric test for whether bid-ask spreads follow a Markov process, rejecting the assumption for 3 of 5 NYSE stocks tested."
related: [hamao-and-hasbrouck-securities-trading-in-the-absence-of-dealers-trades-and-quotes-on-the, madhavan-market-microstructure-a-survey]
source_file: "De Matos And Fernandes-Testing The Markov Property With Ultra-High Frequency Financial Data.pdf"
---

## Summary

Question: many financial-economics models assume asset prices or spreads follow a Markov process (future behavior depends only on the current state, not the full history) — but is this assumption actually testable, and does it hold for real transaction data? Prior tests (Ait-Sahalia 1997; Fernandes and Flores 1999) required evenly time-spaced observations, which real trade-by-trade data does not satisfy. Data: bid and ask price series for five actively traded NYSE stocks — Boeing, Coca-Cola, Disney, Exxon, and IBM. Method: the authors model the price as a continuous-time Markov process observed only when it crosses a discrete price level (a "subordinated" Markov process), which naturally handles irregular trade spacing and price discreteness (tick size). Under this observation rule, consecutive price durations should be conditionally independent given the current price level; they build a nonparametric test of this conditional-independence property, with asymptotic normality derived under both the null (Markov holds) and local alternatives. Finding: because raw bid/ask prices are nonstationary (integrated of order one), the test is applied to bid-ask spreads instead, which are stationary. The Markov assumption is not rejected for Disney and Exxon but is rejected for Boeing, Coca-Cola, and IBM.

## Key points

- Financial-economics theory frequently assumes Markov dynamics, but until this line of work, only two prior nonparametric tests existed, and both required evenly spaced data — unsuitable for irregularly spaced transaction records.
- The paper's test exploits "subordination": prices are observed only when they move by at least a fixed tick size, which makes consecutive price durations conditionally independent under the Markov null.
- Empirically, raw bid and ask price levels for all five stocks appear nonstationary (unit-root-like, integrated of order one), so the spread (ask minus bid) is used as the stationary series tested for the Markov property.
- Results are mixed: the Markov property is not rejected for Disney and Exxon bid-ask spreads, but is rejected for Boeing, Coca-Cola, and IBM.
- The authors link non-Markovian spread behavior to asymmetric-information market-microstructure theory (e.g., Easley and O'Hara 1992): if adverse-selection costs are high enough, the bid-ask spread should depend on the full trading history, not just the current state, breaking the Markov property.
- The test's asymptotic properties (normality under the null and under local alternatives) are formally derived, making it a methodological contribution as much as an empirical one.

## Actionable rules

None given — this is a pure econometric methodology and testing paper, not a trading strategy source. The practical implication for a trader building spread- or microstructure-based models: a Markov (memoryless) assumption for bid-ask spread dynamics is not safe to assume by default — for roughly 60% of the stocks tested here it failed, meaning spread history (not just the current spread level) may carry additional predictive information, consistent with adverse-selection/information-asymmetry effects.

## Caveats

Highly technical (nonparametric kernel-based hypothesis testing, mixing conditions, asymptotic theory) and requires econometrics background to follow the derivations; sample is limited to five large-cap NYSE names in what is now a dated microstructure/tick regime (pre-decimalization, pre-high-frequency-trading era), so results may not generalize to modern markets with different tick sizes and much higher trading frequency.

## Who it is for

Quantitative researchers and market-microstructure specialists interested in the statistical properties of bid-ask spreads and nonparametric time-series testing, not discretionary or retail traders.
