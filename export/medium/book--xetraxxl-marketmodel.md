# Xetra XXL Market Model: the trader's summary

*Deutsche Börse’s 2001 model specifies periodic anonymous block crossings at the midpoint of a liquid Xetra reference market.*

**Deutsche Börse** · 2001 · Quant, Microstructure & Academic Research · advanced

*Source coverage: full. PDF pages inspected: 1-12. These are study notes, not verified trading results.*

## Summary

Deutsche Börse’s dated 13 September 2001 document describes Xetra XXL Block Crossing for large DAX, MDAX, and NEMAX equity orders (pp. 2-4). The model is order-driven but does not discover its own price: a crossing uses the current midpoint between the best bid and ask in a liquid reference market. Orders execute by volume/time priority during a fixed number of periodic crossings (pp. 3, 8-10). The crossing book is closed, and participants cannot see order side, size, or limit; counterparties remain anonymous in the trading system until the end-of-day confirmation process described by the source (pp. 3-4). The document presents a proposed market model whose final binding form depended on amendments to Frankfurt Stock Exchange rules (p. 3).

## Key points

- Each security has a minimum order quantity, with further volume entered in multiples of a defined minimum tradable unit (pp. 3-5).
- Only market and limit orders are supported; limits are execution conditions rather than inputs to price discovery (pp. 3, 5).
- Orders are good for the trading day. Stop orders, execution restrictions, trading restrictions, volatility interruptions, market-order interruptions, and order-book balancing phases are absent from this model (pp. 4-6).
- A crossing period has a pre-call and a call with a random end. The call can be triggered only by a market order or a limit order meeting the exchange’s midpoint-based threshold (pp. 4, 8).
- Execution occurs only when the reference spread is no wider than the instrument’s allowed maximum and the midpoint is not stale beyond a predefined time (pp. 3, 10).
- Nonexecuted and partially executed orders roll to the next crossing period, then are deleted at day-end (p. 10).

## Actionable rules

1. Submit only a market order or a limit whose buy price is at least the midpoint, or whose sell price is no more than the midpoint, if execution at the current crossing is desired (pp. 8, 10).
2. Account for volume/time priority: changing volume or limit in a way that harms other orders’ priority assigns the modified order a new time priority and order number (p. 5).
3. Check that the reference-market spread and quote age satisfy the crossing safeguards; otherwise no crossing occurs (p. 10).

## Caveats

This is a historical, venue-specific proposal and does not establish current Xetra rules or empirical execution quality. Several quantities—the crossing schedule, minimum order size, tradable unit, maximum reference spread, and maximum quote age—are described as predefined but are not numerically supplied. The model includes no designated liquidity-provider role.

## Who it is for

Institutional traders and market-structure readers studying block execution on electronic exchanges.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: xetra, block-trading, market-microstructure, execution
