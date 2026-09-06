---
author: Bruce I. Jacobs and Kenneth N. Levy (editors)
category: Quant, Microstructure & Academic Research
difficulty: advanced
doc_type: book
one_liner: 'Institutional anthology on market neutral investing: equity long-short,
  convertible, sovereign bond, MBS and merger arbitrage, plus the Askin and LTCM collapses
  as risk-management case studies.'
pages: 304
related:
- wyser-pratte-guy-risk-arbitrage
- paul-wilmott-quantitative-finance
- article-market-neutral-investing-long-short-hedge-fund-strategies-joseph-g-nicholas-2000
- hedge-fund-risk-factors-and-value-at-risk-of-credit-trading-strategies
- trading-and-investment-applied-quantitative-methods-for
reviewed_pdf_pages: 4, 10, 14, 18, 43, 55-57, 73, 298 (the margin rules, the worked
  equity-market-neutral capital deployment example and the strategy chapters)
slug: marketneutralstrategies
source_file: Marketneutralstrategies.pdf
source_review: partial
tags:
- market-neutral
- long-short
- pairs-trading
- arbitrage
- convertible-arbitrage
- merger-arbitrage
- hedge-funds
- leverage
tier: A
title: Market Neutral Strategies
year: 2005
---

## Overview

Edited by Jacobs Levy Equity Management principals Bruce Jacobs and Kenneth Levy, this is a multi-author institutional reference (part of the Frank J. Fabozzi Series) rather than a single trading system. Contributing practitioners cover five distinct market neutral strategies — equity long-short, convertible bond hedging, sovereign fixed-income arbitrage, mortgage-backed securities (MBS) arbitrage, and merger (risk) arbitrage — plus a chapter dissecting the failures of Askin Capital Management (1994) and Long-Term Capital Management (1998), and chapters on "alpha transport" and tax/ERISA treatment. The audience is institutional investors, consultants and sophisticated individual investors; the book assumes familiarity with basic investment concepts and mostly avoids heavy mathematics.

## Core thesis

A market neutral portfolio holds long and short positions selected from the same asset class so that the aggregate position has negligible sensitivity to that asset class's systematic risk (a portfolio beta near zero), leaving only the spread in performance between the securities held long and those sold short — pure security-selection return, independent of market direction. Properly built market neutral strategies are not "safe" merely because they are labeled neutral: true benefit comes only from an *integrated* optimization of long and short positions together, not from bolting a separate short book onto a long-only one, and every strategy in the book retains its own residual risks (credit, liquidity, model, and especially leverage risk) that can overwhelm the strategy when markets move to extremes.

## Key concepts

- **Market neutral / beta zero** — long and short positions sized and weighted so systematic (market or interest-rate) risk cancels, leaving only relative-value (security selection) risk.
- **Integrated optimization** — constructing long and short legs jointly in one optimization (using expected returns, return standard deviations, and correlations) rather than as two separate long-only and short-only portfolios; this is what actually frees the portfolio from benchmark-weight constraints.
- **Liquidity buffer** — cash held back (roughly 10% of capital) to absorb daily mark-to-market swings on short positions without breaching margin.
- **Short rebate** — interest paid back to the investor on cash proceeds from a short sale, after the lender's and prime broker's "haircut" (typically 25–30 basis points off the full rate).
- **Delta (convertibles)** — the convertible bond's rate of price change per $1 move in the underlying stock; approaches 1 deeply in-the-money, approaches 0 deeply out-of-the-money (unless bankruptcy risk pushes it back toward or above 1).
- **Duration (convertibles)** — sensitivity of the convertible's value to a change in interest rates; dominant when the bond is out-of-the-money.
- **Cash-and-carry / basis trade** — buying a cash bond and selling the deliverable futures contract (or the reverse, "short basis"), profiting from convergence at delivery.
- **Cheapest-to-deliver (CTD) and factor bias** — in bond futures, the bond in the deliverable basket with the lowest net basis; conversion factors are used to homogenize bonds of different coupons/maturities, and this factor mechanism creates predictable, mathematically-driven relationships between the futures price and each deliverable bond.
- **Option-adjusted spread (OAS)** — a security's expected return spread over the forward yield curve after adjusting for embedded options (e.g., a mortgage's prepayment option); used to screen MBS for cheapness but highly sensitive to the accuracy of the prepayment model.
- **Fixed vs. contingent exchange ratio (merger arbitrage)** — a fixed-ratio stock merger specifies the exact number of acquirer shares per target share up front (short the fixed ratio against the long target position); a contingent (floating) ratio depends on the acquirer's average price over a pricing period near closing.
- **Arbitrage spread** — the percentage gap between the current combined value of a merger arbitrage position and its value on deal completion; compensation for the risk of deal failure.
- **Alpha transport** — using derivatives to move the excess return ("alpha") generated by a market neutral portfolio in one asset class onto exposure to a different asset class's market return (beta).
- **Reg T / maintenance margin** — Federal Reserve Regulation T requires at least 50% margin to initiate a short position; NYSE Rule 431 sets maintenance margin at roughly 25% of price for longs and the greater of $5/30% (or $2.50/100% for sub-$5 stocks) for shorts.

