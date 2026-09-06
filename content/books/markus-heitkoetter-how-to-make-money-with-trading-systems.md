---
title: "How to Make Money with Trading Systems"
author: "Markus Heitkoetter"
year: unknown
slug: markus-heitkoetter-how-to-make-money-with-trading-systems
tier: B
category: Trend Following & Mechanical Systems
tags: [systems, backtesting, entries, exits, futures]
difficulty: intermediate
doc_type: manual
pages: 28
one_liner: "A system-building guide moves from market and timeframe selection through rules, evaluation, improvement, and ten operating principles."
related: [choosing-a-trading-system-that-actually-works, position-sizing]
source_file: "Markus Heitkoetter - How To Make Money With Trading Systems.pdf"
source_review: full
reviewed_pdf_pages: "1-28"
---
## Summary

Heitkoetter’s guide proposes five steps: select a market and timeframe, define entry rules, define exits, evaluate the system, and improve it (p. 3). It distinguishes trend-following entries from swing entries and says indicators should be understood by what they measure rather than collected indiscriminately (p. 4). Exit rules should protect capital and take profits; the guide lists fixed dollars, a percentage of price, a percentage of volatility, and a time stop as possible forms (p. 5). Its ten principles emphasize simple rules, liquid electronic markets, balanced risk and reward, at least five trades per week, starting small, automation, and testing on at least 200 trades (pp. 16-19).

## Key points

- Shorter timeframes generally offer more opportunities but lower average profit per trade; longer timeframes offer fewer trades and potentially larger drawdowns (p. 3).
- Swing and trend systems have different holding and discipline demands (p. 4).
- A backtest needs a valid period and enough trades to evaluate behavior (pp. 18-19).
- The author treats winning percentage as insufficient without risk-reward context.
- The sample Bollinger-band system sells above and buys below the bands, then exits at the same-day close; the author reports $13,525 net profit, $149 average trade, 2.20 profit factor, 66% winners, and $2,775 end-of-day drawdown versus $5,250 intraday drawdown (pp. 9-12).
- Varying the moving-average setting from 29 to 39 changes reported profit factor from 1.80 to 2.24 and maximum drawdown from $3,150 to $3,438, while the author presents these results as a robustness check (p. 12).
- Across five markets, reported profit factors range from 1.43 to 2.08 and maximum drawdowns from $1,490 to $6,350 under original settings; the modified second-day exit changes outcomes materially by market (pp. 13-15).
- In the sample, tested protective stops reduce net profit relative to no stop, while the two-day exit has the strongest reported aggregate result; these are backtest results for one rule set, not a general stop or holding prescription (pp. 14-15).
- System override and periodic evaluation are addressed in the closing chapters (pp. 22-28).

## Actionable rules

1. Specify entry, protective exit, profit exit, and any time stop before testing (pp. 3-5).
2. Prefer liquid electronic markets when execution and commission conditions matter (p. 3).
3. Evaluate at least 200 trades before trusting a system’s statistics, as the guide’s principle states (p. 19).

## Caveats

These are author guidelines and one vendor-style backtest, not independently validated laws. The five-trades-per-week and 200-trade figures are heuristics. The sample’s results vary by market and exit choice, and the document does not establish live profitability after current fees, slippage, or regime changes (pp. 12-15).

## Who it is for

Traders building or auditing rule-based systems and learning the difference between a backtest and a trading plan.
