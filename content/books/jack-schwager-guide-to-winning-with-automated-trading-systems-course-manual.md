---
title: Jack Schwager's Guide to Winning with Automated Trading Systems
author: Jack Schwager
year: unknown
slug: jack-schwager-guide-to-winning-with-automated-trading-systems-course-manual
tier: A
category: Trend Following & Mechanical Systems
tags: [mechanical-systems, trend-following, counter-trend, breakout, system-design, backtesting, whipsaw]
difficulty: intermediate
doc_type: course
pages: 95
one_liner: "A slide-driven course surveying trend-following, counter-trend, and pattern-based mechanical systems, and how to read a system's backtest performance report."
related: [jack-schwager-stock-market-wizards, michael-covel-trend-following, richard-l-weissman-mechanical-trading-systems, mechanical-trading-systems, position-sizing]
source_file: "Jack Schwager - Guide To Winning With Automated Trading Systems (Course Manual).pdf"
---

## Overview

This is the slide/workbook companion to a Jack Schwager video course on mechanical (automated) trading systems, not a prose book. Almost all of its content is chart images with brief on-slide captions and system-performance report screenshots (TradeStation-style "System Report: Performance Summary" tables), built around a handful of illustrative markets: the Deutsche Mark, Allied Signal, COMEX Gold, Aluminum Co. of America, Sugar #11, and Caterpillar. The course walks through the main families of mechanical systems — channel breakout, moving-average crossover, counter-trend band trading, gap/pattern-based systems, and consecutive-close systems — using real chart examples to show where each works well and where it fails, and uses the accompanying performance-summary tables to teach the standard vocabulary for evaluating a system's backtest.

## Core thesis

A mechanical trading system's value comes from removing emotion and inconsistency from trading, but no single system type works in all market conditions: trend-following systems only pay off during sustained trends and will give back a meaningful share of open profit before their reversal signal fires, while counter-trend (band-fade) systems do well in choppy, range-bound markets and are hurt in strong trends. The course's implicit argument, made through repeated chart examples, is that understanding *which* market regime a system is built for — and reading its full performance report rather than just its net profit — is what separates disciplined system trading from curve-fit slide-ware.

## Key concepts

