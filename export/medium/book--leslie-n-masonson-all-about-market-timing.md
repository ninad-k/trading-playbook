# All About Market Timing: the trader's summary

*A backtested survey of mechanical, calendar- and moving-average-based market-timing systems (Best Six Months, presidential cycle, VL4%/NC6% filters) that beat buy-and-hold with lower drawdowns.*

**Leslie N. Masonson** · 2004 · Trend Following & Mechanical Systems · intermediate

*Source coverage: partial. PDF pages inspected: 11, 16, 19, 21, 149-150 (contents, the drawdown-recovery arithmetic, and the seasonal and electoral-cycle studies behind the timing systems). These are study notes, not verified trading results.*

## Overview

Part of McGraw-Hill's "All About..." finance series, this book argues that mechanical market timing — getting out of the market during historically weak periods and back in during historically strong ones — beats passive buy-and-hold on both return and risk over long horizons. Masonson, a financial writer and independent trader, compiles and extends research from named practitioners and researchers (Yale and Jeff Hirsch of the Stock Trader's Almanac, Sy Harding, Ned Davis, Nelson Freeburg of FORMULA RESEARCH, Mark Vakkur, Robert Colby, Paul Merriman, Dennis Tilley, John Murphy) and runs his own backtests using TradeStation and Ultra 7 software. The first third of the book builds the case against buy-and-hold and introduces ten market-health indicators; the middle third (Chapters 7–11) presents five specific, rule-based timing systems with full backtest statistics; the final third covers timing newsletters, advisors and software vendors.

## Core thesis

Stock market returns are not evenly distributed through calendar time (certain months, certain years of the four-year presidential cycle) or through price trends (moves above/below a moving average or a percentage-based trigger tend to persist), so mechanical rules that keep an investor invested only during historically favorable windows can capture most of the market's long-run gain while being out of the market — hence out of risk — during a large fraction of the worst drawdowns. Masonson's repeated empirical claim, backed by multiple independent researchers' backtests spanning different indexes and time periods (1886–2002 in some cases), is that these effects are large, persistent across eras, and simple enough for an individual investor to implement in under an hour a year, without requiring the investor to be right more often than wrong on individual trades.

## Key concepts

- **Buy-and-hold myth** — the book's foil: Masonson argues that unqualified buy-and-hold ignores that most of the market's gain historically clusters in a small fraction of months/years, and that avoiding the worst periods (not predicting the best ones) drives most of timing's edge.
- **Ten market-health indicators** — a checklist of sentiment (Investors Intelligence Bull/Bear Index, UBS/Gallup Index of Investor Optimism, AAII survey, CBOE VIX/VXN) and internal/breadth indicators (weekly new highs/new lows, percent of NYSE stocks above their 10-week moving average) used as a scorecard (+1/–1 per indicator) to gauge whether the market is at a sentiment extreme likely to reverse.
- **Best Six Months (BSM) strategy** — Yale Hirsch's calendar system: long the market roughly November 1–April 30, in cash the other six months.
- **Seasonal Timing Strategy (STS)** — Sy Harding's refinement of BSM using MACD crossovers to move the calendar-based entry/exit earlier or later within a matching window.
- **Presidential (four-year) election cycle** — pre-election, election, post-election and midterm years have historically had very different average returns, with pre-election years strongest.
- **Value Line 4% strategy (VL4%)** — Ned Davis's percentage-filter system: buy when the Value Line Composite Index rises 4% off a low, sell/go short when it falls 4% off a high.
- **Nasdaq Composite/Nasdaq 100 6% strategy (NC6%/NDX6%)** — the same percentage-filter logic applied to more volatile Nasdaq indexes with a wider 6% band.
- **Moving-average crossover (single and dual)** — single: buy when price crosses above a chosen moving average, sell/short when it crosses below; dual: buy when a faster average (e.g., 50-day) crosses above a slower one (e.g., 200-day), sell on the reverse cross.
- **Whipsaw** — repeated false buy/sell signals in a sideways/trading-range market that erode a mechanical system's profits; the book's central practical risk for every rule-based system it presents.
- **Backtesting** — testing a rule mechanically against historical data to gauge validity; Masonson repeatedly notes backtests are theoretical (no dividends, taxes, slippage, or in some cases no tradable vehicle existed historically) and not a guarantee of forward results.

## Rules and setups

