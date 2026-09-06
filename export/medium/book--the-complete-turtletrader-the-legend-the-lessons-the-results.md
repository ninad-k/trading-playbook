# The Complete TurtleTrader: The Legend, the Lessons, the Results: the trader's summary

*Tells the Richard Dennis/William Eckhardt Turtle experiment and, unlike the earlier Covel site archive, publishes the actual N/ATR-based System One and System Two breakout rules.*

**Michael W. Covel** · 2007 · Trend Following & Mechanical Systems · intermediate

*Source coverage: partial. PDF pages inspected: 7-10, 42, 56, 65, 71-73, 86 (the system description with its 2%-unit sizing, expectation arithmetic and the per-Turtle performance tables). These are study notes, not verified trading results.*

## Overview

In 1983-84, Chicago commodities trader Richard Dennis bet his partner William Eckhardt that trading skill could be taught to novices; they recruited and trained two small classes of "Turtles" and funded them with real money. Michael Covel's book reconstructs that experiment from interviews with more than 20 former Turtles and staff, and — unlike Covel's earlier TurtleTrader.com site archive, which discussed the Turtles' fame without disclosing their method — this book publishes the actual entry, exit, and position-sizing rules Dennis and Eckhardt taught: a volatility-scaled ("N", the Turtles' term for Average True Range), two-system price-breakout method with a fixed 2%-of-equity risk unit and mechanical pyramiding. The book intersperses the rules with career profiles of individual Turtles (Jerry Parker, Liz Cheval, Curtis Faith, and others), their post-program track records as independent CTAs, and a broader argument that mechanical trend following, not stock-picking or forecasting, is what actually produces outsized, repeatable returns.

## Core thesis

Trading is a learnable, rules-based skill, not an innate talent — Dennis's core wager, which the book treats as vindicated by the Turtles' subsequent careers. The specific edge that worked was price-based trend following: buying strength and shorting weakness on multi-week breakouts, sized by market volatility rather than intuition, with strict predefined stops and systematic pyramiding of winners. The book argues that discipline in applying a positive-expectation system consistently — not forecasting accuracy — is what separates the Turtles' results (and, Covel argues, many successful trend-following CTAs since) from the median trader and from buy-and-hold indexing.

## Key concepts

- **N (Average True Range)** — volatility measure: the greatest of (today's high − today's low), (yesterday's close − today's high), (yesterday's close − today's low), averaged over 20 days; used both to size positions and to set stops.
- **Unit** — contracts representing 2% of account equity at current volatility; the basic sizing building block, made comparable across unrelated markets (corn, gold, bonds) because each unit carries roughly equal dollar risk.
- **System One (S1)** — a 20-day breakout entry with a 10-day opposite-direction breakout exit, subject to a "last signal was a winner" skip filter.
- **System Two (S2)** — a 55-day breakout entry with a 20-day opposite-direction exit; used both standalone and as a fail-safe re-entry when S1 was filtered out of a big trend.
- **2N stop** — the hard stop, two times N behind the entry price; whichever of the 2N stop or the opposite breakout exit hit first determined the exit.
- **Pyramiding** — adding one unit per 1N favorable move, up to five units per market, with all stops raised to the newest unit's 2N level as each unit is added.
- **Expectation (edge)** — E = (win% × average win) − (loss% × average loss); win rate alone (the Turtles won roughly 35-40% of trades) is meaningless without win/loss size.
- **Unit limits and correlation** — caps of four to five units per market, plus rules for reducing effective risk when trading correlated markets so a portfolio isn't unknowingly doubling exposure.
- **Rate-of-decrease drawdown response** — cutting the 2% risk unit as equity draws down, restoring it only as equity recovers.
- **Random entries** — Eckhardt's finding that exit discipline mattered far more than entry timing; a purely random entry with a sound exit rule performed surprisingly well in testing.

## Rules and setups

A full sub-page, [The Turtle Trading System](https://ninad-k.github.io/trading-playbook/books/the-complete-turtletrader-the-legend-the-lessons-the-results--turtle-trading-system.html), reproduces the complete Turtle system (entries, exits, sizing, pyramiding) in codeable detail. In summary:

1. **Entry**: buy a new 20-day high (S1) or 55-day high (S2); short a new 20-day low (S1) or 55-day low (S2). S1 signals are skipped if the prior S1 trade was a winner (with an exception if that prior trade lost more than 2N), but a skipped trend is still caught via the S2 fail-safe entry.
2. **Exit**: whichever comes first of (a) a 2N stop from the position's entry (raised to the newest unit's level as units are pyramided), or (b) an opposite-direction breakout — 10-day for S1, 20-day for S2.
3. **Position size**: 1 unit = (2% of account equity) ÷ (2N in dollars for that market), rounded down to whole contracts.
4. **Pyramiding**: add one unit per 1N favorable move from the initial entry, to a maximum of five units per market; recompute N and stops with each addition.
5. **Portfolio limits**: no more than four to five units in a single market; reduce combined risk across highly correlated markets rather than treating each as independent.
6. **Drawdown response**: reduce the risk-per-unit percentage as account equity falls, restoring it only as equity climbs back.