- **Mechanical/automated trading system** — a fully rule-based system that generates buy/sell signals without discretionary judgment, so it can be applied consistently and tested statistically.
- **Trend-following system** — a system (e.g., channel breakout, moving-average crossover) designed to catch sustained directional moves; by construction it gives back part of its open profit before the trend-reversal signal triggers.
- **Channel/range breakout system** — enters when price closes beyond the highest high or lowest low of the past N days (the course's example: an 80-day breakout).
- **Moving-average crossover system** — enters/exits when a faster moving average crosses a slower one (example: a 10-day/50-day crossover).
- **Counter-trend (band) system** — enters against short-term extremes, buying near a lower band and selling near an upper band (example: an "ADTR Band Counter-trend" system with a 60-day lookback and a band multiplier k = 3); profits in choppy/range-bound markets, loses in trending ones.
- **Pattern/gap-based system** — trades specific chart patterns such as price gaps (distinguishing, e.g., a 1-day gap from a 5-day gap) and defines stops relative to the gap.
- **Consecutive-close system** — enters after N consecutive up or down closes (example: N = 3 on Caterpillar), with variants adding a "reverse condition" or additional filter/stop rules.
- **Whipsaw** — a losing trade caused by a stop or filter reacting to noise rather than a real move; the course explicitly flags that adding more stop/filter rules to a system can increase whipsaws rather than improve results.
- **Performance-summary metrics** — the standard backtest vocabulary used throughout: total net profit, gross profit/gross loss, number of trades, percent profitable, average winning/losing trade, ratio of average win to average loss, max consecutive winners/losers, average bars in winners/losers, max intraday drawdown, profit factor, max contracts held, account size required, and return on account.

## Rules and setups

The manual is a survey of several distinct system *types* used as teaching examples, not one single tradable method, so the concrete parameters shown are illustrative rather than a recommended system:

1. **80-day breakout**: go long (or short) when price closes beyond the highest high (or lowest low) of the prior 80 days; described as working "very well when there are sustained trends" and poorly otherwise.
2. **10/50 moving-average crossover**: signals on the crossover of a 10-period and 50-period moving average; the slides note it "works well in trending periods" and shows "excellent signals during trending periods" in the DM and Allied Signal examples.
3. **ADTR Band Counter-trend (60-day, k = 3)**: a volatility-band system (average true range–based) that buys near the lower band and sells/shorts near the upper band; the course notes it thrives in a "choppy trading range" (both buy and sell signals profitable) but is hurt by strong trends, and that exiting at the band's median (rather than the far band) "significantly reduces profit during a choppy trading range."
4. **Gap-based pattern system (Sugar #11 example)**: distinguishes a downside gap of one day's duration from a five-day gap, and defines/redefines the protective stop relative to the most recent downside gap; the slides flag that in this style of system a loss can be "theoretically unlimited" without an explicit stop.
5. **Consecutive Close (N = 3) system, with variants**: enters after three consecutive closes in one direction; a "Reverse Condition" variant is shown, and a further version adding a stop rule is explicitly captioned "Stop rule creates many whipsaws" — a direct, in-text warning that piling filters/stops onto a base system can degrade it.

No universal position-sizing, entry, or stop rule applies across all five system types; each example carries its own parameters (N-day lookback, band width, moving-average lengths) as shown above.

## Risk and money management

The course teaches risk almost entirely through the backtest report rather than as prescriptive money-management rules: **max intraday drawdown** (the largest peak-to-trough equity dip during the test) and **account size required** (roughly, the drawdown plus a margin buffer) are presented as the two figures that define how much capital and pain a system demands, alongside **profit factor** (gross profit ÷ gross loss) as the summary measure of reward relative to risk. Sample performance tables in the course show profit factors ranging from roughly 1.1 to nearly 8 and returns on account from under 30% to over 700%, depending on the system and market — illustrating how dramatically results vary by regime and parameter choice rather than establishing one "correct" risk level. The gap-system slide's warning that losses can be "theoretically unlimited" without a defined stop is the closest thing to an explicit risk-control principle in the sampled material: every system needs a stop, but that stop should not be so tight or over-engineered (multiple filters) that it manufactures whipsaws.

## Psychology and discipline

The course opens by listing the discipline case for mechanical systems directly: they eliminate emotion, eliminate the need for constant discretionary decision-making, ensure a consistent approach applied uniformly across many markets, provide built-in risk control, and — critically — can be tested for statistical reliability before real money is risked, which a discretionary approach cannot. This framing (drawn explicitly from Schwager's "Market Wizards" interviews) positions automation not as a shortcut but as a discipline-enforcement mechanism: once a system is chosen, its signals are followed mechanically rather than second-guessed trade by trade.

## Chapter map

- Section 1 — An Overview of Trading Systems and Why You Should Use Them — the case for mechanical systems; six stated benefits.
- Section 2 — Defining and Illustrating the Leading Types of Trading Systems — breakout, moving-average crossover, and counter-trend band systems, shown on the Deutsche Mark, Allied Signal, and COMEX Gold, with full performance-report examples.
- Section 3 — Taking Advantage of Charts by Using Pattern Systems — gap-based and consecutive-close pattern systems, shown on Sugar #11 and Caterpillar, including a full performance-report example and a caution against over-adding stop/filter rules.

## Strengths and caveats

The available text is overwhelmingly chart captions and screenshotted performance tables rather than connected prose explaining methodology, statistical caveats, or curve-fitting pitfalls in depth — this course leans heavily on its (unavailable to this note-taker) video narration, so the written manual alone is a skeletal companion rather than a self-contained text. The specific parameter sets shown (80-day breakout, 10/50 crossover, 60-day/k=3 band, N=3 consecutive close) are presented as single, un-optimized illustrations on a handful of markets and date ranges (mostly late 1980s–1990s); no out-of-sample or walk-forward validation, multi-market robustness testing, or explicit curve-fitting warnings appear in the sampled pages, even though the "stop rule creates many whipsaws" caption gestures at the danger of over-fitting a system with too many added rules.

## Who should read it

Traders who want a concrete, visual introduction to the major families of mechanical system logic (breakout, moving-average, counter-trend/band, gap, and consecutive-close) and to the standard vocabulary of a system backtest report (profit factor, drawdown, win/loss ratios, return on account), before moving to a fuller treatment of system design, optimization, and validation.

## Related books in this library

- [[jack-schwager-stock-market-wizards]] — Schwager's interview-based companion work; source of the "most important lesson" framing this course opens with.
- [[michael-covel-trend-following]] — a fuller treatment of the trend-following system philosophy this course surveys.
- [[richard-l-weissman-mechanical-trading-systems]] — a deeper, more systematic treatment of mechanical system design and testing.
- [[mechanical-trading-systems]] — another general mechanical-systems reference for cross-checking design principles.
- [[position-sizing]] — covers the money-management layer this course's backtest reports touch on (drawdown, account size) but do not develop into rules.

## Caveats

These notes are based on OCR of a sampled subset of pages of a scanned, slide-heavy course manual; total extractable text across all 95 pages was only about 1,400 words, consisting almost entirely of chart titles, axis labels, brief captions, and performance-report screenshots rather than connected narrative. Most explanatory content in this course likely lives in the accompanying video, not in this manual, so these notes describe only what could be reconstructed from the sampled slide text and chart captions and should be treated as a skeleton of the course's content rather than a complete summary.
