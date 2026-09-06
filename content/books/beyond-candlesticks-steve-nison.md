---
author: Steve Nison
category: Candlesticks & Chart Patterns
diagram: candle-anatomy
diagram_caption: The western bar recast as a candle — Nison's starting point.
difficulty: intermediate
doc_type: book
one_liner: 'Nison''s follow-up to Japanese Candlestick Charting Techniques adds the
  disparity index and three under-translated Japanese charting styles: three-line
  break, renko, and kagi.'
pages: 276
related:
- trading-hill-arthur-introduction-to-candlesticks
- greg-morris-candlestick-charting-explained
- candlestick-charting-explained
- john-l-person-swing-trading-using-candlestick-charting-with-pivot-point
reviewed_pdf_pages: 8-11, 22-23, 31, 39-40 (contents, the disparity index and moving-average
  chapters, and the three-line break/renko/kagi construction rules)
slug: beyond-candlesticks-steve-nison
source_file: Beyond_Candlesticks__Steve_Nison_.pdf
source_review: partial
tags:
- candlesticks
- disparity-index
- three-line-break
- renko
- kagi
- moving-averages
- japanese-charting
tier: A
title: 'Beyond Candlesticks: New Japanese Charting Techniques Revealed'
year: 1994
---

## Overview

Steve Nison's follow-up to his original *Japanese Candlestick Charting Techniques* is split into two parts. Part One (Chapters 1-4) re-covers candlestick construction, single- and multi-line patterns, and how to combine candle signals with stops, risk/reward, and prevailing trend. Part Two (Chapters 5-8), the book's real contribution, introduces four Japanese technical tools rarely documented in English at the time: the disparity index (a moving-average oscillator), and three "new price chart" styles — three-line break, renko, and kagi — that plot price changes rather than fixed time intervals and ignore sessions that don't make a new high or low. Each of the three charting chapters follows the same structure: an overview, a step-by-step construction section with a worked numeric example, and a trading-techniques section, closing with a practice dataset and answer key.

## Core thesis

Candlestick patterns are powerful for pinpointing reversal *sessions* but rarely provide price targets or an unambiguous read on the larger trend by themselves. The three-line break, renko, and kagi charts fill that gap: because a new line is drawn only when price makes a new high or low (not on every session), they filter out noise, make support/resistance and the prevailing trend visually obvious, and — since most versions are built from closing prices alone — can chart instruments that report only closes (mutual funds, some yield series). Nison's recommended workflow is to use one of these three charts to establish the dominant trend, then use candlestick signals as the entry trigger within that trend, since candles alone rarely supply a stop-loss or profit target.

## Key concepts

- **Real body / shadow** — the open-close range (body) versus the high/low extremes beyond it (shadows); a long body shows conviction, a long shadow shows rejection at that price.
- **Doji** — open equals (or nearly equals) close; signals indecision, especially significant after an extended trend or at an overbought/oversold extreme.
- **Hammer / hanging man** — a small body with a long lower shadow and little/no upper shadow; bullish (hammer) after a decline, bearish (hanging man) after an advance — same shape, opposite meaning depending on prior trend.
- **Engulfing pattern** — a real body that fully engulfs the prior session's opposite-colored body, signaling a reversal.
- **Dark cloud cover / piercing pattern** — a two-candle reversal where the second body closes beyond the midpoint of the first; the deeper the penetration past the halfway point, the stronger the signal (an incomplete close, short of the midpoint, is treated as weaker and needs confirmation).
- **Disparity index** — (close / chosen moving average - 1) x 100%, expressed as a percentage; shows how far price has stretched from its moving average, used as an overbought/oversold and divergence gauge. Common periods: 5-, 9-, 25-day (short-term) or 13-, 26-week / 75-, 200-day (long-term).
- **Golden cross / dead cross** — a shorter moving average crossing above (golden, bullish) or below (dead, bearish) a longer one; commonly 13-week vs. 26-week in Nison's Japanese sources.
- **Three-line break chart** — plots white/black "lines" that appear only on a new high or new low close; after three consecutive same-color lines, price must break the extreme of those three lines (not just make any new high/low) to draw a reversal ("turnaround") line.
- **Renko chart** — plots equal-height "bricks" of a fixed point (or percentage) size; a new brick is drawn only once price has moved by at least one full brick-height beyond the current extreme.
- **Kagi chart** — plots thick (yang) and thin (yin) lines that reverse direction only once price moves beyond a chosen turnaround amount; the line thickens when it breaks a prior high (a "shoulder") and thins when it breaks a prior low (a "waist").
- **Shoulders and waists** — in kagi charting, prior highs (shoulders) and lows (waists) on the kagi line; a rising sequence of both signals bullish control, a falling sequence signals bearish control.

## Rules and setups

