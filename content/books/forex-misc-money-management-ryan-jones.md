---
title: "The Trading Game: Playing by the Numbers to Make Millions"
author: Ryan Jones
year: 1999
slug: forex-misc-money-management-ryan-jones
tier: A
category: Money Management & Position Sizing
tags: [money-management, position-sizing, fixed-ratio, fixed-fractional, futures, risk-of-ruin, drawdown-control]
difficulty: intermediate
doc_type: book
pages: 115
one_liner: "Introduces Fixed Ratio position sizing (the delta formula) and mathematically dismantles Fixed Fractional and Optimal f sizing as its rivals."
related: [balsara-nauzer-j-money-management-strategies-for-futures-traders, curtis-faith-way-of-the-turtle, the-complete-turtletrader-the-legend-the-lessons-the-results, money-management-report-van-tharp, position-sizing]
source_file: "Forex Misc - Money Management - Ryan Jones.pdf"
---

## Overview

Ryan Jones, a futures broker and money-management researcher, wrote this book around a single claim: in leveraged trading, how many contracts or shares you put on the next trade drives the great majority of an account's long-run outcome — far more than the entry system or the market traded. The book opens by narrowly defining "proper" money management as the sizing decision alone, distinct from stop placement, entries and exits (which Jones calls trade or risk management), and from tactics like pyramiding and cost averaging that are commonly mislabeled as money management. It then works through every common Fixed Fractional variant (one-contract-per-$X, Optimal f, "risk 2-3% per trade") with worked numeric examples, shows why each either grows too slowly or risks catastrophic drawdowns, and proposes Jones's own alternative, Fixed Ratio, built around a single tunable constant he calls delta. Later chapters extend Fixed Ratio to stock trading, multi-market portfolios, drawdown-triggered risk cuts, and capital allocation for professional managers.

## Core thesis

Money management, not the trading system, is responsible for the bulk of an account's profit — Jones estimates roughly 90% in his opening illustration. Any workable sizing method must be antimartingale (bet size rises with equity and falls with losses) and must address risk and reward together; every Fixed Fractional variant fails this test because it either compounds fast but exposes the account to ruinous drawdowns (aggressive per-contract divisors, Optimal f) or compounds so slowly it barely matters (2-3%-per-trade rules, common at fund size). Fixed Ratio resolves the trade-off by requiring an ever-larger but proportionally consistent profit increment to add each new contract, keeping early-stage risk low while letting growth accelerate later, once the account can better absorb a drawdown.

## Key concepts

- **Money management (narrow definition)** — strictly how much equity to risk on the next trade; excludes stop placement, entries/exits, and pyramiding.
- **Antimartingale sizing** — position size increases as equity increases and decreases as equity falls; opposite of a martingale (bet more after a loss).
- **Fixed Fractional trading** — risking a fixed percentage of equity, or one contract per fixed dollar amount; umbrella term covering Optimal f, Secure f, and "risk 2-3% per trade."
- **Optimal f** — Ralph Vince's formula for the capital fraction that maximizes geometric growth for a given trade sequence; Jones shows it implies theoretical drawdowns well past 50%.
- **Fixed Ratio** — the profit required to add the next contract grows in fixed proportion to the number of contracts already held.
- **Delta** — the sole variable in the Fixed Ratio formula; smaller is more aggressive (faster contract increases), larger is more conservative.
- **Asymmetrical leverage** — a loss requires a disproportionately larger percentage gain to recover (a 50% loss needs a 100% gain), eroding over-aggressive Fixed Fractional accounts.
- **Risk of ruin** — the probability of losing a defined fraction of capital before hitting a target; central to Jones's rejection of aggressive Fixed Fractional variants.
- **Rate of decrease** — the drawdown-response overlay: cut trading-unit size as equity falls, restore it as equity recovers.
- **Cost averaging and pyramiding** — classified as trade-management, not money-management, techniques; mostly discouraged for leveraged instruments outside narrow cases.
- **Market weighting** — allocating a different delta per market by its own expected drawdown, applied only after core money management.

## Rules and setups

This is a position-sizing book: it takes entry and exit signals as given from any existing trading method. Its concrete, reproducible numbers:

1. **Fixed Ratio level formula**: previous required equity + (number of contracts held × delta) = the equity level at which the next contract is added.
2. **Choosing delta**: Jones's rule of thumb sets delta near half the market's expected worst-case per-contract drawdown (e.g., an expected $10,000 max drawdown suggests roughly a $5,000 delta); smaller deltas trade more aggressively.
3. **Estimating the pace of contract growth**: delta ÷ average trade profit ≈ average number of trades between contract increases.
4. **Boundary formula for N contracts**: [(N × N ± N) ÷ 2] × delta gives the lower/upper profit boundary of the range in which N contracts are traded.
5. **Drawdown-to-delta ratio**: dividing an expected dollar drawdown by delta gives the maximum number of contract "levels" the account will fall during that drawdown, independent of where in the sequence it strikes.
6. **Stock and portfolio adaptation**: starting balance must include a margin buffer so margin requirements never outrun the Fixed Ratio schedule; the book works this through for $25-$100 stocks traded in 1-, 10- and 100-lot units.
7. **Rate of decrease**: for every 10% drawdown in account equity, cut trading-unit risk by 20% (e.g., 2.0% → 1.6% → 1.28%); restore size only as equity recovers.

