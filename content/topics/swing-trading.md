---
title: Swing Trading
summary: "Multi-day trades built on pullbacks, failed breakouts and volatility contraction — the library's most fully specified setups, and almost none of them backtested."
books_covered: 35
---
## What it is

Swing trading holds a position for roughly one to ten sessions: long enough to need a real directional move, short enough that the entry has to be timed. It sits between day trading, which never carries overnight risk, and trend following, which tolerates large drawdowns waiting for a big win. The category's recurring structure is a trend established on a higher timeframe plus a temporary dislocation on a lower one — a pullback to a moving average, a failed breakout, a narrow-range bar, a gap that reverses — entered with a tight stop defined by the setup's own geometry. Because a swing trader rarely makes a large profit on any single trade, several authors argue the discipline is more about capping losses than finding entries: Connors and Raschke put money management at "80 percent of the battle."

## Core principles

- Trade the pullback, not the breakout: the highest-probability entries come from a temporary counter-move inside an already-established trend [[street-smarts-laurence-connors--holy-grail]] [[alan-farley-the-master-swing-trader--dip-trip]] [[oliver-velez-swing-trading-tactics]].
- Use the higher timeframe for direction and the lower one for timing — the same structural idea appears as 3D charting, cycle nests and stage matching [[alan-farley-the-master-swing-trader--3d-charting-cross-verification]] [[walter-bressert-intraday-timing-for-low-risk-swing-trading]] [[oliver-velez-swing-trading-tactics]].
- Enter only where independently derived levels converge; Farley's cross-verification treats four overlapping signals at one price as the highest-probability case [[alan-farley-the-master-swing-trader--3d-charting-cross-verification]] [[john-l-person-swing-trading-using-candlestick-charting-with-pivot-point]].
- The setup defines the stop. Risk is the distance to the level that invalidates the pattern, not an arbitrary dollar figure [[street-smarts-laurence-connors]] [[oliver-velez-swing-trading-tactics--pristine-buy-sell-setup]] [[marc-boucher-short-term-trading-course]].
- Enter the full position at once; scale out rather than in [[street-smarts-laurence-connors]]. Smith inverts this for funds — build gradually in 25-33% increments, exit all at once [[gary-smith-how-i-trade-living]].
- A large fraction of breakouts fail, which is itself the tradable event: Turtle Soup fades the same 20-day breakout the Turtles used as an entry [[street-smarts-laurence-connors--turtle-soup]].
- Volatility contraction precedes expansion, and a narrow-range bar is a directionless signal — let the market pick the side with a bilateral entry stop [[alan-farley-the-master-swing-trader--coiled-spring]].
- Tighten or exit into a parabolic or range-expansion move: it marks the last wave of participants entering, which is the highest-probability exit rather than a reason to add [[street-smarts-laurence-connors]] [[alan-farley-the-master-swing-trader--power-spike]].
- Trends persist only a minority of the time — Farley puts it at 10-20% — so most setups must assume mean reversion is the default state [[alan-farley-the-master-swing-trader]].
- Liquidity is a hard filter, not a preference: thin names generate meaningless narrow-range bars, single-bar candles and volume spikes [[alan-farley-the-master-swing-trader--finger-finder]] [[a-practical-guide-to-swing-trading]].
- Short setups need different handling from long ones: smaller size, more patience, and awareness that squeezes are engineered where uninformed shorts cluster [[alan-farley-the-master-swing-trader--bear-hug]] [[alan-farley-3-swing-trading-examples-with-charts-instructions-and-definitions-to-get-you-s]].
- A system can be profitable well below a 50% win rate provided the average win sufficiently exceeds the average loss [[alan-farley-the-master-swing-trader]].
- Market selection can matter more than entry timing: Boucher's whole method is finding the few instruments already in a runaway trend and joining them [[marc-boucher-short-term-trading-course]].
- Consistent moderate returns compound better than sporadic large ones once drawdown is counted [[marc-boucher-short-term-trading-course]].

## Concrete rules and setups

