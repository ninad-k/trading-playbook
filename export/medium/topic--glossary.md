# Glossary: a trading-library study guide

*Working definitions of the vocabulary used across this library, grouped by subject, with the pages where each term is developed.*

Terms are grouped by subject rather than alphabetised, because most of them only make sense next to their neighbours. Where sources disagree on a definition, the disagreement is noted — that is usually the interesting part. Each entry links to pages where the term is actually used rather than merely mentioned.

## Risk, sizing and expectancy

**Expectancy** — the average amount won or lost per unit risked across many trades: (win rate × average win) − (loss rate × average loss). The number that decides whether a method is worth trading; win rate alone does not. [Trade Your Way to Financial Freedom](https://ninad-k.github.io/trading-playbook/books/trade-your-way-to-financial-freedom.html)

**R-multiple** — a trade's result expressed as a multiple of its initial risk, where 1R is the distance from entry to the initial stop. Lets trades in different markets be compared on one scale. [Trade Your Way to Financial Freedom](https://ninad-k.github.io/trading-playbook/books/trade-your-way-to-financial-freedom.html)

**Position sizing** — the rule deciding how many shares or contracts to trade, as distinct from stop placement, entry, or diversification. [Special Report on Money Management](https://ninad-k.github.io/trading-playbook/books/money-management-report-van-tharp.html)

**Fixed-fractional sizing** — risking a constant percentage of current equity rather than a constant dollar amount, so exposure shrinks after losses and grows after gains. [Money Management Strategies for Futures Traders](https://ninad-k.github.io/trading-playbook/books/balsara-nauzer-j-money-management-strategies-for-futures-traders.html)

**Fixed Ratio sizing** — Ryan Jones's alternative: the profit required to add the next contract grows in fixed proportion to the number already held, governed by a single parameter, delta. [Fixed Ratio Position Sizing](https://ninad-k.github.io/trading-playbook/books/forex-misc-money-management-ryan-jones--fixed-ratio-position-sizing.html)

**Delta (position sizing)** — in Fixed Ratio, the only free variable; a rule of thumb sets it near half the expected worst-case per-contract drawdown. Not to be confused with the option Greek. [Fixed Ratio Position Sizing](https://ninad-k.github.io/trading-playbook/books/forex-misc-money-management-ryan-jones--fixed-ratio-position-sizing.html)

**Optimal f** — the fixed fraction of the largest historical loss that maximises long-run geometric growth. Also the fraction that maximises drawdown: historical retracement at optimal f is never smaller than f itself. [Optimal f and the TWR/Geometric Mean Framework](https://ninad-k.github.io/trading-playbook/books/mathematicsmoneymanagement--optimal-f-and-twr-framework.html)

**Kelly criterion** — the growth-optimal bet fraction derived from maximising expected log capital rather than expected capital; f = ((B+1)P − 1) ÷ B for a fixed payoff ratio B. Strictly valid only for two-outcome bets. [A New Interpretation of Information Rate](https://ninad-k.github.io/trading-playbook/books/kellybetting.html)

**Terminal Wealth Relative (TWR)** — the product of all holding-period returns in a sequence; the objective function maximised when searching for optimal f empirically. [Optimal f and the TWR/Geometric Mean Framework](https://ninad-k.github.io/trading-playbook/books/mathematicsmoneymanagement--optimal-f-and-twr-framework.html)

**Holding Period Return (HPR)** — one plus a trade's percentage result, so a +10% trade is 1.10. The building block of TWR. [The Mathematics of Money Management](https://ninad-k.github.io/trading-playbook/books/mathematicsmoneymanagement.html)

**Geometric mean** — the Nth root of TWR; the growth factor per trade, and the correct basis for comparing compounding strategies against one another. [The Mathematics of Money Management](https://ninad-k.github.io/trading-playbook/books/mathematicsmoneymanagement.html) [How to Win the Stock Market Game: Developing Short-Term Stock Trading Strategies](https://ninad-k.github.io/trading-playbook/books/vladimir-daragan-how-to-win-the-stock-market-game.html)

**Risk of ruin** — the probability that equity falls far enough that trading must stop, computable from win rate, payoff ratio and the fraction of capital exposed. Only the third is under the trader's control. [Money Management Strategies for Futures Traders](https://ninad-k.github.io/trading-playbook/books/balsara-nauzer-j-money-management-strategies-for-futures-traders.html)

**Drawdown** — the peak-to-trough decline in equity. Recovery is non-linear: a 50% loss needs a 100% gain, a 90% loss needs 900%. [Money Management: Controlling Risk and Capturing Profits](https://ninad-k.github.io/trading-playbook/books/money-management-by-david-landry.html)

**The 2% rule** — never risk more than 2% of account equity on one trade, counting commission and slippage. [Come Into My Trading Room](https://ninad-k.github.io/trading-playbook/books/come-into-my-trading-room-elder-alexander.html)

**The 6% rule** — total risk across open positions plus realised losses for the month may not exceed 6% of equity measured on the first of that month; once hit, stop trading until next month. [Come Into My Trading Room](https://ninad-k.github.io/trading-playbook/books/come-into-my-trading-room-elder-alexander.html)

**Portfolio heat** — total open risk across all positions at once, attributed to Ed Seykota; 20-25% is a common professional ceiling. [Nine Position-Sizing Models (Equal Units, % Risk, % Volatility, Kelly)](https://ninad-k.github.io/trading-playbook/books/money-management-report-van-tharp--position-sizing-models.html)

**Core equity** — total equity minus the dollar risk currently open in all positions, used as the sizing base so capacity shrinks automatically as exposure grows. [Managing Your Money](https://ninad-k.github.io/trading-playbook/books/managing-your-money.html)

**Anti-martingale** — increasing size as equity grows and reducing it after losses. **Martingale** is the reverse — increasing after a loss — and is treated throughout this library as a near-certain path to ruin. [Special Report on Money Management](https://ninad-k.github.io/trading-playbook/books/money-management-report-van-tharp.html) [Mechanical Trading Systems: Pairing Trader Psychology with Technical Analysis](https://ninad-k.github.io/trading-playbook/books/richard-l-weissman-mechanical-trading-systems.html)

**Pyramiding** — adding to a position that is already profitable, ideally in decreasing tranches with the stop moved up on the whole position. Distinct from averaging down. [Phantom of the Pits](https://ninad-k.github.io/trading-playbook/books/phantom-of-the-20-pits.html)

**Averaging down** — adding to a losing position. The most consistently prohibited action in the library. [Just One Thing: Twelve of the World's Best Investors Reveal the One Strategy You Can't Overlook](https://ninad-k.github.io/trading-playbook/books/john-mauldin-just-one-thing-twelve-of-the-world-s-best-investors-reveal-the-one-strategy-y.html)

**Margin-to-equity ratio** — total initial margin on open positions divided by account equity; a fast proxy for how levered a futures book is. Above roughly 30% is aggressive. [The Four Biggest Mistakes in Futures Trading](https://ninad-k.github.io/trading-playbook/books/jay-kaeppel-the-four-biggest-mistakes-in-futures-trading.html)

**Gearing** — leverage expressed as a multiple of capital; in retail forex, treated as the primary determinant of survival rather than a secondary parameter. [Bird Watching in Lion Country: Retail Forex Trading Explained](https://ninad-k.github.io/trading-playbook/books/the-bird-watching-lion-country.html)

**Risk-to-return ratio** — the standard deviation of per-trade return divided by the average return; below 3 is favourable, above 5 should be rejected. [How to Win the Stock Market Game: Developing Short-Term Stock Trading Strategies](https://ninad-k.github.io/trading-playbook/books/vladimir-daragan-how-to-win-the-stock-market-game.html)

## Trend, structure and price action

**Trend** — a sequence of rising peaks and rising troughs, or falling ones. A reversal is not confirmed until both sequences change. [Peaks and Troughs](https://ninad-k.github.io/trading-playbook/books/peaks-and-troughs-pring.html)

**Half-signal** — a change in only one of the two swing sequences; an alert rather than a confirmed reversal. [Peaks and Troughs](https://ninad-k.github.io/trading-playbook/books/peaks-and-troughs-pring.html)

**Support and resistance** — a prior trough or peak where price previously turned. Once decisively broken, the level tends to reverse role. [Charting Made Easy](https://ninad-k.github.io/trading-playbook/books/john-j-murphy-charting-made-easy.html)

**Trendline** — a line through two rising lows or falling highs; validated only by a third touch that holds. [Charting Made Easy](https://ninad-k.github.io/trading-playbook/books/john-j-murphy-charting-made-easy.html)

**Retracement** — a counter-move against the prevailing trend. Conventional bands run one-third to two-thirds of the prior move, with 50% most common. [Charting Made Easy](https://ninad-k.github.io/trading-playbook/books/john-j-murphy-charting-made-easy.html) [Peaks and Troughs](https://ninad-k.github.io/trading-playbook/books/peaks-and-troughs-pring.html)

**Congestion** — sideways price action. Ross's taxonomy: ledges up to 10 bars, congestion of 11-20, trading ranges of 21 or more. [Trading Manual: Appendices 269-320](https://ninad-k.github.io/trading-playbook/books/joerosstrading-manual-appendices-269-320.html)

**1-2-3 formation** — point 1 is the prior swing extreme, point 2 a full correction, point 3 another; the formation is void the moment any bar reaches or passes point 1. [The Law of Charts](https://ninad-k.github.io/trading-playbook/books/joe-ross-how-to-spot-a-trend.html)

**Ross Hook** — the first correction after a breakout of a 1-2-3, ledge, congestion or trading range. [Trading Manual: Appendices 269-320](https://ninad-k.github.io/trading-playbook/books/joerosstrading-manual-appendices-269-320.html)

**Trader's Trick Entry** — entering ahead of a breakout, on a correcting bar's extreme, only if there is enough room to the breakout point to cover costs and bank profit. [Trader's Trick Entry](https://ninad-k.github.io/trading-playbook/books/traders-trick-entry.html)

**Ledge** — Ross's precisely defined consolidation: four to ten bars containing two matching highs and two matching lows, matched within three minimum ticks, inside an existing trend. [The Law of Charts](https://ninad-k.github.io/trading-playbook/books/joe-ross-how-to-spot-a-trend.html)

**NR7** — the narrowest high-low range of the last seven bars; a volatility-contraction signal with no inherent directional bias. [Coiled Spring](https://ninad-k.github.io/trading-playbook/books/alan-farley-the-master-swing-trader--coiled-spring.html)

**Wiggle** — a stock's own average intraday pullback, estimated from five days of its 5-minute bars and used to size the trailing stop instead of a fixed distance. [Stock Patterns for Day Trading and Swing Trading](https://ninad-k.github.io/trading-playbook/books/barry-rudd-stock-patterns-for-day-trading-and-swing-trading.html)

**Box (Darvas)** — a price range a stock holds within, confirmed when it fails to break the ceiling or floor for three consecutive days; the breakout into the next box is the entry. [Darvas Box Theory](https://ninad-k.github.io/trading-playbook/books/how-i-made-2-million-in-the-stock-market--box-theory.html)

**Cross-verification** — Farley's requirement that several independently derived levels converge at one price before a trade is taken; four overlapping signals is his highest-probability case. [3D Charting and Cross-Verification](https://ninad-k.github.io/trading-playbook/books/alan-farley-the-master-swing-trader--3d-charting-cross-verification.html)

**Opening range** — the high and low of the session's first fixed block of time, from which most intraday breakout systems measure. [The ACD Method](https://ninad-k.github.io/trading-playbook/books/mark-b-fisher-the-logical-trader-applying-a-method-to-the-madness--acd-method.html)

**Initial balance** — in Market Profile, the range established while only the short-term participant is active, conventionally the first hour. [Market Profile — Construction and Reading Rules](https://ninad-k.github.io/trading-playbook/books/cbot-a-six-part-study-guide-to-market-profile--market-profile-construction-and-reading.html)

**Value area** — the price range containing about 70% of a session's volume, roughly one standard deviation of the distribution. [A Six-Part Study Guide to Market Profile](https://ninad-k.github.io/trading-playbook/books/cbot-a-six-part-study-guide-to-market-profile.html)

**TPO (Time/Price Opportunity)** — one letter at one price in a Market Profile, recording that a price traded during a given bracket. [A Six-Part Study Guide to Market Profile](https://ninad-k.github.io/trading-playbook/books/cbot-a-six-part-study-guide-to-market-profile.html)

**Point and figure** — a chart plotting only price as alternating columns of Xs and Os, with box size and a reversal amount (commonly three boxes) as the noise filter. [Point-and-Figure Charting and Bullish Percent Timing System](https://ninad-k.github.io/trading-playbook/books/tom-dorsey-s-trading-tips-a-playbook-for-stock-market-success--point-and-figure-and-bullish-percent-system.html)

**Bullish percent** — the share of a universe currently on a point-and-figure buy signal; above 70% is high risk, below 30% low risk. [Tom Dorsey's Trading Tips: A Playbook for Stock Market Success](https://ninad-k.github.io/trading-playbook/books/tom-dorsey-s-trading-tips-a-playbook-for-stock-market-success.html)

**Kagi, renko, three-line break** — Japanese price-only charts that print a new mark only on a qualifying move: a turnaround amount, a fixed brick height, or a break of the prior three lines respectively. [Kagi Charts](https://ninad-k.github.io/trading-playbook/books/beyond-candlesticks-steve-nison--kagi-chart.html) [Renko Charts](https://ninad-k.github.io/trading-playbook/books/beyond-candlesticks-steve-nison--renko-chart.html) [Three-Line Break Charts](https://ninad-k.github.io/trading-playbook/books/beyond-candlesticks-steve-nison--three-line-break-chart.html)

**Wolfe Wave** — a five-point pattern where the 1-3 line projects the reversal point and the 1-4 line projects the target. [Wolfe Waves](https://ninad-k.github.io/trading-playbook/books/street-smarts-laurence-connors--wolfe-waves.html)

## Candlesticks and chart patterns

**Real body and shadow** — the open-to-close range and the extremes beyond it. A long body signals conviction, a long shadow a price rejected. [Introduction to Candlesticks](https://ninad-k.github.io/trading-playbook/books/trading-hill-arthur-introduction-to-candlesticks.html)

**Doji** — open and close effectively equal; Morris's numeric threshold is an open-to-close distance under roughly 1-3% of the day's range, and it only signifies after a run of non-doji sessions. [Candlestick Charting Explained — Pattern Catalogue and Reliability Ranking](https://ninad-k.github.io/trading-playbook/books/greg-morris-candlestick-charting-explained--pattern-catalogue-and-reliability.html)

**Hammer and hanging man** — the same shape — small body, lower shadow at least twice the body, little upper shadow — read as bullish after a decline and bearish after an advance. [Introduction to Candlesticks](https://ninad-k.github.io/trading-playbook/books/trading-hill-arthur-introduction-to-candlesticks.html)

**Engulfing pattern** — a body that fully covers the prior body in the opposite colour, requiring a trend already in force. [Candlestick Charting Explained — Pattern Catalogue and Reliability Ranking](https://ninad-k.github.io/trading-playbook/books/greg-morris-candlestick-charting-explained--pattern-catalogue-and-reliability.html)

**Dark cloud cover and piercing line** — two-candle reversals where the second closes past the midpoint of the first's body; Morris treats the 50% requirement as non-negotiable. [Candlestick Charting Explained](https://ninad-k.github.io/trading-playbook/books/greg-morris-candlestick-charting-explained.html)

**Blending** — reducing a multi-candle pattern to one synthetic candle using the first open, the last close, and the pattern's extremes. [Introduction to Candlesticks](https://ninad-k.github.io/trading-playbook/books/trading-hill-arthur-introduction-to-candlesticks.html)

**Measured move** — projecting a pattern's own height from its breakout as the target: flagpole height for a flag, head-to-neckline for a head and shoulders. [Chart Patterns and Technical Indicators](https://ninad-k.github.io/trading-playbook/books/chart-patterns-and-technical-indicators.html)

**Neckline** — the boundary whose close-basis break completes a head-and-shoulders or double top or bottom. [Double Tops & Double Bottoms](https://ninad-k.github.io/trading-playbook/books/doubletopsandbottoms.html)

**Gap taxonomy** — breakaway gaps start a move, measuring or continuation gaps mark its middle, exhaustion gaps mark its end. [Chart Patterns Tutorial](https://ninad-k.github.io/trading-playbook/books/chart-patterns-tutorial.html)

**Hole-in-the-wall** — Farley's category for a sharp gap down that ends an uptrend at a new high on volume exceeding the prior rally; the rally back into it rarely fills. [Hole-in-the-Wall](https://ninad-k.github.io/trading-playbook/books/alan-farley-the-master-swing-trader--hole-in-the-wall.html)

## Indicators

**Moving average** — a smoothed price series; simple, weighted or exponential. Lagging by construction, since today's value is plotted against today's price. [New Twist on an Old Indicator](https://ninad-k.github.io/trading-playbook/books/new-twist-on-an-old-indicator.html)

**Adaptive moving average (KAMA)** — an average whose smoothing constant varies with the efficiency ratio, accelerating in directional markets and flattening in noise. [The Adaptive Moving Average (KAMA)](https://ninad-k.github.io/trading-playbook/books/perry-kaufman-smarter-trading--adaptive-moving-average-kama.html)

**Efficiency ratio** — net directional change over a period divided by the summed absolute daily changes; 0 is pure noise, 1 perfectly directional. [The Adaptive Moving Average (KAMA)](https://ninad-k.github.io/trading-playbook/books/perry-kaufman-smarter-trading--adaptive-moving-average-kama.html)

**True range** — the greatest of today's range, or the range including yesterday's close, so gaps count toward measured volatility. **ATR** is its average, and **N** is the Turtle name for the 20-day version. [The Turtle Trading System (Original Rules)](https://ninad-k.github.io/trading-playbook/books/turtlerules--turtle-system.html) [A Short Course in Technical Trading](https://ninad-k.github.io/trading-playbook/books/a-short-course-in-technical-trading.html)

**Bollinger Bands** — a 20-period moving average with bands at ±2 standard deviations, the multiplier scaling with the period. Actual containment is nearer 88-89% than the 95% normality implies. [Bollinger on Bollinger Bands](https://ninad-k.github.io/trading-playbook/books/john-bollinger-bollinger-on-bollinger-band.html)

**%b** — (last − lower band) ÷ (upper band − lower band): 1.0 at the upper band, 0.5 at the middle, unbounded beyond either. [Using Bollinger Bands](https://ninad-k.github.io/trading-playbook/books/trading-bollinger-john-bollinger-bands-done.html)

**BandWidth and the Squeeze** — (upper − lower) ÷ middle, and the condition of that value reaching a six-month low. A precondition for volatility expansion, carrying no direction. [Method I — The Squeeze / Volatility Breakout](https://ninad-k.github.io/trading-playbook/books/john-bollinger-bollinger-on-bollinger-band--method-i-squeeze-breakout.html)

**RSI** — a bounded 0-100 momentum oscillator, 14-period by default, conventionally read at 70/30. [Measuring Internal Strength: Wilder's RSI Indicator](https://ninad-k.github.io/trading-playbook/books/wayne-a-thorp-measuring-internal-strength-wilders-rsi-indicator.html)

**RSI range shift** — Cardwell's reading: RSI holds support near 40 and meets resistance near 80 in an uptrend, 20 and 60 in a downtrend; a shift between those ranges signals a trend change. [Trend Determination: A Quick, Accurate & Effective Methodology](https://ninad-k.github.io/trading-playbook/books/trend-determination.html)

**Failure swing** — an RSI double top above 70 followed by a break of the intervening trough, treated as a sell signal even before price turns. [Measuring Internal Strength: Wilder's RSI Indicator](https://ninad-k.github.io/trading-playbook/books/wayne-a-thorp-measuring-internal-strength-wilders-rsi-indicator.html)

**MACD** — the difference between a fast and slow EMA, conventionally 12 and 26, with a 9-period signal line and a histogram of the gap between them. [The MACD: A Combo of Indicators for the Best of Both Worlds](https://ninad-k.github.io/trading-playbook/books/wayne-a-thorp-the-macd-a-combo-of-indicators-for-the-best-of-both-worlds.html)

**ADX** — a 0-100 measure of trend strength, not direction; above 25-30 indicates trending, below indicates chop. [ADX (Average Directional Index)](https://ninad-k.github.io/trading-playbook/books/adx.html)

**CCI and Woodie's rules** — a trend requires six or more CCI bars on one side of zero; the Zero-Line Reject needs a retracement through at least ±100 before turning back with the trend. [Woodies CCI Basic Patterns and Terminology](https://ninad-k.github.io/trading-playbook/books/cci-manual.html)

**Divergence** — price making a new extreme the oscillator does not confirm; a warning that can persist far longer than expected. [Divergence Decisions](https://ninad-k.github.io/trading-playbook/books/divergence.html)

**Hidden divergence** — the oscillator making a lower low while price makes a higher low in an uptrend; a continuation and re-entry signal, not a reversal. [Hidden Divergence](https://ninad-k.github.io/trading-playbook/books/barbara-star-hidden-divergence.html)

**Reverse divergence** — price making a lower high while the oscillator makes a *higher* high; price leads the oscillator into the turn. [Reverse Divergences and Momentum](https://ninad-k.github.io/trading-playbook/books/reverse-divergence-and-momentum.html)

**Disparity index** — ((close − moving average) ÷ moving average) × 100; a percent-from-average oscillator with instrument-specific thresholds. [The Disparity Index](https://ninad-k.github.io/trading-playbook/books/beyond-candlesticks-steve-nison--disparity-index.html)

**Elder-ray** — Bull Power (high − 13-day EMA) and Bear Power (low − 13-day EMA) plotted as histograms, traded on divergence in the direction of the EMA's slope. [Elder-ray (Bull Power / Bear Power)](https://ninad-k.github.io/trading-playbook/books/elder-alexander-trading-for-a-living--elder-ray.html)

**TICK** — NYSE issues trading on an uptick minus those on a downtick; a breadth measure whose useful thresholds have shifted with market structure. [Intraday Trading with the TICK](https://ninad-k.github.io/trading-playbook/books/tick.html)

**Volume Spread Analysis** — reading spread against volume to infer professional activity: No Demand, No Supply, effort without result, up-thrust. [Undeclared Stockmarket Secrets](https://ninad-k.github.io/trading-playbook/books/williams-undeclared-stockmarket-secrets.html)

**Accumulation/distribution** — Williams's volume-weighted flow line: (close − open) ÷ (high − low), multiplied by volume and cumulated. [Accumulation/Distribution Stock Selection System](https://ninad-k.github.io/trading-playbook/books/larry-williams-the-secret-of-selecting-stocks-for-immediate-and-substantial-gains--accumulation-distribution-system.html)

**Multicollinearity (indicator)** — Bollinger's warning against combining indicators derived from the same underlying data and calling their agreement confirmation. [Using Bollinger Bands](https://ninad-k.github.io/trading-playbook/books/trading-bollinger-john-bollinger-bands-done.html)

## Options and derivatives

**Delta** — the change in an option's price per $1 move in the underlying; loosely, the probability of finishing in the money. [The Options Course: High Profit & Low Stress Trading Methods](https://ninad-k.github.io/trading-playbook/books/fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed.html)

**Gamma** — the rate of change of delta; largest at the money and growing toward expiration. A delta-neutral book with large negative gamma is exposed to any large move. [Options, Futures, and Other Derivatives (5th Edition)](https://ninad-k.github.io/trading-playbook/books/hull-options-futures-and-other-derivative-securities-5th-ed.html)

**Theta** — daily time decay of premium, largest for at-the-money options near expiration. [The Options Course: High Profit & Low Stress Trading Methods](https://ninad-k.github.io/trading-playbook/books/fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed.html)

**Vega** — sensitivity to a one-point change in implied volatility, largest far from expiration. [Options: Essential Concepts and Trading Strategies](https://ninad-k.github.io/trading-playbook/books/options-essential-concepts-and-trading-strategies-2nd-edition.html)

**Implied volatility** — the volatility figure that reproduces an option's market price through a pricing model. **Historical volatility** is computed from the underlying's realised price changes. [Using Volatility in Options Trading, Part 1](https://ninad-k.github.io/trading-playbook/books/using-volatility-in-option-tradingpart-1.html)

**Percentile ranking (volatility)** — placing today's implied volatility against its own multi-hundred-day history, rather than comparing implied to historical, because some underlyings structurally trade above their realised volatility. [McMillan's Volatility-Based Option Strategy Selection](https://ninad-k.github.io/trading-playbook/books/lawrence-g-mcmillan-profit-with-options--volatility-based-strategy-selection.html)

**Volatility skew** — the pattern of implied volatility across strikes; forward skew means higher strikes are more expensive, reverse skew the opposite. It tracks the underlying's actual fat-tailedness. [Back to Basics: Historical Option Pricing Revisited](https://ninad-k.github.io/trading-playbook/books/back-to-basics-historical-option-pricing-revisited.html)

**Put-call parity** — c + Ke^-rT = p + S₀; the relation that makes synthetic positions and conversions possible. [Options, Futures, and Other Derivatives (5th Edition)](https://ninad-k.github.io/trading-playbook/books/hull-options-futures-and-other-derivative-securities-5th-ed.html)

**No-arbitrage** — if two portfolios pay the same in every future state they must cost the same today; the principle underlying forward, futures and option pricing. [Rubinstein on Derivatives](https://ninad-k.github.io/trading-playbook/books/rubinstein-mark-rubinstein-on-derivatives.html)

**Risk-neutral valuation** — pricing a derivative as though all investors were risk-neutral, which gives the same answer as the real world because risk preferences cancel out. [Options, Futures, and Other Derivatives (5th Edition)](https://ninad-k.github.io/trading-playbook/books/hull-options-futures-and-other-derivative-securities-5th-ed.html)

**Delta neutral** — a position built so net directional exposure is zero at entry, profiting from movement, time or volatility rather than direction. [Delta-Neutral Straddle & Adjustment System](https://ninad-k.github.io/trading-playbook/books/fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed--delta-neutral-straddles-and-adjustments.html)

**Straddle and strangle** — a long call and put at the same strike, or at different strikes; the basic long-volatility structures. [Delta-Neutral Straddle & Adjustment System](https://ninad-k.github.io/trading-playbook/books/fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed--delta-neutral-straddles-and-adjustments.html)

**Ratio backspread** — selling fewer near-the-money options and buying more further-out ones for a net credit, with capped risk between the strikes. [Call & Put Ratio Backspread System](https://ninad-k.github.io/trading-playbook/books/fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed--ratio-backspreads.html)

**Vertical, calendar and diagonal spreads** — same expiration different strikes; same strike different expirations; and both differing. [The Bible of Options Strategies — Strategy Family Construction Playbook](https://ninad-k.github.io/trading-playbook/books/guy-cohen-the-bible-of-options-strategies--strategy-family-playbook.html)

**Butterfly and condor** — capped-risk structures selling premium near the current price and buying protection further out; explicitly awkward to adjust and normally held to expiration. [Range-Bound Premium Spread System (Butterfly, Condor, Calendar, Collar)](https://ninad-k.github.io/trading-playbook/books/fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed--range-bound-premium-spreads.html)

**Covered call** — selling a call against stock already owned; economically equivalent in risk to selling a cash-backed put at the same strike. [Create Your Own Hedge Fund](https://ninad-k.github.io/trading-playbook/books/m-wolfinger-create-your-own-hedge-fund-increase-profits-and-reduce-risk-with-etfs-and-opti.html)

**Payout ratio (option writing)** — average payout divided by average premium collected. Gallacher's 1996 study across fifteen commodities found it almost exactly 1.0, implying no inherent writer's edge. [The Options Edge: Winning the Volatility Game with Options on Futures](https://ninad-k.github.io/trading-playbook/books/mcgraw-hill-the-options-edge-winning-the-volatility-game-with-options-on-futures.html)

**Spread (futures)** — the price difference between two related contracts, structurally hedged and therefore carrying lower margin and volatility than the outright. [Trading Spreads and Seasonals](https://ninad-k.github.io/trading-playbook/books/joe-ross-trading-spreads-and-seasonals.html)

**Parity and spread (merger arbitrage)** — the value of the offered securities package, and the gap between it and the target's current price. [Merger Arbitrage Spread Calculation and Deal-Risk Checklist](https://ninad-k.github.io/trading-playbook/books/wyser-pratte-guy-risk-arbitrage--merger-arbitrage-spread-and-deal-risk-checklist.html)

## Cycles, ratios and waves

**Fibonacci ratios** — 0.618 and its inverse 1.618, from consecutive terms of the Fibonacci series. Retracements of 38.2%, 50% and 61.8%, extensions at 127%, 161.8% and 261.8%. 50% is not itself a Fibonacci ratio. [Candlesticks, Fibonacci, and Chart Pattern Trading Tools](https://ninad-k.github.io/trading-playbook/books/candlesticks-fibonacci-and-chart-pattern-trading-tools.html)

**Confluence** — two or more projections derived from *different* swings clustering in a narrow band; the actual signal, as opposed to a single ratio hit. [Practical Fibonacci Methods for Forex Trading](https://ninad-k.github.io/trading-playbook/books/forex-systems-research-practical-fibonacci-methods-for-forex-trading-2005.html)

**Impulse and corrective wave** — a five-wave move with the larger trend and a three-wave move against it, nested at every degree. [Elliott Wave Principle](https://ninad-k.github.io/trading-playbook/books/elliott-waves-principle.html)

**The three Elliott rules** — wave 2 never retraces beyond the start of wave 1; wave 3 is never the shortest of 1, 3 and 5; wave 4 never enters wave 1's territory. Everything else is a guideline. [Elliott Wave Rules and Guidelines](https://ninad-k.github.io/trading-playbook/books/elliott-waves-principle--wave-rules-and-guidelines.html)

**Alternate count** — the second-best wave interpretation, maintained continuously so an invalidation leaves a working hypothesis rather than nothing. [Practical Elliott Wave Trading Strategies](https://ninad-k.github.io/trading-playbook/books/practicalew.html)

**Gartley "222" and AB=CD** — harmonic patterns defined purely by Fibonacci ratios between the legs of an XABCD swing sequence. [Fibonacci Ratios with Pattern Recognition — Gartley "222" and Butterfly Patterns](https://ninad-k.github.io/trading-playbook/books/fibonacci-ratios-with-pattern-recognition--gartley-222-and-butterfly-patterns.html)

**Square of Nine** — Gann's spiral of integers used as a square-root calculator, reading 90-, 180- and 270-degree rotations as candidate price levels. [The Gann Wheel](https://ninad-k.github.io/trading-playbook/books/gannwheel.html)

**Kondratieff, Juglar and Kitchin cycles** — nested economic cycles of roughly 50-60 years, 9-11 years and 40 months, the last associated with the US electoral calendar. [Mapping the Markets: A Guide to Stockmarket Analysis](https://ninad-k.github.io/trading-playbook/books/deborah-owen-mapping-the-markets.html)

**Seasonal tendency** — a recurring calendar bias measured from historical data, such as trading day of week and trading day of month. [Long-Term Secrets to Short-Term Trading: TDW/TDM Calendar Filters](https://ninad-k.github.io/trading-playbook/books/larry-williams-long-term-secrets-to-short-term-trading--tdw-tdm-filters.html)

**Best Six Months** — holding the index from 1 November to 30 April and standing aside from May to October. [Best Six Months Seasonal Strategy](https://ninad-k.github.io/trading-playbook/books/leslie-n-masonson-all-about-market-timing--best-six-months-strategy.html)

## Systems, testing and evidence

**Mechanical system** — a fully rule-based method generating signals without discretion, and therefore testable statistically. [Jack Schwager's Guide to Winning with Automated Trading Systems](https://ninad-k.github.io/trading-playbook/books/jack-schwager-guide-to-winning-with-automated-trading-systems-course-manual.html)

**In-sample and out-of-sample** — the data a system's parameters were fitted on, and data held back to verify it. Results from the first mean little without the second. [The Encyclopedia of Trading Strategies — Standard Test Methodology](https://ninad-k.github.io/trading-playbook/books/mcgraw-hill-encyclopedia-of-trading-strategies--test-methodology.html)

**Walk-forward testing** — optimising on one segment and validating on the next untouched one, repeatedly. [Building Winning Trading Systems with TradeStation](https://ninad-k.github.io/trading-playbook/books/george-pruitt-building-winning-trading-systems-with-tradestation.html)

**Curve fitting** — tuning a system so closely to historical data that its apparent edge is an artifact of that dataset. [Smarter Trading](https://ninad-k.github.io/trading-playbook/books/perry-kaufman-smarter-trading.html)

**Robustness** — the property that a system's performance changes little when a parameter is nudged. Sensitivity to a specific value is evidence of fitting. [The Complete TurtleTrader: The Legend, the Lessons, the Results](https://ninad-k.github.io/trading-playbook/books/the-complete-turtletrader-the-legend-the-lessons-the-results.html)

**Multiple comparisons** — the inflation of apparent significance when the best of many parameter runs is reported; requires explicit correction. [The Encyclopedia of Trading Strategies — Standard Test Methodology](https://ninad-k.github.io/trading-playbook/books/mcgraw-hill-encyclopedia-of-trading-strategies--test-methodology.html)

**Random-entry baseline** — comparing a rule against random entries with the same exits, so the question becomes whether it beats chance rather than whether it made money. [The Encyclopedia of Trading Strategies](https://ninad-k.github.io/trading-playbook/books/mcgraw-hill-encyclopedia-of-trading-strategies.html)

**Dollar volatility equalisation** — scaling contracts per market so each contributes comparable risk, rather than trading equal contract counts. [The Encyclopedia of Trading Strategies — Standard Test Methodology](https://ninad-k.github.io/trading-playbook/books/mcgraw-hill-encyclopedia-of-trading-strategies--test-methodology.html)

**Standardised exit** — holding the exit constant while comparing entries, so the comparison measures entry quality rather than exit variation. [The Encyclopedia of Trading Strategies — Standard Test Methodology](https://ninad-k.github.io/trading-playbook/books/mcgraw-hill-encyclopedia-of-trading-strategies--test-methodology.html)

**Profit factor** — gross profit divided by gross loss. A high win rate with a profit factor near 1.0, as in the decade-long gap-fade study, means the losses are simply larger than the wins. [Understanding Gaps](https://ninad-k.github.io/trading-playbook/books/andrews-scott-understanding-gaps.html)

**Whipsaw** — a signal that reverses immediately, producing a small loss and a cost. The characteristic failure mode of trend systems in a range. [Mechanical Trading Systems: Pairing Trader Psychology with Technical Analysis](https://ninad-k.github.io/trading-playbook/books/richard-l-weissman-mechanical-trading-systems.html)

**Stop-and-reverse** — a system always in the market, flipping directly from long to short on the opposite signal. [The CMO-Driven VIDYA Trading System](https://ninad-k.github.io/trading-playbook/books/chande-kroll-the-new-technical-trader--cmo-vidya-trading-system.html)

**Slippage** — the difference between the intended and achieved fill. Excluded from most published results in this library, and large enough to reverse several of them. [How to Test and Interpret Trading System Performance](https://ninad-k.github.io/trading-playbook/books/wayne-a-thorp-testing-trading-success.html)

**Survivorship bias** — computing success statistics only from those who survived, so the base rate of skill appears far higher than it is. [Fooled by Randomness: The Hidden Role of Chance in the Markets and in Life](https://ninad-k.github.io/trading-playbook/books/taleb-nassim-fooled-by-randomness.html)

**Alternative histories** — the distribution of outcomes that could have happened, against which the one that did should be judged. [Fooled by Randomness: The Hidden Role of Chance in the Markets and in Life](https://ninad-k.github.io/trading-playbook/books/taleb-nassim-fooled-by-randomness.html)

**Negative skew** — a payoff of frequent small gains and rare large losses; produces a smooth track record right up until it does not. [Fooled by Randomness: The Hidden Role of Chance in the Markets and in Life](https://ninad-k.github.io/trading-playbook/books/taleb-nassim-fooled-by-randomness.html)

## Microstructure and execution

**Bid-ask spread** — the cost of immediacy, and the first hurdle any short-horizon edge must clear. Wyckoff's "invisible eighth". [The Day Trader's Bible (My Secrets of Day Trading in Stocks)](https://ninad-k.github.io/trading-playbook/books/wyckoff-richard-d-the-day-trader-s-bible-or-my-secret-in-day-trading-of-stocks-2.html)

**Market order versus limit order** — a market order guarantees a fill but not a price; a limit order the reverse. A triggered stop becomes a market order. [Market Mechanics: A Guide to U.S. Stock Markets](https://ninad-k.github.io/trading-playbook/books/nasdaq-education-foundation-a-guide-to-u-s-stock-markets-eng.html)

**Depth** — the size available at each price level; the other half of liquidity alongside the spread, and inversely related to transitory volatility. [Limit Orders, Depth, and Volatility](https://ninad-k.github.io/trading-playbook/books/depth-volatility.html)

**Price impact** — the price movement caused by an order itself; concave in size, roughly proportional to the square root of volume rather than linear. [Are Supply and Demand Driving Stock Prices?](https://ninad-k.github.io/trading-playbook/books/supply-demand.html)

**Order flow imbalance** — the net signed direction of orders, which explained roughly half of return variance on the venue studied. [Are Supply and Demand Driving Stock Prices?](https://ninad-k.github.io/trading-playbook/books/supply-demand.html)

**Commonality in liquidity** — the tendency of spreads and depth to co-move across stocks, so positions correlate exactly when liquidity is needed. [Commonality in Liquidity](https://ninad-k.github.io/trading-playbook/books/chordia-roll-and-subrahmanyam-commonality-in-liquidity.html)

**Liquidity black hole** — a self-reinforcing sell-off in which private loss limits make each exit trigger the next, with no new information required. [Liquidity Black Holes](https://ninad-k.github.io/trading-playbook/books/morris-and-song-shin-liquidity-black-holes.html)

**U-shaped intraday pattern** — the concentration of volume and volatility at the open and close, produced by traders clustering to minimise their own impact — and present even in markets with no market makers. [A Theory of Intraday Patterns: Volume and Price Variability](https://ninad-k.github.io/trading-playbook/books/admati-and-pfleiderer-a-theory-of-intraday-patterns-volume-and-price-variability.html)

**Upstairs market** — broker-negotiated block trading, which lowers execution cost by tapping unexpressed liquidity and certifying the trade as uninformed. [Does an Electronic Stock Exchange Need an Upstairs Market?](https://ninad-k.github.io/trading-playbook/books/bessembinder-and-venkataraman-does-an-electronic-stock-exchange-need-an-upstairs-market.html)

**Value at Risk (VaR)** — the loss level not exceeded at a given confidence over a given horizon. Not a coherent risk measure outside elliptical distributions, biased low, and gameable. [Exploring the Limitations of Value at Risk: How Good Is It in Practice?](https://ninad-k.github.io/trading-playbook/books/exploring-value-at-risk.html)

**Return smoothing** — autocorrelation in reported returns from stale or illiquid pricing; removing it raises estimated volatility by 60-100% for some hedge fund styles. [Hedge Fund Risk Factors and Value at Risk of Credit Trading Strategies](https://ninad-k.github.io/trading-playbook/books/hedge-fund-risk-factors-and-value-at-risk-of-credit-trading-strategies.html)

## Forex and macro

**Pip** — the smallest quoted increment in a currency pair. [Currency Trading: How to Access and Trade the World's Biggest Market](https://ninad-k.github.io/trading-playbook/books/3-how-to-access-and-trade-the-world-s-biggest-market.html)

**Spot and forward** — settlement within two days, and anything beyond, with forward points reflecting the interest-rate differential under covered interest parity. [All About the Foreign Exchange Market in the United States](https://ninad-k.github.io/trading-playbook/books/all-about-forex-market-in-usa-eng.html)

**Carry trade** — buying a higher-yielding currency funded by a lower-yielding one to capture the rate differential; profitable while risk appetite holds and violent when it reverses. [Leveraged Carry Trade](https://ninad-k.github.io/trading-playbook/books/day-trading-the-currency-market--leveraged-carry-trade.html)

**Risk appetite** — a composite read of whether capital is flowing toward risk assets and high-carry currencies or toward havens. [Currency Strategy: The Practitioner's Guide to Currency Investing, Hedging and Forecasting](https://ninad-k.github.io/trading-playbook/books/wiley-currency-strategy-a-practitioner-s-guide-to-currency-trading-hedging-and-forecasting.html)

**Signal grid** — Henderson's four disciplines — economics, flow, technicals and valuation — with a position taken only when at least three agree. [Currency Strategy — Signal Grid and Active Currency Overlay Strategies](https://ninad-k.github.io/trading-playbook/books/wiley-currency-strategy-a-practitioner-s-guide-to-currency-trading-hedging-and-forecasting--signal-grid-and-active-currency-overlay.html)

**COT report** — the CFTC's weekly breakdown of positioning by commercials, large speculators and small speculators. **COT Index** normalises the current net position against its own multi-year range. [Trade Stocks and Commodities with the Insiders: Secrets of the COT Report](https://ninad-k.github.io/trading-playbook/books/williams-larry-trade-stocks-and-commodities-with-the-insiders.html)

**Median grid** — du Toit's manually drawn support-and-resistance channel on one pair, divided into quadrants as a reference for judging whether price is relatively high or low. [The 4x1 Strategy and Median Grid](https://ninad-k.github.io/trading-playbook/books/the-bird-watching-lion-country--4x1-median-grid.html)

**Purchasing power parity** — the proposition that exchange rates converge to relative price levels; rejected as a trading input by most surveyed FX dealers while a minority still think it binds beyond six months. [Macroeconomic Implications of the Beliefs and Behavior of Foreign Exchange Traders](https://ninad-k.github.io/trading-playbook/books/chinn.html)

## Investing and valuation

**Intrinsic value** — the present value of an asset's expected future cash flows discounted at a rate reflecting their risk. [Investment Valuation](https://ninad-k.github.io/trading-playbook/books/investment-valuation-damodaran.html)

**Margin of safety** — the gap between that value and the price paid; it makes an accurate forecast unnecessary rather than guaranteeing a profit. [The Intelligent Investor](https://ninad-k.github.io/trading-playbook/books/the-intelligent-investor-benjamin-graham.html)

**Mr. Market** — Graham's allegorical partner offering a mood-driven quote daily, to be used or ignored at the investor's convenience. [The Intelligent Investor](https://ninad-k.github.io/trading-playbook/books/the-intelligent-investor-benjamin-graham.html)

**FCFE and FCFF** — free cash flow to equity and to the firm; the first discounted at the cost of equity, the second at the cost of capital. [DCF Valuation Method (FCFE / FCFF)](https://ninad-k.github.io/trading-playbook/books/investment-valuation-damodaran--dcf-valuation-method.html)

**Terminal value** — the value beyond the explicit forecast period, which dominates most DCF outputs and whose growth rate cannot exceed the economy's long-run nominal growth. [Investment Valuation](https://ninad-k.github.io/trading-playbook/books/investment-valuation-damodaran.html)

**Fundamental growth** — g = retention ratio × return on equity, so a growth assumption implies a reinvestment assumption. [Investment Valuation](https://ninad-k.github.io/trading-playbook/books/investment-valuation-damodaran.html)

**Price/sales ratio** — market value divided by trailing sales; usable when earnings are negative, and the basis of Fisher's entry and exit bands. [The Price/Sales and Price/Research Screen](https://ninad-k.github.io/trading-playbook/books/kenneth-l-fisher-super-stocks--price-sales-and-price-research-screen.html)

**Magic Formula** — Greenblatt's rank-sum of return on capital (EBIT ÷ [net working capital + net fixed assets]) and earnings yield (EBIT ÷ enterprise value). [The Little Book That Beats the Market — The Magic Formula](https://ninad-k.github.io/trading-playbook/books/the-little-book--magic-formula.html)

**CAN SLIM** — O'Neil's seven-factor growth screen: current earnings, annual earnings, a new catalyst and new high, supply and demand, leader or laggard, institutional sponsorship, and market direction. [CAN SLIM Growth Stock System](https://ninad-k.github.io/trading-playbook/books/how-to-make-money-in-stocks-pdf-forex--can-slim-system.html)

**Relative strength rating** — a 1-99 ranking of a stock's price performance against all others; O'Neil's 500 best performers averaged 87 just before their advance. [How to Make Money in Stocks](https://ninad-k.github.io/trading-playbook/books/how-to-make-money-in-stocks-pdf-forex.html)

**Base and pivot** — a sideways consolidation and the price at which a breakout from it is bought. [CAN SLIM Growth Stock System](https://ninad-k.github.io/trading-playbook/books/how-to-make-money-in-stocks-pdf-forex--can-slim-system.html)

**Market neutral** — long and short positions sized so systematic risk cancels, leaving only the security-selection spread. [Market Neutral Equity Long-Short Portfolio Construction](https://ninad-k.github.io/trading-playbook/books/marketneutralstrategies--equity-long-short-construction.html)

**Integrated optimisation** — selecting longs and shorts jointly in one optimisation rather than bolting a short book onto a long one. [Market Neutral Equity Long-Short Portfolio Construction](https://ninad-k.github.io/trading-playbook/books/marketneutralstrategies--equity-long-short-construction.html)

**Secondary reaction** — a sizeable counter-trend rally inside a bear market, which Rhea's data shows retracing anywhere from 40% to over 85% of the prior decline. [Bear Market Investing Strategies](https://ninad-k.github.io/trading-playbook/books/harry-d-schultz-bear-market-investing-strategies.html)

## Psychology and process

**Loss aversion** — losses felt roughly 2.5 times as intensely as equivalent gains; the mechanism behind refusing to realise a loss and gambling to get back to even. [Aspects of Investor Psychology: Beliefs, Preferences, and Biases Investment Advisors Should Know About](https://ninad-k.github.io/trading-playbook/books/kahneman-daniel-investor-psychology.html)

**Disposition effect** — the resulting tendency to sell winners and hold losers. [Aspects of Investor Psychology: Beliefs, Preferences, and Biases Investment Advisors Should Know About](https://ninad-k.github.io/trading-playbook/books/kahneman-daniel-investor-psychology.html)

**Prospect theory** — the finding that people are loss-averse rather than simply risk-averse, and that framing an identical choice as a gain or a loss reverses the decision. [Why Smart Traders Do Dumb Things: Understanding Prospect Theory](https://ninad-k.github.io/trading-playbook/books/prospect-theory.html)

**Overconfidence** — non-professionals' 98% confidence intervals are wrong 15-20% of the time rather than 2%. [Aspects of Investor Psychology: Beliefs, Preferences, and Biases Investment Advisors Should Know About](https://ninad-k.github.io/trading-playbook/books/kahneman-daniel-investor-psychology.html)

**Hindsight bias** — the inability to recall pre-event probability estimates, which makes past moves look predictable and fuels overconfidence. [Aspects of Investor Psychology: Beliefs, Preferences, and Biases Investment Advisors Should Know About](https://ninad-k.github.io/trading-playbook/books/kahneman-daniel-investor-psychology.html)

**The five fundamental truths** — Douglas's probabilistic frame: anything can happen; you need not know what happens next; wins and losses are randomly distributed for any edge; an edge is only a higher probability; every moment is unique. [Trading in the Zone: Master the Market with Confidence, Discipline, and a Winning Attitude](https://ninad-k.github.io/trading-playbook/books/trading-in-the-zone.html)

**Edge** — a defined set of conditions indicating a higher probability of one outcome than another; nothing more, and no guarantee on any single occurrence. [Trading in the Zone: Master the Market with Confidence, Discipline, and a Winning Attitude](https://ninad-k.github.io/trading-playbook/books/trading-in-the-zone.html)

**Predefined loss** — deciding before entry exactly what invalidates the trade, so the decision is not made while emotionally invested. [The Disciplined Trader: Developing Winning Attitudes](https://ninad-k.github.io/trading-playbook/books/disciplined-trader.html)

**Assume wrong until proven correct** — Phantom's inversion: remove any position that has not actively proven itself, rather than waiting for it to be proven wrong. [Phantom of the Pits](https://ninad-k.github.io/trading-playbook/books/phantom-of-the-20-pits.html)

**Constructed problem** — Steenbarger's term for ordinary variance that becomes a self-reinforcing identity once labelled, and can be entrenched by treating it directly. [A Dozen Reflections on Life and Markets: Collected Trading Psychology Articles](https://ninad-k.github.io/trading-playbook/books/brett-steenbarger-psychology-of-trading.html)

**Trading Pyramid** — Piper's hierarchy running from self-knowledge through commitment, discipline, money management and risk control up to the system itself. [The Way to Trade: Discover Your Successful Trading Personality](https://ninad-k.github.io/trading-playbook/books/john-piper-the-way-to-trade.html)

**Deliberate practice** — segmenting the skill into components and drilling each in isolation before combining them live. [What's in Your Head? Becoming a Trader](https://ninad-k.github.io/trading-playbook/books/whats-in-your-head.html)

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

Full library with search: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/)
