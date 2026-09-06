---
title: Trend Following & Mechanical Systems
summary: "Buy strength, cut losses, size by volatility, accept a 30-40% win rate — the library's most testable category, and the one where curve-fitting does the most damage."
books_covered: 80
---
## What it is

Trend following makes no forecast. It waits for price to establish a direction, gets aboard once the move confirms itself, and stays until price says the move is over — never buying the low or selling the high. Its statistical basis is that price runs are not distributed like coin flips: there are fewer short streaks and more long ones than randomness predicts, and that fat tail is what the strategy harvests. The consequence is a payoff shape most traders find intolerable — roughly 60-75% of trades lose, small and fast, while a handful of large winners pay for everything. Around that core sits the wider discipline of mechanical system building: translating an idea into exact rules, testing it across many markets and years, and defending against the ever-present risk that the backtest is fitted to noise rather than to a real effect.

## Core principles

- Price is the only input. Trend followers explicitly reject forecasts, fundamentals and news as trading inputs [[michael-covel-trend-following]] [[turtletrader]] [[trading-as-a-business]].
- Expect a low win rate and a right-skewed payoff: 30-40% winners for the CTAs Covel profiles, 49.3% with a 2.56 win/loss ratio in the Wilcox and Crittenden equity study [[michael-covel-trend-following]] [[does-trendfollowing-work-on-stocks]].
- Conservation of capital: many small losses funding a few large gains, with average loss and average holding time far below the winners' [[a-short-course-in-technical-trading]] [[curtis-faith-way-of-the-turtle]].
- Never set a profit target. Targets cap exactly the trades the strategy depends on; exit on a trailing signal instead [[michael-covel-trend-following]] [[turtlerules]].
- Size by volatility, not by dollars or share count, so a fixed adverse move costs the same percentage in every market — the mechanism that makes real diversification possible [[turtlerules--turtle-system]] [[curtis-faith-way-of-the-turtle]] [[a-short-course-in-technical-trading]].
- Stops must scale with volatility. A stop tighter than the trend's own noise fights the system rather than protecting it [[a-short-course-in-technical-trading]] [[mechanical-trading-systems]].
- Simple and robust beats optimised: use the same one or two parameter sets across many unrelated markets, and accept losing in some, rather than tuning market by market [[george-pruitt-building-winning-trading-systems-with-tradestation]] [[mechanical-trading-systems]].
- A robust system's performance should not change much when a parameter is nudged; sensitivity to a specific value is evidence of fitting [[the-complete-turtletrader-the-legend-the-lessons-the-results]] [[perry-kaufman-smarter-trading]].
- Build laterally: entry, profit-taking, stop and sizing should each stand alone and be tested separately, so one invalid assumption does not collapse the whole structure [[perry-kaufman-smarter-trading]].
- Test on more data, not less — a system tested on three years has not yet seen its worst drawdown, and short windows systematically underrepresent price shocks [[perry-kaufman-smarter-trading]].
- Normalise system comparisons to a fixed maximum drawdown rather than comparing raw returns [[perry-kaufman-smarter-trading]] [[jack-schwager-guide-to-winning-with-automated-trading-systems-course-manual]].
- Reserve genuinely out-of-sample data; Weissman abandons a system whose post-optimisation drawdown exceeds its in-sample figure by more than 15% [[richard-l-weissman-mechanical-trading-systems]] [[george-pruitt-building-winning-trading-systems-with-tradestation]].
- The system must be trend-following *or* mean-reverting by design, because each is built for a regime the other loses in [[jack-schwager-guide-to-winning-with-automated-trading-systems-course-manual]] [[mechanical-trading-systems]].
- Markets spend most of their time not trending — Weissman estimates about 70%, Hill and Pruitt about 85% — which is why the strategy's flat periods are structural rather than a malfunction [[richard-l-weissman-mechanical-trading-systems]] [[j-r-hill-g-pruitt-and-l-hill-the-ultimate-trading-guide]].
- Deep drawdowns are the price of the edge, not evidence it has broken; enduring them is the real risk-management problem [[the-complete-turtletrader-the-legend-the-lessons-the-results]] [[michael-covel-trend-following]].
- The rules are not the hard part. Several Turtles had the identical rulebook and still lost money [[turtlerules]] [[curtis-faith-way-of-the-turtle]].

