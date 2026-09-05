---
title: "Accumulation/Distribution Stock Selection System"
author: Larry Williams
year: 1972
slug: larry-williams-the-secret-of-selecting-stocks-for-immediate-and-substantial-gains--accumulation-distribution-system
tier: A
category: Indicators
tags: [accumulation-distribution, volume, divergence, stock-selection, trailing-stop]
difficulty: intermediate
doc_type: system
parent: larry-williams-the-secret-of-selecting-stocks-for-immediate-and-substantial-gains
pages: 131
one_liner: "Williams' original volume-weighted accumulation/distribution formula, cumulated into a flow line, traded on divergence from price with a fixed checklist, entry-timing, and trailing-stop rules."
related: []
source_file: "Larry Williams - The Secret Of Selecting Stocks For Immediate And Substantial Gains.pdf"
---

## What it is

A daily, open/high/low/close/volume-based method for estimating what fraction of a stock's trading volume on a given day was buying pressure versus selling pressure, cumulated into a running "A/D line" (accumulation/distribution flow line). The system's edge comes from comparing this line to price: when the two diverge — price makes a new extreme the volume-weighted flow line does not confirm — that divergence is treated as evidence of informed ("professional") buying or selling working against the visible price trend, and is used as the primary buy/sell trigger. It is explicitly Williams' alternative to standard On Balance Volume (which uses only the sign of the day's price change) and to price-only charting.

## Rules

**Step 1 — calculate the day's net buying/selling percentage.**
```
net % = (close − open) / (high − low)
```
If the close is above the open, the day is net buying (positive %); if below, net selling (negative %). If open equals close, buying and selling were equal for the day (no update needed — carry the A/D line forward unchanged).

**Step 2 — convert to a volume figure.**
```
net daily A/D = net % × today's total volume
```
This is the estimated number of shares that were net buying (or net selling) volume for the day.

**Step 3 — cumulate into the A/D flow line.**
Pick an arbitrary starting base value (e.g., 5,000) the first time you "work up" a stock. Each subsequent day, add the net daily A/D figure to (or subtract it from) the previous day's A/D line value — exactly as with a traditional On Balance Volume line, but weighted by *how much* of the day was buying versus selling, not merely which direction the close moved.

Time-saving shortcuts Williams gives:
- If open = close for the day, buying and selling were equal; skip the formula and carry the prior A/D line value forward.
- If open = high and close = low, the entire day's volume was selling; simply subtract the full day's volume from the A/D line.
- If open = low and close = high, the entire day's volume was buying; simply add the full day's volume to the A/D line.

**If opening prices are unavailable**, substitute yesterday's close for today's open: buying units = (today's high − yesterday's close) if positive, else zero; selling units = (yesterday's close − today's low) if positive, else zero, plus (today's high − today's close). Divide the buying unit by the buying-plus-selling total to get the day's buy percentage, then apply Step 2-3 as above. This produces a similar but not identical A/D line to the open-based version.

**Buy signal.** Price makes a new (short/intermediate-term) low, but the A/D line does *not* make a corresponding new low — it holds well above its prior comparable low. This divergence indicates the price decline was not matched by real selling pressure and is treated as likely-artificial weakness engineered to shake out holders before a move higher.

**Sell/short signal.** The mirror case: price rallies to a new high, but the A/D line fails to confirm — it does not make a new high, or actually falls. Indicates the rally is being sold into by informed money despite the apparent price strength.

**Immediate profit signal (early-entry variant).** While price is consolidating in a narrow trading range (basing), watch for a single day's A/D figure to surge sharply, breaking the A/D line clearly above (or below) its own recent range while price is still contained. The direction of this A/D breakout is used to anticipate which way price will break out of its range, ahead of the price move itself.

**Ranking multiple candidates.** When more than one stock shows a qualifying divergence, prefer the one with the *largest* divergence between its price action and its A/D line — the greatest gap between how weak/strong the price looks and how strong/weak the A/D line actually is.

**Pre-trade checklist (all must be satisfied):**
1. Determine whether this is a short-term or intermediate-term setup (which timing indices apply).
2. Confirm the relevant market-timing index has reached its buy/sell zone.
3. Confirm the stock qualifies on the comparative price accumulation/distribution pattern versus the broad market.
4. Confirm the stock's own daily A/D line independently shows accumulation/distribution.
5. Confirm this stock's divergence is the strongest among all candidates currently followed.

**Entry execution.** Once the checklist is satisfied, do not buy on a strong up day — wait for a sharp adverse market day (Williams' example: a 7-10 point DJIA decline) to execute the buy; mirror-image for sells (execute on a strong up day, ideally late Friday afternoon per the seasonal bias noted in the parent book).

## Risk

- **Universe filter:** only apply this system to stocks trading above $30/share; Williams found the formula unreliable on lower-priced, more manipulation-prone, retail-dominated issues.
- **Concentration:** trade the 2-3 strongest qualifying candidates rather than spreading capital across many marginal signals; if more than 2 stocks qualify on all checklist items, use the relative strength of the A/D divergence itself as the final tie-breaker.
- **Trailing stop:** place the stop 2 points below the most recently established price base; as new, higher bases form, raise the stop to sit 2 points below the new base. Never lower a stop once set. Stops must be live broker orders, not "mental stops" ("mental stops don't work," per the text).
- **Loss-cutting rule:** if a position shows a loss for roughly three consecutive days after entry, treat that as confirmation the original read was wrong and exit — do not wait for a round-trip back to breakeven.
- **Avoid over-leveraging a single idea:** the book explicitly flags "plunging" (using all capital plus margin on one position) as a primary cause of large losses in this style of trading.

## Caveats

The A/D formula's estimate of buying/selling volume is a heuristic derived from the intraday close-to-open and high-to-low relationship, not an actual count of buy-side versus sell-side executed volume (which was not available to a retail analyst in this era) — it is an approximation, and Williams' own alternate close-based version (when opens are unavailable) is stated to produce a materially different A/D line and different trades, not merely a proxy for the same one. No formal backtest statistics (win rate, average gain, drawdown) are given for the system as a whole; the book instead relies on individual illustrative trade examples (Bausch & Lomb, McDonald's, Burroughs) rather than a systematic historical test. The "immediate profit signal" and the divergence rules both depend on subjective judgment of what counts as a "new low/high" and how large a divergence is meaningful — the book does not give a precise numeric threshold (e.g., a minimum percentage divergence) for either signal, unlike the more codified breakout and band systems found in later technical-trading texts.
