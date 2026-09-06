---
author: Richard L. Weissman
category: Trend Following & Mechanical Systems
difficulty: intermediate
doc_type: book
one_liner: Pairs trend-following, mean-reversion, and short-term mechanical systems
  with matching trader personality profiles, plus a full price-risk-management toolkit.
pages: 241
related:
- curtis-faith-way-of-the-turtle
- turtlerules
- john-bollinger-bollinger-on-bollinger-band
- come-into-my-trading-room-elder-alexander
reviewed_pdf_pages: 6, 12-14, 34, 43, 48, 99, 101 (position-sizing chapters, the moving-average
  and channel-breakout system definitions, and the portfolio risk tables)
slug: mechanical-trading-systems
source_file: Mechanical Trading Systems.pdf
source_review: partial
tags:
- mechanical-systems
- trend-following
- mean-reversion
- backtesting
- position-sizing
- trader-psychology
- moving-averages
- value-at-risk
tier: A
title: Mechanical Trading Systems
year: 2005
---

## Overview

Mechanical Trading Systems (subtitled "Pairing Trader Psychology with Technical Analysis," John Wiley & Sons, 2005) is a systematic survey of rule-based futures/FX trading systems, organized around the thesis that a system's suitability depends as much on matching the trader's psychological profile as on its backtested statistics. Weissman walks through the mathematics of common technical indicators, converts each into a complete stop-and-reverse trading system, backtests them on a ten-asset diversified portfolio (1993–2003, CQG data), and then devotes separate chapters to trend-following, mean-reversion, and short-term systems, followed by chapters on system development pitfalls, price risk management, diversification, discretion, and trading psychology. Note: this PDF ("Mechanical Trading Systems") is the same book being catalogued elsewhere in this library under the slug richard-l-weissman-mechanical-trading-systems — see Strengths and caveats.

## Core thesis

No single "best" trading system exists in the abstract. Trend-following, (intermediate-term) mean-reversion, and short-term systems each fit a different trader personality (patience and fortitude vs. contrarian discipline vs. quick-mindedness), and a technically superior system that doesn't match the trader's psychological makeup will be abandoned during its inevitable drawdown. Robust systems are simple (few parameters), diversified across uncorrelated asset classes and/or parameter sets, and always paired with strict price-risk management — because system development itself is comparatively easy, while surviving a system's drawdowns is the real challenge.

## Key concepts

- **Trend-following vs. mean-reversion indicators** — trend tools (moving averages, MACD, DMI, Donchian channel breakout) profit from sustained directional moves; mean-reversion tools (RSI, Stochastics, CCI, Bollinger Bands, moving-average envelopes) profit from price snapping back to an average.
- **Whipsaw** — a false trend-following signal that reverses immediately, addressed via whipsaw waiting periods, moving-average envelopes, or a confirming second indicator.
- **Stop-and-reverse (SAR) system** — always in the market, flipping directly from long to short (e.g., two-MA crossover, MACD, DMI, Parabolic).
- **Out-of-sample (walk-forward) study** — reserving 10–20% of data, ideally the most recent, to test a system after optimization; a postoptimization drawdown exceeding 15% of in-sample performance is Weissman's threshold for abandoning a system.
- **Profit spikes** — anomalously good single parameter sets surrounded by poor neighbors in an optimization grid; smoothed out by averaging with neighboring parameter sets to find robust "hilltops."
- **Martingale vs. anti-Martingale position sizing** — Martingale doubles size after a loss (ruinous: 11 straight losses on a $1,000 base destroys over $1M); anti-Martingale (e.g., fixed fractional) increases size as equity grows and shrinks it as equity falls.
- **Value at Risk (VaR)** — statistical estimate of maximum likely loss over a holding period at a confidence level (e.g., 95%); complemented by stress testing for tail/correlation-breakdown scenarios VaR misses.
- **Profit-to-max-drawdown (P:MD) ratio** — Weissman's preferred single metric for system robustness, alongside %W, average profit:loss ratio, max consecutive losses (MCL), and max drawdown duration (MDD).
- **Fixed fractional money management** — position size scales with current equity so that a target maximum drawdown percentage stays roughly constant as the account grows or shrinks.

## Rules and setups

