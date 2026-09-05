---
title: Can Splits Create Market Liquidity? Theory and Evidence
author: V. Ravi Anshuman and Avner Kalay
year: 2002
slug: anshumana-and-kalay-can-splits-create-market-liquidity-theory-and-evidence
tier: B
category: Quant, Microstructure & Academic Research
tags: [stock-splits, market-microstructure, liquidity, tick-size, academic-paper, trading-volume]
difficulty: advanced
doc_type: paper
pages: 43
one_liner: "Journal of Financial Markets (2002) model and NYSE evidence arguing firms split their stocks to reach an optimal price level that maximizes liquidity by inducing traders to concentrate their trades in time, given fixed minimum tick sizes."
related: [chordia-roll-and-subrahmanyam-market-liquidity-and-trading-activity, chordia-roll-and-subrahmanyam-commonality-in-liquidity, liquidity-in-forex-markets]
source_file: "Anshumana And Kalay-Can Splits Create Market Liquidity - Theory And Evidence.pdf"
---

## Summary

Question: why do U.S. firms repeatedly split their stock to keep nominal share prices low (average U.S. stock price has stayed roughly constant for 50 years despite inflation), even though this raises their effective tick size (tick/price) and thus trading costs? Method: a market microstructure model in which liquidity traders differ in their cost of monitoring the market, and can choose to time trades into periods of low "discreteness related commissions" (the cost created by the exchange's fixed minimum price tick); the model is solved numerically, then tested on intraday NYSE TAQ transaction data for 2,173 stocks (August 1993, reduced to 1,796 after filters). Finding: an optimal share price level exists that maximizes the amount of "discretionary" (time-concentrated) trading and therefore minimizes total transaction costs; empirically, the coefficient of variation of trading volume (a measure of how concentrated/"lumpy" trading is in time) is significantly negatively related to a stock's price level — lower-priced stocks show more concentrated trading, consistent with the model.

## Key points

- Because U.S. exchange prices are restricted to fixed ticks (historically 1/8 dollar), a portion of every trade's cost is a pure artifact of price discreteness, unrelated to true supply/demand.
- Liquidity traders with low "monitoring costs" can save money by timing trades into periods when this discreteness cost happens to be low; traders with high monitoring costs cannot profitably do so and trade non-discretionarily.
- The more traders that concentrate into the same period, the lower the adverse-selection cost a market maker charges them (safety in numbers), reinforcing the incentive to cluster trades.
- Because tick size is fixed in nominal dollars, its economic bite is proportionally larger for low-priced stocks — so low-priced stocks see more concentrated ("lumpy") trading than high-priced stocks.
- The model's numerical solutions show the optimal share price rises with the underlying asset's volatility, falls as the fraction of liquidity (vs. informed) traders rises, and scales roughly linearly with tick size.
- Empirical test (Table 8): regressing volume-clustering measures (standard deviation and Herfindahl Index of intraday volume) on price level across ~1,800 NYSE stocks in August 1993 finds a statistically significant negative relationship — higher-priced stocks have smoother, less concentrated volume.
- Cites related evidence: post-split stocks show an increased coefficient of variation in trading volume (Anshuman and Goyal, 2001) and increased return volatility (Ohlson & Penman 1985; Lamoureux & Poon 1987; Koski 1998) — both consistent with the model's predictions.
- Discusses decimalization: if tick size fell from 1/8 to 1 cent, the model implies optimal prices would drop by a factor of ~12.5 (e.g., a $50 optimal price would become ~$4), predicting firms would use splits to re-target the new optimal range.

## Actionable rules

None given as trade entry/exit rules — this is a theoretical asset-pricing/microstructure paper, not a trading system. What a trader can take from it: (1) low-priced stocks should be expected to show more clustered, "lumpy" intraday volume patterns than high-priced stocks, purely as a mechanical consequence of tick size, not necessarily new information; (2) a stock split does not change fundamental value but can be expected to increase both volume clustering and short-term return volatility afterward, which matters for anyone trading around announced splits; (3) treat apparent liquidity/volume shifts after a split as partly mechanical rather than purely informational.

## Caveats

This is a formal, math-heavy peer-reviewed paper (Journal of Financial Markets, Vol. 5, 2002) built on a specific, now-largely-obsolete market structure — 1/8-dollar (and later 1/16, 1/32) minimum tick sizes that predate 2001 U.S. decimalization; the paper's own "Decimalization" section (Section 5.7) explicitly anticipates this regime change and predicts it would alter optimal split targets. The empirical test uses a single month of 1993 NYSE data and is a cross-sectional association (price level vs. volume clustering), not a controlled experiment proving splits caused liquidity gains for any individual firm. Large sections of the paper (Sections 2-4 and Appendices A-B) are numerical model derivations and proofs not reproducible here in narrative form.

## Who it is for

Quantitatively-minded readers and researchers interested in why companies split their stock and how nominal price level mechanically affects trading patterns.
