# Competition Between Exchanges: Euronext versus Xetra: the trader's summary

*A matched comparison of 40 French-German stock pairs finds lower effective spreads and adverse selection on Xetra than Euronext Paris.*

**Maria Kasch-Haroutounian and Erik Theissen** · 2003 · Quant, Microstructure & Academic Research · advanced

*Source coverage: full. PDF pages inspected: 1-32. These are study notes, not verified trading results.*

## Summary

Kasch-Haroutounian and Theissen compare execution costs on two anonymous electronic limit-order books, Euronext Paris and Xetra. They match 40 French-German stock pairs using market capitalization, trading volume, and volatility, then analyze best quotes and transactions over 65 trading days from May 2 to July 31, 2002 (pp. 1–10). Quoted spreads are similar, but Xetra has lower effective spreads, adverse-selection components, and realized spreads. The authors test whether liquidity-provider agreements and minimum tick sizes explain the difference and find that they do not (pp. 1–4, 18–20).

## Key points

- The matched design controls for major observable liquidity drivers, but the authors acknowledge the pairs are not perfectly alike (pp. 4, 8–10).
- Full-sample quoted half spreads average 0.4258% in France and 0.4142% in Germany; the mean difference is not statistically significant (p. 29).
- Effective half spreads average 0.3298% on Euronext and 0.2876% on Xetra, a significant 0.0422 percentage-point difference (p. 29).
- Adverse-selection components average 0.3261% in France and 0.2738% in Germany, while realized spreads are also lower in Germany (p. 30).
- The analysis measures adverse selection using midpoint changes over a five-minute horizon (p. 30).
- Xetra’s fixed 0.01 euro tick and Euronext’s price-dependent ticks range from 0.01 below 50 euros to 0.50 above 500 euros (p. 7; Table I, pp. 23–26).
- Regression controls explain much of the spread difference through size, price, volatility, and transaction counts; liquidity-provider and tick-size indicators do not explain the main result (pp. 31–32).

## Actionable rules

1. None given. The paper evaluates venue quality and does not propose a directional trading system.
2. For execution research, compare effective spread and post-trade midpoint impact, not quoted spread alone; the study’s adverse-selection horizon is five minutes (p. 30).

## Caveats

The data are from 2002 and cover only 40 matched pairs and 65 trading days. No transaction-volume field is available, so transaction count is used as a proxy (p. 9). Venue rules, trading hours, tick sizes, and liquidity programs have since changed. The result is observational and does not prove that venue choice alone caused lower costs.

## Who it is for

Execution analysts, market makers, and traders comparing venues or studying how order-book design affects realized trading costs.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: market-microstructure, liquidity, spreads, execution, exchanges
