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

A general-purpose method for turning any indicator or price pattern into a mechanical strategy, then sizing it so added contracts are funded only by the strategy's own accumulated profits. Two components: (1) "Set-Up and Entry," a design discipline for building the trading rules, usable for trend-following, support/resistance, or volatility-expansion strategies; and (2) the "ANP (Accumulated Net Profit) Pyramid," a position-sizing formula layered on any strategy with a defined per-contract money-management stop.

## Rules

**Building the Set-Up and Entry:**

1. Choose a market type — trending, directionless, or volatile — and a matching Set-Up indicator (trend: moving-average crossover, rising ADX, price outside a channel; support/resistance: RSI or Stochastic overbought/oversold; volatility: an opening gap or a bar range exceeding the recent average).
2. Treat the Set-Up as necessary but not sufficient — it signals "get ready," never triggers a position alone.
3. Design a separate Entry satisfying two rules: **#1** — price must move in the Set-Up's direction before entry (a bare market order fails unless conditioned, e.g. "buy at market only if tomorrow's open exceeds today's high"); **#2** — the Entry (or combination) must guarantee the strategy is in the market for every move it targets — an Entry dependent on an optional pattern (three up closes, a key-reversal bar) that might simply never occur is flawed even if profitable in isolation.
4. Rank order types: stop orders (best — fill once price crosses the trigger, any time of day) > Stop-Close-Only (needs a qualifying close) > conditioned market orders > limit orders (avoided — they require price to move against the Set-Up and aren't guaranteed to fill).
5. If the primary Entry can fail Rule #2 in an unusually strong trend (check by scrolling the chart, not just the Performance Summary), add a failsafe secondary Entry — typically a breakout of a longer-term high/low (e.g., a 50-bar high/low).
6. Validate by comparing the combined strategy against each component alone (Set-Up-only, Entry-only): it should show a higher average trade and better risk-adjusted return (ROMID = Net Profit ÷ MAXID) than any piece alone.
7. Sanity-check: require ≥25–30 historical trades; largest winning trade ≤50% of gross profit or 25% of net profit; require the strategy to clear roughly 2× the T-Bill rate (stocks) or 4× (futures).

**Sizing positions with the ANP Pyramid:**

8. Quantify per-contract risk: attach a money-management stop and optimize its distance (e.g., test $1,000–$5,000 in $500 steps) for the value maximizing both Net Profit and ROMID; a stop hit much more than ~10% of the time is too tight.
9. Capitalize the account to at least 3× the strategy's historical MAXID plus margin before trading at all.
10. Trade exactly one contract with personal capital while Accumulated Net Profit (ANP) is at or near zero.
11. Pick a fixed percentage of ANP to risk (test a range, e.g. 10–60%, choosing on the Net Profit/ROMID/MAXID trade-off). Scale contracts up so total dollar risk always equals that percentage of current ANP (e.g., at 20% risk with a $4,000 per-contract stop, a second contract is added once ANP reaches $40,000).
12. Revert to one contract whenever ANP falls back toward zero — original capital never funds more than the one-contract baseline; only accumulated winnings fund additional size.

## Risk

Two layers: a per-contract money-management stop (fixed distance chosen by optimization, not feel), and account-level sizing tying total contracts to accumulated profit rather than total equity. Capitalizing to 3× historical MAXID before risking real money is the primary defense against being forced out by an ordinary, previously-seen drawdown. This is a trade-off, not a free lunch: in the book's Swiss Franc example, raising ANP risk from 10% to 50% took Net Profit from ~$98,000 to ~$3.4 million over 15 years, but MAXID from ~$16,000 to ~$1.6 million — pick a risk percentage sustainable through the drawdown, not just the highest-return column.

## Caveats

Platform-specific in its worked form (TradeStation/EasyLanguage order types, MAXID/ROMID/SPF/PS terminology); the underlying logic transfers elsewhere but the exact code won't. Assumes a futures-style contract with roughly constant dollar risk per unit — adapting to equities or instruments with varying per-share risk requires recalculating effective "contract size" as volatility changes, which the source doesn't address. Worked examples use flat slippage/commission assumptions and pre-2000 data (Swiss Franc 1982–1997, Coca-Cola 1970–1997); modern spreads and execution costs aren't reflected. The optimization used to pick both the stop and the ANP risk percentage carries acknowledged curve-fitting risk, addressed only by a minimum trade count and cross-checking Net Profit against ROMID/MAXID together — not by out-of-sample or walk-forward testing.