1. **Best Six Months (Hirsch)** — buy a broad index fund (S&P 500, Nasdaq Composite, or Total Market) on November 1; sell into cash (money market/T-bills) on April 30 of the following year; repeat annually. 1950–2001 backtest on the DJIA: total loss of $77 over all May–October periods vs. a $457,103 gain over all November–April periods on a $10,000 stake.
2. **Best Six Months with MACD overlay (Harding's STS)** — use the calendar dates (late October / early May) only as a fallback; take the first MACD buy-signal crossover on or after October 16 as the actual entry, and the first MACD sell-signal crossover on or after April 20 as the actual exit. 1964–2002 backtest: 15,172% compounded total return vs. 4,577% for buy-and-hold on the DJIA.
3. **September-avoidance variant (Vakkur/Colby)** — sell on the last trading day of August, stay in cash through September, buy back on the first trading day of October; more aggressive variant (Colby) shorts the market from the last day of August to the last day of September instead of going to cash. 1900–2000 DJIA backtest (Colby, short variant): $164,048 profit vs. $22,055 for buy-and-hold from a $100 stake.
4. **Presidential-cycle-optimal-months strategy (Vakkur)** — apply 2:1 leverage (50% margin) in the seven historically strongest months (January–April, July, November, December) of the pre-election and election years only; hold 100% cash in May and September of all four cycle years and in June/August of post-election and midterm years; be 100% invested (no margin) in all other months. 1950–1995 backtest: 14.9% annualized return, turning $10,000 into $5,189,384, vs. 8.4%/$372,388 for buy-and-hold, with a comparable maximum drawdown (~21% vs. 41.3%).
5. **Value Line 4% strategy (VL4%)** — using the weekly Friday close of the Value Line Composite (or Arithmetic) Index: buy when the index closes 4% or more above its most recent low; sell (or go short) when it closes 4% or more below its most recent high; hold the position until the opposite signal triggers. Ned Davis's 1966–1988 backtest: 14.9% annualized vs. 2.4% for buy-and-hold; roughly half of all trades were losers (average loss –3.7%) but winners averaged +11.9%, a ~3:1 win/loss ratio.
6. **Nasdaq Composite / Nasdaq 100 6% strategy (NC6%/NDX6%)** — identical percentage-filter logic to VL4%, but with a 6% band applied weekly (not daily — the book's own daily-data tests of this strategy performed far worse and are explicitly flagged as not usable) to the Nasdaq Composite or Nasdaq 100 index. 1971–2002 NC6% weekly backtest: 18.77% annualized ($15.2M profit on $100,000) vs. buy-and-hold's $1.27M; only 54.3% of trades were winners but the profit factor was 2.37.
7. **Single moving-average crossover** — buy an index fund/ETF when its price crosses above a chosen simple moving average (commonly the 20-, 50-, 66-, 100-, 130-, or 200-day); sell to cash (or short, for aggressive traders) when price crosses back below. Colby's 1900–2001 DJIA test found the 66-day SMA crossover 31x more profitable than buy-and-hold ($639,933 vs. $20,105 net profit on a $100 stake); only 21% of trades were profitable but average winners ($6,886) far outsized average losers (–$1,238).
8. **Dual moving-average crossover** — buy when a faster average (e.g., 50-day) crosses above a slower average (e.g., 200-day); sell/short on the reverse cross. Illustrated on the S&P 500 from 1998–2002 avoiding a subsequent 46% decline after a November 2001 sell cross.
9. **Stop-loss overlay (general rule across all systems)** — Masonson recommends an 8–10% trailing/protective stop on open profits in any of the moving-average or percentage-filter systems, so a system does not have to wait for the full opposite signal (which can give back most of an unrealized gain) before locking in profit.

## Risk and money management

Every system in the book trades off return for time-in-market rather than eliminating loss: the BSM strategy is explicitly "50% less risky than buy-and-hold" because it is invested only half the year; the presidential-cycle optimal-months strategy and Merriman's 100-day moving-average tests on the Nasdaq 100 both show that leverage (2:1, i.e., 50% margin, or a beta-2.0 leveraged fund) roughly doubles or more the annualized return but also roughly doubles the standard deviation and maximum drawdown — the book is explicit that leverage should only be added by investors with a higher risk tolerance and combined with a stop-loss. Multiple systems (VL4% weekly/daily, NC6% daily) posted extended flat or losing stretches — the VL4% VLCI weekly test lost money across 15 consecutive whipsawed trades from January 2000–January 2001 — illustrating that a mechanically sound system can still have multi-year drawdowns in range-bound markets. Masonson's blanket money-management rule across chapters: never selectively skip a signal ("take all of them...that is a path to confusion, loss of discipline, and ultimately, financial ruin") and cap losses per trade at roughly 10%.

## Psychology and discipline

The book's discipline argument is that market timing's main psychological cost is not being wrong on individual trades (most of the mechanical systems tested are wrong on 40–60% of trades) but tolerating long stretches where results diverge from a buy-and-hold benchmark, including extended flat/losing periods in range-bound markets (the "whipsaw" problem). Masonson repeatedly quotes the foreword's author, Paul Merriman, and other researchers to argue that consistency — taking every signal, without selectively skipping ones that "feel" wrong — is the main determinant of whether a mechanical system delivers its backtested edge; deviating from the rules (market-timing "purists" abandoning a system after a losing stretch) is presented as the primary reason individual investors fail at timing even when using a historically validated system.

## Chapter map

- Ch 1 — The Stock Market = Bull Markets + Bear Markets — framing bull/bear history and the case that avoiding bears matters more than catching every bull.
- Ch 2 — The Buy-and-Hold Myth — statistical case against unconditional buy-and-hold.
- Ch 3 — Market Timing: What You Need to Know — definitions, objections to timing addressed.
- Ch 4 — Ten Indicators to Determine the Market's Health — sentiment (Bull/Bear Index, Investor Optimism, AAII, VIX/VXN) and internal/breadth indicators (new highs/lows, % above 10-week MA) with bullish/bearish threshold numbers.
- Ch 5 — Specialized Mutual Funds: Index, Sector, and Leveraged Funds — investment vehicles for implementing timing signals.
- Ch 6 — Exchange-Traded Funds — ETF vehicles and mechanics for timing strategies.
- Ch 7 — Calendar-Based Investing: The Best Six Months Strategy — Hirsch's BSM, Harding's MACD-enhanced STS, Vakkur's and Colby's September-avoidance variants.
- Ch 8 — Combining Presidential Cycle Years with Seasonality — Vakkur's and Freeburg's four-year election-cycle research and the leveraged "optimal months" strategy.
- Ch 9 — Using Moving Averages — single/dual crossover mechanics and backtests by Colby, McDonald, Merriman, Tilley and Murphy across the DJIA, S&P 500 and Nasdaq indexes.
- Ch 10 — Value Line 4 Percent Strategy — VL4% history, rules, and multiple decades of backtest results (weekly/daily, geometric/arithmetic index variants).
- Ch 11 — Nasdaq Composite 6 Percent Strategy — the VL4% logic re-parameterized and re-tested on Nasdaq indexes.
- Ch 12 — Market-Timing Resources: Newsletters, Web Sites, and Advisors.
- Ch 13 — Market-Timing Software — TradeStation, Ultra 7, VectorVest and other vendor tools.

## Strengths and caveats

The book's strongest feature is that nearly every claim is backed by a named, checkable backtest (source, date range, index, and precise return/drawdown numbers) rather than vague assertion, and several systems (BSM, VL4%, NC6%) are stated with entry/exit rules complete enough to code directly. Caveats: this is a 2004 book, and several of its recommended data feeds, software packages (Ultra 7, older TradeStation versions) and named newsletters/websites are dated or discontinued; none of the backtests in the book account for transaction costs, taxes, bid-ask slippage, or (in most cases) dividends, and several explicitly acknowledge the underlying index (e.g., the Value Line Composite Index) was not itself directly tradable historically, making the results theoretical. The book reports many strategies' win rates below 50% and leans on results from a fairly small number of researchers (several strategies are cross-validated only by Masonson's own re-tests using the same commercial software), so independent out-of-sample verification is limited. Masonson is candid where a variant fails (e.g., he states outright that daily-interval NC6%/NDX6% signals "should be avoided at all costs"), which is a strength for a book whose thesis could otherwise read as promotional.

## Who should read it

Retail and semi-active investors who want mechanical, low-maintenance calendar- or trend-based alternatives to unconditional buy-and-hold, and who are comfortable being wrong on a majority of individual trades in exchange for avoiding the worst drawdowns. Best paired with a discipline for evaluating and updating a strategy's parameters over time, since several results (e.g., VL4% weekly vs. daily, VLCI vs. VLAI) show meaningful sensitivity to exact rule specification. Less useful for short-term/day traders, since most systems here operate on weekly or slower signals and several explicitly underperform when converted to daily signals.

## Related books in this library

- [Market Timing](https://ninad-k.github.io/trading-playbook/books/marcel-petro-market-timing.html) — another market-timing-focused text covering complementary calendar/technical timing approaches.
- [Trend Following](https://ninad-k.github.io/trading-playbook/books/michael-covel-trend-following.html) — broader trend-following philosophy and evidence that complements the moving-average crossover systems in Chapter 9.
- [Trading for a Living](https://ninad-k.github.io/trading-playbook/books/elder-alexander-trading-for-a-living.html) — adds a discretionary technical-analysis and psychology layer to the purely mechanical systems presented here.
- [Stock Market Wizards](https://ninad-k.github.io/trading-playbook/books/jack-schwager-stock-market-wizards.html) — trader interviews illustrating the discipline-under-a-losing-streak theme central to Masonson's psychology argument.
- [Trading Spreads and Seasonals](https://ninad-k.github.io/trading-playbook/books/joe-ross-trading-spreads-and-seasonals.html) — a complementary treatment of seasonal patterns, applied to spreads rather than index timing.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: market-timing, seasonality, moving-averages, presidential-cycle, sentiment-indicators, backtesting, mechanical-systems
