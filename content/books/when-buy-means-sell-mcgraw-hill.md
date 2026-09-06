---
author: Eric Shkolnik
category: Investing, Value & Market History
difficulty: intermediate
doc_type: book
one_liner: 'Backtests analyst Buy/Hold/Sell ratings and finds two exploitable lags:
  sell Strong-Buy stocks on a fixed 6-12 month date instead of waiting for the downgrade,
  and buy Hold-rated stocks a year after they were downgraded.'
pages: 241
related:
- damodaran-aswath-investment-fables
- david-dreman-contrarian-investment-strategies-the-next-generation
- mcgraw-hill-the-triumph-of-contrarian-investing-crowds-manias-and-beating-the-market-by-go
- mcgraw-hill-buy-the-rumor-sell-the-fact-85-maxims-of-wall-street-and-what-they-really-mean
- doug-henwood-wall-street-how-it-works
reviewed_pdf_pages: 4, 11, 13, 22, 108, 165, 168, 170, 172, 181, 183-184, 226 (the
  screening rules and the backtest tables reporting the strategies' returns)
slug: when-buy-means-sell-mcgraw-hill
source_file: When Buy Means Sell - Mcgraw Hill.pdf
source_review: partial
tags:
- analyst-recommendations
- regression-to-the-mean
- contrarian
- wall-street
- ipo-avoidance
- diversification
- artificial-maturity
- behavioral-finance
tier: A
title: 'When Buy Means Sell: An Investor''s Guide to Investing When It Counts'
year: 2003
---

## Overview

Eric Shkolnik, founder of the recommendation-tracking site MarketPerform.com, builds a book-length case that Wall Street sell-side analysts are systematically slow to downgrade stocks and just as slow to recognize a turnaround once a stock has been left for dead on a Hold rating. Using his site's database of brokerage-house Buy/Hold/Sell calls from 1999-2002, he runs hypothetical portfolio backtests of several ways an individual investor could trade purely off published recommendations rather than off their substance. The first third of the book lays out ten "fundamental rules" of investing (avoid margin, avoid IPOs, watch insider buying, and so on); the middle third profiles analysts, financial statements, and the "food chain" of sector interdependencies; the final third (Chapters 8-11) is the statistical core, presenting two recommendation-based trading strategies and framing both as instances of regression to the mean.

## Core thesis

Analyst ratings contain real information, but analysts anchor to their own prior call and update it too slowly: Strong Buy stocks keep drifting up for a while after they stop deserving the rating, and Hold/Neutral stocks keep drifting down for a while after they get dumped into the "ugly duckling" bin. Consequently, blindly following recommendations and selling only when the analyst finally flips the rating is a losing strategy, but replacing the analyst's exit timing with a fixed artificial holding period captures the same initial signal without absorbing the delayed reversal. The same lag, worked in the other direction, makes stocks that have carried a low rating for a long time (and have therefore already absorbed the bad news and the selling pressure) statistically likely to have bottomed - buying them roughly a year after the downgrade earns the reversion.

## Key concepts

- **Artificial maturity date** — a fixed holding period (6 or 12 months) imposed on a Strong-Buy purchase instead of holding until the analyst issues a downgrade; converts several loss-making rating groups into profitable ones in the book's backtests.
- **Champion-challenger system** — a testing framework borrowed from the author's bank credit-scoring background: run an incumbent ("champion") strategy against one or more candidate ("challenger") strategies in parallel, and promote a challenger only after it beats the champion consistently for a stated period.
- **Regression to the mean** — Shkolnik's overarching explanation for both edges: extreme outperformers (Strong Buy names) and extreme underperformers (Hold/Sell names) both revert toward average performance, and analyst ratings lag that reversion in both directions.
- **The Wall Street food chain** — sector and supply-chain interdependencies (e.g., Dell's slowdown foreshadowing Intel's and Micron's) used to explain why a downgrade in one name is informative about related names.
- **Statistical vengeance / "trust but verify"** — Shkolnik's term for holding financial institutions, not just individual analysts, accountable by tracking the aggregate historical performance of each firm's rating categories.
- **Lockup expiration** — the post-IPO date when insiders are first permitted to sell; used as a red flag for why newly public companies should be excluded from a Strong-Buy portfolio regardless of the rating.
- **"Ugly duckling" stocks** — Hold/Neutral/Market-Perform names that have already absorbed a period of selling pressure and underperformance and are candidates for the contrarian buy-after-downgrade strategy.
- **Sink-or-swim classification** — the book's own after-the-fact bucketing of a simulated portfolio into "turkeys" (down more than 10%), "ducks" (within +/-10%), and "swans" (up more than 10%), used to show the skew of outcomes in the Hold-rating strategy.

## Rules and setups

The book's tradable content is two related recommendation-based strategies (both are also written up as system sub-pages, [[when-buy-means-sell-mcgraw-hill--strong-buy-artificial-maturity]] and [[when-buy-means-sell-mcgraw-hill--hold-rating-reversal]]):

1. **Strong-Buy artificial-maturity strategy**: buy $1,000 of every stock the moment a tracked institution issues its top rating (Strong Buy / Recommended List), using that day's closing price; sell automatically 130 business days (~6 months) or 255 business days (~12 months) later rather than waiting for a downgrade. Reported results: Bank of America Strong Buy names lost 10.57% held-to-downgrade over 1999-2002 versus a 25.79% gain on the 6-month exit; Merrill Lynch Strong Buy names in the utilities sector returned 2.72% held-to-downgrade versus 22.05% (6-month) and 93.59% (12-month, Gerard Klauer Mattison recommendations) on fixed exits.
2. **Hold-rating reversal strategy**: identify stocks that have carried a Hold/Neutral/Market-Perform rating from the same institution continuously for 12 months (discard any that were upgraded or downgraded within that window); buy on the 12-month anniversary of the downgrade and hold until the next rating change. Reported results (Feb 2000 buy dates, priced through Mar 2002): Salomon Smith Barney Neutral names went from a 1% loss (bought immediately) to a 13.83% gain (bought after 1 year); Lehman Brothers Market Perform names went from a 2.75% loss to 36.33%; Goldman Sachs Market Performer names went from 8.02% to 33.12%.
3. **Universal filters for both strategies**: exclude IPOs entirely (a stock trading under ~1 year), including via the "lockup expiration" red flag in an analyst's own commentary; spinoffs and ADRs are treated as an acceptable exception to the IPO filter; exclude sub-$1 penny stocks from the Hold-reversal portfolio. Applying the IPO filter alone improved one utilities-sector test from 8.37% to 11.64% (or 15% if spinoffs/ADRs were allowed back in).
4. **Ten fundamental rules (Chapter 2)**, applied as pre-filters to any strategy: (1) never invest more than you can afford to lose; (2) avoid margin; (3) avoid short selling as a core strategy; (4) treat IPOs as a trap; (5) insider buying is a bullish signal worth weighing; (6) question whether an acquisition's risk is justified by its reward; (7) share buybacks are a positive signal; (8) be wary of stock (as opposed to cash) dividends; (9) diversify daily rather than once; (10) investigate before investing.
5. **No fixed stop-loss or position-sizing formula is given** beyond the $1,000-per-trade convention used to keep the illustrative portfolios comparable and the 80/20 champion/challenger capital split described in Chapter 1 (80% of investable funds in a core S&P 500 index-fund "champion," 20% allocated to challenger stock-picking rules, promoted into the champion slot only after 3 years of consistent outperformance).

## Risk and money management

Formal risk control is thin. Diversification is treated as the primary risk tool: the Hold-reversal strategy alone generates roughly 160 buy/sell transactions a year (about three per week) spread across many names, which the author argues is what makes the edge tradable at low per-position risk. He estimates trading costs (commissions plus bid-ask spread) at a flat ~5% drag on round-trip returns and nets that out of every headline number. Position sizing is a fixed dollar amount per trade in all worked examples ($1,000), not a percentage of equity or a volatility-scaled size, so the book gives no method for scaling positions to account size or to conviction. There is no stop-loss rule for an individual trade going against expectations before its maturity date; the exit is always time-based (the artificial maturity date) or event-based (the next rating change), never price-based.

## Psychology and discipline

The book's psychology chapters (1, 3, 8) target herd behavior and misplaced trust: peer pressure and "keeping up with the Joneses" pushed investors into dot-com names on fundamentals no better than a friend's tip; financial television creates false intimacy with commentators whose track records are never independently audited; and analysts face structural conflicts of interest (investment-banking relationships) that bias ratings upward and delay downgrades. The discipline prescription is largely mechanical: pick a system, verify it against a champion strategy for a multi-year period before adopting it, then follow the maturity dates and filters without discretionary override — the author explicitly frames "gut feel" as the enemy of the regression-to-the-mean edge, since both strategies require holding a position through a period (a "Strong Buy" already looking tired, or a "Hold" stock everyone hates) precisely when instinct says to act early.

## Chapter map

- Ch 1 — Lessons from Corporate America — champion-challenger testing methodology borrowed from bank credit-risk management; 80/20 index-fund-core allocation model.
- Ch 2 — Rules of Engagement — the ten fundamental rules (margin, IPOs, insider buying, buybacks, dividends, diversification, due diligence).
- Ch 3 — Media and the Investor — how financial television and pundits (Cramer and others) distort decision-making.
- Ch 4 — Who Are the Analysts? — anatomy of a sell-side research report and analyst incentives.
- Ch 5 — Types of Analysis: Fundamental versus Technical — brief primer contrasting the two schools.
- Ch 6 — The Food Chain of Capital Markets — sector interdependency (Dell/Intel/Micron example) as an early-warning tool.
- Ch 7 — Broker versus Mouse Click: The Evolution of Trading — history of stock exchanges from medieval Europe through online brokers.
- Ch 8 — Reputation, Trust, and Statistical Vengeance: Trust But Verify — the Strong-Buy artificial-maturity strategy and its backtests.
- Ch 9 — When "Sell" Really Means "Buy" — the Hold-rating reversal strategy and its backtests.
- Ch 10 — Statistics, Probability, Chance, and Uncertainty — general primer on interpreting historical performance data.
- Ch 11 — Taking Advantage of Regression to the Mean — synthesis, the Enron case study, and closing philosophy.
- Appendix — walkthrough of setting up recommendation alerts on MarketPerform.com.

## Strengths and caveats

The backtests are transparent about assumptions (fixed $1,000 trade size, stated closing-price entry/exit rules, a flat 5% cost estimate) and are refreshingly candid about losers (Kmart, Active Power) rather than cherry-picked winners, which is more rigorous than the typical anecdotal investing book. That said, this is not an academic study: sample sizes per institution/rating/sector are small (often a dozen or two names), there is no out-of-sample verification period, no statistical significance testing is shown despite the language of "statistically meaningful," and the entire dataset comes from a single volatile stretch (1999-2002) dominated by the dot-com bust, which likely inflates both the size of the Strong-Buy overreaction and the size of the Hold-rating reversal. The book also predates decimalized, ultra-low-cost brokerage execution, so its 5% round-trip cost estimate is dated for a self-directed investor today. The core insight (analysts lag reality) is well supported by independent academic literature on analyst herding and sluggish revisions, but the specific 6/12-month maturity windows and the "1 year after downgrade" reversal point are fit to this one sample rather than derived from theory.

## Who should read it

Retail and semi-active investors who want a simple, rules-based alternative to either blindly following analyst upgrades or ignoring them entirely, and who have access to historical Buy/Hold/Sell recommendation data (broker research portals, Yahoo/MSN-style aggregators, or a paid data feed). Less useful for short-term traders, since every rule here operates on a 6- to 12-month holding horizon, and less rigorous than a reader wanting peer-reviewed statistical backing will want.

## Related books in this library

- [[damodaran-aswath-investment-fables]] — a far more rigorous version of the same theory-then-portfolio-backtest structure, applied to value and momentum stories rather than analyst ratings.
- [[david-dreman-contrarian-investment-strategies-the-next-generation]] — the fuller academic case for buying out-of-favor stocks that this book's Hold-reversal chapter gestures toward.
- [[mcgraw-hill-the-triumph-of-contrarian-investing-crowds-manias-and-beating-the-market-by-go]] — another contrarian-investing treatment covering similar overreaction and reversion evidence.
- [[mcgraw-hill-buy-the-rumor-sell-the-fact-85-maxims-of-wall-street-and-what-they-really-mean]] — shares this book's project of decoding Wall Street's stated language versus its actual meaning.
- [[doug-henwood-wall-street-how-it-works]] — deeper structural background on the brokerage and research-conflict dynamics summarized in Chapters 4 and 8.
