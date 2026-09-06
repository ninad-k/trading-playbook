# Detecting Breakouts From Flags & Pennants: the trader's summary

*A Stocks & Commodities article coding a mechanical MetaStock system to detect and trade flag/pennant breakouts, backtested with a 187% return on Blue Coat Systems.*

**Markos Katsanos** · 2005 · Candlesticks & Chart Patterns · advanced

*Source coverage: full. PDF pages inspected: 1-9. These are study notes, not verified trading results.*

## Summary

Markos Katsanos presents a fully coded MetaStock system (9 lines) for identifying flag and pennant continuation patterns and trading their breakouts, built from statistics on 100 sampled flag/pennant formations and validated out-of-sample on 250 stocks. The system combines a zigzag-identified flagpole, linear-regression slope filters, and several momentum/volume indicators (stochastics, ADX, FVE, VFI) to flag high-probability setups, then exits using a statistically derived profit target plus four backstop conditions.

## Key points

- Flag/pennant duration is capped at 21 trading days (95th percentile of the 100-sample distribution); flags must last more than 2 days.
- Entry requires a flagpole rise of at least 2.2%/day (13-bar regression slope), a flag slope between -1.2% and +0.2%/day, and declining volume during the flag.
- Confirming filters: declining volatility during the flag; 20-day Stochastic > 55; 10-day ADX > 30; 22-day FVE > 10; 130-day VFI > -3; entry-day close above both yesterday's close and today's open.
- Profit target formula (regression-derived): Target % = 1.94 × (pole height %)^0.724.
- Other exits: stop on a close below the flag's lower trendline; inactivity exit after 14 days if profit is under 25% of target; trailing stop if price drops >10% from the 4-day high close; hard time exit after 24 days.
- Backtest on 4 stocks (2000–2005): Blue Coat Systems 187% profit (100% win rate, 7 trades) vs. -91% buy-and-hold; Applied Digital 111%; Great Atlantic & Pacific Tea 143%; US Gypsum 69% (60% win rate).
- A June 2003 scan of 1,250 stocks produced 13 trades, 85% winners, and a 735% annualized return (26.2% total return in 13 days) on a $100,000 hypothetical account.
- Most losing trades occurred in adverse markets or when a stock was already overextended from a prior successful breakout.

## Actionable rules

1. Enter long only when: flag duration 2–21 days, flagpole slope ≥ 2.2%/day, flag slope -1.2% to +0.2%/day, volume and volatility declining, 20-day Stochastic > 55, 10-day ADX > 30, 22-day FVE > 10, 130-day VFI > -3, close above prior close and today's open.
2. Exit at profit target = 1.94 × pole%^0.724.
3. Stop out on a close below the flag's lower trendline.
4. Exit for inactivity if held over 14 days with profit under 25% of target.
5. Trail a stop 10% below the highest close of the last 4 days; force-exit after 24 days.

## Caveats

The system was optimized on the same 100-sample dataset later used for its statistics, and the multi-hundred-percent returns come from very few trades (1–7 per stock, one 13-day scan) — not a long diversified track record. Requires MetaStock-specific formula language (Zig, LinRegSlope, Stoch, ADX, FVE, VFI) to reimplement exactly.

## Who it is for

Systematic/technical traders comfortable with MetaStock formula scripting who want a fully specified, quantified flag/pennant breakout system rather than a discretionary pattern-recognition approach.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: flags, pennants, breakouts, metastock, backtesting, volume, exit-rules
