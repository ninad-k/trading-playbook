---
author: Douglas W. Hubbard
category: Quant, Microstructure & Academic Research
difficulty: intermediate
doc_type: book
one_liner: Hubbard argues most corporate/financial risk management — subjective scoring
  matrices especially — is unvalidated and often worse than no method at all, and
  prescribes calibrated probabilities plus Monte Carlo modeling as the fix.
pages: 300
related:
- armelle-guizot-the-hedge-fund-compliance-and-risk-management-guide
- risk-management-systems
- prospect-theory
reviewed_pdf_pages: 6, 13 and the scoring-method chapters checked against the note
slug: douglas-hubbard-the-failure-of-risk-management
source_file: Douglas Hubbard - The Failure of Risk Management.pdf
source_review: partial
tags:
- risk-management
- monte-carlo
- risk-matrices
- calibration
- black-swans
- cognitive-bias
- quantitative-methods
tier: B
title: 'The Failure of Risk Management: Why It''s Broken and How to Fix It'
year: 2009
---

## Summary

A critique of mainstream risk-management practice, written after the 2008 financial crisis by decision-analysis consultant Douglas Hubbard (author of *How to Measure Anything*). Part One argues that most risk management has never been objectively tested to see whether it actually reduces losses. Part Two diagnoses why: the "four horsemen" (actuaries, WWII-era operations-research quants, economists, management consultants) each brought incompatible methods and vocabulary; expert judgment is systematically overconfident; the most popular tool — qualitative risk-scoring matrices ("red/yellow/green," 1-5 likelihood/impact grids) — is shown to be worse than random in controlled studies; and even quantitative modelers (Monte Carlo users) routinely misjudge correlations, exclude "too uncertain" tail risks, and assume normal distributions for fat-tailed financial variables. Part Three prescribes fixes: calibrated subjective probabilities, decomposing uncertainty into measurable components, incorporating empirical/actuarial data and Bayesian updating, and building the answers into proper Monte Carlo simulations instead of scoring grids.

## Key points

- **Common mode failure** — many firms failed simultaneously in 2008 despite having "risk management," suggesting a shared flawed methodology rather than isolated bad luck.
- **Scoring/matrix methods worsen decisions** — Hubbard cites research showing 1-5 or red/yellow/green risk matrices produce inconsistent, arbitrary rankings and can be measurably worse than chance at separating high- from low-risk items.
- **Calibrated probability training** — most people (including experts) are poorly calibrated (e.g., "90% confident" answers are right far less than 90% of the time); calibration can be measurably trained and tested.
- **The Measurement Inversion** — the variables risk models most need good data on are usually the ones organizations have measured least.
- **Financial models and fat tails** — Gaussian/normal-distribution assumptions dramatically understate the odds of large market moves (the book notes market crashes described as "13-20 standard deviation events" under normal-distribution assumptions — probabilities that are essentially impossible, exposing the model as wrong, not the event as improbable).
- **Correlation risk** — modelers often ignore or understate correlations between risks, which is what turns many small independent-seeming exposures into one large simultaneous loss.
- **"We're special" objection debunked** — Hubbard rebuts the common claim that a given industry/situation lacks enough data for quantitative methods, citing insurers who successfully price rare events (Olympics cancellation, prize insurance, war-zone credit risk) with little direct historical data.
- **Frequentist vs. subjectivist probability** — the book argues the debate is practically irrelevant to decision-makers; subjective, calibrated probability is the only usable concept for real-world risk decisions.

## Actionable rules

None given as trading rules — this is a book about risk-management methodology, not a trading system. Its actionable takeaway for a trader/allocator: avoid ranking risks on qualitative scoring grids; instead calibrate your own probability estimates, explicitly model correlations between positions/risks, and treat fat-tailed (non-normal) return assumptions as a known blind spot in most standard financial risk models (VaR included).

## Caveats

Aimed at enterprise/insurance/project risk management broadly, not trading specifically — examples span nuclear power, drug manufacturing, and IT projects alongside finance, so a reader wanting only market-risk content must extract it from a wider argument. Hubbard is selling his own calibration-training and Monte Carlo consulting methodology alongside the critique, so treat the "fix" chapters with the same skepticism applied to any vendor's alternative. Published in 2009 in direct response to the financial crisis; some examples and the immediate post-crisis framing are dated, though the core methodological critique (matrix scoring, overconfidence, fat tails) remains widely cited.

## Who it is for

Risk managers, quants, and serious traders who want a rigorous critique of popular but unvalidated risk-assessment tools (scoring matrices, naive VaR) and a case for calibrated, quantitative alternatives — not a beginner's introduction to risk management.
