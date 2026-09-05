---
title: "RSI Extremes with 200-Day Moving Average Filter (Full System)"
author: "Richard L. Weissman"
year: 2005
slug: richard-l-weissman-mechanical-trading-systems--rsi-extremes-mean-reversion
tier: A
category: "Trend Following & Mechanical Systems"
tags: [rsi, mean-reversion, moving-average-filter, intermediate-term, stop-loss, oscillator]
difficulty: intermediate
doc_type: system
parent: richard-l-weissman-mechanical-trading-systems
pages: 241
one_liner: "An intermediate-term mean-reversion system that only fades RSI extremes in the direction of the 200-day trend, exiting at a partial RSI retracement or a 2.5% fail-safe stop."
related: [john-bollinger-bollinger-on-bollinger-band, van-tharp-trading-systems]
source_file: "RICHARD L. WEISSMAN - Mechanical Trading Systems.pdf"
---

## What it is

Weissman's best-performing intermediate-term "trend-following mean reversion" system: it buys oversold dips only when the market is above its 200-day moving average (and sells overbought rallies only when below it), so every trade is a pullback entry in the direction of the dominant long-term trend rather than a pure countertrend bet. Because the trade is aligned with the longer-term trend, the profit exit is set beyond the midline (60/40 instead of 50) rather than at dead-center reversion, and a fixed-percentage fail-safe stop caps the risk if the market keeps trending against the entry instead of reverting.

## Rules

**Indicators needed**
1. A 9-day RSI (Wilder's relative strength index) for entry signals.
2. A 14-day RSI for the profit-exit signal.
3. A 200-day simple moving average (SMA) of closing price, used only as a directional filter.

**Entry**
4. Go long when the 9-day RSI closes below 35 AND the close is above the 200-day SMA.
5. Go short when the 9-day RSI closes above 65 AND the close is below the 200-day SMA.
6. No trade is taken against the 200-day trend filter — an oversold reading below the 200-day average, or an overbought reading above it, is ignored.

**Exit — profit target**
7. Exit a long when the 14-day RSI crosses back above 60.
8. Exit a short when the 14-day RSI crosses back below 40.

**Exit — fail-safe stop**
9. Exit a long if price falls to entry price minus 2.5% of entry price.
10. Exit a short if price rises to entry price plus 2.5% of entry price.
11. For instruments where a percentage-of-value stop is unreliable (e.g., back-adjusted continuous futures data that can go to zero or negative), substitute a fixed-dollar stop sized to the instrument's typical volatility (the book's tested portfolio used stops ranging from $500 to $2,500 depending on the asset).

**Portfolio construction (as tested)**
12. Trade a portfolio weighted toward non-U.S.-dollar currency cross rates and one trending asset (e.g., a dollar pair) for balance, since major currency crosses historically showed the strongest mean-reversion tendency in the book's data; avoid low-volatility instruments (the book specifically flags eurodollars as too low-volatility to profit after a flat $100 round-turn cost).
13. Deduct a flat $100 per round-turn trade for slippage and commissions in backtesting.

## Risk

Per-trade risk is explicitly capped at the 2.5% fail-safe stop distance from entry (or the equivalent fixed-dollar amount). In the book's 10-year (1992–2002) backtest on a nine-instrument, mostly-FX-cross portfolio, the system produced $100,188 total net profit, a 2.27 profit-to-maximum-drawdown ratio, and a 54.57% win rate over 372 trades — a higher win rate but a lower P:MD than the book's trend-following systems (e.g., the two moving average crossover's 4.24 P:MD), which Weissman attributes to mean-reversion systems structurally cutting profits short at the mean rather than letting them run. On the same portfolio without the 200-day trend filter (an ADX-filtered nondirectional variant), results were worse in nearly every category, reinforcing that the directional filter is what makes this version work.

## Caveats

The book cautions that this system's exit condition (14-day RSI crossing 60/40) produced an average trade duration similar to the intermediate-term trend-following systems in the same book — a longer holding period than many mean-reversion traders expect — and that a stochastics-based variant with a tighter exit (20-day moving average) trades faster with a higher win rate but lower per-trade profit. The fixed 2.5% stop is tuned to daily-bar volatility; the book demonstrates elsewhere that the same percentage produced an outright losing system when applied unchanged to 30-minute bars, and had to be reduced to 1.5% to restore performance — so the stop distance must be rescaled to whatever bar interval and instrument volatility is actually being traded, not copied as a universal constant. As with all systems in this source, results reflect a single vendor's data (CQG), a single backtested decade, and flat commission/slippage assumptions.
