# Profit From Prices: the trader's summary

*A rule-based OHLC and volume manual for reversal, continuation, gap, and sideways-market signals.*

**Jayesh Patel** · 2007 · Market Structure & Price Action · intermediate

*Source coverage: partial. PDF pages inspected: 1-16, 41-56, 60-62, 80-82, 92-94 (the framework and discipline chapters, the signal taxonomy and the U-Turn, Full Stop, weekly-reversal and gap specifications). These are study notes, not verified trading results.*

## Summary

Jayesh Patel builds trading signals from daily and weekly open, high, low, and close, with volume as confirmation. The book treats prices as the aggregate result of participants' information and actions, then defines reversal, continuation, gap, expiration, volume-spike, sideways, and chart-pattern setups. Its discipline section calls for a written plan covering capital, per-trade commitment, entry, exit, risk, and monitoring (PDF pp. 5-9).

## Key points

- A bull day closes above its open; a bear day closes below it.
- A strong or weak open gauges overnight change relative to the prior close.
- Reversal signals after long trends are treated as stronger than signals after four to 20 days (PDF p. 53).
- Volume should increase after the candidate turning point.
- The approach separates a signal's detection from position sizing and stop placement.
- The author cautions against calling tops or bottoms solely because price looks extreme.
- Stop-loss orders are the defense against uncontrollable news and estimation errors.
- The signal catalogue is organised into five families: trend-reversal signals R1-R5 on daily prices (U-Turn, Jump-Start, Full Stop, Turn Around, Reverse), R6-R7 on weekly prices (Weekly-Reversal, 3-Week Reversal), continuation signals C1-C2 (Gap, Restart), miscellaneous signals M1-M4 (Monday Morning, Significant Day, Derivatives Expiration, Volume Spike) and sideways signals S1-S2 (Turn Back, Next Top/Bottom), followed by chart-based versions of the same ideas (PDF pp. 8-9, 41-151).
- **Signal strength is graded by lookback**: an extreme that is the highest or lowest of three or more weeks is the "strong form," expected to turn the major trend; an extreme that only spans three to ten trading days is the "weak form," read as the start of a reaction or the end of a correction (PDF p. 48).
- Each signal is given as an explicit OHLC inequality set plus a volume condition, and several are accompanied by a ready-made StockFetcher screening string — unusually reproducible for a retail book (PDF p. 48).
- **Weekly signals may be acted on before Friday's close**: the current price can stand in for This Week's Close, with the explicit instruction to liquidate promptly if the actual weekly close fails to confirm the signal (PDF p. 80).

## Actionable rules

1. For a U-Turn buy, require an established downtrend, today's low to be the lowest of recent days, and an open below the prior day's low. Then require price to reverse, close above both the prior open and prior close, and show noticeable volume expansion (PDF pp. 55-56).
2. Enter long only after all U-Turn conditions are known; place the stop at today's low (PDF p. 56). Reverse the logic for the sell setup.
3. Classify the signal as stronger when the extreme is the lowest or highest over weeks rather than only three to ten days.
4. For the mirror-image U-Turn sell, require a continued uptrend, today's high to be the highest of the recent period, today's open above the previous day's high, today's close below both the previous day's open and close, and volume decisively above the recent norm (PDF p. 48).
5. When trading a weekly signal early, treat the position as provisional: verify the signal against the actual weekly close and exit if it is not confirmed (PDF p. 80).
4. Define OHLC data conventions and adjustment for splits before backtesting.

## Caveats

This review covers the framework chapters, the signal taxonomy and several of the individual signal specifications, not every one of the roughly twenty signals. Claims of broad accuracy are not independently tested, and end-of-day confirmation can create next-session gap risk.

## Who it is for

Price-action traders who want explicit OHLC conditions to code and test on modern adjusted data.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: ohlc, price-action, trend-reversal, stop-loss, volume
