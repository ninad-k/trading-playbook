---
author: Mark D. Wolfinger
category: Options, Futures & Derivatives
difficulty: beginner
doc_type: book
one_liner: A retail-investor guide to replicating a hedge-fund-like return profile
  by writing covered calls (or uncovered puts) on a diversified basket of optionable
  ETFs.
pages: 254
related:
- lawrence-g-mcmillan-profit-with-options
- guy-cohen-the-bible-of-options-strategies
- using-options-to-buy-stocks-build-wealth-with-little-risk-and-no-capital
reviewed_pdf_pages: 2, 4, 33-34, 87, 127, 144, 163 (the BXM benchmark chapters, options
  basics, and the worked covered-write portfolio examples)
slug: m-wolfinger-create-your-own-hedge-fund-increase-profits-and-reduce-risk-with-etfs-and-opti
source_file: M Wolfinger - Create Your Own Hedge Fund - Increase Profits And Reduce
  Risk With Etfs And Options.pdf
source_review: partial
tags:
- covered-calls
- uncovered-puts
- etfs
- options-income
- portfolio-construction
- modern-portfolio-theory
- volatility
tier: A
title: Create Your Own Hedge Fund
year: 2005
---

## Overview

Wolfinger's pitch is that an individual investor, following the tenets of modern portfolio theory (MPT), can approximate the risk-adjusted return profile that hedge funds market to wealthy clients — enhanced returns with reduced volatility — using only a diversified basket of exchange-traded funds (ETFs) and standard exchange-listed options, at retail brokerage cost. The book walks from MPT and the case against stock-picking/market-timing, through how ETFs work and why they beat traditional mutual funds for this purpose, through option mechanics, and into two specific option-writing strategies — covered call writing and uncovered (cash-backed) put writing — supported by historical index data (the CBOE's BuyWrite Index, BXM) and a full simulated year of month-by-month portfolio management.

## Core thesis

Reliably outperforming a buy-and-hold index over the long run by picking stocks or timing the market is very unlikely (the MPT/efficient-markets argument), so an investor's edge should come from a structural, repeatable modification to a passive portfolio rather than from prediction. Selling call options against owned ETF shares (or, equivalently in risk terms, selling cash-backed put options) collects an option premium every expiration cycle; that premium (a) increases the probability that a given month is profitable, (b) reduces portfolio volatility versus buy-and-hold, and (c) caps the upside in a strongly rising market — but historical BXM index data show that the premium collected across many cycles more than compensates for the capped upside over most multi-year periods, because markets spend more time drifting or moving moderately than in strong sustained rallies.

## Key concepts

- **Modern Portfolio Theory (MPT)** — Markowitz's framework: for a given risk level there is an "efficient frontier" of maximum expected return; diversification reduces risk without proportionally reducing return.
- **Exchange-traded fund (ETF)** — a basket security tracking an index (e.g., VTI/Wilshire 5000, IWV/Russell 3000, DIA/Dow 30, OEF/S&P 100, EFA/MSCI EAFE) that trades and is optionable like a stock, unlike traditional open-end mutual funds.
- **Covered call writing** — selling a call option against 100 shares already owned per contract; collects the premium in exchange for capping the stock's upside at the strike price for that expiration.
- **Uncovered (naked, cash-backed) put writing** — selling a put option while holding cash equal to the exercise obligation; economically equivalent in risk/reward to covered call writing at the same strike, but used when the goal is to acquire the underlying at a discount rather than to hedge shares already owned.
- **Strike selection styles**: out-of-the-money (OTM, most bullish/aggressive, least protection, most upside participation), at-the-money (ATM, maximum time premium, moderate protection), in-the-money (ITM, most conservative, most downside protection, least upside).
- **Time premium vs. intrinsic value** — an option's price splits into intrinsic value (in-the-money amount) and time premium (everything else); time premium is the covered call writer's maximum profit from the option leg alone.
- **BuyWrite Index (BXM)** — the CBOE's benchmark tracking a hypothetical S&P 500 portfolio that sells the nearest slightly-OTM one-month call each cycle and holds it to cash-settled expiration; used as the book's evidentiary base for covered call writing's long-run performance.
- **Rolling a position** — closing the currently written option and simultaneously selling a new one with a different strike and/or later expiration; "rolling down and out" (lower strike, later date) adds downside protection when the market falls; "rolling up and out" (higher strike, later date) captures more upside participation when the market rises, at the cost of new capital risked.
- **Break-even points** — upside break-even (strike + premium collected, for calls) marks where a covered call writer starts to underperform an unhedged holder; downside break-even (entry price − premium collected) marks where the position starts to lose money versus cash.
- **Volatility Index (VIX)** — the CBOE's implied-volatility gauge; higher VIX means richer option premiums (more income per contract written) and is read as a rough fear gauge.
- **Effective/net exposure and delta** — mentioned in the options-basics chapters as the standard Greeks vocabulary (ITM options have delta near 1, OTM near 0, ATM near 0.5) used to reason about how closely an option tracks the underlying.

