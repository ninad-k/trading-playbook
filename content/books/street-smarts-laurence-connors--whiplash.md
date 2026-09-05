---
title: "Whiplash"
author: Laurence A. Connors and Linda Bradford Raschke
year: 1995
slug: street-smarts-laurence-connors--whiplash
tier: A
category: Swing Trading
tags: [gap-trading, close-only-entry, market-on-close, reversal]
difficulty: beginner
doc_type: system
parent: street-smarts-laurence-connors
pages: 145
one_liner: "Enters market-on-close after a morning gap fully reverses into the opposite half of the day's range, betting on next-morning follow-through without needing the gap to fill."
related: []
source_file: "Street Smarts (Laurence Connors).pdf"
---

## What it is

A gap-fade pattern that requires the market to prove intraday failure of its own opening gap before entry, then commits only at the close (market-on-close, or MOC) rather than intraday. Unlike other gap strategies in the book, the gap itself never needs to fill for the trade to work — the entry is based purely on the close relative to the open and the day's range, on the premise that a decisive afternoon reversal from a morning gap tends to follow through the next day.

## Rules

**Buy setup (sells are reversed):**
1. The market must gap lower than the previous day's low (night-session data is ignored).
2. The close must be higher than the open and also in the top 50% of the day's trading range.
3. If both conditions are met, buy market-on-close (MOC).
4. If tomorrow opens below today's close (an immediate loss on the position), sell immediately — take the loss without hesitation.
5. If tomorrow opens with a profit, trail a stop to protect it.

## Risk

Risk is bounded and asymmetric by design: the trade is only ever held from today's close to tomorrow's open (a single overnight gap), and any adverse opening is closed out immediately per rule 4 rather than given room to develop. The authors describe backtesting showing "a good win/loss percentage" in the overnight gap action specifically, framing the setup as giving a roughly 60% "headstart" — most of the time the position opens with at least a small profit the next morning, which is the entire edge being harvested. No fixed percent-of-equity position size is specified; risk per trade is inherently small because the loss is capped at one overnight gap move and cut immediately if realized.

## Caveats

The authors note a "slight sell-side bias" to this strategy confirmed in their testing, meaning the sell (short) version may perform somewhat better on average than the buy version — a nuance not reflected in the mechanical rules themselves. It might seem counterintuitive to enter on the close only to exit immediately on a bad opening, but the authors argue this asymmetry (small, quick losses versus a high-probability favorable opening) is the point, not a flaw. No independent backtested win rate, sample size, or drawdown figure is quoted in this specific chapter beyond the general "good win/loss percentage" claim; the illustration given is a run of four soybean examples over a three-week period in November 1995, and the authors note they trade this pattern most often in S&P futures and bonds rather than across all markets equally.
