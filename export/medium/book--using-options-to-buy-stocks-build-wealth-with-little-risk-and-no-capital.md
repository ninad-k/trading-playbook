# Using Options to Buy Stocks: Build Wealth with Little Risk and No Capital: the trader's summary

*Sells long-dated LEAP puts on quality stocks to harvest overpriced premium and fund further stock purchases without new capital.*

**Dennis Eisen** · 2000 · Options, Futures & Derivatives · intermediate

*Source coverage: partial. PDF pages inspected: 3-4, 30, 32-33, 223 (the screening criteria and the simulation-run results). These are study notes, not verified trading results.*

## Summary

Eisen, a retired actuary and long-time buy-and-hold investor, built a strategy of selling long-term equity options (LEAPS) puts on financially strong companies he would be happy to own, using the collected premiums to keep buying stock after his retirement contributions were capped. His core claim: option pricing models (Black-Scholes) ignore expected earnings growth, so long-dated puts on growing companies are systematically overpriced relative to their true assignment risk — the gap widens the longer the option's life, making 24–30 month LEAPS more mispriced than short-dated options. He backtested selling at-the-money LEAP puts monthly on the ~217 stocks with LEAPS available in March 1997 over the prior decade (including the October 1987 crash) to show the approach survives severe drawdowns. The book also covers margin/collateral mechanics, volatility and premium calculation (Black-Scholes, European vs. American pricing), and hedging techniques for when trades move against the writer.

## Key points

- Standard option pricing (Black-Scholes) does not incorporate a stock's expected earnings growth rate, so premiums overstate the true probability of a long-dated put finishing in the money.
- Example: a 24-month at-the-money LEAP put on a $100 stock (0.40 volatility, 6% risk-free rate, 15% forecast earnings growth) has a modeled 31% chance of finishing in the money assuming no growth, but only 15.3% once growth is priced in — a much larger gap than for a 3-month put (43.1% vs. 35.8%).
- Author's screening criteria (initial/conservative version): S&P rating B+ or better, strike at least two intervals out of the money, expiration at least 15 months out, one contract at a time; later relaxed to B or better, expirations as close as 8 months, multiple contracts, and at-the-money or one strike below.
- Target premium: roughly $500+ per contract; largest single premium realized was $3,600 (Dell January 2000 LEAP put, strike $160, stock at $180).
- Avoid extremely low-volatility stocks (premium too small to cover commissions/margin) and extremely high-volatility stocks (roughly 0.75+ volatility signals binary "double or bankrupt" risk).
- Collateral/margin for a naked put is the greater of two formulas, roughly 20% of stock value plus premium (at the money) or 10% of stock value plus premium (deep out of the money); requirement can paradoxically rise even as the position gets safer because the formula was built for calls.
- Mitigation tools when a trade goes against the writer: rolling the put out (later expiration) and down (lower strike) for a net credit; bull put spreads or diagonal put spreads to cap maximum loss; a "double-glove" combination of selling one strike below at-the-money and buying further out-of-the-money protection.
- In over 600 transactions the author was assigned stock early (before expiration) only 6 times; each case still generated a net profit once the original premium was counted.
- Broker stop and stop-limit orders on options are largely unavailable to retail customers and are discouraged anyway, since a temporary dip can trigger an exit right before the stock (and put) recovers.

## Actionable rules

1. Sell LEAP (long-dated, ~1–2.5 year) puts only on stocks you would be comfortable owning outright at the net cost (strike minus premium).
2. Favor higher-quality names: S&P rating of B or better as a baseline screen.
3. Target strike price at or one interval below at-the-money for pure premium income; use a strike one or two intervals above (into the money) if the specific goal is to be assigned the stock cheaply.
4. Avoid stocks with volatility above roughly 0.75; treat these as having meaningfully elevated bankruptcy/blowup risk.
5. Aim for a minimum premium around $500 per contract; skip trades that don't clear a reasonable premium given the collateral tied up.
6. Spread sales evenly across the calendar (dollar-cost-averaging the premium collection) rather than concentrating in one window.
7. If a short put moves against you, prefer rolling out-and-down (close the losing put, sell a longer-dated, lower-strike put) over accepting assignment or holding to expiration.
8. Maintain margin account equity well above minimums — the author's own comfort levels were roughly 2 contracts per $25,000 of account equity, scaling to 20 contracts per $250,000.

## Caveats

The strategy depends on continuous access to LEAPS on quality names, a margin/naked-put-writing account (not available to all investors or account sizes), and stable option-pricing assumptions (constant volatility, no dividends in several worked examples) that don't always hold in practice. The backtest period (1987–1997) predates the dot-com crash and 2008, so tail-risk behavior in a sustained bear market is not directly demonstrated. Numbers, stock symbols, and margin rules reflect late-1990s exchange conventions (pre-decimalization strike intervals, NYSE Rule 431) and may not match current option market structure.

## Who it is for

Experienced, well-capitalized investors already comfortable with margin accounts and naked option writing who want an income overlay on a long-term, buy-and-hold equity portfolio — not a guide for short-term options trading or for investors without meaningful account equity.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: leaps, put-writing, options-income, margin, hedging, stock-acquisition
