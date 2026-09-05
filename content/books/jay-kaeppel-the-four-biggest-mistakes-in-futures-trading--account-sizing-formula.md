---
title: The Blended Account-Sizing Formula
author: Jay Kaeppel
year: 2000
slug: jay-kaeppel-the-four-biggest-mistakes-in-futures-trading--account-sizing-formula
tier: A
category: Money Management & Position Sizing
tags: [futures, position-sizing, optimal-f, drawdown, leverage]
difficulty: intermediate
doc_type: system
parent: jay-kaeppel-the-four-biggest-mistakes-in-futures-trading
pages: 123
one_liner: "A worked, three-input formula for how much capital to allocate per futures contract, then blended into an 'optimum' whole-portfolio account size."
related: []
source_file: "Jay Kaeppel - The Four Biggest Mistakes In Futures Trading.pdf"
---

## What it is

A step-by-step method for answering "how much capital do I need to trade this market/system?" by combining three independent risk measures — Optimal f, the largest historical overnight gap, and maximum drawdown — into a single suggested capital figure per contract, then rolling per-market figures up into a whole-portfolio account size using two complementary methods ("aggressive" and "conservative") and averaging them. It is not an entry/exit system; it answers only the sizing question, and is meant to be applied to whatever trading approach (mechanical or discretionary) the trader has already chosen.

## Rules

**Step 1 — Single-market capital, three factors:**
- **Optimal f** (Ralph Vince, *Portfolio Management Formulas*, 1990): using a trade listing of at least 30 trades, compute for each trade `PR = -(profit or loss) / largest losing trade`, then `HPR = 1 + f × PR` for a trial value of f between .01 and 1.00; the f that maximizes the product of all HPRs (the Terminal Wealth Relative) is the optimal f; suggested capital = largest losing trade ÷ f. (Example: largest loss $2,000, optimal f = 0.40 → suggested capital $5,000.) If you cannot backtest a system, substitute `margin requirement × 3`.
- **Largest overnight gap in dollars**: the biggest historical open-vs-prior-close jump for that market (e.g., Crude Oil gapped $7,500/contract overnight during the 1991 Gulf War air raid); acknowledges that limit-move markets can still be "locked" against you and non-limit markets have no bound at all.
- **Maximum drawdown in dollars**: worst peak-to-trough equity decline produced by the system on that market in testing; use out-of-sample data where possible, since over-optimized in-sample results understate real future drawdowns.
- **Combine (if Optimal f is available)**: `(Optimal f in $ + Largest Overnight Gap in $ + (Maximum Drawdown in $ + Margin Requirement)) / 3`. Worked example (Japanese Yen): Optimal f $3,457, gap $5,938, drawdown $4,124, margin $3,000 → (3,457 + 5,938 + (4,124+3,000)) / 3 = **$5,506** suggested capital for one contract.
- **Combine (if Optimal f is unavailable)**: `((Initial Margin × 3) + Largest Overnight Gap in $) / 2`. Worked example (same Yen contract, margin $3,000, gap $5,938): ((3,000×3) + 5,938) / 2 = **$7,469**.

**Step 2 — Portfolio-level sizing, two methods:**
- **"Aggressive" account size**: sum the per-contract suggested capital for every market in the portfolio (one contract each). Worked 4-market example (Yen $5,506 + T-Bonds $5,982 + Soybeans $5,076 + Natural Gas $4,241) = **$20,805** minimum.
- **"Conservative" account size**: requires ≥30 months of portfolio monthly P/L data. Compute the standard deviation of monthly returns; multiply by 3 (≈99% of monthly outcomes fall within ±3σ); divide by 0.1 to target a 99% probability of not exceeding a 10% monthly drawdown. Worked example: monthly-return σ = $1,500 → ($1,500 × 3) / 0.1 = **$45,000**.
- **"Optimum" account size**: average the aggressive and conservative figures. Worked example: (20,805 + 45,000) / 2 = **$32,903**.

**Step 3 — Sanity-check the resulting portfolio (optional, needs the same ≥30-month data set):**
- Expected Annual % Return = average monthly % return compounded over 12 months.
- Expected Maximum Drawdown in $ = monthly-return σ × 4.
- Expected Maximum Drawdown % = (that $ figure) / account equity.
- P/L-to-Standard-Deviation Ratio = average monthly % return / σ of monthly returns; > 0.5 is "outstanding."
- Expected Profit/Drawdown Ratio = Expected Annual % Return / Expected Maximum Drawdown %; minimum acceptable ≈ 1-to-1, > 1.5 is "outstanding."
- % of profitable rolling 3-month and 12-month periods, as a psychological gauge of how easy the approach will be to stick with.

## Risk

The entire method is a pre-trade sizing exercise rather than an in-trade risk control — its output (a dollar figure per contract and per portfolio) sets the ceiling on how much leverage is being taken on, but stop-losses and position management still have to be layered on top separately (see Mistake #3 in the parent book). The margin-to-equity ratio (total open margin ÷ account equity) is offered as a fast ongoing check that trading hasn't drifted past the sizing the formula implied; Kaeppel's rule of thumb caps this below roughly 30% for non-aggressive trading. The method explicitly assumes future results resemble past results — every dollar figure it produces (Optimal f capital, historical gap, historical drawdown) is a backward-looking estimate, and the book states plainly that "previous records are made to be broken," so all outputs should be treated as a floor, not a guarantee.

## Caveats

Optimal f by itself is explicitly flagged as dangerous for single-market use because its calculation only considers the single largest losing trade and ignores drawdown entirely, which is precisely why it is blended with the drawdown and overnight-gap terms rather than used alone. The conservative-sizing and sanity-check steps require at least 30 months of real or hypothetical monthly data; smaller samples aren't statistically meaningful by the book's own standard-deviation logic. All dollar inputs (margins, historical gaps) are specific to the markets and year (2000) the book was written in and must be refreshed with current data before use — the formulas themselves, not the numbers, are the durable part.
