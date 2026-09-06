# Are Supply and Demand Driving Stock Prices?: the trader's summary

*Paris Bourse order-flow data shows order imbalance explains ~50% of return variance, with a higher R² for market-wide moves than stock-specific ones — pointing to mechanical price pressure, not just information.*

**Carl Hopman** · 2002 · Quant, Microstructure & Academic Research · advanced

*Source coverage: partial. PDF pages inspected: 5, 9, 12-13 (the price-impact estimation and the order-flow autocorrelation results). These are study notes, not verified trading results.*

## Summary

Question: does order-flow imbalance (supply and demand) drive stock returns, beyond what public information can explain? Data: complete limit-order submission data for 34 CAC40-era Paris Bourse stocks, 1995-1999 — an order-driven market with no market maker, so unrealized buy/sell intentions can be measured directly, unlike markets where realized volume nets to zero. Method: builds an order-flow imbalance measure (summing the square root of each order's volume by side, to capture the observed concave price impact of order size) and regresses returns on it across horizons from 10 minutes to 3 months, comparing R² for market-wide vs. idiosyncratic returns to separate private information from mechanical price pressure. Finding: order-flow imbalance explains about 50% of return variance for the average stock, with no reversal out to 3 months; R² is higher for market-wide returns (70%) than idiosyncratic ones (41%) — the opposite of what a pure private-information story predicts — implying a large role for uninformed, mechanical price pressure that can help explain bubble-like, mean-reverting swings.

## Key points

- Price impact of an order is a concave function of its volume (roughly volume^0.5), consistent with Hasbrouck (1991).
- Orders are split into market, spread, and book orders by urgency; more urgent orders have larger price impact for a given size.
- The order-flow measure aggregates orders via a square-root transform rather than raw volume or order count, and correlates best with returns.
- Order-flow imbalance is autocorrelated for 1-2 days (order splitting and/or herding), but the predictable component has almost no incremental price impact — consistent with an efficiently arbitraged market.
- Price impact of an order is not reversed later, holding across horizons from 10 minutes to 3 months.
- Campbell (1991) estimated only 33-50% of market-wide moves are due to fundamental news; this paper's 70% order-flow R² on the market factor exceeds that, implying orders help generate mean-reverting (bubble-like) moves, not just permanent information-driven ones.

## Actionable rules

None given — this is an academic empirical study, not a trading system. Practical takeaway: sustained one-directional order-flow imbalance tends to keep pushing price in the same direction rather than reverting in the short-to-medium term, and this holds for broad market-wide moves as well as single stocks.

## Caveats

Data is specific to the Paris Bourse (1995-1999), a pure limit-order market with no market makers; results may not transfer directly to dealer or hybrid markets. The order-flow measure uses submitted (not executed) orders and approximates cancellations, a limitation the author acknowledges. The paper is dense in econometric method (Box-Cox transforms, non-parametric kernel regression, block-bootstrap standard errors).

## Who it is for

Quant-minded traders and researchers interested in evidence for order-flow-driven price pressure and its role in bubble formation, as an alternative or complement to pure efficient-market explanations.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: order-flow, price-impact, market-microstructure, limit-order-book, bubbles, academic-paper
