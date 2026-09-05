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

A step-by-step method for answering "how much capital do I need to trade this market/system?" by combining three risk measures — Optimal f, the largest historical overnight gap, and maximum drawdown — into a suggested capital figure per contract, then rolling per-market figures into a whole-portfolio account size via two methods ("aggressive" and "conservative") that are averaged. It answers only the sizing question and applies to any entry/exit approach the trader has already chosen.

## Rules

**Step 1 — single-market capital (per contract):**
- **Optimal f** (Ralph Vince): from ≥30 trades, compute `PR = -(P/L) / largest losing trade` per trade, `HPR = 1 + f×PR`, and find the f (0.01–1.00) that maximizes the product of all HPRs; suggested capital = largest losing trade ÷ f (e.g., loss $2,000, f=0.40 → $5,000). Without a backtest, substitute `margin × 3`.
- **Largest overnight gap ($)**: biggest historical open-vs-prior-close jump (Crude Oil gapped $7,500/contract in the 1991 Gulf War air raid); limit-move markets can still lock against you, non-limit markets have no bound.
- **Maximum drawdown ($)**: worst peak-to-trough equity decline in testing; prefer out-of-sample data, since over-optimized results understate future drawdowns.
- **Combine (Optimal f available)**: `(Optimal f $ + Largest Gap $ + (Max Drawdown $ + Margin)) / 3`. Yen example: (3,457 + 5,938 + (4,124+3,000)) / 3 = **$5,506**.
- **Combine (no Optimal f)**: `((Margin × 3) + Largest Gap $) / 2`. Yen example: ((3,000×3) + 5,938) / 2 = **$7,469**.

**Step 2 — portfolio sizing:**
- **"Aggressive"**: sum per-contract capital across markets. Example (Yen $5,506 + T-Bonds $5,982 + Soybeans $5,076 + Nat Gas $4,241) = **$20,805**.
- **"Conservative"** (needs ≥30 months of P/L data): (σ of monthly returns × 3) / 0.1, targeting a 99% chance of not exceeding a 10% monthly drawdown. Example: σ=$1,500 → $45,000.
- **"Optimum"**: average the two. Example: (20,805+45,000)/2 = **$32,903**.

**Step 3 — optional sanity checks** (same ≥30-month data set): Expected Annual % Return (monthly % compounded ×12); Expected Max Drawdown $ (σ×4) and %; P/L-to-σ Ratio (>0.5 outstanding); Profit/Drawdown Ratio (Annual %/Drawdown %, ≥1 minimum, >1.5 outstanding); % of profitable rolling 3- and 12-month periods, as a gauge of how easy the approach is to stick with.

## Risk

The method is a pre-trade sizing exercise, not an in-trade control — its output sets a ceiling on leverage, but stop-losses and position management still have to be layered on separately (see Mistake #3 in the parent book). The margin-to-equity ratio (open margin ÷ equity) is offered as an ongoing check that trading hasn't drifted past the implied sizing; Kaeppel's rule of thumb caps it below roughly 30% for non-aggressive trading. The method assumes future results resemble past results — every input is backward-looking, and the book notes "previous records are made to be broken," so outputs should be treated as a floor, not a guarantee.

## Caveats

Optimal f by itself is explicitly flagged as dangerous for single-market use because its calculation only considers the single largest losing trade and ignores drawdown entirely, which is precisely why it is blended with the drawdown and overnight-gap terms rather than used alone. The conservative-sizing and sanity-check steps require at least 30 months of real or hypothetical monthly data; smaller samples aren't statistically meaningful by the book's own standard-deviation logic. All dollar inputs (margins, historical gaps) are specific to the markets and year (2000) the book was written in and must be refreshed with current data before use — the formulas themselves, not the numbers, are the durable part.