### Failed-breakout and exhaustion reversals

1. Turtle Soup: today makes a new 20-day low whose prior 20-day low occurred at least four sessions earlier; place a buy stop 5-10 ticks above that prior low, good for today only, with a protective stop one tick under today's low. Re-enter at the original price if stopped out on day one or two [[street-smarts-laurence-connors--turtle-soup]].
2. Turtle Soup Plus One: the same setup but requiring day one's *close* at or below the prior 20-bar low, with the entry stop placed at that low the next day and the trade cancelled if unfilled on day two [[street-smarts-laurence-connors--turtle-soup-plus-one]].
3. Whiplash: the market gaps below the prior day's low, then closes above its open and in the top half of the day's range — buy market-on-close. If the next session opens against the position, exit immediately; otherwise trail [[street-smarts-laurence-connors--whiplash]].
4. 2B: price makes a marginal new high above the last swing high then reverses back below it — short, with the stop just above the failed high [[alan-farley-the-master-swing-trader]].
5. Hole-in-the-wall: a stock near a new intermediate high gaps sharply lower on volume exceeding the prior rally impulse. Short the rally back into the gap — even weak holes rarely have their first pullback fill completely [[alan-farley-the-master-swing-trader--hole-in-the-wall]].
6. Profiting from euphoria: a stock up 25% or more in 30 days, volume above its 150-day average, RSI overbought, rising volatility, and a bearish candle that makes a new intraday high before closing down. Skip it if the next day is bullish [[tyler-bollhorn-market-perspectives]].

### Pullback continuation

7. Holy Grail: a 14-period ADX above 30 and rising, then wait for a pullback to the 20-period EMA and place a buy stop above the previous bar's high, with the protective stop at the new swing low. A turndown in ADX during the pullback is normal and not a reversal signal. After the trade, ADX must turn back above 30 before the setup can fire again [[street-smarts-laurence-connors--holy-grail]].
8. The Anti: a 7-period %K and 10-period %D stochastic. With %D in a definite uptrend, wait for a retracement to pull %K back toward %D, then enter as %K hooks back up — buy stop one tick above the previous bar, trailed down each day until filled. Hold two to four bars [[street-smarts-laurence-connors--the-anti]].
9. Dip Trip: a strong prior uptrend, a decline on lower volume than the preceding rally bars, and no violation of important support. Retracements of 38-50% are the tradable zone; the correction should complete in fewer bars than the rally that preceded it. Drop a timeframe to confirm a reversal before entering [[alan-farley-the-master-swing-trader--dip-trip]].
10. Pristine Buy Setup: three or more consecutive lower highs, three or more lower lows, and three or more red bars. Buy $0.05-0.10 above the prior day's high, stop $0.05-0.10 below the lower of the entry day's or prior day's low, and trail under each bar's low once two bars have closed [[oliver-velez-swing-trading-tactics--pristine-buy-sell-setup]].
11. Larry Swing's Master Plan: filter to stocks above roughly $7-12 with 500,000+ average daily volume, price above the 10- and 20-day SMAs with the 10 above the 20. Enter on a buy stop 6 cents above the prior day's high, take half at +7%, stop at the greater of 4% below entry or 6 cents below the entry day's low, and trail to 6 cents below each new day's low. Abandon an unfilled order after five days [[a-practical-guide-to-swing-trading]].
12. Trader's Trick Entry: buy one tick above the high of a correcting bar following a 1-2-3 point 2 or a Ross hook, but only if there is enough room to the breakout point to cover costs and bank profit. No more than three correcting bars; the second is usually the best trade-off [[traders-trick-entry]].

### Volatility contraction and breakouts

