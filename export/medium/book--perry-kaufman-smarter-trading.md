# Smarter Trading: the trader's summary

*A systems-development handbook centered on the Adaptive Moving Average (KAMA) and a rigorous, skeptical process for testing trading strategies for robustness rather than curve-fit profitability.*

**Perry J. Kaufman** · 1995 · Trend Following & Mechanical Systems · intermediate

*Source coverage: partial. PDF pages inspected: 2-4, 32, 40, 250 (contents, cost-of-execution and expectation chapters, and the glossary definitions of the efficiency ratio and risk measures). These are study notes, not verified trading results.*

## Overview

Kaufman's central argument is that markets evolve — structural change, new participants, changing volatility, and price shocks steadily erode any strategy's edge — so a trading approach should be built to adapt and to survive testing scrutiny, not just to have produced good historical returns. The book is organized in three parts: how changing markets and technology affect results, tools for meeting realistic performance objectives (profit-taking, stops, price shocks, the Adaptive Moving Average, computer learning methods), and a detailed methodology for testing a strategy's robustness. Its best-known technical contribution is the Adaptive Moving Average (AMA), commonly known outside this book as KAMA (Kaufman's Adaptive Moving Average), covered in its own system page in this library.

## Core thesis

A "lateral solution" — independent, self-contained components (entry method, profit-taking, stop-loss, risk sizing) that each stand on their own — is more robust than a "vertical solution" where each refinement is built on top of, and therefore dependent on, all previous refinements. Kaufman compares a vertical solution to a fragile skyscraper: pull one brick from the middle (one no-longer-valid assumption) and the whole structure is compromised. Trading system development should therefore isolate and test each component separately, use realistic expectations calibrated by risk (not just return), and treat any system that survives testing as still needing continuous monitoring, because the market conditions it was built for will not last indefinitely.

## Key concepts

- **Efficiency Ratio (ER)** — Kaufman's measure of trend "noise": the net directional price change over a period divided by the sum of absolute daily price changes over that period; ranges from 0 (pure noise, no net direction) to 1 (perfectly directional). Basis of the Adaptive Moving Average (see system page).
- **Lateral vs. vertical solution** — independent, separately-tested strategy components vs. a strategy where each layer depends on all prior layers; lateral solutions degrade more gracefully as markets change.
- **Overfitting (curve-fitting)** — a strategy tuned so closely to historical data that its apparent edge is an artifact of that specific dataset rather than a real, persistent pattern.
- **Maximum drawdown** — the largest peak-to-valley equity decline in a track record; Kaufman treats it as inevitable that a drawdown as large as, or larger than, the worst historical one will eventually recur.
- **Price shock** — a sudden, large, discontinuous price move (e.g., a surprise government report, a market crash) that breaks normal risk assumptions; Kaufman argues most system tests understate this risk because historical optimization naturally favors parameter sets that happened to avoid or benefit from shocks in the test window.
- **Errors of omission** — survivorship bias and the failure to model a worst-case scenario; risks that are invisible precisely because they don't appear in the test data used.
- **Deleveraging** — reducing position size (rather than adding a tighter stop) as the primary tool for controlling risk when small stop-losses prove unreliable or unpredictable in testing.
- **Chi-square significance test for trading reliability** — a formal test (compares actual vs. expected win/loss frequency) Kaufman applies to judge whether a system's live results are statistically consistent with its backtested reliability, adjusted for the number of trades in the sample.
- **Best Choice Index** — a robustness-selection tool for choosing a system's parameters by looking at how average return and its standard deviation move together across a curve of tested parameter values, rather than picking the single best-performing parameter set.

## Rules and setups

