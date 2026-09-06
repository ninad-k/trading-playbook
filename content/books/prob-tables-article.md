---
title: "Selling Options: Examining Risk"
author: "Guy Bower"
year: unknown
slug: prob-tables-article
tier: B
category: Options, Futures & Derivatives
tags: [options, probability, covered-calls, risk]
difficulty: advanced
doc_type: article
pages: 5
one_liner: "An options article estimates the probability of a strike being reached and shows why premium income must be weighed against tail risk."
related: [fixed-income-securities, position-sizing]
source_file: "prob tables article.pdf"
source_review: full
reviewed_pdf_pages: "1-5"
---
## Summary

Bower describes a probability tool for estimating the chance that an option strike will be reached before expiry. The worked example considers a covered call that earns $0.43 per share while a strike roughly 8%-9% away may still be reached in 23 trading days with an estimated probability around 33.14%-35.22%, summarized as about one in three (pp. 3-4). The conclusion is that a strike can be too close when the premium is small relative to the chance of assignment or adverse opportunity cost. The author warns that the imbalance matters even more for naked calls and that a bell-curve assumption may fit less volatile markets better (p. 5).

## Key points

- Probability estimates help compare premium with the chance of the strike being hit.
- A small premium can carry unattractive risk-reward when the strike is close (pp. 3-4).
- Covered calls and naked calls have materially different risk profiles (p. 4).
- The method relies on a distributional assumption and historical volatility.
- The article’s numerical example is market specific.

## Actionable rules

1. Estimate strike-hit probability before selling an option and compare it with collected premium (pp. 3-4).
2. Move the strike farther away or shorten the time frame when the estimated risk-reward is unfavorable (p. 4).
3. Test the probability tool on the chosen market; the author says it works better in less volatile markets (p. 5).

## Caveats

The five-page article does not provide a complete formula or hedge plan. Normality and volatility estimates can fail in jumps, gaps, and stressed markets. Naked option risk can be much larger than the example suggests.

## Who it is for

Options traders learning to quantify assignment or strike-touch risk before selling premium.
