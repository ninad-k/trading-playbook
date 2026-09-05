---
title: "Bollinger Band System"
author: Perry J. Kaufman
year: 2003
slug: a-short-course-in-technical-trading--bollinger-band-system
tier: A
category: Indicators
tags: [bollinger-bands, standard-deviation, mean-reversion, volatility, bands]
difficulty: beginner
doc_type: system
parent: a-short-course-in-technical-trading
pages: 339
one_liner: "20-day moving average with 2-standard-deviation bands; buy the lower band, sell the upper band, exit near the midline."
related: []
source_file: "A Short Course in Technical Trading.PDF"
---

## What it is

A volatility-adaptive band built around a moving average, contrasted in the book against fixed-percentage bands. Where a percentage band (e.g., MA × 1.05 / MA ÷ 1.05) has constant width regardless of market conditions, a Bollinger band's width expands and contracts automatically with recent price volatility, so it stays statistically consistent — about 87% of closes should fall inside the band — across both quiet and volatile stretches of the same instrument.

## Rules

**Calculation (traditional 20-day version):**
1. Calculate a 20-day moving average of closing prices; this is the center line.
2. Calculate the standard deviation of the closing-price changes over the same 20-day window.
3. Multiply the standard deviation by 2.
4. Upper band = 20-day MA + (2 × standard deviation). Lower band = 20-day MA − (2 × standard deviation).

Excel form (prices in column A, most recent 20 values A81:A100):
```
Upper Bollinger band = AVERAGE(A81:A100) + 2*STDEV(A81:A100)
Lower Bollinger band = AVERAGE(A81:A100) - 2*STDEV(A81:A100)
```

**Trading rules (same mean-reversion logic as a percentage band):**
1. Buy when price penetrates the lower band and shows signs of stopping/turning back up.
2. Sell/short when price penetrates the upper band and shows signs of turning back down.
3. Exit (take profit) as price returns to the vicinity of the center 20-day moving average — do not expect or wait for price to run from one band to the other.
4. Optionally combine with chart pattern context (double tops/bottoms) or an underlying trend filter to select which band touches are worth trading, rather than trading every touch mechanically.
5. To adapt the system for longer-horizon, lower-frequency trading, lengthen the calculation window (e.g., 200-day MA with 2-standard-deviation bands): this produces far fewer signals, wider bands (roughly double the width of the 20-day version in Kaufman's AMR example), and lower initial risk per touch, at the cost of longer holding periods and larger price swings before the target (the midline) is reached.

## Risk

- By construction, 2-standard-deviation bands should be touched/penetrated by only about 13% of closes (13 out of 100) — if penetrations are happening much more often than that on a given instrument, the calculation window or band multiplier should be reconsidered.
- The system fails in sustained directional moves: Kaufman's AMR example shows a July-August decline where price closed below the lower band and stayed there for roughly a month before finally returning to the midline — a trader buying the first lower-band touch would have taken a large loss holding through the whole move. This is the same structural failure mode as the fixed-percentage band, just somewhat better contained by Bollinger bands' volatility adaptivity.
- Because the band width is a function of trailing volatility, a sudden volatility spike immediately widens the band (increasing risk if a trade is entered right after the spike) rather than requiring a separate volatility filter.
- No explicit stop-loss level is given for the band-touch entry itself in the text; the book's general stop-sizing rule (never tighter than 1.5x current daily volatility) should be layered on top of any Bollinger entry to define a hard risk limit rather than relying solely on the midline target.

## Caveats

Kaufman is explicit that Bollinger bands are not a fix for the band system's core weakness — a strong, sustained trend will pin price against one band for an extended period regardless of which volatility measure is used to build the band, and the 1998-99 AMR downtrend example shows the Bollinger version failing in essentially the same way (if less severely) as the fixed-percentage version on the identical data. The book presents the standard 20-day/2-standard-deviation parameterization as the norm without testing alternative multipliers (e.g., 1.5 or 2.5 standard deviations) or a systematic sweep of calculation lengths, so those parameters should be treated as a reasonable default rather than a tuned optimum. He also notes a regression-line-based band (2 standard deviations around a rolling linear regression) as a related, sometimes better-fitting alternative, but does not provide comparative performance statistics between the two.
