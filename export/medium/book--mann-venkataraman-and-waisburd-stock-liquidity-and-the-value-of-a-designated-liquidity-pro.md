# Stock Liquidity and the Value of a Designated Liquidity Provider: Evidence from Euronext Paris: the trader's summary

*Event study of 56 Paris Bourse stocks finds a designated liquidity provider adds a 4%+ abnormal return for illiquid stocks by reducing auction failures, but does nothing for already-liquid stocks.*

**Steve Mann, Kumar Venkataraman, and Andy Waisburd** · 2002 · Quant, Microstructure & Academic Research · advanced

*Source coverage: partial. PDF pages inspected: 1-3, 10, 14, 27 (the event-study design and the auction-participation results). These are study notes, not verified trading results.*

## Summary

Question: does adding a designated liquidity provider (DLP) — a passive, non-strategic market maker with no informational edge, obligated only to quote a maximum spread and minimum depth — create measurable value in a purely electronic, order-driven market? Data: 56 Euronext Paris (formerly Paris Bourse) stocks that had a DLP introduced between 1995 and 1998, split into 19 "Liquid" stocks (continuous electronic limit order book) and 37 "Illiquid" stocks (twice-daily call auction). Method: an event study of cumulative abnormal returns (CAR) around the DLP announcement and introduction dates, followed by tests of market-quality changes (trading volume, depth, spreads, price impact) and, for the Illiquid sample, auction clearing-frequency logit regressions and cross-sectional regressions linking CAR to the change in market quality. Finding: Illiquid stocks show a statistically significant CAR of about 4.4% around DLP introduction (roughly 3% before announcement, drifting to 4.4% by ten days after introduction); Liquid stocks show no significant price effect at all.

## Key points

- Illiquid-sample CAR of 4.43% over the event window (five days before announcement to ten days after introduction) is significant at the 1% level; the Liquid sample's CAR is statistically indistinguishable from zero throughout.
- The DLP does not improve traditional liquidity metrics (trading volume, relative volume, quoted/effective spreads, quoted depth, price impact) for either sample — this is not where the value comes from.
- For the Illiquid (call-auction) sample, DLP introduction significantly raises the call-auction clearing frequency, from 79.2% to over 85% of sessions overall, and from 86.5% to 93.5% in morning sessions specifically (where information asymmetry is assumed highest).
- A logit regression confirms the clearing-frequency improvement holds after controlling for order flow and order imbalance — the DLP coefficient stays significantly positive.
- A share is more likely to execute when submitted in the presence of a DLP, especially in morning sessions; afternoon execution likelihood actually falls slightly post-DLP, plausibly because morning liquidity absorbs supply that would otherwise carry into the afternoon.
- Cross-sectionally, stocks whose auction-clearing frequency improved more after DLP introduction also earned larger abnormal returns — directly linking the liquidity-quality channel to the pricing effect.
- Results line up with Glosten (1989): the DLP's value comes from preventing market failure (auctions that fail to clear) in periods of thin liquidity, not from the NYSE-specialist-style role of narrowing spreads or deepening the book.
- The Paris DLP has no informational advantage and cannot condition price on incoming order flow, unlike an NYSE specialist — yet still adds value for illiquid names purely through consistent market presence.

## Actionable rules

None given — this is a market-structure event study, not a trading system. Practical takeaways for a trader: (1) the introduction or removal of a designated market maker/liquidity provider on a stock is more likely to matter for illiquid, thinly-traded names than for already-liquid ones; (2) for illiquid stocks trading via periodic call auctions, "does the auction clear" is a meaningful liquidity-risk signal distinct from spread or volume; (3) a stock's price can re-rate several percent around this kind of market-structure change, which is relevant context when such changes are announced.

## Caveats

Sample is small (19 and 37 stocks) and confined to the Paris Bourse/Euronext of the mid-1990s, a market structure (twice-daily call auctions for illiquid names, continuous ELOB for liquid names) that doesn't map directly onto most modern retail-accessible markets. The authors flag their own selection-bias concern: DLPs tend to be assigned to stocks expected to benefit, which could inflate the apparent gain, though they argue market anticipation partially offsets this for the event-study results. No discussion of transaction costs, execution strategy, or anything directly actionable for discretionary or systematic trading — this is a market-microstructure/asset-pricing research paper.

## Who it is for

Readers interested in market microstructure and how the presence of a market maker or liquidity provider affects price formation and execution quality, particularly for illiquid stocks — useful background for anyone evaluating designated market maker programs (e.g., NYSE DMMs, exchange liquidity-provider schemes) on modern exchanges.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: market-microstructure, liquidity-provider, limit-order-book, event-study, euronext, academic-research
