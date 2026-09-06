---
title: Glossary
summary: "Working definitions of the vocabulary used across this library, grouped by subject, with the pages where each term is developed."
books_covered: 0
---
Terms are grouped by subject rather than alphabetised, because most of them only make sense next to their neighbours. Where sources disagree on a definition, the disagreement is noted — that is usually the interesting part. Each entry links to pages where the term is actually used rather than merely mentioned.

## Risk, sizing and expectancy

**Expectancy** — the average amount won or lost per unit risked across many trades: (win rate × average win) − (loss rate × average loss). The number that decides whether a method is worth trading; win rate alone does not. [[trade-your-way-to-financial-freedom]]

**R-multiple** — a trade's result expressed as a multiple of its initial risk, where 1R is the distance from entry to the initial stop. Lets trades in different markets be compared on one scale. [[trade-your-way-to-financial-freedom]]

**Position sizing** — the rule deciding how many shares or contracts to trade, as distinct from stop placement, entry, or diversification. [[money-management-report-van-tharp]]

**Fixed-fractional sizing** — risking a constant percentage of current equity rather than a constant dollar amount, so exposure shrinks after losses and grows after gains. [[balsara-nauzer-j-money-management-strategies-for-futures-traders]]

**Fixed Ratio sizing** — Ryan Jones's alternative: the profit required to add the next contract grows in fixed proportion to the number already held, governed by a single parameter, delta. [[forex-misc-money-management-ryan-jones--fixed-ratio-position-sizing]]

**Delta (position sizing)** — in Fixed Ratio, the only free variable; a rule of thumb sets it near half the expected worst-case per-contract drawdown. Not to be confused with the option Greek. [[forex-misc-money-management-ryan-jones--fixed-ratio-position-sizing]]

**Optimal f** — the fixed fraction of the largest historical loss that maximises long-run geometric growth. Also the fraction that maximises drawdown: historical retracement at optimal f is never smaller than f itself. [[mathematicsmoneymanagement--optimal-f-and-twr-framework]]

**Kelly criterion** — the growth-optimal bet fraction derived from maximising expected log capital rather than expected capital; f = ((B+1)P − 1) ÷ B for a fixed payoff ratio B. Strictly valid only for two-outcome bets. [[kellybetting]]

**Terminal Wealth Relative (TWR)** — the product of all holding-period returns in a sequence; the objective function maximised when searching for optimal f empirically. [[mathematicsmoneymanagement--optimal-f-and-twr-framework]]

**Holding Period Return (HPR)** — one plus a trade's percentage result, so a +10% trade is 1.10. The building block of TWR. [[mathematicsmoneymanagement]]

**Geometric mean** — the Nth root of TWR; the growth factor per trade, and the correct basis for comparing compounding strategies against one another. [[mathematicsmoneymanagement]] [[vladimir-daragan-how-to-win-the-stock-market-game]]

**Risk of ruin** — the probability that equity falls far enough that trading must stop, computable from win rate, payoff ratio and the fraction of capital exposed. Only the third is under the trader's control. [[balsara-nauzer-j-money-management-strategies-for-futures-traders]]

**Drawdown** — the peak-to-trough decline in equity. Recovery is non-linear: a 50% loss needs a 100% gain, a 90% loss needs 900%. [[money-management-by-david-landry]]

**The 2% rule** — never risk more than 2% of account equity on one trade, counting commission and slippage. [[come-into-my-trading-room-elder-alexander]]

**The 6% rule** — total risk across open positions plus realised losses for the month may not exceed 6% of equity measured on the first of that month; once hit, stop trading until next month. [[come-into-my-trading-room-elder-alexander]]

**Portfolio heat** — total open risk across all positions at once, attributed to Ed Seykota; 20-25% is a common professional ceiling. [[money-management-report-van-tharp--position-sizing-models]]

**Core equity** — total equity minus the dollar risk currently open in all positions, used as the sizing base so capacity shrinks automatically as exposure grows. [[managing-your-money]]

**Anti-martingale** — increasing size as equity grows and reducing it after losses. **Martingale** is the reverse — increasing after a loss — and is treated throughout this library as a near-certain path to ruin. [[money-management-report-van-tharp]] [[richard-l-weissman-mechanical-trading-systems]]

