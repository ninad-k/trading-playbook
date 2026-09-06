---
author: Antonis A. Demos, Charles A. E. Goodhart
category: Quant, Microstructure & Academic Research
difficulty: advanced
doc_type: paper
one_liner: Half-hourly Reuters FX quote data shows volatility, spread, and quote frequency
  are simultaneously determined, with time-of-day dummies removing much of the GARCH-type
  clustering in returns.
pages: 10
related:
- supply-demand
- foucault-kadan-and-kandel-limit-order-book-as-a-market-for-liquidity
- liquidity-in-forex-markets
reviewed_pdf_pages: 1-3, 5 (the data description and the intraday estimation results)
slug: the-interaction-between-the-frequency-of-market-quotes-spread-and-volatility-in-forex
source_file: The Interaction Between The Frequency Of Market Quotes Spread And Volatility
  In Forex.pdf
source_review: partial
tags:
- forex
- volatility
- bid-ask-spread
- quote-frequency
- market-microstructure
- academic-paper
tier: B
title: The Interaction Between the Frequency of Market Quotations, Spread and Volatility
  in the Foreign Exchange Market
year: 1996
---

## Summary

Question: how do quote frequency (a proxy for market activity, since no volume data exists in interbank FX), bid-ask spread, and volatility interact in the FX spot market, and do these interactions explain the well-known heteroskedasticity (volatility clustering) in FX returns? Data: half-hourly Reuters screen quote data for DEM/USD and JPY/USD across 5 weeks (avoiding holiday weeks). Method: a simultaneous equation system (two-stage least squares) relating volatility, average spread, and number of quotations, with the best functional form for each variable found via a Box-Cox transformation search, plus weekly, daily, and half-hourly dummies to separate public-news effects from private-information effects. Finding: quote frequency is a good proxy for market activity and, with the time-of-day dummies, explains a large share of the conditional heteroskedasticity in FX returns; volatility and spread are simultaneously determined and positively related; and quote frequency affects spread only indirectly, through volatility.

## Key points

- No transaction-volume data exists for the interbank FX spot market, so the paper uses Reuters quote-arrival frequency as the activity proxy.
- A log-linear (not linear) relationship among volatility, spread, and quote frequency fits the data much better, though the true best-fitting form is somewhere between the two (found via Box-Cox search).
- Volatility is unusually high during the late-afternoon London/New York overlap despite declining quote activity in that window — a pattern the authors could not fully explain with public-news theories.
- Volatility drops sharply during the Tokyo lunch break (4:00-5:00 BST), accompanied by wider spreads and fewer quotes.
- Quoting activity peaks just after the Tokyo lunch break and again around 5:30-6:00 BST; it is lowest during the Tokyo lunch hour.
- Average spread is significantly higher on Fridays and lowest mid-week — the inverse of the quote-frequency pattern.
- Adding quote frequency and time-of-day dummies removes a large part of the GARCH/ARCH-type volatility clustering typically modeled with univariate time series, implying much of that "clustering" reflects omitted activity and time-of-day effects.

## Actionable rules

None given — this is a statistical/econometric research paper, not a trading system. Practical read for FX traders: expect volatility and spread to move together and to spike around session overlaps and post-lunch-break reopenings, and expect wider spreads heading into weekends (Friday) and around the London open, independent of any specific news release.

## Caveats

Uses early-1990s Reuters indicative-quote data (not firm/tradable quotes or actual transaction prices), and the sample is limited to 5 selected weeks. The paper's central empirical puzzle — persistently high US-afternoon volatility despite falling quote activity — is explicitly left unresolved by the authors.

## Who it is for

Quant researchers and FX microstructure specialists interested in the statistical relationship between quoting activity, spreads, and volatility, and in intraday/day-of-week FX volatility patterns.
