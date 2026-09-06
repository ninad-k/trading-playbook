# Modeling Financial Markets: Using Visual Basic.NET and Databases to Create Pricing, Trading, and Risk Management Models: the trader's summary

*Financial-engineering textbook teaching the Kumiega-Van Vliet trading-system development methodology (research, backtest, implement, manage risk) alongside VB.NET, databases, and exchange API programming.*

**Benjamin Van Vliet and Robert Hendry** · 2004 · Quant, Microstructure & Academic Research · advanced

*Source coverage: partial. PDF pages inspected: 381 and the design-process chapters checked against the note. These are study notes, not verified trading results.*

## Summary

This is a financial-engineering textbook (McGraw-Hill, 2004) using a programming-book structure (VB.NET, arrays, objects, SQL, XML, UML) to teach how automated trading and risk systems are actually built. Chapters 1-2 lay out the "Kumiega-Van Vliet Trading System Development Methodology," combining the software waterfall model with the iterative spiral model into a four-phase process: research/document calculations, back-test, implement, and manage portfolio/risk. The remaining ~300 of 401 pages teach the VB.NET, database, and connectivity/XML/UML skills to execute that methodology. For trading-notes purposes, the highest-value content is the methodology itself, which frames system building as an engineering discipline rather than a set of technical-analysis rules.

## Key points

- Financial engineering combines four disciplines: computer science, quantitative finance, trading strategy, and quality/process development.
- Waterfall model (sequential analysis/design/implementation/testing with a go/no-go gate each phase) forces upfront planning but can't adapt to late-surfacing problems; spiral model (repeated research/plan/implement/test cycles) allows feedback but risks unbounded "scope creep."
- Kumiega-Van Vliet combines both: four phases proceed in a waterfall, each internally cycling through a mini-spiral, with management approving progression at each gate.
- **Phase I — Research/Document**: describe the trading idea in writing; research quantitative methods; prototype in Excel; check profitability before proceeding.
- **Phase II — Back-Test**: gather and clean data; run in-sample/out-of-sample tests (a well-built system performs similarly out-of-sample); check profitability, looping back to Phase I if it fails.
- **Phase III — Implement**: build a vision document (high-level) and scope document (detailed, iteratively revised); build object/program design; program and document; paper-trade and check profitability before going live.
- **Phase IV — Manage Portfolio/Risk**: monitor portfolio statistics; run value-at-risk calculations; document P&L attribution; determine causes of profitability variation — then repeat the whole cycle for continuous improvement.
- Cited estimate: a proprietary automated system from scratch (infrastructure, quant/programmer staff, ≥1 year R&D before the first trade) can require on the order of $10 million; licensing third-party front-end software and connecting proprietary analytics via its API is the less capital-intensive alternative.

## Actionable rules

1. Before coding or committing capital, write a one-paragraph description of the trading idea: market, capital and time horizon, whose capital, success benchmark (e.g., Sharpe ratio), competitive edge, and launch timeline.
2. Always reserve out-of-sample data; require comparable out-of-sample performance before advancing past back-testing.
3. Write separate vision (high-level) and scope (detailed, revised iteratively) documents before implementation, rather than coding directly from an idea.
4. Paper-trade and re-verify profitability after implementation, before committing live capital — recheck profitability at the end of every phase, not just once.
5. After going live, continuously monitor portfolio statistics and VaR, and attribute P&L to specific causes so the four-phase process can repeat.

## Caveats

The book's second half is a VB.NET/ADO.NET/XML programming tutorial tied to now-superseded technology (2003-era VB.NET, specific vendor APIs like MicroHedge and Trading Technologies X_Trader) with limited current relevance. The Chapter 1-2 methodology, however, is technology-agnostic. The book contains no specific trading strategies or entries/exits of its own; "trading strategy" content is limited to the process for developing and testing one.

## Who it is for

Financial engineers, quant developers, and systematic-trading teams who want a structured project-management framework for taking a trading idea from concept through backtesting to live implementation and ongoing risk monitoring, rather than a book of trading signals.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: system-development, financial-engineering, backtesting, automated-trading, vb-net, software-methodology, apis
