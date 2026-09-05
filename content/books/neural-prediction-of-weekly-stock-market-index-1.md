---
title: "Application of Neural Networks to Stock Market Prediction"
author: Amol S. Kulkarni
year: 1996
slug: neural-prediction-of-weekly-stock-market-index-1
tier: B
category: Quant, Microstructure & Academic Research
tags: [neural-networks, backpropagation, s-and-p-500, interest-rates, academic, forecasting, quant]
difficulty: advanced
doc_type: paper
pages: 18
one_liner: "A feedforward neural network using detrended S&P 500 history plus lagged interest rates predicts next week's index one week ahead, tested on the 1987 crash and 1994 bull run."
related: [international-macro-economics-and-finance]
source_file: "Neural Prediction Of Weekly Stock Market Index(1).pdf"
---

## Summary

Question: can a neural network predict next week's S&P 500 level one week ahead using the index's own past values plus lagged short- and long-term interest rates? Data: weekly S&P 500 close, 3-month and 10-year rates from October 1972 to April 1996. Method: cross-correlation found the long rate leads the detrended index by about 25 weeks and the short rate by 20 and 48 weeks; these series plus the index's 5- and 10-week moving averages and first differences (18 inputs, log-detrended and tanh-normalized) feed a single-hidden-layer (7-neuron) feedforward network trained by backpropagation. Finding: on two out-of-sample "worst case" windows — the run-up to the October 1987 crash and the January 1994 bull market — the network predicted correct weekly direction 65/75 and 43/50 times, with average errors of 4.18% and 0.95%.

## Key points

- **Interest rates lead stocks**: the 10-year rate is negatively correlated with the S&P 500 at about a 25-week lag; the 3-month rate similarly at 20 and 48 weeks.
- **Detrending is essential**: raw index normalization saturates the network on trending data; a log-then-linear detrend fixed this.
- **18 network inputs**: detrended index, its 5- and 10-week moving averages, first differences with an encoded trend feature, plus the delayed long and short rates and their differences/trends.
- **1994 bull-run test**: correct direction 43/50 times, average error 0.95% — attributed mainly to underlying momentum rather than the rate inputs.
- **1987 crash test**: correct direction 65/75 times, average error 4.18% — attributed specifically to the rising long-rate input, since the index itself showed no clear momentum going in.
- **Non-linear (tanh) normalization**, not linear scaling, was needed to keep the exponentially trending index learnable.

## Actionable rules

None given as a tradable system. The paper stops at directional prediction accuracy and error metrics; it explicitly flags as future work that "a trading mechanism based on the predictions of the network needs to be established" — no entry/exit/sizing rules, transaction costs, or live trading were tested. The one general takeaway a trader can extract: long-term and short-term interest-rate trends, lagged by roughly 20-50 weeks, showed a statistically meaningful negative correlation with subsequent S&P 500 moves in this 1972-1996 sample.

## Caveats

Extremely small network (7 hidden neurons) and a mid-1990s academic exercise; only two out-of-sample windows are tested, both cherry-picked as "worst case" scenarios rather than a rolling walk-forward evaluation across the full history. No transaction costs, slippage, or trading rule is specified, so the reported accuracy cannot be translated into a return figure. Interest-rate delay values (20, 25, 48 weeks) were fit to this specific historical window and are not shown to be stable out of sample.

## Who it is for

Quant researchers interested in an early, transparent worked example of neural-network stock index forecasting using macro (interest rate) inputs, useful as a methodology reference rather than a source of trading rules.