## Rules and setups

This is an institutional reference, not a signal-generation system, so "setups" are portfolio-construction and hedge-ratio rules rather than entries/exits on a chart. The book's concrete, codeable rules:

1. **Equity market neutral capital deployment** — of $10 initial capital, ~90% goes long, an equal ~90% is sold short, and ~10% is retained as a liquidity buffer; Reg T requires only 50% collateralization to establish shorts, so this structure is comfortably within margin (illustrated at 55.6% initial margin on a $10M account with $9M long / $9M short).
2. **Rebalancing trigger** — when long/short values drift out of balance (from differential returns or price moves), trade back toward equal dollar-weighted long and short exposure; a 2% long-short return spread on a $9M/$9M book required trading roughly $0.2M to restore balance and the 10% liquidity buffer.
3. **Convertible bond delta hedge** — buy the convertible, short shares equal to (delta × conversion ratio) of the underlying; worked example: Staples 5% convertible at $965, delta-neutral hedge ratio of 0.40 → short 12.3 shares of stock trading at $31.50 per convertible bond.
4. **Convertible bond duration hedge** — additionally short Treasury note futures in the ratio given by the interest-rate hedge ratio (e.g., $2.09 per 100bp shift → short 0.00209 of a five-year futures contract per bond) to neutralize interest-rate exposure as well as delta.
5. **Convertible universe filter** — restrict to convertible issues of at least $100 million outstanding for adequate liquidity; rebalance the hedge monthly as delta/duration drift.
6. **Sovereign bond basis trade (factor weighting)** — sell futures contracts equal to (notional bond value × conversion factor) ÷ contract size; buy back any excess ("tail") at the futures settlement price on delivery to eliminate residual exposure.
7. **Merger arbitrage, fixed exchange ratio** — buy 1 share of the target, short (exchange ratio) shares of the acquirer; profit is the arbitrage spread if the deal closes, annualized over the expected time to close; example: HP–Compaq 0.6325 exchange ratio produced a 7.8% spread (29.4% annualized) at announcement, which widened to 47.4% mid-deal on proxy-fight news before the deal closed at an 8.9% total return.
8. **Position sizing discipline for shorting** — keep individual short positions small and diversified across many names to limit exposure to short squeezes and buy-ins; avoid concentrated shorts in illiquid stocks.

## Risk and money management

Leverage is the book's central risk theme: it is optional in equity market neutral (an investor can choose $50 long/$50 short per $100 of capital for zero net leverage) but many funds run levered, and leverage magnifies both the strategy's expected edge and its potential for catastrophic loss. Reg T allows up to 2:1 leverage for equity market neutral; convertible bond hedgers, because the long convertible and its short partially offset for margin purposes, can lever considerably higher — some funds held convertible positions worth up to 13x equity capital. Short positions carry additional cost and risk beyond long-only investing: the short rebate haircut, uptick-rule constraints on when a short sale can be executed, recall/buy-in risk if a lender calls back borrowed shares, and daily mark-to-market cash calls. The book's most consequential quantitative risk lesson comes from Long-Term Capital Management: after asset sales in July 1998 LTCM's leverage ratio was already about 30-to-1; August losses pushed it to 55-to-1; by the September 1998 bailout it exceeded 100-to-1 (excluding over $1 trillion notional in derivatives) — a level none of the fund's own managers had anticipated, illustrating how losses on a leveraged book mechanically increase leverage and can trigger a liquidity spiral of margin calls precisely when assets are hardest to sell.

## Psychology and discipline

The "Tale of Two Hedge Funds" chapter functions as the book's discipline section, using the 1994 collapse of Askin Capital Management (ACM) and the 1998 collapse of LTCM as parallel case studies. ACM's manager based "at least 50%" of buy/sell decisions on "gut instinct" rather than tested models, produced a February 1994 loss statement that understated the fund's true losses, and continued adding to a losing CMO position (inverse IOs) even as evidence mounted against it — a failure of process and transparency rather than of sophistication. LTCM, by contrast, was staffed by highly credentialed quants but placed excessive confidence in historical correlations between markets that had never before diverged together; when Russia's 1998 default triggered a global flight to quality, those historical relationships broke down simultaneously and LTCM's relative-value trades all moved against it at once — a failure of diversification of *ideas*, not just of securities. The book's explicit lesson: high apparent returns combined with apparently low risk should be a "yellow light," not a green one (quoting Nobel laureate William Sharpe: "you can't earn 40% a year without some risk of losing a lot of money"), and investors should independently interrogate the sources of leverage, transparency, and the fundamental (versus merely historical/statistical) basis for a strategy's claimed neutrality.