**Pyramiding** — adding to a position that is already profitable, ideally in decreasing tranches with the stop moved up on the whole position. Distinct from averaging down. [[phantom-of-the-20-pits]]

**Averaging down** — adding to a losing position. The most consistently prohibited action in the library. [[john-mauldin-just-one-thing-twelve-of-the-world-s-best-investors-reveal-the-one-strategy-y]]

**Margin-to-equity ratio** — total initial margin on open positions divided by account equity; a fast proxy for how levered a futures book is. Above roughly 30% is aggressive. [[jay-kaeppel-the-four-biggest-mistakes-in-futures-trading]]

**Gearing** — leverage expressed as a multiple of capital; in retail forex, treated as the primary determinant of survival rather than a secondary parameter. [[the-bird-watching-lion-country]]

**Risk-to-return ratio** — the standard deviation of per-trade return divided by the average return; below 3 is favourable, above 5 should be rejected. [[vladimir-daragan-how-to-win-the-stock-market-game]]

## Trend, structure and price action

**Trend** — a sequence of rising peaks and rising troughs, or falling ones. A reversal is not confirmed until both sequences change. [[peaks-and-troughs-pring]]

**Half-signal** — a change in only one of the two swing sequences; an alert rather than a confirmed reversal. [[peaks-and-troughs-pring]]

**Support and resistance** — a prior trough or peak where price previously turned. Once decisively broken, the level tends to reverse role. [[john-j-murphy-charting-made-easy]]

**Trendline** — a line through two rising lows or falling highs; validated only by a third touch that holds. [[john-j-murphy-charting-made-easy]]

**Retracement** — a counter-move against the prevailing trend. Conventional bands run one-third to two-thirds of the prior move, with 50% most common. [[john-j-murphy-charting-made-easy]] [[peaks-and-troughs-pring]]

**Congestion** — sideways price action. Ross's taxonomy: ledges up to 10 bars, congestion of 11-20, trading ranges of 21 or more. [[joerosstrading-manual-appendices-269-320]]

**1-2-3 formation** — point 1 is the prior swing extreme, point 2 a full correction, point 3 another; the formation is void the moment any bar reaches or passes point 1. [[joe-ross-how-to-spot-a-trend]]

**Ross Hook** — the first correction after a breakout of a 1-2-3, ledge, congestion or trading range. [[joerosstrading-manual-appendices-269-320]]

**Trader's Trick Entry** — entering ahead of a breakout, on a correcting bar's extreme, only if there is enough room to the breakout point to cover costs and bank profit. [[traders-trick-entry]]

**Ledge** — Ross's precisely defined consolidation: four to ten bars containing two matching highs and two matching lows, matched within three minimum ticks, inside an existing trend. [[joe-ross-how-to-spot-a-trend]]

**NR7** — the narrowest high-low range of the last seven bars; a volatility-contraction signal with no inherent directional bias. [[alan-farley-the-master-swing-trader--coiled-spring]]

**Wiggle** — a stock's own average intraday pullback, estimated from five days of its 5-minute bars and used to size the trailing stop instead of a fixed distance. [[barry-rudd-stock-patterns-for-day-trading-and-swing-trading]]

**Box (Darvas)** — a price range a stock holds within, confirmed when it fails to break the ceiling or floor for three consecutive days; the breakout into the next box is the entry. [[how-i-made-2-million-in-the-stock-market--box-theory]]

**Cross-verification** — Farley's requirement that several independently derived levels converge at one price before a trade is taken; four overlapping signals is his highest-probability case. [[alan-farley-the-master-swing-trader--3d-charting-cross-verification]]

**Opening range** — the high and low of the session's first fixed block of time, from which most intraday breakout systems measure. [[mark-b-fisher-the-logical-trader-applying-a-method-to-the-madness--acd-method]]

**Initial balance** — in Market Profile, the range established while only the short-term participant is active, conventionally the first hour. [[cbot-a-six-part-study-guide-to-market-profile--market-profile-construction-and-reading]]

