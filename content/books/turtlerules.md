---
author: Curtis Faith
category: Trend Following & Mechanical Systems
difficulty: intermediate
doc_type: manual
one_liner: The free, original written record of the actual 1983 Turtle rules — N-based
  unit sizing, System 1/2 breakouts, 2N stops, and unit-adding — released by an Original
  Turtle.
pages: 37
related:
- curtis-faith-way-of-the-turtle
- the-complete-turtletrader-the-legend-the-lessons-the-results
- turtletrader
- turtles-matter
- position-sizing
reviewed_pdf_pages: 1-37
slug: turtlerules
source_file: turtlerules.pdf
source_review: full
tags:
- turtle-trading
- trend-following
- breakout
- position-sizing
- money-management
- donchian
- futures
tier: A
title: The Original Turtle Trading Rules
year: 2003
---

## Overview

This short manual, published in 2003 by "OriginalTurtles.org" and signed by Curtis Faith, is a direct release of the complete Turtle Trading System rules as Richard Dennis and William Eckhardt taught them in December 1983. It was written specifically to undercut paid resellers (a website and a former Turtle) who were selling incomplete or inaccurate versions of the rules for hundreds to thousands of dollars. The document opens with the Turtle Experiment's origin — Dennis and Eckhardt's bet over whether great traders are born or made — then lays out every component of the system: markets, position sizing, entries, stops, exits, and execution tactics.

## Core thesis

Trading can be taught as a Complete Trading System that answers every decision a trader faces (what to trade, how much, when to enter, when to cut losses, when to take profits, how to execute) with explicit, mechanical rules, leaving nothing to discretion. The Turtles' four-year 80% average annual compound return is offered as proof the approach works — but the document is equally insistent that knowing the rules is nearly worthless without the confidence and discipline to follow them through extended losing streaks, since several Turtles who had the identical rulebook still lost money.

## Key concepts

- **N** — the market's daily volatility unit: a 20-day exponential moving average of true range (equivalent to ATR). Used to normalize position size and stops across markets of different volatility.
- **Unit** — the base position-size increment, sized so that 1N of adverse movement equals roughly 1% of account equity.
- **System 1 / System 2** — two related breakout entry methods: a 20-day channel breakout (S1) and a 55-day channel breakout (S2).
- **Failsafe breakout** — the 55-day S2 breakout used to catch a move whenever an S1 signal is skipped.
- **Whipsaw stop** — an alternate ½N (≈0.5% risk) stop-and-re-enter variant, more trades and lower win rate but reported better net results for some Turtles.
- **Loaded** — trader jargon for holding the maximum permitted units at a given correlation level.
- **Notional equity** — the Turtles traded against an assigned account size that was ratcheted down 20% for every 10% drawdown, not their literal running balance.
- **Dollar volatility** — N converted to dollars per contract (N × dollars-per-point), the bridge between price volatility and position size.
- **Complete Trading System** — the book's framing device: markets, position sizing, entries, stops, exits, and tactics together, since a system missing any one of these (especially profit exits) is not complete.

## Rules and setups

See [[turtlerules--turtle-system]] for the full, code-ready specification (formulas, entry/stop/exit tables, unit-adding schedule, correlation limits). In summary:

1. **Markets**: liquid U.S. futures only — currencies, financial futures (bonds, notes, Eurodollar, T-bills), metals, energies, and softs (coffee, cocoa, sugar, cotton). Grains and meats were excluded for position-limit and integrity reasons, not by rule.
2. **Position size**: Unit = (1% of account equity) ÷ (N × dollars-per-point), truncated to whole contracts.
3. **Entries**: buy/sell one tick beyond the 20-day high/low (System 1) or the 55-day high/low (System 2); System 1 skips a signal after a winning prior trade, falling back to the System 2 breakout as a failsafe.
4. **Adding units**: one more unit every ½N of favorable movement from the last fill, up to 4 units per market.
5. **Stops**: initial stop at 2N against entry (≈2% equity); stops on earlier units are raised ½N with each add, generally converging near 2N below the newest unit.
6. **Exits**: System 1 exits on a 10-day opposite breakout; System 2 exits on a 20-day opposite breakout.
7. **Correlation caps**: max 4 units/market, 6 units/closely correlated group, 10/loosely correlated group, 12 total in one direction.

