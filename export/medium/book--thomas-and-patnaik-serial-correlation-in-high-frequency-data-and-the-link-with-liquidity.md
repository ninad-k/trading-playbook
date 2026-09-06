# Serial Correlation in High-Frequency Data and the Link with Liquidity: the trader's summary

*Variance-ratio tests on Indian equities find five-minute mean reversion whose speed differs with liquidity and trading intensity.*

**Susan Thomas and Tirthankar Patnaik** · 2002 · Quant, Microstructure & Academic Research · advanced

*Source coverage: full. PDF pages inspected: 1-26. These are study notes, not verified trading results.*

## Summary

Thomas and Patnaik test high-frequency market efficiency in Indian equities using variance-ratio tests on the NSE Nifty index and 100 liquid stocks. At five-minute intervals, all sampled stocks show negative serial correlation and mean reversion, but the time required to revert differs across firms (p. 1). The introduction reports a shortest reversion time of ten minutes and a longest spanning several days (p. 4). The authors relate the pattern to bid-ask bounce and trade-impact mechanics: wider spreads can produce larger short-horizon serial correlation for a given depth (p. 4). The index does not show the expected significant positive serial correlation at five minutes, suggesting asynchronous trading is not enough to explain the index result at that interval (p. 4).

## Key points

- The study uses five-minute returns and variance-ratio methodology (pp. 1, 3-4).
- Individual-stock behavior is heterogeneous even among the most liquid 100 stocks (p. 4).
- Liquidity is measured with impact cost and trading intensity (p. 1).
- High-frequency tests require controls for heteroskedasticity, asynchronous observations, and changing data-generating processes (pp. 3-4).
- Statistical mean reversion may be a microstructure effect rather than an exploitable forecast after costs.
- The sample covers March 1999-February 2001 NSE data, uses 300-second intervals, and selects 100 stocks; the selected stocks represent about 83.32% of recorded trades (pp. 11-12).
- Nifty’s apparent five-minute serial correlation became insignificant after accounting for intraday heteroskedasticity, while individual stocks showed negative dependence whose persistence varied with liquidity (pp. 13, 16-20).

## Actionable rules

1. Before interpreting intraday mean reversion, measure spread, impact cost, and trading intensity for the exact security (pp. 1, 4).
2. Use variance-ratio inference appropriate to high-frequency heteroskedastic data; daily-market assumptions may fail (p. 3).
3. Compare signal magnitude with fees, spread, and execution delay before treating five-minute dependence as a trade.

## Caveats

The sample is Indian equities and historical. The paper’s detected serial correlation may reflect bid-ask bounce, intraday volatility seasonality, or other microstructure effects rather than fundamental predictability.

## Who it is for

Researchers evaluating intraday efficiency and liquidity-linked return dependence.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: high-frequency, mean-reversion, liquidity, variance-ratio
