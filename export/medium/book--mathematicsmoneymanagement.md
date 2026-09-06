# The Mathematics of Money Management: the trader's summary

*Derives optimal f mathematically from trade history, the TWR/geometric-mean framework, and why the best-growing fraction also produces the worst drawdowns.*

**Ralph Vince** · 1992 · Money Management & Position Sizing · advanced

*Source coverage: partial. PDF pages inspected: 2-3, 7, 14-15, 53 (the HPR/TWR definitions, the optimal-f derivation and the worked geometric-growth tables). These are study notes, not verified trading results.*

## Overview

Vince's follow-up to *Portfolio Management Formulas* is a pure math text: no chart patterns, no entries, no indicators. Its subject is what fraction of an account to commit to a trade stream that already has a positive expectancy. The book builds from empirical techniques (Ch. 1-2, using raw trade histories) to parametric techniques (Ch. 3-4, fitting distributions so the same math runs on assumed or fitted curves, not only historical trades). The throughline is optimal f: the single fixed fraction of capital, reinvested trade after trade, that maximizes an account's long-run geometric growth rate. The geometric mean, Terminal Wealth Relative (TWR), the Kelly formulas, drawdown severity, and portfolio-level allocation are all by-products of that one number.

## Core thesis

Trading returns compound multiplicatively, not additively, so a money-management decision must be judged by its effect on geometric, not arithmetic, growth. For a trade stream with positive mathematical expectation, exactly one fixed fraction of equity — optimal f — maximizes the terminal wealth of reinvesting the account trade after trade. Betting more than optimal f reduces long-run return even though each bet still has positive expectancy; betting less also costs return, just more forgivingly. Optimal f is not a percentage of equity to risk — it is the divisor of the single biggest losing trade in the history, and its dollar-per-contract value tells a trader how many contracts to hold. The book's recurring corollary: the better a system's optimal f, the deeper its historical drawdown, because the worst historical loss at the optimal fraction always produces a retracement of at least f percent of equity. There is no way to keep optimal f's growth benefit without its drawdown penalty; diversification buffers this but never eliminates it.

## Key concepts

- **HPR (Holding Period Return)** — 1 plus a trade's percentage gain or loss; a +10% trade is HPR 1.10, a -10% trade is HPR 0.90.
- **TWR (Terminal Wealth Relative)** — the product of all HPRs in a sequence; final stake divided by starting stake under full reinvestment.
- **Geometric mean (G)** — the Nth root of the TWR (N = trades); the "growth factor per play." Systems are compared by G, not win rate, average trade, or total profit.
- **Optimal f** — the fraction (0-1) of the biggest historical loss that, scaling every trade's HPR, produces the highest TWR/geometric mean.
- **Market system** — a synthetic construct: one approach on one market, on a strict 1-unit basis so f can be computed and scaled.
- **Mathematical expectation** — average amount won/lost per trade; must be positive or no money management helps.
- **Kelly formulas** — f = 2P-1 (equal win/loss size) or f = ((B+1)P-1)/B (payoff ratio B, win probability P); valid only for Bernoulli (fixed two-outcome) distributions, which trading is not.
- **Geometric Average Trade (GAT)** — (G-1) × (biggest loss ÷ -f); expected $ profit per contract per trade under fixed-fractional trading.
- **Threshold to the geometric** — the point where reinvesting starts to beat not reinvesting; below it, or above too high an f, reinvestment can turn a winner into a loser.
- **Dependency (runs test, serial correlation)** — checks for whether wins/losses cluster; if present at high confidence, split into after-win/after-loss sub-systems, each with its own f.
- **Estimated Geometric Mean (EGM)** — √(AHPR² - variance of HPRs); ranks candidate portfolio allocations without recomputing full TWRs.
- **Efficient frontier / CPA** — Markowitz's non-dominated portfolio weightings; the Combination Product Allocation with the highest EGM is the optimal-f portfolio.
- **Risk of ruin** — the asymptotic certainty of losing everything trading an unlimited-liability instrument indefinitely; the book's case for a pre-committed equity ceiling.

## Rules and setups

Vince's book has no market timing rules; the "system" is entirely about position sizing given an existing trade history. See the [Optimal f and the TWR/Geometric Mean Framework](https://ninad-k.github.io/trading-playbook/books/mathematicsmoneymanagement--optimal-f-and-twr-framework.html) sub-page for the exact formulas. Summary of the procedure:

1. Reduce every trade to a P&L on a strict 1-unit basis (1 contract, 1 share, or a defined lot); pyramided add-ons count as separate market systems.
2. Test candidate f from 0.01 to 1.00; for each f compute HPR = 1 + f × (-trade ÷ biggest loss) for every trade and the resulting TWR.
3. The f producing the highest TWR is optimal f; its Nth root is the geometric mean. Both peak at the same f.
4. Convert f to a trading unit: dollars per contract = biggest loss ÷ (-optimal f). Divide current equity by that figure (floor to integer) for contract count; recompute as equity changes.
5. For multiple systems, convert each day's $ P&L to a daily HPR relative to that system's optimal-f dollar amount, then search allocations for the combination with the highest estimated geometric mean.
6. Before trading any of this, write down the equity level at which you will stop trading unlimited-liability instruments — mandatory contingency planning, not optional.

