---
title: The Mathematics of Money Management
author: Ralph Vince
year: 1992
slug: mathematicsmoneymanagement
tier: A
category: Money Management & Position Sizing
tags: [optimal-f, kelly-criterion, twr, geometric-mean, drawdown, portfolio-theory, position-sizing, money-management]
difficulty: advanced
doc_type: book
pages: 106
one_liner: "Derives optimal f mathematically from trade history, the TWR/geometric-mean framework, and why the best-growing fraction also produces the worst drawdowns."
related: [balsara-nauzer-j-money-management-strategies-for-futures-traders, a-new-interprtation-of-information-rate-kelly, kellybetting, position-sizing, trade-your-way-to-financial-freedom]
source_file: "MathematicsMoneyManagement.pdf"
---

## Overview

Vince's follow-up to *Portfolio Management Formulas* is a pure math text: no chart patterns, no entries, no indicators. Its subject is what fraction of an account to commit to a given trade stream once that stream already has a positive expectancy. The book builds from empirical techniques (Chapter 1-2, using raw trade histories) to parametric techniques (Chapters 3-4, fitting distributions so the same math can be run on assumed or fitted curves rather than only historical trades). The throughline is optimal f: the single fixed fraction of capital, reinvested trade after trade, that maximizes the long-run geometric growth rate of an account. Everything else in the book — the geometric mean, Terminal Wealth Relative (TWR), the Kelly formulas, drawdown severity, and portfolio-level allocation — is a by-product or a generalization of that one number.

## Core thesis

Trading returns compound multiplicatively, not additively, so any money-management decision has to be judged by its effect on geometric (not arithmetic) growth. For a stream of trades with a positive mathematical expectation, there exists exactly one fixed fraction of equity — optimal f — that maximizes the terminal wealth of reinvesting the account trade after trade. Betting more than optimal f reduces long-run return even though each individual bet still has positive expectancy; betting less also reduces return, just more forgivingly. Optimal f is not a percentage of equity to risk — it is the divisor of the single biggest losing trade in the history, and its dollar-per-contract value is what tells a trader how many contracts to hold. The corollary the book insists on repeatedly: the better a system's optimal f, the deeper its historical drawdown, because the worst historical loss at the optimal fraction always produces a retracement of at least f percent of equity. There is no way to have the growth benefits of optimal f without also accepting its drawdown penalty; diversification buffers this but never eliminates it.

## Key concepts

- **HPR (Holding Period Return)** — 1 plus a trade's percentage gain or loss; a +10% trade is HPR 1.10, a -10% trade is HPR 0.90.
- **TWR (Terminal Wealth Relative)** — the product of all HPRs in a sequence; final stake divided by starting stake, assuming full reinvestment.
- **Geometric mean (G)** — the Nth root of the TWR (N = number of trades); the "growth factor per play." A system is compared to others by G, not by win rate, average trade, or total profit.
- **Optimal f** — the fraction (0 to 1) of the biggest historical loss that, when used to scale every trade's HPR, produces the highest TWR/geometric mean.
- **Market system** — a synthetic construct: one trading approach on one market, calculated on a strict 1-unit (1 contract/1 share/1 lot) basis so f can be computed and then scaled.
- **Mathematical expectation** — the average amount won or lost per trade/bet; the necessary (not sufficient) condition for any money management to help is that this be positive.
- **Kelly formulas** — f = 2P-1 (equal win/loss size) or f = ((B+1)P-1)/B (payoff ratio B, win probability P); valid only for Bernoulli (two-outcome, fixed-size) distributions, which trading is not.
- **Geometric Average Trade (GAT)** — G-1 times (biggest loss ÷ -f); the expected dollar profit per contract per trade under fixed-fractional trading.
- **Threshold to the geometric** — the point at which reinvesting returns starts to beat not reinvesting; below this equity or above too high an f, reinvestment can turn a winning system into a loser.
- **Dependency (runs test, serial correlation)** — statistical checks for whether wins/losses cluster; if present at high confidence, a system should be split into after-win and after-loss sub-systems, each with its own optimal f.
- **Estimated Geometric Mean (EGM)** — √(AHPR² - variance of HPRs); lets a trader rank candidate portfolio allocations without recomputing full TWRs.
- **Efficient frontier / CPA (Combination Product Allocation)** — Markowitz's set of portfolio weightings with no dominated alternative; the CPA with the highest EGM is the one optimal-f portfolio to hold.
- **Risk of ruin** — the asymptotic certainty of losing everything when trading an unlimited-liability instrument for an unlimited length of time; the book's argument for pre-committing an equity ceiling at which to stop.

## Rules and setups

Vince's book has no market timing rules; the "system" is entirely about position sizing given an existing trade history. See the [[mathematicsmoneymanagement--optimal-f-and-twr-framework]] sub-page for the exact formulas. Summary of the procedure:

