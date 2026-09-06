---
author: Gary Gray, Patrick J. Cusatis, J. Randall Woolridge
category: Investing, Value & Market History
difficulty: intermediate
doc_type: book
one_liner: A four-step discounted free-cash-flow-to-the-firm procedure for estimating
  a stock's intrinsic value, worked through real 2002-2003 companies.
pages: 290
related:
- investment-valuation-damodaran
- the-intelligent-investor-benjamin-graham
- r-g-hagstrom-the-warren-buffett-way-2nd-edition
- damodaran-aswath-investment-fables
- asset-valuation-allocation-models
reviewed_pdf_pages: 6, 10, 37, 41 (contents, the DCF framework, cost-of-capital inputs
  and the residual-value share of total value)
slug: streetsmart-guide-to-valuing-a-stock
source_file: Streetsmart Guide To Valuing A Stock.pdf
source_review: partial
tags:
- valuation
- dcf
- fundamental-analysis
- wacc
- free-cash-flow
- capm
- stock-picking
tier: A
title: Streetsmart Guide to Valuing a Stock
year: 2004
---

## Overview

This is a practitioner's manual for discounted-cash-flow (DCF) stock valuation, built around the free cash flow to the firm (FCFF) approach rather than the dividend discount model or relative multiples. Written by two finance academics (Cusatis and Woolridge, Penn State) and a corporate finance practitioner (Gray) in the aftermath of the dot-com crash and the Enron/WorldCom accounting scandals, the book's goal is to give an individual investor the same four-step DCF machinery professional analysts use, spreadsheet and all. It opens with 10 finance principles as a foundation, walks through every input needed to forecast free cash flow and estimate a discount rate, shows where to find that data on the (2002-era) internet, and closes with four full worked valuations — Citigroup, Merrill Lynch, Berkshire Hathaway, and Washington REIT — chosen because each stresses the standard model differently (financials, a conglomerate, a REIT).

## Core thesis

A stock's value equals the present value of the free cash flow the underlying business will generate, discounted at the company's weighted average cost of capital (WACC) — not its trailing or forward earnings per share (EPS), and not what the market currently happens to pay for it. EPS is rejected as a valuation anchor because it ignores the time value of money, ignores risk, is subject to accounting discretion (the book leans heavily on WorldCom's capitalized-expense fraud and Enron's off-balance-sheet entities as cautionary examples), and does not net out the reinvestment a company must make to keep growing. The authors are not strict efficient-market believers: they argue prices can and do diverge from intrinsic value for extended periods, and that a diversified portfolio of stocks bought below and sold above their calculated DCF value, using a percentage threshold, will outperform over time.

## Key concepts

