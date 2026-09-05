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

Six rule-based strategies sharing one process: build a support/resistance "array" from three time frames (near-term 5-min/5-day, midterm 30-min/15-day, long-term daily/6-month), sort the levels around current price, and trade the same buy/short rules against whichever level is nearest. The strategies differ in instrument, holding period, and stop mechanics, but all end flat between signals and none uses discretionary sizing.

## Rules

**Core signal logic (all strategies):**
- Buy when support is tested, or when resistance breaks higher.
- Short (or buy an inverse ETF) when resistance is tested, or when support breaks lower.
- A "test" is price within a small tolerance of a level: 0.05 points for a stock, 3 index points for the NASDAQ, 25 points for the Dow.

| Strategy | Instrument / hold | Key parameters |
|---|---|---|
| 1. Featured Stock of the Day | One stock $5–$100, day trade | Enter within $0.05 of array level; stop $0.21, profit stop $0.35, trailing stop $0.10; trade 5 min after open to 5 min before close; up to 3 re-entries; flat overnight |
| 2. Stock of the Week | One stock, Mon–Fri swing | Start/end week in cash; exclude earnings/news names; unlimited re-entries but updates only overnight; closed by rule Friday close regardless of P/L |
| 3. Strategic Plan | Dow via DDM/DXD, 1–3 months | Fixed size (e.g. $50K); enter only on test of major long-term S/R (within 25 Dow points); stop 0.5%, trailing profit stop 10%; convert DDM↔DXD across the tested level; never mid-channel |
| 4. Day Trading Strategy | NASDAQ via QID/QLD, intraday | Buy QLD on support test/resistance break, QID on the mirror; no fixed stop, exit on level break; 3-point test rule, 5-point re-entry rule, 1-point reversal exit; max 2 stops/parameter (~1.5% cap); never overnight |
| 5. Swing Trading Strategy | NASDAQ via QID/QLD, overnight | Same 3/5/1-point rules and loss cap as #4, but held overnight using the wider swing array (midterm + long-term levels only) |
| 6. Lock and Walk | NASDAQ via QID/QLD, 1 hour | Strategy 4's rules capped at one hour (typically the first); exits at 1–2% gain or when the hour ends |

## Risk

Every strategy fixes size mechanically (same share count or dollar amount every trade) rather than scaling with conviction, so risk is controlled through the stop rules above, not sizing. The index strategies (4–6) cap loss near 1.5% of ETF value per parameter by limiting re-entries to two attempts, then require a fresh test of a different level — this "retire the level" rule is the primary defense against whipsaw losses in a choppy tape. Overnight risk is priced into the strategy choice: 1, 4, and 6 avoid it by closing flat daily; 2, 3, and 5 accept it as the cost of multi-day moves. A surprise gap can exceed the mechanical stop; the response is to take the loss, revert to cash, and re-enter only if the trigger fires again.

## Caveats

The buy/short and test/break rules are internally consistent but depend entirely on the trader's own subjective trendline placement when building the array — two traders following the same instructions could produce different levels and different trades. No independent, out-of-sample backtest is presented; the worked examples are individual live/simulated trades from the 2008–2009 window, not a multi-year track record, so win rates and drawdowns should be read as illustrative, not statistically established. Several execution features (hidden conditional orders, automated simulators, correlated stock filters) are tied to the author's own brokerage/service platform and may not be replicable with a generic broker.
