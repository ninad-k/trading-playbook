---
title: Moving Average Crossover Timing System
author: Leslie N. Masonson
year: 2004
slug: leslie-n-masonson-all-about-market-timing--moving-average-timing-system
tier: A
category: Trend Following & Mechanical Systems
tags: [moving-averages, trend-following, market-timing, mechanical-systems, whipsaw]
difficulty: beginner
doc_type: system
parent: leslie-n-masonson-all-about-market-timing
pages: 275
one_liner: "Single- and dual-moving-average crossover rules for timing index funds/ETFs, with multiple researchers' backtested optimal lookback lengths across the DJIA, S&P 500 and Nasdaq."
related: [michael-covel-trend-following, marcel-petro-market-timing]
source_file: "Leslie N Masonson - All About Market Timing.pdf"
---

## What it is

A trend-following timing system that uses a simple moving average (SMA) of an index's closing price to generate long/cash (or long/short) signals: buy when price crosses above the moving average, exit when price crosses back below it. A "dual" variant instead crosses two moving averages of different lengths against each other. The book compiles independent backtests from five researchers (Robert Colby on the DJIA 1900–2001, Michael McDonald on the S&P 500, Paul Merriman and Dennis Tilley on the Nasdaq 100/S&P 500 Total Return, John Murphy on the Nasdaq Composite) plus the author's own TradeStation tests, converging on the finding that shorter-to-intermediate SMA lengths (roughly 18–130 days, depending on the index) mechanically beat buy-and-hold over multi-decade periods, generally with lower risk, despite a minority of trades being profitable.

## Rules

1. **Single moving-average crossover (base rule).** Choose an index/ETF (S&P 500, Nasdaq Composite, DJIA proxy) and a moving-average length. Buy when the closing price crosses above the moving average. Sell to cash when the price crosses below the moving average; aggressive/short-capable investors may instead sell short (using inverse/bear funds or by shorting the ETF directly, where permitted) rather than just moving to cash.
2. **Dual moving-average crossover.** Track two SMAs of different lengths on the same index (a common pairing is 50-day and 200-day). Buy when the faster average (50-day) crosses above the slower average (200-day). Sell/short when the faster average crosses back below the slower average.
3. **Choosing a lookback length — backtested candidates.** Robert Colby's 1900–2001 DJIA test found all SMA lengths from 1 to 385 days beat buy-and-hold, with the 66-day SMA about 31x more profitable than buy-and-hold ($639,933 vs. $20,105 net profit per $100 invested) and the 126-day SMA the most profitable long-term length tested (2022.5% better than buy-and-hold). Michael McDonald's S&P 500 (with dividends) tests found the 72-day and 132-day SMAs superior, with the 130-day producing a 12.5% annualized return vs. 10.3% for buy-and-hold over 71 years. The author's own TradeStation optimization on the Nasdaq Composite (1971–2002) found the 18- to 22-day SMA range most profitable, with an 18-day SMA producing a 22.47% annualized return (best single result found).
4. **20-day SMA — Nasdaq Composite (specific worked system).** Buy when the Nasdaq Composite closing price crosses above its 20-day SMA; sell short when it crosses below. Backtest (Feb. 1971–Dec. 2002, $100,000 starting capital, no dividends): $46,563,046 net profit vs. $1,139,260 for buy-and-hold (46:1 ratio), from 664 trades (about 21/year) with only 38% of trades profitable.
5. **25-week SMA — Nasdaq Composite (lower-maintenance variant).** Same crossover logic as rule 4 but using weekly closes and a 25-week SMA (≈125 trading days), checked only once a week. Backtest (same period): $4,274,870 net profit vs. $968,400 for buy-and-hold, from only 97 trades (≈3/year) with 42% profitable — a large majority of the 20-day system's total return with roughly 1/7th the trade frequency and monitoring burden.
6. **100-day SMA — Nasdaq 100 (Merriman).** Buy the Nasdaq 100 (or a Nasdaq 100 index/leveraged fund) when price crosses above its 100-day SMA; sell to cash (not short) on a cross below. 1972–2001 backtest: 18.9% annualized ($180,476 on $1,000) vs. 11.8%/$28,396 for buy-and-hold, with lower standard deviation (19.3% vs. 28.0%) and less than half the drawdown. A 50%-leveraged version returned 23.2% annualized ($522,782); a 100%-leveraged (beta 2.0) version returned 26.9% annualized ($1,270,131), both with higher standard deviation than the unlevered version but still better drawdowns than buy-and-hold.
7. **Whipsaw filter (general rule).** Because shorter SMAs generate more signals and more false breakouts in sideways markets, and longer SMAs react more slowly (giving back more of a move before signaling), select the SMA length to match investing horizon (shorter for active traders willing to accept more whipsaws, longer for lower-maintenance investors) and, once chosen, take every signal without selectively skipping ones that "feel" wrong.
8. **Stop-loss overlay.** Apply an 8–10% trailing stop on unrealized gains so a sharp reversal does not give back most of an open profit before the moving-average signal itself triggers an exit.

## Risk

The single largest quantified risk in every backtest reported is the low percentage of winning trades (21% for Colby's 66-day DJIA system, 38–42% for the Nasdaq 20-day/25-week systems) — the system's profitability depends entirely on winners being much larger than losers (Colby's average winner was $6,886 vs. an average loser of –$1,238), so a trader must be able to tolerate a majority of trades closing at a loss without abandoning the system. Whipsaws in sideways/trading-range markets are explicitly flagged as the main failure mode: the book notes there were "many buy and sell signals (whipsaws)" using the 50-day SMA from January through September 2000 alone, and shorter SMAs are systematically more exposed to this than longer ones. Leverage (used in Merriman's 50%/100%-leveraged Nasdaq 100 variants) proportionally increases both the annualized return and the standard deviation/drawdown, so leveraged versions should only be used by investors who have already accepted the higher risk tolerance this implies.

## Caveats

Results are highly sensitive to the exact index, time period, and SMA length tested — Colby's DJIA-based optimal lengths (66-day, 126-day) differ from McDonald's S&P-500-based optimal lengths (72-day, 132-day) and from the author's own Nasdaq-Composite-based optimal length (18-day), so there is no single universally "best" moving-average length; a trader must re-optimize (or at minimum re-validate) for the specific index and vehicle being traded rather than assume the numbers transfer directly. All-shorting variants (using every sell signal to go short rather than to cash) materially changed results in at least one test — Colby notes that the short side of his DJIA system stopped being profitable after the 1987 crash — indicating the long and short legs of these systems do not necessarily have equal edge over time. As with the book's other systems, most backtests exclude dividends, transaction costs and taxes, and use unleveraged historical index data that in some cases was not itself directly tradable over the full test period.
