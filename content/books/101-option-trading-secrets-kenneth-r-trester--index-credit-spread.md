---
title: The Index Credit Spread (Trester)
author: Kenneth R. Trester
year: 2004
slug: 101-option-trading-secrets-kenneth-r-trester--index-credit-spread
tier: A
category: Options, Futures & Derivatives
tags: [options, credit-spread, index-options, naked-writing, risk-management]
difficulty: intermediate
doc_type: system
parent: 101-option-trading-secrets-kenneth-r-trester
pages: 336
one_liner: "A defined-risk alternative to naked index-option writing: sell a far out-of-the-money index option and buy a further out-of-the-money option against it, sized around a simulated stop-loss probability."
related: [101-option-trading-secrets-kenneth-r-trester, guy-cohen-the-bible-of-options-strategies, lawrence-g-mcmillan-profit-with-options]
source_file: "101 Option Trading Secrets - Kenneth.R.Trester.pdf"
---

## What it is

The Index Credit Spread is Trester's answer to the danger of naked option writing: instead of writing an uncovered index option (e.g., on the S&P 100/OEX or S&P 500/SPX) and facing unlimited risk, the trader sells a far out-of-the-money index option and simultaneously buys a further out-of-the-money option of the same type and expiration to cap the risk. It is a high-probability, limited-risk credit strategy intended to be held to expiration or closed early once most of the premium has decayed, and is presented as one of the two "best plays" in the book (alongside the diagonal spread).

## Rules

**Structure**: sell (write) one index option that is far out-of-the-money; buy one index option of the same type (call or put) and expiration that is further out-of-the-money, 5, 10, or 15 strike points beyond the written strike.

**Entry criteria**:
1. Use broad-based index options only (e.g., OEX, SPX) — the index diversification reduces the single-stock "surprise volatility" risk that threatens naked equity option writing.
2. Enter with less than three weeks before expiration, so time decay works quickly in the spread's favor.
3. Require a minimum net credit of 0.45 ($45) for the spread.
4. Before entering, run a simulation (not just an at-expiration probability calculator) to confirm at least an 85% probability that the underlying index will not touch the planned stop-loss level during the life of the trade.
5. Do not enter put credit spreads against the prevailing trend — never write put spreads "in the teeth of a decline" (i.e., do not sell downside protection during an active downtrend).

**Worked example given in the text**: with OEX at 423 (Feb 6, 2003), sell the OEX 460 call at 1, buy the OEX 470 call at 0.5, for a net credit of 0.5 ($50). Maximum risk is the 10-point strike distance ($1,000) minus the credit received. The stop-loss was set around 451, which simulation showed had a 96% probability of not being touched.

**Stop-loss placement**: set the stop-loss out-of-the-money, away from (i.e., below, for a call spread) the strike price of the option that was written — not at the strike itself. For a written 400 call, for instance, the stop might sit around 395, giving room before the short strike is threatened.

**Exit rules**:
- Close the position early and take profits if the spread narrows significantly (most of the credit has been captured) before expiration — "get out of the hot seat" as soon as a good profit is available rather than holding to the last cent.
- Exit immediately if the stop-loss level on the underlying index is hit.
- Exit if the market's overall trend reverses against the position, even if the stop-loss has not technically been touched.
- If held to expiration without incident, the position expires worthless and the full credit is kept.

## Risk

Risk is capped at the difference between the two strike prices minus the net credit received (e.g., 10-point spread with a 0.5 credit = 9.5 points, or $950, maximum loss per spread). This is a defined-risk substitute for unlimited-risk naked index writing, but it is still a net-short-premium, high-probability/limited-reward strategy: many small wins can be erased by a single stopped-out loss if the stop-loss discipline is not followed. Margin requirements are lower than naked writing but not zero. The strategy depends on accurate simulation inputs (volatility assumptions); a probability estimate of "85%+" or "96%" is only as good as the model and historical volatility used.

## Caveats

Trester references only a small number of individually cited example trades (not a full audited track record) to support the "excellent track record" claim since the late 1980s; the specific 85%/96% probability figures come from his own proprietary simulator (Option Master®) and are not independently verifiable from the text. The strategy assumes access to simulation software capable of modeling path-dependent stop-loss probabilities, not just a Black-Scholes probability-of-profit-at-expiration calculator; without that tool the stop-loss sizing rule (85% probability) cannot be replicated exactly. Written pre-decimalization-era liquidity conditions on some indexes; bid/ask spreads and commission costs assumed in the examples (e.g., $1,000 spreads charged low round-trip commissions) may not match current-era costs, which are generally lower today.
