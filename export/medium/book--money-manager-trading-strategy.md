# The Money Manager Trading Strategy: the trader's summary

*Excerpt from Pruitt & Hill's 'Trading Strategies That Work' presenting a TradeStation/EasyLanguage template for volatility-normalized position sizing across markets.*

**George Pruitt and John R. Hill** · 2002 · Money Management & Position Sizing · intermediate

*Source coverage: full. PDF pages inspected: 1-3. These are study notes, not verified trading results.*

## Summary

A short excerpt from George Pruitt and John R. Hill's "Trading Strategies That Work" (Building Winning Trading Systems with TradeStation). The "Money Manager" is presented explicitly as a template rather than a standalone trading system: it demonstrates how to normalize position size across markets with different volatility ("market normalization") so that a fixed percentage of equity is put at risk regardless of which market is traded, using standard deviation of closing prices as the risk proxy. A simple 40-day breakout entry / 20-day breakout exit is included only to illustrate the position-sizing code in a working system, not as the book's recommended entry logic.

## Key points

- **Market normalization** — sizing positions so that the dollar risk is comparable across markets of differing volatility (e.g., Treasury bonds vs. soybeans), rather than trading the same number of contracts in every market.
- **Market risk** = 30-day standard deviation of closing prices × Big Point Value (dollar value of a one-point move).
- **Number of contracts** = (Initial Capital × Risk% per trade) ÷ Market Risk, rounded *down* to the nearest whole contract (never up, since rounding up increases risk exposure).
- Worked example: $100,000 capital, 2% risk per trade, Japanese Yen market risk of $750 → 100,000 × 0.02 / 750 = 2.67 → rounds down to 2 contracts.
- Illustrative entry logic (not the focus of the chapter): buy on a 40-day high breakout, sell short on a 40-day low breakdown; exit longs on a 20-day low, cover shorts on a 20-day high.
- EasyLanguage detail: the platform's Round() function rounds to nearest, so the code subtracts 1 when rounding produces a value greater than the true (unrounded) contract count, to enforce round-down-only behavior; a MaxList() floor ensures at least 1 contract is always traded.
- The authors recommend Nauzer J. Balsara's "Money Management Strategies for Futures Traders" (1992) for further reading on money management schemes.

## Actionable rules

1. Compute market risk per contract as StdDev(Close, 30) × Big Point Value for each market traded.
2. Set a fixed risk percentage per trade (example uses 2% of account equity).
3. Contracts to trade = floor((Equity × Risk%) / Market Risk); never round up.
4. Enforce a minimum of 1 contract if the formula rounds to zero.
5. (Illustrative entries only) Enter long on a 40-day high breakout, short on a 40-day low breakdown; exit on a 20-day low (longs) or 20-day high (shorts).

## Caveats

This is explicitly framed by the authors as a demonstration template for position-sizing code, not a validated trading system — no backtest results, win rate, or drawdown statistics are given for the illustrative 40/20-day breakout entries. The EasyLanguage code is specific to TradeStation and would need translation for other platforms.

## Who it is for

Systematic/mechanical traders who already have an entry method and want a concrete, codeable volatility-normalized position-sizing formula to apply consistently across multiple markets.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: position-sizing, volatility-normalization, tradestation, easylanguage, market-normalization, breakout
