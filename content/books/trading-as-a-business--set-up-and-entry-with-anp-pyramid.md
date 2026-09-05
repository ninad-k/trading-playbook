---
title: Set-Up and Entry Strategy Design with the ANP Pyramid
author: Charlie Wright
year: unknown
slug: trading-as-a-business--set-up-and-entry-with-anp-pyramid
tier: A
category: Trend Following & Mechanical Systems
tags: [strategy-development, mechanical-trading, money-management, position-sizing, backtesting, tradestation]
difficulty: intermediate
doc_type: system
parent: trading-as-a-business
pages: 169
one_liner: "A codeable framework for building any mechanical strategy from a Set-Up plus a rule-checked Entry, sized with a profit-funded ANP Pyramid position-sizing scheme."
related: [curtis-faith-way-of-the-turtle, van-tharp-trading-systems, money-management-report-van-tharp, richard-l-weissman-mechanical-trading-systems]
source_file: "Trading As A Business.pdf"
---

## What it is

A general-purpose method (not a single fixed indicator combination) for turning any indicator or price pattern into a mechanical trading strategy, then position-sizing it so that added contracts are funded only by the strategy's own accumulated profits. It has two components: (1) the "Set-Up and Entry" design discipline for building the trading rules themselves, applicable to trend-following, support/resistance, or volatility-expansion strategy types; and (2) the "ANP (Accumulated Net Profit) Pyramid," a specific position-sizing formula layered on top of any strategy that has a defined per-contract money-management stop.

## Rules

**Building the Set-Up and Entry:**

1. Choose a market type to trade — trending, directionless, or volatile — and a matching class of Set-Up indicator (e.g., trend: moving-average crossover, ADX rising, price outside a channel; support/resistance: RSI overbought/oversold, Stochastic %K/%D cross, price at a moving-average envelope band; volatility expansion: an opening gap over the prior bar's high, a bar range exceeding the recent average range).
2. Treat the Set-Up as necessary but not sufficient — it only signals "get ready," never triggers a position by itself.
3. Design a separate Entry that must satisfy two rules:
   - **Entry Rule #1** — price must move in the direction implied by the Set-Up before a position is taken (a bare market order fails this unless conditioned, e.g. "buy at market only if tomorrow's open exceeds today's high").
   - **Entry Rule #2** — the Entry (or a combination of entries) must guarantee the strategy will be in the market for every move it is designed to catch; an Entry that depends on an optional pattern (three consecutive up closes, a key-reversal bar) that might never occur during a strong move is a flawed Entry, even if it looks profitable in isolation.
4. Prefer stop orders for Entries: they force a fill once price crosses the trigger level regardless of time of day. Stop-Close-Only orders (fill only if the market closes through a level) are an acceptable second choice. Conditioned market orders are usable only with an added directional condition. Limit orders are avoided entirely — they require price to move against the Set-Up direction and are not guaranteed to fill even if touched.
5. When testing reveals the primary Entry can fail Rule #2 during unusually strong trends (verified by scrolling the chart, not just reading the Performance Summary), add a failsafe secondary Entry — typically a breakout of a longer-term high/low (e.g., a 50-bar high or low) — so the combined Entry logic cannot miss a large move.
6. Validate the finished strategy by comparing its combined performance against each component traded alone (Set-Up-only, each Entry-only): the combination should show a higher average trade, lower MAXID (Maximum Intra-day Drawdown), and materially better risk-adjusted return (ROMID = Net Profit / MAXID) than any single component, confirming the pieces are additive rather than redundant.
7. Sanity-check the result: require at least ~25–30 historical trades; the largest single winning trade should be no more than roughly 50% of gross profit or 25% of net profit; require the strategy to clear a return hurdle of roughly 2× the risk-free (T-Bill) rate for stocks or 4× for futures before considering it worth trading over holding cash.

**Sizing positions with the ANP Pyramid:**

8. Quantify per-contract risk first: attach a money-management stop to the strategy and optimize its distance over a reasonable range (e.g., test $1,000–$5,000 in $500 steps) to find the value that maximizes both Net Profit and ROMID; a stop hit far more than ~10% of the time is too tight and should be widened.
9. Fund the account before trading at all: capitalize with at least 3× the strategy's historical MAXID (plus required margin) so a normal drawdown cannot force the trader out.
10. Trade exactly one contract using personal capital while Accumulated Net Profit (ANP) — the strategy's running realized profit since inception — is at or near zero.
11. Choose a fixed percentage of ANP to risk per contract (test a range, e.g. 10–60%, and pick based on the Net Profit / ROMID / MAXID trade-off that matches personal risk tolerance — higher percentages compound faster but multiply drawdown). Add one additional contract for every increment of ANP equal to (money-management stop size ÷ chosen risk percentage); e.g., at 20% risk with a $4,000 stop, trade 2 contracts once ANP reaches $8,000 (2 × $4,000 ÷ 0.20 × ... equivalently: risk 20% of $10,000 ANP ≈ $2,000, funding 2 contracts at a $1,000-per-contract equivalent — scale contracts so total dollar risk stays at the chosen % of current ANP), and continue scaling up as ANP grows.
12. Revert to one contract (funded by personal capital) whenever ANP falls back to (or below) the level implied by the sizing formula — the trader is never willingly risking more of their original capital than the one-contract baseline, only accumulated winnings.

## Risk

Risk is controlled at two layers: a per-contract money-management stop (fixed dollar or point distance chosen by optimization, not by feel), and an account-level sizing rule that ties total contracts traded to accumulated profit rather than to a fixed percentage of total equity. The explicit account-funding rule — capitalize to at least 3× historical MAXID before risking real money — is presented as the primary defense against being forced out of a sound strategy by an ordinary, previously-observed drawdown. There is a stated trade-off, not a free lunch: in the book's own Swiss Franc worked example, raising the ANP risk percentage from 10% to 50% took Net Profit from roughly $98,000 to $3.4 million over the same 15-year test but took MAXID from roughly $16,000 to $1.6 million — the trader must pick a risk percentage they can actually sit through, using the optimization table rather than choosing the highest-return column by default.

## Caveats

The framework is platform-specific in its worked form (TradeStation/EasyLanguage order types and Performance Summary statistics — MAXID, ROMID, SPF/PS tables); the underlying logic (a confirmed, guaranteed-to-fire entry; profit-funded position scaling) transfers to other platforms, but the exact code will not. The ANP Pyramid assumes a futures-style contract structure with a known, roughly constant dollar risk per contract; adapting it to equities or instruments with varying per-share risk requires recalculating the effective "contract size" as volatility changes, which the source does not address. All worked examples use flat historical slippage/commission assumptions ($0–$100 per trade) and pre-2000 data (Swiss Franc futures 1982–1997, Coca-Cola stock 1970–1997); modern spreads, decimalized pricing, and electronic execution costs are not reflected. The optimization step used to select both the money-management stop and the ANP risk percentage carries an acknowledged curve-fitting risk that the source addresses only by requiring a minimum trade count and cross-checking Net Profit against ROMID and MAXID together, not through out-of-sample or walk-forward testing.
