---
title: Trend Following
author: Michael Covel
year: 2004
slug: michael-covel-trend-following
tier: A
category: Trend Following & Mechanical Systems
tags: [trend-following, managed-futures, risk-management, discipline, drawdowns, mechanical-systems, performance-data]
difficulty: intermediate
doc_type: book
pages: 344
one_liner: "Profiles of top CTAs plus the shared rulebook of trend followers: cut losses fast, let winners run, risk a fixed % per trade, ignore forecasts."
related: [curtis-faith-way-of-the-turtle, the-complete-turtletrader-the-legend-the-lessons-the-results, trading-in-the-zone, jack-schwager-stock-market-wizards, turtlerules]
source_file: "Michael Covel - Trend Following.pdf"
---

## Overview

Covel's book is a survey of professional trend-following traders (Bill Dunn, John W. Henry, Ed Seykota, Keith Campbell, Jerry Parker, Richard Dennis, Richard Donchian, Salem Abraham) built around their published performance data, their own words, and a handful of "big event" case studies (1987 crash, LTCM, Barings, Metallgesellschaft, the dot-com bust). Rather than teaching one indicator set, it argues that a small family of shared principles — trade price only, cut losses fast, let winners run, size positions by a fixed percentage of equity, diversify across uncorrelated markets — explains decades of outsized, largely uncorrelated returns across very different traders and eras.

## Core thesis

Markets cannot be reliably forecast; the only tradable, persistent signal is price itself. A trend follower does not predict where a market is going — she waits for a trend to reveal itself, gets aboard once price confirms it, and exits when price says the trend has ended. Profits come from capturing the "meat" of large, unpredictable moves (never the exact bottom or top), while losses are deliberately kept small and frequent. Because winners are rare (historically only 30–40% of trades are profitable for the featured firms) but large, and losers are common but small and capped, the resulting positive mathematical expectation — not forecasting skill — is what produces decades of compounding.

## Key concepts