13. Coiled Spring: identify an NR7 — the narrowest high-low range of the last seven bars — preferably with declining volume and narrowing swings into it, at a triangle apex or against a band extreme. Place a bilateral entry stop just outside both extremes and cancel the untriggered side [[alan-farley-the-master-swing-trader--coiled-spring]].
14. Bear Hug: apply the same NR7 logic filtered for *low* relative strength, or fade a bear-market rally into resistance — commonly the 50-day EMA or a 62% retracement — requiring a visible topping pattern before entry [[alan-farley-the-master-swing-trader--bear-hug]].
15. Boucher's runaway screen: five or more TBBLBG patterns in a trailing 21-day window, no close below the 200-day MA since the trend began, relative strength rank of at least 65 on pullbacks or 80 on new highs, EPS rank 80+, institutional ownership under 16%, long-term debt under 50% of capitalisation, and an identifiable fundamental catalyst [[marc-boucher-short-term-trading-course--runaway-market-tbblbg-breakouts]].
16. Thrust Breakout bar: range at least twice the 20-day average range, volume above the prior day, close in the top third of the range, and the low below the prior close. Breakaway Lap: the low is above the prior close but below the prior high. Breakaway Gap: the low is above the prior high [[marc-boucher-short-term-trading-course]].
17. 3rd Watch: a cup-and-handle compressed to 6-month highs rather than 52-week, no new high within four weeks of the signal, and breakout-bar volume at least 150% of average [[alan-farley-the-master-swing-trader--3rd-watch]].
18. Power Spike: volume at or above 3× the 50-day volume moving average on a single bar, or 2× for two consecutive days, then classify the price context — breakout, breakdown, reversal or pivot — before choosing a strategy. Prints of 5-6× often mark a short-circuited phase; stand aside [[alan-farley-the-master-swing-trader--power-spike]].

### Momentum and overnight bias

19. Momentum Pinball: plot a 3-period RSI of the 1-period rate of change. When it closes below 30, place a buy stop above the next day's first-hour high with the protective stop at that hour's low; carry a profitable position overnight and exit on day three's follow-through at the latest [[street-smarts-laurence-connors--momentum-pinball]].
20. 2-period ROC: subtract today's close from the close two days back, add it to yesterday's close to get the pivot, then go home long above that pivot and short below it [[street-smarts-laurence-connors--2-period-roc]].
21. Smith's V-bottom: the Dow trades down at least 0.75% intraday then reverses to close near unchanged or higher — actionable only after a prior down day, and stronger the later in the session it occurs. His late-day surge requires a choppy session rallying in its final 2-2.5 hours to close at least 0.50% above the prior close [[gary-smith-how-i-trade-living--momentum-fund-timing]].
22. Smith's exit triggers: a 3-4% reaction from the recent high, or a "1% true selling day" where the Dow, S&P, Nasdaq 100 and Russell 2000 all close down 1% or more after at least two weeks of rising prices [[gary-smith-how-i-trade-living--momentum-fund-timing]].
23. Smith's futures entries: note the first 50 minutes' high and buy a break of it between 9:20 and 11:00, most reliably after a narrow-range prior day; or buy 180 points off the intraday low in the same window [[gary-smith-how-i-trade-living--sp-futures-day-trading]].

### Geometry and levels

24. Wolfe Wave: count from a top — wave 2 is that top, wave 3 the following bottom, wave 1 the bottom before the top, wave 4 the bounce after wave 3, with point 3 lower than point 1 and point 4 ideally higher. Extend the 1-3 line to project point 5 as the entry and the 1-4 line as the target [[street-smarts-laurence-connors--wolfe-waves]].
25. Pivot levels with candlestick confirmation: P = (H+L+C)/3, R1 = 2P − L, S1 = 2P − H, calculated daily, weekly and monthly, and acted on only when a candlestick reversal forms at the level [[john-l-person-swing-trading-using-candlestick-charting-with-pivot-point]].
26. Finger Finder: a real body one-third or less of the bar's total range, located at high volume or major support/resistance — best when the shadow pierces a band extreme while the body stays inside. Ignore the pattern in congestion or on 1-minute charts [[alan-farley-the-master-swing-trader--finger-finder]].
27. Arps's retracement bands: pullbacks retrace 35-40% in strong trends and 50-60% in weak ones; beyond about 65%, treat the trend as likely over [[jan-l-arps-surfing-the-market-waves-the-swing-trader-s]].
28. Rockefeller's channel discipline: establish direction with the slow trend model, wait for price to reach the opposite ATR band before entering with the trend, and do not reverse on the first day of a fresh signal — more than 70% of the illustrated ATR breakouts were followed by a breakout the other way [[staying-out-of-trouble-trading-currencies-with-channels]].

