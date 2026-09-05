---
title: "Pullback Swing Trade Scan and Support/Resistance Entries (Full System)"
author: "Tony Oz"
year: 2000
slug: tony-oz-how-i-make-a-living-trading-stocks--pullback-swing-trade-scan
tier: A
category: "Day Trading & Scalping"
tags: [support-resistance, scanning, pullback, breakout, risk-reward-ratio, stop-loss, day-trading]
difficulty: beginner
doc_type: system
parent: tony-oz-how-i-make-a-living-trading-stocks
pages: 146
one_liner: "A long-only setup that scans for three-day pullbacks into support, filters entries with a 3:1 reward-to-risk rule, and manages stops off intraday and multi-day support levels."
related: [john-j-murphy-charting-made-easy, jack-schwager-stock-market-wizards]
source_file: "Tony Oz - How I Make A Living Trading Stocks.pdf"
---

## What it is

Tony Oz's named overnight scan and the entry/exit framework he built around it, used to generate the majority of long trades documented in his four-week trading diary. The scan mechanically identifies liquid, higher-priced stocks that have pulled back for three consecutive days, then screens for the moment price stops making new lows and trades back above the prior day's low — a mean-reversion-style pullback entry inside a stock's larger trading range, always taken in the direction of a bounce off identified support. Two companion real-time scans (Breakout Scan and Power Scan) use the same liquidity/volatility filters to catch continuation setups (new highs) and momentum-thrust setups (closes near the day's high) instead of pullbacks.

## Rules

**Universe filter (applies to all three scans)**
1. Price between $40 and $200 per share.
2. Net change on the day of at least 5/8 of a point (for the real-time variants; the overnight Pullback scan does not require this).

**Pullback Swing Trade Scan (primary overnight scan)**
3. 20-day average volume greater than 350,000 shares (Oz's general watch-list liquidity threshold is 750,000+ shares average daily volume; the coded scan example uses 350,000).
4. Last price is above the previous day's low.
5. Each of the last four closes is lower than the one before it (`Close[1] < Close[2] < Close[3] < Close[4]`, most recent first) — i.e., three consecutive down days.
6. Candidates are reviewed manually on a chart the next session for a defined support level (a price tested and held more than once) before any order is placed — the scan surfaces candidates, it does not auto-trigger entries.

**Breakout Scan (real-time/overnight variant, for continuation entries)**
7. Average volume greater than 400,000 shares; today's volume greater than 1.7x its average.
8. Last trade is a four-week high.

**Power Scan (real-time variant, for momentum-thrust entries)**
9. Average volume greater than 350,000 shares; today's volume greater than 1.5x its average.
10. Last trade is in the top 13% of the day's trading range.

**Entry**
11. For a pullback candidate: buy once price confirms a bounce off the identified support level (support = a price where buying pressure previously stopped the decline, ideally tested more than once).
12. For a breakout candidate: buy once price trades above the defining resistance level (the prior high), or buy the pullback back to that former-resistance/now-support level after the initial breakout.
13. Before entering, compute the reward-to-risk ratio using the planned stop and price target; only take the trade if potential reward is at least 3x the planned risk. If the ratio is worse than 3:1, skip the trade regardless of how clean the pattern looks.

**Exit — stop-loss (choose the applicable level)**
14. Place the initial stop below whichever is most relevant to the setup: today's low, yesterday's low, a secondary intraday support level, a multi-day intraday support level, a 50% retracement of the last rally, or a relevant market index's day-low/support level.

**Exit — trailing stop and targets**
15. Once the trade is working, walk the stop up behind each new local support level (for longs) rather than leaving it at the original level.
16. Once a position is meaningfully in profit (a volatility-scaled threshold — a low-volatility stock is "in the money" after 1 point, a high-volatility stock needs more room), move the stop to at least breakeven so a winner cannot turn into a loss.
17. Take partial profit at the price target to lock in a portion of the trade, trailing the remainder.
18. Apply a time stop if the position stagnates without reaching either the stop or the target, to free up capital.

## Risk

No fixed percent-of-equity or dollar risk cap is attached to this specific setup; risk is bounded by (a) the stop-loss distance chosen from the menu above and (b) the account-wide position-size limits described in the parent book (roughly $25,000–$30,000 per non-index position against $50,000 risk capital and $100,000 buying power). The 3:1 reward-to-risk filter is the setup's main built-in risk control — it rejects trades where the defined stop is too close to the entry relative to the realistic target. Across the four-week diary in which this scan supplied most trades, the account produced a 32.55% return (116 total trades, 64.6% winners) during a period when the Nasdaq fell 30.78%, though the book does not isolate performance of this scan alone from the Constant watch list or the other two scans.

## Caveats

The scan's exact volume thresholds are inconsistent within the source (350,000 in the coded formula versus a stated 750,000+ preference elsewhere), and the $40–$200 price band and fractional-point criteria (5/8 point net change) reflect pre-decimalization, dot-com-era Nasdaq stock prices and tick sizes that do not map cleanly onto modern markets. The setup is explicitly long-only in the source material (a rule imposed by the challenge, not an inherent limitation of the pattern) and was tested on a small sample (116 trades over four weeks) during one unusually volatile historical episode. Confirmation of support before entry, and the choice of which stop-loss rule from the menu applies, both require discretionary chart judgment — the scan narrows a universe of candidates but does not fully mechanize entry timing or stop placement.
