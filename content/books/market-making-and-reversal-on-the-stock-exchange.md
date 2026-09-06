---
title: Market Making and Reversal on the Stock Exchange
author: Victor Niederhoffer and M. F. M. Osborne
year: 1966
slug: market-making-and-reversal-on-the-stock-exchange
tier: B
category: Quant, Microstructure & Academic Research
tags: [market-microstructure, mean-reversion, order-flow, limit-orders, price-clustering]
difficulty: advanced
doc_type: paper
pages: 21
one_liner: Transaction-level NYSE data link bid-ask reversals and fractional-price clustering to specialist order books.
related: []
source_file: "Market Making and Reversal on the Stock Exchange.pdf"
source_review: full
reviewed_pdf_pages: "1-21"
---

## Summary

Niederhoffer and Osborne test whether consecutive NYSE transaction-price changes are independent. In six Dow stocks during October 1964, nonzero changes reversed direction roughly three times as often as they continued (PDF pp. 3–6). The authors explain this through market making: alternating market buys and sells execute at opposite sides of the quote, while limit orders form barriers at favored fractional prices. A second sample across listed stocks confirms both the reversal tendency and effects associated with the preceding two moves and eighth-price location (PDF pp. 9–19).

## Key points

- The first sample contains 10,536 consecutive transaction pairs from six Dow stocks over 22 trading days in October 1964 (PDF pp. 3–4).
- Among 2,518 pairs of nonzero changes, opposite-direction pairs occurred about three times as often as same-direction pairs; the transition distributions strongly reject independence (PDF pp. 5–7).
- Reversal is not constant. A continuation is more likely after a previous continuation than after a previous reversal, although reversal remains the dominant next outcome (PDF pp. 7–9, 15–16).
- Bid and ask coexist. With balanced buy and sell market orders, prints oscillate between them; one-sided orders exhaust limit orders and produce runs (PDF pp. 9–12).
- Limit orders clustered at integers, halves, quarters, then odd eighths. The paper attributes more reversals near the stronger barriers to this placement pattern (PDF pp. 11–13, 17–19).
- In the second sample, 12,777 eighth-change events yielded a 2.34-to-1 reversal/continuation ratio. Twenty-nine of 40 fractional-price predictions agreed with the theory, under assumptions the authors call “heroic” (PDF pp. 14–18).

## Actionable rules

1. Do not read transaction-by-transaction reversal as fundamental mean reversion; first test whether bid-ask alternation explains it (PDF pp. 9–12).
2. The authors’ period-specific rule places limit and stop orders at odd eighths, preferably sell orders at 7/8 and buy orders at 1/8 (PDF p. 19).
3. Their second rule buys when price advances through a limit-order barrier and sells when it falls through one (PDF p. 19).
4. Condition any sequence analysis on both the preceding moves and the terminal price fraction; the paper finds neither dimension interchangeable (PDF pp. 9, 15–18).

## Caveats

The study uses 1960s specialist markets and eighth-dollar ticks, so its quoted order rules do not transfer directly to decimal electronic markets. Statistical dependence is not a net-profit test: costs, queue position, execution uncertainty, and out-of-sample stability are not established. The second sample also overlaps events and simplifies moves into fixed eighth categories (PDF pp. 14, 19–20).

## Who it is for

Microstructure researchers and traders studying how quotes and clustered orders create short-horizon return patterns.
