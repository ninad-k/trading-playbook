# Price Discovery and Trading After Hours: the trader's summary

*Academic study of the 250 largest Nasdaq stocks finding most after-hours price discovery happens in the preopen via ECNs, with postclose trades noisy and often reversed.*

**Michael J. Barclay and Terrence Hendershott** · 2003 · Quant, Microstructure & Academic Research · advanced

*Source coverage: partial. PDF pages inspected: 5, 7-8, 13, 15-16 (the sample description and the price-discovery decomposition). These are study notes, not verified trading results.*

## Summary

Published in the *Review of Financial Studies* (2003), this paper asks how much new information gets priced in outside the 9:30am-4:00pm Nasdaq trading day, and where. Using NASD trade/quote data for the 250 highest-volume Nasdaq stocks from March-December 2000, the authors split the 24-hour day into preopen (8:00-9:30am), trading day, postclose (4:00-6:30pm), and overnight, and apply the Easley-Kiefer-O'Hara (EKO) structural model to estimate the probability of an informed trade (PIN) in each window, plus a "weighted price contribution" (WPC) measure of how much of the close-to-open return each window explains.

## Key points

- Only about 4% of Nasdaq trading volume occurs after hours, concentrated right after the close and right before the open; overnight (after ~6:30pm) trading is minimal.
- The probability of an informed trade (PIN) is higher in the preopen (~25% average) and postclose (~21%) than during the regular trading day (~13%).
- 74% of close-to-open price discovery happens in the preopen, versus only 15% in the postclose and 9% at the actual opening trade.
- Preopen price discovery and volume both start in the highest-volume stocks and spread later to lower-volume names; by 8:45am, ~50% of preopen price discovery has occurred in top-quintile stocks vs. <10% in the bottom quintile.
- Individual trades are far more informative per trade in the preopen (weighted price contribution per trade of ~16-20x) than during the trading day (WPCT <1), because preopen volume is thin but informationally loaded.
- Postclose trading is dominated by market makers (mainly Knight Securities in the sample) negotiating with liquidity traders who need to rebalance overnight positions; preopen trading and virtually all preopen price discovery occurs on ECNs, favored by informed traders for speed and anonymity.
- Postclose price changes are noisy and frequently reversed the next day (low signal-to-noise ratio); preopen prices are noisy too, but less so than postclose.
- After-hours trades are roughly 2-3x larger on average than regular-session trades.

## Actionable rules

None given — this is descriptive academic research, not a trading system. Practical takeaways a trader can extract: (1) price moves that occur in the postclose session carry a meaningfully higher chance of reversing than moves in the preopen or regular session, so don't treat postclose price action as reliable confirmation; (2) if trading around overnight news, expect the preopen — not the postclose — to carry most of the pre-market price discovery, and expect that discovery to appear first in the most liquid names; (3) after-hours liquidity is thin and dominated by professional/institutional flow, so retail-sized after-hours orders face wide spreads and higher effective costs.

## Caveats

Data is from Nasdaq stocks in 2000, before decimalization was complete and before modern extended-hours retail access and dark-pool fragmentation existed — the specific magnitudes (e.g., 4% of volume after hours) are dated, though the underlying mechanism (informed traders prefer preopen/ECN, liquidity traders prefer postclose/dealers) is likely still directionally relevant. Requires familiarity with market-microstructure concepts (PIN, bid-ask spread decomposition) to follow the methodology.

## Who it is for

Quant researchers and advanced traders interested in market microstructure, extended-hours trading behavior, or building models of when informed trading concentrates during the day.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: market-microstructure, after-hours-trading, price-discovery, nasdaq, informed-trading, ecn, academic-paper
