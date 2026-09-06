# Mechanical Trading Systems: Pairing Trader Psychology with Technical Analysis: the trader's summary

*Matches three trader personality types (trend-following, mean-reversion, short-term) to fully coded, backtested mechanical systems and the specific risk-management math each requires.*

**Richard L. Weissman** · 2005 · Trend Following & Mechanical Systems · intermediate

*Source coverage: partial. PDF pages inspected: 2, 6, 12, 34, 43, 48, 74-75 (system definitions and the backtest tables showing the 8.48% annualized return, 19.98% drawdown and their degradation). These are study notes, not verified trading results.*

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

1. **Two moving average crossover (trend-following, stop-and-reverse)**: long when a 9-period MA closes above a 26-period MA, short when it closes below. Backtested 1992–2002 on a 10-market futures/FX portfolio: 8.48% average annualized return on $200,000, 19.98% max drawdown, 61.18% losing trades, 10 consecutive losses.
2. **Three moving average crossover**: adds a 52-period MA, requiring 9 > 26 > 52 for longs (reverse for shorts) and allowing a neutral/flat state when misaligned — fewer, more selective signals than the two-MA version. Ichimoku variants of both (same periods, but requiring the longer MA to already slope in the crossover's direction) helped the three-MA version and hurt the two-MA version, showing filters don't generalize.
3. **Channel breakout (Donchian)**: long at the prior 20-day high, short at the prior 20-day low, stop-and-reverse; Weissman suggests adding a 1–5%-of-value stop or a 20%-of-prior-range confirmation filter since the base system has no volatility filter.
4. **Bollinger Band breakout (trend-following)**: long on a close above the upper band (20-day MA ± 2 SD), short below the lower band, exit at the 20-day MA. Backtested: 5.37% annualized return at only 14.16% max drawdown — roughly half the two-MA system's risk, for a superior P:MD despite lower total profit.
5. **RSI extremes with 200-day MA filter (intermediate-term, trend-following mean reversion)**: long when 9-day RSI closes below 35 and price is above its 200-day MA (mirror for shorts at 65/below); exit at 14-day RSI crossing back above 60 (longs) or below 40 (shorts), with a 2.5%-of-entry fail-safe stop. Backtested on a currency-cross portfolio: 2.27 P:MD, 54.57% winners.
6. **Bollinger Bands with 200-day MA filter (intermediate-term mean reversion)**: same band-fade entry as the breakout system but only with the 200-day trend, exiting at the 20-day MA or a 2.5% stop — higher win rate (68.26%) and much shorter holding period than RSI extremes.
7. **Bollinger Bands with ADX filter (nondirectional mean reversion)**: same band-fade entry, trend filter replaced by ADX below 20; exit at ±1.25–2.5% of entry. Consistently worse P:MD than the trend-filtered version.
8. **Seven-period reversal (short-term, nondirectional)**: sell after 6 consecutive higher closes followed by one lower close (mirror for buys); exit at a 1% profit target or 1% stop.
9. **RSI crossover (short-term, nondirectional)**: buy when 14-period RSI was below 25 two bars ago and crosses above 25 on the prior bar (mirror at 75 for shorts); fixed percentage target/stop, tightened from 3%/1% on 60-minute bars to 1%/1% on 30-minute bars as per-bar volatility shrinks.

Stop and target percentages must shrink as the bar interval shortens (a 2.5% stop that works on 60-minute bars turned into a loser at 30-minute bars until cut to 1.5%), and only a short list of assets (equity indices, T-bonds, major FX) stay liquid and volatile enough to trade profitably below the daily bar.

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

Caveats: all backtests use a single data vendor (CQG), a single decade (1992–2002 in-sample, 2003 out-of-sample), and a flat $75–100 per-round-turn slippage/commission assumption that may not hold for all instruments or eras; the book itself flags that fixed-percentage stops and fixed dollar amounts distort results on back-adjusted continuous futures data. Some systems shown (Ichimoku, DMI+ADX) are explicitly presented as underperforming, included for pedagogical contrast rather than as recommendations. The book predates decimalization-driven changes in FX/futures microstructure and high-frequency competition, so the specific short-term (5- and 15-minute bar) results are the most dated. Note for this library: a separate PDF in this collection titled "Mechanical Trading Systems.pdf" (slug [Mechanical Trading Systems](https://ninad-k.github.io/trading-playbook/books/mechanical-trading-systems.html)) is an identical copy of this same Weissman book (same page count, word count, and table of contents) — treat the two library entries as duplicates of one source rather than independent books.

## Who should read it

Best suited to traders who already have a candidate strategy or two and want a framework for (a) matching a system type to their own temperament, (b) building rigorous position-sizing and stop-loss rules around it, and (c) understanding why backtested optimization results should be distrusted. Less useful as a first introduction to technical indicators (Chapter 2's explanations are brief) or as a source of novel, unpublished trading edges — the systems shown are intentionally simple, publicly known building blocks.

## Related books in this library

- [Way of the Turtle](https://ninad-k.github.io/trading-playbook/books/curtis-faith-way-of-the-turtle.html) — a fully disclosed trend-following channel-breakout system with the position-sizing math this book only outlines in general terms.
- [Trend Following](https://ninad-k.github.io/trading-playbook/books/michael-covel-trend-following.html) — a deeper dive into the trend-following psychology and Market Wizard case studies this book references in passing.
- [What Is a Trading System?](https://ninad-k.github.io/trading-playbook/books/van-tharp-trading-systems.html) — directly cited in this book's risk-management chapter (the Tom Basso random-entry system anecdote); expands on position-sizing philosophy.
- [Bollinger on Bollinger Bands](https://ninad-k.github.io/trading-playbook/books/john-bollinger-bollinger-on-bollinger-band.html) — the primary source for the Bollinger Band mechanics used in several of this book's mean-reversion and trend-following systems.
- [Jack Schwager's Guide to Winning with Automated Trading Systems](https://ninad-k.github.io/trading-playbook/books/jack-schwager-guide-to-winning-with-automated-trading-systems-course-manual.html) — another systems-development and automated-trading course covering similar backtesting and system-design ground.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: mechanical-systems, trend-following, mean-reversion, risk-management, position-sizing, trader-psychology, backtesting, curve-fitting
