---
title: Market Liquidity and Trading Activity
author: Tarun Chordia, Richard Roll, and Avanidhar Subrahmanyam
year: 2001
slug: chordia-roll-and-subrahmanyam-market-liquidity-and-trading-activity
tier: B
category: Quant, Microstructure & Academic Research
tags: [market-microstructure, liquidity, bid-ask-spread, trading-volume, day-of-week-effect, academic-paper, nyse]
difficulty: advanced
doc_type: paper
pages: 30
one_liner: "Journal of Finance (2001) study of 11 years of NYSE data finding aggregate market liquidity and trading volume are highly volatile, decline sharply in down markets, and show strong day-of-week patterns (weak on Fridays, strong on Tuesdays)."
related: [chordia-roll-and-subrahmanyam-commonality-in-liquidity, anshumana-and-kalay-can-splits-create-market-liquidity-theory-and-evidence, liquidity-in-forex-markets, bangia-diebold-schuermann-and-stroughair-modeling-liquidity-risk-with-implications-for-tra]
source_file: "Chordia, Roll And Subrahmanyam -Market Liquidity And Trading Activity.pdf"
---

## Summary

Question: how does aggregate (market-wide) stock liquidity and trading activity vary over time, and what drives those day-to-day changes? Prior research had only studied liquidity at the individual-security level over short windows (a year or less); this paper is the first to study market-wide liquidity over a long span. Data: quoted/effective bid-ask spreads, market depth, share volume, dollar volume, and transaction counts for a comprehensive sample of NYSE stocks, daily, over 1988-1998 (~2,800 trading days, ~3.5 billion transactions from the ISSM and TAQ databases). Method: time-series description of the liquidity/volume series plus regressions of daily changes in liquidity and trading activity on interest rates, market returns/volatility, day-of-week dummies, holiday dummies, and macro-announcement dummies. Finding: aggregate spreads, depth, and volume are even more volatile than returns and are negatively serially correlated day to day; liquidity worsens sharply in down markets but only marginally improves in up markets; there are strong weekly and macro-announcement patterns.

## Key points

- Liquidity/volume measures examined: quoted spread, effective spread (both in dollars and % terms), quoted depth, dollar depth, a composite liquidity measure (%spread/$depth), share volume, dollar volume, and number of transactions.
- Aggregate spreads and depth show a secular trend over the sample: spreads declined and depth/volume rose over 1988-1998, with a structural break when the NYSE minimum tick size dropped from 1/8 to 1/16 in mid-1997.
- Daily changes in liquidity/volume are negatively serially correlated — a large change tends to partially reverse the next day.
- Down markets hurt liquidity asymmetrically: both quoted and effective spreads widen sharply on down days but narrow only slightly on up days; the "down-market" variable was the single most significant regressor found.
- Counter to intuition, recent market volatility tends to reduce (not widen) spreads in this sample.
- Short-term interest rates and the term spread significantly affect both liquidity and trading activity.
- Strong day-of-week effects: liquidity and trading activity decline on Fridays and around major holidays; Tuesdays show the opposite (elevated) pattern.
- Trading activity and depth rise just before scheduled macro announcements (GDP, unemployment) and fall back to normal on the announcement day itself, consistent with informed/uninformed trading dynamics ahead of news.
- The full regression model explains 18-33% of daily variation in liquidity and trading activity — a large residual remains unexplained.
- Authors caution the 1988-1998 sample was a persistent bull market; they explicitly flag that liquidity dynamics (especially the interest-rate and inventory channel) could behave differently in a sustained bear market.

## Actionable rules

None given as trading rules — this is a descriptive/explanatory academic study, not a system. What a trader can take from it: (1) expect execution costs (spreads) to widen disproportionately on down days — size orders or use limit orders more cautiously in falling markets; (2) expect thinner liquidity and wider spreads heading into Friday close and around holidays, and better liquidity on Tuesdays; (3) expect elevated volume/depth in the run-up to scheduled macro releases (GDP, unemployment), normalizing on the release day itself — useful for timing large orders around known announcement dates.

## Caveats

This is a rigorous, peer-reviewed academic paper (The Journal of Finance, Vol. LVI, No. 2, April 2001) built entirely on NYSE data from 1988-1998 — a specific market-structure era (fractional tick sizes for most of the period, pre-decimalization, pre-electronic/algorithmic trading dominance) whose day-of-week and liquidity patterns may not directly transfer to modern markets. The paper is explicitly "atheoretical" (empirical, not built to test one formal model) and the authors note as an open question whether these dynamics hold in bear markets, since the sample period was a prolonged bull run.

## Who it is for

Quantitatively-minded traders and researchers interested in the empirical behavior of market-wide liquidity, execution cost timing, and day-of-week/announcement effects on the NYSE.
