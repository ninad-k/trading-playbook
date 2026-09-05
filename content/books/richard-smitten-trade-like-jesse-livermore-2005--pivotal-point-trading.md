---
title: "Livermore Pivotal Point & Top-Down Trading System"
author: Richard Smitten
year: 2005
slug: richard-smitten-trade-like-jesse-livermore-2005--pivotal-point-trading
tier: A
category: Trend Following & Mechanical Systems
tags: [jesse-livermore, pivotal-points, top-down-trading, tape-reading, trend-following, position-sizing]
difficulty: intermediate
doc_type: system
parent: richard-smitten-trade-like-jesse-livermore-2005
pages: 238
related: []
one_liner: "Confirm market, industry-group, and sister-stock direction top-down, enter only at a Reversal or Continuation Pivotal Point with volume confirmation, size in via a 20/20/20/40 probe, and cap loss at 10%."
source_file: "Richard Smitten - Trade Like Jesse Livermore (2005).pdf"
---

## What it is

A discretionary, price-and-volume-only trend/breakout system reconstructed from Jesse Livermore's trading, combining three layers: a top-down directional filter (overall market, then industry group, then a "sister stock" in the same group), a specific entry trigger (the Pivotal Point — either a Reversal Pivotal Point marking a new trend or a Continuation Pivotal Point confirming an existing one), and a tranche-based position-sizing method (the "probe"). Livermore did not use charts; he tracked prices numerically on a hand-ruled ledger (his "Market Key," reprinted in the book's closing chapter), which gives the pattern-recognition rules below fixed point thresholds rather than purely visual judgment. The system works on any timeframe and either direction (long or short) — it never depends on macro forecasting, only on confirmed price/volume action.

## Rules

**Step 1 — Top-down direction filter (must pass before considering any stock)**
1. Determine the "line of least resistance" (Livermore's term, deliberately avoiding "bull"/"bear") for the overall market the stock trades on (Dow, Nasdaq, S&P, Amex). Only trade in that direction.
2. Identify the stock's industry group and confirm the group as a whole is moving in the same direction as the intended trade. A legitimate group move requires at least the group's two leading stocks to be moving together — unless a single stock represents over 50% of the group's volume, in which case tracking that stock alone suffices.
3. Tandem/sister-stock check: compare the target stock to a same-group leader (e.g., GM vs. Ford, Morgan Stanley vs. Merrill Lynch). Both must show the same pattern before proceeding. This step exists because Livermore held that stocks in a group rarely move alone.
4. Final due diligence on the individual stock before pulling the trigger — a last independent check, made alone, that all upstream signals still hold.
5. Restrict candidates to leading stocks in leading groups only; do not trade cheap/laggard stocks even if a group is strong.

**Step 2 — Entry trigger: Pivotal Points**
6. **Reversal Pivotal Point** — the price marking a definite change in the prior trend. Confirming evidence: a volume surge of roughly 50%–500% over the average daily volume accompanying the reversal (a "climax" of buying met by selling, or vice versa).
7. **Continuation Pivotal Point** — a pause/consolidation within an established trend (support/resistance forms as buyers and sellers reach rough equality) that, when broken in the direction of the prior trend, confirms the trend is intact and offers an additional entry or add-on point.
8. Do not anticipate which way a Continuation Pivotal Point or consolidating base will resolve — wait for the breakout itself.
9. Entry window: do not initiate more than roughly 5%–10% above (below, for shorts) the Reversal Pivotal Point price — beyond that the trade is considered too late and the edge lost.
10. Treat a **One-Day Reversal** (today's high > yesterday's high, but today's close < yesterday's close, on higher volume than yesterday) occurring during an otherwise intact uptrend as a danger signal warranting an exit, even without a full Pivotal Point reversal.
11. New highs (for longs) or new lows (for shorts) that clear a prior consolidation are treated as bullish/bearish continuation signals — because they clear out the supply of trapped former buyers/sellers who had been waiting to exit near breakeven.

**Step 3 — Formalizing Pivotal Points: the Market Key ledger (optional but makes rules codeable)**
12. For a stock priced above roughly $30, record price only when it moves about 6 points from the last recorded extreme — this defines a "Natural Rally" or "Natural Reaction" (minor moves are otherwise ignored).
13. Maintain six tracking columns per stock: Secondary Rally, Natural Rally, Upward Trend, Downward Trend, Natural Reaction, Secondary Reaction. A move that exceeds the last Natural Rally by 3+ points gets promoted into the Upward Trend column (symmetric logic for reactions into the Downward Trend column).
14. For added reliability, combine two stocks in the same group into a single "Key Price" using a 12-point threshold (double the single-stock 6-point threshold) instead of trading off one stock alone.
15. The last price recorded in the Upward or Downward Trend column becomes a marked Pivotal Point once the ledger starts recording in the opposite (reaction/rally) column. A trend is confirmed as resuming only if price subsequently pushes 3 points beyond that marked Pivotal Point (6 points for the combined Key Price); failure to do so signals the trend may be over.

**Step 4 — Position sizing (the probe)**
16. Decide the full target position size before entering.
17. Build the position in tranches rather than all at once — Livermore's example ratio: 20% on the first purchase, 20% on the second, 20% on the third, 40% on the final purchase.
18. Each successive tranche must be bought at a *higher* price than the last (for shorts, a *lower* price) and only after the prior tranche is already showing an open profit — a losing probe is not added to.
19. Cap position count: hold no more than ~10 positions at a time, preferably 5 or fewer.

**Step 5 — Exit / stop**
20. Set a hard stop before entry, typically anchored at the Pivotal Point itself; never risk more than 10% of invested capital on the position.
21. Never meet a margin call or average down into a loser — close the position instead.
22. While the position remains correct (no valid sell signal, no One-Day Reversal, group/tandem confirmation intact), let it run without a fixed profit target.
23. After a large ("windfall") profit, move roughly 50% of it out of the trading account.

## Risk

Per-trade risk is capped at 10% of invested capital, enforced by a hard stop set at entry (usually the Pivotal Point level). The book's reproduced loss-recovery table makes the rationale explicit: an 8% loss requires an 8.7% gain to recover, a 20% loss requires 25%, and a 50% loss requires a full 100% gain to breakeven — the steep convexity of recovery is the stated justification for cutting losses early rather than "hoping." Position-level risk is further controlled by the probe method itself: because each tranche is added only after the prior one shows a profit, a losing thesis is capped near the size of the first (smallest, ~20%) tranche rather than the full intended position. Portfolio-level risk is controlled by limiting the number of concurrently held names (≤10, ideally ≤5) so each can be watched closely, and by keeping a standing cash reserve at all times rather than staying fully invested.

## Caveats

The system is entirely discretionary in its pattern-recognition steps (what counts as a "leading" stock, a valid consolidation, or genuine group confirmation is a judgment call), even though the Market Key ledger and the probe ratios give it more numeric precision than most narrative trend-following descriptions. No backtest, win rate, or performance statistic is provided anywhere in the book — the only evidence offered is Livermore's own anecdotal trades (the 1907 and 1929 crashes) and a handful of 1999–2004 chart illustrations chosen after the fact to match the theory. The Market Key's point thresholds (6-point reactions, $30 minimum price, 12-point combined Key Price) were calibrated to 1930s–40s stock price levels and are not directly portable to modern decimalized, much-higher-priced, or percentage-volatility-scaled markets without the trader rescaling them (e.g., to a percentage basis) independently — the book does not provide that conversion. The top-down/tandem-stock framework also assumes a trader can reliably identify a stock's "sister" and its industry group's true leadership, which requires external market-structure knowledge the system itself does not supply.
