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

The renko chart ("renko" likely from the Japanese for "brick") plots equal-sized white and black bricks in successive columns, built from closing prices. Its key difference from a three-line break chart is that every brick is exactly the same height (a fixed price amount or percentage), chosen in advance as the "price range point" — a 20-point move on a 5-point renko chart always shows as four uniform 5-point bricks, regardless of how choppy the underlying path was. A new brick, white (up) or black (down), is only drawn once price has closed at least one full brick-height beyond the current extreme; a move smaller than a full brick, or any excess beyond the last complete brick, simply isn't shown.

## Rules

**Setup**: choose a fixed price-range unit (e.g., 5 points) or a fixed percentage — this sets both the minimum move required to draw a brick and every brick's height — and a base (starting) price.

**First brick**: if price has risen at least one brick-height above the base, draw one white brick from the base up to that level (two bricks if the rise covers two full brick-heights, each in its own column, excess unshown); the mirror applies for a fall of at least one brick-height (black brick). A smaller move draws nothing.

**Subsequent bricks**: compare each new close to the high/low of the most recently drawn brick. A close at or beyond one brick-height above the top draws one or more white bricks (one column right, starting from that prior high); a close at or beyond one brick-height below the bottom draws black bricks the same way. Price staying within the last brick's range draws nothing.

**Basic signal**: buy on a new white brick; sell/short on a new black brick. This is the only reversal signal Nison gives for renko — simpler than three-line break or kagi (no equivalent of shoulders/waists, multi-level breaks, or record-session counting).

**Sizing**: sensitivity is controlled purely by brick size — smaller bricks generate more signals and whipsaws but react sooner; larger bricks filter more noise but confirm reversals further from the actual turn. No formula for an "optimal" size is given; it's a function of volatility, price level, and holding-period preference.

## Risk

As with three-line break, no explicit stop-loss rule accompanies the basic renko signal — the brick reversal itself is the exit/reversal point, and the amount given back before a new opposite-color brick confirms is bounded by, but can approach, one full brick-height beyond the prior extreme. In genuinely lateral markets, Nison's own examples show renko inducing repeated whipsaw round trips (buy on white, sell shortly after on black) — its edge is concentrated in markets that develop a sustained directional run, letting a trader "ride the major portion of the trend," and is weakest when brick size is poorly matched to the instrument's actual volatility.

## Caveats

Nison states renko techniques are "more limited" than three-line break or kagi — there is no renko equivalent of shoulders/waists, multi-level break confirmation, or the double-window and three-Buddha patterns documented for kagi. Renko, like three-line break, is normally built from daily or weekly closes; intraday use is uncommon (unlike kagi, which does see intraday tick-based use in Japan). A fixed-percentage versus fixed-point brick size changes chart behavior as price shifts over long histories — a fixed-point brick becomes relatively larger as a low-priced stock falls, or smaller as a high-priced stock rises — a trade-off the book flags for kagi but doesn't work through for renko.
