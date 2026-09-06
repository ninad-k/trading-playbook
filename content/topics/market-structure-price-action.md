---
title: Market Structure & Price Action
summary: "Reading the market from price alone — auction theory, point-and-figure, swings and pivots — plus the exchange plumbing that determines what a fill actually costs."
books_covered: 36
---
## What it is

This category covers two things that usually get separated but belong together. The first is price action: methods that derive structure from price alone — trends as sequences of peaks and troughs, support and resistance, swing pivots, point-and-figure columns, Market Profile distributions — without an indicator layer between the trader and the chart. The second is market structure in the literal sense: how exchanges, market makers, ECNs and order types work, and therefore why a market order fills where it does. The connection is that most price-action rules are claims about where other participants have orders. A level matters because it is watched; a stop gets hit because it sits where stops cluster. Knowing how orders reach the book is part of knowing what the chart is showing.

## Core principles

- A trend is a sequence of rising peaks and rising troughs (or falling ones), and a reversal is not confirmed until both sequences change — a break in only one is a half-signal [[peaks-and-troughs-pring]] [[john-j-murphy-charting-made-easy]].
- Broken resistance becomes support and vice versa, because traders caught on the wrong side cover near their old entry while new entrants add on the retest [[introduction-to-charting]] [[john-j-murphy-charting-made-easy]].
- A trendline drawn through two points is only a candidate; a third touch that holds is what validates it [[john-j-murphy-charting-made-easy]] [[common-sense-commodities-a-common-sense-approach-to-trading-commodities]].
- Establish trend on the higher timeframe first and use the lower one only to time the entry [[introduction-to-charting]] [[mulitple-patterns-and-time-periods]].
- Markets spend most of their time not trending — estimates in this category range from roughly 70% to 80% of the time in congestion — so regime classification comes before tool selection [[triangletradingmethod]] [[congestion-markets-estimating-a-breakout-target]] [[trend-vs-no-trend]].
- Filtering noise requires an explicit threshold. Point-and-figure uses box size and a three-box reversal; kagi and renko use a turnaround amount or brick height; three-line break lets the market itself set the reversal by requiring a break of three prior lines [[tom-dorsey-s-trading-tips-a-playbook-for-stock-market-success--point-and-figure-and-bullish-percent-system]] [[beyond-candlesticks-steve-nison--kagi-chart]] [[beyond-candlesticks-steve-nison--three-line-break-chart]].
- Discarding time makes structure legible. Point-and-figure, kagi, renko and three-line break all drop the time axis or plot only on new extremes, which is what makes support and resistance visually obvious [[the-forex-chartist-companion]] [[beyond-candlesticks-steve-nison--renko-chart]].
- Price is the byproduct of a two-sided auction between a short-term participant who needs a fair price now and a longer-term one who can wait for an advantageous price; volume distributed across price reveals which is active [[cbot-a-six-part-study-guide-to-market-profile]].
- Value has a measurable definition: the price range containing about 70% of a session's volume, roughly one standard deviation of the distribution [[cbot-a-six-part-study-guide-to-market-profile--market-profile-construction-and-reading]].
- Pattern rules can be made explicit enough to remove most discretion — bar counts, tick tolerances, minimum durations — which is what separates Ross's Law of Charts from ordinary chart reading [[joe-ross-how-to-spot-a-trend]] [[triangletradingmethod]].
- Confirmation across independent factors matters more than the precision of any one: Murphy's closing principle is that a signal is worth what the number of agreeing factors makes it worth [[john-j-murphy-charting-made-easy]].
- Order type determines which risk you accept: a market order guarantees a fill but not a price, a limit order the reverse, and a triggered stop becomes a market order [[nasdaq-education-foundation-a-guide-to-u-s-stock-markets-eng]] [[how-the-stock-market-works]].
- Clearing and settlement, not the trade itself, account for most of the value chain in an exchange group — the part traders never see [[deutsche-borse-group-from-trading-floor-to-virtual-marketplace]].
- Structure changes what the old rules mean: wider intraday ranges, commodity-like institutional turnover and derivatives-driven pricing make previously stable patterns less reliable [[michael-panzner-the-new-laws-of-the-stock-market-jungle]].
- Almost none of the pattern claims here are tested; where they are, results are sobering — double and triple tops in currencies come out close to a coin flip [[the-forex-chartist-companion]].