## Chapter map

- Ch 1 — Introduction — defines market neutral investing, distinguishes it from hedge funds and market timing, surveys the five strategies covered and their risk/benefit tradeoffs.
- Ch 2 — Questions and Answers About Market Neutral Investing — Q&A format covering neutrality mechanics, sources of return, leverage, and shorting vs. futures-based neutrality.
- Ch 3 — Market Neutral Equity Investing — the core long-short construction chapter: mechanics, margin, integrated optimization vs. long-plus-short, trading and liquidity-buffer rules.
- Ch 4 — Convertible Bond Hedging — delta/duration hedging mechanics, an empirical study of excess returns (1989–1996), and implementation issues (busted convertibles, borrow availability, leverage).
- Ch 5 — Sovereign Fixed-Income Arbitrage — cash-and-carry basis trades, cheapest-to-deliver, factor bias in government bond futures.
- Ch 6 — Market Neutral Strategies with Mortgage-Backed Securities — CMO security selection, option-adjusted spread analysis, prepayment-model risk.
- Ch 7 — Merger Arbitrage — fixed and contingent exchange-ratio stock mergers, cash-flow mechanics, the HP–Compaq case study.
- Ch 8 — Transporting Alpha — using derivatives to combine a market neutral portfolio's alpha with a different asset class's market return.
- Ch 9 — A Tale of Two Hedge Funds — the Askin Capital Management and LTCM collapses, and lessons for investors on leverage, transparency and diversification of insight.
- Ch 10 — Significant Tax Considerations for Taxable Investors in Market Neutral Strategies — UBTI, short-sale tax treatment, and related issues.
- Ch 11 — Tax-Exempt Organizations and Other Special Categories of Investors: Tax and ERISA Concerns.
- Ch 12 — Afterword.

## Strengths and caveats

Written by working practitioners (Jacobs Levy, PAAMCO, Clinton Group, DKR Capital, Och-Ziff/CNH Partners) with real trade examples, worked numeric hedge ratios and actual cash-flow tables (Staples convertible, HP-Compaq merger), which makes several of its rules directly codeable. The Askin/LTCM chapter is an unusually candid institutional post-mortem. Caveats: this is a 2005 book describing mid-1990s to early-2000s market structure — the SEC uptick rule (Rule 10a-1) discussed at length was later eliminated (2007) and partially replaced by an alternative uptick rule in 2010; commission and short-rebate figures reflect pre-decimalization, pre-electronic-market conditions; the convertible-hedging "empirical analysis" in Chapter 4 covers a single 1989–1996 sample from one analyst and should be read as illustrative rather than a rigorous backtest; and several strategies (sovereign basis trading, MBS OAS analysis) require institutional-grade repo, prime brokerage and analytics access not available to individual traders. The book's own conclusion — echoed almost verbatim in the LTCM chapter — is that no strategy examined is riskless "market neutral" in the pure sense; the label describes a construction technique, not an absence of risk.

## Who should read it

Institutional allocators, hedge fund analysts, and advanced individual traders who already understand long-only portfolio construction and want a grounded, non-quantitative-heavy survey of how professional long-short, convertible-arbitrage, fixed-income-arbitrage, MBS-arbitrage and merger-arbitrage desks actually build and hedge positions — and who want the Askin/LTCM chapter as a risk-management case study. Not a beginner's book and not a mechanical trading-signal system; readers wanting entry/exit rules for a specific instrument should pair it with a strategy-specific text.

## Related books in this library

- [[wyser-pratte-guy-risk-arbitrage]] — a dedicated, more detailed treatment of the merger arbitrage strategy covered in Chapter 7 here.
- [[paul-wilmott-quantitative-finance]] — deeper quantitative/derivatives-pricing background for the option-adjusted-spread and delta-hedging math used across several chapters.
- [[article-market-neutral-investing-long-short-hedge-fund-strategies-joseph-g-nicholas-2000]] — a shorter treatment of the same core market-neutral long-short thesis from a different author.
- [[hedge-fund-risk-factors-and-value-at-risk-of-credit-trading-strategies]] — complements the leverage/VaR risk themes of the Askin and LTCM case studies.
- [[trading-and-investment-applied-quantitative-methods-for]] — broader quantitative-methods context for the portfolio-optimization techniques referenced in the equity market neutral chapter.
