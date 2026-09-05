---
title: "Long-Term Secrets to Short-Term Trading: TDW/TDM Calendar Filters"
author: Larry Williams
year: 1999
slug: larry-williams-long-term-secrets-to-short-term-trading--tdw-tdm-filters
tier: A
category: Day Trading & Scalping
tags: [seasonality, calendar-effects, futures, bonds, s-p-500, day-of-week]
difficulty: intermediate
doc_type: system
parent: larry-williams-long-term-secrets-to-short-term-trading
pages: 254
one_liner: "Williams' day-of-week and trading-day-of-month calendar biases, both usable standalone or as filters, backed by decades of open-to-close statistics."
related: [larry-williams-how-to-trade-better]
source_file: "Larry Williams - Long-Term Secrets To Short-Term Trading.pdf"
---

## What it is

Two related calendar-based statistical biases Williams uses as a first-pass filter on nearly every other pattern in the book, but which he also shows produce standalone profits when traded alone. Trading Day of the Week (TDW) measures open-to-close price bias by weekday; Trading Day of the Month (TDM) measures bias by the count of elapsed trading days in the current month (not the calendar date, which shifts around weekends and holidays). Williams attributes the concept partly to researcher Sheldon Knight but says he has relied on it the most of anyone.

## Rules

**TDW bias (documented, 1968–1998 depending on market):**
- Stocks (S&P 500): tend to rally on Mondays — open-to-close positive 57% of the time, average +$109/trade.
- Bonds: tend to rally on Tuesdays — open-to-close positive 55% of the time, average +$53/trade; also positive on Thursdays open-to-close.
- Grains (all markets tested): tend to rally on Wednesdays.
- British Pound: rallies off the open 55% of the time on Wednesdays, average +$18/trade.

**Standalone tradable TDW system (S&P 500):** buy the open on Monday + 0.05% of Friday's range; exit at the close same day. Backtest: $95,150 net profit, 435 winners of 758 trades (57% accuracy), $125 average profit per trade.

**Standalone tradable TDW system (Bonds):** buy the open on Tuesday + 70% of Monday's range; exit at the close same day. Backtest: $28,812 profit, 53% accuracy, $86 average profit per trade (Williams notes a better exit technique improves this materially).

**TDW as a filter on a volatility breakout system:** applied to a 100%-of-prior-day's-range breakout system in Bonds (base system: $73,468 profit, 80% accuracy, 651 trades, $112.86 average profit, $10,031 drawdown, 1990–Aug. 1998), restricting entries to the best buy days (Tuesday, Thursday) and best sell days (Wednesday, Thursday) cut trades roughly in half, raised profit-per-trade to $173, cut drawdown to $3,500, and raised accuracy to 84%.

**TDM rules:** count trading days elapsed in the current month (a month has up to 22 trading days). Backtested Bond TDM sells: TDM 18 or TDM 22 entries with $1,500 stop; TDM 12 sells with $1,400 stop and 3-day exit (1986–mid-1998). Backtested best-TDM tables (not itemized day-by-day in the source) produced $211,910 profit trading Bonds ~6 days/month (with a $1,500 stop from entry day) and $387,320 trading the S&P ~7 days/month (no stop on entry day, $2,000 stop thereafter), both over the 1982–1998 sample.

**Combined filter (TDW + TDM + intermarket trend):** stacking a volatility breakout with TDW, then adding a Bond-price-trend confirmation filter (only buy if Bonds close higher than 5 days ago; only sell if Bonds close lower than 35 days ago) on the S&P system above raised average profit per trade from $228 to $281 and cut drawdown from $13,025 to $5,250; the largest losing trade fell from $8,150 to $2,075. Combining all three filters together reduced total profit to $76,400 but raised average profit per trade to $444 and win rate to 90%.

## Risk

- TDW/TDM is not, by itself, a full risk-managed system — every quoted backtest pairs it with the book's standard exits (fixed dollar stop plus bailout exit, or a stated N-day time exit).
- Williams treats TDM specifically as a "setup" or leading indicator rather than a trade he takes unconditionally every time it fires — he states he reserves judgment based on other confirming conditions present at the time.
- Adding more simultaneous filters (TDW + TDM + intermarket trend) consistently reduces trade count and total profit while raising win rate and per-trade profit and cutting drawdown — a explicit quality-over-quantity trade-off documented across the book's combined-filter examples.

## Caveats

- All statistics are historical averages over specific multi-decade windows (grains to 1968, Bonds to 1977, S&P to 1982) and are explicitly offered as a "bias," not a guarantee that any given week or month will repeat the pattern.
- The book documents that market structure itself changed materially within the sample (e.g., Bonds began trading near-24-hour sessions after October 1988, and the Thursday Fed-report effect on Friday Bond prices disappeared later in the study period), meaning the underlying calendar bias is not presented as fixed or permanent.
- No formal statistical significance testing (beyond raw win-rate/profit figures) is presented for the TDW/TDM effects.
