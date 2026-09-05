---
title: "Exploring the Limitations of Value at Risk: How Good Is It in Practice?"
author: Andreas Krause
year: 2003
slug: exploring-value-at-risk
tier: B
category: "Quant, Microstructure & Academic Research"
tags: [value-at-risk, risk-management, statistics, coherent-risk-measures, derivatives, academic-paper]
difficulty: advanced
doc_type: paper
pages: 10
one_liner: "Journal of Risk Finance article showing Value at Risk is not a coherent risk measure, is prone to large estimation error and downward bias, and can be deliberately manipulated by traders."
related: [fallon-w-calculating-value-at-risk, evaluation-of-value-at-risk-models, hedge-fund-risk-factors-and-value-at-risk-of-credit-trading-strategies]
source_file: "Exploring_Value_at_Risk.pdf"
---

## Summary

Question: is Value at Risk (VaR) — the dominant risk-measurement standard adopted after the derivatives blowups of the early 1990s (Orange County, Metallgesellschaft, Barings, Daiwa) — actually a reliable measure of risk in practice? Method: theoretical/statistical analysis of VaR's mathematical properties (coherence, subadditivity) plus worked numerical examples using Nasdaq Composite daily returns (March 1999–March 2001) and Bienaymé-Chebyshev/Kendall estimation-error formulas. Finding: VaR is not a coherent risk measure — it can rank a more diversified, genuinely safer portfolio as riskier than a concentrated one, and it ignores the size of losses beyond the cutoff. VaR estimates also carry large statistical estimation error, a downward bias when the number of assets approaches the number of historical observations, and can be deliberately manipulated (e.g., with options) to look safer than the position actually is, while systemic use of VaR-based rules can itself amplify market crashes.

## Key points

- VaR is defined as the loss level not exceeded with a given confidence (e.g., "99% confidence that losses will not exceed $13m") over a specified time horizon; estimated either non-parametrically (from historical return quantiles) or parametrically (assuming a distribution, usually normal).
- Under Basel-style banking regulation, the standard VaR horizon is 10 working days, and annual return/volatility figures must be rescaled to that horizon.
- VaR is only a coherent risk measure (correctly ranking riskier positions as riskier) when returns follow an elliptical distribution (e.g., normal); it fails for skewed or fat-tailed payoffs, including most options and other derivatives.
- Worked example: two investments with identical 95% VaR can have very different actual tail risk if the loss distributions diverge only beyond the VaR cutoff — VaR treats them as equally risky when one is clearly worse.
- Worked example: 100 units of one risky asset show VaR of –500, while a diversified 1-asset-each portfolio of the same 100 independent assets shows VaR of +200 — VaR wrongly flags the diversified portfolio as riskier, violating subadditivity.
- Estimation error in the tail quantile is large because tail observations are, by definition, rare; the paper gives closed-form standard-error formulas (non-parametric vs. normal-distribution-assumed) and shows error grows sharply as the confidence level rises.
- When the number of traded instruments approaches the number of historical data points used to estimate the correlation matrix, VaR estimates show a substantial downward bias — the true VaR can be roughly double the estimated VaR under realistic conditions.
- Because VaR is not coherent, traders can manipulate it without reducing true risk — e.g., writing calls at the old VaR cutoff and buying puts at the new lower cutoff shifts the reported VaR down while increasing downside risk and lowering expected return.
- Widespread reliance on VaR-based rules can create systemic risk: when many participants react identically to a VaR breach (selling to cut reported risk), the resulting synchronized selling can itself cause or worsen a crash, echoing the 1987 portfolio-insurance-driven crash dynamic.

## Actionable rules

None given as a trading system — this is a critique of a risk-measurement methodology. What a risk-conscious trader/allocator can take from it: (1) never treat a single VaR number as a complete risk picture, especially for options or other skewed payoffs; (2) complement VaR with stress testing for tail/crash scenarios not present in the historical estimation window; (3) be skeptical of reported VaR from any desk or fund trading many correlated instruments relative to its data history, since the estimate is likely biased low; (4) recognize that VaR-based position limits can be gamed (e.g., via options overlays) without a real reduction in risk.

## Caveats

Technical/mathematical paper (density functions, quantile estimation, Bienaymé-Chebyshev inequality) aimed at risk-management practitioners and academics, not retail traders. Uses a 2003 dataset (Nasdaq 1999–2001) and pre-Basel-II/III regulatory framing; VaR practice and regulation have evolved since (e.g., wider adoption of Expected Shortfall/CVaR specifically to address the non-coherence problem this paper identifies). No entry/exit or position-sizing rules are given.

## Who it is for

Risk managers, quants, and serious allocators who rely on or report VaR and want to understand its mathematical blind spots — not a fit for readers looking for a trading strategy.