**Value area** — the price range containing about 70% of a session's volume, roughly one standard deviation of the distribution. [[cbot-a-six-part-study-guide-to-market-profile]]

**TPO (Time/Price Opportunity)** — one letter at one price in a Market Profile, recording that a price traded during a given bracket. [[cbot-a-six-part-study-guide-to-market-profile]]

**Point and figure** — a chart plotting only price as alternating columns of Xs and Os, with box size and a reversal amount (commonly three boxes) as the noise filter. [[tom-dorsey-s-trading-tips-a-playbook-for-stock-market-success--point-and-figure-and-bullish-percent-system]]

**Bullish percent** — the share of a universe currently on a point-and-figure buy signal; above 70% is high risk, below 30% low risk. [[tom-dorsey-s-trading-tips-a-playbook-for-stock-market-success]]

**Kagi, renko, three-line break** — Japanese price-only charts that print a new mark only on a qualifying move: a turnaround amount, a fixed brick height, or a break of the prior three lines respectively. [[beyond-candlesticks-steve-nison--kagi-chart]] [[beyond-candlesticks-steve-nison--renko-chart]] [[beyond-candlesticks-steve-nison--three-line-break-chart]]

**Wolfe Wave** — a five-point pattern where the 1-3 line projects the reversal point and the 1-4 line projects the target. [[street-smarts-laurence-connors--wolfe-waves]]

## Candlesticks and chart patterns

**Real body and shadow** — the open-to-close range and the extremes beyond it. A long body signals conviction, a long shadow a price rejected. [[trading-hill-arthur-introduction-to-candlesticks]]

**Doji** — open and close effectively equal; Morris's numeric threshold is an open-to-close distance under roughly 1-3% of the day's range, and it only signifies after a run of non-doji sessions. [[greg-morris-candlestick-charting-explained--pattern-catalogue-and-reliability]]

**Hammer and hanging man** — the same shape — small body, lower shadow at least twice the body, little upper shadow — read as bullish after a decline and bearish after an advance. [[trading-hill-arthur-introduction-to-candlesticks]]

**Engulfing pattern** — a body that fully covers the prior body in the opposite colour, requiring a trend already in force. [[greg-morris-candlestick-charting-explained--pattern-catalogue-and-reliability]]

**Dark cloud cover and piercing line** — two-candle reversals where the second closes past the midpoint of the first's body; Morris treats the 50% requirement as non-negotiable. [[greg-morris-candlestick-charting-explained]]

**Blending** — reducing a multi-candle pattern to one synthetic candle using the first open, the last close, and the pattern's extremes. [[trading-hill-arthur-introduction-to-candlesticks]]

**Measured move** — projecting a pattern's own height from its breakout as the target: flagpole height for a flag, head-to-neckline for a head and shoulders. [[chart-patterns-and-technical-indicators]]

**Neckline** — the boundary whose close-basis break completes a head-and-shoulders or double top or bottom. [[doubletopsandbottoms]]

**Gap taxonomy** — breakaway gaps start a move, measuring or continuation gaps mark its middle, exhaustion gaps mark its end. [[chart-patterns-tutorial]]

**Hole-in-the-wall** — Farley's category for a sharp gap down that ends an uptrend at a new high on volume exceeding the prior rally; the rally back into it rarely fills. [[alan-farley-the-master-swing-trader--hole-in-the-wall]]

## Indicators

**Moving average** — a smoothed price series; simple, weighted or exponential. Lagging by construction, since today's value is plotted against today's price. [[new-twist-on-an-old-indicator]]

**Adaptive moving average (KAMA)** — an average whose smoothing constant varies with the efficiency ratio, accelerating in directional markets and flattening in noise. [[perry-kaufman-smarter-trading--adaptive-moving-average-kama]]

**Efficiency ratio** — net directional change over a period divided by the summed absolute daily changes; 0 is pure noise, 1 perfectly directional. [[perry-kaufman-smarter-trading--adaptive-moving-average-kama]]

**True range** — the greatest of today's range, or the range including yesterday's close, so gaps count toward measured volatility. **ATR** is its average, and **N** is the Turtle name for the 20-day version. [[turtlerules--turtle-system]] [[a-short-course-in-technical-trading]]