## Concrete rules and setups

### Trend and swing structure

1. Label an uptrend while peaks and troughs both rise; a failed new high is an alert, but the reversal is confirmed only when price also breaks the previous trough [[peaks-and-troughs-pring]].
2. Treat a reaction as meaningful when it retraces roughly one-third to two-thirds of the prior move, or when a shallower range lasts one-third to two-thirds of the prior move's duration [[peaks-and-troughs-pring]]. Murphy gives the same bands: a third minimum, 50% most common, two-thirds maximum consistent with the trend resuming [[john-j-murphy-charting-made-easy]].
3. Ross's 1-2-3: point 1 is the prior swing extreme, point 2 requires a full correction, point 3 requires another. The formation is void the moment any bar reaches or passes point 1 [[joe-ross-how-to-spot-a-trend]].
4. Ross's ledge: four to ten bars containing two matching highs and two matching lows, each pair separated by at least one bar, matched within three minimum ticks, forming inside an existing trend [[joe-ross-how-to-spot-a-trend]].
5. Ross's sideways taxonomy: ledges up to 10 bars, congestion of 11-20 bars, trading ranges of 21 or more, with range breakouts usually falling around bars 21-29 [[joerosstrading-manual-appendices-269-320]].
6. Ross Hook: the first correction after a breakout of a 1-2-3, ledge, congestion or trading range. Enter on the Hook's breakout; the Trader's Trick enters earlier, on a violation of the high of the first correction bar, but only if the distance to the Hook covers costs and leaves profit — abandon the attempt after three correction bars [[joerosstrading-manual-appendices-269-320]].
7. The 1-2-3 as a standalone signal: enter on a break of the horizontal line at the point-2 level, placed slightly inside it rather than exactly on it, to avoid the clustered breakout orders [[e123system]].
8. Wolfe Wave: require points 1-4 to exist, with point 3 below point 1 and point 4 above it for a buy. Project point 5 with the 1-3 line, enter on a reversal back across it, stop beyond the point-5 extreme, and use the 1-4 line as the estimated price at arrival [[wolfe-waves]].

### Point-and-figure

9. Box size scale (Dorsey Wright): ¼ point from $0-5, ½ point from $5-20, 1 point from $20-100, 2 points from $100-200, 4 points above $200, with a three-box reversal to start a new column [[tom-dorsey-s-trading-tips-a-playbook-for-stock-market-success--point-and-figure-and-bullish-percent-system]].
10. Forex parameters: one pip per box for major pairs, two to five for wide-spread crosses, with a three-box reversal as the default [[the-forex-chartist-companion--point-and-figure-breakout-trading]].
11. Trendline signal: buy when a new column of Xs crosses above the declining line drawn along the downtrend's highs, entering at the first X above the prior X-column high; mirror for sells [[the-forex-chartist-companion--point-and-figure-breakout-trading]].
12. Bullish percent: the share of a universe on a P&F buy signal, plotted 0-100%. Above 70% is high risk, below 30% low risk; the best buys come from a reversal up out of below 30%, the best sells from a reversal down through 70% [[tom-dorsey-s-trading-tips-a-playbook-for-stock-market-success--point-and-figure-and-bullish-percent-system]].
13. Dorsey's four-step sequence: market bullish percent, then sector bullish percent and relative strength, then fundamentals, then the individual chart — buying only above the bullish support line and requiring at least 2:1 reward to risk [[tom-dorsey-s-trading-tips-a-playbook-for-stock-market-success]].
14. Dorsey's sizing and profit-taking: risk exactly 1% of equity per position, with share count derived from the stop distance (a $1,000,000 account, $49 entry, $45 stop gives 2,500 shares), then sell a third at +30%, a third at +50%, and trail the rest [[tom-dorsey-s-trading-tips-a-playbook-for-stock-market-success]].

### Market Profile