- **Trend Following** — trading strategy that waits for price to establish a directional move, then follows it until price signals the move is over; makes no attempt to predict beginnings or ends.
- **Modus operandi: follow price** — decisions are driven by price action alone, not fundamentals, news, or forecasts.
- **Positive mathematical expectation** — the average dollar gain/loss per trade across many trades; trend followers accept a low win rate (30–40%) because winners are disproportionately larger than losers.
- **Heat / core equity (Ed Seykota)** — the percentage of account equity placed at risk across all open positions simultaneously; a portfolio risking 2% on each of five positions has 10% total heat.
- **Whipsaw** — a quick, unprofitable in-and-out trade generated when price triggers an entry and then immediately reverses into the exit; accepted as an unavoidable cost of staying mechanical.
- **Curve-fitting / robustness** — a system whose performance collapses when a parameter is nudged slightly (e.g., works at 20 but not 19 or 21) is overfit; a robust system performs similarly across a range of parameter values.
- **Reversal system** — a portfolio approach (e.g., Bill Dunn's) that is always in the market, long or short, in every instrument traded, rather than sitting in cash between trades.
- **Five questions for a trading system** — what to buy/sell, how much to buy/sell, when to enter, when to exit a loser, when to exit a winner; Covel treats a complete answer to these five as the definition of a trading system.
- **Zero-sum framing** — for every trend-follower profit in futures, a counterparty loses the equivalent amount; the book frames famous blow-ups (Barings, LTCM, MG) as money trend followers won on the other side of.
- **Managed futures / CTA** — a Commodity Trading Advisor manages client capital using futures markets; Covel argues CTA returns have historically shown low-to-zero correlation with stocks and bonds (Modern Portfolio Theory rationale for allocating to trend following).

## Rules and setups

Covel documents no single house system; instead he extracts recurring, quantified statements made by the traders profiled. Treat these as a shared rulebook, not one method:

1. **Entry** — enter only after price confirms a breakout from a range or an established trend (e.g., Microsoft basing 50–55 then breaking to 63 triggers entry); no attempt is made to buy the exact bottom.
2. **Exit on losers** — predefine the stop before entering; when it is hit, exit immediately without debate. Example given: enter with a 2% stop loss — lose 2%, exit, "don't debate it."
3. **Exit on winners** — no fixed profit targets; ride the trend using a trailing exit (e.g., a rolling N-day price breakdown) until price itself signals reversal. Profit targets are explicitly rejected as capping the rare large winners that pay for many small losers.
4. **Position sizing** — risk a small, fixed percentage of current equity per trade; cited figures across traders range from 1% to 5–6% (Craig Pauley: most trend followers risk 1–5% per trade; Dunn Capital: 2–6% depending on market; Seykota's "heat" concept: sum of per-position risk should stay near 10% of equity for a diversified book).
5. **Recompute off current equity, not starting equity** — after a drawdown, size new trades off the reduced equity (Bill Dunn's rule), not the original account balance.
6. **Diversification across uncorrelated markets** — trade a broad portfolio (currencies, rates, stock indices, energies, metals, softs) because no one knows in advance which market will produce the big trend; Dunn's World Monetary Assets portfolio spans ~15 futures markets across five sectors.
7. **Add to winners, not to losers** — Richard Dennis: after a position shows a profit ("a strong day's work"), it is reasonable to add to it; do not wait for a retracement that may never come.
8. **Robustness check** — a system's parameters should work across a range of values; if performance is only good at one exact setting, discard it as curve-fit.
9. **No discretion under fire** — entry, exit, and sizing rules must be fully predefined before the trading day so no judgment calls are made "in the heat of battle."

The book gives one fully specified illustrative system (Bob Spear's Trading Recipes example: 89-day breakout entry / 13-day breakdown exit, 2% equity risk) — see the linked system page for its exact rules; Covel is explicit that this is shown to illustrate mechanics, not as a recommendation.

## Risk and money management

- Programmed risk targets are stated in probabilistic terms, e.g., Bill Dunn's system carries "a 1% probability of a monthly loss of 20% or more."
- Per-trade risk cited across traders: 1–2% is typical/conservative; some go to 5–6% on a single trade; Seykota's "heat" caps aggregate open risk (e.g., 2% × 5 positions = 10% heat).
- Drawdowns are large and expected: Dunn had losing years of 27.1% (1976); LTCM lost 41% of capital (~$1.9B) in August 1998 before its unwind. The book treats deep, prolonged drawdowns as the entry price for the strategy's long-run edge, not evidence it is broken.
- Correlation across the featured CTAs' returns is used as the case for allocating trend following alongside a traditional 60/40 stock/bond portfolio (Modern Portfolio Theory rationale, Appendix D): a hypothetical 10% allocation to a trend-following program (Millburn, cited 1977–2003) raised traditional-portfolio return by ~73bp and cut return volatility by ~0.26 percentage points.
- No stated universal % figure is endorsed by the author as "correct" — the book reports what named traders say they use, and leaves sizing as a per-trader choice bounded by the 1–6% range above.

## Psychology and discipline

Three of the book's four parts are devoted to why trend following is psychologically hard rather than technically hard. Prospect theory and the "disposition effect" (investors sell winners early and hold losers hoping for a rebound) are presented as the exact opposite of the trend-following rulebook (cut losers fast, let winners run) — meaning the strategy's edge partly exists because most investors are constitutionally unable to follow it. Discipline is framed as building all discretionary judgment into rules in advance so none is needed mid-trade; Ed Seykota and Charles Faulkner's "personal inventory" questions (what do you want, how much risk can you tolerate, how disciplined are you) are recommended before a trader writes a single rule. The book repeatedly stresses accepting whipsaws and long strings of small losses as the unavoidable cost of being positioned for trends nobody can predict in advance.

## Chapter map

- Ch 1 — Trend Following — defines the strategy, its price-only philosophy, and why it presupposes constant market change.
- Ch 2 — Great Trend Followers — trader-by-trader profiles and performance data (Dunn, Henry, Seykota, Campbell, Parker, Abraham, Dennis, Donchian, Livermore).
- Ch 3 — Performance Data — absolute returns, drawdowns, correlation, and the zero-sum nature of futures trading.
- Ch 4 — Big Events in Trend Following — five case studies (1987 crash, LTCM, Asian contagion/Niederhoffer, Barings, Metallgesellschaft) framed as money trend followers won on the other side of.
- Ch 5 — Baseball: Thinking Outside the Batter's Box — Moneyball/statistical decision-making as an analogy for systematic trading (via John W. Henry's Red Sox ownership).
- Ch 6 — Human Behavior — prospect theory, emotional intelligence, the disposition effect, Ed Seykota's Trading Tribe.
- Ch 7 — Decision-Making — Occam's razor, fast-and-frugal heuristics, process vs. outcome thinking.
- Ch 8 — Science of Trading — critical thinking, chaos theory, compounding.
- Ch 9 — Holy Grails — critiques buy-and-hold, "losers average losers," and analysis paralysis.
- Ch 10 — Trading Systems — the five questions for a trading system; entry, exit, and sizing logic; FAQs on capital, stocks, and curve-fitting.
- Ch 11 — Conclusion — why trend following is slowly accepted, leverage vs. return, closing arguments.
- Appendices — A: personality traits of successful traders; B: trend-following payoff models; C: a fully specified illustrative system (see system page); D: Modern Portfolio Theory and managed futures; E: critical questions for evaluating a trading system.

## Strengths and caveats

- Performance tables are largely hypothetical/composite ("$1,000 growth" indices) built from manager-reported data through the early 2000s; results are not independently audited in the text and management-fee/survivorship effects are not addressed in depth.
- The one fully worked system (Appendix C) is explicitly presented as illustrative only, using in-sample data (1991–2000) with no out-of-sample validation and no commissions/slippage — the author flags this himself.
- Heavy reliance on quotations from practitioners means the "rules" are anecdotal and inconsistent in specifics (per-trade risk figures range from 1% to 6% depending on who is quoted) rather than a single codified method.
- Strongly polemical against discretionary/fundamental trading and buy-and-hold; contrarian claims (e.g., trend followers profiting from Barings and LTCM) are asserted rather than derived from primary trade data.
- Content is timeless in intent but market examples (dot-com bust, LTCM, early-2000s manager AUM) date the book to its 2004 publication.

## Who should read it

Traders and allocators who want the historical and psychological case for systematic, price-based trend following across futures markets — useful as a "why" companion to more mechanical rule-books like the Turtle system, rather than a standalone how-to.

## Related books in this library

- [[curtis-faith-way-of-the-turtle]] — a fully codified breakout/ATR-sizing trend system in the same tradition Covel describes only anecdotally.
- [[the-complete-turtletrader-the-legend-the-lessons-the-results]] — deeper history of Richard Dennis's Turtles, one of the trader lineages profiled here.
- [[trading-in-the-zone]] — expands on the psychology (discipline, probabilistic thinking) Covel treats in Parts III–IV.
- [[jack-schwager-stock-market-wizards]] — same interview-driven format applied to a broader set of traders, several discretionary.
- [[turtlerules]] — a concrete rule set comparable to Covel's illustrative Appendix C system.
