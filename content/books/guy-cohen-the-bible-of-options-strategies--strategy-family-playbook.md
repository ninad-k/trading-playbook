---
title: The Bible of Options Strategies — Strategy Family Construction Playbook
author: Guy Cohen
year: 2005
slug: guy-cohen-the-bible-of-options-strategies--strategy-family-playbook
tier: A
category: Options, Futures & Derivatives
tags: [options, spreads, iron-condors, calendars, ratio-spreads, collars, construction-rules]
difficulty: intermediate
doc_type: system
parent: guy-cohen-the-bible-of-options-strategies
pages: 401
one_liner: "Construction, adjustment, and exit rules for the six recurring options-strategy families that make up all 58 strategies in the book."
related: [guy-cohen-the-bible-of-options-strategies, lawrence-g-mcmillan-profit-with-options]
source_file: "Guy Cohen The Bible of Options Strategies.pdf"
---

## What it is

A condensed, code-able rulebook distilled from Cohen's 58 individual strategy write-ups, organized by the six recurring strategy families rather than by name. Nearly every strategy in the book is a variant of one of these families; knowing the family's construction, adjustment, and exit logic lets a trader reconstruct any specific named strategy (e.g., a Long Put Condor or a Bear Call Ladder) from its outlook and volatility tag alone.

## Rules

**1. Vertical spreads (bull/bear call/put spreads, ladders).** Construction: buy and sell same-type options, same expiration, different strikes; a ladder adds a third strike to the same side. Selection: strikes typically $2.50–$5.00 apart, ≤1 month to expiration for credit (income) verticals, longer for debit (capital-gain) verticals. Adjust: none specified — Cohen treats verticals as fixed-risk trades held to expiration or unwound in full. Exit: buy back the short leg and sell the long leg together ("unravel"); advanced traders may leg out partially to bank incremental profit, converting the position into a naked single-leg exposure. Risk: max risk = strike gap − net credit (credit vertical) or = net debit (debit vertical); always fully capped.

**2. Calendar and diagonal spreads.** Construction: buy a long-dated option (near-the-money for calendar, deep ITM for diagonal) and sell a short-dated option against it, same strike (calendar) or higher/lower strike (diagonal). Selection: long leg 6+ months out, short leg ≈1 month, re-sold each cycle. Adjust: at each short-leg expiration, if the stock is below the short strike, let it expire worthless and sell another short-dated option at the same or a rolled-up strike; if above the short strike, the short leg is assigned — sell the long leg to fund buying stock at market and delivering at the strike. Exit / caveat: never exercise the long leg early (forfeits remaining time value); a calendar (near-the-money long leg) can lose money even on a big correctly-directional move because the long leg's delta lags the stock — the diagonal's deep-ITM long leg (higher delta) exists specifically to fix this.

**3. Straddles, strangles, and their variants (strip/strap/guts, short versions, synthetic straddles).** Construction: buy (long) or sell (short) a call and a put on the same underlying and expiration, same strike (straddle) or different strikes (strangle); guts uses ITM strikes for both legs; strip/strap add an extra put or call respectively to bias direction. Selection: enter long volatility trades before an anticipated volatility-expanding event with volatility currently low; enter short volatility trades when volatility is currently high and expected to contract. Adjust: none specified for long versions (defined-risk, ride to expiration or the volatility event); short (naked) versions require a hard stop-loss on the underlying since risk is uncapped in one or both directions. Exit: close both legs together, or for a directional winner in a long straddle/strangle, sell the winning leg first and let the other expire worthless.

**4. Butterflies and condors (long/short call/put butterfly, condor, iron butterfly/condor, modified butterfly).** Construction: 3 evenly-spaced strikes for a butterfly (buy outer 2, sell inner 2× — or the reverse for short versions), 4 evenly-spaced strikes for a condor (buy 2 outer, sell 2 inner); iron versions mix puts and calls for the same payoff shape; a modified butterfly moves the middle strike closer to one wing to bias direction. Selection: ≤1 month to expiration, all strikes equidistant, no anticipated news event. Adjust: Cohen flags every member of this family as "awkward to adjust" — the standard guidance is to hold to expiration or unwind the full structure rather than leg-adjust. Exit: unravel all legs together; can be closed just before expiration to capture time-decay profit while avoiding pin risk at the strikes. Risk: fully capped both directions; maximum reward = strike gap − net debit (long versions) and is realized only if the stock finishes exactly at (butterfly) or between (condor) the middle strike(s).

**5. Ratio spreads and backspreads.** Construction: unequal numbers of long and short same-type options at two strikes, ratio of 2:1 or 3:2. A backspread buys more than it sells (net long, uncapped reward, capped risk); a ratio spread sells more than it buys (net short, uncapped risk, capped reward). Selection: enter backspreads expecting a large directional move with rising volatility; compare 2:1 vs. 3:2 constructions by upper/lower breakeven and max risk, not just net credit received — a cheaper net-debit 2:1 can dominate a net-credit 3:2 that pushes breakeven further out. Adjust: none specified. Exit: unravel all legs, or leg out of one bought option to convert a backspread into a simple vertical spread if the volatility thesis fails.

**6. Synthetics and collars (collar, synthetic call/put, synthetic straddle, synthetic future, combo, box).** Construction: reproduce a stock or straddle payoff using only options (synthetic call/put/straddle/future), or protect a long stock position with a long put financed by a short call (collar). Selection for a collar: buy stock, buy an ATM or OTM put sized to your maximum acceptable loss, sell an OTM call to finance the put; best entered in high-volatility, bullish-sentiment conditions when calls are richer than puts, over a 12–18 month horizon. Adjust: none specified — collars and synthetics are held near-to-expiration by design. Exit: for a collar, let the short call get exercised at expiration for the planned maximum gain, or let it expire worthless and roll a new call; for synthetics, unwind all legs simultaneously since the position only replicates another instrument's payoff and has no independent adjustment logic.

## Risk

No family in this playbook uses percent-of-equity or dollar-based position sizing; every risk figure is expressed as a formula in strike differences and net premium (e.g., vertical max risk = strike gap − net credit; butterfly/condor max risk = net debit paid). The trader must supply their own sizing overlay. Uncapped-risk families (naked short straddles/strangles, ratio spreads, ladders) require an independent stop-loss on the underlying stock price since none of Cohen's formulas define a maximum dollar loss for these positions — that is the single largest gap this playbook does not close.

## Caveats

Cohen's own text repeatedly warns that butterflies and condors are "awkward to adjust," meaning families 4 above are best treated as static, hold-to-expiration trades rather than dynamically managed positions — traders wanting active leg-by-leg adjustment tactics (rolling one side, converting a butterfly into a condor mid-trade) should consult a book specifically focused on position adjustment. "One tick" and "one month" conventions throughout reflect pre-2008, wider-tick-size markets and should be rescaled to current minimum price increments and typical bid/ask spreads before being applied literally.