## Rules and setups

1. **Instrument selection**: only ETFs (or stocks) with listed, liquid options; buy and hold in round lots of 100 shares so every 100-share block can carry exactly one written option contract.
2. **Portfolio construction**: allocate across several optionable ETFs (index breadth, cap-size tilt, growth/value tilt, and a foreign-market sleeve such as EFA are all illustrated); Wolfinger's own worked example uses a $100,000 three-ETF portfolio (EFA, MDY, VTI/OEF) to walk through a full trading year.
3. **Which option to write** (per cycle, per holding): choose the front-month (nearest) expiration by default. Pick strike based on objective — OTM if primarily seeking capital gains and only secondarily premium income; ATM/near-the-money for the "recommended" balanced style that maximizes time premium collected while retaining some upside; ITM when the outlook is mildly bearish and additional downside protection is wanted. Wolfinger's personal, stated default is writing slightly in-the-money.
4. **Minimum acceptable premium**: when writing uncovered puts specifically to earn income (not primarily to acquire stock), do not sell for less than roughly 0.5% per month after commissions as a floor; the author's personal target is about 1.5% per month.
5. **Cycle management (stay fully invested)**: at each expiration, if the option expired worthless, immediately write a new option (typically the next Monday morning) against the same shares to remain continuously hedged; if assigned (shares called away, or put shares put to you), reinvest the proceeds the same or next trading day into the same or a different ETF and write new options against the new position.
6. **Sizing an index hedge precisely** (when trying to mimic an index like BXM exactly rather than using ETFs): number of index option contracts = portfolio value ÷ (strike price × 100); round down, since fractional contracts are not allowed. Wolfinger recommends against this approach for most investors — use round-lot ETFs and slightly-OTM calls instead to hedge the full portfolio without leftover unhedged capital.
7. **Rolling for protection**: when a written call's remaining premium has decayed to the point it offers little downside protection and the market is falling, buy back the call and simultaneously sell a new call with a lower strike and/or a later expiration ("rolling down and out") to add fresh downside cushion.
8. **Rolling for profit**: when the underlying has rallied enough that the written call is now meaningfully in the money and there is still time value left in a further-out, higher-strike call, buy back the current call and sell a higher-strike, later-dated call ("rolling up and out") — but only when the additional premium/potential gain justifies the additional capital put at risk, since this locks in more paid-out risk if the market reverses.
9. **Risk of writing too many uncovered puts**: always know, and keep sufficient cash for, the total exercise obligation across every naked put currently written; never rely on margin to cover the full nominal obligation.

## Risk and money management

