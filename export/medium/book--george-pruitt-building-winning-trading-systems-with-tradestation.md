# Building Winning Trading Systems with TradeStation: the trader's summary

*A TradeStation/EasyLanguage programming course built around six full turnkey mechanical systems, each backtested 1982-2002 across 17 futures markets.*

**George Pruitt, John R. Hill** · 2003 · Trend Following & Mechanical Systems · intermediate

*Source coverage: partial. PDF pages inspected: 1-2, 5, 8-10, 130, 134, 176 (the EasyLanguage chapters, the ChoppyMarketIndex function and the system performance tables with their test protocol). These are study notes, not verified trading results.*

## Overview

Pruitt (Futures Truth Company) and Hill co-wrote this as a hybrid programming manual and system-design casebook for TradeStation's EasyLanguage. The first half teaches the language itself — variables, control structures, indicators, PaintBars, functions, strategies, and how to read and optimize TradeStation's performance reports. The second half (Chapter 6, "The Big Damn Chapter on Trading Strategies") is the book's real payload: six complete, non-curve-fit mechanical systems presented as trading idea, pseudocode, full EasyLanguage source, and a 1982-2002 backtest table across 17 futures markets. Later chapters cover debugging, using TradeStation as a research tool, options basics, and transcribed interviews with system developers (Welles Wilder, John Ehlers, Charles Le Beau, Larry Williams, and others).

## Core thesis

A trading system is only as good as the programmer's ability to translate an idea into exact, testable rules, and EasyLanguage removes the barrier between "I have an idea" and "I can prove or disprove it on 20 years of data." The authors argue that robust systems use the same one or two parameter sets across many unrelated markets rather than being curve-fit market by market — if a system needs different settings for the Japanese Yen and live cattle, it is likely fitted to noise, not principle. They repeatedly demonstrate this by running each system, unmodified, across 17 futures markets and accepting that it will lose money in some (grains, in particular) rather than patching in ad hoc filters. Optimization is treated as a necessary but dangerous tool: useful for tuning within a plausible range, destructive when used to chase the single best historical result.

## Key concepts

- **EasyLanguage** — TradeStation's Pascal-derived programming language for indicators, strategies, and studies; compiled, English-like, with reserved words, skip words, and three data types (Numeric, Boolean, String).
- **Pseudocode-to-code workflow** — the book's method for building any system: describe the idea in plain English, formalize it as half-English/half-code pseudocode, then translate to exact EasyLanguage.
- **Profit factor / adjusted profit factor** — gross profit ÷ gross loss, normalized so it can compare performance across unrelated markets; the adjusted version deflates wins and inflates losses (using the square root of trade counts) to discount lucky outlier trades.
- **Walk-forward testing** — splitting history in half, optimizing on the first half and validating on the untouched second half (or testing on older out-of-sample data) before trusting a parameter set.
- **Optimization peaks vs. plateaus** — on a 3-D surface chart of two optimized parameters, a "peak" result is fragile (small parameter changes collapse performance) while a "plateau" of consistently good results nearby is considered robust.
- **Adaptive engine** — a function that changes a system's own parameter (e.g., look-back length) daily based on a market statistic such as volatility, instead of using one fixed value.
- **ChoppyMarketIndex** — a custom function, `Abs(Close-Close[29])/(Highest(High,30)-Lowest(Low,30))*100`, that scores 0-100 how directional (high) versus congested (low) a market currently is; used to switch a system between trend and swing logic.
- **True range vs. range** — true range extends the high-low range to include the prior close, capturing gap moves; used throughout for volatility-based stops and bands.
- **Ghost/paper trading filter** — simulating a system's trades in the background and only firing a live signal when a chosen condition (e.g., the last simulated-or-real trade was a loser) is met.
- **Market normalization** — sizing positions so a dollar of risk means the same thing across markets with very different volatility and contract values (e.g., bonds vs. soybeans).
- **Sharpe ratio / K-ratio / Rina Index** — normalized consistency statistics used alongside total net profit and drawdown to judge a system.

