---
title: "How to Test and Interpret Trading System Performance"
author: Wayne A. Thorp
year: 2001
slug: wayne-a-thorp-testing-trading-success
tier: B
category: Quant, Microstructure & Academic Research
tags: [backtesting, system-testing, optimization, slippage, commissions, money-management-stops]
difficulty: intermediate
doc_type: article
pages: 5
one_liner: "AAII Journal article showing, with a worked 20-year example, how commissions, slippage, margin, stops and idle interest each swing a mechanical system's reported returns."
related: [wayne-a-thorp-measuring-internal-strength-wilders-rsi-indicator, wayne-a-thorp-the-macd-a-combo-of-indicators-for-the-best-of-both-worlds, balsara-nauzer-j-money-management-strategies-for-futures-traders, jack-schwager-guide-to-winning-with-automated-trading-systems-course-manual]
source_file: "Wayne A. Thorp - Testing Trading Success.pdf"
---

## Summary

An AAII Journal (January 2001) technical-analysis column by Wayne Thorp, assistant financial analyst at AAII, explaining why a trading system's headline backtest return is usually misleading. Using a simple moving-average-crossover stock system tested over 20 years, the article layers in commissions, slippage, margin, protective stops, and idle-balance interest one at a time to show how far actual results diverge from the "sterile" (assumption-free) backtest.

## Key points

- Backtested results are more easily manipulated ("optimized") than live results; ask whether performance numbers are from real trading or backtesting, and over what period.
- Recommends a "hold-out" validation method: optimize parameters on half the historical data, then test unchanged on the other half — large divergence between the two halves signals overfitting.
- A system should be compared against a simple buy-and-hold benchmark; if it can't beat buy-and-hold, it needs rework.
- Dividends and taxes are usually ignored by backtesting software but materially affect real returns.
- In the worked example (20-year backtest, simple crossover system), trading on margin cost $141.88 versus not using margin (but buy-and-hold on margin would have earned an extra ~$97,000).
- $15/trade commissions on 807 trades cost $12,105 directly, but $14,101.46 in true opportunity cost.
- Delaying execution to the next day's open (realistic slippage) turned the sterile system's result into a net loss of $1,604.27 — a swing of $22,207.59 versus the no-slippage case.
- Adding a 2%-of-equity max-loss stop and a 20%-of-open-profit trailing stop added $102,050.32 versus the sterile system ($81,447 improvement) — protective stops were the single largest positive factor in this example.
- Combining every real-world factor (margin, commissions, slippage, stops, idle interest) turned the system's $200,000+ theoretical gain into a net loss, ending with only $9,999.46 of the original $100,000 test equity.
- System execution requires ongoing trader attention (or automation); most trading software generates signals but doesn't execute trades — following the system in real time is often the hardest part.

## Actionable rules

1. Never evaluate a system on its raw backtest number alone — re-run it with commissions, realistic slippage (next-bar-open fills), margin cost, and dividend/tax treatment applied.
2. Validate any optimized parameter set on a hold-out period the optimizer never saw; distrust results that only look good in the optimization window.
3. Include an explicit money-management stop (the article's example: 2% of remaining equity per trade) and a trailing stop (example: 20% giveback of open profit) — in the worked example these turned a losing sterile system materially more favorable.
4. Compare final system equity to a buy-and-hold benchmark over the same period before adopting the system.

## Caveats

Single illustrative example (one moving-average-crossover system on one 20-year run) — the specific dollar figures are not generalizable to other systems or markets, only the categories of cost they illustrate. Article is over two decades old; 2001-era commission ($15/trade) and margin conventions are dated, though the underlying methodology (hold-out testing, layering in real-world costs) remains standard practice.

## Who it is for

Anyone building or evaluating a mechanical/systematic trading strategy who needs a checklist of the real-world costs that must be added to a raw backtest before trusting its numbers.
