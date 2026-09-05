---
title: "Call & Put Ratio Backspread System"
author: George A. Fontanills
year: 2005
slug: fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed--ratio-backspreads
tier: A
category: Options, Futures & Derivatives
tags: [options, ratio-backspread, delta-neutral, volatility-skew, spreads]
difficulty: intermediate
doc_type: system
parent: fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed
pages: 592
related: []
one_liner: "Sell fewer near-the-money options and buy more further options in a 1:2 or 2:3 ratio, placed for a net credit or near-zero debit, to profit from a big move with capped risk in between."
source_file: "Fontanills - The Options Course - High Profit And Low Stress Trading Methods, 2nd Ed.pdf"
---

## What it is

A volatility-skew strategy the author calls a "vacation trade" because, once placed correctly, it needs little monitoring. A call ratio backspread sells a smaller number of lower-strike calls and buys a larger number of higher-strike calls (same expiration); a put ratio backspread sells a smaller number of higher-strike puts and buys a larger number of lower-strike puts. Because the short leg (fewer contracts, often more expensive due to volatility skew) partly or fully funds the long leg (more contracts, cheaper), the trade can be structured for a net credit or at breakeven. The payoff resembles a limited-risk zone between the strikes (where the trade can lose) flanked by unlimited profit potential beyond the long strikes if the underlying makes the anticipated large move, and a profit (the credit) if the underlying moves the "wrong" way through the short strike and both legs expire worthless.

## Rules

**Market selection**
1. Trade medium-priced underlyings, roughly $25–$75 a share (or equivalent futures); avoid very expensive, very volatile underlyings like S&P 500 futures where the economics rarely work.
2. For a **call** backspread: look for a market with a **reverse volatility skew** — lower strikes carry higher implied volatility (are relatively overpriced) than higher strikes (relatively underpriced) — and a bullish bias, ideally an industry-leading stock with growing quarter-over-quarter earnings.
3. For a **put** backspread: look for a **forward volatility skew** — lower strikes carry lower IV than higher strikes — with a bearish bias, best placed on strong downtrending stocks (protects long-term bullish positions elsewhere as a hedge, too).
4. Confirm the stock has liquid, exchange-listed options across the needed strikes and at least 90 days to expiration; LEAPS are explicitly favored so time works in the trade's favor rather than against it.

**Entry / construction**
5. Choose a ratio that is a multiple of 1:2 (most common) or 2:3; avoid ratios above 0.67 (i.e., don't buy fewer than ~1.5× the short contracts) except in a genuinely slow market, where up to 0.75 is acceptable at the cost of more risk.
6. **Call ratio backspread:** sell the lower-strike call(s) (ITM or ATM), buy a greater number of higher-strike calls (OTM), same expiration.
7. **Put ratio backspread:** sell the higher-strike put(s) (ITM or ATM), buy a greater number of lower-strike puts (OTM), same expiration.
8. Solve for the ratio that makes the trade delta neutral and as close to a net credit as possible: Credit = (short contracts × short premium × 100); Debit = (long contracts × long premium × 100). Adjust the ratio until credit ≥ debit if possible — a true free (or credit) backspread has no loss if the market reverses against the anticipated direction, only a bounded loss zone between the strikes if the underlying stalls between them.
9. Avoid placing the trade for a net debit if possible; if a debit is unavoidable, only proceed if comfortable losing that full amount (it becomes the position's defined maximum risk in the loss zone).
10. Never leg into the spread — place all legs as a single multi-contract order at a limit price.
11. Write the trade (ratio, strikes, expiration, credit/debit, planned exit) in a trading journal before calling it in.

**Exit**
12. Exit or reduce the position 30 days or less before expiration unless there is strong conviction the underlying will keep moving in the anticipated direction — time decay and gamma both accelerate against multi-leg spreads in the final month.
13. Watch for early-assignment risk on the short leg: once it has a quarter point (¼) or less of time value remaining, assignment probability rises materially — close the spread at that point if it hasn't already been closed.
14. Take partial profits once gains reach roughly 50% or more: close an equal number of short and long contracts, and let the remaining long option(s) — now effectively "free" (cost basis at or below zero) — ride for further gains.
15. If the underlying moves against the anticipated direction and breaks through the unfavorable breakeven (below the downside breakeven on a call backspread, above the upside breakeven on a put backspread), simply let the options expire worthless and keep the net credit.
16. If the underlying sits inside the two breakevens as expiration approaches (the loss zone), close the entire position — buy back the short leg(s), sell the long leg(s) — to mitigate the loss rather than let it run to expiration.

## Risk

Maximum risk is limited and calculable at entry: for a call backspread it is [(number of short calls × difference between strikes) × 100] minus any net credit received (or plus any net debit paid); for a put backspread it is the equivalent calculation on the put side. This maximum loss occurs only if the underlying finishes between the strikes at expiration — not from an adverse move beyond the strikes, which is the direction the trade is actually designed to profit from. Reward is unlimited beyond the long strike (call backspread, upside; put backspread, downside) because the trade holds more long contracts than short. If the underlying reverses hard against the position's original bias and moves through the *short* strike instead, the credit is generally kept and the trade shows a small profit rather than a loss, provided it was constructed at a net credit — this is the main structural attraction over a simple long option or vertical spread. As with all strategies in this book, position-level risk should also respect the account-wide caps: no more than 5% of capital on one trade, no more than 50% deployed at once.

## Caveats

The strategy depends on being able to identify genuine volatility skew (reverse for calls, forward for puts) rather than an illusion created by a low-liquidity options chain; the book gives no quantitative threshold for what counts as an exploitable skew, only qualitative examples. The "vacation trade" framing likely overstates how hands-off the position really is — early-assignment monitoring, the 30-day exit rule, and the profit-taking step all require active attention, not passive holding. No historical backtest or win-rate data is given for the ratio backspread as a system; the worked examples (EBAY, INTC) are single illustrative trades, not a statistically validated track record.
