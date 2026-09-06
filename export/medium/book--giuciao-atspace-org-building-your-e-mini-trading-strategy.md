# Building Your E-mini Trading Strategy: the trader's summary

*Slide presentation on a seven-step process for building a CME E-mini futures trading strategy, from market/timeframe selection through candlestick-based entry rules to performance measurement.*

**Daniel Gramza** · 2005 · Day Trading & Scalping · intermediate

*Source coverage: partial. PDF pages inspected: 2, 5, 12-14, 88 (the contract specifications, the swing entry rules and the risk/heat discussion). These are study notes, not verified trading results.*

## Summary

A slide deck (presented by Daniel Gramza of Gramza Capital Management with IntesaTrade) walking through a seven-step framework for designing a trading strategy on CME E-mini index futures (S&P 500, NASDAQ-100, Russell 2000, S&P MidCap 400, Russell 1000) and CME FX futures: identify the market, pick a trading timeframe, choose fundamental vs. technical approach, build the strategy from trend analysis and Japanese candlestick patterns, define entry/exit parameters, measure performance (profit magnitude and "heat"/drawdown), and implement it.

## Key points

- **E-mini contract specs** — e.g. E-mini S&P 500 (ES): $50 × index, 0.25-point tick = $12.50; E-mini NASDAQ-100 (NQ): $20 × index, 0.50-point tick = $10.00; margin roughly 7% of notional versus ~50% for an equivalent SPDR position.
- **Trading timeframe menu** — scalping, micro day trading, macro day trading, swing trading, position trading, each with different demands on time, approach, and technology.
- **Trend-continuation rule** — a close above the previous swing high confirms an uptrend (buy trigger); a close below the previous swing low confirms a downtrend (sell trigger); a failed close through the prior swing signals a potential trend change.
- **Candlestick pattern components** — every reversal pattern breaks into five phases: Lead Up, Set Up, Trigger Price, Follow Through, Confirmation.
- **Candle characteristics used to grade a setup** — range (high-to-low), body color, body size, shadow location, and shadow size (a measure of buying/selling rejection).
- **Performance measurement** — for each trade, plot the profit magnitude and its frequency distribution, and separately track a "heat index" (how far price moves against the position before turning profitable) to size stops and gauge trade quality.
- **Trade-type distinction** — a "Type One" profitable trade never dips below entry (no heat); a "Type Two" trade dips below entry before recovering (has heat) — tracking the split shows how much risk a strategy carries per winner.

## Actionable rules

1. Uptrend entry: buy on a close above the previous swing high. Downtrend entry: sell on a close below the previous swing low.
2. A failed close through the prior swing high/low after a clear trend warns of a potential reversal — reduce confidence in continuation trades.
3. Illustrative example: enter (buy) the new high of a Japanese candle rejection pattern; exit (sell) on the first lower low that exceeds entry by more than 2 ticks.
4. Illustrative profit-management rule: at 4.00 points of open profit, sell half the position and move the stop on the remainder to breakeven (including costs).
5. Before combining studies (e.g., candles + stochastics), check each study's lead time, whether signals trigger together, and the combined effect on signal frequency, profit magnitude, and heat.

## Caveats

This is a conceptual slide deck, not a fully specified system: it presents the process and illustrative numeric examples (tick values, one profit-taking example, one entry/exit example) rather than one complete, backtested strategy with fixed parameters throughout. Chart diagrams referenced in the slides are not reproducible in text form. E-mini volumes/specs cited are from 2005 and are dated; underlying trend/candlestick concepts remain applicable.

## Who it is for

Traders new to building a systematic day-trading or swing-trading strategy on index or FX futures who want a structured checklist —from market selection through candlestick-based entries to performance/heat measurement — for developing their own rules.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: e-mini-futures, japanese-candlesticks, trend-analysis, trading-strategy-design, stochastics, risk-management, performance-measurement