## Concrete rules and setups

### The Turtle system

1. N = the 20-day exponential average of true range. Unit = (1% of account equity) ÷ (N × dollars per point), truncated to whole contracts [[turtlerules--turtle-system]].
2. Entries: one tick beyond the 20-day high or low (System 1) or the 55-day high or low (System 2). System 1 skips a signal when the prior System 1 trade won, with System 2 as the failsafe that still catches the trend [[turtlerules--turtle-system]] [[the-complete-turtletrader-the-legend-the-lessons-the-results--turtle-trading-system]].
3. Stop: 2N from entry, raised to the newest unit's level as units are added — capping a single unit near 2% of equity [[turtlerules--turtle-system]].
4. Pyramiding: add one unit every ½N of favourable movement, to a maximum of four units per market, with correlation limits of 4/6/10/12 units across related markets, one market and total direction [[turtlerules--turtle-system]].
5. Exits: a 10-day opposite breakout for System 1, 20-day for System 2 [[curtis-faith-way-of-the-turtle--turtle-system]].
6. Drawdown response: cut the notional account by 20% for every 10% of equity lost, so exposure shrinks automatically during losing runs [[turtlerules]].

### Breakout and moving-average systems

7. N-day rolling breakout, three variants of increasing strictness: buy any new N-day high; require the *close* to make the new high, avoiding one-tick false breaks; or require the new high plus a close above yesterday's close. 20-day and 30-week are common defaults [[a-short-course-in-technical-trading--n-day-breakout-system]].
8. Kaufman's moving-average rule: enter or reverse when the average itself turns, comparing today's value to yesterday's, rather than when price crosses it [[a-short-course-in-technical-trading--two-moving-average-system]].
9. King Keltner: a 40-day average of (H+L+C) as the centreline with bands at ±40-day ATR. Go long on a stop at the upper band only when the centreline is rising, short at the lower band when falling, and exit at the centreline whether winning or losing [[george-pruitt-building-winning-trading-systems-with-tradestation--king-keltner]].
10. Bollinger Bandit: 50-day bands at ±1.25 standard deviations, filtered by a 30-day rate of change, with a liquidation counter starting at 50 and decrementing each day a trade stays open [[george-pruitt-building-winning-trading-systems-with-tradestation--bollinger-bandit]].
11. Dynamic Break Out II: adapt the lookback daily by the change in 30-day volatility — lookback × (1 + delta volatility) — clipped to a 20-60 day band, with 2σ Bollinger levels recomputed at the current lookback [[george-pruitt-building-winning-trading-systems-with-tradestation--dynamic-break-out-ii]].
12. Thermostat: compute a 30-bar Choppy Market Index; below 20 use the swing rules, at or above 20 use the trend rules — regime detection built into the system rather than applied by the trader [[george-pruitt-building-winning-trading-systems-with-tradestation--thermostat]].
13. KAMA: efficiency ratio = |net change over the period| ÷ the summed absolute daily changes, mapping onto a smoothing constant bounded by a fast and slow speed, so the average accelerates in directional markets and flattens in noise [[perry-kaufman-smarter-trading--adaptive-moving-average-kama]].
14. Weissman's crossovers: 9/26 two-MA stop-and-reverse; adding a 52-period line for a three-MA version requiring 9 > 26 > 52 with a neutral state when misaligned. The two-MA system tested 1992-2002 across ten markets returned 8.48% annualised with a 19.98% maximum drawdown, 61.18% losing trades and ten consecutive losses [[richard-l-weissman-mechanical-trading-systems--two-moving-average-crossover]].
15. Wilcox and Crittenden's equity system: buy tomorrow's open when today's close is the highest in the stock's entire history, exit on a 10× ATR trailing stop, filtered to stocks above $15 with adequate dollar volume, deducting at least 0.5% round-turn. Expectancy about 15.2% per trade over a 305-day average hold — and explicitly not to be applied short [[does-trendfollowing-work-on-stocks]].

### Price-structure systems

