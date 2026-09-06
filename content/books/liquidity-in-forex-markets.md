---
author: Michael J. Moore and Maurice J. Roche
category: Quant, Microstructure & Academic Research
difficulty: advanced
doc_type: paper
one_liner: Journal of Empirical Finance paper building a limited-participation two-country
  model to explain spot-return autocorrelation, forward-discount persistence, and
  the forward bias puzzle via a liquidity 'wedge.'
pages: 14
related:
- engle-and-lange-predicting-vnet-a-model-of-the-dynamics-of-market-depth
- madhavan-market-microstructure-a-survey
- international-macro-economics-and-finance
reviewed_pdf_pages: 7-11 (the calibration parameters and the model comparison results)
slug: liquidity-in-forex-markets
source_file: Liquidity in Forex Markets.pdf
source_review: partial
tags:
- academic-paper
- forward-exchange-rate
- liquidity
- cash-in-advance-model
- forward-discount-puzzle
- macro
tier: B
title: Liquidity in the Forward Exchange Market
year: 2001
---

## Summary

An academic paper (Journal of Empirical Finance, 2001) by Michael J. Moore and Maurice J. Roche that extends the standard two-country cash-in-advance (CIA) model of exchange rates into a "limited participation" framework where portfolio decisions must be made before money/endowment shocks are known. The question: can this modification better explain three long-standing puzzles — the near-zero autocorrelation of observed spot returns (vs. the standard model's over-prediction of persistence), the persistence of the forward discount, and the volatility/bias of the forward premium as a predictor of future spot returns? The authors calibrate the model to quarterly G7 data (1976–1993) and simulate an "artificial economy" (1,000 replications) to compare its predictions with the standard CIA model.

## Key points

- The standard CIA model predicts spot returns should inherit the autocorrelation of the money-growth differential — counterfactual, since observed spot returns are close to white noise.
- The new "limited participation" model adds a liquidity wedge (assets must be purchased with cash accumulated before shocks are known) between spot returns and the forward discount, breaking the mechanical link to money shocks.
- At high relative risk aversion (coefficient = 10), the new model's first-order autocorrelation of spot returns falls to 0.26, versus a constant 0.72 in the standard model (empirical value is close to zero) — an improvement but not a full resolution.
- The forward discount's persistence in both models tracks the autocorrelation of the underlying money-growth differential; matching empirically observed persistence requires an AR(1) coefficient of about 0.7–0.8 in money growth.
- The "expected profit from currency speculation" (a summary statistic for forward-market bias) rises to a standard deviation of 0.54%/quarter as risk aversion increases in the new model — a fivefold improvement over the standard model, but still far below the empirically observed 2–3%/quarter.
- Risk aversion has no effect on volatility statistics in the standard CIA model; in the liquidity-constrained model, it raises spot-return volatility to levels (6.9%/quarter) that match observed data.
- Calibration parameters: discount factor β based on 3% annual real rate; home-goods consumption share α = 0.5; risk aversion coefficient varied 2–10; money-growth AR(1) coefficient varied 0.1–0.9 (representative G7 value ≈ 0.78).
- Conclusion: the model improves on the standard CIA framework when both risk aversion and money-growth persistence are high, but "fails miserably" to fully explain the high volatility of spot returns relative to the forward premium, and only partially explains the forward discount bias.

## Actionable rules

None given — this is a theoretical/empirical macro-finance paper, not a trading system. Practical takeaway for a trader: the paper is direct academic evidence that neither risk premia nor simple cash-in-advance liquidity effects fully explain why the forward rate is a biased predictor of the future spot rate (the "forward premium puzzle") — a caution against assuming interest-rate-differential-based carry signals are unbiased forecasts of currency direction.

## Caveats

This is a highly technical, equation-heavy academic paper (general-equilibrium modeling, linear-quadratic approximation methods, VAR calibration) aimed at economists, not practitioners; it contains no charts, entry/exit rules, or discussion of retail trading mechanics. Data and calibration are from G7 quarterly series covering 1976–1993, now several decades old. The PDF text extraction is noisy in places (OCR artifacts from mathematical notation), though the narrative sections are legible.

## Who it is for

Quant-minded readers who want to understand the academic literature behind the forward-rate bias / uncovered interest parity puzzle and how market liquidity has been formally modeled to (partially) explain it — not a resource for building a trading system.
