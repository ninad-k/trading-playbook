# Testing for Micro-Structure Effects of International Dual Listings Using Intraday Data: the trader's summary

*Academic study finds dual-listing US stocks in London or Tokyo does not narrow bid-ask spreads because increased informed trading offsets the added market-maker competition.*

**Gregory M. Noronha, Atulya Sarin, Shahrokh M. Saudagaran** · 1996 · Quant, Microstructure & Academic Research · advanced

*Source coverage: partial. PDF pages inspected: 10 (the pre/post-listing spread and depth tables). These are study notes, not verified trading results.*

## Summary

Question: does listing a US (NYSE/AMEX) stock on a foreign exchange (London Stock Exchange or Tokyo Stock Exchange) improve its home-market liquidity, as competition theory would predict? Data: intraday quote and trade data (ISSM database) for 126 US stocks (68 subsequently listed on the LSE, 58 on the TSE) between 1983 and 1989, comparing 100-day windows before and after the foreign listing date (with a 50-day buffer excluded around the event). Method: compares median bid-ask spreads and quote depth pre/post listing (via Wilcoxon and binomial tests), then applies three established microstructure techniques — Hasbrouck's (1991) vector-autoregression measure of trade informativeness, Madhavan and Smidt's (1991) Bayesian weight-on-public-information model, and George, Kaul, and Nimalendran's (1991) adverse-selection-component decomposition — to test whether informed trading increased after dual listing, plus standardized volume/transaction-frequency/transaction-size comparisons. Finding: bid-ask spreads did not narrow after dual listing (and actually widened for the Tokyo sub-sample); quoted depth increased about 10% but that increase disappears once changes in price, volume, and return variance are controlled for. All three informed-trading measures point to an increase in informed trading after London listings (weaker/mixed evidence for Tokyo), which explains why increased market-maker competition failed to translate into tighter spreads — the higher adverse-selection cost of trading with better-informed counterparties offset the competitive pressure. Trading volume, transaction frequency, and average transaction size all rose significantly for the overall sample and the London sub-sample; the Tokyo sub-sample showed no significant volume increase.

## Key points

- Median relative bid-ask spread showed no significant change overall (0.615% pre vs. 0.679% post) or for LSE listings; it rose significantly for TSE listings (0.543% to 0.552%, z=1.96).
- Quoted depth rose significantly for the full sample and both sub-samples (~10% increase, all significant at 1%), but a cross-sectional regression controlling for price, volume, and return variance showed the depth increase was not attributable to the listing itself.
- Hasbrouck's summary informativeness measure (R²w) rose significantly after listing for the full sample (0.265→0.313) and LSE sample (0.210→0.288) but not significantly for TSE (0.304→0.335).
- Madhavan-Smidt's PRIOR statistic (weight on public information; lower = more informed trading) fell significantly for LSE listings (0.834→0.793) but rose slightly for TSE listings, an inconsistent result for Tokyo.
- George-Kaul-Nimalendran adverse selection component of the spread rose for the full sample (0.128→0.152) and LSE sample (0.168→0.195), with no significant change for TSE.
- Standardized daily trading volume, transaction frequency, and average transaction size all increased significantly for the full sample and LSE sub-sample post-listing; none of the three rose significantly for the TSE sub-sample.
- The authors attribute the weaker Tokyo results to generally thin trading of US stocks on the TSE (citing GM's 1992 delisting decision: ~1,300 shares/day average volume in Tokyo vs. 2.1 million on the NYSE) and structural differences (TSE as a centralized auction market, yen-denominated quotes requiring FX conversion).
- Overall conclusion: dual listing does not improve quote quality (spreads), but it does increase trading volume and information flow into the underlying stock, which may still improve market efficiency even without tighter spreads.

## Actionable rules

None given directly — this is an academic microstructure study, not a trading strategy paper. For a trader, the practical takeaway is: don't assume a foreign dual listing by itself will tighten a stock's home-market spread or improve execution cost; watch instead for the accompanying rise in trading volume and informed order flow, which can increase both opportunity and adverse-selection risk around the listing event.

## Caveats

Sample period (1983–1989) and market-structure assumptions (specialist-based NYSE/AMEX, SEAQ-International London quoting, TSE auction market) are specific to that era and predate decimalization, electronic order books, and modern market fragmentation, so the mechanisms described may not transfer directly to current markets. The Tokyo results are described by the authors themselves as weak and partly inconsistent across the three informed-trading measures used.

## Who it is for

Readers interested in academic market-microstructure research on cross-listing, liquidity, and information asymmetry — not a resource for discretionary or systematic trading rules.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: market-microstructure, bid-ask-spread, liquidity, dual-listing, informed-trading, academic-research
