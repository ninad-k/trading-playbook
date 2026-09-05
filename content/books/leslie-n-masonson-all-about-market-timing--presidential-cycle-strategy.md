---
title: Presidential Election Cycle Strategy
author: Leslie N. Masonson
year: 2004
slug: leslie-n-masonson-all-about-market-timing--presidential-cycle-strategy
tier: A
category: Trend Following & Mechanical Systems
tags: [seasonality, presidential-cycle, calendar-effects, market-timing, leverage]
difficulty: intermediate
doc_type: system
parent: leslie-n-masonson-all-about-market-timing
pages: 275
one_liner: "Mark Vakkur's four-year election-cycle timing system: concentrate exposure (and optional leverage) in the pre-election and election years' strongest months, sit out the rest."
related: [marcel-petro-market-timing, joe-ross-trading-spreads-and-seasonals]
source_file: "Leslie N Masonson - All About Market Timing.pdf"
---

## What it is

A calendar-timing system, developed and tested by Mark Vakkur (Technical Analysis of Stocks & Commodities, October 1996) and extended by Nelson Freeburg (FORMULA RESEARCH), that exploits the U.S. four-year presidential election cycle's historically uneven stock market returns. The book documents that pre-election years have by far the strongest average returns (an 18.72% average annual return over 1950–1995, up 100% of years), followed by election years (10.08% average, up 91% of years), while post-election years (2.00% average, up only 45% of years) and midterm years (4.63% average, up 55% of years) are much weaker. The strategy family ranges from simply investing only in the two strong years and holding cash in the two weak years, up to a fully leveraged, month-by-month "optimal months" version.

## Rules

1. **Cycle year classification.** Label each year in the four-year U.S. presidential cycle as pre-election, election, post-election, or midterm (e.g., 2023 pre-election, 2024 election, 2025 post-election, 2026 midterm).
2. **Base strategy — invest in the two strong years only.** Hold a broad market index fund for the entirety of the pre-election year and the election year; hold 100% cash (T-bills) for the entirety of the post-election year and the midterm year. 1950–1995 backtest: 10.0% annualized return ($733,605 on a $10,000 stake) vs. 8.4%/$372,388 for buy-and-hold, with roughly half the standard deviation (8.3% vs. 14.4%) and half the maximum drawdown (18.7% vs. 41.3%).
3. **2:1 Leverage variant.** Use 50% margin (2:1 leverage) during the pre-election year; hold the position unlevered (100% invested, no margin) during the election year; hold 100% cash during the other two years. 1950–1995 backtest: 11.4% annualized, $1,272,369 ending value, but with a larger maximum drawdown (–46%) and higher standard deviation (14.8%) than the unlevered base strategy.
4. **Leveraged Best Months (LBM) variant.** Within the pre-election and election years, apply 2:1 leverage (50% margin) only during the best six months (November–April); remain 100% invested (no margin) during the same November–April window in the post-election and midterm years; also hold 100% invested (no margin) during the May–October period of the post-election and midterm years. The only 100%-cash allocation under this variant is May–October of the post-election and midterm years. 1950–1995 backtest: 12.7% annualized, $2,183,257 ending value, with a lower drawdown than the simple 2:1 leverage variant (better risk-adjusted return than rule 3).
5. **Optimal Months variant (Vakkur's most refined version).** Apply 2:1 leverage in the pre-election and election years during their seven historically strongest months: January, February, March, April, July, November, December. Hold 100% cash in May and September of all four cycle years, and additionally in June and August of the post-election and midterm years. Hold 100% invested (unlevered) in all remaining months: January–April, July, and October–December of the post-election/midterm years, and June and August of the pre-election/election years. 1950–1995 backtest: 14.9% annualized, $5,189,384 ending value — the highest risk-adjusted return (13.7% risk-adjusted annual return) of all variants tested, with a maximum drawdown (~21%) comparable to the unlevered base strategy.
6. **Midterm-low-to-election-year-high pattern (supplementary signal).** Historically (1918–2000, Hays Advisory Group data), buying at the midterm-year low and holding to the following election-year high produced a gain in 20 of 21 cycles, averaging 56.8% (61.8% excluding the single 1930–1932 loss) — used as a confirming, longer-horizon overlay rather than a standalone trading rule.

## Risk

Leverage is the dominant risk lever in this system: moving from the unlevered base strategy (rule 2) to the 2:1-leveraged variant (rule 3) roughly doubled the maximum annual drawdown (from –18.7% to –46%) for an incremental 1.4 percentage points of annualized return, a materially worse risk/reward trade than the more selectively-leveraged LBM and Optimal Months variants (rules 4–5), which achieved higher returns with drawdowns close to the unlevered base case by concentrating leverage only in the historically strongest months rather than across entire years. Being out of the market entirely for two full years out of every four (the post-election and midterm years) means the strategy can badly lag buy-and-hold if a rally breaks out during a normally-weak year — the book's own data shows post-election and midterm years still average positive returns (just far lower than pre-election/election years), so the strategy is giving up modest expected gains during "cash" years in exchange for avoiding the years with the worst average performance and largest historical crashes.

## Caveats

The core sample is thin by statistical standards — only about 11-12 completed four-year cycles in the primary 1950-1995 dataset (fewer for some sub-variants), so each "year type" average return rests on roughly a dozen independent observations; Freeburg's extension back to 1886 (DJIA) increases the sample but changes index and methodology (no dividends, price-only DJIA vs. Vakkur's price-only S&P 500), and the two data sources are not directly comparable trade-for-trade. All backtests exclude dividends, transaction costs, and taxes. The most profitable variants (rules 4–5) require precise month-by-month leverage toggling that assumes frictionless, cost-free entry and exit at each monthly boundary — a level of trading precision a retail investor would need dedicated software or a rules checklist to replicate exactly as tested. As with any calendar-based strategy, the persistence of the political/economic mechanism believed to drive the cycle (fiscal and monetary policy patterned around elections) is an assumption the book states qualitatively rather than proves causally.
