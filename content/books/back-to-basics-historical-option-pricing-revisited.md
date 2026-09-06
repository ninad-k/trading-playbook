---
author: Jean-Philippe Bouchaud, Marc Potters
category: Options, Futures & Derivatives
difficulty: advanced
doc_type: paper
one_liner: Physicists Bouchaud and Potters re-derive option pricing from historical
  (not risk-neutral) probability using a risk-minimization framework, and show the
  resulting volatility smile matches real BUND option data.
pages: 10
related:
- kiesel-financial-mathematics
- black-scholes-option-pricing-model
- hull-options-futures-and-other-derivative-securities-5th-ed
reviewed_pdf_pages: 1, 5, 8 (the residual-risk result, the empirical Bund-future study
  and the model assumptions)
slug: back-to-basics-historical-option-pricing-revisited
source_file: Back To Basics -- Historical Option Pricing Revisited.pdf
source_review: partial
tags:
- option-pricing
- black-scholes
- volatility-smile
- kurtosis
- risk-minimization
- academic-research
tier: B
title: 'Back to Basics: Historical Option Pricing Revisited'
year: 1999
---

## Summary

Question: can option prices be derived directly from the historical (real-world) probability distribution of the underlying asset, rather than from an abstract risk-neutral measure — and if so, does that theory match real option prices? Method: the authors build a risk-minimization pricing framework (minimizing the variance of a hedged wealth balance) for a general process with uncorrelated but not-necessarily-independent, non-Gaussian price increments, show it collapses to the standard Black-Scholes result in the Gaussian limit, then derive a formula linking the volatility smile's curvature to the underlying return distribution's kurtosis. Data: options on the BUND futures contract (a liquid European bond future) traded 1993-1995, compared against 5-minute tick data of the underlying future over the same period.

## Key points

- In the risk-minimization framework, the option price and optimal hedge are not unique — they depend on the definition of risk used — but the Black-Scholes delta-hedge and price emerge exactly in the Gaussian (constant-volatility) special case.
- For realistic (fat-tailed, non-Gaussian) return distributions, residual hedging risk does not vanish: for a typical one-month option the standard deviation of residual risk can be as much as 25% of the option's price.
- A positive average return shifts the price of out-of-the-money and in-the-money options in opposite directions once return kurtosis is nonzero — so the Black-Scholes independence of option price from expected return breaks down outside the Gaussian case.
- The theory predicts implied volatility should vary with strike price in a roughly parabolic shape ("volatility smile"), with curvature set by the terminal distribution's kurtosis at that maturity.
- Empirically, implied volatility tracked a short-window filter of historical volatility closely, and implied kurtosis matched historical kurtosis from the underlying tick data with no free parameters.
- Historical kurtosis decayed with maturity more slowly than the N⁻¹ rate expected for independent, identically distributed returns — evidence of volatility persistence (clustering) in the underlying.

## Actionable rules

None given as trading rules — this is a theoretical/empirical asset-pricing paper. The practical takeaway for a trader: implied volatility skew/smile shape is not an arbitrary market quirk but tracks the real (measurable) fat-tailedness of the underlying's historical return distribution, so historical kurtosis can be used as a sanity check on whether an options market's smile is priced richly or cheaply relative to the underlying's actual statistical behavior.

## Caveats

Dense in stochastic calculus and cumulant-expansion mathematics; assumes graduate-level familiarity with Black-Scholes derivation and Fourier/cumulant methods. Findings are specific to the 1993-1995 BUND futures options market and may not generalize in form (though the qualitative smile-kurtosis link is widely cited in the market-microstructure/econophysics literature). The paper explicitly restricts to short maturities (up to ~2 months) and small average returns; its perturbative expansion is not valid for large trends or long-dated options.

## Who it is for

Quant-leaning readers who want the theoretical link between fat tails/kurtosis and the volatility smile, and empirical confirmation that implied volatility is not fully detached from the underlying's historical statistics.
