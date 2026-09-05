---
title: "Trend Following: Appendix C Illustrative System (Trading Recipes)"
author: Michael Covel
year: 2004
slug: michael-covel-trend-following--trading-recipes-illustrative-system
tier: A
category: Trend Following & Mechanical Systems
tags: [trend-following, breakout-system, atr, position-sizing, futures, backtest]
difficulty: intermediate
doc_type: system
parent: michael-covel-trend-following
pages: 344
one_liner: "Covel's fully coded example system: 89-day breakout entry, 13-day breakdown exit, 2% equity risk sized off ATR — shown to illustrate mechanics, not as a recommendation."
related: [curtis-faith-way-of-the-turtle, turtlerules]
source_file: "Michael Covel - Trend Following.pdf"
---

## What it is

A mechanical, price-only breakout system built in Bob Spear's Trading Recipes software and reproduced in the book's Appendix C purely to demonstrate how a trend-following system enters, sizes, and exits a trade. It trades a small diversified futures portfolio (currencies, energies, grains, softs — 15 markets total) and is explicitly not offered as a live trading recommendation; the backtest uses only in-sample data (1991–2001) with no commissions or slippage.

## Rules

**Entry**
- Long entry stop = highest high of the last 89 days + 1 tick (`MAX[H,89,1] + TICK[1]`).
- Short entry stop = lowest low of the last 89 days − 1 tick (`MIN[L,89,1] − TICK[1]`).
- A resting stop order is placed at this level each day; price touching it fills the entry.

**Exit**
- Long exit stop (trailing) = lowest low of the last 13 days − 1 tick (`MIN[L,13,1] − TICK[1]`).
- Short exit stop (trailing) = highest high of the last 13 days + 1 tick (`MAX[H,13,1] + TICK[1]`).
- The exit stop is recalculated daily while in the trade; if the day's price range touches it, the position is closed.

**Position sizing (risk 2% of equity per trade, taking the more conservative of two sizing methods)**
1. Compute a 15-day Average True Range (`ATR[15]`) and convert it to dollars via the instrument's point value (`MANAGER[1] = ATR[15] × POINTVALUE`).
2. Method A — risk vs. actual stop distance: `contracts_A = (TotalEquity × 0.02) / |entry price − stop price| in dollars`.
3. Method B — risk vs. volatility: `contracts_B = (TotalEquity × 0.02) / (2 × MANAGER[1])` (i.e., 2% of equity divided by twice the dollar value of 15-day ATR).
4. Take the smaller of the two contract counts (more conservative sizing).
5. Cap the result at 100 contracts regardless of what the formula produces.
6. Round down to whole contracts.

**Worked example (from the text):** a Canadian Dollar short entered 14-Dec-1994 with account equity of $2,205,963. Entry/stop distance gave 37.1 contracts (Method A); volatility-based sizing gave 95.9 contracts (Method B). The system took the smaller value, 37 contracts, then applied the 100-contract cap (not binding here), yielding a final 37-contract position.

**Starting parameters used in the book's backtest:** starting cash $1,000,000; sample period 1991-01-01 through 2000-12-31; 15-market portfolio spanning currencies, energies, grains, and softs.

## Risk

- Fixed 2% of current total equity is risked per trade, computed against the *worse* (larger) of two candidate position sizes — actual stop distance or 2× the 15-day ATR — so the system never risks more than 2% by either measure.
- Equity used for the 2% calculation is marked-to-market current equity, not the account's original starting balance, so position size shrinks automatically after losses and grows after gains.
- A hard cap of 100 contracts per position overrides the sizing formula regardless of equity or volatility.
- No portfolio-level heat limit, correlation control, or maximum number of concurrent positions is specified beyond the per-trade 2% and per-position 100-contract cap.

## Caveats

- Illustrative only — the author explicitly states this is shown to demonstrate mechanics, not as a system to trade.
- Backtest uses in-sample data exclusively (1991–2000); no out-of-sample or walk-forward validation is presented.
- Commissions and slippage are excluded from the reported results ("for the sake of simplicity"), which will materially overstate real-world performance, especially given the system trades 18,879 total items over the test.
- Portfolio composition (15 specific futures markets) was not itself optimized or stress-tested in the text — it is presented as a convenience sample.
- No explicit filter, volatility regime check, or trade-frequency limit beyond the breakout/breakdown levels themselves; whipsaws are expected and unmitigated by design.
