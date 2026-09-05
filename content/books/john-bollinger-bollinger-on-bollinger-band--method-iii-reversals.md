---
title: Method III — Reversals
author: John Bollinger
year: 2002
slug: john-bollinger-bollinger-on-bollinger-band--method-iii-reversals
tier: A
category: Indicators
tags: [bollinger-bands, percent-b, mean-reversion, volume-indicators, reversals]
difficulty: intermediate
doc_type: system
parent: john-bollinger-bollinger-on-bollinger-band
pages: 264
one_liner: "Buy a lower-band tag not confirmed by weak volume; sell an upper-band tag not confirmed by strong volume — the opposite logic from Methods I and II."
related: []
source_file: "John Bollinger - Bollinger On Bollinger Band.pdf"
---

## What it is

A mean-reversion method that anticipates trend reversals by comparing band-tag location to volume-oscillator behavior, looking specifically for *non-confirmation* — a band tag that is not backed by matching momentum/volume strength. It descends from the classic 1970s approach of comparing percentage-envelope tags against breadth oscillators (advance-decline, up/down volume), updated by Bollinger to use his own MACD-based "departure" technique for normalizing the breadth data and, on individual stocks, volume oscillators (Intraday Intensity %, Accumulation/Distribution %) in place of broad-market breadth.

## Rules

1. **Simple/discrete form (systematized)**: go long when %b < 0.05 **and** 21-day Intraday Intensity % (or 20-day AD%) is greater than zero; go short when %b > 0.95 **and** the same oscillator is less than zero. This is a tag of one band combined with an indicator reading in the *opposite* state from what the tag would suggest.
2. **Pattern form — W-bottom ("relative W")**: form a W where %b is higher on the retest low than on the initial low (even if price itself makes a marginal new low); check that the volume oscillator (MFI or Volume-Weighted MACD) shows the same higher-low pattern; if confirmed, buy the first strong up day.
3. **Pattern form — M-top**: typically takes three or more pushes to a high rather than two; in a classic top, %b is lower on each successive push, as is the volume oscillator (e.g., Accumulation/Distribution); after that pattern develops, sell on a meaningful down day with above-average volume and range.
4. **Multi-tag variant**: also watch for multiple upper-band tags with a deteriorating indicator (bearish), and multiple lower-band tags with a strengthening indicator (bullish), as a slower-forming version of the same signal.
5. **Legacy/market-breadth variant**: shift a 21-day moving average of the Dow by ±4% to form bands (or substitute Bollinger Bands directly on the index); confirm tags with an oscillator built from the *difference* between a 21-day and 100-day average of advances-minus-declines (or up-volume-minus-down-volume) — implementable directly with a MACD(21,100,9) applied to breadth data instead of price.

## Risk

No explicit stop-loss or position-sizing formula is given for Method III. Risk/reward is instead illustrated through Bollinger's own account of a real trade: a Method III long entered at a triple-bottom/potential breakdown with a close outside the lower band, confirmed by strongly positive Intraday Intensity %; because a new price low was close by, risk was well-defined at about 2.5 points, while the upper-band tag (the logical target) was 10 points away — roughly a 4-to-1 reward-to-risk setup. The implicit risk control is structural: because entries are keyed to band extremes with non-confirmation, the adverse excursion needed to invalidate the setup (a new low/high beyond the recent extreme) tends to be small relative to the reversion target at the opposite or middle band.

## Caveats

The method depends on volume-indicator data quality and choice — Bollinger notes AD and Intraday Intensity require well-specified bars, so results can be less reliable intraday or on thinly traded issues. No systematic backtest statistics are provided; the chapter's evidence is qualitative chart examples (Dow Chemical W-bottom, Lyondell M-top) plus the one narrated real-money trade. Because the method explicitly fades band extremes, it is the philosophical opposite of Method I and can produce conflicting signals with it on the same instrument if both are run concurrently — Bollinger does not offer a rule for reconciling the two.
