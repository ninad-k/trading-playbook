# The Forex Report - Core Concepts: Signal Selection: the trader's summary

*Short FX Engines newsletter piece classifying technical-indicator signal types (crossing, oscillator, threshold, condition) and warning that longer chart intervals mask price action that causes stops to be hit.*

**Scott Owens** · 2005 · Indicators · beginner

*Source coverage: partial. PDF pages inspected: the signal-selection discussion checked against the note; the brief states no numeric parameters. These are study notes, not verified trading results.*

## Summary

A short educational newsletter ("The Forex Report," Core Concepts series) from FX Engines, Inc., a forex system-building/automation vendor. It argues against "shopping charts" for a signal confirming a preconceived view, recommending instead understanding what each class of indicator measures before building a system. It explains why chart interval choice matters (a smoother, longer-interval chart hides swings that trigger stops on a shorter one) and surveys four categories of trading signals with pros/cons, closing with a three-step process: select deliberately, test, and experiment with combinations.

## Key points

- Signals are indicator-based triggers for entry, exit, or intra-trade adjustment, giving traders "a precise, explicit script" instead of subjective judgment.
- Chart interval materially changes what a signal shows: a 5-minute chart smooths swings visible on a 1-minute chart, which can make a system look reliable on the smoothed view while getting stopped out on the underlying volatility.
- **Crossing signals** (MACD, MA, Stochastic crosses) — explicit, but prone to false signals in low volume and can lag on longer intervals.
- **Oscillators** (Stochastics, MACD, RSI, DMS) — good for reversals/targets, but volume-sensitive and can get "stuck" in overbought/oversold zones.
- **Thresholds** (price/indicator hitting a fixed level) — explicit and responsive in high volume, but can be meaningless in low volume.
- **Conditions** (relationship between two indicators, e.g. price above a MA) — good for trend context, but unresponsive to small moves.
- Exit signals are argued more context-sensitive than fixed stops/limits, since they react to actual market behavior rather than a static distance.

## Actionable rules

1. Choose signal type based on what you're trying to capture, not on whichever chart "looks right."
2. Match indicator choice to volume/volatility regime: crossing/threshold signals suit higher volume; oscillators risk sticking in trending, low-volume conditions.
3. Test any signal both historically and in demo mode before trading real capital.
4. Consider an exit signal instead of a purely fixed stop/limit to better capture a genuine move's length.
5. Combine multiple signal types as a check-and-balance system rather than relying on one indicator.

## Caveats

Vendor content promoting FX Engines' own platform; a conceptual primer with no specific parameters, backtested statistics, or complete system — it explicitly disclaims suggesting live-trading action. Very short (6 pages, much of it promotional).

## Who it is for

Beginner-to-intermediate forex traders wanting a vocabulary for comparing indicators before building their own system, not a ready-made strategy.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: forex, technical-indicators, signals, macd, timeframes, system-building, indicators-overview