16. Darvas box: track daily high, low and close, treat the box as confirmed when price fails to break its ceiling or floor for three consecutive days, then buy an on-stop order above the ceiling into the next box — never on dips inside it [[how-i-made-2-million-in-the-stock-market--box-theory]].
17. Livermore's top-down sequence: establish the market's direction, confirm the industry group agrees, confirm a sister stock shows the same pattern, then check the individual stock. Trade only leaders in leading groups [[richard-smitten-trade-like-jesse-livermore-2005--pivotal-point-trading]].
18. Livermore's five money rules: probe rather than committing at once, never lose more than 10% on a trade, always hold a cash reserve, require a specific reason to sell rather than selling because there is a profit, and move roughly half of a windfall out of the trading account [[richard-smitten-trade-like-jesse-livermore-2005]].
19. Ross Hook: trade hooks only inside an established trend, entering one tick beyond the hook's extreme, with stops at natural support and resistance and a trail behind each new correcting bar's extreme [[joe-ross-trading-the-ross-hook--ross-hook-system]].
20. Profitunity: build the Alligator from a 13-bar smoothed average offset 8 bars, an 8-bar offset 5, and a 5-bar offset 3. Take no signal until price produces its first fractal breakout outside the Alligator's mouth, then only buy above it and only sell below [[bill-williams-new-trading-dimensions-how-to-profit-from-chaos-in-stocks-bonds-and-commodit--profitunity-alligator-system]].
21. Moving Average Channel: a 10-day average of highs and an 8-day average of lows, with the trend confirmed after two or more consecutive closes outside the channel; buy at the channel low in a confirmed uptrend [[jake-bernstein-stock-market-strategies-that-work--moving-average-channel-mac]].

### Timing and filter overlays

