---
author: Joao Amaro de Matos, Marcelo Fernandes
category: Quant, Microstructure & Academic Research
difficulty: advanced
doc_type: paper
one_liner: Academic paper developing a nonparametric test for whether bid-ask spreads
  follow a Markov process, rejecting the assumption for 3 of 5 NYSE stocks tested.
pages: 24
related:
- hamao-and-hasbrouck-securities-trading-in-the-absence-of-dealers-trades-and-quotes-on-the
- madhavan-market-microstructure-a-survey
reviewed_pdf_pages: the methodology and results sections checked against the note;
  the paper reports test statistics rather than trading parameters
slug: de-matos-and-fernandes-testing-the-markov-property-with-ultra-high-frequency-financial-dat
source_file: De Matos And Fernandes-Testing The Markov Property With Ultra-High Frequency
  Financial Data.pdf
source_review: partial
tags:
- market-microstructure
- bid-ask-spread
- markov-process
- nonparametric-testing
- academic
- nyse
- ultra-high-frequency
tier: B
title: Testing the Markov Property with Ultra-High Frequency Financial Data
year: 2001
---

## Summary

Question: many financial-economics models assume asset prices or spreads follow a Markov process (future behavior depends only on the current state, not the full history) — but is this testable, and does it hold for real transaction data? Prior tests required evenly time-spaced observations, unsuited to trade-by-trade data. Data: bid and ask price series for five actively traded NYSE stocks — Boeing, Coca-Cola, Disney, Exxon, IBM. Method: the authors model price as a continuous-time Markov process observed only when it crosses a discrete level (a "subordinated" Markov process), naturally handling irregular spacing and tick discreteness, and build a nonparametric test of the resulting conditional-independence property. Finding: raw bid/ask prices are nonstationary, so the test is applied to bid-ask spreads instead; the Markov assumption is not rejected for Disney and Exxon but is rejected for Boeing, Coca-Cola, and IBM.

## Key points

- Only two prior nonparametric Markov tests existed, both requiring evenly spaced data — unsuitable for irregularly spaced transaction records.
- The test exploits "subordination": prices observed only on moves of at least a fixed tick, making consecutive price durations conditionally independent under the Markov null.
- Raw bid/ask price levels for all five stocks appear nonstationary, so the spread (ask minus bid) is the stationary series actually tested.
- Results are mixed: Markov not rejected for Disney and Exxon spreads, rejected for Boeing, Coca-Cola, and IBM.
- Non-Markovian spread behavior is linked to asymmetric-information microstructure theory: high adverse-selection costs make the spread depend on full trading history, breaking the Markov property.
- Asymptotic normality of the test statistic is formally derived under both the null and local alternatives, making this a methodological as well as empirical contribution.

## Actionable rules

None given — a pure econometric methodology paper, not a strategy source. Practical implication: a Markov (memoryless) assumption for bid-ask spread dynamics is not safe by default — it failed for 3 of 5 stocks here — meaning spread history may carry predictive information beyond the current level.

## Caveats

Highly technical (nonparametric kernel testing, mixing conditions, asymptotic theory), requiring econometrics background. Sample of five large-cap NYSE names from a pre-decimalization, pre-HFT era; results may not generalize to modern tick regimes.

## Who it is for

Quantitative researchers interested in bid-ask spread statistics and nonparametric time-series testing, not discretionary or retail traders.
