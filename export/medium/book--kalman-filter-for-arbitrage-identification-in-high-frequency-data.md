# A Robust Non-Linear Multivariate Kalman Filter for Arbitrage Identification in High Frequency Data: the trader's summary

*London Business School paper using a robust multivariate Kalman filter to detect FX triangular-arbitrage mispricings in erratic 1990s tick data.*

**P. J. Bolland and J. T. Connor** · 1995 · Quant, Microstructure & Academic Research · advanced

*Source coverage: partial. PDF pages inspected: 1-2, 16 (the triangular-arbitrage formulation and the worked outlier case study). These are study notes, not verified trading results.*

## Summary

Question: how can triangular FX arbitrage be identified in real time from irregularly-arriving, error-prone tick data? Data: second-by-second Reuters ticks for $/DM, £/$, and £/DM, 1993–1995. Method: the no-arbitrage identity (the three cross rates around a currency triangle must multiply to 1, or their logs sum to zero) is formulated as a state-space model. A multivariate Kalman filter, made robust via a neural-network-based estimator, treats real arbitrage as a statistical outlier against the fitted no-arbitrage relationship, producing an updated estimate of every cross rate each second regardless of whether a tick arrived. Finding: the filter separated genuine mispricings from noise and data corruption, produced continuous robust estimates through data gaps, and correctly identified a documented spurious price spike as an outlier rather than following it.

## Key points

- Triangular arbitrage: the product of the three exchange rates around the loop must equal 1; in logs this becomes a simple additive identity, suiting a linear state-space model.
- The filter's "state" is the log of each base-currency rate; "observations" are whichever ticks arrive that second, often an incomplete subset.
- Two noise sources are modeled separately: ordinary bid-ask/transaction-cost noise (an unprofitable band) and additive outliers (real mispricing or data corruption).
- Parameters are estimated via the EM algorithm to handle missing data from irregular tick arrival.
- Prior daily-data studies likely missed most intraday arbitrage; prior intraday studies needed simultaneous quotes across all three rates, which this model avoids.
- The filter handles non-linear (neural network) state-transition functions via point-wise linearization, not just linear autoregression.
- Case study: the filter flagged a spurious $/DM tick as an outlier (robust score ~4.65) and used pure prediction instead of following it, while instantly propagating a genuine DM/£ trade into its $/£ estimate.

## Actionable rules

None for retail trading — this is infrastructure for institutional/quant arbitrage desks. Takeaway: (1) linear arbitrage relationships can be monitored as a state-space/Kalman-filter estimation problem rather than by naive simultaneous-quote comparison; (2) a robust filter separating outliers from noise can maintain continuous "fair value" cross-rate estimates even with stale or missing quotes.

## Caveats

The 1993–1995 dataset predates modern electronic FX market structure by decades — costs, latency, and arbitrage competition have all changed. This is a methodology demonstration, not a profitability study: no realized P&L or execution-cost analysis is given, only that known mispricing events are correctly flagged as outliers. Some equations are rendered ambiguously in the source (OCR artifacts around subscripts/matrices).

## Who it is for

Quant researchers or FX arbitrage system builders wanting an early worked example of robust multivariate Kalman filtering for real-time cross-rate consistency checking on noisy tick data.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: kalman-filter, triangular-arbitrage, high-frequency-data, tick-data, forex, outlier-detection, neural-network
