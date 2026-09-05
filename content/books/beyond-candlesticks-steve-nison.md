---
title: "Beyond Candlesticks: New Japanese Charting Techniques Revealed"
author: "Steve Nison"
year: 1994
slug: beyond-candlesticks-steve-nison
tier: A
category: Candlesticks & Chart Patterns
tags: [candlesticks, disparity-index, three-line-break, renko, kagi, moving-averages, japanese-charting]
difficulty: intermediate
doc_type: book
pages: 276
one_liner: "Nison's follow-up to Japanese Candlestick Charting Techniques adds the disparity index and three under-translated Japanese charting styles: three-line break, renko, and kagi."
related: [trading-hill-arthur-introduction-to-candlesticks, greg-morris-candlestick-charting-explained, candlestick-charting-explained, john-l-person-swing-trading-using-candlestick-charting-with-pivot-point]
source_file: "Beyond_Candlesticks__Steve_Nison_.pdf"
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

1. **Disparity index construction**: Disparity % = ((Close - MA) / MA) x 100. A reading of +10% to +15% (market-dependent) is commonly treated as overbought; -10% to -15% as oversold. Between extremes, a rising disparity index confirms an uptrend and a falling one confirms a downtrend; a new price high with a lower disparity peak than the prior high is bearish divergence (and the mirror is bullish divergence at lows).
2. **Three-line break construction**: pick a base price; draw a white line up (black line down) only when a new closing high (low) exceeds the prior line's range — not merely touches it. Once three consecutive lines share a color, a reversal ("turnaround") line requires price to close beyond the extreme of all three same-colored lines, not just make a one-tick new high/low.
3. **Three-line break signal**: buy when a white line (or white turnaround line) appears; sell/short when a black line appears. In a trendless, alternating market this whipsaws; the tool is designed for markets that have entered a run of 3+ same-color lines.
4. **Renko construction**: choose a fixed brick size (points or %); a white brick is drawn only once price closes at or beyond one full brick-height above the current high; a black brick only once price closes at or beyond one brick-height below the current low; overshoot beyond a full brick multiple draws multiple bricks, each in its own column, with any partial excess unplotted.
5. **Renko signal**: buy on the appearance of a new white brick; sell/short on a new black brick — a pure trend-following stop-and-reverse system, prone to whipsaw in lateral ranges.
6. **Kagi construction**: choose a fixed (or percentage) turnaround amount; extend the current line for any move in the same direction, however small; only draw a reversal line, in the next column, once price reverses by the full turnaround amount from the line's tip. The line thickens (yin to yang) when it exceeds a prior shoulder; it thins (yang to yin) when it breaks a prior waist.
7. **Kagi signal ("buy on yang, sell on yin")**: buy when the line converts from thin to thick (breaks a prior shoulder); sell when it converts from thick to thin (breaks a prior waist). Confirmation variants: a two- or three-level break (requiring two or three prior shoulders/waists to be broken) trades less often but with higher confidence.
8. Full construction and signal details for the disparity index, three-line break, renko, and kagi charts are broken out as standalone system pages: [[beyond-candlesticks-steve-nison--disparity-index]], [[beyond-candlesticks-steve-nison--three-line-break-chart]], [[beyond-candlesticks-steve-nison--renko-chart]], [[beyond-candlesticks-steve-nison--kagi-chart]].

## Risk and money management

Nison gives comparatively little formal money-management guidance; the book is a pattern-and-charting-technique manual, not a risk-sizing manual. What it does offer: stops are typically placed on the far side of the candle pattern's extreme (e.g., below a hammer's low, above a hanging man's high); a candle signal is treated as more reliable when it agrees with an oversold/overbought disparity-index reading; and because candles rarely supply a profit target, Nison recommends using the reversal signal from a three-line break, renko, or kagi chart as the exit mechanism for a position that was originally entered on a candle trigger. The book also flags a structural timing problem for all three new-price charts: because a reversal line is only confirmed on the close, by the time the reversal amount is definitively met price may already be well beyond it. Nison notes some Japanese traders address this by taking a small position intraday once the reversal threshold is touched, then adding — or exiting if unconfirmed — at the close.

## Psychology and discipline

The recurring theme is patience and trend discipline rather than trade-by-trade psychology: three-line break, renko, and kagi charts are explicitly described as tools for catching the "meat" of a move, not for picking exact tops or bottoms, and Nison repeatedly cautions that reversal confirmation on these charts comes later than a candlestick reversal signal would — traders uncomfortable with that lag should combine the trend read from a new-price chart with the earlier, more precise timing of a candlestick signal rather than relying on either alone. The "nine record sessions" concept (nine consecutive higher shoulders or lower waists on a kagi chart) is presented as a Japanese exhaustion heuristic — after roughly nine record highs or lows, traders are counseled to start watching for a countertrend move rather than chasing the trend further.

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
