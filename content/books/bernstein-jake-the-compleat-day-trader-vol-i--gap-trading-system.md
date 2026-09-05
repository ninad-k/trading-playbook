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

A low-attention gap-fade system built on the definition that an opening price gap occurs when today's open is above yesterday's high (gap up) or below yesterday's low (gap down). Orders are placed either right at the open or one hour after it, and the trade is typically closed the same day — Bernstein cites low required screen time as the method's main appeal relative to indicator-driven systems in the same book. Two variants are given: the basic Gap Opening (GO) method, entered immediately at the open, and a Delayed Gap Down/Up (GDO) method that waits through the first trading hour before committing, to avoid being run over by a gap that continues in its opening direction.

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

The initial stop/entry offset in both variants is denominated in ticks (two ticks beyond the relevant prior-day extreme) rather than dollars or percent of equity, so dollar risk scales with the instrument's tick value and the distance between the entry trigger and the trader's chosen protective stop. No specific protective-stop distance or percent-of-equity sizing rule survives in the sampled pages for this system specifically; the general risk framing elsewhere in the book (a stop distance sized to an acceptable dollar loss, converted to a trailing stop once profitable) applies here by extension. Because entries are tied to a fixed two-tick trigger regardless of the size of the gap itself, very large gaps can produce a materially different risk/reward profile than small ones — the source does not give a gap-size filter or minimum/maximum gap threshold for this basic version.

## Caveats

The two-tick entry offset is a fixed default in the sampled text, not derived per-instrument; a trader applying this to a market with a very different tick value or volatility profile than the futures contracts Bernstein tested should expect to need a different offset. The delayed (GDO) variant's purpose — avoiding a whipsaw where the basic GO stop is barely triggered and then reverses — is explained qualitatively, but no comparative backtest of GO versus GDO win rate or average trade appears in the sampled pages. The book states that gap determination must use day-session data only and explicitly warns against using overnight/Globex-style prints to define the gap, which matters for any market that trades close to continuously; applying the system to a 24-hour instrument requires deciding what counts as the "session open" and "previous day's high/low" in the first place, a judgment call the source does not resolve.
