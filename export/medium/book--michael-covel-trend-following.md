# Trend Following: the trader's summary

*Profiles of top CTAs plus the shared rulebook of trend followers: cut losses fast, let winners run, risk a fixed % per trade, ignore forecasts.*

**Michael Covel** · 2004 · Trend Following & Mechanical Systems · intermediate

*Source coverage: partial. PDF pages inspected: 7, 20-21, 29-30, 33, 36, 44, 51, 63, 78 (the entry/exit philosophy chapters, the heat and robustness discussions and the trader profiles). These are study notes, not verified trading results.*

## Overview

Covel's book surveys professional trend-following traders (Bill Dunn, John W. Henry, Ed Seykota, Keith Campbell, Jerry Parker, Richard Dennis, Richard Donchian, Salem Abraham) using their published performance data, their own words, and "big event" case studies (1987 crash, LTCM, Barings, Metallgesellschaft, the dot-com bust). Rather than teaching one indicator set, it argues a small family of shared principles — trade price only, cut losses fast, let winners run, size positions by a fixed % of equity, diversify across uncorrelated markets — explains decades of outsized, largely uncorrelated returns across very different traders and eras.

## Core thesis

Markets cannot be reliably forecast; the only tradable, persistent signal is price itself. A trend follower does not predict direction — she waits for a trend to reveal itself, gets aboard once price confirms it, and exits when price says the trend has ended. Profits come from capturing the "meat" of large, unpredictable moves (never the exact bottom or top), while losses are kept small and frequent. Because winners are rare (only 30–40% of trades are profitable for the featured firms) but large, and losers are common but small and capped, positive mathematical expectation — not forecasting skill — produces decades of compounding.

## Key concepts

