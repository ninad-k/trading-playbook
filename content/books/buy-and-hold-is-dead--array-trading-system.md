---
title: The Array Trading System
author: Thomas H. Kee
year: 2010
slug: buy-and-hold-is-dead--array-trading-system
tier: A
category: Trend Following & Mechanical Systems
tags: [support-resistance, market-timing, mechanical-trading, day-trading, swing-trading]
difficulty: intermediate
doc_type: system
parent: buy-and-hold-is-dead
pages: 322
one_liner: "Six named strategies that trade a mechanical buy/short rule against a daily support/resistance array built from three time frames across the Dow, NASDAQ, and S&P."
related: []
source_file: "Buy and Hold Is Dead.pdf"
---

## What it is

Six rule-based strategies sharing one process: build a support/resistance "array" from three time frames (near-term 5-min/5-day, midterm 30-min/15-day, long-term daily/6-month), sort the levels around current price, and trade the same two buy rules and two short rules against whichever level price is nearest. The strategies differ in instrument, holding period, and stop mechanics, but all end flat/in cash between signals and none uses discretionary sizing.

## Rules

**Core signal logic (all strategies):**
- Buy when support is tested, or when resistance breaks higher.
- Short (or buy an inverse ETF) when resistance is tested, or when support breaks lower.
- A "test" is price coming within a small tolerance of a level: 0.05 points for an individual stock, 3 index points for the NASDAQ, 25 points for the Dow.

**Strategy 1 — Featured Stock of the Day** (day trading one stock, $5–$100, liquid, fixed share count): enter within $0.05 of the array level; stop loss $0.21, profit stop $0.35, trailing stop $0.10; trade 5 minutes after open to 5 minutes before close; re-enter after a stop up to 3 times; always flat overnight.

**Strategy 2 — Stock of the Week** (swing trading one stock, Monday–Friday): start/end each week in cash; exclude stocks with earnings or major news that week; unlimited same-week re-entries but updates only overnight, never intraday; closed by rule Friday before the close regardless of open P/L.

**Strategy 3 — Strategic Plan** (position trading the Dow via DDM/DXD ETFs, 1–3 months): fixed dollar size (e.g., $50K); enter only on a test of major long-term support/resistance (within 25 Dow points); stop loss 0.5%, trailing profit stop 10%; convert DDM↔DXD as price crosses the tested level, repeating as needed; never initiate mid-channel; mostly cash.

**Strategy 4 — Day Trading Strategy** (NASDAQ via QID/QLD, intraday only): buy QLD on a support test or resistance break, QID on the mirror; no fixed stop — exit immediately if the tested level breaks; "three-point rule" defines a test (within 3 NASDAQ points); "five-point rule" re-enters in the new direction after a 5-point move past balance; "one-point rule" exits to cash on a 1+ point reversal back through the level; max 2 stops per parameter (~1.5% loss cap), then that level retires until freshly tested; never held overnight.

**Strategy 5 — Swing Trading Strategy**: identical three-point/five-point/one-point rules and loss cap as Strategy 4, but positions are held overnight using the wider swing-trading array (midterm + long-term levels only).

**Strategy 6 — Lock and Walk Strategy**: Strategy 4's rules capped at one hour (typically the first); exits automatically at 1–2% gain or when the hour ends, whichever comes first.

## Risk

Every strategy fixes size mechanically (same share count or dollar amount every trade) rather than scaling with conviction, so risk is controlled entirely through the stop rules above, not sizing. The index strategies (4–6) cap loss near 1.5% of ETF value per parameter by limiting re-entries to two attempts, then require a fresh test of a different level before resuming — this "retire the level" rule is the primary defense against whipsaw losses in a choppy tape. Overnight risk is priced into the strategy choice itself: Strategies 1, 4, and 6 avoid it by closing flat each day; Strategies 2, 3, and 5 accept it as the cost of multi-day moves. A surprise overnight gap can exceed the mechanical stop; the prescribed response is to take the loss, revert to cash, and re-enter only if the rule-based trigger fires again.

## Caveats

The buy/short and test/break rules are internally consistent but depend entirely on the trader's own subjective trendline placement when building the array — two traders following the same instructions could produce different levels and different trades. No independent, out-of-sample backtest is presented; the worked examples are individual live/simulated trades from the 2008–2009 window, not a multi-year track record, so win rates and drawdowns should be read as illustrative, not statistically established. Several execution features (hidden conditional orders, automated simulators, correlated stock filters) are tied to the author's own brokerage/service platform and may not be replicable with a generic broker.
