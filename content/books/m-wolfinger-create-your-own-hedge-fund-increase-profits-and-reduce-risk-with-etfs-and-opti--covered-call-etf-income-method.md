---
title: Covered Call / Uncovered Put ETF Income Method
author: Mark D. Wolfinger
year: 2005
slug: m-wolfinger-create-your-own-hedge-fund-increase-profits-and-reduce-risk-with-etfs-and-opti--covered-call-etf-income-method
tier: A
category: Options, Futures & Derivatives
tags: [covered-calls, uncovered-puts, etfs, options-income, rolling, strike-selection]
difficulty: beginner
doc_type: system
parent: m-wolfinger-create-your-own-hedge-fund-increase-profits-and-reduce-risk-with-etfs-and-opti
pages: 254
one_liner: "A mechanical, cycle-by-cycle method for writing covered calls (or cash-backed puts) against a diversified round-lot ETF portfolio, with strike-selection and rolling rules."
related: [lawrence-g-mcmillan-profit-with-options, guy-cohen-the-bible-of-options-strategies]
source_file: "M Wolfinger - Create Your Own Hedge Fund - Increase Profits And Reduce Risk With Etfs And Options.pdf"
---

## What it is

A repeatable monthly-cycle option-writing overlay for a diversified ETF portfolio: own round lots (100-share multiples) of several optionable, broad-market ETFs and, every expiration cycle, sell one call per 100 shares held (or, as a variant, sell cash-backed puts, which carry the same risk profile). It assumes the investor cannot reliably time or pick the market and instead extracts a repeatable premium edge cycle after cycle, trading some upside for higher win-rate income and lower volatility than plain buy-and-hold.

## Rules

1. **Setup**: buy several optionable, diversified ETFs in exact round lots of 100 shares each.
2. **Choosing the strike each cycle**, front-month expiration by default: **OTM call** — most bullish, smallest premium/protection, full upside to the strike (use when stock-picking-style gains are the priority); **ATM call** — maximizes time premium, moderate protection (the recommended balanced default); **ITM call** — most conservative, largest cushion, least profit potential (use when mildly bearish but still wanting to stay invested). Never write at parity (zero time value left).
3. **Uncovered puts**: choose ATM/slightly ITM if the goal is to be assigned the stock cheaply; choose further OTM, with enough premium to clear a minimum return, if the goal is income with a lower assignment chance.
4. **Minimum return floor**: do not write for less than ~0.5%/month net of commissions; a more comfortable target is ~1.5%/month.
5. **Cycle management**: if the option expires worthless, write a new one the next trading day against the same shares. If assigned, reinvest the proceeds the next trading day into the same or a different qualifying ETF and write a fresh option — stay fully invested and hedged at all times rather than sit in cash.
6. **Roll down and out** (defensive): if the market falls and the written call's remaining premium offers little further protection, buy it back and sell a new call with a lower strike and/or later expiration, only when the added protection justifies the debit paid.
7. **Roll up and out** (offensive): if the underlying rallies and the call is meaningfully ITM while a further-out, higher-strike call still has worthwhile premium, buy back and roll up, only when the extra potential gain justifies the extra capital put at risk.
8. Never repurchase a losing written option out of frustration and hold the shares unhedged hoping for a bigger rally — that is unstructured market-timing; any repurchase should be a planned roll.
9. **Cash discipline on naked puts**: before writing, hold or be able to raise cash equal to 100 × strike per contract; never rely on margin to cover the full obligation, and always compute the total cash needed if every open put is assigned before adding size.

## Risk

Maximum loss per lot is the full ETF value, offset by premium collected — capped only by the underlying going to zero, not by any stop built into the strategy. Maximum gain per cycle is the premium collected plus, for OTM writes, appreciation up to the strike; once ITM at expiration, further gains accrue to the option owner. The strategy is expected to underperform unhedged buy-and-hold in strongly, persistently rising markets — a structural cost of the added protection and higher win-rate income elsewhere, not a flaw to fix. No formal stop-loss or percent-of-equity sizing rule exists beyond round lots and full cash coverage of any naked-put obligation.

## Caveats

Assumes liquid, tight-spread options on every ETF held; thin ETF options erode the premium edge shown in the book's historical (BXM, 1988–2004) comparisons, which is not quantified here. That period was net favorable to selling slightly-OTM calls monthly and underperformed materially during 1995–1999's strong bull run — performance in other regimes will differ. Commission assumptions ($10/stock order, $10 + $1.50/contract for options) are mid-2000s deep-discount-broker figures and should be updated. This is covered calls and cash-backed uncovered puts only, not a true collar — there is no protective put purchased, so full downside below the premium cushion remains exposed.