- **Free cash flow to the firm (FCFF)** — `NOP − Taxes − Net Investment − Change in Working Capital`; the cash actually available to all capital providers after taxes and reinvestment.
- **Net operating profit (NOP) / NOPM** — Revenue − operating expenses (CGS + SG&A + R&D); NOPM = NOP / Revenue, the core profitability ratio driving the forecast.
- **NOPAT** — NOP × (1 − tax rate); the after-tax operating profit before the free-cash-flow adjustments.
- **The Five Chinese Brothers** — the authors' mnemonic for the five inputs that drive FCFF: revenue growth rate, NOPM, tax rate, working-capital investment rate, and fixed-capital investment rate.
- **Excess return period** — the years during which a company earns returns on new investment above its WACC because of a competitive advantage; after it ends, new investment earns exactly the WACC and adds no incremental value.
- **The 1-5-7-10 Rule** — the authors' framework for picking an excess return period length by competitive quality: 1 year (boring, no edge), 5 years (decent, e.g. a regulated utility), 7 years (good brand/scale, e.g. McDonald's), 10 years (great, durable moat, e.g. Microsoft/Intel/Coca-Cola).
- **Residual (terminal) value** — `NOPAT at end of excess return period / WACC`, discounted back to the present at the WACC; typically 60-90% of total corporate value.
- **WACC (weighted average cost of capital)** — the blended, tax-adjusted required return on debt, preferred stock, and common equity, weighted by their share of the capital structure; used as the single discount rate for all projected cash flows.
- **CAPM cost of equity** — `Rf + Beta × Equity Risk Premium`; the risk-free 10-year Treasury yield plus the stock's beta times the market's expected excess return.
- **Corporate (enterprise) value** — discounted cash flow from operations + discounted residual value + short-term assets.
- **Intrinsic value per share** — `(Corporate Value − Debt − Preferred Stock − Short-term Liabilities) / Diluted Shares Outstanding`.
- **Rational Analysis** (borrowed usage distinct from Bollinger's identical term) — the book's shorthand for combining DCF output with a percentage over/undervaluation threshold to trigger buy/sell decisions.

## Rules and setups

This is a valuation framework, not a trading system, so "setups" here means the repeatable four-step procedure (fully detailed as a checklist in the companion system page [[streetsmart-guide-to-valuing-a-stock--fcff-valuation-checklist]]):

1. **Forecast expected free cash flow** for the excess return period using the Five Chinese Brothers inputs (revenue growth, NOPM, tax rate, working-capital ratio, fixed-capital ratio), typically a 2-3 year historical average blended with analyst growth consensus.
2. **Estimate the WACC** from the risk-free 10-year Treasury rate, a credit spread for debt, the preferred stock yield, and CAPM-based cost of equity (beta × equity risk premium), weighted by market-value capital structure (book values for debt/preferred, market value for equity).
3. **Calculate enterprise value**: discount the excess-return-period FCFF stream and the residual value (NOPAT-at-terminal-year / WACC) back to the present at the WACC, then add short-term liquid assets (cash, securities, receivables, inventory — never goodwill or PP&E).
4. **Calculate intrinsic value per share**: subtract debt, preferred stock, and short-term liabilities from enterprise value, then divide by diluted shares outstanding.
5. **Decision rule**: buy when a stock trades more than X% (the authors use 15% as an example) below its calculated intrinsic value; sell when more than X% above; cut a losing position that falls 20% or more below purchase price regardless of the model's verdict.
6. **Excess return period selection**: apply the 1-5-7-10 Rule by competitive-advantage quality rather than defaulting to one horizon for every company.
7. **Net investment forecast**: during the excess return period, project new investment and depreciation as historic percentages of revenue; after it, set new investment equal to depreciation (maintenance capex only).

## Risk and money management

The book has no position-sizing or stop-loss framework — it is a valuation tool, not an entry/exit system — but it embeds two risk disciplines directly into the model. First, the 1-5-7-10 Rule is explicitly conservative: the authors recommend valuing a company at both its "maximum" 10-year excess return period and a shorter, more defensible period, and treating the lower number as the reasonable estimate, erring toward not overpaying. Second, the 20%-below-cost stop is offered as a blunt, valuation-independent capital-preservation rule: if the market disagrees with the model by a wide enough margin, the authors advise deferring to the market rather than the spreadsheet. They also flag that FCFF, as specified, works well for roughly 95% of listed companies but needs adjustment for highly levered financials/REITs (book uses excess marketable assets over liabilities as a substitute lens) and for firms with no current free cash flow, where an option-pricing approach is suggested but not covered.

## Psychology and discipline

The recurring psychological warning is against treating market price as truth: the authors repeatedly invoke the dot-com bubble, EntreMed's one-day quadrupling on a non-informative newspaper article, and Steve Ballmer's 1999 admission that Microsoft's own stock was overvalued, to argue that price can be driven by narrative and momentum independent of underlying cash flows for long stretches. Discipline is framed as sticking to the DCF-plus-threshold rule set — buying below intrinsic value, selling above it, cutting losses at a fixed drawdown — rather than chasing headlines, hot tips, or "continuous" market-timing behavior. The book is candid that the profession itself was captured by the accounting scandals it discusses (WorldCom, Enron, Computer Associates), which the authors present as the reason cash-flow-based valuation, not reported earnings, is the only trustworthy anchor.

## Chapter map

- Ch 1 — Introduction and Overview: the high-tech bubble, why DCF over hype.
- Ch 2 — The 10 Principles of Finance: risk/return, market efficiency, supply/demand, time value of money, diversification, and CAPM as the book's theoretical foundation.
- Ch 3 — Stock Valuation: Some Preliminaries: fundamental vs. technical vs. MPT approaches; why DCF/FCFF was chosen.
- Ch 4 — How to Value a Stock: NOP/NOPM definitions, the FCFF formula, the four-step process, a worked Microsoft example.
- Ch 5 — Forecasting Expected Cash Flow: the Five Chinese Brothers, a full Cisco worked example.
- Ch 6 — Estimating the Cost of Capital: market vs. book value weighting, CAPM, beta sourcing, worked ConEd and Cisco WACC calculations.
- Ch 7 — Finding Information for Valuations: where to source each input (SEC EDGAR, Yahoo Finance, MSN Investor, ValuePro.net); dated but conceptually relevant.
- Ch 8 — Valuing a Stock, Putting It All Together: four case studies (Citigroup, Merrill Lynch, Berkshire Hathaway, Washington REIT) as of December 2002.

## Strengths and caveats

The book's core strength is rigor and reproducibility: every formula is given explicitly, every input is traced to a specific line on a specific financial statement, and four full real-company valuations let a reader check their own spreadsheet against the authors' numbers. The 1-5-7-10 Rule is a genuinely useful, simply-stated discipline for an otherwise easy-to-abuse assumption (the terminal growth/excess-return horizon). Caveats: the book is dated on data sourcing — most named websites and the ValuePro/Quicken.com/VectorVest online tools in Chapter 7 are stale or defunct, and 2002-2003 examples (rates, prices) need updating before reuse. The FCFF approach itself needs real adjustment for financials and REITs and does not work for pre-revenue or option-like companies, a limitation the authors flag but do not solve. There is no scenario/Monte Carlo sensitivity on the terminal value despite the residual value routinely representing 60-90% of total valuation — a single point estimate for WACC and the excess return period drives most of the output, a fragility the book does not stress-test.

## Who should read it

Best suited to an intermediate investor who already reads financial statements and wants a rigorous, checklist-able alternative to P/E-based stock picking — someone willing to build a spreadsheet and pull 10-K data rather than rely on a screener's canned "fair value" number. Less useful as a first finance book (Chapter 2's principles are a fast, compressed survey rather than a teaching text) and not a trading or technical-analysis resource at all — it complements, rather than replaces, the timing-focused books in this library.

## Related books in this library

- [[investment-valuation-damodaran]] — the deeper, more rigorous academic treatment of the same DCF/FCFF machinery this book condenses into a practitioner checklist.
- [[the-intelligent-investor-benjamin-graham]] — the classical value-investing foundation (margin of safety, Mr. Market) that motivates the buy-below/sell-above intrinsic-value rule used here.
- [[r-g-hagstrom-the-warren-buffett-way-2nd-edition]] — a complementary qualitative lens (moat, management quality) for judging which "excess return period" bucket (1-5-7-10) a company belongs in.
- [[damodaran-aswath-investment-fables]] — a useful counterweight that stress-tests common valuation shortcuts and misconceptions this book's checklist approach can encourage.
- [[asset-valuation-allocation-models]] — another cost-of-capital and valuation-modeling resource for cross-checking WACC and CAPM assumptions.
