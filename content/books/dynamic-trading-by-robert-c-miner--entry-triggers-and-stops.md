---
title: Dynamic Trading — Entry Triggers and Stop-Loss Rules
author: Robert C. Miner
year: 1997
slug: dynamic-trading-by-robert-c-miner--entry-triggers-and-stops
tier: A
category: Fibonacci, Gann & Elliott Wave
tags: [entry-triggers, stop-loss, trade-management, price-action, gann]
difficulty: advanced
doc_type: system
parent: dynamic-trading-by-robert-c-miner
pages: 505
one_liner: "A catalogue of daily-bar trend-reversal and trend-continuation entry triggers, each with an exact, mechanical initial stop-loss placement."
related: [dynamic-trading-by-robert-c-miner, gann-w-d-new-stock-trend-detector]
source_file: "Dynamic.Trading.by.Robert.C..Miner.pdf"
---

## What it is

Miner's Chapter 6 execution layer: a set of fully mechanical daily-bar patterns for entering trades, each paired with a specific initial stop-loss rule, split into trend-reversal triggers (used only at a projected time/price/pattern reversal zone — see the companion Time, Price and Pattern Projection system page) and trend-continuation triggers (used to add to or initiate positions once a new trend is already established). All are described for identifying a top/short entry; the mirror-image rules apply at a bottom for long entries.

## Rules

**Trend-reversal entry triggers** (only valid when the market is at a projected reversal zone — otherwise these patterns are common and not meaningful):

1. **Reversal Day (RD)** — the market makes a new high, then closes below both the current day's open and the prior day's close. Variants, in increasing strength: Key Reversal Day (also opens below the prior close), Outside Reversal Day, Outside Key Reversal Day. Stop: one tick above the reversal day's high.
2. **Signal Day (SD)** — opens in the top third of the day's range, makes a new high, closes in the bottom third of the range (the close need not be below the prior close, only below the day's own open). Gap Signal Day (GSD): the entire day's range gaps above the prior day's range — a stronger version. Stop: one tick above the signal day's high.
3. **Snap-Back Reversal Day (SBRD)** — a two-day pattern. Day 1: opens in the lower third, makes a new high, closes in the upper third (looks bullish). Day 2: opens in the upper third, closes in the lower third. Stop: one tick above the higher of the two days' highs.
4. **Reversal-Confirmation Day (RCD)** — used when the actual pivot did not produce an RD/SD/SBRD. Enter (sell) on any close below the current day's open and the prior day's close, within roughly 1–3 days of the suspected pivot. A stronger variant additionally requires the day's low to exceed the prior day's low. Stop: no further than one tick beyond the pivot extreme (may be placed closer, e.g., above a minor swing high formed since the pivot).

Entries are placed via a Stop-Close-Only order for RD (known criteria before the close) or a limit/market order in the closing minutes for SD/SBRD (since the day's range isn't fully known until near the close).

**Trend-continuation entry triggers** (used only in the direction of the already-established trend):

5. **Inside-Day set-up** — an inside day (high and low both within the prior day's range) forms. As long as the low of the day *before* the inside day hasn't been exceeded, buy one tick above the high of that pre-inside-day. Stop: one tick below the lower of the inside-day low or the entry-day low.
6. **Outside-Day set-up** — a day of range expansion. If, intraday, price first exceeds the prior day's low without first exceeding the prior day's high, buy one tick above the prior day's high. Stop: one tick below the low of the entry day. Exit on the close if the close falls below the current day's open and the prior close (failure to confirm). Outside-Day-Plus-One (OSD+1): the same buy-stop carried over to be triggered the next day if not filled intraday, or maintained even after an OSD exit, until the outside day's range is broken.
7. **Gann Pull-Back (GPB)** — built on the observation that minor corrections against an established trend usually run about three days. For a sell set-up in a downtrend: once the three most recent days show higher highs (or two higher highs plus one inside day), place a sell-stop one tick below the low of the prior day; ratchet the stop down (adjust to one tick below the new prior-day low) each time a new correction high is made. Initial protective buy-stop: one tick above the higher of the entry day's high or the day before it. Exit the position on the close of the entry day if that close is above the day's open and the prior close (failure to confirm follow-through). Buy-side rules mirror this in an uptrend.

**General stop-management rules (apply to any of the above once filled):**
- Keep the stop relatively far from the market (at the swing extreme, or one tick beyond the Three-Day Low/High — the lowest/highest price of the three days measured back from the last extreme, excluding inside days) while the trend is unconfirmed or in its early stages.
- Tighten the stop to the Two-Day, then One-Day extreme once time/price/pattern analysis signals the trend is approaching a projected completion zone.
- Prefer to let the market's own stop end the trade rather than exiting at a fixed profit target, except when running a multi-unit position (cover a short-term unit near a conservative minimum objective; let the remaining unit(s) run on the trailing stop).
- Treat the stop level as a candidate stop-and-reverse point whenever the same price also constitutes a valid opposite-direction entry signal.

## Risk

The maximum acceptable dollar capital-exposure per trade must be fixed in the trading plan before entry; if the mechanical stop distance for a given setup would exceed that ceiling, the trade is not taken at all — the stop is never moved closer than the rule specifies just to fit a position-size budget. Every entry rule above has its stop distance defined by market structure (a specific tick beyond a specific bar's high or low), not by a percentage or dollar amount chosen in advance, so position size (contracts/shares) is the variable that adapts to the stop distance and the account's exposure ceiling — not the reverse. No trade is initiated without the stop level being decided first.

## Caveats

These patterns are common in any trending or choppy market and are explicitly not reliable as reversal signals on their own — Miner cites unnamed studies showing daily reversal-day patterns fail as standalone reversal indicators, and states they should only be acted on at a projected time/price/pattern reversal zone. "One tick above/below" placement predates decimalized, high-tick-count electronic markets and needs rescaling to modern minimum price increments and typical intraday noise. The Gann Pull-Back and Inside/Outside-Day set-ups can require two or three failed attempts (small stop-outs) before a successful entry in a genuinely resuming trend, by Miner's own worked examples — the method assumes the trader will take each qualifying signal rather than discretionarily skip after a loss. All variants are illustrated on daily bars for futures markets of the 1990s; intraday application is mentioned as possible but not worked through with examples.
