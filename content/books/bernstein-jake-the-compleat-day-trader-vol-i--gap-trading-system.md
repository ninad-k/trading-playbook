---
title: "Gap Trading System (GO / Delayed GDO)"
author: Jake Bernstein
year: 1995
slug: bernstein-jake-the-compleat-day-trader-vol-i--gap-trading-system
tier: A
category: Day Trading & Scalping
tags: [gap-trading, opening-gap, futures, day-trading, stop-orders]
difficulty: beginner
doc_type: system
parent: bernstein-jake-the-compleat-day-trader-vol-i
pages: 242
one_liner: "Bernstein's opening-gap fade system: buy a gap-down open near the previous day's low (or its delayed, first-hour-confirmed variant), sell a gap-up open near the previous day's high."
related: [bernstein-jake-the-compleat-day-trader-vol-i, bernstein-jake-the-compleat-day-trader-vol-ii, jake-bernstein-stock-market-strategies-that-work]
source_file: "Bernstein, Jake - The Compleat Day Trader Vol I.pdf"
---

## What it is

A low-attention gap-fade system built on the definition that an opening price gap occurs when today's open is above yesterday's high (gap up) or below yesterday's low (gap down). Orders are placed either right at the open or one hour after it, and the trade is typically closed the same day — Bernstein cites low required screen time as the method's main appeal relative to the book's indicator-driven systems. Two variants: the basic Gap Opening (GO) method, entered immediately at the open, and a Delayed Gap Down/Up (GDO) method that waits through the first trading hour before committing, to avoid being run over by a gap that continues in its opening direction.

## Rules

**Basic gap opening (GO) method:**
1. Identify a gap-down open (today's open below yesterday's low) or a gap-up open (today's open above yesterday's high), using day-session price data only — the source stresses this is important and should not be based on overnight/extended-hours prints.
2. On a gap-down open, enter long on a buy stop set two ticks above the previous day's low.
3. On a gap-up open, enter short using the mirror-image sell stop two ticks below the previous day's high.

**Delayed Gap Down Buy (GDO), and its gap-up mirror for sells:**
1. On a gap-lower opening, place a buy stop two ticks above the low of the previous day — identical to the basic GO entry level.
2. If that buy stop has not been elected (triggered) by the end of the first hour of trading, do not abandon the setup; instead watch the current price relative to today's opening price.
3. If, after the first hour, price is trading above the opening price by two ticks or more, enter the long position at the market rather than waiting further for the original stop level.
4. Apply the mirror-image logic for a gap-up opening to generate a delayed short entry.

**Both variants:**
5. Exit intraday, using either a fixed-dollar risk stop, a technical stop, or by the close of the session — the book frames the gap methods as same-day trades by default.

## Risk

The initial stop/entry offset in both variants is denominated in ticks (two ticks beyond the relevant prior-day extreme) rather than dollars or percent of equity, so dollar risk scales with the instrument's tick value and the distance to the trader's chosen protective stop. No specific protective-stop distance or percent-of-equity sizing rule survives in the sampled pages for this system; the book's general risk framing (a stop sized to an acceptable dollar loss, converted to a trailing stop once profitable) applies here by extension. Because entries are tied to a fixed two-tick trigger regardless of gap size, very large gaps can produce a materially different risk/reward profile than small ones — no gap-size filter or minimum/maximum threshold is given for this basic version.

## Caveats

The two-tick entry offset is a fixed default in the sampled text, not derived per-instrument; a market with a very different tick value or volatility profile than Bernstein's tested futures contracts would likely need a different offset. The GDO variant's purpose — avoiding a whipsaw where the basic GO stop is barely triggered and then reverses — is explained qualitatively, but no comparative GO-versus-GDO win rate or average trade appears in the sample. The book states that gap determination must use day-session data only, warning against overnight/Globex-style prints; applying the system to a near-continuous 24-hour instrument requires deciding what counts as the "session open" and "previous day's high/low" in the first place, a judgment call the source does not resolve.
