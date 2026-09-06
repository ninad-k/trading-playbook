# Does Trend Following Work on Stocks?: the trader's summary

*Blackstar Funds' study buying 24,000+ US stocks at all-time highs with a 10-ATR trailing stop over 1983-2004, finding a positive expectancy despite realistic costs and survivorship correction.*

**Cole Wilcox and Eric Crittenden** · 2005 · Trend Following & Mechanical Systems · intermediate

*Source coverage: partial. PDF pages inspected: 3, 7-8, 11 (the universe construction, the expectancy and holding-period statistics and the year-by-year trade counts). These are study notes, not verified trading results.*

## Summary

Question: does a long-only trend-following approach, well-documented on futures, also work on individual stocks? Data: 24,000+ US securities on NYSE/AMEX/NASDAQ from January 1983 to December 2004 (over half already delisted, included specifically to remove survivorship bias), back-adjusted for all corporate actions (splits, dividends, mergers). Method: buy any stock making a new all-time closing high (the purest possible trend-following entry), sized in a realistic tradable universe (minimum $15 price filter, minimum $500K/$1M average daily dollar volume for NYSE/AMEX vs. NASDAQ), exit on a 10-unit Average True Range (ATR) trailing stop, with 0.5% round-turn transaction costs deducted per trade. Finding: over 18,000+ trades and 22 years, the system shows a strongly right-skewed return distribution and a positive mathematical expectancy of approximately 15.2% per trade, supporting a "yes" answer.

## Key points

- **Entry rule**: buy tomorrow's open whenever today's close is the highest close in the stock's entire history — a purely mechanical trend-following trigger.
- **Exit rule**: a 10x Average True Range trailing stop (exit next open once price closes through it); ATR settings from 8 to 12 showed no material difference.
- **Win rate 49.3%** with a 2.56 average-win-to-average-loss ratio; 17% of trades gained 50%+ while under 3% lost 50%+ — a right-skewed, long-volatility payoff typical of trend systems.
- **Expectancy ≈ 15.2%** per trade, average holding period 305 calendar days.
- **Risk-normalized results**: only about 2% of trades lost more than their initial budgeted risk by a wide margin, mostly from overnight gaps.
- **Short selling excluded** deliberately — borrow/buy-in uncertainty and the asymmetry of unlimited loss vs. capped 100% gain was judged to break the model's assumptions.
- **Data integrity matters**: excluding delisted stocks or failing to adjust for dividends materially distorts both entries (breakout levels) and exits (phantom volatility from unadjusted ex-dividend gaps).
- **Portfolio overlay** (mechanics undisclosed): never add to losers, only trim winners, never skip a signal, always honor stops, cap total open risk — hypothetical result: 19.3% annualized vs. 12.0% for the S&P 500 Total Return Index over 1991-2004, with a smaller max drawdown (−20.8% vs. −44.7%).

## Actionable rules

1. Buy at a new all-time closing high; enter on the next day's open.
2. Set a trailing stop at 10x ATR below the high-water mark since entry; exit next open if breached.
3. Apply a minimum price filter ($15) and minimum average dollar-volume filter ($500K NYSE/AMEX, $1M NASDAQ) to keep the universe realistically tradable.
4. Deduct at least 0.5% round-turn for commissions/slippage; the paper warns lower assumptions distort results.
5. Do not apply this same entry logic to shorts — the risk/reward and borrow mechanics are judged fundamentally asymmetric for it.

## Caveats

Published by Blackstar Funds as research/marketing for their own managed programs; the portfolio-level equity curve is explicitly hypothetical and its risk-management mechanics are undisclosed ("not disclosed"), so it cannot be independently verified or replicated. Results predate 2005 and are US-equity-specific; no out-of-sample period beyond the study window is shown. The paper is a single-parameter-set case study (10 ATR) rather than a robustness sweep, though it notes 8-12 ATR gave similar results.

## Who it is for

Systematic/trend-following traders and researchers deciding whether trend entries (breakout to new highs) and ATR-based trailing stops, well known from futures CTAs, transfer to a long-only stock portfolio.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: trend-following, backtesting, atr-stop, survivorship-bias, stocks, expectancy, blackstar-funds