## Risk and money management

Risk is governed entirely by N: a 2N stop caps single-unit loss near 2% of equity, and the unit-correlation ladder (4/6/10/12) caps aggregate exposure to any one market or related group. The account itself is dynamically resized — a 20% notional cut for every 10% drawdown — so risk automatically shrinks during losing periods. The document is explicit that this is a low-win-rate system (most breakouts fail) that depends on a small number of large trend trades to be profitable, and that skipping or slow-rolling unit adds (a common trader "improvement") tends to reduce returns rather than protect capital, because slower entries increase the odds a normal retracement hits the stop before the trend resumes.

## Psychology and discipline

The document's real argument is psychological, not technical: identical rules produced wildly different results across the 23 Turtles because outcomes were determined by who could follow the system without overriding it. It quotes Richard Dennis's famous line that publishing his rules in a newspaper wouldn't create competitors, because confidence and discipline — not rule knowledge — were the scarce resource. Traders are warned specifically against widening stops "to give it room," second-guessing exits during long profitable runs, and doubting the system during the inevitable multi-month losing streaks a trend-following method produces. The recommended antidote is doing your own historical research on the system so conviction is earned, not borrowed.

## Chapter map

- Foreword — why the rules are being given away free, and a critique of paid Turtle-rules resellers.
- Introduction: The Turtle Experiment — Dennis vs. Eckhardt's nature/nurture bet and how the Turtles were recruited and funded.
- Ch 1 — A Complete Trading System — the six components every system must define.
- Ch 2 — Markets: what the Turtles traded and why (liquidity, position limits, floor corruption in meats).
- Ch 3 — Position Sizing — N, dollar volatility, the Unit formula, worked examples, correlation-based unit limits.
- Ch 4 — Entries — System 1/System 2 breakout rules, the failsafe breakout, adding units every ½N.
- Ch 5 — Stops — 2N stop placement, stop-raising on adds, the Whipsaw alternative.
- Ch 6 — Exits — 10-day/20-day opposite breakout exits and why they're psychologically the hardest part of the system.
- Ch 7 — Tactics — order entry (limit vs. market), handling fast markets, buying strength/selling weakness among correlated signals, rolling futures contracts.
- Ch 8 — Further Study — pointers on trading psychology, money management, and doing your own historical research.

## Strengths and caveats

This is a primary source, not a secondary summary — it is the closest thing to an authoritative, free written record of the actual rules, corroborated independently by Michael Covel's [[the-complete-turtletrader-the-legend-the-lessons-the-results]] and Curtis Faith's own [[curtis-faith-way-of-the-turtle]]. Its dollar examples (heating oil, gold, crude oil) reflect early-2000s prices and contract sizes and need rescaling for current markets. The document itself notes the rules "are not very complicated" but repeatedly stresses that most readers will still fail to trade them profitably, which the document attributes entirely to discipline rather than any gap in the rules — a claim readers should weigh against selection bias in which former Turtles chose to go public with success stories. It offers no formal backtest statistics, drawdown figures, or win-rate data beyond anecdote.

## Who should read it

Traders who want the mechanical Turtle system specified precisely enough to code and backtest, without wading through a memoir or narrative history. It assumes no prior background but rewards readers who also read a narrative account ([[curtis-faith-way-of-the-turtle]] or [[the-complete-turtletrader-the-legend-the-lessons-the-results]]) for the psychological and historical context this document only gestures at.

## Related books in this library

- [[curtis-faith-way-of-the-turtle--turtle-system]] — a second, independently written reprint of the same rules from a Turtle who traded them.
- [[the-complete-turtletrader-the-legend-the-lessons-the-results--turtle-trading-system]] — the rules reconstructed by a journalist from more than 20 Turtle interviews, with career outcomes attached.
- [[turtletrader]] — the commercial site the foreword explicitly criticizes for selling an incomplete version of these same rules.
- [[position-sizing]] — deeper treatment of the volatility-normalized sizing approach the Turtles pioneered.
