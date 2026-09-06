---
title: "Liquidity Supply and Demand in Limit Order Markets"
author: "Burton Hollifield, Robert A. Miller, Patrik Sandås and Joshua Slive"
year: 2002
slug: hollifield-miller-sandas-and-slive-liquidity-supply-and-demand-in-limit-order-markets
tier: B
category: Quant, Microstructure & Academic Research
tags: [market-microstructure, limit-orders, liquidity, execution-risk]
difficulty: advanced
doc_type: paper
pages: 55
one_liner: "A structural model links limit-versus-market order choice to immediacy, execution probability, and picking-off risk."
related: [madhavan-market-microstructure-a-survey, chordia-roll-and-subrahmanyam-commonality-in-liquidity]
source_file: "Hollifield, Miller, Sandas And Slive-Liquidity Supply And Demand In Limit Order Markets.pdf"
source_review: full
reviewed_pdf_pages: "1-55"
---
## Summary

The paper models how traders choose market orders, limit orders, or no order when they differ in private valuations. It defines the price of immediacy from quoted prices, expected execution probability, and picking-off risk, then estimates the model with order and transaction records from three Vancouver Stock Exchange mining stocks observed from May 1990 to November 1993. The estimates show that market conditions alter both order timing and order type. In the sample, market orders were about 37% of submissions at a 2.5% proportional spread and about 30% at a 3.5% spread; market-order traders had valuations at least 4.9% and 7.1% from the average, respectively (pp. 5-7). Wider spreads and low depth made patient limit orders more attractive, with estimated utility gains up to 40% for liquidity traders and 10% for value traders (p. 6).

## Key points

- A market order buys immediacy; a limit order buys price improvement while accepting delay and non-execution risk (pp. 5, 14-15).
- Extreme private valuations create high willingness to pay for immediacy; moderate valuations tend toward limit orders or no order (pp. 5-6, 13-15).
- The sample’s average time between submissions was about 6 minutes, versus about 23 minutes for a value trader arrival (p. 7).
- A Weibull hazard estimate found order-arrival probability declines with elapsed time since the previous submission; its shape parameter was below one (pp. 11-12).
- In the competing-risks estimates, execution-hazard shape parameters were 0.544-0.817 and cancellation-hazard parameters 0.468-0.652; cancellation becomes relatively more likely the longer an order remains (pp. 21-22).
- Wider spreads predicted longer time to the next submission but increased the probability that a submitted order was a limit order (pp. 11-12).
- The study uses 2.5% of mid-quote as a depth boundary and identifies marginal versus one-tick-away orders in its regressions (pp. 9, 15).
- The paper’s two-day execution forecasts put marginal sell/buy fill probabilities near 16%/13% and one-tick sell/buy probabilities near 61%/63%; wider spreads raise execution probability for one-tick orders, while larger size lowers it (pp. 23-24).
- Conditional picking-off risk is near zero for one-tick orders and about one cent for marginal orders at mean conditions; it is sensitive to the distance between common value and mid-quote (p. 25).
- The three-stock sample contains 55,444, 56,599, and 47,578 order submissions, with mean percentage spreads of 3.9%, 2.8%, and 3.4% and mean depths of 21, 10, and 10 thousand shares (p. 37, Table 1).
- Ordered-probit estimates show spread, depth, order size, recent trades, volatility, lagged return, and time-of-day variables jointly affect market-versus-limit choice, with 23,199-31,254 observations per stock-side model (p. 41, Table 5).

## Actionable rules

1. Compare spread, same-side depth, volatility, and order urgency before selecting a market or limit order; the paper’s model treats these as determinants of expected utility (pp. 11-15).
2. Treat a limit order as a trade-off: estimate fill probability and adverse price movement rather than assuming quoted price improvement is free (pp. 5, 14-15).
3. Do not generalize the 2.5%, 3.5%, 4.9%, or 7.1% thresholds into universal triggers; they are estimates from this sample (pp. 6, 8).

## Caveats

The evidence is from three mining stocks on a pre-decimal Vancouver market, and member firms’ proprietary versus customer trades could not be separated. Trader identities could not be linked across submissions, and the model relies on rational expectations and expected-utility maximization (p. 10). CEPR labels the discussion paper provisional. The paper’s execution probabilities are forecast over a two-day horizon and its tables are model estimates, not a complete trading strategy or current venue calibration (pp. 23-32, 37-44).

## Who it is for

Readers studying order-book liquidity, execution quality, or empirical market microstructure.
