# Money Management Strategies for Serious Traders: the trader's summary

*A workshop shows how to evaluate a trading system’s stability and match position sizing to drawdown tolerance and trader psychology.*

**David C. Stendahl** · 1999 · Money Management & Position Sizing · intermediate

*Source coverage: full. PDF pages inspected: 1-46. These are study notes, not verified trading results.*

## Summary

Stendahl presents money management as a separate design problem from signal generation. The workshop evaluates breakout systems on Yen and Corn, reviews trade and equity stability, then considers methods for sizing, adding, reducing, and stopping positions. The opening pages argue that a positive-expectancy method can still fail when risk is too large, while aggressive sizing can create drawdowns a trader cannot follow psychologically (pp. 1-3). Evaluation should include net profit, percent profitable, profit factor, run-up, drawdown, Sharpe and related stability measures rather than a single return number (pp. 5-10). The method is therefore a workflow for testing and matching risk, not a universal percentage formula.

## Key points

- Position size must fit both the system’s drawdown profile and the trader’s capitalization and tolerance (pp. 1-3).
- Run-up is maximum unrealized profit potential during a trade; drawdown is maximum loss potential (p. 6).
- Trade clustering and coefficient of variation help assess stability before adding leverage (p. 7).
- Mark-to-market summaries allocate open-trade gains and losses to each reporting period (pp. 8-9).
- The sample Yen system buys or sells on closes breaking a set lookback period; other conditions were omitted from the extract (p. 4).
- MAE uses realized profit/loss versus drawdown to locate protective levels; the Yen illustration tests a 1.75% open unrealized-loss trigger (pp. 14-16).
- MFE uses run-up versus realized profit to locate additions; the Yen illustration adds one contract at 2.5% unrealized profit, while a later example adds two at 10% (pp. 17-19, 35-38).
- The fixed-fractional example reserves 20% of equity as trading capital and shows contract count rising as equity grows; its contract and margin assumptions are examples, not general settings (pp. 20-22, 38-39).
- Drawdown support adds to an open position at a tested loss level; the examples use $500-$1,000 as an observed recovery area and .25% as an illustrative trigger (pp. 23-25).

## Actionable rules

1. Analyze a signal system before applying money management; the workshop makes this a required preceding stage (p. 3).
2. Compare average trade, run-up, drawdown, and equity-curve stability across annual and monthly periods (pp. 6-10).
3. Reject a sizing method whose modeled drawdown exceeds the trader’s ability to continue executing it; no single risk percentage is prescribed (pp. 1-3).

## Caveats

This is a 1999 workshop with vendor-specific exhibits and incomplete strategy details. Claims about profitability depend on the supplied Yen and Corn systems and their test periods. MAE/MFE thresholds are fitted examples, and the extract does not provide enough trade-level data to reproduce all sizing experiments or judge out-of-sample performance (pp. 16-25, 34-39).

## Who it is for

Traders and system developers who need a risk-first evaluation process before optimizing returns.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: position-sizing, drawdown, expectancy, risk-management