- **Trend Following** — waits for price to establish a directional move, then follows it until price signals the move is over; no attempt to predict beginnings or ends.
- **Modus operandi: follow price** — decisions are driven by price action alone, not fundamentals, news, or forecasts.
- **Positive mathematical expectation** — average dollar gain/loss per trade across many trades; trend followers accept a low win rate (30–40%) because winners are disproportionately larger than losers.
- **Heat / core equity (Ed Seykota)** — % of account equity at risk across all open positions simultaneously; a portfolio risking 2% on each of five positions has 10% total heat.
- **Whipsaw** — a quick, unprofitable in-and-out trade where price triggers an entry then immediately reverses into the exit; an unavoidable cost of staying mechanical.
- **Curve-fitting / robustness** — a system whose performance collapses when a parameter is nudged slightly (works at 20 but not 19 or 21) is overfit; a robust system performs similarly across a range of values.
- **Reversal system** — a portfolio (e.g., Dunn's) always in the market, long or short, in every instrument traded, rather than sitting in cash.
- **Five questions for a trading system** — what to buy/sell, how much, when to enter, when to exit a loser, when to exit a winner; a complete answer to these five defines a trading system.
- **Zero-sum framing** — for every trend-follower profit in futures, a counterparty loses the equivalent; famous blow-ups (Barings, LTCM, MG) are framed as money trend followers won.
- **Managed futures / CTA** — a Commodity Trading Advisor manages client capital in futures markets; CTA returns have historically shown low-to-zero correlation with stocks and bonds (the MPT case for allocating to trend following).

## Rules and setups

Covel documents no single house system; he extracts recurring, quantified statements from the traders profiled. Treat these as a shared rulebook, not one method:

1. **Entry** — enter only after price confirms a breakout from a range or trend (e.g., Microsoft basing 50–55 then breaking to 63); never try to buy the exact bottom.
2. **Exit on losers** — predefine the stop before entering; when hit, exit immediately without debate (e.g., a 2% stop loss — lose 2%, exit, "don't debate it").
3. **Exit on winners** — no fixed profit targets; ride the trend with a trailing exit (e.g., a rolling N-day price breakdown) until price itself signals reversal. Targets are rejected as capping the rare large winners that pay for many small losers.
4. **Position sizing** — risk a small, fixed % of current equity per trade; cited figures range 1% to 5–6% (Pauley: most risk 1–5%; Dunn: 2–6% depending on market; Seykota's "heat": aggregate open risk near 10% of equity for a diversified book).
5. **Recompute off current equity, not starting equity** — after a drawdown, size new trades off the reduced equity (Dunn's rule), not the original balance.
6. **Diversify across uncorrelated markets** — trade a broad portfolio (rates, currencies, indices, energies, metals, softs) since no one knows which market will trend big; Dunn's World Monetary Assets portfolio spans ~15 markets across five sectors.
7. **Add to winners, not losers** — Dennis: after a position shows profit ("a strong day's work"), add to it; don't wait for a retracement that may never come.
8. **Robustness check** — parameters should work across a range of values; if performance only holds at one exact setting, discard it as curve-fit.
9. **No discretion under fire** — entry, exit, and sizing rules must be fully predefined so no judgment calls happen mid-battle.

The book gives one fully specified illustrative system (Bob Spear's Trading Recipes example: 89-day breakout entry / 13-day breakdown exit, 2% equity risk) — see the linked system page; Covel is explicit it illustrates mechanics, not a recommendation.

## Risk and money management

- Programmed risk targets are stated probabilistically, e.g., Bill Dunn's system carries "a 1% probability of a monthly loss of 20% or more."
- Per-trade risk cited: 1–2% is typical/conservative; some traders go to 5–6% on a single trade; Seykota's "heat" caps aggregate open risk (e.g., 2% × 5 positions = 10% heat).
- Drawdowns are large and expected: Dunn had a losing year of 27.1% (1976); LTCM lost 41% of capital (~$1.9B) in August 1998 before its unwind. Deep, prolonged drawdowns are treated as the entry price for the strategy's edge, not evidence it is broken.
- Correlation across the featured CTAs' returns is the case for allocating trend following alongside a 60/40 stock/bond portfolio (Modern Portfolio Theory, Appendix D): a hypothetical 10% allocation to a trend program (Millburn, 1977–2003) raised traditional-portfolio return by ~73bp and cut volatility by ~0.26 points.
- No universal % figure is endorsed as "correct" — the book reports what named traders use, leaving sizing a per-trader choice within the 1–6% range above.

## Psychology and discipline

Three of the book's four parts explain why trend following is psychologically hard rather than technically hard. Prospect theory and the "disposition effect" (investors sell winners early, hold losers hoping for a rebound) are presented as the exact opposite of the trend-following rulebook — meaning the edge partly exists because most investors are constitutionally unable to follow it. Discipline means building all discretionary judgment into rules in advance so none is needed mid-trade; Seykota and Charles Faulkner's "personal inventory" questions (what do you want, how much risk can you tolerate) are recommended before writing a single rule. The book stresses accepting whipsaws and strings of small losses as the unavoidable cost of being positioned for trends nobody can predict in advance.

## Chapter map

- Ch 1 — Trend Following — defines the strategy and its price-only philosophy.
- Ch 2 — Great Trend Followers — trader-by-trader profiles and performance data (Dunn, Henry, Seykota, Campbell, Parker, Abraham, Dennis, Donchian, Livermore).
- Ch 3 — Performance Data — absolute returns, drawdowns, correlation, zero-sum nature of futures trading.
- Ch 4 — Big Events in Trend Following — five case studies (1987 crash, LTCM, Asian contagion/Niederhoffer, Barings, Metallgesellschaft).
- Ch 5 — Baseball: Thinking Outside the Batter's Box — Moneyball-style statistical decision-making as an analogy for systematic trading.
- Ch 6 — Human Behavior — prospect theory, emotional intelligence, the disposition effect, Seykota's Trading Tribe.
- Ch 7 — Decision-Making — Occam's razor, fast-and-frugal heuristics, process vs. outcome thinking.
- Ch 8 — Science of Trading — critical thinking, chaos theory, compounding.
- Ch 9 — Holy Grails — critiques buy-and-hold, "losers average losers," analysis paralysis.
- Ch 10 — Trading Systems — the five questions for a trading system; entry, exit, sizing logic; FAQs.
- Ch 11 — Conclusion — why trend following is slowly accepted; leverage vs. return.
- Appendices — A: trader personality traits; B: payoff models; C: fully specified illustrative system (see system page); D: Modern Portfolio Theory and managed futures; E: critical questions for trading systems.

## Strengths and caveats

- Performance tables are largely hypothetical/composite ("$1,000 growth" indices) built from manager-reported data through the early 2000s; not independently audited, and fee/survivorship effects are not addressed in depth.
- The one fully worked system (Appendix C) is explicitly illustrative only, using in-sample data (1991–2000) with no out-of-sample validation and no commissions/slippage — the author flags this himself.
- Heavy reliance on practitioner quotations means the "rules" are anecdotal and inconsistent in specifics (per-trade risk ranges 1–6% depending on who is quoted) rather than one codified method.
- Strongly polemical against discretionary/fundamental trading and buy-and-hold; contrarian claims (e.g., profiting from Barings and LTCM) are asserted rather than derived from primary trade data.
- Timeless in intent, but market examples (dot-com bust, LTCM, early-2000s manager AUM) date the book to 2004.

## Who should read it

Traders and allocators who want the historical and psychological case for systematic, price-based trend following — a "why" companion to more mechanical rule-books like the Turtle system, rather than a standalone how-to.

## Related books in this library

- [Way of the Turtle](https://ninad-k.github.io/trading-playbook/books/curtis-faith-way-of-the-turtle.html) — a fully codified breakout/ATR-sizing system in the tradition Covel describes anecdotally.
- [The Complete TurtleTrader: The Legend, the Lessons, the Results](https://ninad-k.github.io/trading-playbook/books/the-complete-turtletrader-the-legend-the-lessons-the-results.html) — deeper history of Richard Dennis's Turtles, a lineage profiled here.
- [Trading in the Zone: Master the Market with Confidence, Discipline, and a Winning Attitude](https://ninad-k.github.io/trading-playbook/books/trading-in-the-zone.html) — expands on the psychology (discipline, probabilistic thinking) Covel treats in Parts III–IV.
- [Stock Market Wizards](https://ninad-k.github.io/trading-playbook/books/jack-schwager-stock-market-wizards.html) — same interview-driven format applied to a broader, partly discretionary set of traders.
- [The Original Turtle Trading Rules](https://ninad-k.github.io/trading-playbook/books/turtlerules.html) — a concrete rule set comparable to Covel's illustrative Appendix C system.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: trend-following, managed-futures, risk-management, discipline, drawdowns, mechanical-systems, performance-data
