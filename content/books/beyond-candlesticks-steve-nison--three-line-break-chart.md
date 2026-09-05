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

The three-line break chart plots a series of white and black rectangular "lines" (blocks) in successive columns, built from closing prices only. Unlike a time-based bar or candle chart, a new line is added only when price makes a new closing high or low relative to the current chart extreme — sessions that stay within the existing range are simply skipped, drawing nothing. Its defining rule, and the source of its name, is that once three consecutive lines share the same color, a reversal line of the opposite color cannot be drawn until price breaks the low (for three white lines) or high (for three black lines) of all three of those lines — not merely a new one-tick extreme. This makes the chart naturally resistant to noise and, according to the Japanese trader Nison quotes, lets "the market" rather than an arbitrary fixed amount decide when a reversal is confirmed.

## Rules

**Setup**: Choose a base (starting) price. All lines are built from closing prices; no time axis is meaningful (Nison adds an approximate time reference to his exhibits only for orientation).

**First line**: Compare today's close to the base price. If higher, draw a white line from the base price up to the new high. If lower, draw a black line from the base price down to the new low. If unchanged, draw nothing.

**Second and later lines (while under three same-color lines)**: Compare each new close to the high and low of the current line(s). A new white line is drawn (shifted one column right) only when price closes above the current high; a new black line only when price closes below the current low. Price must exceed the prior high/low, not merely touch it. If price stays within the existing high-low range, nothing is drawn for that session.

**After three consecutive same-color lines**: A new line of the *same* color continues to be added on any new high (white) or new low (black), however small the increment. But a reversal ("turnaround") line of the *opposite* color requires price to close beyond the low (for a black turnaround, breaking three white lines) or the high (for a white turnaround, breaking three black lines) of the last three consecutive same-color lines. A black turnaround line is drawn from the bottom of the highest white line down to the new low close; a white turnaround line is drawn from the top of the lowest black line up to the new high close.

**Basic buy/sell signal**: Buy on the appearance of a new white line (or white turnaround line); sell/short on a new black line (or black turnaround line). In an alternating (non-trending) market, this whipsaws; the chart's value is concentrated in markets that have established a run of 3+ same-color lines, signaling a confirmed trend.

**Trend-plus-candle combination**: Use the three-line break chart's current color/direction to define the prevailing trend, then take only candlestick signals that agree with that trend as entries (e.g., only take bullish candle signals while the three-line break chart is in a white-line uptrend); use a black or white turnaround line as the exit signal for a position originally entered on a candlestick trigger, since candle patterns themselves rarely define a profit target.

**Early/light-position variant**: Because a turnaround line only confirms on the close (by which point price may already be well past the reversal threshold), some traders take a smaller position intraday once the prior three-line extreme is touched or exceeded, then add to it if the close confirms the turnaround, or exit the intraday position if the close fails to confirm.

## Risk

No explicit stop-loss rule is given for trading purely off the three-line break chart; risk management is implicit in the chart's own lag — a position is effectively "stopped out" only when a full reversal line prints, which by construction happens well after the actual price extreme. This means realized risk per trade can be large relative to a fixed-percentage or ATR-based stop, particularly on the first line drawn after a long same-color run (the position may give back a meaningful portion of open profit before the turnaround line confirms). Nison recommends combining the trend read from this chart with tighter candlestick-based entries/exits, or with a lighter, unconfirmed intraday position around the reversal threshold, specifically to manage this lag risk.

## Caveats

The chart requires closing-price data only, so intraday three-line break charts are uncommon in Nison's account — he notes the technique is normally applied on daily or weekly closes, unlike kagi charts which do see some intraday use. Choosing to trade on light, unconfirmed intraday signals versus waiting for the close-confirmed turnaround line is explicitly a trade-off between earlier entry and higher whipsaw risk (an intraday touch that fails to close through the threshold gives no line at all, and any light position taken on it should be unwound). As with renko and kagi charts, the technique is described by Nison as suited to capturing the "meat" of a sustained move rather than picking exact tops or bottoms, and is prone to whipsaw in genuinely range-bound, alternating markets.
