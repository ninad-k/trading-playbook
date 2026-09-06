# MTPredictor Trading Course — Part 2: the trader's summary

*Advanced manual on MTPredictor's Elliott wave software: manual wave counting, Wave Price Targets, coloured Reversal Bars, and a strict 2:1 risk/reward filter for every trade.*

**Steve Griffiths** · 2004 · Fibonacci, Gann & Elliott Wave · intermediate

*Source coverage: partial. PDF pages inspected: 1-3, 9, 12, 14-16 (the ratio set, Elliott module description, connected pivots and the 2-3 initial-risk zone). These are study notes, not verified trading results.*

## Overview

This is the second, advanced volume of Steve Griffiths' training course for the MTPredictor charting software (MTPredictor Ltd, third edition October 2004). Where Part 1 covers the software's automatic trade set-ups, Part 2 opens the analysis "black box": how the underlying Elliott wave counts, Fibonacci-derived Wave Price Targets (WPTs), and coloured Reversal Bars are built, so a trader can perform the same analysis manually when the automatic routines fail. It then adds discretionary set-ups (minor pullback, 80/20 day, inside/outside day), trade management (pyramiding, multi-unit exits, the 2-3 profit zone), and applications to day trading, weekly charts, and stocks — all subordinated to one filter: only take a trade whose projected profit is at least twice the initial risk.

## Core thesis

Markets unfold in a clear, tradable Elliott wave pattern only about half the time; the discipline is to act solely when the pattern is obvious, at a price zone independently projected by Fibonacci-ratio Wave Price Targets, and confirmed by the market's own reversal action (a coloured Reversal Bar), with the trade sized so that potential profit is at least twice the risk of the protective stop. Predicting reversals is possible only within this narrow, rules-based window — WPTs are meant to be "leading indicators" that prepare a trader in advance, not a signal to force trades on ambiguous charts.

## Key concepts

- **Wave Price Target (WPT)** — a support/resistance projection from multiplying a prior swing by core ratios (0.382, 0.5, 0.618, 0.786, 1.00, 1.272, 1.618, 2.618, 4.236) and clustering the results; each Elliott wave label (1orA, 2orB, 3, 4, 5, C, E) has its own swing set and click sequence.
- **Coloured Reversal Bar** — a bar marked blue (buy) or red (sell) when price reacts inside a WPT zone; confirmed only once price exceeds that bar's high (buy) or low (sell).
- **Show Elliott Waves module** — automatic pattern recognition across Minor/Intermediate/Major degree, shown only when a valid count exists (roughly 50% of the time), paired with automatic WPTs and Reversal Bars.
- **Near-miss** — price slightly exceeding a WPT zone (up to about half its width), or immediately closing back inside it, still counts as a valid reaction.
- **Connected Pivots** — the software's Intermediate-degree swing markers, used to hand-label a wave count when the automatic module fails, checked against Elliott rules (wave 3 not shortest, wave 4 doesn't overlap wave 1, alternation between waves 2 and 4).
- **2-3 initial risk zone** — the area where profit equals roughly 2–3× initial risk, used both as a numeric risk/reward check and later as a place to bank profit or tighten stops.
- **Minor pullback** — a Gann-derived, single-swing correction against an established trend, used to add a position mid-trend.
- **80/20 day** — a Connors/Raschke ("Street Smarts") day-trading pattern adapted with WPT confirmation.
- **Inside day / outside day** — trend-continuation entries, occasionally reversal entries when combined with WPT support/resistance.
- **Pyramiding** — treating a trade as a sequence of add-on entries (initial set-up plus later inside-day or pullback triggers) rather than one static position.

## Rules and setups

1. **WPT projection** — select the relevant WPT (e.g. Wave 5 WPT needs 5 clicks across waves 1–4), click the defining pivots; software draws minimum/typical/maximum target zones. Best support/resistance = clusters of several ratios in a small area.
2. **Reversal Bar confirmation** — a valid signal needs all three: price inside a WPT zone, a coloured Reversal Bar forming there, and price then exceeding that bar's high (buy) or low (sell).
3. **Minor pullback trade** — valid only as a single-swing correction (verified with connected pivots) that doesn't exceed the prior swing extreme. Entry: break of the pullback bar's high/low. Stop: just beyond its opposite extreme.
4. **80/20 day (day-trading)** — a day where open/close sit in opposite 20% extremes of a wider-than-recent range, using day-session data only. Enter on a small break back through the 80/20 day's extreme the next day; strongest when it falls inside a WPT zone.
5. **Inside day / outside day (trend continuation)** — enter as the prior bar's high/low is exceeded (inside day) or, best, when a narrow inside day is followed by a break of its high after price first dips below its low (outside day). Stop just beyond the triggering bar's extreme.
6. **Risk/reward filter (applies to every set-up above)** — project the first profit target (nearest WPT) against initial risk; minimum acceptable ratio 2:1. The 2-3 zone is then used to bank partial profit or tighten the stop.
7. **Pyramiding (worked Corn trade)** — with a $25,000 account risking a fixed 3% of capital per position, take an initial TS1 entry, then add further units on later inside-day triggers, each sized to the same 3% risk cap with its own stop.
8. **Stop management as a trade matures** — initial stop just beyond the triggering bar's extreme; once in the 2-3 zone, bank part of the position or tighten the stop; avoid parking stops at obvious minor swing points.

If "Show Elliott waves" finds no valid pattern, the explicit fallback is not to force a trade — wait, or repeat the WPT/Reversal Bar analysis manually on a hand-drawn count.

