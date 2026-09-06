---
author: Alex Frino, Thomas H. McInish, Martin Toner
category: Quant, Microstructure & Academic Research
difficulty: advanced
doc_type: paper
one_liner: An academic study finds bid-ask spreads on the automated DTB were narrower
  than on floor-traded LIFFE for German Bund futures in 1997, contradicting older
  research.
pages: 17
related:
- harris-sofianos-and-shapiro-program-trading-and-intraday-volatility
- chordia-roll-and-subrahmanyam-market-liquidity-and-trading-activity
reviewed_pdf_pages: 10, 12 (the descriptive-statistics and regression tables)
slug: frino-mcinish-and-toner-the-liquidity-of-automated-exchanges-new-evidence-from-german-bund
source_file: Frino, Mcinish And Toner-The Liquidity Of Automated Exchanges - New Evidence
  From German Bund Fut.pdf
source_review: partial
tags:
- market-microstructure
- liquidity
- bid-ask-spread
- futures
- automated-trading
- open-outcry
- academic
tier: B
title: 'The Liquidity of Automated Exchanges: New Evidence from German Bund Futures'
year: 1998
---

## Summary

Question: is an automated electronic exchange less liquid than a traditional open-outcry floor, as widely claimed? Data: intraday trade and quote data for the Bund futures contract, simultaneously traded on Germany's automated Deutsche Terminbörse (DTB) and London's floor-based LIFFE, over 30 trading days (14 October–24 November 1997), a period when the two exchanges' market shares were closer than in prior studies. Method: time-weighted quoted bid-ask spreads are compared directly and via regression, controlling for trading activity (number of trades) and price volatility (standard deviation of quote midpoints), using the McInish-Wood (1992) determinants-of-spread framework with Newey-West adjusted standard errors. Finding: contrary to older studies (Kofman & Moser 1997, Shyy & Lee 1995, Franke & Hess 1995, Pirrong 1996), spreads were narrower on the automated DTB than on the floor-based LIFFE, even after controlling for volume and volatility differences.

## Key points

- Mean 5-minute quoted spread: DTB 0.0100 points vs. LIFFE 0.0105–0.0110 points; LIFFE spreads run about 9% (2.25 DM) wider after controlling for trading activity and volatility.
- The LIFFE dummy coefficient is positive and statistically significant (t = 4.03), confirming wider LIFFE spreads aren't just an artifact of differing volume/volatility.
- Spreads on both exchanges rise with price volatility and fall as trade count increases, consistent with prior microstructure literature.
- DTB spreads widen faster than LIFFE's as volatility rises, meaning the automated exchange's liquidity advantage shrinks in high-volatility periods.
- Spreads, trading activity, and volatility are all elevated at the open and close on both exchanges (intraday U-shape).
- At the very open, LIFFE spreads were briefly narrower than DTB's — the one reversal, possibly tied to DTB's call-market opening mechanism.
- Robustness checks (morning/afternoon partitions, trade-size proxies) did not change the core finding.
- Four candidate explanations proposed: DTB's trader anonymity, fuller order-book depth transparency, strict price/time priority (vs. LIFFE's per-trade "new auction"), and its call-market open.

## Actionable rules

None given — this is an academic microstructure study, not a trading system. Takeaways: (1) don't assume an electronic venue is automatically less liquid than a floor-traded one — check quoted spreads directly; (2) expect automated-venue spreads to deteriorate disproportionately in high-volatility windows relative to floor markets; (3) expect wider spreads at the open/close on both venue types, suggesting lower execution costs mid-session.

## Caveats

A 1998 paper using 1997 Bund futures data from now-merged exchanges (DTB became Eurex; LIFFE was absorbed into ICE) — findings are of historical/methodological interest rather than directly applicable today. The sample is only 30 trading days and one instrument; average trade size, a known spread determinant, could not be included for LIFFE due to data limitations.

## Who it is for

Quant researchers and market-structure students interested in the liquidity trade-offs between electronic and floor-traded execution venues, and in the historical debate over exchange automation.