## Risk and money management

Risk is defined entirely in units of N rather than dollars, a deliberate psychological device — Turtles reported thinking "I'm one N up," not "I have $34 million in bonds on," to keep position size from triggering emotional overreaction. The 2%-per-trade unit risk, combined with 2N stops and five-unit pyramiding caps, bounds worst-case loss on any single market to roughly 10% of equity before the drawdown-response rule further cuts exposure. The book documents that Turtle-style traders and CTAs experienced significant monthly and multi-month drawdowns (30-40%+ in some years) even while producing strong long-run expectation, and frames enduring those drawdowns — not avoiding them — as the central risk-management challenge.

## Psychology and discipline

The book's second major theme, after the rules themselves, is that following a positive-expectation system consistently is harder than designing one. It documents Turtles washing out not from bad rules but from overriding them — hesitating on signals, cutting winners early, or abandoning the system during a losing streak just before a large trend arrived. Recurring points: statistical "Type I/Type II error" thinking (better to take many small false-positive losses than to reject a real trend), a deliberate emphasis on price action over news or fundamentals ("stop watching TV"), and Jerry Parker's repeated point that simplicity and robustness — not fine-tuned parameters — are what let a system keep working out of sample. The book also covers uncomfortable internal dynamics, including disputes over capital allocation and whether some traded outside the rules (notably Curtis Faith), as a case study in how individual psychology diverges even under a shared mechanical system.

## Chapter map

1. Nurture versus Nature — the premise of Dennis's bet with Eckhardt.
2. Prince of the Pit — Dennis's early trading career and rise.
3. The Turtles — recruitment and selection of the trainees.
4. The Philosophy — trend following as a worldview; statistics over forecasting.
5. The Rules — the full System One/System Two, N, unit sizing, and pyramiding rules.
6. In the Womb — the Turtles' training period and early live trading.
7. Who Got What to Trade — capital allocation disputes among Turtles.
8. Game Over — the end of Dennis's program.
9. Out on Their Own — Turtles launching independent trading businesses.
10. Dennis Comes Back to the Game — Dennis's later trading comeback.
11. Seizing Opportunity — case studies of Turtles applying the system post-program.
12. Failure Is a Choice — Turtles (and traders generally) who abandoned discipline.
13. Second-Generation Turtles — traders who learned the method indirectly.
14. Model Greatness — closing argument for systematic trend following as a repeatable skill.

## Strengths and caveats

Strength: this is one of the few popular trading books to publish a complete, numerically worked, codeable trading system (entries, exits, sizing, pyramiding all specified) rather than gesture at "trend following" in the abstract, with market examples (Eurodollars, natural gas, live cattle) worked using real dates and prices. Caveats: the book is written by a long-time promoter of trend following, and its performance claims for Turtle-derived CTAs rely on the funds' own reported track records rather than independent audit; the specific 20/55/10/20-day parameters are explicitly called non-sacred by the book itself (Parker: "a minor change of a variable in any robust trading system should not cause significant performance changes"), so readers hunting for a magic parameter set are reading it wrong. Cited markets and margin figures are dated (pre-2008 electronic-market liquidity), and the Curtis Faith capital-allocation dispute is presented largely from other Turtles' perspective.

## Who should read it

Traders wanting a fully specified, historically validated trend-following system to study or adapt, and readers who want the actual Turtle rules rather than the marketing-heavy account in Covel's earlier site archive ([TurtleTrader.com Site Archive](https://ninad-k.github.io/trading-playbook/books/turtletrader.html)). Pairs naturally with a Market Wizards-style read for the psychology of sticking with a system through drawdowns.

## Related books in this library

- [Way of the Turtle](https://ninad-k.github.io/trading-playbook/books/curtis-faith-way-of-the-turtle.html) — a first-person account of the same system from the Turtle who traded the largest size; useful for comparing rule interpretation and discipline in practice.
- [The Original Turtle Trading Rules](https://ninad-k.github.io/trading-playbook/books/turtlerules.html) — the original written Turtle rules document this book's Chapter 5 draws on and expands.
- [TurtleTrader.com Site Archive](https://ninad-k.github.io/trading-playbook/books/turtletrader.html) — Covel's earlier, pre-disclosure site archive that discusses the Turtles' fame without publishing the actual rules; read together to see what changed once the rules became public.
- [Trend Following](https://ninad-k.github.io/trading-playbook/books/michael-covel-trend-following.html) — Covel's broader case for systematic trend following across many CTAs, of which the Turtles are one example.
- [Stock Market Wizards](https://ninad-k.github.io/trading-playbook/books/jack-schwager-stock-market-wizards.html) — comparable trader-profile format, useful for cross-referencing psychology and discipline themes.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: turtle-trading, trend-following, breakout, position-sizing, money-management, risk-of-ruin, market-wizards
