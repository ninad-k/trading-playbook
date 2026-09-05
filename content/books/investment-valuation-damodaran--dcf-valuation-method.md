---
title: "DCF Valuation Method (FCFE / FCFF)"
author: Aswath Damodaran
year: 2002
slug: investment-valuation-damodaran--dcf-valuation-method
tier: A
category: Investing, Value & Market History
tags: [valuation, dcf, fcfe, fcff, terminal-value, cost-of-capital]
difficulty: advanced
doc_type: system
parent: investment-valuation-damodaran
pages: 1356
one_liner: "Step-by-step discounted cash flow method: forecast cash flows and growth in explicit stages, discount at a risk-adjusted rate, and close with a bounded terminal value."
related: [investment-valuation-damodaran, damodaran-aswath-investment-fables, the-intelligent-investor-benjamin-graham]
source_file: "Investment Valuation - Damodaran.pdf"
---

## What it is

A general-purpose intrinsic-value method: value a firm (or its equity) as the present value of expected future cash flows plus a terminal value, discounted at a rate reflecting risk. Two parallel tracks: Free Cash Flow to Equity (FCFE), discounted at the cost of equity for equity value directly, and Free Cash Flow to Firm (FCFF), discounted at WACC for firm value, from which debt is subtracted to reach equity value. Both share the same growth/terminal-value machinery; FCFF/WACC is more robust when leverage is changing.

## Rules

1. **Classify the growth stage** — stable, two-stage (n years high growth then stable), or three-stage (with a declining-growth transition). Judge high-growth length from firm size relative to its market, growth momentum, and durability of competitive advantages.

2. **Compute the cash flow.**
   - FCFE = Net Income − (CapEx − Depreciation) − ΔWorking Capital + (New Debt − Debt Repaid) − Preferred Dividends.
   - FCFF = EBIT×(1−tax rate) + Depreciation − CapEx − ΔWorking Capital.

3. **Forecast growth from fundamentals**, not analyst guesses: g = Retention Ratio × ROE (equity income) or Reinvestment Rate × Return on Capital (operating income). For historical growth use the geometric, not arithmetic, average, and treat negative-earnings periods as "not meaningful" rather than forcing a distorted number.

4. **Build the discount rate.** Cost of equity = riskless rate + beta × equity risk premium (CAPM). WACC = ke×E/(D+E) + kd(1−tax)×D/(D+E), with kd from the riskless rate plus a rating-based default spread. Re-lever beta as the debt ratio changes across stages.

5. **Discount explicit-period cash flows** year by year at ke (FCFE) or WACC (FCFF).

6. **Estimate terminal value** at stable growth: TV(n) = CF(n+1) / (r − g_stable). Cap g_stable at the economy's long-run growth rate (rule of thumb: at or below the risk-free rate). Reset stable-period beta toward 1 (cap ~1.2), ROE/ROC toward industry averages, and the reinvestment ratio to g_stable ÷ Stable ROE (or ROC). Alternatives: liquidation value or an exit multiple (the latter effectively blends in relative valuation).

7. **Sum and adjust.** Value = Σ PV(cash flows) + PV(terminal value); for FCFF subtract debt and minority interests before dividing by shares outstanding.

8. **Cross-check with the implied growth rate** — solve backward from market price for the growth rate it requires, and compare to the fundamentals-based estimate.

## Risk

No stop-loss or position-sizing rule; risk is priced through the discount rate and the margin between estimated value and market price. Because terminal value dominates total value, the model is highly sensitive to the stable growth rate and high-growth length — value moves non-linearly as growth approaches the discount rate. Practical control: run the valuation across a range of growth/discount-rate assumptions rather than trusting one point estimate, and sanity-check the implied growth rate.

## Caveats

Every input (growth duration, stable ROE, beta convergence) is a judgment call dressed in algebra; two analysts can reach very different values from the same model. It requires clean, forward-looking financial data (R&D capitalization, operating leases, one-time items) that is easy to get wrong mechanically. It is a multi-year intrinsic-value estimate, not a timing tool — it says whether a stock is cheap, not when the market will agree.
