---
author: Tushar S. Chande and Stanley Kroll
category: Indicators
difficulty: intermediate
doc_type: system
one_liner: 'A fully backtested trend system: buy/sell stop when price closes on the
  same side of a CMO-indexed VIDYA for two consecutive days, reverse on the opposite
  signal, flat $1,500 stop.'
pages: 115
parent: chande-kroll-the-new-technical-trader
related:
- perry-kaufman-smarter-trading
slug: chande-kroll-the-new-technical-trader--cmo-vidya-trading-system
source_file: Chande Kroll - The New Technical Trader.pdf
tags:
- momentum
- moving-average
- mechanical-system
- backtesting
tier: A
title: The CMO-Driven VIDYA Trading System
year: 1994
---

## What it is

A single-indicator, always-in-the-market trend-following system built entirely on VIDYA (Variable Index Dynamic Average), a moving average whose smoothing constant is scaled by the absolute value of the Chande Momentum Oscillator (CMO), so it speeds up in strongly trending/volatile conditions and flattens in quiet ones. The system was backtested across ten years of daily data (roughly 1983–1993, split into two five-year blocks) on a broad set of futures markets (bonds, currencies, metals, softs, grains, livestock) using System Writer Plus.

## Rules

**Indicator construction**
- Compute the 9-day sum of up-day price changes (Su) and down-day price changes (Sd).
- `CMO = (Su − Sd) / (Su + Sd)`, bounded −1 to +1; `absCMO = |CMO|`.
- `VIDYA(today) = (0.5 × absCMO) × Close(today) + (1 − 0.5 × absCMO) × VIDYA(yesterday)`. A higher scaling multiplier than 0.5 makes VIDYA more responsive; the book also demonstrates indexing VIDYA off the r² of a rolling linear regression instead of CMO.

**Entry**
- **Long**: if today's close and yesterday's close are both above today's VIDYA, place a buy stop for tomorrow one tick above today's high.
- **Short** (mirror rule): if today's close and yesterday's close are both below today's VIDYA, place a sell stop for tomorrow one tick below today's low.

**Exit / reversal**
- No separate profit target or independent exit rule is used — the system is always in the market. A new signal in the opposite direction simultaneously closes the current position and opens the reverse position (stop-and-reverse).

**Backtest configuration used by the authors**
- Flat $1,500 initial stop per trade.
- $125 added to every loss and subtracted from every gain to approximate slippage and commissions.
- Continuous/perpetual futures contracts, tested over two five-year blocks (~1983–1988 and ~1988–1993).
- Design targets stated before testing: 30–45% win rate, payoff ratio (average winner ÷ average loser) above 2.50.

## Risk

Risk is controlled entirely by the flat $1,500 stop plus the stop-and-reverse structure (there is no flat, unstopped period). The authors report the first five-year Swiss franc test block hit their design targets: 33 trades, a 36% win rate, a 3.37 payoff ratio (3.18 excluding the single largest winner and loser), average losing trades cut off in 13 trading days, average winning trades held for 79 trading days, and an average per-trade profit above $700 (comfortably above the $175 modeled slippage/commission cost). No position-sizing formula (fixed-fractional, volatility-based, or otherwise) is specified — the $1,500 stop is a fixed dollar amount per contract, not a percentage of equity.

## Caveats

This system is reconstructed from a sampled OCR pass over a scanned book; the sampled pages contained the short (sell) side of the entry rule explicitly, and the long side has been mirrored here on the assumption of symmetry (consistent with how the rest of the book presents long/short rule pairs), but the exact long-side wording was not present in the sample and should be verified against the source before live use. Only the first five-year backtest block's results (33 trades, Swiss franc) were present in the sampled text; the book states a second five-year block (~1988–1993) and a wider set of markets were also tested, but those specific numbers were not recoverable from the OCR sample. The system is unoptimized by the authors' own description — it is presented as a reasonable baseline trend-follower rather than a tuned, market-specific system, and the $1,500/$ 125 dollar figures are 1990s futures-contract-scale assumptions that would need rescaling for other instruments or account sizes.