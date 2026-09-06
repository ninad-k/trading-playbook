# Superior Returns from Average Indicators: the trader's summary

*A backtest of moving-average crossover systems on QQQQ (1990-2004) showing multiple MA combinations beating buy-and-hold with smaller drawdowns.*

**Easan Katir** · 2005 · Trend Following & Mechanical Systems · beginner

*Source coverage: full. PDF pages inspected: 1-4. These are study notes, not verified trading results.*

## Summary

**Question:** can a simple moving-average crossover system beat buy-and-hold (BAH) on a heavily-traded index? **Method:** a hypothetical $1,000,000 portfolio trading QQQQ from its 1990 IPO through 2004 (15 years spanning a bull market, bear market, and chop). The system buys in full when a short MA crosses above a long MA and sells to cash on the reverse cross; no position sizing, cash interest, or taxes modeled; commissions ignored given QQQQ's liquidity. **Finding:** every tested MA pair beat the $7.0M BAH result, with the best combinations reaching roughly $16-17.5M — over twice BAH — with smaller drawdowns and a less volatile equity curve.

## Key points

- Buy-and-hold control: $1,000,000 → $7,001,754 over 15 years.
- A 60-day/120-day moving-average crossover is shown as the representative example (the article does not say whether the averages are simple or exponential): long at the start of uptrends, whipsaws in chop, but avoids catastrophic drawdowns.
- Result matrix (short MA 10-60 days vs. long MA 120-240 days) ranges roughly $8.5M-$17.5M, all beating BAH; the best "plateau" zone averages around $16M.
- Only ~25 trades occurred over 15 years for the most active combination, making commissions immaterial.
- BAH is highly sensitive to starting date; the crossover method reduces that sensitivity by holding cash during downtrends.
- In extended bear markets the crossover system re-enters with more shares (cash buys more at lower prices), ending with over 400,000 shares vs. 175,439 for static BAH.

## Actionable rules

1. Buy the full portfolio when the short moving average crosses above the long moving average; sell to 100% cash on the reverse cross.
2. Tested pairs: short averages of 10-60 days against long averages of 120-240 days — all profitable, with longer-period combinations performing best in this backtest.
3. No stop-loss or position-sizing overlay is used; the crossover itself is the only risk control.

## Caveats

Single-instrument backtest (QQQQ only) over one period (1990-2004) — a classic overfitting risk, since many MA combinations were tried and the best "plateau" highlighted after the fact. No out-of-sample or other-market validation; taxes and slippage beyond stated assumptions are excluded, flattering the cash-holding periods versus real execution.

## Who it is for

Trend-following systematic traders wanting a simple, one-rule benchmark for moving-average crossover backtesting methodology and a caution about buy-and-hold's sensitivity to starting date.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: moving-averages, crossover-system, backtesting, trend-following, drawdown-control