**Bollinger Bands** — a 20-period moving average with bands at ±2 standard deviations, the multiplier scaling with the period. Actual containment is nearer 88-89% than the 95% normality implies. [[john-bollinger-bollinger-on-bollinger-band]]

**%b** — (last − lower band) ÷ (upper band − lower band): 1.0 at the upper band, 0.5 at the middle, unbounded beyond either. [[trading-bollinger-john-bollinger-bands-done]]

**BandWidth and the Squeeze** — (upper − lower) ÷ middle, and the condition of that value reaching a six-month low. A precondition for volatility expansion, carrying no direction. [[john-bollinger-bollinger-on-bollinger-band--method-i-squeeze-breakout]]

**RSI** — a bounded 0-100 momentum oscillator, 14-period by default, conventionally read at 70/30. [[wayne-a-thorp-measuring-internal-strength-wilders-rsi-indicator]]

**RSI range shift** — Cardwell's reading: RSI holds support near 40 and meets resistance near 80 in an uptrend, 20 and 60 in a downtrend; a shift between those ranges signals a trend change. [[trend-determination]]

**Failure swing** — an RSI double top above 70 followed by a break of the intervening trough, treated as a sell signal even before price turns. [[wayne-a-thorp-measuring-internal-strength-wilders-rsi-indicator]]

**MACD** — the difference between a fast and slow EMA, conventionally 12 and 26, with a 9-period signal line and a histogram of the gap between them. [[wayne-a-thorp-the-macd-a-combo-of-indicators-for-the-best-of-both-worlds]]

**ADX** — a 0-100 measure of trend strength, not direction; above 25-30 indicates trending, below indicates chop. [[adx]]

**CCI and Woodie's rules** — a trend requires six or more CCI bars on one side of zero; the Zero-Line Reject needs a retracement through at least ±100 before turning back with the trend. [[cci-manual]]

**Divergence** — price making a new extreme the oscillator does not confirm; a warning that can persist far longer than expected. [[divergence]]

**Hidden divergence** — the oscillator making a lower low while price makes a higher low in an uptrend; a continuation and re-entry signal, not a reversal. [[barbara-star-hidden-divergence]]

**Reverse divergence** — price making a lower high while the oscillator makes a *higher* high; price leads the oscillator into the turn. [[reverse-divergence-and-momentum]]

**Disparity index** — ((close − moving average) ÷ moving average) × 100; a percent-from-average oscillator with instrument-specific thresholds. [[beyond-candlesticks-steve-nison--disparity-index]]

**Elder-ray** — Bull Power (high − 13-day EMA) and Bear Power (low − 13-day EMA) plotted as histograms, traded on divergence in the direction of the EMA's slope. [[elder-alexander-trading-for-a-living--elder-ray]]

**TICK** — NYSE issues trading on an uptick minus those on a downtick; a breadth measure whose useful thresholds have shifted with market structure. [[tick]]

**Volume Spread Analysis** — reading spread against volume to infer professional activity: No Demand, No Supply, effort without result, up-thrust. [[williams-undeclared-stockmarket-secrets]]

**Accumulation/distribution** — Williams's volume-weighted flow line: (close − open) ÷ (high − low), multiplied by volume and cumulated. [[larry-williams-the-secret-of-selecting-stocks-for-immediate-and-substantial-gains--accumulation-distribution-system]]

**Multicollinearity (indicator)** — Bollinger's warning against combining indicators derived from the same underlying data and calling their agreement confirmation. [[trading-bollinger-john-bollinger-bands-done]]

## Options and derivatives

**Delta** — the change in an option's price per $1 move in the underlying; loosely, the probability of finishing in the money. [[fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed]]

**Gamma** — the rate of change of delta; largest at the money and growing toward expiration. A delta-neutral book with large negative gamma is exposed to any large move. [[hull-options-futures-and-other-derivative-securities-5th-ed]]

**Theta** — daily time decay of premium, largest for at-the-money options near expiration. [[fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed]]

**Vega** — sensitivity to a one-point change in implied volatility, largest far from expiration. [[options-essential-concepts-and-trading-strategies-2nd-edition]]

