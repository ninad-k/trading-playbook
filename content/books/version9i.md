---
title: "Stealth Forex System: Trading Methodology"
author: Unknown
year: unknown
slug: version9i
tier: B
category: Day Trading & Scalping
tags: [forex, scalping, proprietary-indicators, money-management, metatrader, multi-timeframe]
difficulty: beginner
doc_type: manual
pages: 16
one_liner: "The trading-rules manual for the proprietary 'Stealth Forex' system, covering four sub-strategies (Simple, Scalper, Mission, Creamer) built on custom LCD and Stealth buy/sell indicators."
related: [forex-trading-machine-ebook, mcrae-mark-sure-fire-forex-trading, take-the-money-and-run, six-forces-of-forex]
source_file: "Version9i.PDF"
---

## Summary

A rules document for a commercial MetaTrader4 forex system ("Stealth Forex System") built around two proprietary indicators — "LCD" and "Stealth buy/sell" — plus standard tools (volume/"grass" bars, Bollinger Bands, Awesome Oscillator). It defines when not to trade, core money-management rules, and entry/exit mechanics for four named sub-strategies of increasing complexity: Simple (beginner), Scalper, Mission Trader, and Creamer.

## Key points

- Never risk more than 2% of account equity on any single trade; never add to a losing position or widen a stop.
- Do not trade within 40 minutes (Scalpers) to 1 hour (Simple System) of major news releases, or when volume ("grass" bars) is low/flat.
- Stealth Simple System: 1-hour chart only; enter on a new LCD buy/sell bar with sufficient volume; stop placed at the tip of the Stealth signal, trailed to each new signal.
- Stealth Scalpers: requires agreement across 1-minute, 5-minute, and 15-minute Stealth buy/sell indicators plus LCD confirmation before entry; stop at the prior Stealth signal on the 1-minute chart; trades EUR/USD preferentially for tight spreads.
- Stealth Mission Traders: 1-hour chart entry confirmed on the 1-minute chart for timing; wider stops than the Scalper system; positions can run hours to about a week; uses the Awesome Oscillator (AO) reaching extreme levels as an early profit-taking signal.
- Stealth Creamer Strategy: USD/JPY only, active after 00:30 GMT; requires Bollinger Band width above 23 pips before considering a trade; stop at the outer Bollinger Band edge + 5 pips (minimum 20 pips + spread); fixed 30-pip take-profit target.
- Mixed or conflicting signals across timeframes are an explicit no-trade condition in every sub-strategy.

## Actionable rules

1. Risk cap: 2% of account equity per trade, no exceptions.
2. Stealth Simple System: 1-hour chart, enter on new LCD bar + sufficient volume; stop at the Stealth signal tip (plus spread), trailed forward.
3. Stealth Scalpers: require Stealth buy/sell agreement on 1-min, 5-min, and 15-min charts plus LCD confirmation; exit on any LCD color change on the 5-min or 15-min chart.
4. Stealth Creamer: enter only when Bollinger Band width > 23 pips and price retraces to the mid-band on a new Stealth signal; stop = outer Bollinger Band edge + 5 pips (min. 20 pips + spread); target = fixed 30 pips.
5. No trading on Fridays after 16:00 GMT or Sundays before 02:00 GMT Monday (Simple System/Scalpers); Mission Traders must flatten before the weekend close.

## Caveats

Undated commercial forex-system manual (author/publisher not named in the text; references only the "Stealth Forex System" brand); all entry/exit logic depends on two proprietary, non-public indicators ("LCD" and "Stealth buy/sell") whose exact calculation is not disclosed here, so the rules cannot be independently coded or verified without the indicator files. No backtest statistics, win rate, or track record are provided. Read alongside its companion "set up" document, which is not included in this excerpt.

## Who it is for

Discretionary forex day traders already using (or evaluating) the Stealth Forex indicator package who want the documented entry/exit/money-management rules for its four sub-strategies.
