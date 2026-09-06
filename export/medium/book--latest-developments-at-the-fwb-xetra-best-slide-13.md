# Latest Developments at the FWB: Reshaping of the Cash Markets: the trader's summary

*Deutsche Börse presentation on the 2003 Frankfurt/Xetra market segmentation overhaul (Prime/General Standard, DAX index family) and the Xetra BEST retail best-execution model.*

**Rainer Riess (Deutsche Börse)** · 2002 · Quant, Microstructure & Academic Research · intermediate

*Source coverage: partial. PDF pages inspected: 5-6, 9-11, 14, 17-18 (the index framework, Best Executor commitment types and the worked execution-price example). These are study notes, not verified trading results.*

## Summary

A December 2002 Deutsche Börse investor/customer presentation (Rainer Riess, Head of Xetra Customers) covering two related market-structure changes at the Frankfurt Stock Exchange (FWB): the 2003 replacement of the old Neuer Markt/SMAX/Prime segmentation with a new two-tier "Prime Standard / General Standard" disclosure framework and its associated index family (DAX, MDAX, TecDAX, SDAX plus 18 sector indices), and the "Xetra BEST" retail order-execution model, which routes small retail orders (up to €52,500) to a "Best Executor" for guaranteed price improvement over the standing Xetra order book, with automatic fallback into the regular order book if no improvement is available.

## Key points

- Prime Standard requires quarterly reports, IAS/US-GAAP accounting, an investor-relations calendar, and bilingual (German/English) ad hoc disclosure; General Standard requires only the legal minimum (annual/half-yearly reports, German-only ad hoc disclosure).
- From 2003, index membership is decoupled from market segment and instead driven by market capitalization/turnover within Prime Standard: DAX (30 largest), MDAX and SDAX (50 each, "classic" sectors), TecDAX (30, technology sector) — plus 18 Prime sector indices and the broad CDAX/All Share.
- Xetra BEST launched 3 September 2002 with 3 "Best Executors" and 2 "Order Flow Providers," averaging about €6.76 million volume and 1,380 transactions per day at that time.
- Xetra BEST execution logic: a customer order is only executed against a Best Executor if the price is strictly better than the best price already in the Xetra order book; otherwise it is routed straight into the regular order book. Orders larger than the quoted Best size, or above the maximum eligible size, are also routed to the regular book.
- Best Executor commitments come in two types: Type A (already a Designated Sponsor, no minimum monthly fee/contract term) and Type B (not a Designated Sponsor, minimum €50,000/month transaction fee, 24-month minimum contract).
- Worked example in the deck: a 500-share market buy order gets a volume-weighted execution price of about €54.43 blended down to a "Best Price" of €54.42 — a one-cent price improvement versus the top of the visible order book.

## Actionable rules

None — this is a market-structure/venue-rules briefing, not a trading strategy document. Its practical relevance is informational:

1. On Xetra, retail-size orders (historically up to €52,500) routed through a Best-Executor-enabled broker are, by design, guaranteed either a price at or better than the standing order book, or automatic fallback execution in the order book itself.
2. When trading German equities/indices, index membership (DAX/MDAX/SDAX/TecDAX) is determined by Prime Standard listing plus market cap/turnover ranking, not by the older, now-defunct Neuer Markt/SMAX segment labels.

## Caveats

Entirely dated to the German equity market's 2002-2003 segmentation reform; the "Neuer Markt," SMAX, and this specific version of Xetra BEST's fee schedule and size caps no longer reflect the current market. Contains no content applicable to Forex, futures, or non-German equities, and no discretionary or systematic trading guidance. Useful only as historical/reference context on exchange market structure and best-execution mechanics.

## Who it is for

Readers researching European equity market microstructure history or how exchange-level best-execution routing worked in the early 2000s; not relevant to active trading strategy.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: market-structure, xetra, frankfurt-stock-exchange, market-microstructure, order-execution, best-execution, index-rules
