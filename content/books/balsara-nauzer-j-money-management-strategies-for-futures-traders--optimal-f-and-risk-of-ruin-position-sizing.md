---
title: Optimal f, Fixed-Fractional Sizing, and Risk-of-Ruin Allocation
author: Nauzer J. Balsara
year: 1992
slug: balsara-nauzer-j-money-management-strategies-for-futures-traders--optimal-f-and-risk-of-ruin-position-sizing
tier: A
category: Money Management & Position Sizing
tags: [optimal-f, kelly-criterion, fixed-fractional, risk-of-ruin, position-sizing, pyramiding]
difficulty: advanced
doc_type: system
parent: balsara-nauzer-j-money-management-strategies-for-futures-traders
pages: 137
one_liner: "The formula set for sizing futures positions: fixed-fractional and Kelly/optimal-f exposure, risk-of-ruin control, multi-commodity allocation, and pyramiding of open profits."
related: [a-new-interprtation-of-information-rate-kelly, position-sizing, forex-misc-money-management-ryan-jones]
source_file: "BALSARA, Nauzer J. - Money Management Strategies for Futures Traders.pdf"
---

## What it is

A formula-driven procedure for deciding what fraction of capital to risk per trade and per portfolio, independent of the signal-generation method. It answers, in sequence: what fraction to expose per trade (maximizing long-run growth without unacceptable ruin risk), how many contracts that implies given margin/stop constraints, how to scale across several commodities at once, and how to pyramid a winner's own locked-in profit.

## Rules

**1. Choose an exposure fraction, f.**
- Probability-only (payoff ratio A=1): f = p − (1 − p), p = win rate. Trade only if p > 0.51.
- Kelly/optimal-f with payoff ratio A (avg $ win ÷ avg $ loss): f = [(A+1)p − 1] / A. Example: p=0.33, A=5 → f=0.20.
- Trade-specific optimal f: A = expected win ÷ permissible loss; expected value = (p×A) − (1−p); f = expected value ÷ A. Example: risking 8¢ to make 20¢, p=0.45 → A=2.50, expected value=0.575, f≈0.23.
- Historic-returns (Vince/TWR): divide each trade's return by the (negated) worst loss to get r_i; for a candidate f, HPR_i = 1 + f×(−r_i); TWR(f) = product of all HPR_i. Test f from 0.01–1.00 and pick the f maximizing TWR — that's the empirically optimal fraction.

**2. Convert f to contracts.**
Risk capital = f × bankroll (or a lower user cap). Risk-based contracts = risk capital ÷ dollar risk per contract; margin-based contracts = capital allocated ÷ initial margin per contract. Trade the smaller of the two; round fractions down. If under one contract, skip the trade or replicate the delta with options (ATM ≈ 0.50 futures-equivalent; two 0.25-delta OTM options ≈ same).

**3. Scale across multiple commodities.**
Don't simply sum individual f's — ignores correlation and can exceed 100%. Avoid concurrent full-size positions in positively correlated commodities; negative correlations may be conservatively ignored. For a precise aggregate F: compute each round's geometric joint return across commodities, then run the same TWR-maximization as step 1 on those joint returns. Allocate per commodity equally (F × bankroll ÷ number of concurrent commodities), by mean-variance (Markowitz) optimization, or by each commodity's own f scaled to sum to F. A user cap on any single commodity always overrides the formula. If a commodity's (permissible risk ÷ margin) ratio exceeds F, risk governs contract count; if lower, margin governs.

**4. Control risk of ruin directly.**
Estimate p and A from a track record; look up or simulate risk of ruin R at the planned exposure (closed-form: R=(q/p)^k for A=1; R=[(0.25+1/(2A))(1/p−0.5)]^k for A=2; other ratios need simulation — tables cover A=1–10 at exposure levels 100/50/33/25/20/10%). If R is unacceptable, reduce exposure (increase capital units k=1/exposure) and recheck. Hard floor: at A=2, R=1 (certain ruin) once p ≤ 0.33, regardless of size.

**5. Pyramid only realized profit on winners.**
Effective exposure = |entry − stop| × contracts while the stop hasn't passed breakeven. Once past breakeven, assured unrealized profit = (stop − entry) × contracts (long) or (entry − stop) × contracts (short). Choose p (0–1), the fraction of that locked-in gain to risk again: additional contracts = (p × assured profit × current contracts) ÷ permissible loss per new contract. Never use pyramiding to average down a loser.

## Risk

Cutting exposure from 50% to 20% of capital (p=0.60, A=2) cuts risk of ruin from 0.209 to 0.020. Percentage gain needed to recover a percentage loss L = 1/(1−L) − 1: a 50% loss needs +100% to recover, a 90% loss needs +900% — the reason oversized single-trade losses matter more than raw edge. Optimal f, uncapped, can recommend aggressive exposure (20%+ in the worked examples) that maximizes growth but produces large drawdowns; always run the risk-of-ruin check (step 4) alongside any optimal-f result rather than trusting f alone.

## Caveats

All formulas assume p and A are stable and will hold for the next trade; in practice these measures drift as market conditions change, undermining precision. Closed-form risk-of-ruin only exists for A=1 or A=2; other ratios require simulation and table interpolation is approximate. Mean-variance multi-commodity allocation assumes a stable opportunity set and correlations, better suited to a longer-horizon position trader than a short-term futures trader with a daily-changing tradable universe. Dollar and margin examples are 1980s-era; the mechanics transfer to any market but inputs must be updated.
