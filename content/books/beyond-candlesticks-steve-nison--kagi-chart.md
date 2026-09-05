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

The kagi chart (from the Japanese word for an old L-shaped key; also called a key, price range, hook, delta, or string chart) plots one continuous vertical line per trend leg, built from closing prices, that changes thickness rather than color. A thick line is "yang"; a thin line is "yin." The line extends in its current direction for any move, however small, and only reverses — via a short horizontal "inflection line" into the next column — once price moves against it by a pre-chosen turnaround amount (a fixed price move or percentage). The line thickens from yin to yang when it breaks above a prior high (a "shoulder"); it thins from yang to yin when it breaks below a prior low (a "waist"). Of the three "new price chart" styles in the book, kagi is the most popular in Japan and the only one commonly built on an intraday, tick-by-tick basis as well as daily/weekly.

## Rules

**Setup**: choose a turnaround (reversal) amount — a fixed price move (e.g., 4 points) or a fixed percentage (~3% is common for Japanese equities, ~5% among longer-term traders) — and a starting base price.

**First line**: if price moves the turnaround amount or more above the base, draw a thick (yang) line up to that close; if the turnaround amount or more below, draw a thin (yin) line down. A smaller move draws nothing yet.

**Extending vs. reversing**: while price continues in the line's current direction, extend it on any move, however small — no threshold applies to continuation. Only once price moves against the tip by the full turnaround amount does a reversal print: shift one column right, draw a short inflection line, then a new vertical line to the new price. A countertrend move smaller than the turnaround amount is ignored entirely.

**Thickness change**: a yin line becomes yang the moment it exceeds a prior shoulder (previous high); a yang line becomes yin the moment it breaks a prior waist (previous low).

**Basic signal ("buy on yang, sell on yin")**: buy when the line converts thin-to-thick (breaks a shoulder); sell/short when it converts thick-to-thin (breaks a waist). Whipsaws in sideways markets like the other new-price charts; built to capture sustained trends, not pinpoint exact turns.

**Shoulders and waists**: rising shoulders and waists show the bulls in control (each pullback holds a higher low); falling shoulders and waists show the bears in control. The first break in that sequence warns the dominant side is losing grip.

**Multi-level break**: wait for a two- or three-level break (2-3 prior highs/lows exceeded) instead of a single shoulder/waist break — slower but higher-confidence, an explicit reward-for-risk trade-off.

**Midpoint read**: a pullback holding above the vertical midpoint of a long kagi line (uptrend), or a rally failing to reach it (downtrend), favors the prevailing trend continuing.

**Double windows**: a double-window bottom forms when a downtrend shoulder sits below both flanking waists (a price gap around it) — bullish; a double-window top is the mirror — bearish.

**Three-Buddha / reverse three-Buddha**: a three-peak (or trough) formation analogous to head-and-shoulders; triggers when the pattern's "right shoulder" is broken, with a two-level break adding confirmation.

**Record sessions**: about nine higher shoulders (not necessarily consecutive) is "nine record session highs," nine lower waists is "nine record session lows" — a Japanese heuristic for watching for a countertrend move.

## Risk

No explicit percentage-of-equity or stop-distance rule is given; risk is managed structurally through the turnaround amount — larger means fewer, later, more confident reversals but more of the move conceded before exit; smaller reacts faster but whipsaws more. The multi-level break and midpoint read add confirmation at the cost of later entries/exits — there is no "correct" setting, only a sensitivity/reliability trade-off. Fixed-percentage kagi charts are recommended over fixed-point when trading an instrument across a wide price range over time, since a fixed-point turnaround reasonable at one price level becomes mismatched as price moves substantially.

## Caveats

Nison's own tweezers-top example (Wal-Mart) shows the kagi reversal confirming visibly later than a candlestick topping signal on the same instrument — a real limitation: kagi, like three-line break and renko, isn't built for picking exact tops or bottoms. The "nine record sessions" heuristic is Japanese trading convention rather than a statistically derived rule, and no backtested win-rate or threshold-sensitivity data is given for any kagi signal (buy-on-yang/sell-on-yin, double windows, three-Buddha, record sessions) — all are illustrated with historical chart examples, not quantified performance.
