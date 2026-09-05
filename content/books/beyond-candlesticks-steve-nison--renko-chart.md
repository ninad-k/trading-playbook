---
title: "Renko Charts"
author: "Steve Nison"
year: 1994
slug: beyond-candlesticks-steve-nison--renko-chart
tier: A
category: Market Structure & Price Action
tags: [renko, japanese-charting, trend-following, price-based-charts, brick-charts]
difficulty: intermediate
doc_type: system
parent: beyond-candlesticks-steve-nison
pages: 276
one_liner: "A Japanese brick chart where every block is the same fixed height and a new brick prints only after price closes a full brick-size beyond the current extreme."
related: [trading-hill-arthur-introduction-to-candlesticks]
source_file: "Beyond_Candlesticks__Steve_Nison_.pdf"
---

## What it is

The renko chart ("renko" likely from the Japanese for "brick") plots equal-sized white and black bricks in successive columns, built from closing prices. Its key difference from a three-line break chart is that every brick is exactly the same height (a fixed price amount, or a fixed percentage), chosen in advance as the "price range point" — so a 20-point move on a 5-point renko chart always shows as four uniform 5-point bricks, regardless of how choppy or smooth the underlying path was. A new brick, white (up) or black (down), is only drawn once price has closed at least one full brick-height beyond the current extreme; any move smaller than a full brick, or any excess beyond the last complete brick, is simply not shown.

## Rules

**Setup**: Choose a fixed price-range unit (e.g., 5 points) or a fixed percentage; this sets both the minimum move required to draw a brick and the height of every brick on the chart. Choose a base (starting) price.

**First brick**: Compare the base price to the current close.
- If price has risen by at least one full brick-height above the base, draw one white brick from the base up to the base-plus-one-brick level. If the rise is enough for two bricks' worth of movement, draw two white bricks (each in its own column); any partial excess beyond the last complete brick is not shown.
- If price has fallen by at least one full brick-height below the base, draw one (or more) black brick(s) the same way, downward.
- If the move is smaller than one brick-height in either direction, draw nothing.

**Subsequent bricks**: Compare each new close to the high and low of the most recently drawn brick.
- If price closes at or beyond one brick-height above the top of the last brick (white or black), shift one column right and draw one or more equal-height white bricks starting from that prior high.
- If price closes at or beyond one brick-height below the bottom of the last brick, shift one column right and draw one or more equal-height black bricks starting from that prior low.
- If price stays within (above the low, below the high of) the last brick's range, draw nothing.

**Basic buy/sell signal**: Buy on the appearance of a new white brick; sell/short on the appearance of a new black brick. This is the only trend-reversal signal Nison describes for renko charts — simpler and more limited than the range of techniques available on three-line break or kagi charts (no equivalent of shoulders/waists, multi-level breaks, or record-session counting is given for renko).

**Sizing the chart**: Renko sensitivity is controlled purely by brick size — a smaller brick generates more signals and more whipsaws but reacts to a new trend sooner; a larger brick filters more noise but confirms a reversal further from the actual turning point. Nison gives no formula for an "optimal" brick size, treating it as a function of the instrument's volatility, price level, and the trader's holding-period preference.

## Risk

As with the three-line break chart, no explicit stop-loss rule accompanies the basic renko buy/sell signal — the brick reversal itself functions as the exit/reversal point, and the amount given back before a new opposite-color brick confirms is bounded by (but can approach) one full brick-height beyond the prior extreme. In genuinely lateral, range-bound markets, Nison's own examples show renko charts inducing repeated whipsaw round trips (buy on a white brick, sell shortly after on a black brick, repeatedly) — the system's edge is concentrated in markets that develop a sustained directional run, where it lets a trader "ride the major portion of the trend" per Nison's framing, and is weakest exactly when brick size is poorly matched to the instrument's actual volatility regime.

## Caveats

Nison states renko trading techniques are "more limited" than those available for three-line break or kagi charts — there is no renko equivalent of the shoulders/waists analysis, multi-level break confirmation, or the double-window and three-Buddha reversal patterns documented for kagi charts. Renko charts, like three-line break charts, are normally built from daily or weekly closes; Nison notes intraday use is uncommon for renko (unlike kagi, which does see some intraday tick-based use in Japan). Choice of a fixed-percentage versus fixed-point brick size changes chart behavior as price levels shift over long histories (a fixed-point brick becomes relatively larger as a low-priced stock falls, or relatively smaller as a high-priced stock rises) — the book flags this trade-off for kagi charts explicitly but does not give a parallel percentage-based worked example for renko.
