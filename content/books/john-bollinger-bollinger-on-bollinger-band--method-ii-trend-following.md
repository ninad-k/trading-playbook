---
title: Method II — Trend Following with %b and MFI
author: John Bollinger
year: 2002
slug: john-bollinger-bollinger-on-bollinger-band--method-ii-trend-following
tier: A
category: Indicators
tags: [bollinger-bands, percent-b, money-flow-index, trend-following]
difficulty: intermediate
doc_type: system
parent: john-bollinger-bollinger-on-bollinger-band
pages: 264
one_liner: "Buy price strength near the upper band only when confirmed by Money Flow Index strength; sell weakness near the lower band only when confirmed by MFI weakness."
related: []
source_file: "John Bollinger - Bollinger On Bollinger Band.pdf"
---

## What it is

A confirmation-based trend-anticipation system: rather than requiring a Squeeze precondition (Method I), it looks for price already pushing toward a band while an independent volume-based momentum indicator, Money Flow Index (MFI), confirms the same strength or weakness. When both agree, the method anticipates the birth of a new trend leg. It is described as a variation on Method I that can fire earlier, before a Squeeze-based breakout signal would trigger.

## Rules

1. **Buy signal**: %b > 0.8 **and** 10-period MFI > 80. (%b > 0.8 means price is in the top 20% of the distance between the lower and upper band; MFI > 80 is a strong reading, analogous in significance to RSI > 70.)
2. **Sell/short signal**: %b < 0.2 and MFI(10) < 20 — the exact mirror condition.
3. **Bands**: standard 20-period, ±2σ.
4. **Indicator length rule of thumb**: set the confirming indicator's period to roughly half the length of the band's calculation period (a 10-period MFI paired with 20-period bands), not a quarter as cycle-analysis convention might suggest — testing showed quarter-length indicators fired too early.
5. **Exit**: a modified Parabolic stop, or a tag of the Bollinger Band on the opposite side of the trade for a longer-duration trade.
6. **Late-entry mitigation**: because %b and MFI may already be well into their extremes by the time the signal fires, consider treating the signal as an alert and buying the first pullback afterward instead of the signal bar itself — this misses some setups but improves the risk/reward on the ones taken.
7. **Variations**: substitute Volume-Weighted MACD (or its histogram, for a faster/more sensitive variant) for MFI; vary the %b and MFI thresholds up for more volatile growth stocks (e.g., requiring %b > 1); adjust the Parabolic's speed constant to trade-off stop tightness against time given to the trade; optionally start the Parabolic under the most recent significant swing low/high rather than under the entry bar, to better capture recent price character.
8. **Optional pre-filter (Rational Analysis)**: presort the trading universe with fundamental criteria into buy lists and sell lists, then take only buy signals from the buy list and sell signals from the sell list.

## Risk

No fixed percent-risk or position-sizing rule is specified; risk is controlled through the same two exit mechanisms as Method I (Parabolic stop for a tighter, more conservative trade, or opposite-band tag for a longer, wider one). The main quantified risk-control lever is parameter choice: more risk-averse traders are directed toward faster (larger) Parabolic acceleration constants that tighten stops more quickly, while more patient traders use smaller constants that give trades more room. Late entry is flagged as the primary risk to the strategy's risk/reward — much of the move may already have occurred by the time both conditions are satisfied — which is why the pullback/alert variant is recommended as the more risk-efficient version.

## Caveats

Because there is no Squeeze precondition, Method II can generate signals in already-extended markets, and the book explicitly warns that risk/reward is harder to quantify than in Method I since the move may be well underway before the signal fires. No specific backtested statistics (win rate, average return) are given — only worked chart examples (AG Edwards buy, Micron sell, PerkinElmer as a near-miss/alert case). The indicator-length rule of thumb (half the band period) is presented as empirically derived from Bollinger's own experimentation rather than from a closed-form statistical justification.
