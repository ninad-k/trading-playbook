---
author: William R. Gallacher
category: Options, Futures & Derivatives
difficulty: advanced
doc_type: book
one_liner: An empirical, 1996-data-driven study of commodity option pricing that finds
  no inherent writer's edge, then builds one through defensive straddle writing.
pages: 294
related:
- lawrence-g-mcmillan-profit-with-options
- hull-options-futures-and-other-derivative-securities-5th-ed
- using-volatility-in-option-tradingpart-1
- volatility-part-2
- balsara-nauzer-j-money-management-strategies-for-futures-traders
reviewed_pdf_pages: 13, 16, 24, 30, 35, 51, 62, 67, 76 (the MAD and market-volatility
  formulas, the implied-volatility shortcut and the payout-ratio study tables)
slug: mcgraw-hill-the-options-edge-winning-the-volatility-game-with-options-on-futures
source_file: Mcgraw Hill - The Options Edge Winning The Volatility Game With Options
  On Futures.pdf
source_review: partial
tags:
- options-on-futures
- volatility
- straddle-writing
- implied-volatility
- option-pricing
- defensive-hedging
- commodity-options
tier: A
title: 'The Options Edge: Winning the Volatility Game with Options on Futures'
year: 1999
---

## Overview

William Gallacher, a futures trader and author of Winner Take All, set out to answer a question he found unanswered in the literature: does the writer or the buyer of a commodity option have the mathematical edge? Rather than theorize, he built a two-year (1996-98) database of daily option and futures prices across 15 commodities and tested straddle writing and buying empirically. The book spends its first half critiquing option-pricing theory (the normal-distribution assumption, the Black-Scholes "million dollar formula") and building a simpler alternative from first principles, then spends the second half reporting what actually happened when 3,781 hypothetical at-the-money straddles were bought or written and held to expiry.

## Core thesis

Contrary to conventional wisdom, indiscriminate option writing carries no inherent edge — the aggregate payout ratio (average payout ÷ average premium) across the 1996 test came out almost exactly 1.0, meaning the option market prices itself fairly on average. Any edge the writer can extract has to be manufactured through discipline: (1) a mechanical defensive rule that offsets a straddle's losing side with a futures position once the market moves against it, and (2) selectivity, writing only when implied volatility exceeds a measured "market volatility." Gallacher also argues that the Black-Scholes formula is built on a false premise (that futures price changes are normally distributed) and, while usable for at-the-money options, systematically misprices out-of-the-money options because it underweights the fat tails real commodity prices exhibit.

## Key concepts

- **Million dollar formula** — Gallacher's name for Black-Scholes as applied to futures options; he argues it is directionally correct but scope-limited, working only near the money.
- **Mean absolute deviation (MAD)** — the average, unsigned daily price change over a lookback window (he uses 30 days), his preferred and more intuitive alternative to standard deviation for measuring market volatility.
- **Market volatility formula** — Market volatility = 22 × MAD (expressed as a percentage of futures price); originally derived as 20 × MAD, then empirically recalibrated to 22 so that valuation comparisons split the 1996 sample roughly in half.
- **Implied volatility (ATM shortcut)** — for an at-the-money option, Implied volatility ≈ 40 × (ATM option price) ÷ (futures price × √(days to expiry)), his simplified, algebra-light substitute for solving Black-Scholes for volatility.
- **Payout ratio** — average dollar payout to option buyers at expiry ÷ average premium collected by writers; the book's core scorecard, with 1.0 meaning no edge to either side.
- **U-factor (unreflected uncertainty)** — the portion of an option's premium tied to a specific, dated, upcoming resolution of uncertainty (a Fed meeting, a USDA report, an OPEC meeting) that is not yet showing up in the futures' recent price variability.
- **Writer's edge** — the discipline-derived improvement in the payout ratio (from 1.00 toward roughly 0.85-0.88) achieved through defensive futures hedging and volatility-based selectivity.
- **Straddle vs. strangle** — writing at-the-money puts and calls together (straddle) versus out-of-the-money combinations (strangle); the book argues straddles are structurally superior for writers because they yield the maximum premium per position.
- **Normal-distribution critique** — Gallacher's statistical case, using coffee futures data, that daily commodity price changes have far fatter tails than a normal curve predicts, which is why theoretical pricing models misprice out-of-the-money options.
- **Trading edge vs. return on capital** — his distinction between the gross statistical edge (percent of premium kept) and the very different number (annualized return on required margin/equity) that actually matters to a trader.

## Rules and setups

