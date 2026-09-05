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

**1. Vertical spreads (bull/bear call/put spreads, ladders).** Construction: same-type options, same expiration, different strikes. Selection: strikes $2.50–$5.00 apart; ≤1 month for credit verticals, longer for debit. Adjust: none — fixed-risk, held to expiration or unwound in full. Exit: buy back the short leg and sell the long leg together; advanced traders may leg out partially, accepting naked exposure. Risk: capped at strike gap − net credit, or net debit paid.

**2. Calendar and diagonal spreads.** Construction: long-dated option (near-the-money for calendar, deep ITM for diagonal) plus a short-dated option sold against it, same strike (calendar) or different (diagonal). Selection: long leg 6+ months, short leg ≈1 month, resold each cycle. Adjust: below the short strike, let it expire and resell; if assigned, sell the long leg to fund buying stock and delivering at the strike. Exit/caveat: never exercise the long leg early; the calendar's near-the-money long leg can still lose on a big correct-direction move since its delta lags the stock — the diagonal's deep-ITM leg fixes this.

**3. Straddles, strangles, and variants (strip/strap/guts, short/synthetic versions).** Construction: a call and a put, same strike (straddle) or different (strangle); guts uses ITM strikes both legs; strip/strap add an extra put or call to bias direction. Selection: buy volatility before an expected volatility event with volatility low; sell volatility when it is high and expected to contract. Adjust: none for long versions; short versions need a hard underlying stop-loss (uncapped risk). Exit: close both legs together, or on a directional winner sell that leg and let the other expire worthless.

**4. Butterflies and condors (incl. iron and modified versions).** Construction: 3 evenly-spaced strikes for a butterfly (buy outer two, sell inner two), 4 for a condor; iron versions mix puts and calls for the same shape; modified butterflies shift the middle strike to bias direction. Selection: ≤1 month, equidistant strikes, no anticipated news. Adjust: flagged as "awkward to adjust" — hold to expiration or unwind fully. Exit: unravel all legs together, often just before expiration. Risk: fully capped; max reward = strike gap − net debit, realized only at (butterfly) or between (condor) the middle strike(s).

**5. Ratio spreads and backspreads.** Construction: unequal long/short same-type counts at two strikes (2:1 or 3:2). A backspread is net long (uncapped reward, capped risk); a ratio spread is net short (uncapped risk, capped reward). Selection: backspreads for a large move with rising volatility; compare by upper/lower breakeven and max risk, not net credit alone. Adjust: none. Exit: unravel all legs, or leg out of one bought option to convert into a plain vertical.

**6. Synthetics and collars.** Construction: reproduce a stock, straddle, or future payoff using only options, or protect long stock with a put financed by a short call (collar). Collar selection: put sized to maximum acceptable loss, call sold OTM to finance it; best in high-volatility, bullish conditions over 12–18 months. Adjust: none — held near-to-expiration. Exit: let the collar's call get exercised for the planned gain or roll it; unwind synthetics' legs simultaneously.

## Risk

No family uses percent-of-equity sizing; every risk figure is a formula in strike differences and net premium (e.g., vertical max risk = strike gap − net credit). Uncapped-risk families (naked short straddles/strangles, ratio spreads, ladders) need an independent underlying stop-loss, since none of Cohen's formulas cap their dollar loss — the largest gap this playbook doesn't close.

## Caveats

Butterflies and condors are explicitly "awkward to adjust" — treat them as static, hold-to-expiration trades; traders wanting active leg-by-leg adjustment need a dedicated position-adjustment text. "One tick" and "one month" conventions reflect pre-2008, wider-tick markets and should be rescaled to current price increments and spreads.
