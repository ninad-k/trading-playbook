# Technical Analysis of Stocks & Commodities, Volume 5 (1987): the trader's summary

*A bound year of S&C magazine (1987) mixing indicator research, a 15-part Wyckoff Method series, Sweeney's MAE stop technique, and dated software reviews.*

**Various** · 1987 · Indicators · intermediate

*Source coverage: partial. PDF pages inspected: 1, 4-6, 19, 175, 180, 191, 218, 242, 248, 275 (the article index and the MAE stop-setting, stochastic and Wyckoff position-sheet articles). These are study notes, not verified trading results.*

## Overview

This file is a bound compilation of Volume 5 (1987) of *Technical Analysis of Stocks & Commodities* magazine, sold as "S&C on CD." It is not a book with a single author or argument; it is 11 monthly issues stitched together, containing feature articles, editor's columns, letters, book reviews, and dozens of paid product reviews for 1980s charting software (Back Trak/High Tech, MetaStock, CompuTrac, options calculators, and similar). There is no unifying thesis. The value for a trader today is in a handful of recurring, well-documented threads: a 15-part serialized exposition of the Wyckoff Method (parts 9-15 run through this volume), John Sweeney's introduction of Maximum Adverse Excursion (MAE) as a stop-setting tool, John Ehlers' early cycle-analysis (MESA/maximum entropy) and BASIC-language charting programs, academic-style profitability studies of RSI and other oscillators, an explanatory piece on stochastics, an early CBOT Market Profile primer, and a recurring cast of columnists (John Sweeney as editor, Van K. Tharp on trading psychology, interviews with Larry Williams and Van Tharp).

## Core thesis

There is no single thesis; the magazine's implicit position, expressed repeatedly by editor John Sweeney, is that technical trading should be built on disclosed, testable rules rather than black-box software or gut calls, and that risk control (cutting losses, sizing stops from real data) matters more than signal generation. Several contributors push back on popular indicators: in an interview reprinted here, Larry Williams argues stochastics has no obvious edge in raw form and that traders fool themselves by eyeballing crossover charts that look good only in hindsight.

## Key concepts

- **Wyckoff Method** — Richard D. Wyckoff's early-1900s method of reading supply/demand from price and volume via Vertical (bar), Figure (point & figure), and Wave charts; treats chart action as the footprint of a manipulating "composite operator." Full method covered in the [The Wyckoff Method of Trading Stocks](https://ninad-k.github.io/trading-playbook/books/s-and-c--wyckoff-method.html) system page.
- **Position Sheet** — Wyckoff's manual tracking device (from 1916) that scores individual stocks into five positions (rally, reaction, and three others) to rank candidates for entry versus the market and sector.
- **Maximum Adverse Excursion (MAE)** — John Sweeney's technique of measuring how far price moves against a position before it becomes a winner, across a sample of historical trades, then setting the stop just beyond the point that separates winners from losers.
- **MESA (Maximum Entropy Spectrum Analysis)** — John F. Ehlers' cycle-extraction method, an alternative to Fourier analysis for finding a market's "dominant cycle" from noisy price data, used to tune moving-average and oscillator lengths.
- **Stochastic oscillator (%K/%D)** — (current close − lowest low over n) / (highest high over n − lowest low over n) × 100; %D is a moving average of %K; described in this volume with worked overbought/oversold thresholds.
- **Selling Climax / Technical Rally / Secondary Reaction / Springboard** — Wyckoff's sequence of chart events marking a bottom (mirrored by a Buying Climax at tops); each stage implies a different, decreasing level of risk for taking a long entry.
- **CBOT Market Profile / TPO (Time Price Opportunity)** — the Chicago Board of Trade's price-by-time-block display introduced to retail traders in this era; the volume's article explains estimating the intraday "value area" but stops short of full trading rules.
- **Modern Portfolio Theory applied to managed futures** — a two-part article (Antonacci) arguing MPT diversification benefits extend to a basket of trend-following futures programs, not just stocks and bonds.
- **Spread investing** — a four-part introductory series (Taucher) on intermarket and intramarket futures spreads as a lower-margin, lower-volatility alternative to outright positions.
- **Indicator profitability studies** — a recurring academic-style series (Drinka and Kille) back-testing RSI, stochastics, and other oscillators contract by contract (T-bonds, silver, Eurodollars) rather than asserting profitability from theory alone.

## Rules and setups

The magazine format means "rules" live inside individual articles rather than one coherent system. The most fully specified are Wyckoff's (see system page) and Sweeney's MAE procedure:

