---
title: Way of the Turtle
author: Curtis M. Faith
year: 2007
slug: curtis-faith-way-of-the-turtle
tier: A
category: Trend Following & Mechanical Systems
tags: [turtle-trading, trend-following, breakout, position-sizing, backtesting, robustness, psychology]
difficulty: intermediate
doc_type: book
pages: 313
one_liner: "The youngest Turtle's own account of the original Turtle rules, plus his later work on robust backtest statistics (RAR%, R-cubed, robust Sharpe)."
related: [the-complete-turtletrader-the-legend-the-lessons-the-results, turtlerules, michael-covel-trend-following, trading-in-the-zone]
source_file: "Curtis Faith - Way of the Turtle.pdf"
---

## Overview

Curtis Faith was 19 when he was selected in 1983 for Richard Dennis and William Eckhardt's famous "Turtle" experiment, which set out to prove that trading could be taught. Faith went on to be one of the program's top performers. Way of the Turtle mixes his personal account of that training and its immediate aftermath with a later-career, more rigorous treatment of system design: how to measure edge, size risk, test a system honestly, and judge whether a backtest result is real or noise. The book culminates in his own alternative breakout systems (ATR Channel Breakout, Bollinger Breakout, Donchian Trend, dual/triple moving average) built to illustrate the same principles the Turtles used, and closes with a full reprint of the original Turtle trading rules.

## Core thesis

Trading success comes from psychology and discipline applied to a system with genuine positive expectation, not from a secret formula. Faith argues the Turtles' specific entry rules were "well known" even in 1983 and unimportant relative to the ability to execute them consistently through losing streaks. He treats trading as a long-run statistical game: manage risk so ruin is never possible, measure systems with robust statistics that aren't fooled by a lucky test window, and accept that most trades lose money while a few large trends pay for everything.

## Key concepts

