---
title: "Program Trading and Intraday Volatility"
author: "Lawrence Harris, George Sofianos, James E. Shapiro"
year: 1994
slug: harris-sofianos-and-shapiro-program-trading-and-intraday-volatility
tier: B
category: Quant, Microstructure & Academic Research
tags: [program-trading, index-arbitrage, volatility, liquidity, microstructure, s-and-p-500, academic]
difficulty: advanced
doc_type: paper
pages: 33
one_liner: "NYSE-affiliated researchers find program trades follow (more than lead) S&P 500 price moves and show little reversal, contradicting the claim that program trading destabilizes markets."
related: [frino-mcinish-and-toner-the-liquidity-of-automated-exchanges-new-evidence-from-german-bund, chordia-roll-and-subrahmanyam-market-liquidity-and-trading-activity]
source_file: "Harris, Sofianos And Shapiro-Program Trading And Intraday Volatility.pdf"
---

## Summary

Question: does program trading (especially index arbitrage) increase intraday volatility and drain liquidity from the cash stock market, as critics of computerized trading argued after the 1987 crash? Data: every intraday program trade reported by NYSE member firms in 1989–1990 (two full years), matched against one-minute S&P 500 futures and cash index returns; a June 1989 subsample with disaggregated stock-level quote data is used to isolate microstructure noise. Method: event-study regressions of index/futures returns on leads and lags of program-trade "episodes" (classified as index-arbitrage or non-arbitrage, buy or sell), plus a decomposition of the cash index into a bid-ask-bounce component, a stale-price (nonsynchronous trading) component, and a "true" midquote component. Finding: futures prices (and to a lesser extent cash prices) tend to lead program trades more than the reverse; index-arbitrage trades are followed by an immediate cash-index move that partially reverses, while non-arbitrage trades show no reversal; the relationship is stable across the two-year sample and not explained away by bid-ask bounce or stale pricing.

## Key points

- A $10 million program trade is associated with an average cumulative 30-minute S&P 500 move of about 0.03%; a $100 million trade implies roughly a 1-point move (linear extrapolation).
- Buy/sell program trades and index-arbitrage/non-arbitrage trades all show similar-magnitude cumulative associations with the index.
- Non-arbitrage program trades reach their final price impact quickly with no subsequent reversal.
- Index-arbitrage trades show stronger short-run co-movement with the index right after the trade, followed by a slight reversal; the cash-futures basis widens just before the trade and normalizes within about 10 minutes.
- The average program trade involved 172 stocks, virtually all bought or all sold together.
- A June 1989 decomposition shows bid-ask bounce and nonsynchronous (stale-price) trading are not economically significant contributors to the measured program-trading/index relationship.
- No major short-term liquidity problems were detected — the lack of large reversals implies most price change after a program trade reflects genuine new information.
- The October 1989 "minicrash" showed slightly higher-than-average reversals, particularly in futures.
- NYSE's program-trading definition used: simultaneous/near-simultaneous purchase or sale of 15+ stocks with aggregate value ≥ $1 million.

## Actionable rules

None given — this is an empirical study, not a trading system. What a trader can take from it: (1) program-driven index moves in this era were mostly information-driven, so fading them on a pure mean-reversion thesis had weak support; (2) the cash-futures basis reliably widens just ahead of index-arbitrage trades and normalizes within ~10 minutes; (3) findings apply only to trades occurring 30 minutes after the open and 5 minutes before the close — open/close program activity (e.g. expirations) was excluded.

## Caveats

A 1994 paper on 1989–1990 data, from a market-structure era (manual reporting, no modern circuit breakers) very different from today's algorithmic markets — magnitudes should not be extrapolated to current program trading. The linear-regression approach may not scale to much larger programs, and reversals beyond the studied 30-minute window are not ruled out.

## Who it is for

Quant researchers, academics, and market-structure-focused traders interested in the historical evidence on whether program/index-arbitrage trading destabilizes cash equity markets.
