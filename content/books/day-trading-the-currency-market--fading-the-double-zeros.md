---
title: Fading the Double Zeros
author: Kathy Lien
year: 2006
slug: day-trading-the-currency-market--fading-the-double-zeros
tier: A
category: Day Trading & Scalping
tags: [forex, day-trading, mean-reversion, round-numbers, scalping]
difficulty: intermediate
doc_type: system
parent: day-trading-the-currency-market
pages: 259
one_liner: "A short-term contrarian scalp that fades price into round-number ('double zero') levels where take-profit orders cluster, aiming for roughly a 2.5:1 reward-to-risk ratio."
source_file: "Day Trading the Currency Market.pdf"
---

## What it is

Double zeros are price levels where the last two digits are 00 (e.g., 107.00 in USD/JPY, 1.2800 in EUR/USD); "triple zeros" (e.g., 1.2000) are less frequent and considered even more significant. The strategy exploits the tendency of retail and institutional traders to cluster take-profit orders at these psychologically round levels while placing stop-losses just beyond them. Large banks with visibility into this order-flow clustering can trigger reactions at these levels; the strategy positions the trader on the same side as that flow, expecting a short, sharp contra-trend bounce as the round number is approached.

## Rules

**Long setup**:
1. Locate a currency pair trading well below its intraday 20-period simple moving average on a 10- or 15-minute chart.
2. Enter long several pips below the round-number "figure" (no more than 10 pips below).
3. Place an initial protective stop no more than 20 pips below the entry price.
4. When the position is profitable by double the amount risked, close half the position and move the stop on the remainder to breakeven; trail the stop as price continues in your favor.

**Short setup** (mirror image):
1. Locate a currency pair trading well above its intraday 20-period SMA on a 10- or 15-minute chart.
2. Enter short several pips above the figure (no more than 10 pips above).
3. Place an initial protective stop no more than 20 pips above the entry price.
4. When the position is profitable by double the amount risked, close half the position and move the stop on the remainder to breakeven; trail the stop as price continues in your favor.

**Market conditions**: works best in quieter markets, absent a major scheduled economic release; most reliable on tighter-range pairs, crosses, and commodity currencies; can be used on majors but only under quiet conditions since the stops are relatively tight.

**Optimization**: the setup has a higher probability of success when the round number coincides with another significant technical level — a key moving average, a Fibonacci retracement, or a Bollinger band.

## Risk

Risk per trade is capped at the fixed initial stop (up to 20 pips), while the profit target on the first half-position is double that (up to ~40 pips), producing a built-in ~2:1 reward-to-risk skew before the trailing-stop portion is considered. Because entries are only 10 pips from the round number, the trade requires precise timing and tight execution; slippage or a wide spread can materially erode the edge. The setup is a counter-trend scalp and is vulnerable to a genuine breakout through the round number (rather than a bounce), especially around scheduled news.

## Caveats

The book's worked examples (EUR/USD, USD/JPY, USD/CAD) are individually selected illustrations from the mid-2000s rather than an audited statistical track record, so the implied win rate is not independently verified. The underlying premise — that large banks exploit visible order-flow clustering to "gun stops" around round numbers — reflects mid-2000s interbank/voice-market structure; in a more electronic, algorithmically arbitraged market this dynamic may be weaker or faster to resolve. The strategy is explicitly described as working best in quiet, non-news conditions, which limits how often a valid setup appears.
