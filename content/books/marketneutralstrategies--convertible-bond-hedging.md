---
title: Convertible Bond Delta-Duration Hedge
author: Bruce I. Jacobs and Kenneth N. Levy (editors)
year: 2005
slug: marketneutralstrategies--convertible-bond-hedging
tier: A
category: Quant, Microstructure & Academic Research
tags: [convertible-arbitrage, delta-hedging, market-neutral, fixed-income, arbitrage]
difficulty: advanced
doc_type: system
parent: marketneutralstrategies
pages: 304
one_liner: "Jane Buchan's convertible-bond hedge: buy the convertible, short the delta-weighted amount of stock (and optionally Treasury futures for duration), collecting the standstill spread."
related: [wyser-pratte-guy-risk-arbitrage, paul-wilmott-quantitative-finance]
source_file: "Marketneutralstrategies.pdf"
---

## What it is

A relative-value strategy (Warren Buffett reportedly began his career doing this) that buys a convertible bond and simultaneously sells short the underlying common stock in an amount proportional to the convertible's delta, so that small moves in the stock price no longer move the combined position's value. A more complete version adds a short position in interest-rate futures sized to the convertible's duration, hedging interest-rate risk as well as equity risk. The position earns the "standstill" or cost-of-carry return (coupon income plus short rebate, minus dividends owed on the short) while remaining close to market- and rate-neutral, profiting from the perceived cheapness of the convertible's embedded conversion option relative to the stock and bond markets.

## Rules

1. **Identify the hedge ratios.** For any convertible under consideration, obtain (or compute) its delta — the sensitivity of the convertible's price to a $1 move in the underlying stock (∂C/∂S) — and, for the fuller hedge, its duration/interest-rate hedge ratio (∂C/∂r ÷ C), typically stated as a dollar sensitivity per 100bp rate move. Delta is near 1 when the convertible is deeply in-the-money (its value tracks the stock almost one-for-one) and near 0 when deeply out-of-the-money (it trades like a straight bond), except when bankruptcy risk appears, in which case delta can rise back toward or above 1 even out-of-the-money.
2. **Size the stock short.** Short (delta × conversion ratio) shares of stock for each convertible bond held. Worked example from the book: Staples 5% convertible due 1999, price $965, delta-neutral hedge ratio 0.40, stock at $31.50 → short 12.3 shares of stock per bond ($0.40 of stock short per $1.00 of convertible).
3. **Size the rate hedge (optional, fuller hedge).** Short Treasury note futures in the amount given by the interest-rate hedge ratio. Example: hedge ratio of $2.09 per 100bp shift → short 0.00209 of a five-year Treasury note futures contract per bond held.
4. **Universe filter.** Restrict candidates to convertible issues of at least $100 million outstanding to ensure adequate liquidity for entry, exit and stock-borrow availability (used in the book's own 1989–1996 study, which held ~146 positions on average, equally weighted, rebalanced monthly).
5. **Collect the standstill return.** With the hedge in place and the stock price unchanged, the position earns coupon income on the bond plus the short rebate on the stock-short proceeds, minus any dividends owed to the stock lender. Worked example: $50 coupon + $9.75 short rebate (85% of a 2.96% rate) − $0 dividends = $59.75 on a $965 convertible, a 6.19% annualized standstill return.
6. **Rebalance as delta drifts.** Delta and duration change as the stock price and interest rates move and as time passes; re-hedge (adjust the stock-short and futures-short sizes) periodically — the book's own study rebalanced monthly — to keep the position close to delta- and duration-neutral.
7. **Screen out credit risk before entry.** Do fundamental/credit research on the issuer up front. Avoid convertibles at meaningful risk of becoming "busted" (the issuer approaching bankruptcy), because delta-hedging breaks down exactly when it is needed most in that scenario (see Risk below).
8. **Optional partial hedging.** An investor with a directional view (e.g., expecting falling rates or a rising stock market over time) may deliberately under-hedge delta or duration to retain some of that exposure, accepting reduced neutrality for a directional bet layered on top of the arbitrage.

## Risk

The central risk is a "busted convertible": as an issuer's credit deteriorates toward bankruptcy, the convertible's bond-value floor erodes, its price becomes driven by liquidation/recovery value rather than by the stock price or interest rates, and its delta — instead of falling toward zero as a straight out-of-the-money hedge would predict — rises toward or above 1, meaning the hedger needs to sell far more stock short at exactly the moment the stock is also crashing and other investors are racing to short the same name; uptick-style rules can make it difficult or impossible to add the needed short size in a falling market, leaving the position under-hedged during the worst move. Stock-borrow availability and recall risk are ever-present: harder-to-borrow names can force a buy-in that unwinds the hedge involuntarily. Leverage materially amplifies both return and risk: because the long convertible and its offsetting stock short net close to zero exposure for margin purposes, hedgers can run far higher leverage than a standard 2:1 equity margin account — the book notes some funds held convertible exposure worth up to 13x equity capital — so a small percentage move against an imperfectly hedged position can produce an outsized capital loss. The book's own regression tests found no significant residual exposure to stock or bond market indices in its 1989–1996 sample, suggesting the historical excess return was not simply compensation for un-hedged market beta, but it could not rule out compensation for harder-to-measure liquidity risk.

## Caveats

The favorable results cited (9.06% average annual unleveraged return, ~364bp annualized excess return over Treasury bills, only 19 of 90 months negative) come from a single study covering January 1989–July 1996 using one data source (Value Line Convertibles) and a simplified simulated portfolio (equal weighting, monthly rebalancing, assumed transaction costs); it is presented as evidence the strategy can work, not as a guarantee, and the author explicitly notes the results could reflect an unmeasured liquidity-risk premium rather than a free lunch. Determining the hedge ratio in practice requires software with subjective inputs (assumed future volatility, assumed likelihood of an issuer calling the bond) — different practitioners using the same convertible can compute meaningfully different "correct" hedge ratios, so the rules above should be treated as a framework rather than a fully mechanical algorithm. The uptick-rule friction described (era-specific SEC Rule 10a-1) no longer applies in its original form after 2007–2010 rule changes, though borrow availability and recall risk remain live constraints today.
