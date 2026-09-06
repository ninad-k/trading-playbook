# Investment Valuation: the trader's summary

*Graduate-level valuation textbook covering DCF models (dividend, FCFE, FCFF), relative valuation multiples, and growth/terminal-value estimation, with worked company examples.*

**Aswath Damodaran** · 2002 · Investing, Value & Market History · advanced

*Source coverage: partial. PDF pages inspected: 45, 85, 384, 452 (the model-choice chapters and the worked Con Ed dividend/FCFE comparison; the note's formulas were checked against these sections). These are study notes, not verified trading results.*

## Overview

This is Damodaran's comprehensive graduate-level valuation textbook (2nd edition), covering discounted cash flow (DCF) valuation, relative valuation (multiples), and contingent-claim (real-option) valuation across equity, private firms, financial-service firms, distressed firms, real estate, and derivatives. It is not a trading book; it is a reference for estimating what a business is intrinsically worth, and for understanding why market multiples diverge from that value. Every model is illustrated with a real-company example (Con Ed, Boeing, Procter & Gamble, Amgen, Motorola, Home Depot, Cisco, and others), and Damodaran stresses throughout that valuation is not objective — analyst bias, growth assumptions, and choice of comparables drive most of the dispersion in value estimates.

## Core thesis

The value of any asset equals the present value of its expected future cash flows, discounted at a rate reflecting the riskiness of those cash flows — the unifying idea behind every model in the book, whether applied to a dividend stream, a company's free cash flow, a bond, a private business, or an option to expand a project. Relative valuation (multiples) is a shortcut version of the same DCF logic: every multiple (P/E, P/B, EV/EBITDA, P/S) can be derived algebraically from a stable-growth DCF model, so a multiple is only "cheap" or "expensive" relative to peers after controlling for the same growth, risk, and payout differences a full DCF would make explicit. The second major theme is that terminal value dominates most valuations arithmetically, so its assumptions — stable growth rate, length of the high-growth period, and perpetual return on capital — deserve more scrutiny than the explicit-period forecasts usually receive.

## Key concepts

- **Free Cash Flow to Equity (FCFE)** — cash left for stockholders after reinvestment and net debt flows: Net Income − (CapEx − Depreciation) − ΔWorking Capital + (New Debt − Debt Repaid); a more complete measure of "affordable" dividends than the dividend itself.
- **Free Cash Flow to Firm (FCFF)** — cash available to all capital providers: EBIT(1−tax rate) + Depreciation − CapEx − ΔWorking Capital; discounted at the cost of capital to get firm (enterprise) value.
- **Cost of capital (WACC)** — ke × E/(D+E) + kd(1−t) × D/(D+E); the blended discount rate used for FCFF valuation.
- **Fundamental growth rate** — g = Retention Ratio × ROE (equity income) or Reinvestment Rate × Return on Capital (operating income); growth is manufactured by reinvesting above the cost of capital, not an exogenous input.
- **Competitive Advantage Period (CAP)** — years a firm can sustain returns on capital above its cost of capital before competition erodes the excess return to zero; the central judgment call behind any high-growth forecast, and can be solved backward from price (Market Implied CAP) as a sanity check.
- **Gordon Growth / terminal value** — Value = Cash Flow(n+1) / (discount rate − stable growth rate); dominates total value for most companies and blows up as growth approaches the discount rate, so stable growth is capped at the economy's long-run growth rate.
- **Two-stage / three-stage models** — an explicit high-growth phase followed by a stable phase, with payout ratio, beta, and ROE reset toward "mature firm" levels in the terminal stage.
- **PE, PBV, PS ratios (fundamentally derived)** — each multiple is a function of payout ratio, ROE (PBV) or profit margin (PS), growth, and risk; e.g., PE = Payout×(1+g)/(ke−g) for a stable-growth firm. The PEG ratio (PE ÷ growth rate) implicitly, and often wrongly, assumes this relationship is linear.
- **Definitional/uniformity tests** — a multiple's numerator and denominator must both be equity-based (P/E) or both firm-based (EV/EBITDA); mixing equity price with firm-level earnings produces a distorted, debt-blind comparison.
- **Liquidation value** — an alternative to going-concern terminal value: book value adjusted for inflation, or the discounted earning power of the remaining assets.

## Rules and setups

This is a valuation reference, not an entry/exit trading system; there are no price triggers, stops, or holding periods. Its "rules" are the numeric conventions and decision criteria used to build an intrinsic-value estimate.

1. **Model choice by cash-flow policy:** use the Dividend Discount Model only if dividends closely track FCFE (Con Ed's dividends were 91.5% of average FCFE, 1996–2000); use FCFE directly when a firm pays out persistently less or more than it can afford; use FCFF/WACC when leverage is changing or the whole firm is being valued.
2. **Stable growth rate ceiling:** terminal growth cannot exceed the long-run nominal growth rate of the economy the firm operates in, and as a rule of thumb should not exceed the risk-free rate used in the discount rate.
3. **Stable-period resets:** beta converges toward 1 (cap ~1.2), ROE/ROC converges toward industry averages, and the reinvestment/retention ratio equals Stable growth ÷ Stable-period ROE (or ROC).
4. **Historical growth estimation:** use geometric, not arithmetic, average growth for volatile series; for negative-earnings years use the absolute value of the prior-period denominator, and treat growth as "not meaningful" rather than force a distorted number.
5. **Implied growth check:** solve the DDM/FCFE formula backward from market price for the growth rate it requires, and compare against an independent fundamentals-based estimate as a bias check.
6. **Multiple comparability tests:** confirm definitional consistency (same PE variant), numerator/denominator consistency (equity-to-equity or firm-to-firm), and use the median, not the mean, when negative-earnings firms drop out and bias the average upward.
7. **Length of high-growth period:** judged from firm size relative to its addressable market, growth momentum, and durability of competitive barriers — examples use 0 years (Con Ed, stable), 5 years (P&G), and 10 years (Amgen, patent-protected).

## Risk and money management

The book has no position-sizing chapter; "risk" is embedded entirely in the discount rate — riskier cash flows are discounted more heavily via a higher cost of equity (riskless rate, equity risk premium, beta) or cost of debt (default spread). Since terminal value dominates total value, the practical implication is to stress-test valuations across a range of terminal growth rates and CAP lengths rather than trust one point estimate — the book's own sensitivity tables (Con Ed's value swinging from roughly $25 to over $60 as growth assumptions shift a few points) show how fragile a single DCF output can be. Cross-checking against relative valuation and the market-implied growth rate substitutes for a stop-loss.

## Psychology and discipline

Damodaran opens by debunking the idea that valuation is objective: models require subjective inputs, and analyst bias (pressure to issue buy over sell recommendations, self-serving takeover valuations, setting a price target first and reverse-engineering the model) is a bigger source of error than any modeling choice. His prescribed discipline: avoid a public position on over/under-valuation before finishing the analysis, minimize personal stake in the outcome, and treat every valuation as perishable — it ages with new information and must be updated, not treated as a fixed verdict.

## Chapter map

- Ch 1-3 — Introduction to Valuation; Approaches to Valuation; Understanding Financial Statements: philosophical basis, the three valuation approaches, and accounting inputs.
- Ch 4-8 — Risk; Option Pricing; Market Efficiency; Riskless Rates and Risk Premiums; Estimating Risk Parameters: building the discount rate and real-option mechanics.
- Ch 9-12 — Measuring Earnings; From Earnings to Cash Flows; Estimating Growth; Terminal Value: the most value-sensitive inputs in the book.
- Ch 13-16 — Dividend Discount, FCFE, and Firm Valuation (Cost of Capital/APV) Models; Equity Value Per Share: the core DCF toolkit.
- Ch 17-20 — Relative Valuation Principles; Earnings, Book Value, and Revenue/Sector Multiples: the multiples toolkit and its DCF-derived logic.
- Ch 21-24 — Financial Service Firms; Negative Earnings; Young/Start-up Firms; Private Firms: special-case adaptations.
- Ch 25-27 — Acquisitions and Takeovers; Real Estate; Other Assets: applications beyond public equity.
- Ch 28-30 — Options to Delay, Expand, Abandon; Distressed Equity: real-options extensions, including equity as a call option on a levered firm.
- Ch 31-32 — Value Enhancement (DCF Framework; EVA/CFROI): linking valuation to corporate strategy.
- Ch 33-35 — Valuing Bonds; Futures and Forwards; Overview and Conclusion: fixed-income/derivatives valuation and model-selection guidance.

## Strengths and caveats

The worked examples use late-1990s/2000-2001 companies, interest rates, and risk premiums (5.4% riskless rate, 4% equity risk premium), so absolute numbers need updating — the formulas and logic transfer, not the plugged-in figures. The book assumes fairly sophisticated familiarity with financial statements and algebra; it is not introductory despite covering fundamentals. Because it treats relative valuation as a derivative of DCF logic, it is more skeptical of pure multiple-based investing than practitioner books like [The Intelligent Investor](https://ninad-k.github.io/trading-playbook/books/the-intelligent-investor-benjamin-graham.html); the trade-off is far greater rigor at the cost of more inputs and judgment calls, particularly around growth duration and terminal value, which the book admits dominate the answer and are hardest to pin down.

## Who should read it

Equity analysts, buy-side investors, and serious retail investors who want defensible intrinsic-value estimates rather than screens or multiples alone; readers comfortable with algebra and financial statements; anyone who wants to understand why two "value" investors reach different conclusions on the same stock (usually a growth-rate or terminal-value disagreement, not a data disagreement). Traders wanting entry/exit signals should look elsewhere — this informs the "is it cheap" question over years, not the "when to buy" question.

## Related books in this library

- [Investment Fables: Exposing Myths About Stocks](https://ninad-k.github.io/trading-playbook/books/damodaran-aswath-investment-fables.html) — same author, applies this toolkit to debunk specific market myths and valuation shortcuts.
- [The Intelligent Investor](https://ninad-k.github.io/trading-playbook/books/the-intelligent-investor-benjamin-graham.html) — a simpler, screen-based framework this book's relative-valuation chapters formalize algebraically.
- [The Warren Buffett Way](https://ninad-k.github.io/trading-playbook/books/r-g-hagstrom-the-warren-buffett-way-2nd-edition.html) — a qualitative, moat-focused companion to this book's quantitative DCF machinery.
- [Pick Stocks Like Warren Buffett](https://ninad-k.github.io/trading-playbook/books/j-k-lasser-pick-stocks-like-warren-buffett.html) — a more accessible, checklist-driven route to the same fundamental-value question.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: valuation, dcf, relative-valuation, cost-of-capital, terminal-value, growth-rate, cash-flow
