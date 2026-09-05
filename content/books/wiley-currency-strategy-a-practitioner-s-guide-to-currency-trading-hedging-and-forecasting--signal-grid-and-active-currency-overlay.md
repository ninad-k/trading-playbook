---
title: "Currency Strategy — Signal Grid and Active Currency Overlay Strategies"
author: Callum Henderson
year: 2002
slug: wiley-currency-strategy-a-practitioner-s-guide-to-currency-trading-hedging-and-forecasting--signal-grid-and-active-currency-overlay
tier: A
category: Forex Mechanics & Macro Drivers
tags: [carry-trade, trend-following, moving-averages, risk-appetite, currency-overlay]
difficulty: advanced
doc_type: system
parent: wiley-currency-strategy-a-practitioner-s-guide-to-currency-trading-hedging-and-forecasting
pages: 235
one_liner: "A four-discipline signal grid gates entries; three named quantitative overlays (differential forward, 32/61/117-day trend-following, carry-trade optimization) size and time the position."
related: [wiley-currency-strategy-a-practitioner-s-guide-to-currency-trading-hedging-and-forecasting, dynamic-trading-by-robert-c-miner, lehman-currency-hedging-in-fixed-income-portfolios]
source_file: "Wiley - Currency Strategy A Practitioner's Guide To Currency Trading, Hedging And Forecasting.pdf"
---

## What it is

Henderson's actionable synthesis for both currency hedgers and speculators, combining a qualifying filter (the signal grid) with three specific, numbered active-management strategies that were academically documented (Bilson, Taylor, LeBaron, Levich and Thomas, Lequeux and Acar) to have produced consistent excess returns while also reducing portfolio risk versus an unhedged benchmark. The same three overlays can be read either as directional speculative trades (long/short a currency pair) or as a variable hedge ratio applied to an underlying currency exposure — the book presents both readings side by side.

## Rules

**1. Signal grid (gate).** Score four independent readings for the currency pair in question, each as buy/sell:
- Currency economics (balance of payments, REER/FEER, productivity, interest-rate differentials)
- Flow analysis (IMM Commitments of Traders report, proprietary bank flow models, TIC/Euro-zone portfolio reports)
- Technical analysis (trend, moving averages, RSI/MACD, Fibonacci/Elliott/Gann levels)
- Long-term valuation (PPP, monetary, interest-rate, balance-of-payments, or portfolio-balance model fair value)

Only put on a major new position when at least 3 of the 4 readings agree. When the grid is inconclusive (Henderson notes this is true most of the time), fall back to the risk-appetite/carry overlay below rather than forcing a trade.

**2. Differential forward strategy (rate-based hedge/trade sizing).**
- If the interest-rate differential is in the hedger's favor (forward points at a discount to spot for the exposure being hedged), hedge ratio = 100%.
- If the interest-rate differential is a cost (forward points at a premium), hedge ratio = 0%.
- Under a symmetrical (50%) benchmark, translate this into overweighting the hedge by 50% when the differential favors the hedger, and underweighting it by 50% when it doesn't.
- As a directional speculative read: be long the higher-yielding currency when its forward is at a discount to spot, flat/short otherwise.

**3. Trend-following overlay (Lequeux and Acar, 1998) — an equally-weighted three-moving-average system.**
- Compute simple moving averages of the spot rate over 32, 61, and 117 days.
- If spot is above all three MAs: hedge 100% of the underlying exposure (or, as a directional trade, be fully long the currency).
- If spot is above exactly two of the three MAs: hedge one-third of the exposure (or hold a one-third-sized long position).
- In all other cases (spot above one or zero of the three MAs): remain unhedged / flat.
- Mirror the same three thresholds for a short/underweight-hedge signal when spot is below the MAs.

**4. Carry-trade optimization (risk-appetite gated).**
- Construct a basket of higher-carry (higher-yielding) currencies to buy, funded by shorting lower-carry currencies.
- Monitor a risk-appetite/instability indicator (built from leverage, credit-spread, and cross-asset correlation data — Henderson's own reference is the "Instability Index").
- **Enter/hold long the carry basket** when the indicator reads risk-seeking or risk-neutral.
- **Take half profit** when the indicator shifts from risk-seeking to risk-neutral.
- **Close the entire position and reverse to short the carry basket** when the indicator moves into risk-averse mode.
- Optional refinement: use a portfolio optimizer to weight the basket toward higher-carry currencies with *lower* volatility and away from lower-carry currencies with *higher* volatility, rather than equal-weighting by yield alone.

**5. Combining the three overlays.** All three can be run concurrently on the same underlying exposure; each was shown (per the cited studies) to add positive expected return individually while reducing volatility relative to an unhedged position, so they are not mutually exclusive alternatives but complementary sleeves of an active-management program.

## Risk

Position sizing under this framework is expressed as a hedge ratio (0%, 33%, 50%, or 100% of the underlying exposure) rather than a fixed percent-of-equity stop-loss figure — the method was designed for institutional currency-overlay and hedging mandates, not standalone speculative position sizing. For speculators adapting the framework directionally, Henderson's general risk rules apply: define entry, exit, and stop levels from the flow and technical evidence before entering, always cut losses, and take fewer, larger, higher-conviction positions rather than many small ones. The carry-trade leg carries acknowledged tail risk — Henderson cites the October 1998 dollar-yen move of roughly 15% in a few days as a reminder that carry trades can suffer sharp, low-warning reversals, which is precisely why the risk-appetite gate (rule 4) exists: it is meant to exit or flip the carry position before a full risk-aversion event, not to eliminate the underlying tail risk.

## Caveats

The strategies are presented as academically documented (largely pre-2000) results; Henderson reports historical outperformance but the book does not include an updated, current-era backtest, and carry-trade dynamics in particular were structurally altered by the near-zero global interest rates that followed the 2008 financial crisis. The trend-following overlay's specific 32/61/117-day windows come from a single cited paper (Lequeux and Acar, 1998) chosen to represent a spread of trader time horizons — they are not derived or re-optimized within this book, and no sensitivity analysis to other window lengths is given. The signal-grid's "3 of 4 agree" threshold is a discipline heuristic, not a statistically validated cutoff. Transaction costs from the differential-forward and trend-following strategies' relatively frequent re-hedging are acknowledged as a consideration but are described only qualitatively ("historically small relative to returns"), without a worked cost model.
