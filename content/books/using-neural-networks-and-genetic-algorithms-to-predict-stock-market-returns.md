---
title: Using Neural Networks and Genetic Algorithms to Predict Stock Market Returns
author: Efstathios Kalyvas
year: 2001
slug: using-neural-networks-and-genetic-algorithms-to-predict-stock-market-returns
tier: B
category: Quant, Microstructure & Academic Research
tags: [neural-networks, genetic-algorithms, stock-prediction, autoregressive, academic-research, efficient-markets]
difficulty: advanced
doc_type: paper
pages: 166
one_liner: "MSc thesis testing whether autoregressive and neural-network models can predict daily FTSE/S&P excess returns; neither beats naive random-walk benchmarks."
related: [neural-prediction-of-weekly-stock-market-index-1, madhavan-market-microstructure-a-survey]
source_file: "Using Neural Networks and Genetic Algorithms to Predict Stock Market Returns.pdf"
---

## Summary

A University of Manchester MSc thesis asking whether daily excess returns (stock index return minus the Treasury Bill rate) of the FTSE 500 and S&P 500 can be predicted using historical data. Data spans roughly eleven years of daily prices for model fitting plus about one year held out for testing. Method: first run two randomness tests (the Run test and the BDS test) on the excess-returns series to confirm they are not purely random; then fit two model families — univariate/multivariate autoregressive (AR) models, with lag length chosen via Akaike and Bayesian information criteria, and feed-forward neural networks (NN), with a genetic algorithm (GA) searching the space of network topologies (neuron counts, hidden layers) for the best structure. Both model types are evaluated against three naive benchmarks (random walk on price level, random walk on returns, and a "same return as bonds" model) using mean absolute error and three Theil-style benchmark ratios.

## Key points

- Both randomness tests reject pure randomness for the FTSE and S&P excess-returns series — the data does contain some structure, so prediction is not a priori hopeless.
- Despite that, neither the AR models nor the GA-optimized NN models beat the naive "no change in market value" and "same return as bonds" benchmarks; only the weakest naive benchmark (random walk on returns) was reliably beaten.
- The GA did not converge on one dominant network topology; instead several different structures performed comparably well, with a consistent pattern of few neurons in the second hidden layer.
- NN mean absolute error was close to figures reported in comparable studies (e.g., Steiner & Wittkemper on Frankfurt data), suggesting the result is not an artifact of this particular dataset.
- Mean absolute error alone is judged a misleading metric — models can look good on MAE while still failing to beat a "no change" naive predictor, which the study argues is the harder, more meaningful bar.
- NN models are judged theoretically superior to AR models because they can capture nonlinear as well as linear patterns, but this advantage did not translate into a practical edge in these experiments, and NN results are sensitive to random weight initialization.
- The authors' interpretation: daily data may be too noisy, and any real patterns may be "local" (stable only over short sub-periods) rather than the stable "global" patterns these models are built to find.

## Actionable rules

None given — no tradable entry/exit system is proposed. The transferable takeaway for a trader evaluating any predictive model (ML-based or otherwise) is:
1. Always benchmark against naive predictors, especially a "no significant change" random-walk model — the paper found these surprisingly hard to beat.
2. Don't rely on mean absolute error alone to judge a forecasting model; use directional/benchmark-ratio metrics as well.
3. Be skeptical of "global" pattern-mining over long historical windows given markets' evolving regimes; consider testing on shorter, adaptive windows instead.

## Caveats

This is an academic MSc thesis, not a trading manual — there is no discussion of transaction costs, position sizing, or live execution. The dataset and NN architectures (2001-era feed-forward nets) are dated relative to modern deep-learning approaches; conclusions about NN inability to beat naive predictors may not generalize to more recent architectures, features, or higher-frequency data. Findings support (rather than refute) a broadly efficient-markets view for the specific setup tested — daily excess returns using only lagged own-history as input.

## Who it is for

Quantitatively minded readers or systematic traders evaluating whether generic ML/NN forecasting on daily index data can produce an edge, and who want a rigorous, benchmark-driven cautionary study before building a return-prediction model.