## Rules and setups

The book documents six complete turnkey systems in Chapter 6, each with its own authoritative rule set as a system sub-page in this library: [The King Keltner Trading Strategy (Full System)](https://ninad-k.github.io/trading-playbook/books/george-pruitt-building-winning-trading-systems-with-tradestation--king-keltner.html), [The Bollinger Bandit Trading Strategy (Full System)](https://ninad-k.github.io/trading-playbook/books/george-pruitt-building-winning-trading-systems-with-tradestation--bollinger-bandit.html), [The Thermostat Trading Strategy (Full System)](https://ninad-k.github.io/trading-playbook/books/george-pruitt-building-winning-trading-systems-with-tradestation--thermostat.html), [The Dynamic Break Out II Strategy (Full System)](https://ninad-k.github.io/trading-playbook/books/george-pruitt-building-winning-trading-systems-with-tradestation--dynamic-break-out-ii.html), [The Super Combo Day Trading Strategy (Full System)](https://ninad-k.github.io/trading-playbook/books/george-pruitt-building-winning-trading-systems-with-tradestation--super-combo.html), and [The Ghost Trader Trading Strategy (Full System)](https://ninad-k.github.io/trading-playbook/books/george-pruitt-building-winning-trading-systems-with-tradestation--ghost-trader.html). Two book-wide rules apply across all of them:

1. **Backtest protocol.** Every system is tested 1982-2002 (or a stated sub-period) across the same 17-market futures basket, with a flat $75 commission/slippage assumption per trade, and reported per-market rather than as a blended portfolio equity curve.
2. **One parameter set per system.** The authors deliberately use identical parameters across all markets (e.g., King Keltner's 40/40) rather than optimizing per instrument, arguing this is the better test of whether a principle is real; they concede sector-level parameter grouping (e.g., one setting for all currencies) is a defensible middle ground.

A seventh construct, the **Money Manager** template (Chapter 6), demonstrates position sizing around illustrative trading rules: `numContracts = (initCapital × riskPercent) / marketRisk`, where `marketRisk = StdDev(Close,30) × BigPointValue`. The code rounds down to a whole contract, then enforces a minimum of one contract. Its example uses 40-bar high/low breakout entries and opposite 20-bar low/high exits. The authors present it primarily as a platform for developing money management, with volatility-normalized sizing rather than a fixed contract count. (PDF pp. 170–172; printed pp. 153–155.)

## Risk and money management

Individual systems carry their own exits: King Keltner and Bollinger Bandit exit at a moving average (win or lose); Dynamic Break Out II and Thermostat use volatility-scaled trailing stops; Super Combo uses a percent-of-range protective stop that moves to breakeven and then trails. None of the six includes account-level position sizing — the authors are explicit that a "money management overlay" (like the Money Manager template) must be added before any becomes a full trading program. The book's implicit risk message is diversification: these are long-term trend followers that "require heavy capitalization," can run for years without profit in any single market, and are only viable traded across a basket. No fixed percent-of-equity rule is prescribed in the core chapter; the Money Manager example uses a 2% risk input, but presents it as illustrative, not a house rule. The example uses initial capital and a volatility proxy, so 2% is not a guaranteed maximum loss. Its minimum-one-contract instruction can exceed even that nominal allocation when the calculated size is below one; this exception needs explicit review before implementation. (PDF pp. 170–172; printed pp. 153–155.)

## Psychology and discipline

The book is light on psychology compared to trading-mindset titles, but it makes a few pointed arguments: sub-50% win rates are normal and acceptable for trend-following breakout systems, provided the average win is large relative to the average loss, and traders should not abandon a system after a string of small losing breakouts if that is its known character. On optimization, the authors warn against "curve-fit until it looks perfect" behavior — the temptation to run thousands of parameter combinations in search of a mythical best result — and recommend a disciplined, stepwise process (optimize the two most important parameters first, validate for robustness, then move to the next pair) instead.

## Chapter map

- Ch 1 — Fundamentals — EasyLanguage syntax, data types, and TradeStation 2000i/6.0 basics.
- Ch 2 — EasyLanguage Program Structure — structured programming and program headers.
- Ch 3 — Program Control Structures — If-Then, If-Then-Else, For/While loops.
- Ch 4 — TradeStation Analysis Techniques — indicators, PaintBar/ShowMe studies, functions, strategies.
- Ch 5 — Measuring Trading System Performance and System Optimization — reading the Summary/Analysis/Graphs reports, profit factor, Sharpe/K-ratio, optimization and walk-forward testing.
- Ch 6 — Trading Strategies That Work — the six full systems (King Keltner, Bollinger Bandit, Thermostat, Dynamic Break Out II, Super Combo, Ghost Trader) plus the Money Manager position-sizing template.
- Ch 7 — Debugging and Output — syntax vs. logical errors, Print Log debugging technique.
- Ch 8 — TradeStation as a Research Tool — Commitment of Traders reports, day-of-week/time-of-day analysis, pattern recognition, intermarket analysis.
- Ch 9 — Using Percent Change Charts to Track Relative Performance.
- Ch 10 — Options — contract basics, the Greeks, and single/combination option strategies.
- Ch 11 — Interviews with Developers — Wilder, Clayburg, Fitschen, Ehlers, Le Beau, Larry Williams, and others on system design philosophy.
- Appendices — EasyLanguage syntax errors, source code listings, reserved-word reference.

## Strengths and caveats

The systems are unusually transparent for a published book — full source code, exact parameters, and a 20-year, 17-market backtest table for each, letting a reader verify rather than take on faith. The consistent-parameter, multi-market testing approach is a genuine defense against curve-fitting that many system books skip. Caveats: backtests use flat $75 commission/slippage assumptions with no walk-forward or true out-of-sample validation, and results are shown per-market rather than as a combined portfolio equity curve, so real drawdown and correlation effects across simultaneous positions are never demonstrated. Every system underperforms in grain markets, which the authors acknowledge but do not solve (their own fade and seasonal-filter experiments on soybeans both lose money). The book is dated on tooling — it targets TradeStation 2000i/6.0 — and none of the systems account for the post-2000s shift to smaller tick sizes, electronic execution, or higher-frequency competition, so live performance should not be assumed to match the 1982-2002 figures.

## Who should read it

Systematic futures traders and programmers who want to see complete, working mechanical systems end-to-end — idea, pseudocode, code, and multi-market backtest — rather than a black-box description of a strategy. Also useful for anyone learning EasyLanguage who wants realistic, non-trivial example programs (multi-data-stream day trading, adaptive parameters, trade-outcome-dependent filters) instead of toy demonstrations.

## Related books in this library

- [The Dynamic Break Out II Strategy](https://ninad-k.github.io/trading-playbook/books/dynamic-breakout-ii-strategy.html) — a shorter Tier B excerpt of the same system; this book's sub-page is the fuller version with complete pseudocode and source.
- [The King Keltner Trading Strategy](https://ninad-k.github.io/trading-playbook/books/king-keltner-trading-strategy.html) — likewise, an existing shorter excerpt this book covers in full.
- [The Ghost Trader Trading Strategy](https://ninad-k.github.io/trading-playbook/books/ghost-trader-trading-strategy.html) — the same relationship for the Ghost Trader trade-filtering template.
- [What Is a Trading System?](https://ninad-k.github.io/trading-playbook/books/van-tharp-trading-systems.html) — complements this book's system-construction focus with the business-plan and position-sizing side Pruitt and Hill leave to a single template.
- [Way of the Turtle](https://ninad-k.github.io/trading-playbook/books/curtis-faith-way-of-the-turtle.html) — another fully disclosed, rules-based trend-following system with multi-market backtesting, useful for comparison.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: tradestation, easylanguage, mechanical-systems, backtesting, optimization, bollinger-bands, keltner-channel, donchian-breakout, day-trading, money-management
