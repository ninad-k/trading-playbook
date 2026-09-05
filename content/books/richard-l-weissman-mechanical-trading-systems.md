---
title: "Mechanical Trading Systems: Pairing Trader Psychology with Technical Analysis"
author: Richard L. Weissman
year: 2005
slug: richard-l-weissman-mechanical-trading-systems
tier: A
category: Trend Following & Mechanical Systems
tags: [mechanical-systems, trend-following, mean-reversion, risk-management, position-sizing, trader-psychology, backtesting, curve-fitting]
difficulty: intermediate
doc_type: book
pages: 241
one_liner: "Matches three trader personality types (trend-following, mean-reversion, short-term) to fully coded, backtested mechanical systems and the specific risk-management math each requires."
related: [curtis-faith-way-of-the-turtle, michael-covel-trend-following, van-tharp-trading-systems, john-bollinger-bollinger-on-bollinger-band, jack-schwager-guide-to-winning-with-automated-trading-systems-course-manual]
source_file: "RICHARD L. WEISSMAN - Mechanical Trading Systems.pdf"
---

## Overview

Weissman's central argument is that the hard part of mechanical trading is not discovering a profitable system but finding one that matches the trader's psychological temperament closely enough that they can actually execute its signals through losing streaks. The book is organized around three trader archetypes — long/intermediate-term trend followers, intermediate-term mean-reversion traders, and short-term (swing/day) traders — and for each one it supplies fully specified, CQG-code-level trading systems, ten years of backtested portfolio results (1992–2002, plus a 2003 out-of-sample year), and a matching psychological profile. Later chapters cover system-development pitfalls (curve fitting, optimization), price-risk management (stop-loss sizing, Martingale/anti-Martingale position sizing, value at risk, stress testing), diversification, discretion within a mechanical framework, and the psychology of adhering to a system.

## Core thesis

Markets are inefficient because participants act on emotion rather than rational calculation; this produces "leptokurtic" price distributions in which prices spend roughly 70 percent of the time mean-reverting and the rest of the time trending with amplified tails. Trend-following systems profit from the tails (a low win rate offset by large winners); mean-reversion systems profit from the 70 percent (a high win rate with smaller, capped gains). Because both approaches work through mechanisms that feel psychologically unnatural — buying recent highs, fading a crowd, sitting through many small losses — the primary determinant of trading success is not system discovery but disciplined execution matched to trader personality, reinforced by rigorous price-risk management.

## Key concepts

- **Mathematical vs. interpretive technical analysis** — objective, rule-based indicators (moving averages, RSI) versus subjective chart patterns (head-and-shoulders, triangles); only the former can be coded into a mechanical system.
- **Trend-following vs. mean-reversion indicators** — moving averages, MACD, DMI, channel breakout, and parabolic SAR profit from trends; RSI, stochastics, Bollinger Bands, and CCI profit from reversion to the mean, though any of them can be "faded" to work the other way.
- **Leptokurtic distribution** — Weissman's statistical framing for why markets spend most of their time range-bound (around 70 percent) but generate outsized trending moves the rest of the time.
- **Whipsaw filters** — techniques (time-driven waiting periods, percentage penetration envelopes, secondary indicator confirmation) added to trend-following triggers to reduce false breakout signals, always trading faster response against more whipsaws.
- **Profit-to-maximum-drawdown (P:MD)** — Weissman's preferred single metric for comparing systems, since total net profit alone says nothing about the risk taken to earn it.
- **Cutting the tails of a system's distribution** — deliberately capping losses (stop-loss filters) while explicitly arguing against capping profits on trend-following trades, since a small fraction of trades produce most of the profit.
- **Fixed fractional position sizing** — an anti-Martingale approach that scales the number of contracts traded up or down in proportion to current equity, keeping worst-case drawdown as a constant percentage of capital.
- **Value at risk (VaR) and stress testing** — VaR quantifies the probability of losing more than $X over a given horizon using historical volatility and correlation; stress testing complements it by modeling severity (price shocks, correlation breakdowns) that VaR's normal-market assumptions ignore.
- **Curve fitting / optimization risk** — parameter sets that look best over an in-sample period frequently rank worst (or even flip from profitable to losing) in the following out-of-sample year.
- **Mechanical discretion** — using objectively quantifiable factors (volatility regime shifts, drawdown severity) to scale position size up or down within an otherwise mechanical framework, as distinct from fully subjective ("true") discretion.

## Rules and setups

Weissman gives complete, codeable systems (shown here with CQG-style logic) for each trader type:

1. **Two moving average crossover (trend-following, stop-and-reverse)**: go long when a 9-period simple moving average closes above a 26-period MA; go short (reverse) when it closes below. Backtested 1992–2002 across a 10-market futures/FX portfolio: 8.48% average annualized return on $200,000, 19.98% max drawdown, 61.18% losing trades, 10 consecutive losses.
2. **Three moving average crossover**: adds a 52-period MA; requires 9 > 26 > 52 (in that order) for longs, the reverse for shorts, and allows a neutral/flat state when the averages are not aligned — trading fewer, more selective signals than the two-MA version.
3. **Ichimoku variants**: same 9/26 (or 9/26/52) periods, but require the longer MA(s) to already be sloping in the crossover's direction before entry — a built-in whipsaw filter that helped in the three-MA version but hurt in the two-MA version, illustrating that filters cannot be generalized from one test.
4. **Channel breakout (Donchian)**: go long at the prior 20-day high, short at the prior 20-day low, stop-and-reverse; no volatility filter is built in, so Weissman suggests adding a 1–5% of asset value stop-loss or a 20%-of-prior-range breakout-confirmation filter.
5. **Bollinger Band breakout (trend-following)**: enter long when price closes above the upper band (20-day MA ± 2 standard deviations), short below the lower band; exit at the 20-day MA. Backtested: 5.37% annualized return, only a 14.16% max drawdown (roughly half the two-MA system's), for a superior P:MD despite lower total profit.
6. **RSI extremes with 200-day moving average filter (intermediate-term, trend-following mean reversion)**: go long when 9-day RSI closes below 35 and price is above its 200-day MA (short when RSI closes above 65 and price is below the 200-day MA); exit with profit when 14-day RSI crosses back above 60 (longs) or below 40 (shorts); fail-safe stop at 2.5% of entry value. Backtested on a currency-cross-heavy portfolio: 100,188 total profit, 2.27 P:MD, 54.57% winners.
7. **Bollinger Bands with 200-day MA filter (intermediate-term mean reversion)**: fade a close beyond the Bollinger Band only in the direction of the 200-day MA trend; exit at the 20-day MA or a 2.5% fail-safe stop. Produced a higher win rate (68.26%) and much shorter average holding period than RSI extremes on the same portfolio.
8. **Bollinger Bands with ADX filter (nondirectional mean reversion)**: same band-fade entry, but replace the trend filter with ADX below 20 (a non-trending-market signal); exit at ±1.25–2.5% of entry value. Removing the trend-following bias consistently produced worse P:MD than the trend-filtered version.
9. **Seven-period reversal (short-term, nondirectional)**: sell after 6 consecutive higher closes followed by one lower close (mirror for buys); exit at a 1% profit target or 1% stop-loss.
10. **RSI crossover (short-term, nondirectional)**: buy when 14-period RSI was below 25 two bars ago and crosses above 25 on the prior bar (mirror for shorts at 75); exit at a fixed percentage profit target and stop (tightened from 3%/1% on 60-minute bars down to 1%/1% on 30-minute bars as volatility per bar shrinks).

Across all systems, Weissman stresses that stop-loss and profit-exit percentages must shrink as the bar interval shortens (a 2.5% stop appropriate for 60-minute bars produced an outright loser at 30-minute bars until reduced to 1.5%), and that only a short list of asset classes (equity indices, T-bonds, and major FX pairs) retain enough liquidity and volatility to trade profitably below the daily bar.

## Risk and money management

Weissman treats price-risk management as the one part of trading fully within the trader's control. Concrete rules given: risk 1–2% of total account equity per position (a 1% per-trade stop survives roughly 47 consecutive losses before hitting a 37.5% account-level drawdown stop, versus only 12 at 4% per trade); set a fund/account-level stop-loss around 37.5% of peak equity, since a 50% drawdown requires a 100% gain — on half the original capital — to recover, and a 15% drawdown still requires a 17.6% gain. Volumetric (position-sizing) risk is split into Martingale strategies (doubling size after a loss, including "averaging down" — rejected as a near-certain path to ruin) and anti-Martingale strategies (fixed fractional sizing, which scales contracts traded up or down with current equity to hold worst-case drawdown at a constant percentage). Value at risk and stress testing are presented as portfolio-level complements to per-trade stops, with VaR's key weaknesses spelled out: it assumes serial independence (ignoring trend-driven loss clustering, as in the 1995 peso crisis's nine days beyond 20 standard deviations), assumes liquidity that vanishes exactly when needed (October 1987), and assumes historical correlations hold through the price shocks that break them (the 1992 ERM crisis).

## Psychology and discipline

Each trader archetype gets a dedicated psychological profile. Trend followers must be willing to buy recent highs and sell recent lows, give back a significant share of unrealized gains without trying to "call the top" (the "psychic trader syndrome"), tolerate many consecutive small losses, and accept that 1–5% of trades will generate most of the profit — meaning no skipped signals and no vacations from the system. Mean-reversion traders need the discipline to fade crowd psychology and media narratives, the willingness to exit losers immediately when the market keeps trending against a "temporarily unsustainable" extreme, and unusual patience (roughly 30 trades a year, flat 91% of the time in one example). Short-term/day traders benefit most from mechanical systems precisely because manual, discretionary decision-making at high frequency causes burnout; a system converts constant judgment calls into fixed rules. A recurring theme is the "breakeven syndrome" (abandoning risk discipline to chase back to even) and "sideline regret" (chasing a missed trade into its blowoff phase) — both framed as predictable failure modes that mechanical systems, backtesting, and trade journaling are meant to counteract.

## Chapter map

- Ch 1 — Dispelling myths, defining mechanical trading systems, the psychology of price and indicator triggers, trend-following vs. mean-reversion indicator types.
- Ch 2 — Mathematical technical indicators as building blocks: moving average variants, whipsaw filters, MACD, DMI/ADX, parabolic SAR, Donchian channel breakout, stochastics, RSI, momentum/ROC, Bollinger Bands, CCI.
- Ch 3 — Trend-following systems: portfolio construction and data-integrity issues, backtested comparisons of the systems above, trending vs. mean-reverting asset classes, cutting losses vs. cutting profits, psychological profile of a trend trader.
- Ch 4 — Mean-reversion systems: trend-following and nondirectional mean-reversion systems, stop-loss design for backtesting, psychological profile of an intermediate-term mean-reversion trader.
- Ch 5 — Short-term systems: liquidity/volatility screening for day trading, swing trading with 2-hour bars down to 5-minute bars, psychological profile of a short-term trader.
- Ch 6 — Trader psychology across time frames; matching personality traits to trading system type.
- Ch 7 — System development: benefits and pitfalls of mechanical systems, curve fitting and optimization (in-sample vs. out-of-sample parameter reversal), system philosophy statements, performance measurement.
- Ch 8 — Price risk management: stop-loss sizing, Martingale/anti-Martingale volumetric sizing, value at risk, stress testing, psychology of risk management and drawdowns.
- Ch 9 — Improving rate of return via three types of diversification: asset class, parameter set, and system type (trend-following plus mean-reversion combined).
- Ch 10 — Discretion within a mechanical framework: paradigm shifts, volatility-driven position sizing, pros and cons of "true" discretion.
- Ch 11 — Psychology of mechanical trading: discipline and flexibility, single-mindedness, intuition vs. the "psychic trader syndrome," trading as a transformational practice.

## Strengths and caveats

The book's strength is giving away complete, reproducible system logic (entry, exit, filter, stop) alongside 10-year backtested performance tables rather than vague indicator descriptions — a reader can code every system shown directly from the text. The explicit in-sample/out-of-sample optimization comparison (Chapter 7) is an unusually honest demonstration of curve-fitting risk, showing a top-ranked parameter set becoming the worst performer the following year. The pairing of each system type with a specific, named psychological failure mode (breakeven syndrome, psychic trader syndrome, sideline regret) is more concrete than most trading-psychology treatments.

Caveats: all backtests use a single data vendor (CQG), a single decade (1992–2002 in-sample, 2003 out-of-sample), and a flat $75–100 per-round-turn slippage/commission assumption that may not hold for all instruments or eras; the book itself flags that fixed-percentage stops and fixed dollar amounts distort results on back-adjusted continuous futures data. Some systems shown (Ichimoku, DMI+ADX) are explicitly presented as underperforming, included for pedagogical contrast rather than as recommendations. The book predates decimalization-driven changes in FX/futures microstructure and high-frequency competition, so the specific short-term (5- and 15-minute bar) results are the most dated. Note for this library: a separate PDF in this collection titled "Mechanical Trading Systems.pdf" (slug [[mechanical-trading-systems]]) is an identical copy of this same Weissman book (same page count, word count, and table of contents) — treat the two library entries as duplicates of one source rather than independent books.

## Who should read it

Best suited to traders who already have a candidate strategy or two and want a framework for (a) matching a system type to their own temperament, (b) building rigorous position-sizing and stop-loss rules around it, and (c) understanding why backtested optimization results should be distrusted. Less useful as a first introduction to technical indicators (Chapter 2's explanations are brief) or as a source of novel, unpublished trading edges — the systems shown are intentionally simple, publicly known building blocks.

## Related books in this library

- [[curtis-faith-way-of-the-turtle]] — a fully disclosed trend-following channel-breakout system with the position-sizing math this book only outlines in general terms.
- [[michael-covel-trend-following]] — a deeper dive into the trend-following psychology and Market Wizard case studies this book references in passing.
- [[van-tharp-trading-systems]] — directly cited in this book's risk-management chapter (the Tom Basso random-entry system anecdote); expands on position-sizing philosophy.
- [[john-bollinger-bollinger-on-bollinger-band]] — the primary source for the Bollinger Band mechanics used in several of this book's mean-reversion and trend-following systems.
- [[jack-schwager-guide-to-winning-with-automated-trading-systems-course-manual]] — another systems-development and automated-trading course covering similar backtesting and system-design ground.
