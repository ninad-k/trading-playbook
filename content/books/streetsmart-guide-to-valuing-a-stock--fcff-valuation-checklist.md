---
title: "The FCFF Valuation Checklist"
author: "Gary Gray, Patrick J. Cusatis, J. Randall Woolridge"
year: 2004
slug: streetsmart-guide-to-valuing-a-stock--fcff-valuation-checklist
tier: A
category: "Investing, Value & Market History"
tags: [valuation, dcf, wacc, free-cash-flow, capm, checklist]
difficulty: intermediate
doc_type: system
parent: streetsmart-guide-to-valuing-a-stock
pages: 290
one_liner: "Step-by-step discounted free-cash-flow-to-the-firm procedure for computing a stock's per-share intrinsic value."
related: [streetsmart-guide-to-valuing-a-stock, investment-valuation-damodaran]
source_file: "Streetsmart Guide To Valuing A Stock.pdf"
---

## What it is

A four-step, fully specified procedure for computing a stock's intrinsic value from its financial statements, using free cash flow to the firm (FCFF) discounted at the weighted average cost of capital (WACC). It is not a trading signal — it produces a single per-share number to compare against the current market price, on a schedule (the authors suggest periodic re-valuation as fundamentals change), to decide whether a stock is a buy, a hold, or a sell candidate.

## Rules

**Step 1 — Forecast free cash flow for the excess return period.**
Pull three years of income statement, balance sheet, and cash flow statement data. Compute the five drivers ("Five Chinese Brothers"):
- Revenue growth rate — analyst consensus or historical average.
- Net operating profit margin (NOPM) = Operating Income / Revenue = `(Revenue − CGS − SG&A − R&D) / Revenue`. Use the most recent year if the trend is stable/directional; use a 3-year average if erratic.
- Tax rate = Income Tax Provision / Pretax Income (3-year average if volatile).
- Net investment rate = (Capital Expenditures − Depreciation) / Revenue, historical average during the excess return period; after it, set new investment = depreciation (maintenance only).
- Incremental working capital rate = Δ(Accounts Receivable + Inventories − Accounts Payable) / Δ Revenue.

Choose the excess return period length by the 1-5-7-10 Rule: 1 year for a company with no competitive edge in a commodity industry; 5 years for a decent, moderately protected business (e.g., a regulated utility); 7 years for a strong brand/scale business; 10 years (the cap — never go longer) for a business with a durable, wide moat. Project NOP = Revenue × NOPM for each year of the excess return period, then NOPAT = NOP × (1 − Tax Rate), then FCFF = NOPAT + Depreciation − Net Investment − Δ Working Capital for each year.

**Step 2 — Estimate the WACC.**
- Cost of debt (after-tax) = Pretax Cost of Debt × (1 − Tax Rate); pretax cost = current 10-year Treasury yield + the company's credit spread.
- Cost of preferred stock = stated/market preferred dividend yield.
- Cost of common equity (CAPM) = Risk-Free Rate (10-year Treasury) + Beta × Equity Risk Premium (Rm − Rf; use an estimate such as 3%). Source beta from at least two providers (e.g., Yahoo Finance, a data vendor) and use the higher of the two, or average them, for conservatism.
- Determine capital structure weights: use book values for debt and preferred stock (market quotes are hard to obtain reliably) and market value (share price × diluted shares outstanding) for common equity.
- WACC = %Debt × After-tax Cost of Debt + %Preferred × Cost of Preferred + %Equity × Cost of Equity.

**Step 3 — Calculate enterprise (corporate) value.**
- Discount each year's projected FCFF back to the present at the WACC and sum — this is the discounted cash flow from operations.
- Compute residual (terminal) value = NOPAT in the final excess-return year / WACC (a cash-flow perpetuity, since post-period returns on new investment equal the WACC exactly and add no NPV), then discount that lump sum back to the present at the WACC.
- Add current short-term assets from the balance sheet — cash, marketable securities, accounts receivable, inventories — but never intangibles (goodwill) or long-term operating assets (property, plant & equipment), which are already embedded in the operating cash flow forecast.
- Enterprise Value = Discounted Cash Flow from Operations + Discounted Residual Value + Short-term Assets.

**Step 4 — Back into per-share intrinsic value.**
- Value to Common Equity = Enterprise Value − Book Value of Debt − Book Value of Preferred Stock − Short-term Liabilities.
- Intrinsic Value per Share = Value to Common Equity / Diluted Shares Outstanding.

**Step 5 — Apply the decision rule.**
Set a threshold percentage (the authors use 15% as an illustration). Buy when market price is more than that percentage below intrinsic value; sell/avoid when more than that percentage above. Re-run the model when fundamentals materially change, and independent of the model's output, exit any position that falls 20% or more below its purchase price.

## Risk

The model has two structurally sensitive points that function as its real risk exposure: the terminal (residual) value routinely accounts for 60-90% of total enterprise value, so small changes in the assumed WACC or the length of the excess return period swing the output disproportionately — always compute a "conservative" case using a shorter excess return period alongside the "maximum" 10-year case rather than reporting a single number. There is no stated stop-loss inside the model itself; the fixed 20%-below-cost rule from the parent book is the only capital-preservation mechanism, applied independent of what the DCF says. The approach also silently assumes a roughly stable capital structure and management that reinvests only in projects earning above the WACC — both worth sanity-checking against the company's actual capital allocation history before trusting the output.

## Caveats

The FCFF framework as specified is stated by the authors to work reasonably for about 95% of publicly traded companies but requires real modification for highly levered financials and REITs (where balance-sheet excess-asset analysis substitutes for the standard operating-cash-flow build) and breaks down for companies with no current free cash flow or highly speculative, option-like payoffs (early-stage biotech, for example), where the book explicitly defers to option-pricing methods it does not itself cover. Betas, risk-free rates, and equity risk premiums are all point-in-time market inputs that must be refreshed at valuation time — the book's own worked examples use 2002 Treasury yields and betas that are now purely illustrative of the method, not usable inputs. No sensitivity or scenario analysis is built into the procedure; a practitioner should run the checklist multiple times across a plausible range of WACC and growth assumptions rather than trusting a single point estimate.
