---
title: Darvas Box Theory
author: Nicolas Darvas
year: 1960
slug: how-i-made-2-million-in-the-stock-market--box-theory
parent: how-i-made-2-million-in-the-stock-market
tier: A
category: Trend Following & Mechanical Systems
tags: [box-theory, breakout, stop-loss, pyramiding, momentum, growth-stocks]
difficulty: beginner
doc_type: system
pages: 120
one_liner: "Buy a stock breaking decisively into a new, higher price box on strong volume, ride it with a rising trailing stop, cut it fast if the stop is hit."
related: [how-i-made-2-million-in-the-stock-market, michael-covel-trend-following, richard-l-weissman-mechanical-trading-systems]
source_file: "How I Made 2 Million In The Stock Market.pdf"
---

## What it is

A discretionary-but-rule-bound breakout system for actively traded, higher-priced growth stocks. Price is assumed to advance in a "staircase" of overlapping trading ranges, or **boxes**. A stock is bought only when it convincingly leaves its current box on the upside, moving into a new, higher box; it is held while it continues to establish successively higher boxes, and sold automatically when a trailing stop is triggered. Entries and exits were both placed as standing stop-orders (buy-stop above, sell-stop below), since Darvas traded remotely by daily broker cable and could not react to intraday price moves.

## Rules

**Universe / fundamental filter**
- Trade only actively traded, higher-priced, exchange-listed stocks (no over-the-counter names).
- Prefer industries with a genuine, plausible growth or earnings story (Darvas used electronics, missiles, and rocket-fuel companies as his examples) — improving or anticipated earnings power, not just a hot price.
- Ignore tips, rumors, and advisory-service recommendations; use only price, volume, and the company's earnings trend as inputs.

**Defining a box**
- Track each candidate's daily high, low, and close.
- A box's ceiling is the level price fails to close above (or only fractionally penetrates) for three consecutive days; the floor is defined symmetrically as the level it fails to close below for three consecutive days.
- A stock can sit in one box for days or weeks; normal daily noise inside the box (e.g., a reaction from the top of a 55–60 box back to 55) is not a sell signal.
- If a stock's daily close moves decisively below the current box's floor, the box thesis is broken — the stock is no longer in an uptrend structure and is not a candidate (or is stopped out if held).

**Entry**
- Place a buy-stop order a fraction above the current box's ceiling; only get filled if price actually pushes through, confirming the breakout rather than guessing at it.
- Optionally start with a smaller "pilot" buy at or near the breakout, then add a larger tranche once the stock confirms it is holding the new, higher box rather than slipping back.
- Do not buy on dips inside a box, and do not chase a stock that is already deep into a new box without a fresh, confirmed breakout.

**Pyramiding (adding to winners)**
- As the stock establishes each successive higher box (again confirmed by the three-consecutive-day test), add another tranche on the breakout above that box's ceiling, using a buy-stop order the same way as the initial entry.
- Position size can be scaled up using unrealized profits and margin as the position works, not only initial capital.
- Never add to a losing position, and never lower a stop to "give a trade more room."

**Stop-loss (exit)**
- On entry, set an initial protective sell-stop below the entry price / below the box's floor.
- As the stock advances into new boxes, raise ("trail") the stop up to just below the floor of the most recently confirmed box — in fast-moving conditions, Darvas sometimes tightened it to within about 2 points of the latest close.
- The stop is only ever moved up, never down, and once hit, the position is closed without exception or second-guessing.
- If stopped out and the stock subsequently re-establishes a valid box breakout, treat it as a fresh, independent setup and re-enter — a stop-out is not a permanent verdict on the stock.

**Filter for weak candidates**
- When holding several similar candidate stocks, an arbitrary stop-loss (Darvas used 10% in at least one instance) can be used purely to cull the weakest performer(s) from the group, independent of the box-specific stop on any individual position.

## Risk

- Per-trade loss is bounded by the trailing stop, which Darvas describes keeping tight enough to hold most closed-out losses under roughly 10% of the position, though he gives no formal percent-of-equity sizing rule.
- No explicit maximum position size or portfolio-heat rule is stated; Darvas ran a concentrated book (often a handful of names) and used margin aggressively to size up winners, including one large stock-rights arbitrage trade that materially levered a single position.
- Because entries and exits are both stop orders, slippage/gaps are a real risk: several of the book's examples show fills well away from the intended stop level during fast moves (e.g., sold "at varying prices" well below the nominal stop).
- The system is trend-dependent: it performs best in stocks with a genuine sustained advance and can produce a string of small, quick stop-outs in choppy, range-bound, or declining markets (Darvas himself stopped trading entirely during one prolonged "baby bear" market rather than force trades).

## Caveats

The box boundaries and the "three consecutive days" confirmation rule are described narratively and through reader Q&A rather than as a precise, unambiguous algorithm; Darvas's own answers to readers concede judgment calls remain (e.g., how to treat closing prices with different fractions at the same whole-number level). No backtest, win rate, or systematic performance statistics are given — the evidence is a small set of narrated real trades (Lorillard, Universal Controls, Thiokol, Zenith, Fairchild, Diners' Club, and others) plus profit/loss tables, not a rigorous study. These notes are based on OCR of a sampled subset of pages of a scanned copy; the book's full worked examples were not all available for review, and some box-boundary specifics may be incomplete.
