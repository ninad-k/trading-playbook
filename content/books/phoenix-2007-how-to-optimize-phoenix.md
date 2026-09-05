---
title: "How to Optimize Phoenix's Settings"
author: "VinceTheBeast"
year: 2007
slug: phoenix-2007-how-to-optimize-phoenix
tier: B
category: Trend Following & Mechanical Systems
tags: [forex, expert-advisor, metatrader, optimization, backtesting, envelope, walk-forward]
difficulty: intermediate
doc_type: manual
pages: 10
one_liner: "A forum-written walkthrough for optimizing the settings of the 'Phoenix' MetaTrader expert advisor using the Strategy Tester's parameter-sweep function."
related: [automated-forex-ea, trade-easy-with-an-automated-forex-trading-system, how-effective-is-automated-forex-trading, jack-schwager-guide-to-winning-with-automated-trading-systems-course-manual]
source_file: "Phoenix-2007-How-To-Optimize-phoenix.pdf"
---

## Summary

A community-written how-to guide for optimizing the parameters of "Phoenix," a MetaTrader4 forex expert advisor (EA) built by a user named "Hendrick." It is a software/process manual, not a strategy description: it walks through the MetaTrader Strategy Tester UI, setting up baseline data (six months, M15 bars, "every tick" modeling), verifying settings transferred correctly, then running iterative parameter sweeps (coarse range first, then narrowed range) on the EA's signal parameters, followed by take-profit/stop-loss, and finally risk-management add-ons (trailing stop, break-even, close-after-hours).

## Key points

- Optimizing improves back-tested results but is explicitly stated to be no guarantee of live-account performance.
- The EA's settings (currency pair, timeframe, TP, SL, and each signal) are described as needing to be kept "in balance" — changing one parameter requires re-optimizing the others rather than tweaking in isolation.
- Recommended workflow: optimize each signal parameter individually first (coarse step size, then a narrower range around the best result), only optimize combined signals afterward, and address TP/SL/other money-management settings last.
- A parameter found at the edge of its tested range (its "Stop" value) is flagged as a warning that the true optimum lies outside the tested range and the sweep should be widened.
- Maximum profit alone is treated as a misleading metric; the author explicitly weighs drawdown against profit (e.g., preferring a lower-profit result with an 8% drawdown over a higher-profit result with 50% drawdown).
- The guide references a prerequisite ("Hendrick's manual on getting 90% modeling quality") as required reading before any of this optimization is meaningful.

## Actionable rules

1. Back-test using "Every tick" modeling quality and roughly six months of data before optimizing.
2. Optimize signal parameters individually first with a coarse step size, then re-run with a narrower range centered on the best result.
3. If the best-found value sits at the edge of the tested range, re-run the sweep with that range shifted/widened.
4. After finding acceptable values for each signal individually, re-test them together (retesting one unit above/below each found value) to confirm the combination still holds.
5. Optimize TP/SL last, starting with a wide range (e.g., 0-100 pips, step 10) then narrowing around the best result (e.g., ±5 pips, step 1).
6. Reject the highest-profit parameter set if it carries disproportionately higher drawdown than a nearby, slightly-lower-profit set.

## Caveats

This is a process guide for one specific, non-public commercial/community EA ("Phoenix," version 5.6.03) whose actual trading logic, signals, and rules are never described — only how to tune it inside MetaTrader's Strategy Tester. It has no value as a standalone trading strategy and is really a generic lesson in walk-forward-style parameter optimization and overfitting awareness applied to a black-box system the reader must already own. Written in 2007 for an old MT4 build; UI details are dated.

## Who it is for

Owners of the Phoenix EA (or readers wanting a concrete, low-level example of how retail forex traders historically approached EA parameter optimization and the curve-fitting risks around it).