## Risk and money management

This entire book is a risk/money-management text. Its distinctive numeric claims: historical drawdown at optimal f is never smaller than f itself as a percentage of equity (f = .55 implies a drawdown of at least 55%); a well-tested multi-system portfolio traded at optimal f should still expect 30-95% equity retracements over a 5+ year history; diversification buffers but never eliminates this, since uncorrelated systems still periodically draw down in unison. Vince's practical response is to trade a fraction of full optimal f (he cites trimming to f/2 as a common compromise, with no universal ratio prescribed) and to size the smallest-denomination market possible so allocation tracks optimal f precisely as equity changes.

## Psychology and discipline

Before any math, the book instructs the reader to write out a worst-case contingency plan — what to do, who to call, and at what equity level to stop trading unlimited-liability instruments — and put it in a drawer before reading further. Vince's argument: money management only works on top of discipline most traders cannot sustain; optimal f is "plutonium" — tremendous growth power paired with the ability to produce a catastrophic, career-ending drawdown if a trader can't stay with it through the trough. He also warns against averaging win/loss sizes into the Kelly formula (this understates true optimal f) and against assuming dependency between trades without a very high statistical confidence level, since a wrong assumption of dependency is the costlier mistake.

## Chapter map

- Ch 1 — The Empirical Techniques — HPR/TWR/geometric mean, dependency testing (runs test, serial correlation), mathematical expectation, Kelly formulas and their Bernoulli-only validity, finding optimal f by geometric-mean search, severity of drawdown, Markowitz portfolio theory reworked with optimal f.
- Ch 2 — Fixed Fractional Trading Characteristics — optimal f for small accounts, threshold to the geometric, combined vs. separate bankrolls, time to reach a goal, comparing systems, sensitivity to the biggest loss, equalizing f, Arc Sine Laws and time in drawdown.
- Ch 3 — Parametric Optimal f on the Normal Distribution — distribution basics and moments, the Normal and Lognormal distributions, deriving optimal f from distribution parameters instead of raw trade lists.
- Ch 4 — Parametric Techniques on Other Distributions — Kolmogorov-Smirnov test, building a custom distribution function, fitting parameters, scenario planning, optimal f on binned/empirical data, choosing among candidate f's.
- Appendices — Bernoulli/Binomial distribution and significance testing; other common distributions and finding optimal f on them; further dependency tests (turning points, phase length).

## Strengths and caveats

The math is rigorous and largely self-contained, and the book is candid that its worked examples assume fractional contracts and continuous reinvestment — real integer-lot trading lags the theoretical TWR, especially for small accounts. Vince is explicit this is a book about sizing, not signal generation, and repeatedly claims system profitability barely matters once a marginal edge exists — counterintuitive to some, and it assumes the edge stays stable out of sample, never guaranteed. The drawdown-severity argument is the book's own biggest caveat: full optimal f is mathematically correct but often psychologically and financially unsurvivable, and Vince gives no formal rule for how much to dilute f beyond noting the trade-off is geometric, not linear. The parametric chapters (3-4) need comfort with probability theory and curve-fitting most discretionary traders won't use directly; they matter mainly for quants automating the empirical technique.

## Who should read it

Systematic and quantitative traders, and CTAs or fund managers who already have a positive-expectancy system and need a rigorous, math-first framework for position sizing and portfolio allocation across multiple systems. Not useful as a source of entries or trading rules, and too dense in probability theory for a trader who only wants a rule of thumb — for that, [Money Management Strategies for Futures Traders](https://ninad-k.github.io/trading-playbook/books/balsara-nauzer-j-money-management-strategies-for-futures-traders.html) packages similar optimal-f math with more accessible worked examples.

## Related books in this library

- [Money Management Strategies for Futures Traders](https://ninad-k.github.io/trading-playbook/books/balsara-nauzer-j-money-management-strategies-for-futures-traders.html) — a more approachable, worked-example treatment of the same optimal-f and Kelly math applied directly to futures position sizing.
- [A New Interpretation of Information Rate](https://ninad-k.github.io/trading-playbook/books/kellybetting.html) — Kelly's original 1956 paper deriving the criterion Vince builds on and explicitly departs from for non-Bernoulli trading outcomes.
- [A New Interpretation of Information Rate](https://ninad-k.github.io/trading-playbook/books/kellybetting.html) — a further technical treatment of the Kelly criterion useful for comparing against Vince's optimal-f generalization.
- [Position-Sizing Effects on Trader Performance: An Experimental Analysis](https://ninad-k.github.io/trading-playbook/books/position-sizing.html) — a shorter, practitioner-oriented look at position sizing effects on trading performance, a useful counterpoint to this book's academic depth.
- [Trade Your Way to Financial Freedom](https://ninad-k.github.io/trading-playbook/books/trade-your-way-to-financial-freedom.html) — Van Tharp's position-sizing framework, a less mathematically demanding alternative approach to the same core problem.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: optimal-f, kelly-criterion, twr, geometric-mean, drawdown, portfolio-theory, position-sizing, money-management
