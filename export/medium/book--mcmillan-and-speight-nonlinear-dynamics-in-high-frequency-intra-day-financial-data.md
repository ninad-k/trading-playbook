# Nonlinear Dynamics in High Frequency Intra-Day Financial Data: the trader's summary

*STAR models of UK long-gilt futures find short-horizon nonlinearities that fade for larger moves and after friction costs.*

**David G. McMillan and Alan E. H. Speight** · 1999 · Quant, Microstructure & Academic Research · advanced

*Source coverage: full. PDF pages inspected: 1-30. These are study notes, not verified trading results.*

## Summary

McMillan and Speight test whether conditional mean dynamics in high-frequency UK long-gilt futures returns are linear. Using five- and fifteen-minute data, they test and estimate smooth-transition autoregressive models, then check robustness with asymmetric EGARCH and component-GARCH variance specifications. The abstract reports nonlinearities at both frequencies: the five-minute model is first-order autoregressive with a switching intercept, while the fifteen-minute model is autoregressive near zero and close to a random walk for large returns (p. 1). The interpretation is consistent with transaction costs and arbitrage activity: small deviations can show short-lived predictability, while larger opportunities are rapidly removed. The authors therefore confine any regularity to fine intervals and small price movements.

## Key points

- The model allows dynamics to change smoothly with lagged returns rather than using one fixed AR coefficient (pp. 3-7).
- Market frictions create a band around equilibrium in which arbitrage may not be profitable (pp. 4-6).
- The nonlinear mean survives controls for asymmetric and component conditional variance in the reported summary (p. 1).
- Five-minute and fifteen-minute frequencies show different transition behavior (p. 1).
- Large moves are less predictable because profitable deviations are extracted quickly (p. 1).
- The result concerns conditional mean structure, not a guaranteed trading edge.
- The sample is UK Long Gilt futures on LIFFE from 24 January 1992 through 30 June 1995: 846 trading days yield 80,163 five-minute and 26,721 fifteen-minute observations after excluding overnight returns (pp. 10-11).
- Returns are standardized by the mean absolute value for each intraday interval to address opening/closing periodicity and news effects; distributions remain peaked and show friction-consistent shoulders (pp. 11-12).
- Linearity tests reject a simple AR description at both frequencies and support STAR models; the authors evaluate models with information criteria, residual ARCH checks, and simulated dynamic behavior (pp. 13-15).
- At five minutes, the ESTAR-EGARCH result retains negative autocorrelation in the central and outer regimes, with a near-zero equilibrium and adjustment in roughly 11 periods or 55 minutes; the reported threshold is around 1.75 interval norms (p. 16).
- The fifteen-minute results identify a central regime and near-random-walk behavior for larger returns; the estimated threshold regions and volatility components differ from the five-minute model (pp. 17-23).
- The paper reports that conditional variance has transitory and permanent components, with the permanent component’s shock half-life around 10 days and the transitory component around one hour in the reported estimates (pp. 19-23).

## Actionable rules

1. If modeling intraday returns, test linearity before assuming a single AR process; the paper uses STAR/ESTAR alternatives (pp. 3-7).
2. Include transaction costs and sampling interval when judging small return predictability; a signal smaller than frictions is not actionable (pp. 4-6).
3. Do not extrapolate the five- or fifteen-minute result to daily data; the paper motivates the phenomenon as frequency dependent (pp. 2-4).

## Caveats

This is an empirical model of one UK futures market and a historical sample. The nonlinear estimates are model- and interval-specific, and adjusted returns, transaction costs, and market microstructure may not transfer. Nonlinearity does not imply stable directional profits or a positive net return after costs (pp. 10-23).

## Who it is for

Quant researchers studying intraday predictability, nonlinear time series, and market-friction effects.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: high-frequency, futures, nonlinear-models, volatility
