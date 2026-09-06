# Money Management Strategies for Futures Traders: the trader's summary

*An academic but practitioner-oriented treatment of risk of ruin, fixed-fractional and optimal-f position sizing, diversification, and capital allocation across futures trades.*

**Nauzer J. Balsara** · 1992 · Money Management & Position Sizing · advanced

*Source coverage: partial. PDF pages inspected: 1-3, 6, 84, 115, 137 (contents, the risk-of-ruin and payoff-ratio chapters, fixed-fraction exposure and the optimal-f allocation sections). These are study notes, not verified trading results.*

## Overview

Balsara (a finance professor) treats money management as a distinct discipline separate from signal generation: given that a trading signal has fired, how much should be risked, how many contracts should be traded, and how should capital be allocated when several opportunities compete for the same funds? The book moves from the mathematics of ruin, through chart-based risk/reward estimation, portfolio diversification and commodity selection, stop-setting, fixed-fractional and Kelly/optimal-f exposure sizing, capital allocation across multiple commodities (including modern portfolio theory and pyramiding), and finishes with a critique of mechanical systems and a chapter on the psychology of loss. It is one of the more rigorous, formula-driven treatments of futures money management, with worked numerical examples and appendices containing programs and full risk-of-ruin tables.

## Core thesis

Signal generation (deciding when to buy or sell) and money management (deciding how much) are separate problems, and most trading failure comes from getting the second one wrong even when the first is sound. The probability of ruin is a precise, computable function of three things — probability of trading success, the payoff ratio (average win ÷ average loss), and the fraction of capital exposed per trade — and only the third is under the trader's direct control. Because of this, disciplined, formula-based control of exposure (not signal quality alone) is what separates traders who survive long enough to let a positive-expectancy system work from those who don't.

## Key concepts

- **Risk of ruin (R)** — the probability that a trader's equity is depleted to the point where trading must stop; a function of probability of success (p), payoff ratio (A), and the fraction of capital exposed per trade.
- **Payoff ratio** — the ratio of the average dollar win to the average dollar loss; a payoff ratio of 2 means winners average twice the size of losers.
- **Fixed-fractional exposure** — always risking a constant fraction (not dollar amount) of the current bankroll, so bet size shrinks after losses and grows after wins; formula for the probability-only case: f = p − (1 − p).
- **Optimal f / Kelly criterion** — the fraction of capital that maximizes long-run (geometric) growth of the bankroll, incorporating both win probability and payoff ratio: f = [(A + 1)p − 1] / A.
- **Modified Kelly system** — applies the Kelly formula per-trade using trade-specific projected risk/reward and probability rather than a single historical average across all trades.
- **Terminal Wealth Relative (TWR)** — Ralph Vince's iterative method for finding the empirically optimal f from a historical series of trade returns, by testing candidate f values and picking the one that maximizes compounded terminal wealth.
- **Martingale vs. anti-Martingale** — Martingale doubles bet size after a loss (recovers losses on the next win but risks ruin during a losing streak); anti-Martingale doubles after a win and resets to one unit after a loss (lower risk, higher long-run profit potential when the system has positive expectancy).
- **Effective exposure / assured unrealized profit** — the dollar amount genuinely at risk on an open trade, computed from entry price, current stop, and position size; turns negative (locked-in profit) once the stop is moved past breakeven.
- **Pyramiding** — adding contracts to an already-profitable position, financed by reinvesting a chosen fraction (p, 0 to 1) of the assured (locked-in) unrealized profit; never advised for averaging into a losing position.
- **Correlation-based diversification** — combining commodities whose returns are not strongly positively correlated reduces aggregate portfolio risk without proportionally reducing expected return; positively correlated commodities should generally not be traded concurrently at full size.
- **The Shame Ratio / Commodity Selection Index (CSI)** — Wilder's CSI and related indices used to rank which of several signaled opportunities is most worth taking when capital is limited.
- **Four-star blunder** — Balsara's escalating error taxonomy (one-star: exiting a winner too early; two-star: missing a big winner entirely; three-star: refusing to cut a losing trade; four-star: the three-star error magnified by overexposure to a single commodity) used to frame why exposure control matters more than being "right."
- **Expected profit per trade** — p(W) − (1 − p)L (projected form) or [p(A + 1) − 1] (historical-average form); a trade or system with negative expected profit should not be traded regardless of any money-management overlay.

## Rules and setups

