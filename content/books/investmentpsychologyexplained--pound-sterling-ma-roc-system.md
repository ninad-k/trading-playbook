---
title: "Investment Psychology Explained: Pound Sterling MA/ROC System"
author: Martin J. Pring
year: 1993
slug: investmentpsychologyexplained--pound-sterling-ma-roc-system
tier: A
category: Trading Psychology & Discipline
tags: [mechanical-system, moving-average, rate-of-change, futures, trend-following, currencies]
difficulty: intermediate
doc_type: system
parent: investmentpsychologyexplained
pages: 134
one_liner: "Pring's fully specified trend-following system for British pound futures: 10-week MA plus dual rate-of-change filters, used to illustrate why staying the course matters more than the rules themselves."
related: [curtis-faith-way-of-the-turtle]
source_file: "InvestmentPsychologyExplained.pdf"
---

## What it is

A simple mechanical trend-following system for trading British pound futures, originally introduced in Pring's *Technical Analysis Explained* and reproduced in Chapter 6 ("Staying the Course") to make a psychological point rather than to promote the system itself: that a genuinely profitable method still produces losing trades and drawdowns, and the discipline to hold every signal — not the cleverness of the rules — is what turns a profitable long-run system into an actual profit. The system combines a moving average (trend filter) with two rate-of-change readings (momentum confirmation) on weekly data.

## Rules

**Go long (Rule 1)** when all three conditions hold simultaneously:
1. Price is above its 10-week moving average.
2. The 13-week rate of change is above zero.
3. The 6-week rate of change is above zero.

**Go short (Rule 2)** when all conditions in Rule 1 are reversed:
1. Price is below its 10-week moving average.
2. The 13-week rate of change is below zero.
3. The 6-week rate of change is below zero.

The system is always in the market, reversing from long to short (or vice versa) as the three conditions flip together. No separate stop-loss, profit target, or position-sizing rule is specified in the text beyond the reversal logic itself — the system is presented purely as an entry/exit signal generator.

**Backtested performance (as reported):** tested back to the early 1970s; following it "religiously" using 10% margin and reinvesting profits would have turned an initial $10,000 into more than $1,000,000 by 1980, with performance continuing to improve after that. A separate unleveraged equity curve (1980–1992, starting at $1,000) is shown growing over the period, though with counter-trend signals producing the largest losing trades along the way.

## Risk

- The system uses no explicit dollar or percentage stop; risk control comes entirely from the reversal mechanism — a losing long position is closed out as soon as the three conditions flip to a short signal, not before.
- Pring's own commentary stresses that nearly all of the system's profit came from signals taken in the direction of the prevailing main trend; counter-trend signals were consistently the source of its largest losing trades — implying the system performs worse (or should be filtered further) when the primary trend is unclear or absent.
- No portfolio-level risk guidance (position size, leverage limit, correlation with other positions) is given specific to this system; the 10% margin figure cited in the backtest is illustrative of the historical leverage used, not a recommended maximum.

## Caveats

- Presented explicitly as a teaching example about psychological discipline (staying the course through drawdowns), not as a system Pring is currently recommending traders adopt.
- No out-of-sample test, transaction cost accounting, or slippage adjustment is mentioned for either the 1970s–1980 or 1980–1992 backtest windows.
- The system trades a single instrument (British pound futures) with no diversification; its equity curve reflects concentration risk that a real portfolio would typically want to spread across multiple markets.
- Because the system is always in the market (constant long-or-short exposure with no flat/cash state), it will underperform structurally in prolonged sideways or choppy conditions, as the moving-average-crossover example earlier in the same chapter (S&P 500, 25-day MA) is shown to do.