## Risk and money management

Beyond delta selection, Jones's main risk control is the rate-of-decrease rule above. He runs the same bounded drawdown scenario (a $1,000-$2,000 largest loss per contract) through several Fixed Fractional variants and Fixed Ratio at comparable capital: one-contract-per-$10,000 destroys 51-66% of the account on that drawdown; "risk 2-3% per trade" only loses 8-27% but grows so slowly a small account may wait years to add a second contract; Fixed Ratio at a matched delta produces materially smaller percentage drawdowns for equal or larger total profit. He is explicit, however, that this edge narrows and can reverse at large fund size — a big Fixed Fractional account can add near-fractional position sizes and approach true geometric compounding in a way a small account cannot, which is why the closing chapters treat CTA-scale capital allocation as a separate problem.

## Psychology and discipline

Jones frames money management as a "numbers game" precisely to remove discretion: judgment calls about the "right" percentage to risk, adding to losers (cost averaging), or skipping trades after a losing streak cannot be mathematically justified and should be replaced by one tested, mechanical formula applied without exception. He presents this as psychologically easier than trade timing, since delta and current equity dictate contract count without a decision in the moment. He is candid that most traders — even institutional accounts — chronically under-apply money management out of fear of drawdowns, illustrating the cost with an anecdote about a trader who delayed adopting position-sizing software for a year and, by his estimate, left roughly $530,000 in additional profit on the table.

## Chapter map

1. Why? What? Where? When? Who? How? — the case that money management drives the bulk of trading profit.
2. Why (Proper) Money Management? — narrow definition versus stops, entries, and pyramiding.
3. Types of Money Management — Fixed Fractional variants, Optimal f, cost averaging, pyramiding compared.
4. Practical Facts — drawdown math, largest-loss statistics, asymmetrical leverage.
5. Fixed Fractional Trading — full breakdown of its growth-versus-risk trade-offs.
6. Fixed Ratio Trading — the delta formula and its extension to stocks and portfolios.
7. Rate of Decrease — the drawdown-triggered unit-size-cutting overlay.
8. Portfolios — applying Fixed Ratio across several simultaneous markets.
9. Market Weighting — allocating delta unevenly by expected drawdown.
10. Market Weighting through Money Management, Not before It — correct sequencing.
11. Other Profit-Protecting Measures — additional drawdown and profit-lock techniques.
12. Risk of Ruin — probability-of-ruin math applied to both sizing families.
13. The System — combining a full trading system with Fixed Ratio end to end.
14. Optimization — pitfalls of curve-fitting delta alongside system parameters.
15. Commodity Trading Advisors (CTAs) and Money Management — capital allocation for fund managers.
16. Money Management Marriage — reconciling large-fund constraints with Fixed Ratio's edge.
17. Putting It All Together — implementation summary.

## Strengths and caveats

The delta formula is fully specified and worked with real numbers across futures, stocks, and multi-market portfolios — unusually rigorous for the genre, showing the algebra rather than asserting conclusions. That said, dollar figures, margins, and contract values are late-1990s futures pricing and need re-deriving for current markets. Jones's drawdown comparisons favor Fixed Ratio using selected, bounded-loss scenarios rather than a full simulation across trade sequences, so the "always superior" framing deserves skepticism at aggressive delta choices or fat-tailed loss distributions. His claim of Fixed Ratio's edge is explicitly walked back for large funds in the later chapters, worth reading before applying the method at scale. His narrow definition of money management (excluding stops, pyramiding, and trade-skipping rules) is a deliberate choice, not an industry consensus — other authors define the term more broadly.

## Who should read it

Futures and forex traders who already have a profitable entry/exit method and want a mechanical, mathematically explicit position-sizing overlay for it. Also useful as a rigorous counterpoint to the Fixed Fractional and Optimal f approaches covered elsewhere in this library.

## Related books in this library

- [[balsara-nauzer-j-money-management-strategies-for-futures-traders]] — covers Optimal f and risk of ruin in more statistical depth; a useful counterpoint to Jones's dismissal of Fixed Fractional.
- [[curtis-faith-way-of-the-turtle]] — the Turtles used a related but distinct volatility-based (N/ATR) sizing approach; a good contrast in philosophy and mechanics.
- [[the-complete-turtletrader-the-legend-the-lessons-the-results]] — another antimartingale, volatility-scaled sizing method built into a complete trading system.
- [[money-management-report-van-tharp]] — Van Tharp's broader definition of position sizing, including the fixed-fractional variants Jones critiques.
- [[position-sizing]] — a shorter treatment of the same core sizing problem, useful for comparison.
