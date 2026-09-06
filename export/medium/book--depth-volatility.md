# Limit Orders, Depth, and Volatility: the trader's summary

*Academic study of the Hong Kong Stock Exchange finding transitory volatility and market depth move inversely, and volatility side determines limit-order flow direction.*

**Hee-Joon Ahn, Kee-Hong Bae & Kalok Chan** · 1999 · Quant, Microstructure & Academic Research · advanced

*Source coverage: partial. PDF pages inspected: 2-4 (the hypotheses and the regression results). These are study notes, not verified trading results.*

## Summary

Question: in a pure order-driven market with no designated market maker, how does short-term ("transitory") volatility interact with the depth of the limit-order book and the mix of limit versus market orders? Data: intraday trade and quote records (best five bid/ask queues, 30-second snapshots) for the 33 Hang Seng Index component stocks on the Stock Exchange of Hong Kong, July 1996–June 1997. Method: cross-sectional time-series regressions of upside and downside volatility on lagged bid/ask depth, buy/sell order-flow imbalance, and time-of-day dummies, averaged across the 33 stocks. Finding: consistent with Handa and Schwartz (1996), a rise in transitory volatility is followed by an increase in market depth, and a rise in depth is followed by a decline in subsequent volatility — the two variables self-correct. Volatility arising specifically from the bid side draws more limit buy orders (relative to market buy orders), while ask-side volatility draws more limit sell orders, consistent with liquidity providers stepping in on whichever side is currently paying for immediacy.

## Key points

- All liquidity in this market comes from public limit orders; there is no designated market maker (unlike NYSE or NASDAQ dealers).
- Hypothesis 1 (supported): higher transitory volatility → more limit-order submission → higher subsequent market depth.
- Hypothesis 2 (supported): higher market depth → lower subsequent transitory volatility.
- Effect is asymmetric by side: bid-side volatility spurs limit buy orders; ask-side volatility spurs limit sell orders.
- Regression coefficients on lagged "best depth" and "best 5 depths" are negative and statistically significant (t-stats in the −2 to −6 range) for both upside and downside volatility.
- Findings support the view that an order-driven market without market makers can be self-sustaining because natural liquidity suppliers step in exactly when liquidity is scarce.
- Sample: 33 most liquid HSI stocks, averaging 346–387 trades/stock/day, with average percentage bid-ask spread of about 0.39–0.47%.

## Actionable rules

None given as trading rules — this is a market-microstructure research paper, not a system. Practical takeaway for traders: in a pure limit-order market, expect a burst of short-term volatility to be met by an influx of resting limit orders that dampens follow-through volatility shortly after, and expect the side (bid or ask) generating the volatility to indicate where new liquidity/limit orders will appear next.

## Caveats

Findings are specific to the Hong Kong market structure (fully transparent, discriminatory-execution, price-time-priority electronic limit order book) in 1996–97 and may not generalize to dealer/specialist markets or to modern high-frequency environments with different order types (icebergs, hidden orders, co-located HFT).

## Who it is for

Quant researchers and microstructure-focused traders interested in the empirical dynamics between order-book depth and short-term volatility in electronic limit-order markets.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: market-microstructure, limit-orders, liquidity, volatility, order-driven-market, academic-research