**Implied volatility** — the volatility figure that reproduces an option's market price through a pricing model. **Historical volatility** is computed from the underlying's realised price changes. [[using-volatility-in-option-tradingpart-1]]

**Percentile ranking (volatility)** — placing today's implied volatility against its own multi-hundred-day history, rather than comparing implied to historical, because some underlyings structurally trade above their realised volatility. [[lawrence-g-mcmillan-profit-with-options--volatility-based-strategy-selection]]

**Volatility skew** — the pattern of implied volatility across strikes; forward skew means higher strikes are more expensive, reverse skew the opposite. It tracks the underlying's actual fat-tailedness. [[back-to-basics-historical-option-pricing-revisited]]

**Put-call parity** — c + Ke^-rT = p + S₀; the relation that makes synthetic positions and conversions possible. [[hull-options-futures-and-other-derivative-securities-5th-ed]]

**No-arbitrage** — if two portfolios pay the same in every future state they must cost the same today; the principle underlying forward, futures and option pricing. [[rubinstein-mark-rubinstein-on-derivatives]]

**Risk-neutral valuation** — pricing a derivative as though all investors were risk-neutral, which gives the same answer as the real world because risk preferences cancel out. [[hull-options-futures-and-other-derivative-securities-5th-ed]]

**Delta neutral** — a position built so net directional exposure is zero at entry, profiting from movement, time or volatility rather than direction. [[fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed--delta-neutral-straddles-and-adjustments]]

**Straddle and strangle** — a long call and put at the same strike, or at different strikes; the basic long-volatility structures. [[fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed--delta-neutral-straddles-and-adjustments]]

**Ratio backspread** — selling fewer near-the-money options and buying more further-out ones for a net credit, with capped risk between the strikes. [[fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed--ratio-backspreads]]

**Vertical, calendar and diagonal spreads** — same expiration different strikes; same strike different expirations; and both differing. [[guy-cohen-the-bible-of-options-strategies--strategy-family-playbook]]

**Butterfly and condor** — capped-risk structures selling premium near the current price and buying protection further out; explicitly awkward to adjust and normally held to expiration. [[fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed--range-bound-premium-spreads]]

**Covered call** — selling a call against stock already owned; economically equivalent in risk to selling a cash-backed put at the same strike. [[m-wolfinger-create-your-own-hedge-fund-increase-profits-and-reduce-risk-with-etfs-and-opti]]

**Payout ratio (option writing)** — average payout divided by average premium collected. Gallacher's 1996 study across fifteen commodities found it almost exactly 1.0, implying no inherent writer's edge. [[mcgraw-hill-the-options-edge-winning-the-volatility-game-with-options-on-futures]]

**Spread (futures)** — the price difference between two related contracts, structurally hedged and therefore carrying lower margin and volatility than the outright. [[joe-ross-trading-spreads-and-seasonals]]

**Parity and spread (merger arbitrage)** — the value of the offered securities package, and the gap between it and the target's current price. [[wyser-pratte-guy-risk-arbitrage--merger-arbitrage-spread-and-deal-risk-checklist]]

## Cycles, ratios and waves

**Fibonacci ratios** — 0.618 and its inverse 1.618, from consecutive terms of the Fibonacci series. Retracements of 38.2%, 50% and 61.8%, extensions at 127%, 161.8% and 261.8%. 50% is not itself a Fibonacci ratio. [[candlesticks-fibonacci-and-chart-pattern-trading-tools]]

**Confluence** — two or more projections derived from *different* swings clustering in a narrow band; the actual signal, as opposed to a single ratio hit. [[forex-systems-research-practical-fibonacci-methods-for-forex-trading-2005]]

**Impulse and corrective wave** — a five-wave move with the larger trend and a three-wave move against it, nested at every degree. [[elliott-waves-principle]]

**The three Elliott rules** — wave 2 never retraces beyond the start of wave 1; wave 3 is never the shortest of 1, 3 and 5; wave 4 never enters wave 1's territory. Everything else is a guideline. [[elliott-waves-principle--wave-rules-and-guidelines]]

**Alternate count** — the second-best wave interpretation, maintained continuously so an invalidation leaves a working hypothesis rather than nothing. [[practicalew]]