22. Best Six Months: buy a broad index on 1 November and move to cash on 30 April. On the DJIA from 1950-2001, a $10,000 stake gained $457,103 across the November-April periods and lost $77 across all the May-October ones [[leslie-n-masonson-all-about-market-timing--best-six-months-strategy]].
23. The MACD overlay on the same calendar: take the first MACD buy crossover on or after 16 October and the first sell crossover on or after 20 April, using the dates only as a fallback [[leslie-n-masonson-all-about-market-timing--best-six-months-strategy]].
24. COT Index = (this week's net position − the lowest in the lookback) ÷ (the highest − the lowest), over three years. Above 80% marks unusually heavy commercial buying, below 20% heavy selling; the public index is read inverted, shorting above 75% and buying below 25%. It shows what, not when, so it requires a trend filter [[williams-larry-trade-stocks-and-commodities-with-the-insiders]].
25. Murphy's regime filter: a rising ADX favours moving averages, a falling ADX favours oscillators [[trading-strategies-john-murphy-s-ten-laws-of-technical-trading]].
26. Kee's array: buy when support is tested or resistance breaks higher, short when resistance is tested or support breaks lower, with "tested" defined as within 0.05 points for a stock, 3 for the NASDAQ, 25 for the Dow [[buy-and-hold-is-dead--array-trading-system]].

### Sizing and capitalisation

27. Risk 1-2% of equity per position, sized from the stop distance rather than from margin. At 1% per trade it takes roughly 47 consecutive losses to reach a 37.5% account-level drawdown stop, against only 12 at 4% [[richard-l-weissman-mechanical-trading-systems]] [[mechanical-trading-systems]].
28. Seykota's heat: total open risk across all positions, so 2% on each of five positions is 10% heat [[michael-covel-trend-following]].
29. Hill and Pruitt's ruin arithmetic: PR = ((1−TA)/(1+TA))^IU, where TA is win% minus loss% and IU is capital divided by bet size — near 45% eventual ruin at a 10% edge with four units, under 2% at twenty [[j-r-hill-g-pruitt-and-l-hill-the-ultimate-trading-guide]].
30. Wright's ANP Pyramid: capitalise at three times the strategy's historical maximum intraday drawdown plus margin, trade one contract on personal capital, and add contracts funded only from accumulated net profit, dropping back to one when that profit falls toward zero [[trading-as-a-business--set-up-and-entry-with-anp-pyramid]].
31. Equalise dollar volatility across portfolio holdings rather than share counts or dollar values [[a-short-course-in-technical-trading]].

## Common mistakes

- Setting a profit target, which truncates the small number of trades the whole expectancy depends on [[michael-covel-trend-following]] [[turtlerules]].
- Optimising parameters per market, producing a system fitted to noise rather than to a principle [[george-pruitt-building-winning-trading-systems-with-tradestation]] [[richard-l-weissman-mechanical-trading-systems]].
- Judging a system on net profit alone rather than reading the whole performance report — maximum drawdown and required account size define what it actually costs to trade [[jack-schwager-guide-to-winning-with-automated-trading-systems-course-manual]].
- Testing on a short, recent window, which has not contained enough price shocks to reveal the real drawdown [[perry-kaufman-smarter-trading]].
- Setting a stop tighter than the trend's own noise, so the system stops itself out of the moves it was built to catch [[a-short-course-in-technical-trading]].
- Skipping or slowing unit additions to feel safer, which the Turtle rules note actually reduces returns because slower entries let normal retracements reach the stop [[turtlerules]].
- Abandoning the system during the drawdown it was always going to have [[the-complete-turtletrader-the-legend-the-lessons-the-results]] [[curtis-faith-way-of-the-turtle]].
- Increasing size after losses on the belief a win is due — the failure mode in the cited experiment where only two of forty players finished ahead in a 60%-win-rate game [[turtletrader]].
- Averaging down, which Weissman classes as a Martingale strategy and a near-certain path to ruin [[richard-l-weissman-mechanical-trading-systems]] [[trading-strategies-john-murphy-s-ten-laws-of-technical-trading]].
- Sizing a new position as if it were independent when it correlates with an existing one [[richard-l-weissman-mechanical-trading-systems]] [[turtlerules--turtle-system]].
- Running a trend system on a single market, where it can go years without profit and needs a basket to be viable [[george-pruitt-building-winning-trading-systems-with-tradestation]].
- Applying a counter-trend band system in a strong trend, or a breakout system in chop, without knowing which regime the system was built for [[jack-schwager-guide-to-winning-with-automated-trading-systems-course-manual]].
- Trading a single contract, which Ross treats as gambling rather than trading because it removes all scaling flexibility [[joe-ross-trading-the-ross-hook]].

## Best books for this topic

1. [[turtlerules]] — the primary source: the actual 1983 rules, free, complete enough to code, and corroborated by two independent later accounts.
2. [[curtis-faith-way-of-the-turtle]] — the insider's version, plus robustness statistics (RAR%, R-cubed, robust Sharpe) taught almost nowhere else.
3. [[a-short-course-in-technical-trading]] — every technique backed by a reproducible spreadsheet formula and a real backtest table rather than a chart picture. The best starting point.
4. [[george-pruitt-building-winning-trading-systems-with-tradestation]] — six complete systems with full source code and 20-year, 17-market backtests, so a reader can verify rather than believe.
5. [[richard-l-weissman-mechanical-trading-systems]] — complete codeable systems with 10-year performance tables, and an unusually honest demonstration of a top-ranked parameter set becoming the worst the following year.
6. [[perry-kaufman-smarter-trading]] — the best treatment of testing methodology and why short backtests systematically understate risk. KAMA is the durable contribution.
7. [[michael-covel-trend-following]] — the philosophy and the practitioner evidence, though the performance tables are composite and unaudited.
8. [[trading-as-a-business]] — the most concrete treatment of capitalisation and scaling, with the ANP Pyramid fully worked.
9. [[j-r-hill-g-pruitt-and-l-hill-the-ultimate-trading-guide]] — supply-and-demand chart reading plus genuine risk-of-ruin arithmetic, with stated commission and test-period assumptions throughout.
10. [[leslie-n-masonson-all-about-market-timing]] — nearly every claim tied to a named, checkable backtest; the honest counterweight to buy-and-hold.
11. [[does-trendfollowing-work-on-stocks]] — the clearest single piece of evidence that the futures logic transfers to equities, with the caveat that its publisher sells the strategy.
12. [[how-i-made-2-million-in-the-stock-market]] — the earliest complete breakout-plus-trailing-stop method in this library: Darvas's boxes are channel breakouts by another name, run entirely from a hotel telegram with a stop that only ever moves up.
13. [[jake-bernstein-stock-market-strategies-that-work]] — the Moving Average Channel (a 10-day average of highs against an 8-day average of lows) is a usefully different way to define a trend without a crossover, paired with a momentum/moving-average filter.
14. [[jake-bernstein-trade-your-way-to-riches]] — the Key Date Seasonal method, notable because it publishes the full year-by-year trade table rather than a summary win rate; read it alongside the data-mining warning below.
15. [[bill-williams-trading-chaos]] — the fractal-and-Alligator framework: a five-bar fractal breakout filtered by three displaced smoothed averages, with the 5/34 oscillator for confirmation. The chaos-theory framing is decoration; the rules underneath are ordinary and codeable.
16. [[buy-and-hold-is-dead]] — a demographic model of investment demand used to argue when trend systems will have trends to follow at all.

A note on two of these: [[jake-bernstein-trade-your-way-to-riches]] and [[bill-williams-trading-chaos]] both wrap a conventional rule set in a distinctive vocabulary — calendar seasonality in one case, chaos theory in the other. Strip the vocabulary and test what remains.

## Open debates

- **Whether the entry rules matter at all.** Faith says the Turtles' entries were well known by 1983 and unimportant next to execution [[curtis-faith-way-of-the-turtle]]; the TurtleTrader site attributes 90% of the result to money management [[turtletrader]]; yet both reprint a parameter-specific rule set in full, and Weissman's own in-sample/out-of-sample comparison shows parameter choice changing results dramatically [[richard-l-weissman-mechanical-trading-systems]].
- **Whether optimisation is legitimate.** Wright treats it as a core skill and optimises the money-management stop directly [[trading-as-a-business]]; Pruitt and Hill deliberately refuse to optimise per market, treating a system that needs different settings for yen and cattle as fitted to noise [[george-pruitt-building-winning-trading-systems-with-tradestation]]; Kaufman's answer is to test a neighbourhood of parameters rather than a point [[perry-kaufman-smarter-trading]].
- **Whether stops improve returns.** Kaufman's own tests across markets found stop size had inconsistent and often minimal effect on long-run return once normalised to a fixed drawdown — stops reshape risk rather than reliably adding expectancy [[perry-kaufman-smarter-trading]]; the Turtle and Weissman frameworks make the stop the load-bearing element of the whole design [[turtlerules--turtle-system]] [[richard-l-weissman-mechanical-trading-systems]].
- **Whether a fixed percentage risk rule belongs in a system at all.** Weissman, Covel and the Turtles all specify one [[richard-l-weissman-mechanical-trading-systems]] [[michael-covel-trend-following]]; Bill Williams singles out "never risk over 2 percent" as an ungrounded assessment to be discarded in favour of market-generated stops, and gives no sizing formula anywhere [[bill-williams-new-trading-dimensions-how-to-profit-from-chaos-in-stocks-bonds-and-commodit]].
- **Whether regime should be detected or accepted.** Thermostat switches rule sets on a choppiness index [[george-pruitt-building-winning-trading-systems-with-tradestation--thermostat]] and Murphy switches indicator families on ADX [[trading-strategies-john-murphy-s-ten-laws-of-technical-trading]]; the Turtle and Donchian tradition simply accepts the losing regime as the cost of being positioned when the trend arrives [[turtlerules]].
- **Whether adaptation beats fixed parameters.** KAMA and Dynamic Break Out II both vary their speed with measured volatility [[perry-kaufman-smarter-trading--adaptive-moving-average-kama]] [[george-pruitt-building-winning-trading-systems-with-tradestation--dynamic-break-out-ii]]; the fixed-parameter systems in the same Pruitt book test just as well across the same basket, and neither book compares the two approaches directly.
- **What the evidence actually shows.** Pruitt, Weissman, Masonson and Wilcox all publish dated, parameterised backtests [[george-pruitt-building-winning-trading-systems-with-tradestation]] [[does-trendfollowing-work-on-stocks]]; none includes a true walk-forward with portfolio-level drawdown, most report per-market rather than combined equity curves, and the Wilcox portfolio curve is explicitly hypothetical with undisclosed risk mechanics. Covel's tables are manager-reported and unaudited [[michael-covel-trend-following]]. The category is the library's most testable and still largely untested.