Kaufman documents general system-testing and risk-control mechanics rather than a single tradable rule set (aside from KAMA, covered separately):
1. **Profit-taking**: spreading profit-taking across multiple objective levels, rather than one fixed target, improved risk-adjusted results in Kaufman's tests (one cited test improved a return/risk ratio from .33 to .50 by taking profits on 4 of 10 trades across staggered levels); a stop-loss smaller than the largest profit-taking level will prevent the largest objective from ever being reached.
2. **Stop-losses**: Kaufman's own tests across multiple markets (e.g., Chrysler, Siemens) found stop-loss size had inconsistent, often minimal, effect on long-run annualized return once results were normalized to a fixed maximum drawdown — stops mainly change risk shape, not necessarily expectancy.
3. **Deleveraging procedure** (used when stops don't reliably control risk): (a) measure the system's long-term risk via a combination of max drawdown and standard deviation of equity changes; (b) size the position so that roughly 3 standard deviations of annualized risk equals your acceptable annual loss threshold (Kaufman's own example targets under a 10% chance of losing more than 10%/year); (c) size capital accordingly; (d) still use a wider stop-loss for shock protection, sized to avoid triggering on normal noise.
4. **Robustness testing process** (Part 3, condensed): (1) decide what to test — write rules complete and specific enough to be fully programmed, with no unstated assumptions; (2) decide how to test — use enough historical data to include multiple price shocks and regime types, avoid "continuation"/"perpetual" contract series that erase real gaps, verify data accuracy visually; (3) evaluate results using multiple parameter sets around the chosen one (not just the single best) to confirm the strategy is robust across a neighborhood of parameters, not curve-fit to one; (4) choose parameters from the middle of a stable-performance plateau, not the isolated peak of an optimization surface; (5) monitor live performance against the tested statistical distribution (e.g., via the chi-square test) to catch when a system stops working.
5. **Trend-speed selection by market type** — runaway markets favor the fastest practical trend speed; fast trending markets with sharp reversals need enough lag to avoid whipsaws; congested/sideways markets need a very slow trend speed with a large trend-change threshold to avoid repeated false signals.

## Risk and money management

Risk is the book's central technical concern. Key numbers and rules: normalize comparisons across systems to a fixed maximum drawdown (Kaufman's tables use 25%) rather than comparing raw returns; assess risk using more data, not less, because longer histories contain more price-shock episodes and regime types (a system tested on only 3 years of data will not have seen its worst-case drawdown yet); consider testing a strategy twice — once on recent data for parameter/timing selection, once on a longer history for risk assessment — since longer tests tend to show lower returns and higher risk than short, cherry-picked windows. A worked example of price-shock exposure compares an unleveraged stock portfolio (50% cash, rest in stock) against a 5%-margined futures portfolio under the same shock size, showing futures losses scaled up roughly 5–10x for the same underlying price move. Kaufman is explicit that "the greatest failure in trading is undercapitalization," driven by unrealistic (too-low) expectations of risk drawn from over-optimized backtests.

## Psychology and discipline

Less a psychology book than a discipline-of-process book: the discipline Kaufman asks for is intellectual honesty in testing — starting from a market-based idea rather than mining data for patterns ("start by knowing the answer" you're testing for, rather than letting an optimizer hand you an answer), being suspicious of unrealistically good backtest results, and resisting the temptation to abandon an originally sound rationale once favorable-looking test output arrives (his term: "starting with one idea and ending with another"). He also warns against selection bias in how traders judge market commentary after the fact — the traders who happened to be right about a move are the ones who get remembered and quoted, which distorts perceived forecasting skill.

## Chapter map

- Ch 1 — The Impact of Change on Markets and Trading — how markets and prices structurally change over time, obsolescence of once-reliable technical patterns, seasonality.
- Ch 2 — Assessing Market Reality — execution problems, performance measurement pitfalls, globalization effects.
- Ch 3 — Reasonable Expectations Give Achievable Results — the danger of letting computers "free-reign" over strategy discovery; realistic use of systems.
- Ch 4 — Risk and Return — standardizing risk/return comparisons, diversification, risk of ruin, maximum drawdown.
- Ch 5 — Profit-Taking — testing multiple profit objectives and their effect on risk.
- Ch 6 — The Mixed Role of Stops for Controlling Risk — stop-loss testing results, when stops conflict with a system's underlying logic.
- Ch 7 — Understanding Price Shocks — types of shocks, portfolio impact, and how to build shock-resistant test data.
- Ch 8 — Smarter Trend-Following — the Efficiency Ratio and the Adaptive Moving Average (see system sub-page).
- Ch 9 — Computer Learning, Neural Networks, and New Technology — expert systems, neural networks, fuzzy logic applied to trading.
- Ch 10 — Testing for Robustness — the full multi-step testing methodology and guidelines for selecting stable parameters.
- Ch 11 — Improving the Performance of Existing Systems — statistical significance testing, filtering signals, anticipation, overnight risk, leverage/cost trade-offs by trend speed.

## Strengths and caveats

Kaufman's stop-loss and price-shock test tables reflect early-1990s markets and instruments (Chrysler stock, Deutschmark futures, pre-euro European currencies) and transaction-cost assumptions that are dated, though the qualitative conclusions (stops mainly reshape risk rather than reliably improving expectancy; shocks are systematically underrepresented in short backtests) hold up as general principles. The book predates walk-forward and modern out-of-sample validation terminology but describes an equivalent process in its own vocabulary (testing a neighborhood of parameters, holding out data for a second risk-only test). The Adaptive Moving Average is Kaufman's most durable and widely-adopted contribution; other sections (expert systems, fuzzy logic, neural networks in Ch. 9) reflect mid-1990s computing enthusiasm and are more dated than the core testing methodology.

## Who should read it

System developers and quantitatively-minded traders who want a rigorous, skeptical process for building and validating mechanical strategies, and specifically anyone wanting the origin and mechanics of the Adaptive Moving Average / KAMA. Less useful for discretionary traders looking for chart-pattern or psychology-focused material — this is a testing-and-development handbook, not a setup catalog.

## Related books in this library

- [The Adaptive Moving Average (KAMA)](https://ninad-k.github.io/trading-playbook/books/perry-kaufman-smarter-trading--adaptive-moving-average-kama.html) — this library's dedicated system page for the KAMA method introduced in Chapter 8.
- [Mechanical Trading Systems: Pairing Trader Psychology with Technical Analysis](https://ninad-k.github.io/trading-playbook/books/richard-l-weissman-mechanical-trading-systems.html) — complementary coverage of mechanical trend-following system design and testing discipline.
- **New Concepts in Technical Trading Systems** (no library summary: corrupt) — another foundational adaptive/volatility-aware indicator text (Wilder's ATR, RSI) in the same technical lineage as Kaufman's Efficiency Ratio.
- [What Is a Trading System?](https://ninad-k.github.io/trading-playbook/books/van-tharp-trading-systems.html) — a complementary framework for position sizing and system evaluation alongside Kaufman's robustness-testing approach.
- [Building Winning Trading Systems with TradeStation](https://ninad-k.github.io/trading-playbook/books/george-pruitt-building-winning-trading-systems-with-tradestation.html) — practical implementation of systematic testing methodology similar in spirit to Kaufman's Part 3.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: trend-following, adaptive-moving-average, systems-testing, robustness, risk-management, price-shocks, overfitting