**Gartley "222" and AB=CD** — harmonic patterns defined purely by Fibonacci ratios between the legs of an XABCD swing sequence. [[fibonacci-ratios-with-pattern-recognition--gartley-222-and-butterfly-patterns]]

**Square of Nine** — Gann's spiral of integers used as a square-root calculator, reading 90-, 180- and 270-degree rotations as candidate price levels. [[gannwheel]]

**Kondratieff, Juglar and Kitchin cycles** — nested economic cycles of roughly 50-60 years, 9-11 years and 40 months, the last associated with the US electoral calendar. [[deborah-owen-mapping-the-markets]]

**Seasonal tendency** — a recurring calendar bias measured from historical data, such as trading day of week and trading day of month. [[larry-williams-long-term-secrets-to-short-term-trading--tdw-tdm-filters]]

**Best Six Months** — holding the index from 1 November to 30 April and standing aside from May to October. [[leslie-n-masonson-all-about-market-timing--best-six-months-strategy]]

## Systems, testing and evidence

**Mechanical system** — a fully rule-based method generating signals without discretion, and therefore testable statistically. [[jack-schwager-guide-to-winning-with-automated-trading-systems-course-manual]]

**In-sample and out-of-sample** — the data a system's parameters were fitted on, and data held back to verify it. Results from the first mean little without the second. [[mcgraw-hill-encyclopedia-of-trading-strategies--test-methodology]]

**Walk-forward testing** — optimising on one segment and validating on the next untouched one, repeatedly. [[george-pruitt-building-winning-trading-systems-with-tradestation]]

**Curve fitting** — tuning a system so closely to historical data that its apparent edge is an artifact of that dataset. [[perry-kaufman-smarter-trading]]

**Robustness** — the property that a system's performance changes little when a parameter is nudged. Sensitivity to a specific value is evidence of fitting. [[the-complete-turtletrader-the-legend-the-lessons-the-results]]

**Multiple comparisons** — the inflation of apparent significance when the best of many parameter runs is reported; requires explicit correction. [[mcgraw-hill-encyclopedia-of-trading-strategies--test-methodology]]

**Random-entry baseline** — comparing a rule against random entries with the same exits, so the question becomes whether it beats chance rather than whether it made money. [[mcgraw-hill-encyclopedia-of-trading-strategies]]

**Dollar volatility equalisation** — scaling contracts per market so each contributes comparable risk, rather than trading equal contract counts. [[mcgraw-hill-encyclopedia-of-trading-strategies--test-methodology]]

**Standardised exit** — holding the exit constant while comparing entries, so the comparison measures entry quality rather than exit variation. [[mcgraw-hill-encyclopedia-of-trading-strategies--test-methodology]]

**Profit factor** — gross profit divided by gross loss. A high win rate with a profit factor near 1.0, as in the decade-long gap-fade study, means the losses are simply larger than the wins. [[andrews-scott-understanding-gaps]]

**Whipsaw** — a signal that reverses immediately, producing a small loss and a cost. The characteristic failure mode of trend systems in a range. [[richard-l-weissman-mechanical-trading-systems]]

**Stop-and-reverse** — a system always in the market, flipping directly from long to short on the opposite signal. [[chande-kroll-the-new-technical-trader--cmo-vidya-trading-system]]

**Slippage** — the difference between the intended and achieved fill. Excluded from most published results in this library, and large enough to reverse several of them. [[wayne-a-thorp-testing-trading-success]]

**Survivorship bias** — computing success statistics only from those who survived, so the base rate of skill appears far higher than it is. [[taleb-nassim-fooled-by-randomness]]

**Alternative histories** — the distribution of outcomes that could have happened, against which the one that did should be judged. [[taleb-nassim-fooled-by-randomness]]

**Negative skew** — a payoff of frequent small gains and rare large losses; produces a smooth track record right up until it does not. [[taleb-nassim-fooled-by-randomness]]

## Microstructure and execution

**Bid-ask spread** — the cost of immediacy, and the first hurdle any short-horizon edge must clear. Wyckoff's "invisible eighth". [[wyckoff-richard-d-the-day-trader-s-bible-or-my-secret-in-day-trading-of-stocks-2]]

