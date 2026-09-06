# Intraday Timing for Low-Risk Swing Trading: the trader's summary

*A workshop handout on nesting weekly, daily, and intraday cycles to time swing entries with smaller price risk.*

**Walter Bressert** · 2000 · Swing Trading · advanced

*Source coverage: full. PDF pages inspected: 1-20. These are study notes, not verified trading results.*

## Overview

This short workshop handout outlines Walter Bressert's multi-timeframe cycle method. The objective is to trade daily swings in the direction of the weekly cycle while entering from intraday charts, where smaller bars permit tighter dollar risk. The document is chart-led and the OCR captures the explanatory text better than the graphics. It conveys the hierarchy and confirmation logic, but does not preserve every plotted threshold needed to reproduce the proprietary mechanical signals.

## Core thesis

Markets contain cycles within cycles. The higher timeframe determines directional preference; the lower timeframe supplies timing. In the S&P examples, a weekly cycle contains daily trading cycles, while a daily swing can be decomposed into 102-minute, 54-minute, and 20-minute cycles. A cluster of cycle lows across those scales creates a “nest.” Entering as the shortest scale confirms first can reduce initial risk while retaining exposure to the longer swing (PDF pp. 9-15).

## Key concepts

- **Dominant cycle** — The recurring bottom-to-bottom rhythm most useful on a chosen timeframe.
- **Weekly cycle** — The higher-order cycle used to define the trading trend.
- **Daily trading cycle** — The intermediate swing targeted for the position.
- **Cycle nest** — Coincident lows or highs on several timeframes.
- **Mechanical signal** — An oscillator turn after reaching a buy or sell zone.
- **RSI3M3** — Three-period RSI smoothed by a three-bar moving average (PDF p. 5).
- **Timing band** — A projected window for the next cycle top or bottom.
- **Right translation** — A cycle that spends more bars rising than falling, associated here with bullish structure.
- **Left translation** — A cycle whose peak occurs early, associated here with declining structure.
- **Setup bar** — The bar created when the oscillator turns from an extreme zone.

## Rules and setups

1. Establish the weekly-cycle direction. Favor daily-cycle bottom buys while it rises and daily-cycle top sells while it falls (PDF pp. 4-8).
2. Anticipate the daily swing. The handout says S&P daily swings commonly bottom three to five days after the prior swing low (PDF p. 3).
3. Move to a 102-minute chart divided into four equal bars per day. The featured cycle averages 18 bars, or roughly 4.5 trading days (PDF pp. 9-10).
4. Use timing bands to focus on the probable top or bottom window, then require an oscillator reversal rather than entering on elapsed time alone (PDF pp. 10-11).
5. Refine with 54-minute and, where appropriate, 20-minute charts. Each also uses an 18-bar cycle in the examples; two 54-minute cycles tend to fit within one 102-minute cycle (PDF p. 12).
6. Confirm from short to long timeframe: 20-minute first, then 54-minute, 102-minute, daily, and weekly. This sequence is the central entry logic for a cycle nest (PDF p. 14).
7. Read translation as a filter. More rising than falling bars supports the long case; an early high followed by a longer decline supports the short case (PDF p. 13).
8. Use multiple contracts only when risk permits. Take partial profits into strength and trail the remainder to participate in the longer swing (PDF p. 15).

The handout does not expose the oscillator-zone numbers or a complete stop formula, so its mechanical entry cannot be coded faithfully from this scan.

## Risk and money management

Risk reduction comes mainly from timeframe selection. A 20-minute entry bar is smaller than a daily bar, allowing a closer technical invalidation point, but ever-shorter charts add noise and false signals. Bressert considers 20 minutes about the practical lower bound for trading the 4.5-day swing (PDF pp. 14-15). Multi-contract entries make partial profit-taking possible, but the handout supplies no position-sizing formula, maximum account risk, or exact trailing-stop algorithm.

## Psychology and discipline

The framework asks traders to wait for alignment rather than predict every turn. Direction comes from the larger cycle; action waits for a smaller-cycle confirmation. This separation can reduce impulsive countertrend entries, provided the trader does not treat approximate cycle lengths as fixed schedules.

The handout also distinguishes preparation from commitment. A projected timing band narrows attention, but the trader still waits for the oscillator to reverse from its zone. That ordering matters psychologically: the calendar creates a watch window, while observed price and indicator behavior decide whether there is a trade at all (PDF pp. 10-11).

## Chapter map

- Workshop introduction — Objective, daily swings, and cycles within cycles (PDF pp. 2-3).
- Weekly and daily structure — Trend direction and oscillator confirmation (PDF pp. 4-8).
- 102-minute cycle — The 18-bar, roughly 4.5-day timing structure (PDF pp. 9-11).
- 54-minute refinement — Translation and nested confirmation (PDF pp. 12-13).
- 20-minute refinement — Cycle nests, noise, and multi-contract management (PDF pp. 14-15).
- Closing charts and workshop information — Mostly graphics and administrative material (PDF pp. 16-20).

## Strengths and caveats

The strongest idea is structural: use the higher chart for direction and the lower chart for controlled entry. The method also acknowledges the tradeoff between tighter bars and greater noise. However, several central claims are promotional or sample-specific. The handout advertises patterns “up to 90% accurate” without a documented test, and its timing-band illustration reports only nine tops and nine bottoms (PDF pp. 2, 11). The OCR loses chart detail, oscillator thresholds, setup-bar definitions, stop placement, and exit rules. The dated S&P session structure also means the exact 102-minute division may not transfer cleanly to current products and hours.

## Who should read it

Experienced swing traders studying cycle-based, multi-timeframe timing. It is useful as a conceptual workshop companion, but insufficient as a standalone rulebook or backtest specification.

## Related books in this library

- [The Fractal's Edge Basic User's Guide](https://ninad-k.github.io/trading-playbook/books/fractal.html) — Explores self-similar market structure from a broader theoretical angle.
- [Staying Out of Trouble Trading Currencies with Channels](https://ninad-k.github.io/trading-playbook/books/staying-out-of-trouble-trading-currencies-with-channels.html) — Uses a different form of structure to control entries and exits in currency markets.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: cycles, swing-trading, multi-timeframe, oscillators, timing
