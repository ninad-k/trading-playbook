---
title: "The Forex Report - Core Concepts: Signal Selection"
author: Scott Owens
year: 2005
slug: signalselection
tier: B
category: Indicators
tags: [forex, technical-indicators, signals, macd, timeframes, system-building, indicators-overview]
difficulty: beginner
doc_type: article
pages: 6
one_liner: "Short FX Engines newsletter piece classifying technical-indicator signal types (crossing, oscillator, threshold, condition) and warning that longer chart intervals mask price action that causes stops to be hit."
related: [macd, chart-formations, technical-indicators-tutorial]
source_file: "signalselection.pdf"
---

## Summary

A short educational newsletter ("The Forex Report," Core Concepts series) published by FX Engines, Inc., a forex system-building/automation vendor, aimed at traders of all experience levels. The article argues against "shopping charts" for a signal that confirms a preconceived view, and instead recommends understanding what each class of technical indicator actually measures before building a system. It explains why chart interval choice matters (a smoother, longer-interval chart hides the price swings that trigger stops on a shorter interval the trader may also be watching) and surveys four broad categories of trading signals with their pros and cons, then closes with a three-step process: select signals deliberately, test them (live and historically), and experiment with combining them.

## Key points

- Signals are technical-indicator-based triggers for market entry, exit, or intra-trade adjustment; they exist to give traders "a precise, explicit script" instead of subjective judgment.
- Chart interval choice materially changes what a signal shows: a 5-minute chart smooths out swings visible on a 1-minute chart, which can make a system look reliable on the smoothed view while getting stopped out on the underlying volatility.
- **Crossing signals** (e.g., MACD line crosses, moving-average crosses, Stochastic crosses) — explicit and easy to see, but prone to false signals in low volume and can lag heavily on longer intervals.
- **Oscillators** (e.g., Stochastics, MACD, RSI, DMS) — good at showing reversals and targets, but volume-sensitive and prone to getting "stuck" in overbought/oversold zones during strong trends.
- **Thresholds** (price or indicator reaching a fixed level — Stochastics, RSI, DMS, breakouts) — explicit and responsive in high volume, but can be arbitrary/meaningless in low-volume conditions.
- **Conditions** (a relationship between two indicators, e.g., price above a moving average signaling a trend) — good for defining trend context and filtering bad trades, but unresponsive to small price moves.
- Exit signals are argued to be more context-sensitive than fixed trailing stops or limit exits, because they react to what the market is actually doing rather than a static numeric distance (illustrated with a hypothetical Fed-announcement scenario where a fixed 30-pip limit exit leaves profit on the table versus a signal-based exit).

## Actionable rules

1. Choose signal type deliberately based on what you are trying to capture (reversal, trend continuation, target level) rather than picking whichever chart "looks right."
2. Match indicator choice to the market's current volume/volatility regime: crossing and threshold signals are more reliable in higher volume; oscillators risk getting stuck in overbought/oversold zones in low-volume or strongly trending conditions.
3. Test any signal or signal combination both historically and in a demo/live-test mode before trading it with real capital.
4. Consider using an exit signal (the same type of technical trigger used for entry) rather than a purely fixed stop or limit exit, to better capture the full length of a genuine move.
5. Combine multiple signal types as a "checks and balances" system to reduce false positives, rather than relying on a single indicator.

## Caveats

This is vendor content promoting FX Engines' own system-building/automation platform; it is a conceptual primer with no specific parameter settings, backtested statistics, or a complete trading system — it explicitly states it "does not suggest any particular action that could be utilized in live trading." Very short (6 pages, much of it branding/promotional material).

## Who it is for

Beginner-to-intermediate forex traders who want a vocabulary for classifying and comparing technical indicators before building their own system, not readers looking for a ready-made strategy.
