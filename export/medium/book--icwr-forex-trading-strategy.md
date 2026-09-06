# ICWR Forex Trading Strategy: the trader's summary

*A fully mechanical Fibonacci-retracement system (the Impulsive/Corrective Wave Retracement phenomenon) with precise entry, exit and stop rules for both intraday (5-min) and long-term (4-hour) forex trading.*

**Quantum Globe Inc.** · 2005 · Fibonacci, Gann & Elliott Wave · intermediate

*Source coverage: partial. PDF pages inspected: 1, 5, 7, 9, 12-13, 15, 18, 37 (leverage arithmetic, the Fibonacci level set, the worked intraday examples and the stop-loss rules). These are study notes, not verified trading results.*

## Overview

This self-published manual (Quantum Globe Inc., 2005, ISBN 0-0997773-04) presents a single, complete trading method for the forex spot market: the "Impulsive/Corrective Wave Retracement" (ICWR) Trading Rules. The core observation — framed as an original discovery by the authors — is that corrective price waves against a trend tend to retrace the preceding impulsive wave in the same Fibonacci ratios (25%, 38%, 50%, 61.8%, 75%) that Elliott Wave practitioners have long used to describe stock and index price structure. The book builds a fully mechanical entry/exit/stop-loss system around this observation, offers a chapter of self-reported backtest and parameter-sensitivity results, and walks through several full worked trading examples (EUR/USD and USD/CAD intraday; EUR/USD and GBP/USD long-term) with real historical price levels and timestamps.

## Core thesis

Markets alternate between impulsive waves (moves in the direction of the prevailing trend) and corrective waves (counter-trend retracements), and the depth of each corrective retracement, measured against the impulsive wave that preceded it, clusters around standard Fibonacci ratios. By mechanically tracking the most recent significant price swing (the "active wave"), drawing Fibonacci retracement levels from its extremes, and waiting for a full candlestick close beyond a specific confirmation level (0.250 or 0.750), a trader can generate objective, repeatable bullish/bearish signals for both entries and exits — removing subjective judgment from trade timing. A single momentum filter (a 14-period RSI relative to the 50 midline on the daily chart) is layered on top to align trades with a longer-term bias.

## Key concepts

- **Impulsive wave** — a price movement in the direction of the prevailing longer-term trend.
- **Corrective wave** — a price movement against the prevailing trend, typically shorter and shallower than the impulsive wave it follows.
- **ICWR phenomenon** — the book's central claim: corrective waves retrace their prior impulsive wave in Fibonacci ratios (25%, 38%, 50%, 61.8%, 75%), described as a "self-similarity effect" analogous to patterns found in other complex systems.
- **Active wave** — the most recent qualifying price swing (minimum height threshold) nearest to the current time; the base unit the system tracks and re-draws Fibonacci levels from as new swings form.
- **Retracement channel** — the price zone between the 0.382 and 0.618 Fibonacci levels; a candlestick closing inside this channel "triggers" the setup and activates the confirmation levels.
- **Confirmation levels** — the 0.250 (lower) and 0.750 (upper) Fibonacci levels; a full candlestick closing beyond one of these, after the retracement channel has been triggered, generates a bullish or bearish signal depending on the active wave's direction.
- **RSI(1-day; 50/50) filter** — the long-term momentum filter used to align entries with the broader trend: only take bullish ICWR signals when the daily 14-period RSI is above 50, and only bearish signals when it is below 50.
- **Hard stop order** — a fixed-pip stop-loss (50 pips intraday, 100 pips long-term) placed immediately on entry as a backstop independent of the ICWR exit signal.
- **"Let profits run"** — the book's framing of its exit logic: rather than a fixed profit target or trailing stop, the position is held through multiple corrective waves as long as none of them breaches the 0.750/0.250 confirmation level, only exiting on an opposite ICWR signal or the hard stop.

## Rules and setups