The two core strategies (covered calls and cash-backed uncovered puts) are stated to carry identical risk profiles: maximum loss is the ETF going to zero, offset by the premium collected; maximum profit is the collected time premium plus (for OTM writes) any gain up to the strike. Uncovered put writers are warned specifically against over-extending — selling more puts than they can cover in cash — since it is easy to underestimate the true exercise obligation on a naked short put ("$50 per contract" framing hides a $2,000+ per-contract buy obligation). The book's stated numeric example: a $20,000 stock buyer and a 10-lot writer of $20 puts face the same $20,000 worst case, but the put writer's cash-backed cushion is reduced by the premium received. No formal position-sizing formula (percent-of-equity, fixed-fractional, etc.) is given; sizing is implicit in "buy round lots" and "keep the strategy applied to the entire portfolio."

## Psychology and discipline

Wolfinger frames covered call writing as psychologically demanding in a specific way: it performs worse than unhedged buy-and-hold in strongly rising markets, and a writer who cannot tolerate watching a written call rally deep in the money — and is tempted to buy it back "to stop the bleeding" and hold the shares unhedged, hoping to fully participate in further gains — will sabotage the strategy's long-run edge. The book's explicit advice is to accept the capped-upside months as the cost of steadier, higher-probability profits in flat and moderately bullish/bearish months, to pick one style (aggressive OTM vs. conservative ITM) that matches personal risk tolerance, and to stay consistent rather than guessing month to month which style will do best — since guessing direction is exactly what MPT argues investors cannot reliably do.

## Chapter map

- Part I (Ch. 1–3) — Outperforming the Market: modern portfolio theory, the case against stock-picking/market-timing, and what hedge funds actually do.
- Part II (Ch. 4–6) — Exchange Traded Funds: history of mutual funds vs. ETFs, mechanics of traditional mutual funds, and ETF structure/advantages.
- Part III (Ch. 7–12) — Options: option basics and terminology, why investors buy/sell options, covered call writing mechanics, uncovered put writing mechanics, and historical evidence (BXM, VIX).
- Part IV (Ch. 13–17) — Putting It All Together: building a diversified ETF portfolio (with sample $100,000 portfolios and lists of optionable ETFs/HOLDRs/SPDRs), choosing a strike-selection style, a full simulated year of covered call trading month by month, the same for uncovered put writing, and closing odds and ends.

## Strengths and caveats

The BXM/VIX historical evidence (1988–2004) and the fully worked month-by-month trading year are unusually concrete for a retail options book and make the mechanics (rolling, assignment handling, break-even math) genuinely codeable. The book is explicitly time-bound: option and ETF prices, commission schedules ($10/order plus $1.50/contract, in the author's example), and the ETF universe (early iShares/SPDR/HOLDRs line-up circa 2004) are all dated, and several named products (e.g., certain HOLDRs) no longer trade in that form. The BXM comparison period (1988–2004) was unusually favorable to a "slightly bullish, income-collecting" strategy and underperformed buy-and-hold specifically during the strongest bull years (1995–1999), a limitation the author acknowledges directly. No true "collar" (protective put purchased against covered stock) is discussed — despite surface similarity, the book's two core strategies are covered calls and naked cash-backed puts, not a collar; readers looking for defined-risk collar mechanics need a different source. The strategy's real-world edge is also sensitive to option liquidity and bid/ask spreads on less-traded ETFs, which the book does not quantify.

## Who should read it

Buy-and-hold ETF investors who already accept the MPT case against stock-picking and want a mechanical, repeatable way to add income and reduce volatility using options they are willing to actively manage every expiration cycle; a good practical companion to a first options textbook, since it deliberately restricts itself to two strategies rather than surveying the full options-strategy menu.

## Related books in this library

- [[lawrence-g-mcmillan-profit-with-options]] — broader options-strategy reference for readers who want strategies beyond covered calls and cash-backed puts, including true hedged/collar structures this book does not cover.
- [[guy-cohen-the-bible-of-options-strategies]] — a fuller strategy catalogue to cross-reference the covered-call and short-put payoff diagrams against other income and hedging structures.
- [[using-options-to-buy-stocks-build-wealth-with-little-risk-and-no-capital]] — complementary reading on using puts/calls to acquire stock positions at a discount, the same objective behind Wolfinger's uncovered-put-writing chapters.