15. Build the profile by assigning each time bracket a letter and recording it at every price traded in that bracket; stacked letters form the distribution [[cbot-a-six-part-study-guide-to-market-profile--market-profile-construction-and-reading]].
16. The initial balance is the range while only the short-term participant is active, conventionally the first hour, and needs re-tuning for near-24-hour electronic sessions [[cbot-a-six-part-study-guide-to-market-profile--market-profile-construction-and-reading]].
17. Classify the day by range extension against that balance: 85% of range inside it is a Normal day; extension up to about 2× in one direction is a Normal Variation; well beyond 2× with a close on the extreme is a Trend day; extension both ways is a Neutral day and carries the highest reversal risk [[cbot-a-six-part-study-guide-to-market-profile--market-profile-construction-and-reading]].
18. Compute the value area by starting at the highest-volume price and repeatedly adding whichever adjacent price carries more volume until 70% of session volume is captured [[cbot-a-six-part-study-guide-to-market-profile]].

### Breakouts, congestion and targets

19. Congestion targets: the measured move adds or subtracts the range's height from its boundary; the time-based method subtracts the number of days the congestion took to form; the Andrews method divides the range into eighths and multiplies the range by the count of zone re-entries [[congestion-markets-estimating-a-breakout-target]].
20. Symmetrical triangle validity: at least 28 days, two reference points on each trendline, and an apex falling in the centre third of the base [[triangletradingmethod]].
21. Channel projection: draw the trendline, duplicate it to the opposite extreme, then measure the perpendicular width and project it from a retracement point to estimate where a pullback halts, or from a breakout as a target [[channeltrading]].
22. Andrews' Pitchfork: take three reversal points A, B and C, draw A-B, run the median line from C through its midpoint, and project parallels from A and B [[andrews-pitchfork]].
23. Gap screen: require today's low above yesterday's high, plus abnormal volume, prior low volatility and dollar volume of at least $250,000; treat the gap's base as support and reassess if it is penetrated [[using-up-gaps-to-anticipate-upward-price-moves]].
24. Gimmee bar: with 20-bar, 2σ Bollinger Bands in a range, sell one tick below the low of a bearish reversal bar after an upper-band touch (or buy one tick above a bullish one at the lower band); stand aside if the extreme is near the middle average, the bar is unusually large, or the next bar gaps beyond it [[gimmibar]].
25. Regime filter: mark daily and weekly trendlines first, then treat ADX above 25 as trending and below 20 as not, confirming a DI crossover only when price exceeds that period's high or low [[trend-vs-no-trend]].
26. Stops belong at odd price points rather than round numbers, which price tends to touch before turning [[common-sense-commodities-a-common-sense-approach-to-trading-commodities]].

## Common mistakes

- Calling a reversal on a failed high alone, before the opposite swing has actually broken [[peaks-and-troughs-pring]].
- Reading the daily chart in isolation without establishing the higher-timeframe trend first [[introduction-to-charting]] [[mulitple-patterns-and-time-periods]].
- Applying trend-following tools in a range or oscillators in a trend, instead of classifying the regime first [[trend-vs-no-trend]] [[triangletradingmethod]].
- Placing stops at round numbers where everyone else's sit [[common-sense-commodities-a-common-sense-approach-to-trading-commodities]] [[e123system]].
- Adding to winners in a way that raises average risk — pyramiding rather than keeping weight on the original entry [[common-sense-commodities-a-common-sense-approach-to-trading-commodities]].
- Chasing a breakout that was missed instead of waiting for the next setup [[triangletradingmethod]].
- Treating a P&F double or triple top as an edge when the measured continuation rate is near a coin flip [[the-forex-chartist-companion]].
- Trusting a pattern-recognition claim with no target, invalidation level or failure discussion attached [[metastock-chart-patterns-tutorial]] [[fractal]].
- Assuming a seasonal or technical regularity still holds after it became widely known [[michael-panzner-the-new-laws-of-the-stock-market-jungle]].
- Using market orders in fast or thin conditions, where a triggered stop can fill far past its level [[how-the-stock-market-works]] [[nasdaq-education-foundation-a-guide-to-u-s-stock-markets-eng]].
- Mistaking a pattern's mathematical vocabulary — fractals, chaos, wavelets — for evidence that it has been tested [[fractal]].

## Best books for this topic

