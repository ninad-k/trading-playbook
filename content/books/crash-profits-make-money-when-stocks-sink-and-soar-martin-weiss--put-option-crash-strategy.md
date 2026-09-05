---
title: "The 15-Rule Put Option Crash Strategy"
author: Martin D. Weiss
year: 2003
slug: crash-profits-make-money-when-stocks-sink-and-soar-martin-weiss--put-option-crash-strategy
tier: A
category: Money Management & Position Sizing
tags: [put-options, position-sizing, risk-limitation, bear-market, options-trading]
difficulty: beginner
doc_type: system
parent: crash-profits-make-money-when-stocks-sink-and-soar-martin-weiss
pages: 368
one_liner: "A capped-risk, staged-entry put-option program for speculating on further stock declines without stop-loss orders."
related: []
source_file: "Crash Profits Make Money When Stocks Sink And Soar Martin Weiss.pdf"
---

## What it is

A small-allocation, long-put-only speculation program described in Chapter 14 ("Deflation!"), intended for an investor who has already moved the bulk of a portfolio to safety (Treasuries/money markets) and wants a strictly capped-risk way to profit further from a continuing decline. It is not a timing system with chart triggers; it is a position-sizing and order-management discipline layered on top of the investor's own bearish view, built around buying only, never writing/selling puts, and treating each contract as a fully disposable bet.

## Rules

**Allocation and pacing**
1. Cap total options exposure at roughly 5% of the portfolio; keep at least 95% in safe/conservative instruments. If losing the 5% would be a problem, skip options entirely.
2. Don't deploy the allocation at once — spread it over about a year (e.g., a planned $10,000 becomes $2,500/quarter).
3. Avoid contracts costing less than ~$50 per contract (poor odds, commission-heavy) or more than ~$500 per contract (too concentrated; buy more, cheaper contracts instead to diversify).
4. Buy an even number of contracts per position (e.g., two) for exit flexibility: once the position doubles, sell half to lock in a breakeven-or-better on the trade and let the remainder run uncapped.

**Timing filter**
5. Prefer buying puts while the underlying market is in "rally mode" (index above its 20-day moving average) — puts are cheaper on strength; prefer selling puts you hold while the market is still in a short-term decline. (The reverse applies to calls.)

**Order execution**
6. Always specify a limit price when buying or selling an option (based on the last trade), adjusted by no more than ~10% for market movement — never use "at the market" orders, because options can be thinly traded and volatile.
7. Don't chase a resting order: wait 2-3 full trading days; if unfilled, reassess and resubmit at the current price rather than repeatedly bidding up.

**Trade management**
8. Expect many small losers and a few large winners; treat any option that never gets in the money as a routine, budgeted loss.
9. Try to close a position (win or lose) before its final two weeks of life to avoid a total loss from time decay.
10. Do not add to a position that is already a clear winner (it's typically too late/expensive); do not rush to dump a loser either — options can reverse from behind.
11. If stopped out of the underlying thesis early (rare), re-enter at the original price level; this occasionally captures a subsequent large move.
12. Traditional stop-loss (sell-stop) orders are explicitly not recommended for this sleeve — risk is already capped by rules 1-3, and a stop would force selling into a temporary adverse move, violating rule 5's discipline.
13. Never write (sell) uncovered puts or calls against this program — that reintroduces unlimited risk, defeating the purpose of a capped-loss strategy.

## Risk

Maximum loss per contract is the premium paid, by construction (rule 3 caps this at roughly $500/contract). Portfolio-level risk is capped at ~5% of total capital (rule 1), with that exposure built up gradually over roughly a year (rule 2) rather than risked all at once. There is no stop-loss mechanism within the options sleeve itself; risk control is entirely front-loaded into sizing, contract-cost limits, and pacing. The strategy has an inherent negative-carry cost: options are wasting assets, so an unchanged or slow-moving market erodes the position's value daily even with no adverse price move, and the book's own worked example shows an investor's put win rate running as low as ~30%, with profitability coming from a small number of large winners (illustrating rule 8's "expect many small losers" framing in practice).

## Caveats

The book explicitly states this is a speculative sleeve, not a core strategy — the safer, lower-cost alternative offered in the same chapter is simply holding Treasury bills (which rise in relative value as deflation deepens) or a reverse index fund (no time decay). No backtested win rate, sample size, or drawdown statistics are given; the 30% cited win rate is a single fictionalized example, not a study. The no-stop-loss rule (13/15 in the book's own numbering) is a deliberate design choice specific to this small, capped-size sleeve and should not be generalized to position-sized equity or futures trading, where stops typically remain the primary risk control. All dollar and percentage thresholds (contract cost, allocation cap) reflect 2002-era option pricing and premium levels and may need scaling for a different volatility or market-cap environment.
