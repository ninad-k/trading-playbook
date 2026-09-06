---
title: "Commonality in Liquidity"
author: "Tarun Chordia, Richard Roll and Avanidhar Subrahmanyam"
year: 2000
slug: chordia-roll-and-subrahmanyam-commonality-in-liquidity
tier: B
category: Quant, Microstructure & Academic Research
tags: [liquidity, spreads, depth, market-risk]
difficulty: advanced
doc_type: paper
pages: 26
one_liner: "NYSE evidence shows quoted spreads, depth, and effective spreads co-move with market and industry liquidity after stock-level controls."
related: [madhavan-market-microstructure-a-survey, hollifield-miller-sandas-and-slive-liquidity-supply-and-demand-in-limit-order-markets]
source_file: "Chordia, Roll And Subrahmanyam -Commonality In Liquidity.pdf"
source_review: full
reviewed_pdf_pages: "1-26"
---
## Summary

Chordia, Roll, and Subrahmanyam examine whether liquidity is partly a market-wide and industry-wide phenomenon rather than only a property of one stock. Using NYSE transaction and quote data for 1992, they study quoted spreads, quoted depth, and effective spreads while controlling for stock-level volatility, volume, and price. The abstract reports significant and material common movements in all three liquidity measures (p. 1). The authors motivate this through correlated dealer inventories, market-wide volatility, institutional trading, and asymmetric information affecting several firms at once (pp. 2-4). The practical implication is that diversification of securities does not necessarily diversify liquidity risk.

## Key points

- Market and industry factors explain co-movement in liquidity beyond individual stock characteristics (p. 1).
- Inventory pressure and asymmetric information are proposed sources, while precise identification remains open (pp. 2-4).
- The 1992 data include every transaction, nearest preceding bid/ask, and specialist-guaranteed depth (p. 4).
- Quote data are matched using quotes at least five seconds before a transaction because of reporting delay (p. 4).
- In the 1,169-stock regressions, market and industry liquidity sums were positive and significant for quoted spread, proportional quoted spread, depth, and effective spread measures (Table 5, p. 15).
- Individual trading frequency raised spread measures, market-wide volume generally reduced spreads, and industry volume tended to increase spreads, consistent with mixed inventory and informed-trading effects (pp. 17-20).
- Liquidity shocks can affect liquidation across otherwise unrelated positions (p. 3).
- After filtering, the study retains 1,169 NYSE equities, 29,655,629 transactions, and 289,612 stock-days; mean quoted spread is $0.3162, mean effective spread $0.2245, and mean quoted depth 3,776 shares (pp. 5-6, Table 1).
- Daily proportional changes are volatile: the mean absolute change is about 24% for quoted spreads and about 78% for depth (p. 7, Table 2).
- Individual-stock regressions have low average adjusted R2, generally below 2%, despite statistically strong market co-movement; size-quintile results show larger spread sensitivities for larger firms (pp. 9-12, Tables 3-4).
- Cross-sectional controls show industry liquidity remains significant alongside stock volatility, price, and dollar volume (p. 21, Table 9), while portfolio regressions raise adjusted R2 to 0.552 for proportional quoted spreads and 0.811 for depth (p. 22, Table 10).

## Actionable rules

1. Monitor market and industry liquidity conditions alongside each security’s own spread and depth (pp. 1-3).
2. Include liquidity stress as a common risk factor when estimating portfolio exit costs.
3. Preserve the paper’s five-second quote-matching convention when reproducing its 1992 transaction study (p. 4).

## Caveats

The evidence is historical NYSE data and cannot provide current coefficients. Buyer and seller identities and specialist inventories are not directly observed, so the paper documents commonality more strongly than it identifies one causal mechanism (pp. 3-4, 12, 19). Individual adjusted R2 values are small even where coefficients are significant; portfolio results are stronger but still do not imply a forecast of future spreads (pp. 10, 22).

## Who it is for

Quantitative researchers and portfolio traders studying market-wide execution risk.
