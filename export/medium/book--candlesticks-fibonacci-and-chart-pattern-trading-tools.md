# Candlesticks, Fibonacci, and Chart Pattern Trading Tools: the trader's summary

*Merges Fibonacci retracements/extensions, candlestick reversal patterns, and 3-point chart patterns into a single confluence timing method, plus the proprietary PHI-ellipse tool.*

**Robert Fischer, Jens Fischer** · 2003 · Fibonacci, Gann & Elliott Wave · intermediate

*Source coverage: partial. PDF pages inspected: 7, 9, 27, 31, 33-34, 68, 70 (the PHI ratio derivations, extension and correction targets, and the worked trade tables). These are study notes, not verified trading results.*

## Overview

Robert and Jens Fischer argue that Fibonacci retracement/extension levels, candlestick reversal patterns, and classic 3-point chart formations (double/triple tops and bottoms, head and shoulders, triangles) all describe the same underlying investor-behavior phenomenon, and that trading them in combination produces materially better entries than any one tool alone. The book covers each tool separately (Ch. 2-5), then spends Ch. 6 explicitly merging them on real S&P 500, Microsoft, Allianz, and Dax 30 data to show the improvement. A secondary, proprietary tool — the PHI-ellipse, a Fibonacci-ratio-scaled ellipse fitted to a 3-wave price swing — gets a full chapter (5) and is presented as unifying the other three, since it geometrically "contains" 3-point patterns while using the same PHI ratios as the retracement/extension work.

## Core thesis

