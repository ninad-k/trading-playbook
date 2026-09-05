---
title: "NDR Crowd Sentiment Indicators (Contrarian Extremes)"
author: Ned Davis
year: 2004
slug: mcgraw-hill-the-triumph-of-contrarian-investing-crowds-manias-and-beating-the-market-by-go--ndr-crowd-sentiment-indicators
tier: A
category: Investing, Value & Market History
tags: [sentiment-indicators, contrarian-investing, market-timing, valuation]
difficulty: intermediate
doc_type: system
parent: mcgraw-hill-the-triumph-of-contrarian-investing-crowds-manias-and-beating-the-market-by-go
pages: 194
one_liner: "A set of quantified sentiment indicators with stated overbought/oversold thresholds for taking contrarian long/short or long/cash positions in the S&P 500."
related: []
source_file: "Mcgraw-Hill, The Triumph Of Contrarian Investing - Crowds, Manias, And Beating The Market By Goin.pdf"
---

## What it is

A family of related sentiment-timing indicators, developed by Ned Davis Research (NDR), that convert survey data, fund-flow data, and futures positioning into a single bullish-percentage reading, then flag "excessive optimism" or "excessive pessimism" once that reading crosses a back-tested threshold. The underlying logic is the same across all of them: when a large majority of a given group (individual investors, newsletter writers, leveraged-fund investors, futures speculators) is already positioned or opinionated one way, there is little incremental buying or selling power left to extend the move, and historically the market has performed better than average after pessimism extremes and worse than average after optimism extremes. The indicators are meant to be combined (the book's own composite, the NDR Crowd Sentiment Poll, averages seven of them) and paired with a trend filter rather than traded individually or purely on a threshold cross.

## Rules

For each indicator, compute the stated ratio, compare it to the fixed or dynamic threshold, and treat a crossing as an "extreme" flag rather than an automatic trade trigger:

| Indicator | Data source | Extreme pessimism (bullish signal) | Extreme optimism (bearish signal) |
|---|---|---|---|
| AAII sentiment | American Association of Individual Investors weekly survey; % bullish of (bullish+bearish), 2-week average | below 44% | above 61% |
| Investors Intelligence advisors, falling-rate regime | Newsletter writer poll; bulls/(bulls+bears) | below 51% | above 81% |
| Investors Intelligence advisors, rising-rate regime | same poll | below 31% | above 58% |
| Rydex bull/bear fund assets | Assets in leveraged/inverse index funds; bull assets / (bull+bear assets) | below 51% | above 82.5% |
| COT Speculator Index (S&P futures) | CFTC noncommercial net position as % of trailing 78-week range, 6-week smoothed | below 40% | above 60% |
| NDR Crowd Sentiment Poll | Composite of 7 sentiment series | decline below 55.5% (with 10-point reversal to confirm) | rise above 61.5% (with 10-point reversal to confirm) |
| S&P 500 P/E | Trailing 12-month reported earnings | below 9.3 | above 20.2 |
| Bond yield / earnings yield | 10-yr Treasury yield ÷ S&P 500 earnings yield | 1.2 and below (favors stocks) | 1.45 and above (favors bonds) |

**Regime switch (Investors Intelligence example).** Determine whether short-term interest rates are currently in a falling or rising 26-week trend, then apply the corresponding pair of thresholds from the table above — the same raw sentiment reading is not evaluated against a fixed bar across all monetary regimes.

**Entry/exit for the illustrated Investors Intelligence strategy.** Buy the S&P 500 (from cash/commercial paper) when the applicable "extreme pessimism" threshold is crossed; sell out of the S&P 500 into commercial paper when the applicable "extreme optimism" threshold is crossed. This produces a long/cash rotation rather than a long/short position. The book reports this specific rule set produced zero losing round-trip trades and a higher annualized return than buy-and-hold over 1968-2003 (hypothetical, in-sample).

**Individual-stock version.** For a single stock, test each of 7 valuation ratios (price to: dividends, sales, earnings, cashflow, 20-quarter average earnings, 20-quarter average cashflow, book value) against a range of threshold levels using that stock's own historical data, and keep whichever ratio/threshold pair best separated subsequent good and bad forward returns historically. Combine the resulting "overconfident" / "overly fearful" valuation zone with a 39-week simple moving average trend filter: after the stock shows an "overly fearful" valuation reading, wait for price to cross back above its 39-week moving average before buying; after an "overconfident" reading, wait for a cross back below the 39-week average before selling.

**Confirmation rule for the composite poll.** Do not treat a threshold cross on the NDR Crowd Sentiment Poll alone as a signal; the book only marks a confirmed extreme once the indicator has additionally reversed by 10 percentage points off its extreme reading, and states plainly that the arrows shown in its own charts are placed in hindsight and "do not represent buy and sell signals" that could have been followed in real time.

## Risk

No explicit stop-loss or position-sizing rule is given for any of these indicators. The book's implicit risk control is being out of the market (in cash/commercial paper) during the "extreme optimism" phase rather than short, which caps downside participation without adding short-side risk. Two risk warnings are stated directly in the text: (1) sentiment extremes "can persist for frustratingly long periods" — a stock or index can stay in an extreme-pessimism or extreme-optimism valuation zone for a large share of its history (one example cited spent roughly 60% of the time outside its "reasonable" valuation band), so a threshold cross alone is not a precisely timed entry; and (2) threshold levels themselves are not static — advisor and investor sentiment "normal ranges" have shifted over multi-decade samples, which is why the book applies a regime-dependent (dynamic bracket) adjustment for at least one of the series rather than a single fixed number for all market environments.

## Caveats

The COT Speculator Index, Rydex fund ratio, and NDR Crowd Sentiment Poll all draw on data histories under 20 years (Rydex funds only existed from the mid-1990s at publication), which is a small sample for setting "extreme" thresholds meant to hold across future decades and regimes. The book's own strongest performance claim (the Investors Intelligence dynamic-bracket strategy with zero losing trades, 1968-2003) is a single-market, single-period, in-sample backtest with no out-of-sample validation shown, and past 2003 the retail brokerage, options, and ETF landscape changed enough (proliferation of leveraged and inverse products, options market growth, algorithmic flow) that some of these specific series' historical thresholds likely need re-calibration rather than direct reuse. The individual-stock valuation-band approach explicitly requires re-optimizing per stock from that stock's own history — it has no universal threshold — and the authors state outright that it is intended as a sentiment-perspective tool, not as a standalone trading system, so treat it as a filter to be combined with independent price/trend signals rather than a complete method on its own.
