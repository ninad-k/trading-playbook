---
title: "E.A.S.Y. Trading Method"
author: Dean Malone
year: 2007
slug: e-a-s-y-method
tier: B
category: Indicators
tags: [forex, heiken-ashi, rsi, price-action-channel, traders-dynamic-index, mechanical-system]
difficulty: beginner
doc_type: manual
pages: 88
one_liner: "Slide-deck forex system combining Heiken Ashi bars, a price-action channel, and the Traders Dynamic Index (RSI-based) into concrete entry/exit rules."
related: [jan-l-arps-surfing-the-market-waves-the-swing-trader-s, king-keltner-trading-strategy]
source_file: "E.A.S.Y.Method.pdf"
---

## Summary

A slide-deck presentation (originally a webinar handout) by Dean Malone introducing the "E.A.S.Y." (Effective, Accurate, Simple, Yield) forex trading method, built around three chart tools: Heiken Ashi average price bars, a Price Action Channel (PAC) of two smoothed moving averages, and the Traders Dynamic Index (TDI), a composite RSI-based indicator with a price line, trade-signal line, market-base line, and volatility bands. The deck defines exact numeric rules for entries and exits and walks through two annotated example trades (GBP/USD 5-minute and multi-day GBP/USD swing trade with a trailing stop). The back third of the deck is broker/vendor promotional material (CompassFX, a managed-account program) rather than trading content.

## Key points

- Heiken Ashi ("average bar") smooths price: haClose = (Open+High+Low+Close)/4; haOpen = average of the prior bar's haOpen and haClose; haHigh/haLow take the max/min of the actual high/low versus haOpen.
- Price Action Channel (PAC) = two smoothed moving averages of the 5-period high and 5-period low; its slope defines the visible trend direction.
- Traders Dynamic Index (TDI) settings: RSI on 13-period close; RSI Price Line = 2-period SMA of RSI; Trade Signal Line = 7-period SMA of RSI; Volatility Bands = 34-period SMA/bands of RSI (Bollinger-style bands on the RSI itself).
- TDI reading rules: RSI Price Line (green) above 50 favors longs, below 50 favors shorts; crossing above/below 68/32 signals an overbought/oversold condition worth considering an exit.
- Long entry requires all three tools to agree: haClose above the PAC high average, PAC trending up, and RSI Price Line above 50, above the Trade Signal Line, and above the Market Base Line.
- Short entry is the mirror condition: haClose below the PAC low average, PAC trending down, RSI Price Line below 50, below the Trade Signal Line, and below the Market Base Line.
- Exit triggers: a much shorter or color-flipped Heiken Ashi bar, price closing back inside the PAC, or the RSI Price Line crossing back through the Trade Signal Line, the 68/32 extreme, or the volatility band.
- In the worked multi-day example, the stop is trailed to the Low PAC value (or the low of the prior day, whichever is tighter) after each favorable close, capturing roughly 386 pips before being stopped out.

## Actionable rules

1. Enter long only when all three conditions align: Heiken Ashi close above the PAC high moving average, PAC channel sloping up, and TDI green line above 50, above the red Trade Signal Line, and above the yellow Market Base Line (mirror for shorts).
2. Treat a TDI green line crossing above 68 (or below 32) as a signal to tighten stops or take profits rather than a fresh entry signal.
3. Use the Price Action Channel's low (for longs) or high (for shorts) as the primary trailing-stop reference, tightening it to the prior day's low/high once a trade is working.
4. Exit immediately if price closes back inside the PAC channel, regardless of what the other two tools show.
5. Avoid adding to a long once RSI Price Line exceeds 68, and avoid adding to a short once it falls below 32 — the deck explicitly flags these as zones to avoid new entries, not just extremes to fade.

## Caveats

This is a promotional slide deck, not a book: roughly 15 of 88 pages are vendor/broker marketing (CompassFX platform, a third-party managed-account program) rather than trading content, and the whole method is presented via annotated screenshots rather than a written backtest or performance statistics. No win rate, drawdown, or sample size is given beyond two illustrative trades, so the system's edge is asserted, not demonstrated. The "TDI" indicator described here is the same tool later distributed widely as a MetaTrader custom indicator; exact input parameters may differ across implementations found elsewhere.

## Who it is for

Discretionary forex traders who want a simple, fully mechanical checklist for entries and exits built from one composite RSI indicator and Heiken Ashi charting, and who are comfortable evaluating a system from worked chart examples rather than a formal backtest.