No single technical tool reliably times a trend reversal on its own; retracement levels alone generate too many false signals (the book's own backtest shows 9 trades, mostly losers, from a stand-alone 61.8% retracement rule on the S&P 500). Requiring confluence — a Fibonacci level reached and confirmed by a candlestick reversal pattern, a completed 3-point chart pattern, or the terminal point of a PHI-ellipse — filters out most false signals at the cost of entering later and catching a smaller piece of the move. The authors frame this as their central "synergistic strategy": tools traded individually leave money on the table or take needless losses; layering them earns the risk reduction the subtitle promises.

## Key concepts

- **PHI / PHI′** — the Fibonacci ratio 1.618 (PHI) and its reciprocal 0.618 (PHI′), derived from the ratio of consecutive terms in the Fibonacci summation series (1, 1, 2, 3, 5, 8, 13, 21...).
- **Retracement levels** — 38.2% (0.618 ÷ 1.618), 50.0% (not a true Fibonacci ratio but used as the midpoint), and 61.8% (1.000 ÷ 1.618) of a prior swing; the book concentrates on 61.8% as its default working level.
- **Price extension (3-wave)** — a target for wave 3 of a 3-wave move: swing 1 size × 1.618, added to the swing's starting point.
- **Price extension (5-wave)** — a target band for the end of wave 5, combining wave 1 × 1.618 and the wave-1-to-wave-3 amplitude × 0.618; a narrow band between the two is considered tradable, a wide one is discarded.
- **PHI-ellipse** — a proprietary ellipse whose major:minor axis ratio is a PHI-series number, drawn around a minimum 3-point swing (points A, B, C); the market's exit through the ellipse's outer boundary near its narrow end is the trade trigger.
- **3-point chart patterns** — double/triple tops and bottoms, head and shoulders, triangles, rectangles, flags, and wedges — all sharing "the magic figure three" (three peaks/valleys or three waves) as their organizing structure.
- **Confirmation candlestick patterns** — hammer/hanging man, bullish/bearish belt-hold, bullish/bearish engulfing, harami/harami cross, doji, piercing pattern/dark-cloud cover, morning star/evening star — used here as entry triggers after a Fibonacci level is reached, not as stand-alone setups.
- **Swing size** — the minimum basis-point (or price-unit) move required before a leg counts as a valid swing high/low; must be calibrated per instrument from historical data, since too small a swing size over-generates signals and too large a size generates none.
- **Trend channel / PHI-channel** — a parallel-line channel used as a secondary, independent confirmation alongside the PHI-ellipse for a "double confirmation" entry.
- **Elliott 5-wave count** — used as one more independent confirming input when a Fibonacci price target, a wave-1/wave-3 ratio target, and the wave count all converge near the same price.

## Rules and setups

The book's central tradable method — Fibonacci retracement plus candlestick or 3-point-pattern confirmation — is detailed with exact parameters in [The Fibonacci-Candlestick-Chart-Pattern Confluence Method](https://ninad-k.github.io/trading-playbook/books/candlesticks-fibonacci-and-chart-pattern-trading-tools--confluence-method.html). Other rule sets covered in the text:

1. **Stand-alone 61.8% retracement** (shown to underperform): swing size 30 basis points, immediate countertrend entry the instant the level is touched, stop at the prior swing high/low. The S&P 500 test (Dec 2001-Apr 2002) produced 9 trades and a net loss — the "before" case for the confluence approach.
2. **PHI-ellipse entry (daily data)**: wait for price to fully traverse a 3-wave swing inside the ellipse; enter on a break of its outer line, on a chart pattern forming at that break, or on a break of the line parallel to the median. Sell at the end of an upward-sloping ellipse, buy at the end of a downward-sloping one.
3. **PHI-ellipse entry (intraday)**: entry on the outer/median-parallel line break, or on a bar closing beyond it for a later fill; stop at the median line, a fixed basis-point distance (30 bp for Dax 30), or ratcheted to the most recent peak/valley; target at session end or a point distance equal to ellipse height; positions closed by end of day.
4. **Three-peaks/valleys signal**: sell when three peaks form at a PHI-ellipse's upper border and price breaks the median-parallel line down (mirror for buy signals on three valleys).
5. **Price extension entries**: after a completed 3- or 5-wave pattern, target the 1.618×swing-1 (and, for 5-wave, 0.618×wave-3) level(s) as a reversal zone for a countertrend entry.

## Risk and money management

Stop-loss placement is tool-specific: the prior swing high/low for retracement trades, the PHI-ellipse's median line (or a fixed basis-point distance, or a ratcheted new peak/valley) for ellipse trades. Trailing stops apply once in profit — the confluence examples use a 3-day high/low trailing stop. Profit targets are similarly tool-specific: 0.618× or 1.618× the initiating swing size for retracement/extension trades, or the triggering PHI-ellipse's height for ellipse trades. The book gives no percent-of-equity risk-per-trade rule or position-sizing formula; risk management here means signal filtering (confluence) and stop/target placement, not capital allocation.

## Psychology and discipline

Chapter 1 (Trading Psychology and Investor Behavior) frames all of the book's chart tools as visualizations of collective investor behavior rather than as mechanical price triggers — the recurring "figure three" pattern is presented as evidence that crowds reverse decisions in a repeatable rhythm. The authors are explicit that a countertrend entry at the terminal point of a Fibonacci tool (retracement, extension, or PHI-ellipse) requires real discipline because it means selling into strength or buying into weakness with no immediate market support for the trade, and that this is precisely where a stand-alone signal fails without the added patience of waiting for confirmation. They also stress patience with false breakouts and multiple whipsaws as a normal cost of the strategy, particularly on shorter (intraday) timeframes.

## Chapter map

- Ch 1 — Trading Psychology and Investor Behavior — why chart patterns encode repeatable crowd behavior.
- Ch 2 — The Magic Figure Three — the shared three-wave/three-point structure across all of the book's chart tools.
- Ch 3 — Basic Principles of Trading Strategies — Fibonacci ratios and the summation series; candlestick pattern catalogue; chart pattern basics; trend lines and channels.
- Ch 4 — Applications of Trading Strategies — double tops/bottoms; Fibonacci price corrections and extensions (3-wave and 5-wave); candlestick chart patterns in practice; 3-point patterns for trend reversals; PHI-channel applications.
- Ch 5 — PHI-Ellipses — construction and parameters; working with PHI-ellipses on daily and intraday data; constant-scale backtests on the Japanese Yen, S&P 500, and Dax 30; reliability assessment.
- Ch 6 — Merging Candlesticks, 3-Point Chart Patterns, and Fibonacci Tools — the book's core confluence method, tested on the S&P 500, Microsoft, and Allianz.
- Appendices — WINPHI software tutorial and user manual (the authors' companion charting/backtesting tool); abbreviations; disclaimer.

## Strengths and caveats

The confluence chapter is unusually transparent for a Fibonacci-strategy book: it shows the stand-alone retracement strategy's actual trade log, losses included, before showing the improved results with candlestick and 3-point-pattern confirmation, rather than only cherry-picked winners. That said, all worked examples use a handful of instruments over short windows (roughly 4-12 months each) — a thin sample for the reliability claims made; the book cites Bulkowski's pattern-reliability statistics for 3-point patterns but runs no equivalent large-sample test on its own combined method. The PHI-ellipse is proprietary and non-standard — it appears under this name nowhere else in the literature, its construction depends on the authors' own undisclosed "Fischer-transformed" formula, and reproducing it requires their WINPHI software rather than a generic charting platform. Swing size, a critical parameter throughout, is stated to require per-instrument historical calibration with no general formula given.

## Who should read it

Discretionary swing traders already comfortable with basic Fibonacci retracement/extension work and candlestick pattern recognition who want a structured way to combine them rather than trade either in isolation; less useful for a trader wanting a fully mechanical, backtestable system, since swing size, stop placement, and PHI-ellipse construction all retain a discretionary, chart-reading component.

## Related books in this library

- [Fibonacci Applications and Strategies for Traders](https://ninad-k.github.io/trading-playbook/books/fischer-robert-fibonacci-applications-and-strategies-for.html) — Robert Fischer's earlier, more focused treatment of Fibonacci retracement and extension trading that this book builds on and extends with candlesticks and PHI-ellipses.
- [Elliott Wave Principle](https://ninad-k.github.io/trading-playbook/books/elliott-waves-principle.html) — the wave-counting framework this book borrows its 3-wave/5-wave structure and extension targets from.
- [Candlestick Charting Explained](https://ninad-k.github.io/trading-playbook/books/greg-morris-candlestick-charting-explained.html) — a deeper reference for the individual candlestick patterns used here only as confirmation triggers.
- [Candlestick Charting Explained](https://ninad-k.github.io/trading-playbook/books/candlestick-charting-explained.html) — Nison's foundational candlestick text, useful background for the patterns cited in Chapter 3.
- [Fibonacci Studies (AIQ TradingExpert Pro Reference Manual excerpt)](https://ninad-k.github.io/trading-playbook/books/fibonacci-studies.html) — a shorter companion reference on Fibonacci ratio applications in trading.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: fibonacci, candlesticks, chart-patterns, phi-ellipse, confluence, retracement, 3-point-patterns, elliott-wave