Representative parameter sets given in the text (illustrative defaults, not the book's final optimized values):

| System | Parameters |
|---|---|
| Two-MA crossover | e.g., 9- and 26-period; long/flat-reverse on cross |
| Three-MA crossover | 9-, 26-, 52-period; neutral when misaligned |
| MACD | 13-period EMA minus 26-period EMA, 9-period signal line |
| DMI / ADX | 9-period smoothing; ADX > 20 = trending, < 20 = sideways |
| Donchian channel breakout | Buy/sell at n-period high/low (Donchian used 20 days) |
| Bollinger Bands (trend) | 20-period MA, 2 std dev; enter on close beyond a band |
| Moving-average envelope (mean reversion) | Fade a 2.5% envelope around a 21-day MA; exit at MA or 1% profit; fail-safe stop at 5% of entry or 2.5 std dev from a 20-day MA |
| RSI extremes (mean reversion) | 14-period RSI; enter beyond 35/65 (tighter than the classic 30/70), 200-day MA filter for regime |
| Stochastics | 9- or 14-day %K, 3-day smoothing for %K/%D |
| CCI | Entries at ±100 or ±200, exits at 0 or the opposite trigger, fail-safe stop ~2.5% |

General rules of thumb: fewer parameters are more robust than many; prefer end-of-day signal confirmation over intraday triggers to avoid false settles; avoid portfolios of highly correlated assets (e.g., all grains) which can make a losing system look profitable or vice versa; discard markets where commissions/slippage consume the edge (the book excludes CBOT corn and Nymex coal on this basis).

## Risk and money management

Per-trade risk: limit exposure to 1–2% of total account equity per position, sized from the stop-loss distance rather than margin/leverage. Account-level stop: since a 50% peak-to-valley drawdown needs a 100% gain (on half the capital) to recover, some hedge funds set a fund-wide stop around 37.5% drawdown from the last equity peak; a 1% per-trade risk level needs 47 consecutive losses to hit that threshold, versus only 12 at a 4% per-trade risk level. Sizing must also account for correlation: a position correlated to an existing one can exceed the effective 1–2% limit even if it looks acceptable stand-alone. Two "schools" are presented: the trader school (stop-loss + Martingale/anti-Martingale volumetric sizing) and the quant school (VaR + stress testing) — Weissman argues both are needed, since VaR only bounds the "likely" loss, says nothing about severity beyond the confidence threshold, and assumes serial independence that trending/mean-reverting markets violate.

## Psychology and discipline

Weissman assigns each system family a personality profile: trend-following requires patience and fortitude (tolerating long strings of losses — potentially 7+ consecutive — for a low %W, high avg-win/avg-loss payoff structure); intermediate-term mean reversion requires patience for a different reason (frequent smaller wins, occasional large adverse trend moves); short-term/day trading requires "quick-mindedness." A recurring theme is that mechanical systems do not remove psychology from trading — they relocate it to the discipline required to follow the system through drawdowns exactly as designed, and traders who pick a system mismatched to their own risk tolerance will deviate from it at the worst possible time.

## Chapter map

- Ch 1 — Dispelling Myths and Defining Terms — market efficiency debate, technical analysis definition, trend-following vs. mean-reversion indicator families.
- Ch 2 — Mathematical Technical Analysis — builds each indicator (MAs, MACD, DMI/ADX, Parabolic, Donchian, Stochastics, RSI, CCI, Bollinger Bands) into a tradable system.
- Ch 3 — Trend-Following Systems — backtested comparisons, portfolio construction, data-integrity issues (contract rollover, point vs. percentage changes), general rules of thumb.
- Ch 4 — Mean Reversion Systems — trend-following mean reversion vs. nondirectionally biased variants, intermediate-term application.
- Ch 5 — Short-Term Systems — 2-hour down to 5-minute bar mean-reversion variants, RSI-extreme filters at multiple bar sizes.
- Ch 6 — Knowing Oneself — matching time frame/system to personality.
- Ch 7 — System Development and Analysis — optimization pitfalls, profit spikes, out-of-sample testing, performance-metric definitions.
- Ch 8 — Price Risk Management — stop-loss vs. VaR schools, Martingale/anti-Martingale, stress testing, drawdown psychology.
- Ch 9 — Improving the Rate of Return — diversification of assets and of parameter sets.
- Ch 10 — Discretion and Systems Trading — where discretionary judgment can legitimately override a mechanical system (paradigm shifts, volatility shocks).
- Ch 11 — Psychology of Mechanical Trading — discipline, flexibility, and the "transformational" framing of systematic trading.

## Strengths and caveats

**Duplicate-coverage note**: this document ("Mechanical Trading Systems") is Richard L. Weissman's book of the same title; the library's slug list also includes richard-l-weissman-mechanical-trading-systems, which another agent may be cataloguing as a separate PDF of the same text under a different filename. The content overlaps substantially or completely — treat the two pages as covering one book, and prefer whichever page is more complete if both exist.

Strengths: unusually rigorous about backtesting methodology (rollover artifacts, in-sample vs. out-of-sample discipline, correlation-aware portfolio construction) versus most retail trading books, and honest that trend-following can lose money most of the time while staying profitable overall. Caveats: backtests use 1993–2003 futures/FX data on a fixed ten-asset portfolio with $100 round-turn costs that may not hold in modern electronic markets; the book states no parameter set is durably "optimal" (its own tables show different best parameters in-sample vs. out-of-sample), so treat the settings as illustrative, not prescriptive; some claims (typical professional win rates, specific hedge-fund drawdown practices) are asserted from experience rather than cited studies.

## Who should read it

Best for traders building or evaluating rule-based trend-following or mean-reversion systems in futures, FX, or similarly liquid, trending markets, and for anyone wanting a rigorous framework for backtesting discipline (out-of-sample testing, drawdown-based position sizing) rather than specific indicator settings to copy directly. Less suited to discretionary equity swing traders or those seeking a single "the" system to trade unmodified.

## Related books in this library

- [[curtis-faith-way-of-the-turtle]] — a concrete historical case study of the trend-following, drawdown-tolerant trader personality Weissman describes abstractly.
- [[turtlerules]] — the original Donchian-channel-style breakout rules that Weissman's channel-breakout system generalizes.
- [[john-bollinger-bollinger-on-bollinger-band]] — deeper treatment of the Bollinger Band mechanics used in both the trend and mean-reversion systems here.
- [[come-into-my-trading-room-elder-alexander]] — a discretionary counterpoint on risk management (2% rule, psychology) that pairs with Weissman's stop-loss/VaR framework.