The complete mechanical rule set — active wave identification, Fibonacci level construction, the four signal cases (downward/upward impulsive and corrective waves), RSI entry filter, and both the intraday (5-minute, 40-pip minimum wave, 50-pip stop) and long-term (4-hour, 150-pip minimum wave, 100-pip stop) parameter sets — is documented in full on the linked system page: [The ICWR Trading Rules](https://ninad-k.github.io/trading-playbook/books/icwr-forex-trading-strategy--icwr-trading-rules.html). In brief: identify the nearest qualifying price swing (the active wave), draw Fibonacci levels from its extremes, wait for a full candlestick to close beyond the 0.750 or 0.250 confirmation level (after first closing inside the 0.382–0.618 retracement channel), confirm direction with the daily RSI relative to 50, enter on that combined signal, and exit either on an opposite signal or a fixed hard stop.

## Risk and money management

The book's only formal risk control is the hard stop-loss (50 pips intraday, 100 pips long-term), sized as a fixed distance from entry rather than as a percentage of account equity or based on volatility. It illustrates position sizing purely through leverage mechanics: a worked example uses $5,000 of capital at 1:20 leverage (controlling $100,000 notional) on a single EUR/USD position, explicitly warning that at higher leverage (e.g., 1:50) a roughly 2% adverse move can wipe out the entire account, and recommending beginners cap leverage at 1:20 until "comfortable and profitable." No per-trade percentage-of-equity risk cap, no diversification guidance across multiple simultaneous positions, and no explicit maximum-drawdown or position-count limit are given — money management is essentially reduced to "use a hard stop and don't over-leverage."

## Psychology and discipline

The book's discipline message is narrow but repeated throughout: the central behavioral lesson is "cut losses short and let profits run," illustrated with the arithmetic that two 50-pip losses followed by an 80-pip win nets a loss, while two 50-pip losses followed by a 250-pip win (achievable, the authors argue, only by not exiting prematurely) nets a solid profit. The book explicitly frames premature exits — closing a winning trade too early out of fear — as the main psychological trap the ICWR exit rule is designed to remove by replacing discretionary judgment with an objective signal.

## Chapter map

- Ch 1 — Introduction — case for trading forex, leverage mechanics, and the initial statement of the ICWR phenomenon with a simplified worked exit example.
- Ch 2 — Scientific Research — the authors' self-reported development process, backtest results (net pips with/without various long-term filters), and parameter-sensitivity ("consistency") charts.
- Ch 3 — The Intraday ICWR Trading Rules — full formal rule set for 5-minute chart trading: active wave recognition, Fibonacci construction, the four signal cases, RSI entry filter, exit/stop rules.
- Ch 4 — Intraday EUR/USD Trading Example — full worked walkthrough.
- Ch 5 — Intraday CAD/USD Trading Example — full worked walkthrough.
- Ch 6 — The Long-Term ICWR Trading Rules — the same rule set restated with 4-hour-chart parameters (150-pip active wave, 100-pip stop).
- Ch 7 — Long-Term EUR/USD Trading Example — full worked walkthrough.
- Ch 8 — Long-Term GBP/USD Trading Example — full worked walkthrough.

## Strengths and caveats

The rule set itself is unusually explicit and complete for a retail forex product — every entry, filter, and exit condition is spelled out precisely enough to code directly, and the worked examples show real price levels, timestamps, and pip/dollar outcomes rather than vague chart annotations. That said, this is a self-published, heavily promotional product (marketed with "crack team of PhDs" and "knee to the groin" language, sold as a proprietary discovery), and its "Scientific Research" chapter, while presenting backtest figures (e.g., ~2,700–3,900 pips net over what appears to be a 5-month parallel test of three pairs, informed by "two years" of historical data), does not disclose methodology in enough detail to independently verify: sample size, date ranges, whether spread/slippage/commission were modeled, drawdown statistics, and out-of-sample validation are all absent. The claim that the ICWR/Fibonacci-retracement effect is a novel, "until now unpublished" discovery overstates its originality — Fibonacci retracement analysis of impulsive/corrective wave structure is a long-standing feature of Elliott Wave theory that predates this book by decades. The strategy also depends on subjective judgment at the margins (identifying "the" active wave among several candidate swings, and drawing wave endpoints precisely) despite its mechanical framing.

## Who should read it

Retail forex traders who want a fully specified, rule-based Fibonacci/Elliott-Wave-adjacent method they can test and automate, and who are comfortable independently verifying the book's backtest claims before risking capital. Not recommended as a source of statistical proof of an edge — treat the performance figures as illustrative rather than validated, and expect to run independent testing before live use.

## Related books in this library

- [Day Trading the Currency Market](https://ninad-k.github.io/trading-playbook/books/day-trading-the-currency-market.html) — a more rigorously documented FX day-trading book with comparable rule-based technical strategies for direct comparison.
- [Elliott Wave Principle](https://ninad-k.github.io/trading-playbook/books/elliott-waves-principle.html) — the foundational impulsive/corrective wave framework this book's Fibonacci-retracement rules are built on top of.
- [Fibonacci Applications and Strategies for Traders](https://ninad-k.github.io/trading-playbook/books/fischer-robert-fibonacci-applications-and-strategies-for.html) — a deeper, more academically grounded treatment of Fibonacci ratios in trading.
- [Practical Fibonacci Methods for Forex Trading](https://ninad-k.github.io/trading-playbook/books/forex-systems-research-practical-fibonacci-methods-for-forex-trading-2005.html) — another practical Fibonacci-based forex method for cross-reference.
- [Come Into My Trading Room](https://ninad-k.github.io/trading-playbook/books/come-into-my-trading-room-elder-alexander.html) — useful counterpoint on trade-journaling, discipline, and system validation discipline the ICWR book largely skips.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: forex, fibonacci, elliott-wave, retracement, rsi, mechanical-system, eur-usd