1. **MAE stop-setting (Sweeney)**: Take a completed trading system's historical trades on a given contract (Sweeney used four years of December T-bonds). For each winning trade, record the maximum adverse excursion (worst open loss) before it closed profitably. Set the stop distance at roughly the largest MAE seen across winners, rounded up (Sweeney used 19 points against a T-bond sample where winners rarely saw more than 18 points of adverse movement). This does not generate entries — it only sizes the stop for an existing system.
2. **Stochastic overbought/oversold (magazine's stated levels)**: %K/%D readings above 75 = overbought; below 24 = oversold. A 3-period moving average of raw %K gives %D Fast; a further 3-period average of %D Fast gives %D Slow, used to cut whipsaws.
3. **Wyckoff reward:risk filter**: Do not commit capital unless probable profit is at least 3x the dollar risk to the stop (detailed in the system page).
4. **Wyckoff position sizing note**: pyramiding (adding to a winner) is only justified when the stock has the potential for a further 10-15 point move; otherwise the added risk is not compensated.

No consolidated position-sizing or portfolio-level risk framework is given anywhere in the volume; each article's numbers apply only to its own example.

## Risk and money management

Risk discussion in this volume is scattered but consistent in tone: cut losses quickly, do not average down, and size the stop from evidence rather than habit. Wyckoff's stop rules (system page) and Sweeney's MAE technique are the two concrete, reusable procedures. A separate short item on money management ("Assessing Risk on Wall Street," Hull) and a Van Tharp psychology column ("The Danger in Profits") both argue that traders mismanage winners as often as losers — cutting winning trades short from fear of giving back profit is treated as a mirror-image mistake to letting losers run. No article in the volume gives a percent-of-equity position-sizing formula; sizing is implicitly left to whatever system produced the trade being stopped out.

## Psychology and discipline

Van K. Tharp contributes a recurring column across this volume, including "Winning Under Stress: The Fight-Flight Reaction" (physiological arousal degrades trading decisions the same way it does combat decisions), "The Loss Trap" (the sunk-cost tendency to hold losers to avoid "admitting" a mistake), and "The Danger in Profits" (giving back open profits out of fear, or closing winners too early from the same fear). A full interview with Tharp ("Trader's Psychologist") and one with Larry Williams round out the volume's psychology content. Wyckoff's own writing (excerpted in the Part 13-14 installments) is explicitly psychological: he insisted students "play a lone hand," avoid advisory-service dependence, commit only a fraction of capital until proven right, and develop patience for the right setup rather than staying in the market at all times.

## Chapter map

The volume has no chapters; it is organized by monthly issue (5:1 through 5:11). Notable recurring threads, in order of appearance:

- Issues 5:1-5:2 (pp. 1-126) — Product/software reviews; "In Search of the Perfect System"; early Drinka/Kille indicator-profitability studies; Wyckoff in Action Part 2.
- Issue 5:3 (pp. 127-250ish) — Wyckoff Method Part 9 (Position Sheet); Ehlers' Complete Computer Trading Program Part 1 (BASIC charting code); Market Profile intro.
- Issue 5:4 (pp. 248-310) — Wyckoff Part 10 (buy/sell tests, Figure 1 summary); Sweeney's MAE article; RSI profitability study.
- Issue 5:5 (pp. 311-380) — Wyckoff Part 11 (stop-order rules); Ehlers Part 3; Larry Williams interview (skeptical of stochastics).
- Issue 5:6 (pp. 374-420) — continued MPT-in-futures Part 2; Using Stochastics (Keel/Schmidt), full %K/%D explanation.
- Issue 5:7 (pp. 416-480) — Wyckoff Part 12 (Wave Chart); Enhanced Williams %R.
- Issue 5:8 (pp. 480-530) — Market Profile Value Area estimation (Jones); spread-investing series continues.
- Issue 5:9 (pp. 532-560) — Wyckoff Part 13 (trading apprenticeship, discipline rules).
- Issue 5:10 (pp. 557-625) — Wyckoff Part 14 (personal trading style); Ehlers' "How to Use Maximum Entropy" (MESA).
- Issue 5:11 (pp. 638-675) — Wyckoff Part 15 (final synthesis: manipulator campaign phases, chart patterns, support/resistance rules); Market Profile and Market Logic Part 1.

## Strengths and caveats

The Wyckoff series and the MAE article hold up well: both are concrete, numbers-based, and still cited in modern technical-analysis writing (MAE in particular became a standard concept in system-development software decades later). The indicator-profitability studies (Drinka/Kille) are a rare example, for 1987, of testing rather than asserting. Most of the rest of the volume is dated and low-value: the bulk of the page count is software/hardware product reviews for programs and computers (Apple II, IBM PC/XT, 640K RAM, dot-matrix printers) that no longer exist, and Ehlers' "Complete Computer Trading Program" is largely a line-by-line Applesoft BASIC listing rather than a portable set of rules. Some content is internally contradictory — Larry Williams dismisses stochastics as unproven in the same volume that runs an uncritical explanatory piece on the same indicator. Treat any single-contract, hindsight-optimized "profitability" result in these articles (MAE stop distances, indicator thresholds) as illustrative rather than robust; sample sizes are small (often one to four contracts) by modern standards.

## Who should read it

Traders curious about the original, non-derivative exposition of the Wyckoff Method, or about the historical origin of Maximum Adverse Excursion as a stop-sizing concept, will find both here in more depth than most modern secondary summaries. It is not a good entry point for someone wanting a coherent, modern trading system, and the software reviews and dated hardware discussion are skippable.

## Related books in this library

- [The Day Trader's Bible (My Secrets of Day Trading in Stocks)](https://ninad-k.github.io/trading-playbook/books/wyckoff-richard-d-the-day-trader-s-bible-or-my-secret-in-day-trading-of-stocks-2.html) — Wyckoff's own writing, for readers who want the primary source behind the magazine's 15-part series.
- [A Six-Part Study Guide to Market Profile](https://ninad-k.github.io/trading-playbook/books/cbot-a-six-part-study-guide-to-market-profile.html) — a fuller treatment of Market Profile than the single introductory article in this volume.
- [Stop Worrying Yourself Out of Profits](https://ninad-k.github.io/trading-playbook/books/van-tharp-stop-worrying-yourself-out-of-profits.html) — the same Van Tharp piece reprinted in this volume's issue 5:5, on its own.
- [Special Report on Money Management](https://ninad-k.github.io/trading-playbook/books/money-management-report-van-tharp.html) — Tharp's dedicated treatment of position sizing, absent from this volume.
- [Trade Stocks and Commodities with the Insiders: Secrets of the COT Report](https://ninad-k.github.io/trading-playbook/books/williams-larry-trade-stocks-and-commodities-with-the-insiders.html) — Larry Williams' own material, for context on his stochastics skepticism voiced in the interview here.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: magazine-anthology, wyckoff, stochastics, maximum-adverse-excursion, market-profile, cycles, spread-trading, sentiment
