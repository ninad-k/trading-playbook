---
title: When Buy Means Sell — Hold-Rating Reversal Strategy
author: Eric Shkolnik
year: 2003
slug: when-buy-means-sell-mcgraw-hill--hold-rating-reversal
tier: A
category: "Investing, Value & Market History"
tags: [analyst-recommendations, contrarian, regression-to-the-mean, entry-strategy]
difficulty: intermediate
doc_type: system
parent: when-buy-means-sell-mcgraw-hill
pages: 241
one_liner: "Buy stocks a full year after a brokerage downgraded them to Hold/Neutral, on the theory that a rating that has stuck for a year means the bad news is priced in and a reversal is due."
related: [when-buy-means-sell-mcgraw-hill, david-dreman-contrarian-investment-strategies-the-next-generation, damodaran-aswath-investment-fables]
source_file: "When Buy Means Sell - Mcgraw Hill.pdf"
---

## What it is

A contrarian, delayed-entry counterpart to the Strong-Buy artificial-maturity strategy (see [[when-buy-means-sell-mcgraw-hill--strong-buy-artificial-maturity]]). Its premise: stocks downgraded to a middling rating (Hold, Neutral, Market Perform — one notch above the rarely-used outright Sell) have already absorbed a period of selling pressure and negative sentiment by the time a year has passed, and are statistically likely to be closer to a bottom than a top. Buying them a year after the downgrade, rather than on the downgrade day itself, converts a mildly market-beating strategy into a strongly market-beating one in the book's tests.

## Rules

1. **Universe**: stocks that receive a middling rating (Hold / Neutral / Market Perform / Market Performer, i.e., the tier immediately above outright Sell) from a tracked institution.
2. **Qualification filter — the 12-month hold requirement**: only include a stock if the same institution has kept it at that same middling rating continuously for a full 12 months from the downgrade date. If the institution upgrades or downgrades the stock again at any point within that 12-month window, the stock is disqualified from this portfolio entirely (it belongs, if anything, to a different vintage of the screen once its rating re-stabilizes).
3. **Entry**: buy a fixed dollar amount (book's illustrations: $1,000/position) at the closing price on the exact 12-month anniversary of the original downgrade date — this is the "artificial purchase-maturity date." Do not buy on the downgrade day itself; the book's side-by-side tests found immediate purchase underperformed the 1-year-delayed purchase by roughly 15-39 percentage points across three institutions tested (Salomon Smith Barney, Lehman Brothers, Goldman Sachs).
4. **Exit**: hold until the institution issues its next rating change (up or down) from that middling rating, then sell at that day's closing price. No fixed holding period or profit target is used on the exit side of this strategy (contrast with the Strong-Buy strategy, which uses a fixed maturity date on exit).
5. **Optional refinement — let upgrades run**: rather than mechanically selling the instant a Hold is upgraded, the book notes that stocks upgraded out of a qualifying Hold rating (in its retail-sector example, by Goldman Sachs) tended to keep appreciating for a further ~10% over the following 3 months; a discretionary refinement is to hold briefly past the upgrade rather than exiting same-day.
6. **Mandatory filters**:
   - Exclude penny stocks (roughly sub-$1) from the qualifying universe — in the book's dataset, stocks that fell below $1 during the year at a middling rating disproportionately failed to survive, dragging down the group's average by about 2 percentage points.
   - The IPO exclusion from the companion strategy is naturally satisfied here in most cases, since a stock must have held a stable rating for a full year before qualifying, but should still be checked for very recently listed names.
7. **Diversification requirement**: run this across a full sector or a full institution's rated universe, not a handful of names. The book's own worked example (18 Goldman Sachs "Market Performer" retail names, $1,000 each) produced a wide dispersion of outcomes — 3 "turkeys" (down >10%), 4 "ducks" (within +/-10%), 11 "swans" (up >10%) — with one severe loser (Kmart, -89%) offset by several large winners (Gymboree +238%, Pep Boys +230%); only the pooled, diversified result (+48% on the $18,000 book) represents the tradable edge, not any individual name.
8. **Turnover expectation**: following this strategy across a single institution's full Hold-rated universe generates roughly 160 buy/sell transactions per year (about 3 per week) — plan execution and cost assumptions (low-cost or asset-fee brokerage) around that turnover rather than a buy-and-hold cadence.

## Risk

Risk control is again structural rather than price-based: fixed equal-dollar position sizing, mandatory broad diversification across a full rated universe (single-name blowups like the Kmart example are expected and are absorbed by the portfolio), and the penny-stock exclusion filter. There is no stop-loss and no fixed maximum loss per position — a name can go to zero (or near it, as with sub-$1 stocks that fail to survive) between the 1-year entry and the eventual rating-change exit, since the exit trigger is a rating event, not a price level. The book estimates a flat ~5% round-trip cost drag (commissions plus bid-ask spread) and states its headline returns are large enough to absorb that drag with room to spare (e.g., Lehman Brothers' 39-point improvement from delayed entry, or the 48% pooled Goldman Sachs retail-sector result), but a user should re-underwrite that cost assumption against current commission-free or low-cost brokerage economics, which would make the net edge even larger, and against a possibly wider bid-ask spread on the smaller, less-liquid, out-of-favor names this strategy specifically selects for.

## Caveats

Same dataset limitation as the companion Strong-Buy strategy: all reported results come from stocks reaching their 12-month qualification point and being priced through February/March 2002, a period straddling the dot-com collapse, so both directions of the underlying regression-to-the-mean effect may be unusually strong in this sample and would need re-testing in a different market regime. Sample sizes are small (the worked retail-sector example uses only 18 stocks), and the disqualification rule (drop any stock whose rating changed within the 12-month qualification window) introduces a subtle selection effect: it deliberately keeps only the most "stuck" ratings, which may behave differently from a middling rating that saw some interim analyst activity before restabilizing. No statistical significance testing accompanies the return figures. The requirement to track a rolling 12-month rating history per stock per institution demands a maintained recommendation database (the book's own examples rely on the author's MarketPerform.com tracking) — an investor without such a data feed cannot easily reconstruct the qualifying universe from a single snapshot of today's ratings.
