---
title: Mathematical Economics and Finance
author: "Michael Harrison, Patrick Waldron"
year: 1998
slug: harrison-waldron-mathematical-economics-and-finance
tier: B
category: Quant, Microstructure & Academic Research
tags: [mathematical-finance, portfolio-theory, capm, optimization, linear-algebra, academic, lecture-notes]
difficulty: advanced
doc_type: course
pages: 153
one_liner: "Trinity College Dublin lecture notes building math finance from linear algebra and optimization through mean-variance portfolio theory and the CAPM."
related: [black-scholes-option-pricing-model, kiesel-financial-mathematics, bass-the-basics-of-financial-mathematics, lecture-notes-in-mathematical-finance-lin-1996]
source_file: "Harrison_ Waldron - Mathematical Economics and Finance.pdf"
---

## Summary

Course notes for MA381/EC3080, taught at Trinity College Dublin, aimed at advanced undergraduates crossing over between mathematics and economics. Part I covers the mathematical toolkit: linear algebra (matrices, eigenvalues, quadratic forms), vector calculus (partial derivatives, the implicit function theorem, Taylor's theorem), and convexity/optimization (unconstrained, Lagrange, and Kuhn-Tucker constrained optimization, duality). Part II applies this machinery to economics and finance: choice under certainty and uncertainty, portfolio theory, and investment analysis. The portfolio theory chapter derives the mean-variance efficient frontier (with and without a riskfree asset) from first principles and builds up to the Capital Asset Pricing Model (CAPM). A final chapter sketches arbitrage pricing of derivatives (binomial and Black-Scholes models) but is left largely as a stub.

## Key points

- Frames finance as a subset of microeconomics: allocation across goods (prices), across time (term structure of interest rates), and across states of nature (risky asset returns).
- Builds the portfolio frontier by minimizing variance subject to a target expected return, deriving the frontier both in weight space and in mean-standard-deviation (mu-sigma) space.
- With a riskfree asset, the frontier becomes a straight line (capital market line) from the riskfree rate through the tangency portfolio; frontier portfolios above the tangency point imply borrowing.
- Derives the CAPM beta relationship (E[r_q] - E[r_zp] = beta_qp * (E[r_p] - E[r_zp])) from the tangency condition between an inner and outer frontier.
- CAPM's core assumption is stated plainly: every investor has mean-variance preferences, achieved by assuming either quadratic utility or normally distributed returns.
- Notes the limiting behavior of diversification: as the number of securities in an equally weighted portfolio grows, portfolio variance converges toward the average covariance across assets (the "systematic risk" floor).
- Chapter 7 (arbitrage pricing, binomial and Black-Scholes option pricing) is only outlined in the table of contents and not developed in the available text.

## Actionable rules

None given — this is a theoretical/mathematical reference, not a trading system. Its practical takeaway for a trader is conceptual: portfolio risk cannot be diversified below the average covariance among held assets, and CAPM-style beta pricing rests on the (often unrealistic) assumption of mean-variance investor preferences.

## Caveats

This is an unfinished course draft, not a polished textbook: several sections are explicitly marked "[To be written]" (the Linear Algebra and Mathematics introductions) or "Need more waffle here" (the CAPM pricing-and-prediction section), and figures are referenced as "Figure 3C goes here" without being included. The option-pricing chapter, which would be most directly relevant to derivatives traders, is essentially a stub. The material assumes graduate-level comfort with proofs, matrix calculus, and constrained optimization; it is not accessible to readers without a quantitative background.

## Who it is for

Mathematically trained readers wanting the formal derivation of mean-variance portfolio theory and CAPM from optimization first principles, not practitioners looking for trading rules or a complete options-pricing treatment.