1. [[cbot-a-six-part-study-guide-to-market-profile]] — the exchange's own account of auction theory, day types and the value area; the most conceptually complete framework here, though it deliberately gives no trade signals.
2. [[tom-dorsey-s-trading-tips-a-playbook-for-stock-market-success]] — point-and-figure with actual numbers: box scales, bullish percent thresholds, worked position sizing at 1% risk and a specific profit-taking schedule.
3. [[john-j-murphy-charting-made-easy]] — the clearest short primer on trends, patterns, targets and retracement bands. Conventional practice stated well, with no testing.
4. [[the-forex-chartist-companion]] — unusual for actually measuring its claims against a large tick database, and candid when the numbers are unimpressive. A charting reference, not a system.
5. [[joe-ross-how-to-spot-a-trend]] and [[joerosstrading-manual-appendices-269-320]] — the most rigorously specified price-action rules in the library, with bar counts and tick tolerances that remove most of the usual ambiguity.
6. [[peaks-and-troughs-pring]] — a few pages, and the cleanest statement of what actually constitutes a confirmed trend change.
7. [[nasdaq-education-foundation-a-guide-to-u-s-stock-markets-eng]] — the best explanation of how an order really gets filled, written by an academic rather than a vendor.
8. [[profitfromprices]] — rule-based signals built from raw OHLC and volume, with explicit conditions and stops rather than named patterns.
9. [[michael-panzner-the-new-laws-of-the-stock-market-jungle]] — useful counterweight: a practitioner's argument for why the older structural assumptions behind many of these methods no longer hold.
10. [[wolfe-waves]] — a compact, well-specified geometric pattern with entry, stop and projected target defined together, which most pattern sources omit.

## Open debates

- **Whether technical structure works because it forecasts or because it is watched.** The reflexive argument is that enough participants act on the same levels to make the collective reaction the tradable event, with "winning" traders fading the moves the crowd's stops create [[doestawork]]. The auction-theory view instead grounds levels in where volume actually transacted, independent of who is watching [[cbot-a-six-part-study-guide-to-market-profile]].
- **How much discretion a pattern method should retain.** Ross reduces pattern recognition to bar counts and tick tolerances [[joe-ross-how-to-spot-a-trend]]; Market Profile deliberately declines to mechanise day-type recognition while the day is forming [[cbot-a-six-part-study-guide-to-market-profile--market-profile-construction-and-reading]]; the Andrews and Wolfe methods leave pivot selection to judgement, which is where most of their variance lives [[andrews-pitchfork]] [[wolfe-waves]].
- **Which timeframe is tradable at all.** One primer calls day trading categorically the worst way to trade because shorter frames are more random, asserting it without data [[introduction-to-charting]]; the multi-timeframe and Market Profile traditions treat intraday structure as readable given the right framework [[mulitple-patterns-and-time-periods]] [[cbot-a-six-part-study-guide-to-market-profile]].
- **Whether breakout targets can be projected at all.** Three incompatible methods are offered for the same congestion range — measured move, time-based, and an eighths-and-re-entries count — with no comparison between them [[congestion-markets-estimating-a-breakout-target]], and the channel-projection technique adds a fourth [[channeltrading]].
- **How much risk a price-action setup justifies.** Dorsey fixes 1% per position [[tom-dorsey-s-trading-tips-a-playbook-for-stock-market-success]]; the 1-2-3 report allows 3% with a 10% stop [[e123system]]; most of the category gives no figure at all [[andrews-pitchfork]] [[channeltrading]] [[wolfe-waves]].
- **Whether structural change has invalidated the older reading.** Panzner argues wider ranges, derivative-driven pricing and institutional turnover have degraded traditional indicators and seasonals [[michael-panzner-the-new-laws-of-the-stock-market-jungle]]; the pit-era frameworks in this category — half-hour brackets, floor specialists, CTI-classified volume — assume a market structure that has since been replaced [[cbot-a-six-part-study-guide-to-market-profile]] [[nasdaq-education-foundation-a-guide-to-u-s-stock-markets-eng]].

**Category note:** [[economics-how-the-stock-market-works]] and [[how-the-stock-market-works]] are two copies of the same Bradley tutorial and should be reconciled to one page.