### Risk

29. Boucher caps theoretical risk — entry minus the open protective stop — at 2% of capital, sets stops at market-determined support and resistance rather than fixed distances, and only adds size once the trailing stop has eliminated the initial risk [[marc-boucher-short-term-trading-course]].
30. Farley requires a profit target at least 3× the distance to the failure target before slippage, which lands nearer 2.5:1 in practice [[alan-farley-the-master-swing-trader]].
31. Smith risks 1-2% of a position's value on any initial purchase and avoids leverage once the account no longer needs it [[gary-smith-how-i-trade-living]].
32. Forex-specific stop conventions: 40-50 pips minimum on GBP/USD and 100-150 on GBP/JPY [[general-observations-thoughts-on-trading-gbp]]; 100 and 150 pips respectively with breakeven moves at the same distances [[vanessafx-advanced-systems]].

## Common mistakes

- Scaling into a winner rather than entering the full position at once and scaling out [[street-smarts-laurence-connors]].
- Exiting or reversing because ADX turns down during a pullback, when that turndown is a normal feature of the setup [[street-smarts-laurence-connors--holy-grail]].
- Chasing a parabolic breakout through new highs with no base beneath it, so there is no defined stop level [[alan-farley-the-master-swing-trader--3rd-watch]].
- Treating a bare NR7 as directional when it carries no inherent bias [[alan-farley-the-master-swing-trader--coiled-spring]].
- Trading single-bar candlestick signals in thin names or on very short intraday charts where bad ticks distort the shadows [[alan-farley-the-master-swing-trader--finger-finder]].
- Applying volume-spike analysis intraday, where the first and last hour can carry 60% or more of the session's volume [[alan-farley-the-master-swing-trader--power-spike]].
- Shorting into a sharply falling market or during the first and last hour, where squeezes are most likely [[alan-farley-the-master-swing-trader--bear-hug]] [[alan-farley-3-swing-trading-examples-with-charts-instructions-and-definitions-to-get-you-s]].
- Shorting on the initial neckline break of a widely known pattern rather than waiting for the weak retracement into resistance [[alan-farley-3-swing-trading-examples-with-charts-instructions-and-definitions-to-get-you-s]].
- Trading a 1-2-3 formation that sits inside a consolidation rather than at the end of a trend, where the same shape occurs in both directions [[traders-trick-entry]].
- Committing heavily to a first channel breakout in a currency market [[staying-out-of-trouble-trading-currencies-with-channels]].
- Reading short-term oscillator extremes on a lower timeframe during a strong trend, when they stay pinned [[general-observations-thoughts-on-trading-gbp]].
- Trading frequently for its own sake: Smith cites research finding accounts with 48+ round trips a year earned roughly a third less than average [[gary-smith-how-i-trade-living]].

## Best books for this topic

1. [[street-smarts-laurence-connors]] — the most completely specified collection of short-term setups anywhere in this library, each with real entry and stop prices, and honest that none is a standalone mechanical system.
2. [[alan-farley-the-master-swing-trader]] — the richest framework: pattern cycles, cross-verification, 3D charting and seven named setups, plus explicit expectancy arithmetic.
3. [[marc-boucher-short-term-trading-course]] — teaches money management before entries, and its breakout-bar definitions are precise enough to code directly.
4. [[gary-smith-how-i-trade-living]] — real dates, real percentages and audited multi-year returns, which makes the patterns testable even where the vehicles are obsolete.
5. [[oliver-velez-swing-trading-tactics]] — the simplest fully numeric entry pattern in the category, and a clean four-stage mental model for trend context.
6. [[a-practical-guide-to-swing-trading]] — the most mechanical rule set here: fixed targets, fixed stops, fixed trailing, no intraday judgement required.
7. [[walter-bressert-intraday-timing-for-low-risk-swing-trading]] — the clearest statement of using nested timeframes to shrink the stop without changing the trade.
8. [[john-l-person-swing-trading-using-candlestick-charting-with-pivot-point]] — a compact pairing of pivot arithmetic with candlestick confirmation, and candid that it is not a holy grail.
9. [[tyler-bollhorn-market-perspectives]] — usable screening criteria for bottom-fishing and fading euphoric spikes, stated as numbers rather than descriptions.
10. [[jan-l-arps-surfing-the-market-waves-the-swing-trader-s]] — a useful catalogue of swing-detection tools and retracement bands, though tied to a proprietary indicator suite.

