---
title: The Little Book That Beats the Market — The Magic Formula
author: Joel Greenblatt
year: 2006
slug: the-little-book--magic-formula
tier: A
category: Investing, Value & Market History
tags: [magic-formula, earnings-yield, return-on-capital, quantitative-investing, stock-screening]
difficulty: beginner
doc_type: system
parent: the-little-book
pages: 177
one_liner: "Step-by-step construction, portfolio build, holding-period, and tax-lot rules for running Greenblatt's Magic Formula stock-ranking system."
related: [the-little-book, the-intelligent-investor-benjamin-graham]
source_file: "The Little Book.pdf"
---

## What it is

A mechanical, computer-screenable stock-ranking system that buys good businesses (high return on capital) only when they are cheap (high earnings yield), diversified across 20–30 names and rebalanced on a rolling one-year-per-position schedule. It requires no forecasting, no financial-statement modeling beyond the two ratios below, and no discretionary judgment about individual companies — the entire selection process is a rank-and-sum calculation over a large stock universe.

## Rules

**Universe and exclusions.** Start from the largest ~3,500 U.S.-exchange-listed companies by market capitalization (or restrict to the largest 2,500 or 1,000 for a higher-liquidity, lower-return variant — see performance table on the parent page). Exclude utilities, financial stocks (banks, insurers, mutual-fund companies), foreign ADRs, and any company with unreliable or stale financial data (e.g., earnings reported in the last week, distorting trailing figures).

**Step 1 — Compute return on capital.** Return on capital = EBIT / (Net Working Capital + Net Fixed Assets). EBIT is pre-tax operating earnings before interest, calculated over the trailing 12 months. Net working capital excludes excess cash not needed for operations and excludes short-term interest-bearing debt from current liabilities. Net fixed assets exclude goodwill (only tangible capital counts). Rank all companies 1-to-N, rank 1 = highest return on capital.

**Step 2 — Compute earnings yield.** Earnings yield = EBIT / Enterprise Value. Enterprise value = market value of equity (including preferred stock) + net interest-bearing debt, using the most recent closing price and most recent balance sheet. Rank all companies again 1-to-N, rank 1 = highest earnings yield (cheapest).

**Step 3 — Combine ranks.** For each company, add its return-on-capital rank to its earnings-yield rank. The lowest (best) combined-rank companies are the Magic Formula's top selections. (Example from the source: a company ranked 232nd in return on capital and 153rd in earnings yield gets combined rank 385, which can outrank a company ranked 1st in return on capital but only 1,150th in earnings yield, combined rank 1,151.)

**Step 4 — Build the portfolio gradually.** Do not buy all 20–30 positions at once. Using the top-ranked names, buy 5–7 stocks every two to three months, investing only 20–33% of the total capital earmarked for the strategy at each round, until a full 20–30-stock portfolio is built over the first 9–10 months.

**Step 5 — Hold and rotate.** Hold each individual stock for one year. In a tax-free/tax-deferred account, sell exactly at the one-year mark and replace with the next top-ranked name(s). In a taxable account, sell winning positions a few days *after* the one-year mark (to qualify for long-term capital-gains tax treatment) and sell losing positions a few days *before* the one-year mark (to qualify the loss for short-term-loss tax treatment, deductible against ordinary income at potentially higher rates than the long-term gains rate). Reinvest all proceeds into freshly re-ranked top names.

**Step 6 — Commit for the long run.** Continue the process unmodified for a minimum of three to five years, regardless of interim results. Do not abandon or tweak the formula after a bad month, quarter, or even a full year or two — the source backtest shows the formula lagged the market in roughly 1 of every 4 rolling one-year periods and could lag for two or three years running, but beat the market in 95% of rolling three-year periods and never lost money over any rolling three-year period in the 1988–2004 sample.

**Alternative construction (no dedicated screening tool available).** Screen for Return on Assets (ROA) ≥ 25% as a substitute for return on capital; from that group, screen for the lowest Price/Earnings ratios as a substitute for earnings yield; exclude utilities, financials, and foreign ADRs; treat a P/E of 5 or below as a possible data-quality flag rather than a genuine bargain; then apply Steps 4–6 above unchanged.

## Risk

Diversification is by stock count, not position weighting or stop-losses: hold 20–30 positions so that any single business-specific loss is diluted across the portfolio. There is no per-position stop-loss, no volatility targeting, and no percent-of-equity risk cap — the system's only defense against a bad pick is (a) breadth (20–30 names) and (b) the statistical tilt toward historically higher-returning rank deciles (top-ranked decile groups returned 17.9%/year vs. 2.5%/year for bottom-ranked groups over 1988–2004, in a 10-decile backtest of the 2,500-largest-company universe). The largest practical risk the source material flags is behavioral, not financial: abandoning the system during one of its normal multi-year underperformance stretches before the long-run edge has a chance to show up.

## Caveats

The formula is a ranking system, not a valuation model — it does not estimate intrinsic value or a price target, only relative attractiveness within the chosen universe at a point in time. Results are highly sensitive to the exact universe and exclusion rules (financials and utilities are excluded because their capital structures make EBIT/tangible-capital comparisons unreliable); applying the ranking to those sectors is not supported by the source. The named implementation tool (magicformulainvesting.com) and the general screening substitutes (ROA ≥ 25%, lowest P/E) reflect mid-2000s web resources and screening conventions; a modern implementation should independently verify data quality and consider transaction costs and tax-lot accounting software rather than relying on the book's manual process. The backtest (1988–2004) is a single historical sample from a period of generally rising U.S. equity markets; the source does not test the formula through earlier regimes (e.g., the 1970s) or non-U.S. markets.
