---
title: "Overnight Information and Intraday Trading Behavior: Evidence from NYSE Cross-Listed Stocks and Their Local Market Information"
author: "Kalok Chan, Mark Chockalingam, Kent W.L. Lai"
year: 2000
slug: chan-chockalingam-and-lai-overnight-information-and-intraday-trading-behavior-evidence-fro
tier: B
category: Quant, Microstructure & Academic Research
tags: [market-microstructure, intraday-volatility, overnight-returns, cross-listed-stocks, academic-research, opening-volatility]
difficulty: advanced
doc_type: paper
pages: 15
one_liner: "Academic study finding NYSE opening-hour volatility in foreign cross-listed stocks tracks overnight local-market returns, but opening trading volume does not."
related: [hedge-fund-risk-factors-and-value-at-risk-of-credit-trading-strategies]
source_file: "Chan, Chockalingam And Lai-Overnight Information And Intraday Trading Behavior - Evidence From Ny.pdf"
---

## Summary

Published in the Journal of Multinational Financial Management (2000), this paper asks whether elevated trading activity in the first minutes after the NYSE opens for foreign cross-listed stocks (UK and Asia-Pacific names) is explained by overnight information accumulating in the stock's home market. Using NYSE Trades and Quotes (TAQ) intraday data plus local-market closing prices for Q1 1993 (21 UK stocks, 7 Asia-Pacific stocks), the authors regress NYSE intraday returns and volume in 30-minute intervals on local-market price innovations (local close-to-close returns, purged of the prior US trading session's effect). Method: split the NYSE session into 14 intervals (overnight/open-to-10am, then 30-minute blocks), estimate the sensitivity (beta) of each interval's price movement and volume to local overnight information, and test whether that sensitivity declines through the day. Finding: local overnight price movements strongly predict the NYSE open-to-10am return (and, for UK stocks with 2 hours of session overlap, up to 10:30-11:00am) but the effect fades quickly afterward, explaining why price volatility is highest at the open and lower by midday; local information has no significant relationship with NYSE trading volume at any interval, whereas volume is instead strongly tied to same-day NYSE opening price volatility, implying that intraday volume for foreign stocks reflects US investor liquidity trading more than overseas information flow.

## Key points

- **Sample** — 21 UK cross-listed stocks (2-hour London/NYSE session overlap) and 7 Asia-Pacific stocks (local markets close before NYSE opens), NYSE TAQ data plus EXTEL/local prices, January-March 1993.
- **Price-volatility result** — the beta on local overnight price innovation is highest and most significant in the close-to-open and open-to-10:00am intervals, then decays toward zero by roughly 11:00am-12:30pm.
- **Volume result** — local overnight price innovation is not a significant explanator of NYSE intraday trading volume for either UK or Asia-Pacific stocks.
- **What does explain volume** — same-day NYSE opening price volatility (a proxy for incremental US-specific information/liquidity trading) is a strong, significant driver of subsequent intraday volume; local price volatility is not.
- **Interpretation** — the pattern of high volatility/high volume at the open and calmer midday trading is driven by two separate causes: overnight foreign information for the volatility spike, and US liquidity trading for the volume spike.
- **Methodology note** — because local close-to-close returns partly reflect the prior US trading session, the authors estimate local overnight "innovations" as the residual of local returns regressed on the prior day's US session return, then use that residual (not the raw local return) in the main regressions.

## Actionable rules

None given directly, but the implications for traders: (1) expect the sharpest reaction to overnight news in a cross-listed/ADR-type name to occur in the first 30-60 minutes after the US open, with the effect largely dissipated within about an hour for Asia-Pacific-linked names and up to mid-morning for UK-linked names with overlapping sessions; (2) don't expect elevated opening-hour volume in such names to be explained by the size of overnight foreign price moves — use domestic (NYSE) opening volatility/liquidity signals instead when anticipating volume; (3) informational edge from overnight foreign price action decays quickly and is largely priced in by mid-morning.

## Caveats

Academic microstructure paper with a small, dated sample (21+7 stocks, one quarter of 1993 data) predating decimalization, electronic/algorithmic trading, and modern ADR/cross-listing structures; findings on volume vs. volatility drivers may not generalize to current market microstructure. Written for an academic audience with regression tables and formal hypothesis tests rather than a trading-strategy framework.

## Who it is for

Quant researchers or advanced traders interested in market-microstructure evidence on how overnight foreign information versus domestic liquidity trading separately drive opening-hour volatility and volume in cross-listed stocks.
