---
title: Market Profile — Construction and Reading Rules
author: Chicago Board of Trade
year: 1996
slug: cbot-a-six-part-study-guide-to-market-profile--market-profile-construction-and-reading
tier: A
category: Market Structure & Price Action
tags: [market-profile, tpo, value-area, initial-balance, day-types, liquidity-data-bank]
difficulty: intermediate
doc_type: system
parent: cbot-a-six-part-study-guide-to-market-profile
pages: 346
one_liner: "Step-by-step rules for building a Market Profile graphic, classifying the day type, calculating the value area, and reading LDB volume for continuation/change."
related: [dynamic-trading-by-robert-c-miner, elder-alexander-trading-for-a-living]
source_file: "Cbot - A Six-Part Study Guide To Market Profile.pdf"
---

## What it is

A codeable procedure for building the Market Profile graphic from price/volume data, classifying each session into one of four day types, computing the value area, and overlaying actual volume (the Liquidity Data Bank, LDB) to judge whether a move is being "facilitated" (likely to continue) or losing participation (likely to end). It is a market-reading and classification framework, not a signal generator — it identifies regime and who is in control, leaving entries/exits to the user.

## Rules

1. **Build the profile.** Divide the session into fixed brackets (originally half-hour, one letter per bracket). For every price traded in a bracket, record that letter at that price; stacked letters form a histogram (one letter at one price = one TPO, Time/Price Opportunity). The first bracket(s) is the "pioneer range."
2. **Find the initial balance**: the high-low range while only the short-term trader is active (empirically ~first hour; longer in extended electronic sessions).
3. **Classify the day** by comparing later range extension to the initial balance: ≥85% of range inside it → **Normal day** (short-term trader controls); extension up to ~2x, one direction → **Normal Variation** (control split); extension well beyond 2x, one direction, close on the extreme → **Trend day** (long-term trader controls); extension both directions → **Neutral day** (uncertainty, higher reversal risk).
4. **Calculate the 70% value area**: start at the highest-volume price; repeatedly add whichever adjacent price (above or below the band) has more volume; stop at ≥70% of session total. A cruder proxy, the TPO value area, is the range bounded by two-or-more single prints per side (a single print = a price touched by only one TPO letter — a rejection).
5. **Classify initiating vs. responsive activity**: buying above value or selling below = initiating (new money flow, the stronger signal); selling above value or buying below = responsive (fading back). Strong responsive activity at a fresh extreme warns the extension may fail.
6. **Track control across sessions**: plot each day's value-area range on a long-term chart. Value areas moving vertically = trend continuing; moving sideways = the auction stalled, favoring reversal or basing.
7. **Overlay LDB volume**: rising volume as price extends = facilitated move (favors continuation); falling volume = not facilitated (favors reversal). Commercial (CTI2) volume inside the value area is routine hedging; CTI2 buying above or selling below value is a deviation and a stronger signal. A value area sitting mid-range suggests the market is efficient there and more likely to start a new move than keep distributing.

## Risk

The framework has no position-sizing, stop, or target rules of its own — it is a market-structure lens layered under the trader's own system. Its practical risk use is regime identification: a Neutral day, a failed range extension, or a mid-range value area are all flagged as higher-uncertainty conditions warranting smaller size or no new directional entry until a fresh day type or value-area location clarifies control.

## Caveats

Construction assumes an official time-and-sales/TPO feed and CBOT's CTI-classified LDB volume; modern platforms replicate value-area and initial-balance mechanics via volume-profile tools, but commercial-vs-local classification has no standard retail equivalent. The half-hour bracket and "first hour" initial-balance convention is tuned to 1980s–1990s pit sessions and needs re-tuning per instrument for near-24-hour electronic markets. Day-type classification in the source's own examples is applied retrospectively, after the close — recognizing a Trend day while it is still forming requires judgment the text does not fully mechanize.