**Market order versus limit order** — a market order guarantees a fill but not a price; a limit order the reverse. A triggered stop becomes a market order. [[nasdaq-education-foundation-a-guide-to-u-s-stock-markets-eng]]

**Depth** — the size available at each price level; the other half of liquidity alongside the spread, and inversely related to transitory volatility. [[depth-volatility]]

**Price impact** — the price movement caused by an order itself; concave in size, roughly proportional to the square root of volume rather than linear. [[supply-demand]]

**Order flow imbalance** — the net signed direction of orders, which explained roughly half of return variance on the venue studied. [[supply-demand]]

**Commonality in liquidity** — the tendency of spreads and depth to co-move across stocks, so positions correlate exactly when liquidity is needed. [[chordia-roll-and-subrahmanyam-commonality-in-liquidity]]

**Liquidity black hole** — a self-reinforcing sell-off in which private loss limits make each exit trigger the next, with no new information required. [[morris-and-song-shin-liquidity-black-holes]]

**U-shaped intraday pattern** — the concentration of volume and volatility at the open and close, produced by traders clustering to minimise their own impact — and present even in markets with no market makers. [[admati-and-pfleiderer-a-theory-of-intraday-patterns-volume-and-price-variability]]

**Upstairs market** — broker-negotiated block trading, which lowers execution cost by tapping unexpressed liquidity and certifying the trade as uninformed. [[bessembinder-and-venkataraman-does-an-electronic-stock-exchange-need-an-upstairs-market]]

**Value at Risk (VaR)** — the loss level not exceeded at a given confidence over a given horizon. Not a coherent risk measure outside elliptical distributions, biased low, and gameable. [[exploring-value-at-risk]]

**Return smoothing** — autocorrelation in reported returns from stale or illiquid pricing; removing it raises estimated volatility by 60-100% for some hedge fund styles. [[hedge-fund-risk-factors-and-value-at-risk-of-credit-trading-strategies]]

## Forex and macro

**Pip** — the smallest quoted increment in a currency pair. [[3-how-to-access-and-trade-the-world-s-biggest-market]]

**Spot and forward** — settlement within two days, and anything beyond, with forward points reflecting the interest-rate differential under covered interest parity. [[all-about-forex-market-in-usa-eng]]

**Carry trade** — buying a higher-yielding currency funded by a lower-yielding one to capture the rate differential; profitable while risk appetite holds and violent when it reverses. [[day-trading-the-currency-market--leveraged-carry-trade]]

**Risk appetite** — a composite read of whether capital is flowing toward risk assets and high-carry currencies or toward havens. [[wiley-currency-strategy-a-practitioner-s-guide-to-currency-trading-hedging-and-forecasting]]

**Signal grid** — Henderson's four disciplines — economics, flow, technicals and valuation — with a position taken only when at least three agree. [[wiley-currency-strategy-a-practitioner-s-guide-to-currency-trading-hedging-and-forecasting--signal-grid-and-active-currency-overlay]]

**COT report** — the CFTC's weekly breakdown of positioning by commercials, large speculators and small speculators. **COT Index** normalises the current net position against its own multi-year range. [[williams-larry-trade-stocks-and-commodities-with-the-insiders]]

**Median grid** — du Toit's manually drawn support-and-resistance channel on one pair, divided into quadrants as a reference for judging whether price is relatively high or low. [[the-bird-watching-lion-country--4x1-median-grid]]

**Purchasing power parity** — the proposition that exchange rates converge to relative price levels; rejected as a trading input by most surveyed FX dealers while a minority still think it binds beyond six months. [[chinn]]

## Investing and valuation

**Intrinsic value** — the present value of an asset's expected future cash flows discounted at a rate reflecting their risk. [[investment-valuation-damodaran]]

**Margin of safety** — the gap between that value and the price paid; it makes an accurate forecast unnecessary rather than guaranteeing a profit. [[the-intelligent-investor-benjamin-graham]]

**Mr. Market** — Graham's allegorical partner offering a mood-driven quote daily, to be used or ignored at the investor's convenience. [[the-intelligent-investor-benjamin-graham]]

