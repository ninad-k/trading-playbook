---
title: Understanding Gaps
author: Scott Andrews
year: 2008
slug: andrews-scott-understanding-gaps
tier: B
category: Day Trading & Scalping
tags: [gap-trading, gap-fade, s-p-500-futures, day-trading, statistics, stop-loss, target-optimization]
difficulty: intermediate
doc_type: book
pages: 61
one_liner: "Statistical framework for fading the opening gap in S&P 500 futures using gap size, zone, seasonality, stop, and target data."
related: [using-up-gaps-to-anticipate-upward-price-moves, big-profit-patterns-using-candlestick-signals-and-gaps-stephen-w-bigalow, jeff-cooper-intra-day-trading-strategies-proven-steps]
source_file: "Andrews, Scott - Understanding Gaps.pdf"
---

## Summary

A short, data-driven guide to trading the opening gap, focused on the E-mini S&P 500 futures. The author defines a gap as the difference between the prior day's regular-session close and the next day's open, classifies gaps into four types (breakaway, common, continuation/runaway, exhaustion), and shows that roughly 72–73% of opening gaps in the S&P 500 fill (retrace to the prior close) the same day, based on 1998–2008 data. The book's central point is a paradox: trading every gap fade with no stop is only marginally profitable (average profit factor ~1.08) because the 25–30% of gaps that don't fill tend to run hard against the position. The bulk of the book is a framework — gap size, gap zone (location relative to prior day's open/high/low/close), seasonality, stop size, and target optimization — for filtering which gaps to fade and how to manage the trade.

## Key points

- Four gap types: breakaway (after consolidation, doesn't fill same day, high volume), common (average/below-average volume, usually fills same day), continuation/runaway (confirms an ongoing trend, often doesn't fill same day), exhaustion (occurs near trend end, high volume, often reverses sharply).
- 1998–2008 E-mini S&P 500 data: ~72.6% average win rate fading gaps >1 point with no stop and closing at day's end if unfilled; but average profit factor was only 1.08 — gross profits barely exceeded gross losses.
- Smaller gaps fill more often: win rate ranges from 84.5% for gaps <0.2% of the index down to roughly 49–59% for gaps over 1%.
- "Gap zone" (location of the open relative to the prior day's high/low/close, and whether the prior day was up or down) materially changes win rate — zones ranged from 54% to 82% in the study.
- Day-of-week and month-of-year seasonality affects win rate; Wednesday and October historically had the highest fill rates, September the lowest, in the sample studied.
- Stop size trades off win rate against payoff: at 25% of gap size the stop gave a 21.4% win rate with a 3.49 win/loss ratio (profit factor 0.95); at 200% of gap size, win rate rose to 66.1% but win/loss ratio fell to 0.53 (profit factor 1.03) — profit factor stayed close to breakeven across all tested stop sizes.
- The author trades a fixed point stop per gap zone rather than scaling the stop to gap size, citing the flat/marginal profit-factor curve as evidence that variable stops add little edge.
- Target optimization (using extended targets beyond the full gap-fill level, not just the prior close) is presented as a key lever for turning a marginal edge into a profitable strategy.

## Actionable rules

1. Define the gap as opening price minus prior regular-session closing price; trade primarily in liquid index futures (S&P 500, Nasdaq 100) rather than single stocks to reduce single-name news risk.
2. Filter for smaller gaps and favorable gap zones first — win rate is far higher for gaps <0.4% of the index and for zones where the gap direction runs counter to (fades) the prior day's trend.
3. Use a fixed-point stop sized per gap zone (not scaled to gap size); the author's own studies found win rate rises with stop size but win/loss ratio falls almost proportionally, netting little edge from stop-size alone.
4. Do not rely on gap-fill probability alone as an edge — with no stop, the aggregate strategy was barely profitable (profit factor ~1.08); a full system requires combining gap size, zone, and seasonality filters plus stop and target rules together.
5. Consider extended targets beyond the prior day's close (partial or full gap-fill plus continuation) rather than exiting exactly at the fill level, since the author found this materially improved results.
6. Enter at or shortly after the market open with a market order; day traders manage the trade within roughly 1–2 hours, closing by day's end if the gap has not filled.

## Caveats

All statistics are drawn from a single instrument (E-mini S&P 500 futures) over 1998–2008, a specific volatility regime; results will not necessarily transfer to other markets, single stocks, or post-2008 conditions. Sample sizes for some breakdowns (individual months, zones) are in the low hundreds, and the author himself warns readers not to over-optimize on subdivided seasonality data. The book stops short of giving one complete, ready-to-code system — it presents component statistics (size, zone, seasonality, stop, target) as inputs the reader must combine, not a single stated rule set.

## Who it is for

Day and swing traders who want a probability-based approach to gap trading and are comfortable building their own filter/stop/target combination from historical win-rate and profit-factor tables rather than following one fixed rule set.
