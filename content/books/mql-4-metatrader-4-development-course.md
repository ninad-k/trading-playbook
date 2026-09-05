---
title: MQL4 - MetaTrader 4 Development Course
author: Coders' Guru
year: 2006
slug: mql-4-metatrader-4-development-course
tier: B
category: Trend Following & Mechanical Systems
tags: [mql4, metatrader, expert-advisor, custom-indicator, automation, programming]
difficulty: intermediate
doc_type: manual
pages: 258
one_liner: "Free web-published MQL4 tutorial series covering syntax through building a first custom indicator, Expert Advisor, and script in MetaTrader 4."
related: []
source_file: "Mql 4- Metatrader 4 Development Course.pdf"
---

## Summary

A lesson-by-lesson programming course teaching MQL4, the C-like scripting language used to automate trading in MetaTrader 4. It is not a trading-strategy book; it teaches the mechanics of writing Expert Advisors (EAs), Custom Indicators, and Scripts so a trader can code up their own rules rather than trade manually. Lessons progress from basic syntax, data types, operators, and loops through functions, variables, and preprocessor directives, then apply those fundamentals to build a first custom indicator (three parts), a first Expert Advisor (four parts), and a first script, finishing with a lesson on chart templates.

## Key points

- MQL4 has three output types: Expert Advisors (automate order entry/management), Custom Indicators (technical-analysis display only, cannot trade), and Scripts (run once on demand, no indicator access).
- Syntax closely follows C/C++: free-form whitespace, `//` and `/* */` comments, identifiers up to 31 characters, case-sensitive names, and a fixed list of reserved words that cannot be used as identifiers.
- Code can be compiled the "hard way" via the command-line `metalang.exe` compiler or the "easy way" via the built-in MetaEditor IDE (F5 to compile, integrated error tab and F1 help lookup).
- Core data types (int, double, string, bool, color, datetime), operators/expressions, and control flow (loops, if/else, switch) are taught before any trading code is introduced.
- The first custom indicator example computes a simple volatility measure (high minus low) purely as a teaching exercise, not a usable signal.
- An EA is framed as the automation solution to the limits of manual chart-watching: it can place, modify, and close orders using coded rules without the trader monitoring the terminal continuously.
- Building the first EA is spread over four lessons, progressively adding order logic, stops, and refinements.
- Later lessons cover writing a first Script and working with chart templates for reusing chart/indicator setups.

## Actionable rules

None given — this is a programming reference, not a trading system. It teaches the tools (MQL4 syntax, indicator/EA/script structure) a trader would use to implement their own entry, exit, and money-management rules in code.

## Caveats

The material is a mid-2000s MetaTrader 4 web tutorial (metatrader.info); syntax and IDE details apply to classic MQL4 (not MQL5) and predate later MetaEditor and language changes, so some specifics may be outdated for current MT4/MT5 builds. No trading edge, backtest, or strategy is presented or implied — the example indicator is explicitly described as not useful for trading. Because it is written as a sequence of short web lessons, coverage of any one topic is brief; it is best used as a first-pass primer before consulting the official MQL4/MQL5 reference documentation for production code.

## Who it is for

Traders with little or no programming background who want to automate a strategy in MetaTrader 4 — build Expert Advisors, custom indicators, or one-off scripts — and need a plain-language, example-driven starting point before diving into MetaQuotes' own language documentation.
