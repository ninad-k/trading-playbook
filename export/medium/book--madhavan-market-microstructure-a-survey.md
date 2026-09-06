# Market Microstructure: A Survey: the trader's summary

*A broad review connects trading institutions, information, liquidity, price formation, and empirical tests of market microstructure.*

**Ananth Madhavan** · 2000 · Quant, Microstructure & Academic Research · advanced

*Source coverage: full. PDF pages inspected: 1-54. These are study notes, not verified trading results.*

## Summary

Madhavan surveys market microstructure as the study of how trading mechanisms and information shape prices, quantities, and transaction costs. The review contrasts dealer and order-driven markets, discusses asymmetric information and inventory risk, and summarizes empirical work on spreads, price discovery, volatility, and market design. Its central lesson is that observed prices and returns depend on the trading process as well as on fundamental information. The paper treats bid-ask spreads as compensation for several components, including order-processing costs, inventory exposure, and adverse selection, while emphasizing that the components vary by institution and data. It also reviews how order flow can reveal information and how trades may move prices temporarily or permanently.

## Key points

- Market structure determines who supplies liquidity, how orders interact, and how quickly information reaches prices.
- Dealer models emphasize inventory and information asymmetry; limit-order models emphasize order placement, execution, and book competition.
- Trade prices can differ from efficient values because of bid-ask bounce, discreteness, inventory, and asymmetric information.
- Signed order flow is useful for studying price impact and information revelation, but it is not itself a trading signal.
- Volatility, volume, spreads, and depth are jointly determined and should not be interpreted in isolation.
- Institutional comparisons require attention to sampling interval, quote conventions, and the distinction between quoted and effective spreads.
- Surveyed evidence separates permanent information impact from temporary liquidity or inventory impact; one cited block-trade study found one-way impact of -4.3% using a prior-day benchmark versus -10.2% using a three-week benchmark (pp. 15-16).
- The review reports that trading-hour return variance can be at least 20 times non-trading variance, while French and Roll attribute at most 12% of daily variance to the trading process itself (pp. 14-15).
- The network-externality discussion predicts that volume can consolidate in the lower-cost venue, while call auctions can aggregate information when uncertainty is high; upstairs block markets may persist because large traders seek less disclosure and lower impact (pp. 21-24).
- Limit-order models frame a trade-off between gains from uninformed liquidity demand and losses to informed traders; reducing the minimum tick can lower quoted spreads yet reduce liquidity away from the best quotes (pp. 25-26).
- The survey notes that individual market-liquidity regressions often have low explanatory power even when coefficients are significant, and cites evidence that upstairs trades’ price movements can precede execution by up to four weeks (pp. 27-29).
- Transparency has distributional effects: TSE public depth disclosure was followed by wider effective and percentage spreads in one cited study, while LSE delayed reporting produced little clear liquidity change after market-wide controls (pp. 35-37).
- The review links illiquidity to expected-return premia in classic studies, reports common factors in returns and order flow accounting for 50% of commonality in one cited analysis, and cautions that short-run predictability remains open (pp. 38-40).
- In FX, the “hot potato” model explains high turnover as dealers passing inventory through a low-transparency network; changing dealer structure or transparency could reduce the volume amplification (pp. 43-44).

## Actionable rules

1. When evaluating an execution, separate quoted spread, effective spread, realized spread, depth, and price impact; the survey’s framework treats these as different measurements.
2. Use trade direction and order-book state together when studying short-horizon price changes; a trade’s information and liquidity components can have opposite signs.
3. Specify the venue and market institution before transferring a microstructure result to another market.

## Caveats

This is a literature survey rather than a single forecast model or tested entry system. The cited results come from different markets and periods, so parameter values are not portable. Several conclusions are theoretical or based on studies with different controls; transparency can help one trader group while harming another (pp. 33-37). The assigned PDF’s extracted metadata is generic.

## Who it is for

Advanced readers who want a map of empirical and theoretical market-microstructure research.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: market-microstructure, price-discovery, liquidity, informed-trading
