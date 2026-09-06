# Xetra XXL: The New Dimension: the trader's summary

*Deutsche Börse sales deck explaining Xetra XXL, its periodic crossing-auction block-trading platform for large stock orders on DAX/MDAX/TecDAX names.*

**Deutsche Börse AG** · 2001 · Quant, Microstructure & Academic Research · advanced

*Source coverage: partial. PDF pages inspected: 10-11, 29 (the crossing-auction schedule, order-book design and the fee model). These are study notes, not verified trading results.*

## Summary

This is a Deutsche Börse internal/client presentation (PowerPoint deck) introducing Xetra XXL, an exchange-based, fully electronic block-trading venue launched to pull large-order ("block") volume away from telephone trading, brokered "upstairs" markets, and crossing networks like POSIT and E-Crossnet. It is not a trading strategy document; it explains the market model, transaction cost theory behind block trading, and the fee structure of this specific 2001-era German market-structure product.

## Key points

- Breaks transaction costs into explicit costs (commissions/fees), spread, market impact, timing costs, and opportunity costs — the framework used to justify why block trading needs a separate venue.
- Xetra XXL uses a completely closed order book with periodic crossing auctions (originally every 15 minutes, 34 crossings per trading day) rather than continuous price discovery.
- Trades execute at the current Xetra reference-market midpoint price, not at an independently discovered price — no autonomous price formation happens inside the block segment.
- A "trigger corridor" around the midpoint prevents manipulation: only a market order or a marketable limit order within the corridor advances the auction from pre-call to call phase.
- Only DAX, MDAX, and TecDAX-listed instruments were eligible for Xetra XXL trading.
- Fee model rewards liquidity supply: orders that trigger a call phase pay no transaction fee; orders that trade during a call phase pay 0.02% (2 basis points) of trade value, capped at €1,000 (cap reached at €5 million order size).
- Access required members/clearing banks to hold a minimum €10 million security deposit under the exchange's exposure-monitoring regime.
- Settlement and contract notes use the underlying instrument's original identifier (WKN/ISIN), even though trades are booked under an artificial "BC-" prefixed block-crossing identifier.

## Actionable rules

None given. This is a market-structure/venue description, not a trading system — there are no entry, exit, or position-sizing rules for an individual trader. The only "numbers" of note are structural: 15-minute crossing intervals, a 2bp/€1,000-cap fee schedule, and the €10 million minimum deposit for direct access.

## Caveats

Historical and highly institutional: this describes a specific Deutsche Börse product as it existed around 2001, aimed at large block traders and clearing members, not retail or even most active individual traders. Xetra XXL as a specific platform has since been superseded by other block-trading mechanisms; treat the numbers (crossing frequency, fee levels, deposit minimum) as historical rather than current. Useful mainly as a case study in how exchanges structure block/crossing markets and transaction-cost trade-offs.

## Who it is for

Readers interested in market microstructure and exchange design — how large orders are matched away from continuous trading to minimize market impact — rather than traders looking for a strategy.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: market-microstructure, block-trading, xetra, crossing-network, transaction-costs, exchange-mechanics
