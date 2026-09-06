---
author: Nauzer J. Balsara
category: Money Management & Position Sizing
difficulty: advanced
doc_type: system
one_liner: 'The formula set for sizing futures positions: fixed-fractional and Kelly/optimal-f
  exposure, risk-of-ruin control, multi-commodity allocation, and pyramiding of open
  profits.'
pages: 137
parent: balsara-nauzer-j-money-management-strategies-for-futures-traders
related:
- kellybetting
- position-sizing
- forex-misc-money-management-ryan-jones
slug: balsara-nauzer-j-money-management-strategies-for-futures-traders--optimal-f-and-risk-of-ruin-position-sizing
source_file: BALSARA, Nauzer J. - Money Management Strategies for Futures Traders.pdf
tags:
- optimal-f
- kelly-criterion
- fixed-fractional
- risk-of-ruin
- position-sizing
- pyramiding
tier: A
title: Optimal f, Fixed-Fractional Sizing, and Risk-of-Ruin Allocation
year: 1992
---

## What it is

A formula-driven procedure for deciding what fraction of capital to risk per trade and per portfolio, independent of the signal method. It answers, in sequence: what fraction to expose per trade, how many contracts that implies given margin/stop constraints, how to scale across several commodities, and how to pyramid a winner's own locked-in profit.

## Rules

**1. Choose an exposure fraction, f.**
- Probability-only (payoff ratio A=1): f = p − (1 − p), p = win rate. Trade only if p > 0.51.
- Kelly/optimal-f with payoff ratio A (avg $ win ÷ avg $ loss): f = [(A+1)p − 1] / A. Example: p=0.33, A=5 → f=0.20.
- Trade-specific: A = expected win ÷ permissible loss; expected value = (p×A) − (1−p); f = expected value ÷ A. Example: risking 8¢ to make 20¢, p=0.45 → A=2.50, expected value=0.575, f≈0.23.
- Historic-returns (Vince/TWR): divide each trade's return by the (negated) worst loss to get r_i; for candidate f, HPR_i = 1 + f×(−r_i); TWR(f) = product of all HPR_i. Test f from 0.01–1.00; the f maximizing TWR is the empirically optimal fraction.

**2. Convert f to contracts.**
Risk capital = f × bankroll (or a lower user cap). Risk-based contracts = risk capital ÷ dollar risk per contract; margin-based contracts = capital allocated ÷ initial margin per contract. Trade the smaller; round down. If under one contract, skip the trade or replicate the delta with options (ATM ≈ 0.50 futures-equivalent).

**3. Scale across multiple commodities.**
Don't sum individual f's — ignores correlation and can exceed 100%. Avoid full-size concurrent positions in positively correlated commodities; negative correlations may be ignored. For a precise aggregate F: compute each round's geometric joint return across commodities, then run the step-1 TWR-maximization on those joint returns. Allocate per commodity equally (F × bankroll ÷ concurrent commodities), by mean-variance (Markowitz) optimization, or by each commodity's own f scaled to sum to F. A user cap on any single commodity overrides the formula. If a commodity's (permissible risk ÷ margin) exceeds F, risk governs contract count; if lower, margin governs.

**4. Control risk of ruin directly.**
Estimate p and A from a track record; look up or simulate risk of ruin R at the planned exposure (closed-form: R=(q/p)^k for A=1; R=[(0.25+1/(2A))(1/p−0.5)]^k for A=2; other ratios need simulation — tables cover A=1–10 at exposures 100/50/33/25/20/10%). If R is too high, raise capital units k=1/exposure and recheck. Hard floor: at A=2, R=1 (certain ruin) once p ≤ 0.33.

**5. Pyramid only realized profit on winners.**
Effective exposure = |entry − stop| × contracts while the stop hasn't passed breakeven. Past breakeven, assured unrealized profit = (stop − entry) × contracts (long) or (entry − stop) × contracts (short). Choose p (0–1), the fraction of that locked-in gain to risk again: additional contracts = (p × assured profit × current contracts) ÷ permissible loss per new contract. Never pyramid to average down a loser.

## Risk

Cutting exposure from 50% to 20% of capital (p=0.60, A=2) cuts risk of ruin from 0.209 to 0.020. The gain needed to recover a percentage loss L = 1/(1−L) − 1: a 50% loss needs +100% to recover, a 90% loss needs +900% — why oversized single-trade losses matter more than raw edge. Optimal f, uncapped, can recommend aggressive exposure (20%+ in the worked examples) that maximizes growth but produces large drawdowns; always run the risk-of-ruin check (step 4) alongside any optimal-f result.

## Caveats

All formulas assume p and A stay stable for the next trade; in practice these drift as conditions change. Closed-form risk-of-ruin only exists for A=1 or A=2; other ratios need simulation and table interpolation is approximate. Mean-variance multi-commodity allocation assumes a stable opportunity set and correlations, better suited to a longer-horizon position trader than a short-term futures trader. Dollar/margin examples are 1980s-era; the mechanics transfer but inputs must be updated.