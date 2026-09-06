---
title: "Footprint Charts: Imbalance, Absorption and Delta Divergence"
author: "Ninad K"
year: unknown
slug: institutional-order-flow-and-amt-playbook--footprint-and-delta
tier: A
category: "Quant, Microstructure & Academic Research"
tags: [footprint, order-flow, delta, cumulative-volume-delta, imbalance, absorption, trapped-traders, futures]
difficulty: advanced
doc_type: system
parent: institutional-order-flow-and-amt-playbook
pages: 235
one_liner: "The book's footprint method: read bid-versus-ask volume per price, track delta and CVD divergence/exhaustion, flag diagonal imbalances and stacked zones, and distinguish absorption from genuine initiative by what happens on the next one to two bars."
related: [institutional-order-flow-and-amt-playbook, institutional-order-flow-and-amt-playbook--volume-profile, institutional-order-flow-and-amt-playbook--vwap-and-session-levels]
source_file: "The Institutional Order Flow & Auction Market Theory Playbook.pdf"
---

## What it is

A footprint chart explodes a single candle into its constituent transactions: every price the bar traded through gets its own row showing bid-side volume (aggressive selling into a resting buyer) versus ask-side volume (aggressive buying from a resting seller), written as "BID x ASK" (e.g., "120 x 340"). Aggressor side is inferred with the quote rule (trade at the best ask = buy, at the best bid = sell) or, on ambiguous mid-prints, the Lee-Ready tick rule — reliable in aggregate across thousands of prints, but the book flags it as probabilistic, not exact, especially during fast markets where quote updates can lag trade prints. Where a candlestick compresses a bar to four numbers (OHLC), a footprint keeps the full price-by-price transaction record, answering a question OHLC cannot: was a stall caused by aggressive sellers overwhelming weak buyers, or by a large passive buyer absorbing everything sellers could throw at the level?

**Delta** = (volume traded at the ask) − (volume traded at the bid) for a bar, session, or as a never-reset running total called **Cumulative Volume Delta (CVD)**. Delta is a flow measurement, not a price measurement — a bar can close red with positive delta and vice versa — and CVD's *slope*, not any single bar's value, is what the method reads.

## Rules

1. **Track delta at three nested scopes** — bar delta (resets each bar), session delta (resets each session), and CVD (never resets) — and never conflate them; use CVD slope as a directional filter, not a standalone trigger.
2. **Four advanced delta signals convert CVD into a trigger:** *divergence* (price makes a higher high but CVD makes a lower high, or the bearish/bullish mirror — the move is being carried by thinning participation); *exhaustion* (a single bar's |delta| exceeds 2× the last-20-bar average while its range is under 0.5× the average range — large one-sided aggression producing almost no follow-through); *confirmation* (price and CVD both make new highs/lows together — favors continuation); *delta flip* (CVD crosses sign exactly as price interacts with a pre-identified level — the aggressor population actually changed, not just paused).
3. **Footprint imbalance is a diagonal comparison, not a vertical one.** A buy imbalance at price P compares Ask(P) against Bid(P − 1 tick); a sell imbalance at P compares Bid(P) against Ask(P + 1 tick). Default threshold: ratio ≥ 300% (3:1) AND the larger side clears a minimum volume filter (the book's worked example: 10-15 contracts) so a 1-lot against a 3-lot doesn't falsely register. Three or more consecutive same-side flags form a "stacked" zone — a materially stronger institutional-grade support/resistance reference than one isolated cell, especially if the imbalance sits unfilled at the bar's own high or low when it closes.
4. **Distinguish absorption from initiative only by what happens next.** Both start identically — a large, lopsided-volume row. Initiative is followed by continued range expansion in the same direction with same-sign, often-accelerating delta on the next bar; absorption is followed by the price stalling or reversing within 1-2 ticks, with the next bar's delta flipping sign and volume often dropping sharply as the aggressor gives up.
5. **Trapped-trader pattern:** a wave of late aggressive buyers (or sellers) pushes to a new high (low) on a footprint row with unusually large ask (bid) volume, then price reverses hard before the bar or the very next bar closes; their resting protective stops then trigger as forced flow that fuels and extends the reversal — the reversal is entered once the bar closes back below (above) the extreme with delta turning against the trapped side.
6. **Finished vs. unfinished auctions.** A literal zero on one side at a bar's extreme (e.g., "0 x 45" at the low) means that side gave up entirely — a resolved, low-revisit-priority extreme; both sides non-zero at the extreme ("35 x 20" at the high) means the negotiation there was still active when the bar ended — an unresolved, higher-revisit-priority extreme.
7. **Read POC location within the bar for strength.** On a bullish (up-closing) bar, POC at the bottom (heaviest trading occurred at the low, before the close ran away from it) is the strong, accumulation signature; POC at the top (most volume near the close/high with little follow-through) is the weak signature — mirrored for bearish bars.
8. **Never read a footprint signal in isolation from the volume profile.** The same absorption or imbalance signal at a random mid-range price is noise; at VAH, VAL or POC it is signal — confirm or deny the level (absorption/delta-flip against the approach = the level holds; a stacked imbalance breaking through with sustained delta = the level is denied and value is expanding).

## Risk

Every footprint setup in the source is given a structural, not arbitrary, stop: a stacked-imbalance fade is stopped 1-2 ticks beyond the zone's low/high (a clean break through the whole zone invalidates it as support/resistance); an absorption fade is stopped 1-2 ticks beyond the absorption row's own extreme (a genuine break through it after the fact means the passive order was finally exhausted); a trapped-trader reversal is stopped 1-2 ticks above/below the original extreme that trapped the late entrants (reclaiming that level means they were bailed out, not trapped); a divergence entry is stopped 1-2 ticks beyond the higher-high/lower-low that produced the divergence. Targets are similarly structural — the session's developing POC, the next volume-profile HVN/LVN, or the opposite value-area boundary — rather than fixed point counts. The book is explicit that large delta with no price progress (a big print that moves nothing) is information about a large passive counterparty and frequently *precedes a reversal*, calling this out as the single most common way novice traders misread "big green delta bar" as automatically bullish.

## Caveats

Aggressor classification is inferential except where an exchange supplies an explicit flag (e.g., CME futures); on aggregated retail or spot-forex/CFD feeds the book itself (in a chapter not detailed on this sub-page) says the classification can be unreliable or effectively meaningless, which undercuts every delta-based rule above outside centralized-matching-engine futures. No source, sample size, or backtest underlies the imbalance ratio's default 300% threshold or the specific tick/volume figures in the worked examples — treat them as a reasonable, internally-consistent starting convention to validate on your own instrument and data feed, not an empirically optimized parameter. As with the rest of this book, every numeric example (delta values, CVD tables, imbalance ratios) is a clean, invented illustration rather than a captured real trading session.