1. **Disparity index**: Disparity % = ((Close - MA) / MA) x 100. A reading of roughly +10% to +15% (market-dependent) is commonly overbought, -10% to -15% oversold; a rising index confirms an uptrend, a falling one a downtrend; a new price high with a lower disparity peak is bearish divergence (mirrored at lows).
2. **Three-line break**: draw a white line up (black down) only when a new closing high (low) exceeds the prior line's range, not merely touches it. Once three lines share a color, a reversal line requires price to close beyond the extreme of all three, not just a one-tick new high/low. Buy on a new white line, sell on a new black line.
3. **Renko**: fixed brick size (points or %); a brick prints only once price closes a full brick-height beyond the current extreme, in either direction; excess beyond a full brick is unplotted. Buy on a new white brick, sell on a new black brick — a pure stop-and-reverse system.
4. **Kagi**: fixed (or percentage) turnaround amount; extend the line for any same-direction move, however small; only reverse, in the next column, once price moves against it by the full turnaround amount. The line thickens (yin to yang) exceeding a prior shoulder, thins (yang to yin) breaking a prior waist. Buy on thin-to-thick, sell on thick-to-thin; two- or three-level breaks (requiring 2-3 prior shoulders/waists broken) trade less often with higher confidence.
5. Full construction and signal rules: [[beyond-candlesticks-steve-nison--disparity-index]], [[beyond-candlesticks-steve-nison--three-line-break-chart]], [[beyond-candlesticks-steve-nison--renko-chart]], [[beyond-candlesticks-steve-nison--kagi-chart]].

## Risk and money management

Nison gives comparatively little formal money-management guidance; this is a pattern-and-charting manual, not a risk-sizing manual. Stops are typically placed on the far side of the candle pattern's extreme (below a hammer's low, above a hanging man's high); a candle signal is treated as more reliable when it agrees with an oversold/overbought disparity-index reading; and since candles rarely supply a profit target, Nison recommends using the reversal signal from a three-line break, renko, or kagi chart as the exit for a position entered on a candle trigger. All three new-price charts share a structural timing problem: a reversal line only confirms on the close, so by the time it prints, price may already be well beyond the reversal threshold. Some Japanese traders address this by taking a light intraday position once the threshold is touched, adding — or exiting if unconfirmed — at the close.

## Psychology and discipline

The recurring theme is patience and trend discipline rather than trade-by-trade psychology: three-line break, renko, and kagi charts are explicitly tools for catching the "meat" of a move, not for picking exact tops or bottoms, and reversal confirmation on them comes later than a candlestick signal would — traders uncomfortable with that lag should combine a new-price chart's trend read with a candlestick signal's earlier timing rather than relying on either alone. The "nine record sessions" concept (nine higher shoulders or lower waists on a kagi chart) is a Japanese exhaustion heuristic — after roughly nine record highs or lows, traders are counseled to watch for a countertrend move rather than chase the trend further.

## Chapter map

- Ch 1 — Overview — introduces candles and previews the book's two-part structure.
- Ch 2 — The Basics — candle construction, real bodies, shadows, doji, high-wave candles.
- Ch 3 — The Patterns — hammer, hanging man, shooting star, dark cloud cover, piercing pattern, engulfing, harami, windows, evening/morning star.
- Ch 4 — Candles and the Overall Technical Picture — stops, risk/reward, trend context, computerizing candle signals.
- Ch 5 — How the Japanese Use Moving Averages — golden/dead cross, disparity index, divergence index.
- Ch 6 — Three-Line Break Charts — construction and trading techniques, with a practice session.
- Ch 7 — Renko Charts — construction and trading techniques, with a practice session.
- Ch 8 — Kagi Charts — construction, shoulders/waists, multi-level breaks, double windows, three-Buddha patterns, record sessions, with a practice session.

## Strengths and caveats

The construction chapters (5-8) are the book's core value: each new-price chart is built step-by-step from a worked numeric table, which makes the (otherwise hard-to-find in English) rules unambiguous enough to code. The candlestick chapters (1-4) are largely a condensed restatement of Nison's first book and add little new for readers who already know standard candle patterns. All three new-price charting techniques are explicitly trend-following and slow to reverse — Nison states plainly that they are not designed to pick exact tops or bottoms, and every example shows some degree of whipsaw in lateral markets. The choice of reversal amount (kagi turnaround, renko brick size) or table thresholds is left to trader judgment with only general Japanese-market conventions (e.g., ~3% kagi for stocks) offered as a starting point, not a rule.

## Who should read it

Traders already familiar with basic candlestick patterns who want a trend-confirmation layer beyond candles — particularly futures, forex, or closing-price-only instruments (mutual funds, some yield series) where three-line break, renko, or kagi charting can be applied. Less useful as a first introduction to candlesticks; readers new to candles are better served starting with a dedicated candlestick primer before this book's construction-heavy Part Two.

## Related books in this library

- [[trading-hill-arthur-introduction-to-candlesticks]] — a shorter primer covering the same core candle patterns this book's Part One restates.
- [[greg-morris-candlestick-charting-explained]] — an alternative, statistics-oriented treatment of the same candlestick pattern set.
- [[candlestick-charting-explained]] — another candlestick reference for cross-checking pattern definitions and reliability claims.
- [[john-l-person-swing-trading-using-candlestick-charting-with-pivot-point]] — applies candlestick signals (as this book recommends) within a broader trend/pivot framework for entries.