**FCFE and FCFF** — free cash flow to equity and to the firm; the first discounted at the cost of equity, the second at the cost of capital. [[investment-valuation-damodaran--dcf-valuation-method]]

**Terminal value** — the value beyond the explicit forecast period, which dominates most DCF outputs and whose growth rate cannot exceed the economy's long-run nominal growth. [[investment-valuation-damodaran]]

**Fundamental growth** — g = retention ratio × return on equity, so a growth assumption implies a reinvestment assumption. [[investment-valuation-damodaran]]

**Price/sales ratio** — market value divided by trailing sales; usable when earnings are negative, and the basis of Fisher's entry and exit bands. [[kenneth-l-fisher-super-stocks--price-sales-and-price-research-screen]]

**Magic Formula** — Greenblatt's rank-sum of return on capital (EBIT ÷ [net working capital + net fixed assets]) and earnings yield (EBIT ÷ enterprise value). [[the-little-book--magic-formula]]

**CAN SLIM** — O'Neil's seven-factor growth screen: current earnings, annual earnings, a new catalyst and new high, supply and demand, leader or laggard, institutional sponsorship, and market direction. [[how-to-make-money-in-stocks-pdf-forex--can-slim-system]]

**Relative strength rating** — a 1-99 ranking of a stock's price performance against all others; O'Neil's 500 best performers averaged 87 just before their advance. [[how-to-make-money-in-stocks-pdf-forex]]

**Base and pivot** — a sideways consolidation and the price at which a breakout from it is bought. [[how-to-make-money-in-stocks-pdf-forex--can-slim-system]]

**Market neutral** — long and short positions sized so systematic risk cancels, leaving only the security-selection spread. [[marketneutralstrategies--equity-long-short-construction]]

**Integrated optimisation** — selecting longs and shorts jointly in one optimisation rather than bolting a short book onto a long one. [[marketneutralstrategies--equity-long-short-construction]]

**Secondary reaction** — a sizeable counter-trend rally inside a bear market, which Rhea's data shows retracing anywhere from 40% to over 85% of the prior decline. [[harry-d-schultz-bear-market-investing-strategies]]

## Psychology and process

**Loss aversion** — losses felt roughly 2.5 times as intensely as equivalent gains; the mechanism behind refusing to realise a loss and gambling to get back to even. [[kahneman-daniel-investor-psychology]]

**Disposition effect** — the resulting tendency to sell winners and hold losers. [[kahneman-daniel-investor-psychology]]

**Prospect theory** — the finding that people are loss-averse rather than simply risk-averse, and that framing an identical choice as a gain or a loss reverses the decision. [[prospect-theory]]

**Overconfidence** — non-professionals' 98% confidence intervals are wrong 15-20% of the time rather than 2%. [[kahneman-daniel-investor-psychology]]

**Hindsight bias** — the inability to recall pre-event probability estimates, which makes past moves look predictable and fuels overconfidence. [[kahneman-daniel-investor-psychology]]

**The five fundamental truths** — Douglas's probabilistic frame: anything can happen; you need not know what happens next; wins and losses are randomly distributed for any edge; an edge is only a higher probability; every moment is unique. [[trading-in-the-zone]]

**Edge** — a defined set of conditions indicating a higher probability of one outcome than another; nothing more, and no guarantee on any single occurrence. [[trading-in-the-zone]]

**Predefined loss** — deciding before entry exactly what invalidates the trade, so the decision is not made while emotionally invested. [[disciplined-trader]]

**Assume wrong until proven correct** — Phantom's inversion: remove any position that has not actively proven itself, rather than waiting for it to be proven wrong. [[phantom-of-the-20-pits]]

**Constructed problem** — Steenbarger's term for ordinary variance that becomes a self-reinforcing identity once labelled, and can be entrenched by treating it directly. [[brett-steenbarger-psychology-of-trading]]

**Trading Pyramid** — Piper's hierarchy running from self-knowledge through commitment, discipline, money management and risk control up to the system itself. [[john-piper-the-way-to-trade]]

**Deliberate practice** — segmenting the skill into components and drilling each in isolation before combining them live. [[whats-in-your-head]]
