---
author: Vladimir Daragan
category: Quant, Microstructure & Academic Research
difficulty: intermediate
doc_type: book
one_liner: 'Statistics-first framework for short-term stock trading: growth coefficients
  vs. average return, risk-to-return ratios, Markowitz-style portfolio allocation,
  and empirical stop-loss touch probabilities.'
pages: 57
related:
- position-sizing
- money-management-report-van-tharp
- balsara-nauzer-j-money-management-strategies-for-futures-traders
reviewed_pdf_pages: 4, 8, 27, 33, 35, 37, 51 (the probability calculations, stop-order
  statistics and the correlation tables)
slug: vladimir-daragan-how-to-win-the-stock-market-game
source_file: Vladimir Daragan - How_to_Win_the_Stock_Market_Game.pdf
source_review: partial
tags:
- statistics
- risk-management
- position-sizing
- correlation
- portfolio-theory
- stop-loss
- short-term-trading
tier: B
title: 'How to Win the Stock Market Game: Developing Short-Term Stock Trading Strategies'
year: unknown
---

## Summary

A four-part, math-heavy guide (by a physicist-turned-trader who ran stta-consulting.com) that teaches short-term stock traders how to properly measure their own strategy's performance and risk before betting on it. It builds up from basic return-per-trade math, through why simple averaging overstates real returns (growth coefficients are the correct tool), to standard-deviation-based risk measures, correlation and Markowitz portfolio theory applied to trading strategies, and empirical studies of how often stop-loss orders get touched at various distances and holding periods.

## Key points

- Simple average return per trade overstates true performance when trades compound; the correct measure is the geometric average growth coefficient, Kav = (K1×K2×...×Kn)^(1/n).
- Defines "risk" as the standard deviation of returns per trade, and the risk-to-return ratio (σ/Rav) as the key strategy-quality metric: under 3 is very good, avoid anything above 5.
- Applies Markowitz portfolio theory to trading strategies (not just assets): optimal capital allocation between two strategies minimizes portfolio-level risk-to-return, generally requiring diversification even when one strategy alone has a higher return.
- Shows that brokerage commissions materially raise the probability of a 50%+ capital drawdown, especially for smaller accounts, because the fixed-dollar commission eats a larger percentage of a shrunken account.
- Studied 11 years of history on 300 randomly selected stocks: the probability a stop placed at "1×daily amplitude (A)" below the purchase price gets touched is ~45% after 1 day, ~60% after 2 days, and ~80% after 8 days; a stop at "3×A" stays under 50% even after 8 days.
- Counterintuitive finding: for a 4-day, $100-stock example, the worst stop placement (highest expected average dollar loss) was a moderate $94 stop (-6%), not the tightest or the widest tested level.
- Introduces the D-parameter: deviation of the current close from a linear trend-fit line, measured in standard deviations (σ); D < -1 suggests oversold, D > +1 suggests overbought, over the chosen lookback window.
- Recommends dividing capital across multiple positions/days when holding periods exceed one day, since risk falls proportional to 1/√N of positions while expected return per trade only mildly declines from added commissions.
- Warns that a single large outlier loss (e.g., -20% on a market-crash day) should not be averaged in with normal trades using equal weighting; recalculate assuming rare tail events have their own probability.

## Actionable rules

1. Judge a strategy by its risk-to-return ratio (σ/average return), not average return alone; treat ratios below 3 as favorable and reject or downsize anything above 5.
2. When capital allows more than one simultaneous position, split it (diversify) rather than concentrating, since risk falls as 1/√N of positions held while returns fall much more slowly, net of added commissions.
3. Recognize that a stop placed exactly at 1× the stock's average daily price amplitude (A) has roughly a coin-flip (45%) chance of being touched on day one alone, rising toward 80% by day eight — size stops relative to A and intended holding period, not an arbitrary percentage.
4. Do not abandon a strategy after a loss on a single outlier trade (e.g., a market-wide crash day); separate rare tail-risk trades from the normal-trade sample before recalculating average return.
5. If a strategy is confirmed profitable, use full trading capital rather than holding a cash reserve — but keep a reserve specifically to re-capitalize after a large (~50%) drawdown if the underlying edge is still believed to work.

## Caveats

No publication date is given in the text (references to data through April 2000 and a 1996–2000 low-risk strategy track record suggest early-2000s); all worked examples reference the author's own now-defunct stta-consulting.com strategies and cannot be independently verified. Math derivations (correlation coefficient formula, portfolio variance) are stated without full proofs, and the analysis assumes roughly normal (gaussian) return distributions, which the author himself notes is an approximation that breaks down for tail events.

## Who it is for

Short-term stock traders (1–8 day holding periods) who want a rigorous, formula-based way to evaluate their own strategy's risk and to size stops, position counts, and capital allocation — not a source of entry signals or chart patterns.