Balsara gives no chart patterns or entry signals of his own (Chapter 3's head-and-shoulders/triangle/flag examples are for risk/reward *estimation*, borrowed from Edwards and Magee, not entry rules); the book's rules are entirely about sizing, allocation, and exit management once a signal exists:

1. **Fixed-fraction sizing (probability only, payoff ratio = 1)**: risk fraction f = p − (1 − p), where p is the historical win rate. A system must clear p > 0.51 to justify any exposure under this simplified formula; at p = 0.50 the formula recommends 0% exposure.
2. **Optimal f / Kelly sizing (with payoff ratio)**: f = [(A + 1)p − 1] / A, where A is the payoff ratio. Worked example: p = 0.33, A = 5 → f = 0.20 (risk 20% of capital).
3. **Trade-specific optimal f (projected risk/reward)**: compute A = expected win ÷ permissible loss for the specific trade; compute expected value = (p × A) − ((1−p) × 1); then f = expected value ÷ A. Worked example: risking 8¢ to make 20¢ on a trade with p = 0.45 gives A = 2.50, expected value = 0.575, f ≈ 23%.
4. **Historic-returns (Vince/TWR) method**: divide each historical trade's return by the worst losing trade's return (negated) to get a weighted holding-period return as a function of candidate f; multiply across all trades to get TWR(f); the f that maximizes TWR is the empirically optimal fraction to risk on the next trade.
5. **Aggregate exposure across multiple commodities (F)**: for a multi-commodity portfolio, compute the geometric average joint return per round of trades across commodities, then apply the same TWR-maximization procedure to find the aggregate exposure fraction F (not a simple sum of individual f's, since that ignores correlation and can exceed 100%).
6. **Cap on single-trade exposure**: whatever f or F recommends, an investor-set maximum percentage per single commodity should override the formula's recommendation if the formula's output exceeds that cap.
7. **Number of contracts to trade**: compute both a margin-based estimate (capital allocated ÷ initial margin per contract) and a risk-based estimate (risk capital allocated ÷ permissible risk per contract); trade the *lower* of the two so neither the margin nor the risk constraint is violated. Round fractional contracts down; if the recommended size is under one contract, either skip the trade or replicate it with an options position of equivalent delta.
8. **Pyramiding formula**: additional contracts = (p × assured unrealized profit × current number of contracts) ÷ permissible loss per contract, where p (0 to 1) is the fraction of locked-in profit the trader chooses to risk again. Only apply to winning positions with a locked-in (stop moved past breakeven) profit; never to average down a loser.
9. **Risk-of-ruin control procedure**: given an estimated p and payoff ratio, use the risk-of-ruin tables (or simulate) to read off the risk of ruin at a candidate exposure level; if unacceptable, reduce the exposure fraction (equivalently, increase the number of "units" of capital, k) until the risk of ruin falls to an acceptable level — the book's example shows going from 50% to 33.33% exposure cuts risk of ruin roughly in half at p=0.60, payoff ratio 2 (0.208 → 0.095).
10. **Stop-setting menu** (Ch. 6): visual chart-based stops (beyond a pattern's invalidation point), volatility stops (a multiple of recent average range/ATR beyond entry), time stops (exit if no favorable move within N periods), and fixed dollar-value money-management stops — chosen per trade based on which best fits the setup, not a single universal rule.
11. **Expected-profit screen**: before taking a trade, compute expected profit = p(W) − (1−p)L (or the historical-average equivalent); do not trade signals with zero or negative expected profit, with the single exception of a trade in a market negatively correlated with an existing position, where the portfolio-level allocation math can still justify it.

## Risk and money management

This entire book is about risk and money management; the two central quantitative tools are the risk-of-ruin formula/simulation tables (Chapter 2, with a full appendix of tables by probability of success, payoff ratio, and capital-exposure fraction) and the optimal-f/Kelly family of sizing formulas (Chapter 7), extended to multi-commodity portfolios via modern portfolio theory and the geometric-joint-return TWR method (Chapter 8). Key numeric findings: for a payoff ratio of 2, risk of ruin is certain (R=1) whenever the probability of winning is ≤ one-third of the probability of losing (p ≤ 0.33); reducing exposure from 50% to 20% of capital at p=0.60/payoff-ratio=2 cuts risk of ruin from 0.209 to 0.020. The percentage profit needed to recoup a percentage loss L is 1/(1−L) − 1 — a 50% loss requires a 100% gain to recover, and a 90% loss requires a 900% gain, which is the book's core argument for why avoiding "four-star blunders" (large single-commodity overexposure) matters more than any single trade's edge.

## Psychology and discipline

Chapter 10 catalogs the emotional aftermath of a loss and the behavioral traps that follow it: trading more frequently (dropping to shorter timeframes to "react faster"), trading more extensively (adding commodities to force more opportunities), taking riskier positions (chasing volatile markets to recoup losses quickly), despair-induced paralysis (quitting after a losing streak), selectively overriding a system's signals, and system-switching in search of a "perfect system." Balsara's prescriptions: treat back-to-back trades as statistically independent (he demonstrates this with a runs test on real system trades across three commodities, all non-significant at the 1% level, meaning wins and losses were not clustered/patterned); always screen trades on positive expected profit rather than on the emotional pull of a recent win or loss streak; and accept that errors of judgment are inevitable — the trader's job is to recognize them promptly and limit their financial consequences (avoid four-star blunders), not to avoid ever being wrong.

## Chapter map

- Ch 1 — Understanding the Money Management Process — ranking opportunities, controlling overall exposure, allocating risk capital, the risk equation.
- Ch 2 — The Dynamics of Ruin — inaction/incorrect action, the risk-of-ruin formula, simulated risk-of-ruin tables.
- Ch 3 — Estimating Risk and Reward — chart-pattern-based risk/reward estimation (head-and-shoulders, double tops, triangles, wedges, flags).
- Ch 4 — Limiting Risk through Diversification — measuring trade return and risk, correlation across commodities, limits of diversification.
- Ch 5 — Commodity Selection — ranking competing signals (Shame Ratio, Wilder's Commodity Selection Index, Price Movement Index, Adjusted Payoff Ratio Index).
- Ch 6 — Managing Unrealized Profits and Losses — visual, volatility, time, and dollar-value stops; bull/bear traps; surviving locked-limit markets.
- Ch 7 — Managing the Bankroll: Controlling Exposure — equal-dollar exposure, fixed-fraction exposure, optimal f / modified Kelly, Martingale vs. anti-Martingale.
- Ch 8 — Managing the Bankroll: Allocating Capital — equal-dollar, MPT-based, and optimal-f-based capital allocation across commodities; contracts-to-trade formula; pyramiding.
- Ch 9 — The Role of Mechanical Trading Systems — predictive vs. reactive systems, moving-average crossover and stochastics examples, why fixed-parameter systems drift out of tune.
- Ch 10 — Back to the Basics — four-star blunders, the emotional aftermath of loss, maintaining emotional balance, expected-profit screening.
- Appendices — Pascal/BASIC programs to compute risk of ruin; correlation data and dollar-risk tables for 24 commodities; opening-price analysis; mathematical statement of the optimal-portfolio-weights problem.

## Strengths and caveats

The formulas are precise, fully worked with numbers, and directly codeable — a real strength versus most money-management chapters that stay qualitative. The risk-of-ruin tables and optimal-f derivations rest on simplifying assumptions the book states plainly: constant probability of success and payoff ratio across trades (rarely exactly true in live trading, and the book's own Chapter 9 shows these measures drift as market conditions change), independence between trades, and (for the precise ruin formulas) a payoff ratio of exactly 1 or exactly 2 — anything else requires simulation. The multi-commodity portfolio-optimization approach (Ch. 8) borrows directly from Markowitz mean-variance portfolio theory and assumes a stable opportunity set and stable correlations, which the author himself flags as more suited to a longer-term position trader than a short-term futures trader facing a constantly changing opportunity set. The book predates modern computing power (BASIC/Pascal appendix programs, 24-commodity correlation tables computed by hand-era software) and its numeric examples are 1980s-era futures and margin levels, but the underlying mathematics (Kelly/optimal f, risk of ruin, TWR) is timeless and still the standard reference framework used across later money-management writing.

## Who should read it

Systematic and discretionary futures/derivatives traders who already have a signal-generation method and want a rigorous, formula-based framework for position sizing, risk-of-ruin control, and multi-market capital allocation; also useful as a primer on the Kelly criterion and optimal-f before reading Ralph Vince's more specialized portfolio-formula books.

## Related books in this library

- [A New Interpretation of Information Rate](https://ninad-k.github.io/trading-playbook/books/kellybetting.html) — Kelly's original 1956 paper, the source of the optimal-f/Kelly formula this book builds its exposure-sizing chapter around.
- [Position-Sizing Effects on Trader Performance: An Experimental Analysis](https://ninad-k.github.io/trading-playbook/books/position-sizing.html) — a complementary, narrower treatment of position-sizing's effect on trader performance, useful alongside Balsara's fixed-fractional and optimal-f chapters.
- [Special Report on Money Management](https://ninad-k.github.io/trading-playbook/books/money-management-report-van-tharp.html) and [What Is a Trading System?](https://ninad-k.github.io/trading-playbook/books/van-tharp-trading-systems.html) — Van Tharp's parallel position-sizing and system-design framework, a useful second perspective on the same core problem.
- [The Trading Game: Playing by the Numbers to Make Millions](https://ninad-k.github.io/trading-playbook/books/forex-misc-money-management-ryan-jones.html) — an alternative (non-Kelly) fixed-ratio position-sizing scheme worth contrasting with Balsara's optimal-f approach.
- [Money Management and Risk Control for Traders](https://ninad-k.github.io/trading-playbook/books/money-management-risk-control-for-traders.html) and [Fine-Tuning Your Money Management System](https://ninad-k.github.io/trading-playbook/books/fine-tuning-your-money-management.html) — shorter, more applied companion pieces on the same risk-control themes.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: risk-of-ruin, optimal-f, kelly-criterion, fixed-fractional, position-sizing, diversification, pyramiding