## Open debates

- **Fade the breakout or join it.** Connors and Raschke's Turtle Soup profits precisely because 20-day breakouts fail often [[street-smarts-laurence-connors--turtle-soup]]; Boucher's entire method is joining breakouts in markets already running, filtered so that only the strongest qualify [[marc-boucher-short-term-trading-course--runaway-market-tbblbg-breakouts]]. Neither offers a rule for telling in advance which regime applies.
- **Build the position gradually or all at once.** Connors and Raschke require the full size immediately, arguing scaling in is how short-term traders let losses run [[street-smarts-laurence-connors]]; Smith builds in 25-33% increments and exits in large chunks [[gary-smith-how-i-trade-living]]; Boucher adds only after the trailing stop has removed the original risk [[marc-boucher-short-term-trading-course]].
- **Whether these setups can be mechanised at all.** Velez's and Larry Swing's rules are fully numeric [[oliver-velez-swing-trading-tactics--pristine-buy-sell-setup]] [[a-practical-guide-to-swing-trading]]; Farley says outright that "the skilled eye does a better job than any mathematics" for several of his [[alan-farley-the-master-swing-trader--finger-finder]]; Smith reports his own attempts to automate his patterns failed [[gary-smith-how-i-trade-living--momentum-fund-timing]].
- **How much risk one setup justifies.** Boucher fixes 2% of capital [[marc-boucher-short-term-trading-course]]; Larry Swing uses a 4% price stop with capital split across 15-20 buckets [[a-practical-guide-to-swing-trading]]; Velez gives dollar offsets and no equity percentage at all [[oliver-velez-swing-trading-tactics]]; Farley constrains by reward-to-risk instead [[alan-farley-the-master-swing-trader]].
- **Whether reward-to-risk filters or invalidation levels should govern entry.** Farley requires 3:1 before taking a setup [[alan-farley-the-master-swing-trader]]; Connors and Raschke instead define risk purely by the tick beyond the tested level and say nothing about a ratio [[street-smarts-laurence-connors--turtle-soup]].
- **Fixed stop distances versus structural ones.** Velez's $0.05-0.10 offsets and the forex pip conventions are fixed numbers calibrated to a market era [[oliver-velez-swing-trading-tactics--pristine-buy-sell-setup]] [[vanessafx-advanced-systems]]; Boucher and Connors both derive the stop from price structure, which adapts automatically to volatility [[marc-boucher-short-term-trading-course]] [[street-smarts-laurence-connors]].
- **What the evidence base actually is.** Only Smith offers an audited multi-year record [[gary-smith-how-i-trade-living]], and Connors and Raschke's appendix explicitly says its cited studies show "a market's tendency," not a validated system [[street-smarts-laurence-connors]]. Every other source in this category rests on annotated chart examples, and several — Boucher's "85% of 1,300 runaway markets," Bressert's "up to 90% accurate," the toolkit's "75% of the time" — assert frequencies with no reproducible method [[marc-boucher-short-term-trading-course--runaway-market-tbblbg-breakouts]] [[walter-bressert-intraday-timing-for-low-risk-swing-trading]] [[jan-l-arps-surfing-the-market-waves-the-swing-trader-s]].
