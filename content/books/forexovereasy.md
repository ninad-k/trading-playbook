---
author: Unknown
category: Day Trading & Scalping
difficulty: beginner
doc_type: manual
one_liner: A two-page 15-minute forex system requiring three confirming signals (channel
  slope, two oscillator crossovers, a volatility filter) before entry, using non-standard
  custom indicators.
pages: 2
related:
- amazing-forex-system
- catfx50-rules
reviewed_pdf_pages: 1-2
slug: forexovereasy
source_file: Forexovereasy.pdf
source_review: full
tags:
- forex
- channel-trading
- custom-indicators
- scalping
- 15-minute-chart
tier: B
title: The FxOverEasy System
year: unknown
---

## Summary

A very short, informally-written rule sheet for a 15-minute-chart forex system requiring three separate confirming signals before a trade is taken: trend direction from a proprietary channel indicator, an entry/exit trigger from two custom oscillators, and a volatility filter from a third custom indicator. The whole document is essentially a checklist rather than a discursive explanation.

## Key points

- Direction filter: an "SHI channel" that recalculates in real time — only sell when its slope is down, only buy when its slope is up; no trades are taken when the channel is narrow/thin or when price falls outside the channel (wait for a new channel to form).
- Primary entry trigger: "I_trend" indicator — a red line crossing to the top signals sell, a green line crossing to the top signals buy.
- Secondary entry/exit trigger: "La Guerre" oscillator — crossing down through its 0.75 upper line signals sell; crossing up through its 0.15 lower line signals buy; if a separate "Juice" indicator is still green, the trade is held to the opposite side of the channel, otherwise exit when La Guerre reaches its 0.45 midline.
- Tertiary/optional trigger: "Perkyasctrend1" indicator — pink dot signals sell, blue dot signals buy; described as useful for beginners and unnecessary for advanced traders.
- Volatility filter: "Juice" histogram — never enter a trade if the histogram is red, even if every other indicator lines up; it must be green as the final confirmation.
- Core discipline rule, repeated twice in the text: only ever trade in the direction of the SHI channel's slope, and require all three categories of confirmation (direction, entry/exit, volatility) before entering.
- Stated stop loss: 15 pips.

## Actionable rules

1. Trade only in the direction of the SHI channel slope; skip trading entirely if the channel is thin or price is outside it.
2. Entry: I_trend crossing (red-top = sell, green-top = buy), confirmed by La Guerre crossing its 0.75 (sell) or 0.15 (buy) line.
3. Confirmation filter: Juice histogram must be green (not red) before entering, regardless of other signals.
4. Exit: hold to the opposite side of the channel if Juice remains green; otherwise exit when La Guerre reaches its 0.45 midline.
5. Stop loss: 15 pips ("safety stop") on every trade.
6. Rule of three: require all three reasons — direction, entry/exit signal, and volatility confirmation — before entering any trade.

## Caveats

The document names several custom/proprietary indicators (SHI channel, I_trend, La Guerre, Juice, Perkyasctrend1) without defining their calculation, parameters, or platform/source, so the system cannot be reproduced or verified without the original indicator files — this is a companion cheat-sheet for users who already have those indicators installed, not a self-contained specification. No timeframe beyond "15 min," no currency pair, no position sizing, and no backtest or performance data are given; author and publication year are unknown, and the source appears to be an informal forum handout.

## Who it is for

Traders who already have access to the SHI channel, I_trend, La Guerre, Juice, and Perkyasctrend1 custom indicators (e.g., from the same forum/vendor this sheet originated with) and need a quick reference for how the rules combine — not useful as a standalone system for anyone without those indicators.
