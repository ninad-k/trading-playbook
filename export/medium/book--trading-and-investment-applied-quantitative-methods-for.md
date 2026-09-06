# Applications of Advanced Regression Analysis for Trading and Investment: the trader's summary

*A book chapter benchmarks a Neural Network Regression model against naive, ARMA, logit, and MACD models forecasting EUR/USD, finding NNR gives the best risk-adjusted trading returns.*

**Christian L. Dunis, Mark Williams** · 2003 · Quant, Microstructure & Academic Research · advanced

*Source coverage: partial. PDF pages inspected: 7, 9, 14-15, 36 (the ARMA estimation tables and the strategy performance comparison). These are study notes, not verified trading results.*

## Summary

Question: can regression-based models, and Neural Network Regression (NNR) in particular, add forecasting and trading value on the EUR/USD exchange rate beyond simpler benchmark techniques? Data: a synthetic daily EUR/USD series (retropolated before the euro's 1999 launch) plus related macro/market inputs (FTSE, DAX, S&P 500, Nikkei, CAC 40, yield curves), in-sample from 17 October 1994 to 18 May 2000, out-of-sample from 19 May 2000 to 3 July 2001. Method: five models — naive (random walk), MACD, ARMA(10,10), logit, and NNR — are each used to generate daily buy/sell signals (long EUR if forecast positive, short otherwise), then compared on statistical forecast-accuracy measures (MAE, RMSE, MAPE, Theil-U, correct directional change) and on simulated trading performance (annualized return, Sharpe ratio, maximum drawdown, % winning trades), including transaction costs. Finding: statistical accuracy measures gave no clear winner, but on trading performance the NNR model dominated — highest annualized return, highest Sharpe ratio, and still profitable after estimated transaction costs.

## Key points

- Only 3 in 10 spot FX dealers are profitable in any given year, per a cited industry estimate — underscoring how hard EUR/USD forecasting is.
- Out-of-sample trading performance: NNR annualized return 29.68%, cumulative return 34.16%, Sharpe ratio 2.57 — best of all five models on every trading metric.
- Comparison: naive model 21.34% return (Sharpe 1.83); MACD 11.34% (Sharpe 0.97); ARMA(10,10) 12.91% (Sharpe 1.10); logit 21.05% (Sharpe 1.81).
- Forecasting-accuracy measures alone did not identify NNR as best — the naive model had the lowest Theil-U (0.6901) and MACD the highest correct-directional-change rate (60%), showing low forecast error does not guarantee trading profit.
- The FX managed-futures industry's average Sharpe ratio is cited as only about 0.8; all five models beat that bar out-of-sample.
- Transaction costs (3 pips/trade, ~0.033% average) cut the NNR strategy's return by an estimated 4.55% (136 transactions) but it remained the top performer after costs.
- MACD had far fewer transactions (25) than NNR (136), reflecting a structurally longer holding-period style.
- All five models forecast down-moves more accurately than up-moves, attributed to the in-sample EUR/USD series itself trending down.
- Stated NNR weakness: it is a "black box" whose internal logic cannot be statistically tested the way linear regression can.

## Actionable rules

1. Do not select a forecasting model on statistical accuracy (RMSE, MAPE, Theil-U) alone — evaluate on realized trading performance (Sharpe ratio, drawdown, win rate).
2. Include realistic transaction costs (3 pips/trade here) before judging any high-frequency FX signal strategy profitable.
3. Treat a Sharpe ratio above ~0.8 as competitive with FX managed-futures averages, and above ~2.5 as strong.
4. Expect a model trained on a directionally skewed in-sample series to forecast that same direction better out-of-sample.

## Caveats

This academic/practitioner chapter uses data through mid-2001 and era-typical NNR architectures — modern deep learning methods are not compared. NNR's edge may partly reflect its higher trading frequency (136 transactions, second-most of all models) rather than pure forecasting skill, and the authors caution NNR results depend heavily on data quality and are not always superior. All results are backtested/simulated, not a live track record.

## Who it is for

Quant-oriented FX traders and researchers evaluating machine-learning/regression approaches to currency forecasting, and anyone wanting a concrete illustration of why trading-performance metrics should govern model selection over pure statistical accuracy.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: neural-networks, regression, forex, eur-usd, backtesting, sharpe-ratio, forecasting, academic
