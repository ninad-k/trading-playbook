---
title: "Three-Line Break Charts"
author: "Steve Nison"
year: 1994
slug: beyond-candlesticks-steve-nison--three-line-break-chart
tier: A
category: Market Structure & Price Action
tags: [three-line-break, japanese-charting, trend-following, price-based-charts, point-and-figure]
difficulty: intermediate
doc_type: system
parent: beyond-candlesticks-steve-nison
pages: 276
one_liner: "A price-only Japanese charting method where a new line is drawn only on a fresh closing high or low, and reversals require breaking the extreme of the prior three same-color lines."
related: [trading-hill-arthur-introduction-to-candlesticks, macd]
source_file: "Beyond_Candlesticks__Steve_Nison_.pdf"
---

## What it is

The three-line break chart plots white and black rectangular "lines" (blocks) in successive columns, built from closing prices only. A new line is added only when price makes a new closing high or low relative to the current chart extreme — sessions that stay within the existing range are skipped, drawing nothing. Its defining rule, and the source of its name: once three consecutive lines share a color, a reversal line of the opposite color cannot be drawn until price breaks the low (for three white lines) or high (for three black lines) of all three — not merely a new one-tick extreme. This makes the chart naturally resistant to noise and, per the Japanese trader Nison quotes, lets "the market" rather than an arbitrary fixed amount decide when a reversal is confirmed.

## Rules

**Setup**: choose a base (starting) price; all lines are built from closing prices, with no meaningful time axis.

**First line**: if today's close is higher than the base, draw a white line up to it; if lower, draw a black line down to it; if unchanged, draw nothing.

**Second and later lines (under three same-color lines)**: a new white line is drawn (one column right) only when price closes above the current high; a new black line only when it closes below the current low — price must exceed, not merely touch, the prior extreme. Otherwise nothing is drawn.

**After three consecutive same-color lines**: a new line of the *same* color continues on any new high/low, however small. A reversal ("turnaround") line of the *opposite* color requires price to close beyond the low of the last three white lines (for a black turnaround) or the high of the last three black lines (for a white turnaround) — drawn from the bottom of the highest white line, or the top of the lowest black line, to the new close.

**Basic signal**: buy on a new white line (or white turnaround); sell/short on a new black line (or black turnaround). Whipsaws in an alternating market; value is concentrated once a run of 3+ same-color lines confirms a trend.

**Trend-plus-candle combination**: use the chart's current color/direction as the prevailing trend filter, taking only candlestick signals that agree with it as entries; use a turnaround line as the exit for a position entered on a candlestick trigger, since candle patterns rarely define a profit target.

**Early/light-position variant**: since a turnaround line only confirms on the close (by which point price may be well past the threshold), some traders take a smaller intraday position once the prior extreme is touched, adding on close-confirmation or exiting if it fails to confirm.

## Risk

No explicit stop-loss rule accompanies the pure three-line break signal; risk management is implicit in the chart's own lag — a position is effectively "stopped out" only when a full reversal line prints, well after the actual price extreme. Realized risk per trade can therefore be large relative to a fixed-percentage or ATR-based stop, especially on the first line after a long same-color run, where open profit can be given back before the turnaround confirms. Nison recommends pairing this chart's trend read with tighter candlestick entries/exits, or a lighter unconfirmed intraday position around the reversal threshold, to manage that lag.

## Caveats

The chart requires closing-price data only, so intraday three-line break charts are uncommon — Nison notes it is normally applied on daily or weekly closes, unlike kagi charts, which do see intraday use. Trading light, unconfirmed intraday signals versus waiting for the close-confirmed turnaround line is an explicit trade-off between earlier entry and higher whipsaw risk. Like renko and kagi, the technique is suited to capturing the "meat" of a sustained move rather than picking exact tops or bottoms, and whipsaws in genuinely range-bound, alternating markets.
