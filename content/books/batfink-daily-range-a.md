---
author: MarkJ
category: Day Trading & Scalping
difficulty: intermediate
doc_type: manual
one_liner: Mechanical GBP/USD intraday-range breakout system entering 40 pips from
  the daily close, with staged profit targets and trailing stops, backtested May-Oct
  2006.
pages: 16
related:
- forex-intraday-pivots-trading-system-complete-system
- automated-intraday-open-pivot-setup
- camarilla-levels
- day-trading-the-currency-market
reviewed_pdf_pages: 4-8 (the entry-line construction, target ladder and the per-pair
  results tables)
slug: batfink-daily-range-a
source_file: Batfink Daily Range (A).pdf
source_review: partial
tags:
- forex
- day-trading
- daily-range
- mechanical-system
- gbp-usd
- trailing-stop
- backtest
tier: B
title: BatFink Daily Range (A)
year: 2006
---

## Summary

A retail-authored, purely price-based (no indicators) intraday Forex system built around the prior day's closing price ("Home Line," set at 00:00 GMT). It enters on a breakout 40 pips from the Home Line and manages the trade through four staged profit targets with trailing stops. Manually backtested May-October 2006 on GBP/USD (best results), USD/CHF, USD/JPY and EUR/USD.

## Key points

- Home Line (HL) = price at 00:00 GMT (prior close). Entry lines L1/L2 are set 40 pips above/below HL.
- Initial stop-loss (SLA) is 10 pips above/below HL (i.e., 30 pips from the entry lines).
- Four profit targets from HL: T1 = 55 pips, T2 = 70 pips, T3 = 85 pips, T4 = 100 pips (110 pips for GBP/USD).
- Recommended position size: no more than 3% of account per trade.
- On hitting T1, stop moves to "SLB"; on hitting T2, stop becomes a 30-pip trailing stop; the trade is closed by T4 or trailing stop.
- Backtest hit rates (all pairs, May-Oct 2006): ~75% reached T1, ~50% reached T2, ~34% reached T3 (once T3 is hit, T4 is usually also reached).
- Same-direction re-entries are allowed intraday if price falls back below the prior stop level and then re-breaks L1/L2 (accounts for ~70% of re-entries observed).
- All open/pending orders are flattened at 22:00 GMT (New York close); highest volatility window is European session open to 18:00 GMT.
- Largest observed drawdown over the 6-month backtest was 150 pips (worst on EUR/USD).
- Author recommends demo-trading the system for 3 months before going live, and notes spread costs were not factored into results (recommends not adding spread to the first target only).

## Actionable rules

1. Chart timeframe: 1-hour candles.
2. Mark HL at 00:00 GMT = prior day's close; mark L1 = HL + 40 pips, L2 = HL - 40 pips.
3. Enter long at L1 breakout, short at L2 breakout.
4. Initial stop-loss: 10 pips beyond HL on the entry side (SLA).
5. Profit targets from HL: 55 / 70 / 85 / 100 pips (110 for GBP/USD); ratchet the stop to the prior target level each time a target is hit, switching to a 30-pip trailing stop after target 2.
6. Position size ≤ 3% of account equity per trade.
7. Close all positions/orders at 22:00 GMT regardless of status.
8. Allow re-entry in the same direction intraday only if price closes back through the prior stop before re-breaking L1/L2.

## Caveats

Manually backtested on only 6 months of 2006 data across 4 pairs, with no forward-test or out-of-sample validation, and results are described as understated (registered target hits rather than full trailing-stop gains). Spread/commission is explicitly excluded from the reported results. GBP/USD outperformed the other pairs materially; the system was not tested beyond these four pairs. "Version A" implies companion variants exist that are not included here.

## Who it is for

Discretionary Forex day traders who want a fully mechanical, indicator-free range-breakout system to test on GBP/USD, with concrete entry/stop/target levels ready to code or trade manually.