The complete mechanical system — defensive futures hedging plus volatility-based straddle selection — is documented in the companion page [[mcgraw-hill-the-options-edge-winning-the-volatility-game-with-options-on-futures--defensive-straddle-writing]]. In brief: write at-the-money straddles only when implied volatility exceeds 22×MAD market volatility; hedge the losing side with an offsetting futures position once the future closes beyond the strike plus/minus the premium collected; and protect the hedge itself with a second trigger if it reverses through the original strike. Gallacher explicitly tested and rejected two further selectivity ideas as statistically unsound: comparing implied volatility to a commodity's long-term historical average (impossible to use without hindsight, since the average can only be computed after the fact) and writing options based on a forecast of trend versus range-bound conditions (untestable, since that forecast isn't knowable in advance either).

## Risk and money management

Gallacher frames option writing as a diversification and capital-efficiency play rather than a directional bet: because a straddle's value can only rise against the writer with a genuinely large futures move, the odds of many independent straddles going bad simultaneously are low, letting a diversified short-option book run on relatively little margin. His worked example: $100,000 in equity supports enough straddle writing to collect roughly $100,000 in premium (averaging about 4 months to expiry), most of which is redeployed as T-bill collateral; an 8% net trading edge (after commissions and slippage) plus roughly 5% T-bill interest on the collateral produces an illustrative ~32% annualized return. He sets a practical floor of about $2,500 in premium per straddle, below which fixed commission costs (roughly $130 per straddle round-trip) erode the edge to nothing, which effectively excludes low-premium markets like sugar, cocoa, and cattle from his approach. He estimates the theoretical 15% gross writer's edge shrinks to about 12% after execution slippage and to roughly 8% net after commissions.

## Psychology and discipline

The book's psychological argument is narrow but pointed: option writers, unlike option buyers, must be willing to act — closing out or hedging a losing straddle — while it is still only moderately underwater, because delay compounds losses in a business built on thin margins. Gallacher recounts his own "false starts" learning to write options and generalizes that most traders, himself included, are prone to giving a losing position "one more day" that becomes "one more week." He also devotes space to warning against confirmation bias in research (citing the Beardstown Ladies and Victor Niederhoffer as cautionary examples of spurious correlations mistaken for edges) and to the cautionary tale of Long-Term Capital Management, whose reliance on a Black-Scholes-style normal-distribution model he presents as a real-world confirmation of his statistical critique.

## Chapter map

- Ch 1 — Roads Less Traveled — the book's empirical rationale and methodology.
- Ch 2 — Fast Forward — option basics, the writer/buyer relationship, and expectation as a zero-sum game.
- Ch 3 — Ockham's Equation — building a simplified option-pricing model from first principles; the normal-distribution critique.
- Ch 4 — The Word of God — a detailed critique of the Black-Scholes ("million dollar") formula's assumptions and scope.
- Ch 5 — The Emperor of China's Nose — estimating volatility from imperfect data; why averaging multiple estimates helps.
- Ch 6 — Phantom of the Option — building the 1996-98 database; implied vs. market volatility formulas.
- Ch 7 — The Promised Land — the core empirical finding: aggregate payout ratio ≈ 1.0, no inherent writer's edge.
- Ch 8 — Born Again — the defensive futures-hedging strategy, volatility-based selectivity, and the U-factor.
- Ch 9 — The Armchair Bookmaker — execution costs, commissions, position sizing, and realistic return-on-capital math.
- Ch 10 — Volatility Profiles — reference appendix of historical volatility data and charts by commodity.

## Strengths and caveats

The book's empirical, data-first method is unusual and valuable in a genre dominated by theory; its statistical honesty (rejecting his own promising-looking but hindsight-biased test results) is a model of good practice. Caveats: the entire quantitative case rests on a single calendar year (1996) of data across 15 commodities, a sample Gallacher himself flags as possibly unrepresentative; commission and margin figures reflect 1990s brokerage pricing and need heavy rescaling; and the S&P 500 discussion, written mid-bull-market in 1998, explicitly acknowledges it may not generalize. The book also predates decimalization, electronic execution, and the collapse of retail option commissions, all of which materially change the $2,500 minimum-premium threshold and the practicality of the defensive strategy today.

## Who should read it

Futures and commodity option traders who want a rigorously tested, numbers-first case for (and against) systematic straddle writing, and readers who want a plain-language, skeptical critique of Black-Scholes-style option pricing without wading into stochastic calculus.

## Related books in this library

- [[lawrence-g-mcmillan-profit-with-options]] — a more conventional, strategy-catalog treatment of options that complements Gallacher's single-minded focus on straddle writing.
- [[hull-options-futures-and-other-derivative-securities-5th-ed]] — the academic, formula-heavy treatment of the same pricing theory Gallacher spends much of the book arguing against.
- [[using-volatility-in-option-tradingpart-1]] — a shorter, complementary treatment of trading implied versus historical volatility.
- [[volatility-part-2]] — further practical volatility-trading material to pair with Gallacher's market-volatility formulas.
- [[balsara-nauzer-j-money-management-strategies-for-futures-traders]] — futures-specific money management to pair with the book's thin treatment of capital allocation across a straddle-writing book.
