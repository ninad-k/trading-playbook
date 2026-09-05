---
title: When Buy Means Sell — Strong-Buy Artificial-Maturity Strategy
author: Eric Shkolnik
year: 2003
slug: when-buy-means-sell-mcgraw-hill--strong-buy-artificial-maturity
tier: A
category: "Investing, Value & Market History"
tags: [analyst-recommendations, exit-strategy, time-based-exit, regression-to-the-mean]
difficulty: intermediate
doc_type: system
parent: when-buy-means-sell-mcgraw-hill
pages: 241
one_liner: "Buy on a brokerage's top rating, but replace the analyst's own (late) downgrade with a fixed 6- or 12-month sell date to capture the drift and skip the reversal."
related: [when-buy-means-sell-mcgraw-hill, david-dreman-contrarian-investment-strategies-the-next-generation]
source_file: "When Buy Means Sell - Mcgraw Hill.pdf"
---

## What it is

A time-exit overlay on ordinary sell-side stock ratings. The observation driving it: brokerage-house Strong Buy (or equivalent top-tier) recommendations do generate real outperformance for a while, but analysts are consistently slow to downgrade once the story turns, so holding a Strong-Buy stock all the way to the eventual downgrade gives back most or all of the gain. Instead of waiting for the analyst's sell signal, the strategy imposes its own fixed holding period and exits on schedule regardless of what the analyst still says.

## Rules

1. **Universe**: any stock that receives a top-tier rating (Strong Buy, Recommended List, or the issuing institution's equivalent highest category) from a tracked brokerage house. Recommendation data can be pulled from free aggregators (Yahoo Finance, MSN Money) or a paid feed; the book's own tests used MarketPerform.com's database.
2. **Entry**: buy a fixed dollar amount (the book's illustrations use $1,000 per position for comparability) at that day's closing price — not the prior day's close, which analysts and vendors often quote to flatter results, and not an average/opening price.
3. **Exit — the artificial maturity date**: sell automatically 130 business days (~6 months) or 255 business days (~12 months) after entry, regardless of the current rating, UNLESS the institution issues a rating change (upgrade, downgrade, or dropped coverage) before that date, in which case sell immediately at that day's close instead.
4. **Choosing 6 vs. 12 months**: the book found no single dominant choice — 12-month exits outperformed 6-month exits in some sectors/institutions (e.g., Gerard Klauer Mattison utilities recommendations: 22.05% at 6 months vs. 93.59% at 12 months) but underperformed in others (e.g., Bank of America's PC Connection call: 25.79% at 6 months vs. 10.7% at 12 months). Treat the horizon as a parameter to test per sector/institution rather than a universal constant; extending a day or two past the 1-year mark also converts a short-term gain into a long-term-capital-gains holding period under U.S. tax rules.
5. **Mandatory filters before entry**:
   - Exclude IPOs outright — any stock trading for less than roughly one year. Check the price history on the recommendation date; if it is short, skip the trade even if the rating and commentary look compelling. A same-day analyst note mentioning "lockup expiration" is treated as a hard skip regardless of the rating.
   - Spinoffs and ADRs are an explicit exception to the IPO filter — they behave more like established companies (the book found NRG Energy, a spinoff, and British Energy, an ADR, performed acceptably despite being nominally new listings) and may be admitted back into the universe.
6. **Diversification requirement**: never concentrate in a handful of names; run the strategy across an institution's full set of top-rated names in a sector (or across sectors) so that individual blowups (the book's example: Active Power Corp., -63% after a Strong Buy issued the same day as a lockup-expiration warning) are absorbed by the portfolio rather than sinking the account.
7. **Segment by institution and sector, not blindly across the whole market**: track performance separately by brokerage house and by sector before committing capital, since results vary meaningfully — in the book's tests, a given institution's second-best rating tier (plain Buy) sometimes outperformed its top tier (Strong Buy) in the same period, which would not be visible without segmenting.
8. **Position management between entry and exit**: fully passive — no scaling in/out, no stop-loss, no profit target. The only two events that can end the trade early are a rating change from the issuing institution or (implicitly) a delisting/bankruptcy.

## Risk

No price-based stop-loss exists in this system; risk control is entirely structural: (a) fixed, equal dollar sizing per position so no single name can dominate the portfolio, (b) mandatory diversification across many simultaneous positions (the book's Hold-strategy companion piece notes roughly 160 trades/year, i.e., about 3 open positions turning over per week, when run across a full sector), and (c) the IPO/lockup exclusion filter, which in the book's tests removed the single largest loss from every portfolio it was tested on (excluding IPOs improved one utilities-sector test from 8.37% to 11.64%, and to 15% if spinoffs/ADRs were allowed). Transaction costs are estimated at a flat ~5% of round-trip return (commissions plus bid-ask spread) and should be subtracted from any backtested figure before judging viability; several of the book's headline gains (e.g., 11.51% raw improving to 16.71% after excluding IPOs, in the combined technology-sector test) were reported as still net-positive after this haircut, but some were not (Bank of America's original held-to-downgrade portfolio lost 10.57%, in line with a losing market).

## Caveats

The entire evidence base is one brokerage-recommendation dataset covering February 1999 through roughly February 2002 — a period dominated by the dot-com bubble and its collapse — so both the size of the early Strong-Buy drift and the size of the subsequent give-back on held-to-downgrade portfolios may be larger than in a calmer market; the strategy has not been shown to hold up out-of-sample in a different regime. Sample sizes per institution/sector/rating combination are often small (a dozen or so names), and no formal statistical significance test accompanies the percentage-return figures despite the author's language of "statistically meaningful" results. The 6-versus-12-month choice is not resolved by the book's own data — it flips depending on institution and sector — so a user must re-test both horizons on current data rather than assume either is universally better. Analyst rating taxonomies and thresholds also drift over time and across firms (a "Buy" at one house may mean 5%+ expected outperformance, at another something else entirely), so the universe definition requires re-verifying each institution's current rating scale before applying the rule mechanically.