1. Reduce every trade in the market system's history to a P&L on a strict 1-unit basis (1 contract, 1 share, or a defined lot size); pyramided add-ons count as separate market systems.
2. Test candidate f values from 0.01 to 1.00 in increments; for each f compute the sequence of HPR = 1 + f × (-trade ÷ biggest loss) and the resulting TWR.
3. The f producing the highest TWR is optimal f; take its Nth root for the geometric mean. Both TWR and G peak at the same f, so either can be used as the search target.
4. Convert f to a trading unit: dollars per contract = biggest loss ÷ (-optimal f). Divide current equity by that figure (floor to an integer) to know how many contracts/shares to hold; recompute daily as equity changes.
5. For multiple market systems, convert each day's dollar P&L to a daily HPR relative to that system's optimal-f dollar amount, then search percentage allocations across systems for the combination with the highest estimated geometric mean (the efficient frontier's optimal point).
6. Before trading any of this, write down the equity level at which you will "quit trading unlimited-liability vehicles altogether" — Vince frames this as mandatory contingency planning, not optional.

## Risk and money management

This entire book is a risk/money-management text, so the material above largely is the risk section. Its distinctive numeric claims: historical drawdown at optimal f is never smaller than f itself as a percentage of equity (f = .55 implies a drawdown of at least 55%); a well-tested multi-market-system portfolio traded at optimal f should still be expected to see 30-95% equity retracements over a 5+ year history; diversification buffers but never eliminates this because there will always be periods when uncorrelated systems draw down in unison. Vince's practical response is not to trade full optimal f but a fraction of it (he references trimming to f/2 as a common compromise, without prescribing a universal ratio), and to size the smallest-denomination market possible so allocation can track optimal f more precisely as equity changes.

## Psychology and discipline

The book opens, before any math, with an instruction to write out a worst-case contingency plan — what you will do, who you will call, at what equity level you will stop trading unlimited-liability instruments — and put it in a drawer before reading further. Vince's argument is that money management only works on top of the discipline to tolerate emotional pain most traders cannot sustain; optimal f is described explicitly as "plutonium" — tremendous growth power paired with the ability to produce a catastrophic, career-ending drawdown if a trader cannot stay with it through the trough. He also warns against the common trader error of averaging win/loss sizes into the Kelly formula (this understates true optimal f) and against assuming dependency between trades without a very high statistical confidence level, since wrongly assuming dependency is a more expensive mistake than wrongly assuming independence.

## Chapter map

- Ch 1 — The Empirical Techniques — HPR/TWR/geometric mean, dependency testing (runs test, serial correlation), mathematical expectation, Kelly formulas and their Bernoulli-only validity, finding optimal f by geometric mean search, severity of drawdown, an introduction to Markowitz modern portfolio theory reworked with optimal f.
- Ch 2 — Characteristics of Fixed Fractional Trading and Salutary Techniques — optimal f for small accounts, threshold to the geometric, combined vs. separate bankrolls, time to reach a goal, comparing systems, sensitivity to the single biggest loss, equalizing f across systems, the Arc Sine Laws and time spent in drawdown.
- Ch 3 — Parametric Optimal f on the Normal Distribution — probability distribution basics, moments, the Normal and Lognormal distributions, deriving optimal f and its by-products from distribution parameters instead of raw trade lists.
- Ch 4 — Parametric Techniques on Other Distributions — the Kolmogorov-Smirnov test, building a custom characteristic distribution function, fitting parameters, scenario planning and "what if" analysis, optimal f on binned/empirical data, choosing among candidate optimal f's.
- Appendices — the Bernoulli/Binomial distribution and statistical significance testing for a system; other common probability distributions (Uniform and others) and how to find optimal f on any of them; further dependency tests (turning points, phase length).

## Strengths and caveats

The math is rigorous and largely self-contained, and the book is candid that its own worked examples assume fractional contracts and continuous reinvestment — real integer-lot trading will lag the theoretical TWR, especially for small accounts. Vince is explicit that this is a book about sizing, not signal generation, and repeatedly states that system profitability barely matters once a marginal positive edge exists — a claim that some traders will find counterintuitive and that assumes the edge is genuinely stable out of sample, which is never guaranteed. The drawdown-severity argument is the book's most important caveat on itself: trading full optimal f is presented as mathematically correct but often psychologically and financially unsurvivable, and Vince offers no formal rule for how much to dilute f beyond noting that halving f roughly halves the drawdown while giving up a geometric (not linear) amount of return. The parametric chapters (3-4) require comfort with probability theory and curve-fitting that most discretionary traders will not use directly; they matter mainly for quants building the empirical technique into automated systems.

## Who should read it

Systematic and quantitative traders, and CTAs or fund managers who already have a positive-expectancy system and need a rigorous, math-first framework for position sizing and portfolio allocation across multiple systems. Not useful as a source of entries or trading rules, and too dense in probability theory for a trader who only wants a rule of thumb — for that, [[balsara-nauzer-j-money-management-strategies-for-futures-traders]] packages similar optimal-f math with more accessible worked examples.

## Related books in this library

- [[balsara-nauzer-j-money-management-strategies-for-futures-traders]] — a more approachable, worked-example treatment of the same optimal-f and Kelly math applied directly to futures position sizing.
- [[a-new-interprtation-of-information-rate-kelly]] — Kelly's original 1956 paper deriving the criterion Vince builds on and explicitly departs from for non-Bernoulli trading outcomes.
- [[kellybetting]] — a further technical treatment of the Kelly criterion useful for comparing against Vince's optimal-f generalization.
- [[position-sizing]] — a shorter, practitioner-oriented look at position sizing effects on trading performance, a useful counterpoint to this book's academic depth.
- [[trade-your-way-to-financial-freedom]] — Van Tharp's position-sizing framework, a less mathematically demanding alternative approach to the same core problem.
