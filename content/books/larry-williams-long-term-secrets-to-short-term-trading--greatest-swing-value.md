---
title: "Long-Term Secrets to Short-Term Trading: Greatest Swing Value"
author: Larry Williams
year: 1999
slug: larry-williams-long-term-secrets-to-short-term-trading--greatest-swing-value
tier: A
category: Day Trading & Scalping
tags: [volatility-breakout, position-sizing, futures, bonds, s-p-500, stops]
difficulty: intermediate
doc_type: system
parent: larry-williams-long-term-secrets-to-short-term-trading
pages: 254
one_liner: "Williams' volatility-offset entry built from average failed intraday swings; Bond and S&P versions backtested to six-figure profits with $1,600-2,500 stops."
related: [larry-williams-how-to-trade-better]
source_file: "Larry Williams - Long-Term Secrets To Short-Term Trading.pdf"
---

## What it is

A volatility-based entry technique Williams developed from 1977 onward and calls one of the most durable tools in his arsenal. The "greatest swing value" (GSV) measures how far price moved from the open toward the high on down-close days, or toward the low on up-close days — a "failure swing," since that move did not hold through the close. Averaging these failure swings over the past few days gives a volatility cushion added to (or subtracted from) the next open to set an entry level for a contra-trend/mean-reversion trade, always layered on an oversold/overbought setup filter.

## Rules

**Bond buy:** setup requires today's close lower than the close 5 days ago (oversold), restricted to Tuesday/Wednesday/Friday (TDW filter). Compute the 4-day average "buy swing" (open-to-high distance over the last 4 days). Entry: open + 180% of that average. Stop $1,600; exit on first profitable opening after 2 days in the trade.

**Bond sell:** setup requires close greater than 6 days ago, and (better performance) Gold lower than 20 days ago. Compute the 4-day average "sell swing" (open-to-low distance). Entry: open − 180% of that average. Same $1,600 stop and 2-day bailout exit.

**S&P 500:** same 180%-of-4-day-average-swing offset (buy-swing = high − open; sell-swing = close − low). TDW filter: buy Mon/Tue/Wed, sell any day but Monday. Setup filter: close lower than 6 days ago for a buy, higher for a sell, plus Bonds closing higher than 15 days ago for a buy / lower for a sell (intermarket confirmation). Stop $2,500 flat, bailout exit. Backtest: $105,675 profit, 67% winners, $427 average profit per trade (long side stronger than short in the tested bull-market sample).

**Stop-and-reverse variant:** for a tighter band, use the largest failed swing value of the past few days (instead of the 4-day average) as the open offset, with a stop-and-reverse just beyond that level.

**Monday variant (S&P):** setup requires a down close Friday and Bonds closing Friday higher than 15 days ago. Entry: buy Monday at Friday's open + (Friday's high − Friday's open) swing value. Exit: bailout and $2,500 stop, or open minus the swing value (or below the prior day's low if that value is unusually large). Tested 1982–March 1998; Williams calls it "the most successful interday mechanical trading technique I know of."

Williams tested averaging windows up to 10 days and found the previous 1–4 days consistently produced the best results — longer smoothing did not help.

## Risk

- All variants pair the GSV offset with a fixed dollar stop: $1,600 (Bonds), $1,750 (the S&P/Bond volatility-breakout variant using GSV as a filter, see main book page), or $2,500 (S&P 4-day-average and Monday variants).
- Exits are standardized to the bailout technique (first profitable opening, delayed 2 days for Bonds) rather than a profit target.
- Williams notes his backtest software could not simulate an intraday stop on the entry day itself, so live results should show smaller losses than the historical figures reported.

## Caveats

- Every quoted result is an in-sample backtest (1982–1998 for the S&P set, 1990–1998 for the Bond set); no out-of-sample test is shown.
- The pattern is explicitly described by Williams as "dumb" in the sense that it has no forecasting power about which specific trade will be the big winner — he states you must take every signal mechanically, since picking and choosing tends to select losers and skip winners.
- The S&P version's strong results were generated during "a gargantuan bull market," per the author's own caveat, and short-side results were markedly weaker than long-side results in that sample.
