---
title: "Kagi Charts"
author: "Steve Nison"
year: 1994
slug: beyond-candlesticks-steve-nison--kagi-chart
tier: A
category: Market Structure & Price Action
tags: [kagi, japanese-charting, trend-following, price-based-charts, support-resistance]
difficulty: intermediate
doc_type: system
parent: beyond-candlesticks-steve-nison
pages: 276
one_liner: "A Japanese charting method where line thickness (yin/yang) and shoulder/waist levels track shifting control between bulls and bears, reversing only on a set turnaround amount."
related: [trading-hill-arthur-introduction-to-candlesticks]
source_file: "Beyond_Candlesticks__Steve_Nison_.pdf"
---

## What it is

The kagi chart (from the Japanese word for an old L-shaped key; also called a key, price range, hook, delta, or string chart) plots a single continuous vertical line per trend leg, built from closing prices, that changes thickness rather than color. A thick line is called "yang"; a thin line is called "yin." The line extends in its current direction for any move, however small, and only reverses — via a short horizontal "inflection line" into the next column — once price moves against it by at least a pre-chosen turnaround amount (a fixed price move or a fixed percentage). The line thickens from yin to yang whenever it breaks above a prior high (a "shoulder"); it thins from yang to yin whenever it breaks below a prior low (a "waist"). Of the three "new price chart" styles in the book, Nison notes kagi is the most popular in Japan and the only one commonly built on an intraday, tick-by-tick basis as well as daily/weekly.

## Rules

**Setup**: Choose a turnaround (reversal) amount — a fixed price move (e.g., 4 points) or a fixed percentage (e.g., 3% of current price, common for Japanese equities; ~5% is cited as popular among longer-term traders). Choose a starting (base) price.

**First line**: Compare today's close to the base price. If price has moved by the turnaround amount or more above the base, draw a thick (yang) line up to that close. If it has moved the turnaround amount or more below the base, draw a thin (yin) line down to that close. If the move is smaller than the turnaround amount, draw nothing yet.

**Extending the line**: While price continues in the same direction as the current line's tip, extend that line further in the same direction on any move, no matter how small — no turnaround-amount threshold applies to continuation, only to reversal.

**Drawing a reversal line**: Once price moves against the current line's direction by the full turnaround amount or more (measured from the tip), shift one column right, draw a short horizontal inflection line, and draw a new vertical line in the new direction to the new price. A move against the trend that is smaller than the turnaround amount is ignored entirely (no line, no notation) — that session's price simply does not affect the chart.

**Thickness change (yin/yang)**: If a thin (yin) line's advance takes it above a prior shoulder (previous high), the line becomes thick (yang) at the exact price where that shoulder is exceeded. If a thick (yang) line's decline takes it below a prior waist (previous low), the line becomes thin (yin) at the exact price where that waist is broken.

**Basic buy/sell signal ("buy on yang, sell on yin")**: Buy when the kagi line converts from thin to thick (breaks a prior shoulder); sell/short when it converts from thick to thin (breaks a prior waist). This whipsaws in sideways markets exactly like the other new-price charts, and is intended to capture sustained trends rather than pinpoint exact turns.

**Shoulders and waists (trend strength read)**: A sequence of rising shoulders and rising waists shows the bulls maintaining control (each pullback holds at a higher low than the last); a sequence of falling shoulders and falling waists shows the bears in control. The first break in that sequence (e.g., a waist that undercuts the prior waist during an otherwise rising pattern) is an early warning the dominant side is losing its grip.

**Multi-level break (extra confirmation)**: Instead of acting on a single shoulder/waist break, wait for a two-level break (two consecutive prior highs/lows exceeded) or three-level break (three) before treating the reversal as confirmed. More levels means slower but higher-confidence signals — Nison frames this explicitly as trading reward for risk.

**Length of yang/yin within one line**: Where a corrective move stops relative to the vertical midpoint of a long kagi line is diagnostic — if a pullback in an uptrend holds above the midpoint of the prior long line, that is bullish (bulls kept the bears out of their territory); if a countertrend rally in a downtrend fails to reach the midpoint of the prior long line, that is bearish.

**Double windows**: A double-window bottom forms when a shoulder made during a downtrend is lower than both the waist before it and the waist after it (i.e., there is a price gap between the intervening shoulder and the waists flanking it) — a bullish reversal signal. A double-window top is the mirror: a waist during an uptrend that sits above both flanking shoulders — bearish.

**Three-Buddha / reverse three-Buddha**: A three-peak (or three-trough) formation directly analogous to a head-and-shoulders (or inverse head-and-shoulders) pattern; the sell (buy) signal triggers when the "right shoulder" of the pattern is broken. As with shoulder/waist breaks generally, a two-level break of the pattern's neckline-equivalent adds confirmation.

**Record sessions**: A run of about nine higher shoulders (not necessarily consecutive) is called nine record session highs; nine lower waists is nine record session lows. Japanese practice treats approximately nine record highs/lows as a point to start watching for a countertrend move.

## Risk

No explicit percentage-of-equity or stop-distance rule is given; risk is managed structurally through the choice of turnaround amount — a larger turnaround amount produces fewer, later, more confident reversal signals but concedes more of the move before an exit prints, while a smaller turnaround amount reacts faster but whipsaws more in sideways conditions. Nison explicitly frames the multi-level break and the midpoint-of-the-line read as ways to add confirmation at the cost of later entries/exits — there is no single "correct" setting, only an explicit sensitivity/reliability trade-off the trader must choose. Fixed-percentage kagi charts (versus fixed-point) are recommended when trading an instrument across a wide price range over time, since a fixed-point turnaround that is reasonable at one price level becomes too tight or too loose as price moves substantially.

## Caveats

Nison's own tweezers-top example (Wal-Mart) shows the kagi chart's reversal confirming visibly later than a candlestick topping signal on the same instrument — he states this reflects a real limitation: kagi (like three-line break and renko) is not built for picking exact tops or bottoms. The "nine record sessions" exhaustion heuristic is presented as a piece of Japanese trading folklore/convention rather than a statistically derived rule, and Nison offers no backtested win-rate or threshold-sensitivity data for any of the kagi signals (buy-on-yang/sell-on-yin, double windows, three-Buddha, or record sessions) — all are illustrated with historical chart examples rather than quantified performance.
