---
title: "Hedge Fund Risk Factors and Value at Risk of Credit Trading Strategies"
author: "John Okunev, Derek White"
year: 2003
slug: hedge-fund-risk-factors-and-value-at-risk-of-credit-trading-strategies
tier: B
category: "Quant, Microstructure & Academic Research"
tags: [hedge-funds, value-at-risk, credit-trading, return-smoothing, autocorrelation, risk-factors, fixed-income, academic-research]
difficulty: advanced
doc_type: paper
pages: 63
one_liner: "Academic paper finding fixed-income hedge fund returns understate true risk by 60-100% due to smoothing, and that a short put on high-yield debt is the dominant risk factor across most strategies."
related: [armelle-guizot-the-hedge-fund-compliance-and-risk-management-guide, s-a-mccrary-hedge-fund-course, hedges-on-hedge-funds-how-to-successfully-analyze-2005]
source_file: "Hedge Fund Risk Factors and Value at Risk of Credit Trading Strategies.pdf"
---

## Summary

This 2003 working paper asks how risky fixed-income hedge fund strategies really are once reported returns are corrected for artificial smoothing. Using monthly index returns (1994-2001) for 21 hedge fund indices across six fixed-income styles (Convertible Arbitrage, Fixed Income Arbitrage, Credit Trading, Distressed Securities, Merger Arbitrage, MultiProcess-Event Driven) from FRM, HFR, CSFB, Hennessee, and Zurich, the authors develop a method to strip serial autocorrelation from returns (autocorrelation being evidence of smoothing from stale/illiquid pricing), then use stepwise regression against 100+ candidate risk factors to find each style's true risk drivers, and finally run Monte Carlo value-at-risk simulations comparing linear versus linear-plus-nonlinear factor mappings. Key finding: after unsmoothing, true risk for many styles is 60-100% higher than reported, and a short put position on high-yield debt (UBS Warburg sub-BBB/NR index) is the single most important risk factor for 17 of 21 indices — including Merger Arbitrage, where it beats the short-put-on-equities factor proposed by earlier research (Mitchell and Pulvino 2001).

## Key points

- Reported returns show significant positive autocorrelation, most severe for Convertible Arbitrage and Fixed Income Arbitrage — a signature of return smoothing from stale/illiquid pricing.
- After removing autocorrelation, true estimated standard deviation of returns rises 60-100% for many indices versus as-reported figures.
- Correlations across styles are high, especially Credit Trading with Distressed Securities, and Merger Arbitrage with MultiProcess-Event Driven.
- A short put on high-yield debt is the dominant risk factor for the majority of indices tested (top factor in 17 of 21).
- Small-cap stock exposure is a secondary factor for Distressed Securities, Merger Arbitrage, and MultiProcess-Event Driven, often displaced once the high-yield short-put factor is included.
- Nonlinear (option-like) factors give only moderate improvement in explanatory power, and none for Fixed Income Arbitrage or Credit Trading; several styles show negative exposure to volatility changes.
- Nonlinear factors increase estimated downside VaR only marginally across all styles.
- Merger Arbitrage was the safest, best-performing style in the sample, consistent with its low observed autocorrelation.
- VaR estimates varied substantially across index providers within the same style (e.g., Convertible Arbitrage VaR from CSFB ran 2-4x higher than from FRM) despite consistent risk-factor exposures.

## Actionable rules

None given as trade-execution rules (this is risk research, not a trading system). Practical takeaways: (1) don't trust reported hedge fund volatility at face value for illiquid fixed-income strategies — true risk runs meaningfully higher; (2) when assessing credit strategies including merger arbitrage, high-yield credit downside (a short put on high-yield debt) is a better risk proxy than equity beta or small-cap exposure; (3) cross-check any one index provider's stated VaR for a style against other providers, since estimates can differ 2-4x by methodology.

## Caveats

Highly technical academic paper aimed at researchers, not practitioners; the "unsmoothing" mathematics is not something a discretionary trader would apply directly. Sample period is 1994-2001 using index-level (not individual fund) returns; results are specific to that era's fixed-income hedge fund strategies. Statistical tables referenced throughout are not reproduced here.

## Who it is for

Quant researchers, risk managers, or allocators evaluating fixed-income and credit-strategy hedge funds who need to understand why reported hedge fund volatility understates true risk and what factor exposures actually drive that risk.
