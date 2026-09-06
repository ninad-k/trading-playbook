# Portfolio Risk Reduction: Optimising Selection of Resource Projects by Application of Financial Industry Techniques: the trader's summary

*Exploration Geophysics paper applying Markowitz portfolio theory to mineral-exploration project selection, showing that combining projects by correlation (not ranking by Expected Monetary Value alone) minimizes portfolio uncertainty.*

**Noll Moriarty** · 2001 · Money Management & Position Sizing · advanced

*Source coverage: full. PDF pages inspected: 1-5. These are study notes, not verified trading results.*

## Summary

An academic paper published in Exploration Geophysics (2001) by geophysicist Noll Moriarty, importing Harry Markowitz's financial portfolio theory into resource-exploration project selection. The question: given a capped exploration budget and several candidate projects, how should a company allocate funds to maximize expected value while minimizing the uncertainty (variance) of the total outcome? Using a worked two-project example (Project A: high chance of success, lower payoff; Project B: lower chance, higher payoff; both cost $2m), the paper shows that ranking and funding only the highest-Expected-Monetary-Value project is not optimal — splitting the budget between correlated and uncorrelated projects, weighted by their correlation coefficient, produces a lower-uncertainty portfolio for the same or better expected value. The method: quantify each project's mean outcome, standard deviation ("risk" in financial terms, distinct from geological chance-of-failure), and pairwise correlation coefficients, then use the standard portfolio-variance formula to find the efficient allocation.

## Key points

- Financial portfolio theory (Markowitz, 1952/1957) treats "risk" as the standard deviation of returns; the resource industry's "risk" (chance-of-failure) is a separate, complementary concept — geological chance is not part of the financial-portfolio calculation at all.
- Expected Value (EV) = Mean NPV x chance-of-success; Expected Monetary Value (EMV) = EV - (Failure NPV x chance-of-failure). Ranking projects by EMV alone (the conventional industry approach) is shown to be suboptimal for portfolio construction.
- Portfolio standard deviation formula for two assets: σP = √[(%A·σA)² + (%B·σB)² + 2(%A·σA)(%B·σB)·ρAB], where ρAB is the correlation coefficient between the two projects/assets.
- Worked example: Project A ($10m std dev) and Project B ($15m std dev) combined at a correlation of 0.0 produce a minimum portfolio standard deviation of $8.3m at a 70%A/30%B split — lower uncertainty than either project alone, at a comparable expected value.
- For an equal-weighted portfolio of N uncorrelated projects, portfolio uncertainty falls to σ/√N; for N correlated projects with correlation ρ, it falls to σ√[(1+ρ(N-1))/N], converging to σ√ρ as N grows large.
- Positive correlation between projects reduces the chance of exactly one success (increases chance of "all or none"); negative correlation increases the chance of exactly one success — relevant when a company only needs one success to justify a program.
- For X projects in a portfolio, X(X-1)/2 correlation coefficients are required (45 for 10 projects) — determining these is described as the paper's hardest practical problem, requiring judgment on resource size, geological similarity, cost structure, commodity-price exposure, and country risk.
- The method assumes a normal distribution of outcomes; if the true distribution is lognormal (common for both mineral deposits and financial returns), standard deviation is overestimated because of high-side outliers, so the portfolio uncertainty computed by this method is a conservative (upper-bound) estimate.

## Actionable rules

1. Do not rank exploration or investment candidates by Expected Monetary Value alone when constructing a multi-project portfolio; combining a lower-EMV but low-correlation project can lower total portfolio uncertainty for the same expected return.
2. Compute pairwise correlation coefficients (geological similarity, cost structure, commodity exposure, geography, political risk) between candidate projects before allocating budget, not just each project's standalone chance-of-success.
3. Use the two-asset portfolio standard deviation formula to solve for the allocation percentage that minimizes σP for a target expected value (the "efficient frontier" point), rather than an equal-weight or highest-EMV-first allocation.
4. If diversification's sole purpose is to raise the odds of at least one success (not to maximize total expected NPV), prefer projects with negative or low correlation, not just projects with the highest individual chance-of-success.

## Caveats

Written for a technical geophysics/resource-exploration audience; the "portfolio" is mineral exploration projects, not tradable securities, though the mathematics (and the [Volatility Matters: The Case for Investment in Resource Stocks](https://ninad-k.github.io/trading-playbook/books/resource-stocks-in-portfolio.html) companion article) apply directly to equity portfolio construction. The model assumes normally distributed outcomes and independently estimable correlation coefficients — both flagged by the author as imperfect assumptions (lognormal skew, and the practical difficulty of estimating dozens of correlations with any precision). No backtested results are given; this is a methodological/theoretical paper, not an empirical performance study.

## Who it is for

Portfolio managers, allocators, or resource-sector analysts who want the underlying Markowitz mathematics (formulas, not just concepts) for combining assets or projects by correlation rather than by standalone expected return.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: portfolio-theory, diversification, correlation, expected-value, uncertainty, resource-projects