## Risk and money management

The book's single money-management constant is the 2:1 minimum profit-to-initial-risk ratio, checked with the Initial Risk to Reward module before every entry; trades that don't clear it are skipped regardless of how good the pattern looks. The one explicit position-sizing rule appears in the pyramiding chapter: risk a fixed 3% of account equity per position (used identically for the initial entry and for each pyramided add-on), with the initial protective stop placed at the pattern-defined level (just beyond the triggering bar), not a fixed dollar or percentage stop distance. The 2-3 initial risk zone is used as a secondary tool for scaling out of winners or trailing stops once a trade is comfortably in profit.

## Psychology and discipline

Griffiths repeatedly frames restraint as the core discipline: because a valid Elliott wave count exists only about half the time, most days should produce no trade at all, and forcing WPT analysis onto an unclear or choppy chart is explicitly called out as a common and costly error. He also stresses accepting smaller-than-hoped profits (e.g., a trade that returns only 0.8× initial risk) as a normal cost of following the system, arguing that consistently keeping losses small and profits at least 2× risk compounds into profitability even without a high win rate.

## Chapter map

- Ch 1 — Introduction — roadmap, reiterating the small-initial-risk principle from Part 1.
- Ch 2 — Important numbers — Fibonacci sequence and ratio derivations (0.382–4.236) underlying all WPTs; Gann's 50%/100% numbers.
- Ch 3 — WPTs — click sequences and ratio sets per wave label; price clustering; the near-miss rule.
- Ch 4 — Coloured Reversal Bars — how bar colour confirms a WPT reaction.
- Ch 5 — Show Elliott Waves — automatic multi-degree wave recognition, paired WPTs/Reversal Bars, worked examples.
- Ch 6 — Manual Analysis — connected pivots for hand-labelling counts when the automatic module fails.
- Ch 7 — Advanced Elliott Wave Analysis — guidelines (5-wave sequences get corrected; waves subdivide into minor patterns) and how to trade them.
- Ch 8 — Initial Risk to Reward module — the 2-3 profit zone and exact risk/reward calculation.
- Ch 9 — Training Mode — software feature for practising wave labelling.
- Ch 10 — Advanced Trading Strategies — minor pullback, 80/20 day, inside/outside day, Doji, 20-period EMA.
- Ch 11 — Advanced Trade Management — wave 3 vs. wave C decisions, the 2-3 zone, multi-unit trading, pyramiding, gap openings.
- Ch 12 — Time analysis — dynamic and static time retracements/projections/clusters.
- Ch 13–14 — Day trading and Weekly charts — applying the method intraday and on longer-term charts.
- Ch 15 — Trading stocks with MTPredictor — equity-specific notes.
- Ch 16–17 — Trend and the "Techniques Curve" self-assessment framework.
- Ch 18 — Daily routine — a suggested end-of-day analysis workflow.
- Ch 19 — Studies — moving averages, moving-average oscillator, Stochastic, Stochastic RSI, Strong Trend Filter.
- Ch 20–23 — Case study, Summary, Q&A, Conclusion.

## Strengths and caveats

Unusually explicit and mechanical for an Elliott wave text — every WPT has a defined click sequence and ratio set, and every entry has a stated stop, making the "TS" set-ups genuinely codeable. But it is a software manual first: much of the value depends on owning MTPredictor, since manual replication of WPT clustering is described as impractically tedious. Performance claims rely on hand-picked chart examples (SPY, FTSE, IBM, Corn, Soybean Meal), some drawn from the author's own prior public calls, with no aggregate win-rate or drawdown statistics. The 80/20 day is explicitly borrowed from Connors and Raschke's "Street Smarts." Wave counting retains an irreducibly discretionary element — deciding which pivots define a "clear and obvious" wave — despite the software layer.

## Who should read it

Traders already comfortable with basic Elliott wave and Fibonacci concepts (e.g., from Part 1 of this course or a general Elliott wave text) who want a fully specified, mechanical entry/stop/target framework rather than pure discretionary wave counting. Less useful to traders unwilling to learn wave labelling by hand, since several techniques assume the reader can verify or override the software's automatic count.

## Related books in this library

- [MTPredictor Trading Course — Part 1](https://ninad-k.github.io/trading-playbook/books/forex-mtpredictor-trading-course-part-1a.html) — Part 1 covers the automatic trade set-ups this volume explains and extends.
- [Elliott Wave Principle](https://ninad-k.github.io/trading-playbook/books/elliott-waves-principle.html) — the foundational wave-counting rules this course applies with added Fibonacci price targets.
- [Fibonacci Applications and Strategies for Traders](https://ninad-k.github.io/trading-playbook/books/fischer-robert-fibonacci-applications-and-strategies-for.html) — a deeper, software-independent treatment of the same Fibonacci ratio families used for WPTs.
- [Street Smarts: High Probability Short-Term Trading Strategies](https://ninad-k.github.io/trading-playbook/books/street-smarts-laurence-connors.html) — original source of the 80/20 day set-up adapted in Chapter 10.
- [New Stock Trend Detector](https://ninad-k.github.io/trading-playbook/books/gann-w-d-new-stock-trend-detector.html) — origin of the minor-pullback observation and the 50%/100% numbers discussed in Chapter 2.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: elliott-wave, fibonacci, wave-price-targets, reversal-bars, risk-reward, mtpredictor, forex, futures