- **Edge / expectation** — the average dollar return per dollar risked across many trades; a system must have positive expectation before position sizing or psychology matter.
- **N (volatility unit)** — the 20-day exponential moving average of the daily true range (today's high/low range, or the range including the prior close, whichever is largest); the book's term for what is now commonly called ATR.
- **Unit** — a position sized so that 1N of adverse price movement equals roughly 1% of account equity; the base building block of Turtle position sizing.
- **Outcome bias** — judging a decision by how the trade turned out rather than by whether it was the right decision given the information available at the time; the Turtles were trained to ignore it.
- **Whipsaw** — an alternative, tighter (½N) stop strategy that raises trade frequency and lowers the win rate but the book credits with better long-run results for some Turtles.
- **E-ratio (edge ratio)** — a measure comparing typical favorable versus adverse price movement following a signal, used to test whether an entry has real predictive value before backtesting a full system.
- **Regressed Annual Return (RAR%)** — Faith's own metric: the annualized return implied by a linear-regression best-fit line through the equity curve, far less sensitive to the exact start/end dates of a test than CAGR%.
- **R-cubed (robust risk/reward ratio)** — RAR% divided by a length-adjusted average of the five largest drawdowns; Faith's more stable replacement for the MAR ratio.
- **Robust Sharpe ratio** — RAR% divided by the annualized standard deviation of monthly returns, substituting the regression-based return figure for the ordinary mean used in the classic Sharpe ratio.
- **Monte Carlo simulation** — resampling historical trades to generate alternate equity curves and build a confidence distribution around a system's likely RAR%, rather than trusting one historical run.
- **Robustness through diversity and simplicity** — Faith's design philosophy: simple rules with few free parameters, applied across many uncorrelated markets, survive changing market conditions better than complex, curve-fit rules.

## Rules and setups

The complete original Turtle System (N, System 1/System 2 breakout entries, unit sizing, 2N stops, pyramiding, and exits) is documented in the companion system page [[curtis-faith-way-of-the-turtle--turtle-system]]; the numbers there match the book's own reprint of the "Original Turtle Trading Rules." In the main chapters Faith also outlines four lessons he says summarize the whole program: trade with an edge, manage risk, be consistent, and keep it simple. He additionally sketches several non-Turtle systems built to teach the same concepts with different entries: an ATR Channel Breakout (enter on a close outside a volatility-scaled channel around a moving average), a Bollinger Breakout (enter on a close outside a standard-deviation band), a Donchian Trend system (20-day breakout entries filtered to the direction of a longer-term trend, with a 10-day opposite breakout exit), and a time-exit variant that closes trades after a fixed holding period. These are illustrations of system-building principles rather than a second complete trading plan, and the book does not give every parameter needed to reproduce them exactly.

## Risk and money management

Turtle risk control is entirely N-based: each unit risks about 1% of equity, each 2N stop caps a unit's loss near 2%, and portfolio-level unit limits (detailed on the system page) bound how much can be riding on correlated markets at once. Faith stresses that this volatility normalization — sizing contracts so a fixed-dollar move represents the same percentage risk in every market — is what let the Turtles diversify meaningfully across roughly 20 futures markets. He also discusses reducing the trading-size base (a notional account) after sustained drawdowns and restoring it only as equity recovers, and argues that traders chronically underestimate the drawdowns they can tolerate: he describes historical tests of a Donchian Trend system with drawdowns of 38–42%, and states his own worst personal drawdown was on the order of 70%.

## Psychology and discipline

Faith's central psychological story is the Turtles' first big trend, a February 1984 heating oil breakout: trained identically, he was the only Turtle who took and held the full position through a scary pullback, and made roughly three times what his classmates made — a result he attributes entirely to emotional discipline, not knowledge. He frames trading as psychologically a "losers' game": most trades lose, so a trader must be comfortable being wrong often and must not need each trade to work to feel competent. He also warns against "system death" anxiety — mistaking a normal drawdown for a broken system — arguing that traders who abandon a valid system after a losing streak, rather than after honest testing shows it has actually stopped working, are making a psychological error, not a rational one.

## Chapter map

- Ch 1 — Risk Junkies — why some people are drawn to trading and to risk generally.
- Ch 2 — Taming the Turtle Mind — introduces the psychological training Dennis and Eckhardt gave the class.
- Ch 3 — The First $2 Million Is the Toughest — the heating oil trade story and the four core lessons.
- Ch 4 — Think Like a Turtle — cognitive biases and how the Turtles were trained to counter them.
- Ch 5 — Trading with an Edge — expectation, breakouts, support/resistance, and the E-ratio.
- Ch 6 — Falling Off the Edge — points of price instability and stop placement logic.
- Ch 7 — By What Measure? — drawdowns, low returns, price shocks, system death, and the Sharpe ratio.
- Ch 8 — Risk and Money Management — position sizing philosophy and drawdown-based size reduction.
- Ch 9 — Turtle-Style Building Blocks — breakouts and moving averages as system components.
- Ch 10 — Turtle-Style Trading: Step by Step — the ATR Channel Breakout, Bollinger Breakout, and Donchian systems.
- Ch 11 — Lies, Damn Lies, and Backtests — pitfalls in historical simulation, including hindsight and trader-effect biases.
- Ch 12 — On Solid Ground — RAR%, R-cubed, and the robust Sharpe ratio.
- Ch 13 — Bulletproof Systems — robustness via diversity and simplicity, market classes, and market selection.
- Ch 14 — Mastering Your Demons — emotional and psychological strength as the deciding factor in results.
- Bonus chapter — Original Turtle Trading Rules — the full reprinted rule set (N, System 1/2, sizing, stops, pyramiding, exits).

## Strengths and caveats

The book is unusually candid about both the mechanics and emotional reality of trading a mechanical system, and its robustness statistics (RAR%, R-cubed, robust Sharpe) are a genuinely useful, if idiosyncratic, contribution not commonly taught elsewhere. Caveats: dollar and contract examples reflect mid-2000s futures pricing and account sizes and need rescaling; the alternative systems in Chapters 9–10 are illustrative and under-specified compared with the fully documented original rules; and Faith's claim that entry rules were unimportant to the Turtles' success sits in tension with the detailed, parameter-specific rule set he reprints in full — read "rules don't matter, discipline does" as a claim about his own experience, not license to ignore parameter choices.

## Who should read it

Traders who want the original Turtle system from a primary source, and anyone building or evaluating mechanical trend-following systems who wants tools (RAR%, R-cubed, Monte Carlo resampling) for judging whether a backtest result is trustworthy rather than curve-fit.

## Related books in this library

- [[the-complete-turtletrader-the-legend-the-lessons-the-results]] — an outside journalist's account of the same program and the same rule set, useful for cross-checking Faith's version.
- [[turtlerules]] — the original written rules document the Turtles themselves used, which the bonus chapter here closely mirrors.
- [[michael-covel-trend-following]] — broader context on trend-following as a discipline beyond the Turtle program specifically.
- [[trading-in-the-zone]] — a deeper treatment of the probabilistic mindset Faith says was decisive for his own results.
