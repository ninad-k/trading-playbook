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

Question: why do U.S. firms repeatedly split their stock to keep nominal share prices low (the average U.S. stock price has stayed roughly constant for 50 years despite inflation), even though this raises their effective tick size (tick/price) and trading costs? Method: a microstructure model where liquidity traders differ in their cost of monitoring the market and can time trades into periods of low "discreteness related commissions" (the cost created by a fixed minimum price tick); solved numerically, then tested on intraday NYSE TAQ data for ~1,800 stocks (August 1993). Finding: an optimal share price exists that maximizes time-concentrated ("discretionary") trading and minimizes total transaction costs; empirically, the coefficient of variation of trading volume is significantly negatively related to price level — lower-priced stocks show more clustered trading, matching the model.

## Key points

- Because U.S. exchange prices are restricted to fixed ticks (historically 1/8 dollar), part of every trade's cost is a pure artifact of price discreteness, unrelated to supply/demand.
- Low-monitoring-cost traders can save money by timing trades into low-discreteness-cost periods; high-monitoring-cost traders cannot do so profitably and trade non-discretionarily.
- The more traders concentrate into one period, the lower the adverse-selection cost a market maker charges (safety in numbers), reinforcing the clustering incentive.
- Since tick size is fixed in nominal dollars, its bite is proportionally larger for low-priced stocks, so they show more clustered ("lumpy") trading than high-priced stocks.
- Numerical solutions: optimal price rises with volatility, falls as the fraction of liquidity (vs. informed) traders rises, and scales roughly linearly with tick size.
- Empirical test (Table 8): volume-clustering measures regressed on price level across ~1,800 NYSE stocks (Aug. 1993) show a significant negative relationship — higher-priced stocks have smoother volume.
- Cited corroborating evidence: post-split stocks show increased volume clustering (Anshuman & Goyal 2001) and increased return volatility (Ohlson & Penman 1985; Lamoureux & Poon 1987; Koski 1998).
- Decimalization discussion: cutting tick size from 1/8 to 1 cent implies optimal prices would fall ~12.5x (e.g. $50 to ~$4), predicting firms would re-split to the new optimal range.

## Actionable rules

None given as entry/exit rules — this is a theoretical microstructure paper, not a trading system. Takeaways: (1) low-priced stocks mechanically show more clustered intraday volume than high-priced stocks, independent of new information; (2) a split doesn't change fundamental value but can be expected to raise volume clustering and short-term volatility afterward; (3) treat post-split liquidity/volume shifts as partly mechanical, not purely informational.

## Caveats

A math-heavy peer-reviewed paper (Journal of Financial Markets, Vol. 5, 2002) built on a now-largely-obsolete market structure — 1/8-dollar (later 1/16, 1/32) minimum ticks that predate 2001 U.S. decimalization; the paper's own decimalization discussion anticipates this regime change. The empirical test uses one month of 1993 data and is a cross-sectional association, not proof splits caused liquidity gains for any individual firm. The model derivations and proofs (most of the paper) are not reproducible here in narrative form.

## Who it is for

Quantitatively-minded readers and researchers interested in why companies split their stock and how nominal price level mechanically affects trading patterns.
