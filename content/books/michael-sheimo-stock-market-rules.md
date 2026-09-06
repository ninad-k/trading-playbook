---
author: SAS Institute Inc.
category: Quant, Microstructure & Academic Research
difficulty: advanced
doc_type: manual
one_liner: A Version 6 SAS applications manual for return measurement, valuation,
  portfolio optimization, CAPM, and options.
pages: 240
related:
- 1-the-mathematics-of-financial-derivatives
- handbook-for-investment-committee-members-how-to-make-prudent-investments-for-your-organiz
reviewed_pdf_pages: 1-18, 26, 36, 46, 55, 65, 75, 85, 94, 104, 114, 124, 133, 143,
  153, 163, 172, 182, 192, 202, 211, 217-230 (every page the scan yields text for;
  the remaining pages are image-only)
slug: michael-sheimo-stock-market-rules
source_file: Michael Sheimo - Stock Market Rules.pdf
source_review: partial
tags:
- sas
- portfolio-analysis
- capm
- optimization
- discounted-cash-flow
- options
tier: B
title: 'Stock Market Analysis Using the SAS System: Portfolio Selection and Evaluation'
year: unknown
---

## Summary

Despite its filename, the source is not Michael Sheimo's Stock Market Rules. It is the first edition of Stock Market Analysis Using the SAS System: Portfolio Selection and Evaluation for SAS Version 6. The task-oriented manual demonstrates return and risk calculations, dividend-discount valuation, stock sorting and clustering, CAPM, linear and nonlinear portfolio optimization, performance evaluation, and option pricing. The OCR is sampled and sparse, so this note documents the actual source and its reliable high-level content rather than reconstructing code.

## Key points

- Single- and multiple-period return measures establish the data foundation.
- Discounted cash-flow examples value fixed and growing dividends and screen for relative mispricing.
- Sorting and clustering group stocks by financial characteristics.
- CAPM chapters estimate beta and use the security market line.
- Linear and integer programming impose portfolio constraints; nonlinear programming implements a Markowitz model.
- Evaluation compares expected with realized returns and distinguishes systematic from total risk.
- Final chapters value options with binomial and Black–Scholes methods.

## Actionable rules

Except for the CAPM interpretation in item 2, these are editorial workflow implications drawn from the manual's covered tasks, not its verbatim rules:

1. Standardize return intervals and risk-free rates before comparing securities or portfolios.
2. Treat CAPM alpha as the regression intercept: positive alpha indicates consistent positive nonmarket returns and performance above the fitted expectation; negative alpha indicates the reverse (PDF p. 221).
3. Compare portfolios by beta only when systematic risk is the relevant denominator; also inspect total volatility and constraints.
4. Encode diversification, short-sale, and integer-lot limits explicitly in the optimizer rather than adjusting a solution afterward.
5. Validate any optimized weights out of sample because estimated means and covariances are unstable.

## Chapter coverage recovered from the scan

Sampled pages confirm the book's arc: Chapter 1 covers single- and multiple-period return measures, expected returns computed from probability-weighted outcomes across large stock lists, and risk measures. Chapter 2 works through discounted-cash-flow analysis — fixed-dollar and constant-growth dividend models, multiperiod DCF, and a regression screen for over- and under-priced stocks (the worked example reports an R-squared of 0.733, with only the intercept and one slope significant at the 0.10 level, and advises respecifying the model). Chapter 3 sorts and clusters stocks by financial characteristics, converting a correlation matrix into Euclidean dissimilarities and building single-linkage cluster trees. Chapter 4 estimates the CAPM in risk-premium form, warns that autocorrelated errors invalidate the significance tests, and applies the fitted betas to the security market line. Chapters 5 and 6 build portfolios: linear programming (PROC LP) for optimal weights subject to a maximum acceptable risk, with and without short sales, then nonlinear programming (PROC NLP) for the efficient frontier, ending with the arithmetic that converts optimal weights into dollar amounts for a $100,000 portfolio. The book repeatedly cautions that solution weights are only as good as the return and risk estimates fed into them.

## Caveats

Most equations and code are absent from the sampled OCR, and SAS Version 6 syntax is obsolete. The filename and slug are materially misleading; the title page and contents determine this note's identity (PDF pp. 1-4).

## Who it is for

Readers studying the history of statistical portfolio workflows or translating legacy SAS finance examples into modern tools.
