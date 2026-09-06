---
title: "Volume Profile: Point of Control, Value Area and Volume Nodes"
author: "Ninad K"
year: unknown
slug: institutional-order-flow-and-amt-playbook--volume-profile
tier: A
category: "Quant, Microstructure & Academic Research"
tags: [volume-profile, point-of-control, value-area, high-volume-node, low-volume-node, naked-poc, futures]
difficulty: advanced
doc_type: system
parent: institutional-order-flow-and-amt-playbook
pages: 235
one_liner: "The book's volume-profile method: build the volume-at-price histogram, locate POC and the 70% Value Area with a precise two-row algorithm, and trade High/Low Volume Nodes and Naked POCs as rotation shelves, acceleration zones and revisit magnets."
related: [institutional-order-flow-and-amt-playbook, institutional-order-flow-and-amt-playbook--footprint-and-delta, institutional-order-flow-and-amt-playbook--vwap-and-session-levels, cbot-a-six-part-study-guide-to-market-profile]
source_file: "The Institutional Order Flow & Auction Market Theory Playbook.pdf"
---

## What it is

Volume Profile is a horizontal histogram of traded volume plotted against price rather than time: for a chosen window (a session, a visible range, a fixed range, a composite of several sessions, or an anchored range from a swing point or event), every trade increments the accumulator at its price row, and the resulting distribution shows where the market actually reached agreement (heavy rows) versus where it was merely passed through (thin rows). The book's central claim is that volume-at-price is harder evidence of institutional acceptance than price alone, because size cannot transact without displacing the order book — a price with a lot of volume is a price both sides repeatedly agreed to trade at, not just a price that was touched.

Five window types answer five different questions and must not be conflated: a **Session** profile resets daily and answers "where did today's auction accept price"; **Visible Range (VRVP)** recomputes on every zoom/scroll and is a charting convenience only — never a reproducible reference; **Fixed Range (FRVP)** is drawn once between two explicit anchors and frozen, used for a specific analytically-meaningful leg; **Composite** profiles concatenate many sessions to reveal the larger structural map; **Anchored** profiles run forward from a chosen event (a confirmed swing point, a news release) to show the average price paid since that pivot.

## Rules

1. **Match profile type to question before reading any level from it.** Session for today's acceptance, Composite/Fixed-Range for durable swing/position levels, VRVP only for a quick, non-reproducible eyeball read — never quote a VRVP level without freezing the exact date range that produced it.
2. **Point of Control (POC) = argmax(volume_at_price).** Distinguish the **Developing POC (DPOC)**, the running argmax while a session is still in progress (its migration direction is itself a trend tell — a DPOC that climbs with price confirms two-sided acceptance following the rally; a DPOC pinned low while price makes new highs warns the rally is not being accepted), from a **Naked/Virgin POC (NPOC)** — a completed prior session's POC that price has not since retraded, treated as an unfinished, statistically-likely-to-be-revisited magnet (more so when isolated than when several newer NPOCs sit between it and current price).
3. **Value Area (VA) is built mechanically, not eyeballed.** Starting at the POC row, repeatedly compare the sum of the next two rows above the current VA edge against the next two rows below; add whichever pair is larger; stop once cumulative volume reaches 70% of the session total. VAH/VAL are the resulting top/bottom rows. A fully worked 15-row example in the source (POC at 2,400 contracts, 15,000 total session volume) reaches target after three two-row steps, landing at 74.5% enclosed — slightly over 70%, which the book notes is normal since the algorithm only adds in complete two-row increments and never stops mid-step.
4. **The 80% Rule.** If price opens inside the prior session's Value Area and holds inside it for two consecutive ~30-minute periods, the source states a historically high probability (cited around 80%, without a shown sample) that price continues through the entire Value Area to test the opposite side.
5. **High-Volume Nodes (HVN) slow price; Low-Volume Nodes (LVN) accelerate it.** An HVN is a local peak (resting liquidity concentrated there, so an incoming order must work through a lot of size — rotational/choppy behavior); an LVN is a local trough (little resting liquidity, so price transits it fast) — the alternating HVN→LVN→HVN structure is described as the market's "rungs and gaps" of acceptance.
6. **Read volume context, not just shape, at any new extreme.** A new high/low printed on volume clearly above the recent row average, with the bid/ask split skewed in the breakout's direction, is acceptance (higher-conviction); the same new extreme on thin, oppositely-skewed volume is rejection (a vulnerable, exhaustion-prone print).
7. **Classify the completed or developing shape** — P (fat top, thin tail — trend-into-balance), b (fat bottom, mirror), D (bell curve, two-sided rotation), B (two humps split by an LVN gap — two distinct sub-auctions in one session), or thin/elongated (a low-negotiation trend day with few reliable rungs) — before reading any individual level inside it.
8. **Build a multi-profile confluence map before the session.** Stack session, composite, weekly and any live anchored profiles' POC/VAH/VAL; a price where two or more independently-derived levels cluster within a small tick tolerance is a confluence zone that should carry more size and wider expected defense than any single-source level.

## Risk

The source ties every profile-based read to a specific risk placement rather than treating levels as targets in isolation. A heavily-traded row (fat POC/HVN) is explicitly called a *poor* place to hold a stop, because its very liquidity means stops resting inside it get run on ordinary two-way churn, not because the underlying thesis was wrong — stops belong just beyond a VAH/VAL edge, beyond a stacked-imbalance zone, or inside a thin LVN band (which sees far less two-way rotation and is therefore statistically safer for a breakout stop than an adjacent HVN). Value-area fade trades are sized with the stop just beyond VAH/VAL plus a tick buffer, targeting POC first and the opposite edge only if momentum carries through; confluence-zone trades are explicitly sized with wider stops (the whole tolerance band) because a multi-level cluster is expected to be defended harder and chopped through more slowly than a single-source level. No fixed percentage-of-equity figure is given in this section — that framework lives in the parent book's risk chapter (position sizing, R-multiples, circuit breakers) and is not repeated here.

## Caveats

Volume profile construction (bin size, session boundaries, the two-row Value Area convention) varies by charting platform, and the book explicitly warns to confirm these settings before comparing POC/VA readings across tools or across days — a VRVP-derived POC in particular is a viewport artifact, not a fixed market fact, and the text is direct that quoting one without freezing the date range is a common analytical error. The 80% rule and the NPOC-fill-rate claim ("gets filled a large majority of the time within 1-10 sessions") are stated as historical/empirical findings but no sample, market, or time period is cited anywhere in the source — treat both as plausible heuristics inherited from classical Market Profile literature rather than validated statistics for any specific instrument you trade. Composite profiles are also explicitly flagged as laggy: after a genuine regime change, a composite will keep showing the old range as heaviest for some time even though price no longer wants to trade there, so an LVN or HVN read off a stale composite should be cross-checked against the current developing profile before being used as a live acceleration or rotation zone.
