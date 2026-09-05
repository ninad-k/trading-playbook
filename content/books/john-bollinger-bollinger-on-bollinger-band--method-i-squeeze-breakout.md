---
title: Method I — The Squeeze / Volatility Breakout
author: John Bollinger
year: 2002
slug: john-bollinger-bollinger-on-bollinger-band--method-i-squeeze-breakout
tier: A
category: Indicators
tags: [bollinger-bands, the-squeeze, volatility-breakout, bandwidth]
difficulty: intermediate
doc_type: system
parent: john-bollinger-bollinger-on-bollinger-band
pages: 264
one_liner: "Trade the expansion that follows a Bollinger BandWidth Squeeze: buy a close above the upper band, sell short a close below the lower band."
related: []
source_file: "John Bollinger - Bollinger On Bollinger Band.pdf"
---

## What it is

The most direct application of Bollinger Bands: it anticipates high volatility by exploiting the cyclical nature of volatility itself — low volatility tends to be followed by high volatility, and vice versa. The setup (precondition) is The Squeeze, defined as BandWidth `(Upper BB − Lower BB) / Middle BB` falling to its lowest level in six months. Once the precondition is set, the trade is a breakout in whichever direction the market resolves. Unlike the popular myth about Bollinger Bands, this method does not fade band tags — it buys strength through the upper band and sells weakness through the lower band.

## Rules

1. **Precondition**: BandWidth at (or near) a six-month low. The longer the look-back used to define "low," the more explosive and less frequent the resulting setups.
2. **Bands**: standard 20-day/±2σ default, since bands are already tight during a Squeeze so triggers are close by; short-term traders may tighten to ~15-day/±1.5σ for a faster, noisier version.
3. **Entry (long)**: buy when price closes above the upper band while in/near a Squeeze.
4. **Entry (short)**: sell short when price closes below the lower band while in/near a Squeeze.
5. **Head-fake filter**: coming out of a Squeeze, price often makes a short false move opposite the eventual real move before reversing — watch prior Squeezes on the same instrument to see whether it is prone to head fakes. Two ways to handle it: (a) wait for the move to develop clearly before entering (loses some of the trade but avoids most fakes), or (b) trade half a position on the first strong move away from the range in the head-fake direction, then add the other half on the confirmed breakout, using a stop to exit the first half if it was indeed a fake.
6. **Volume confirmation**: before the head fake resolves, check a volume indicator — Intraday Intensity, Accumulation/Distribution, or Money Flow Index — for an early read on the likely direction of the real move.
7. **Universe**: screen at least several hundred securities for BandWidth six-month lows on any given day to generate a workable number of candidates.

## Risk

Two exit techniques, chosen by risk preference: (1) a Welles Wilder Parabolic stop, set initially just outside the breakout formation's range and incremented each day the trade is open — more conservative, shorter average trade duration; (2) a tag of the opposite Bollinger Band as the exit — allows the trade to run through minor corrections for a longer average duration but a further-away, less precise stop. There is no fixed percent-risk rule given; sizing and stop tightness scale with the trader's own tolerance, and tightening the BandWidth/period parameters makes the system faster but also more prone to whipsaw around head fakes.

## Caveats

Do not trade breakout logic without a preceding Squeeze — Bollinger states directly that in his testing, The Squeeze is a necessary precondition for this approach, not merely a helpful filter. Head fakes are the main source of losing trades and some securities are more head-fake-prone than others by history, so the same parameter set will not perform identically across instruments. No specific backtested win rate, profit factor, or drawdown figures are given for Method I in the text; the chapter provides worked chart examples (AvalonBay, Ocean Energy, Noble Drilling, Pinnacle Holdings, PPL Corp) rather than a statistical track record.
