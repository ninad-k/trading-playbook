---
author: Coders' Guru
category: Trend Following & Mechanical Systems
difficulty: intermediate
doc_type: manual
one_liner: Free web-published MQL4 tutorial series covering syntax through building
  a first custom indicator, Expert Advisor, and script in MetaTrader 4.
pages: 258
related: []
reviewed_pdf_pages: 9-10 and the lesson chapters checked against the note's description
  of the language and examples
slug: mql-4-metatrader-4-development-course
source_file: Mql 4- Metatrader 4 Development Course.pdf
source_review: partial
tags:
- mql4
- metatrader
- expert-advisor
- custom-indicator
- automation
- programming
tier: B
title: MQL4 - MetaTrader 4 Development Course
year: 2006
---

## Summary

A lesson-by-lesson programming course teaching MQL4, the C-like language used to automate trading in MetaTrader 4. It is not a strategy book; it teaches the mechanics of writing Expert Advisors (EAs), Custom Indicators, and Scripts so a trader can code rules instead of trading manually. Lessons progress from syntax, data types, operators, and loops through functions and preprocessor directives, then apply those fundamentals to build a first custom indicator, a first Expert Advisor (four parts), and a first script, finishing with chart templates.

## Key points

- MQL4 has three output types: Expert Advisors (automate order entry/management), Custom Indicators (display only, cannot trade), and Scripts (run once on demand).
- Syntax closely follows C/C++: free-form whitespace, `//` and `/* */` comments, identifiers up to 31 characters, case-sensitive names, and reserved words that cannot be used as identifiers.
- Code compiles the "hard way" via the command-line `metalang.exe` or the "easy way" via the built-in MetaEditor IDE (F5 to compile, integrated error tab, F1 help).
- Core data types (int, double, string, bool, color, datetime), expressions, and control flow are taught before any trading code appears.
- The first custom indicator example computes a simple volatility measure (high minus low) purely as a teaching exercise, not a usable signal.
- An EA is framed as the automation fix for the limits of manual chart-watching, coded to place, modify, and close orders without constant monitoring.
- Building the first EA spans four lessons, progressively adding order logic and stops; later lessons cover a first Script and chart templates.

## Actionable rules

None given — this is a programming reference, not a trading system. It teaches the tools (MQL4 syntax, indicator/EA/script structure) needed to implement a trader's own entry, exit, and sizing rules in code.

## Caveats

A mid-2000s MetaTrader 4 web tutorial (metatrader.info); syntax and IDE details apply to classic MQL4, not MQL5, and predate later MetaEditor changes. No trading edge or strategy is presented — the example indicator is explicitly not a usable signal. As a sequence of short web lessons, coverage of any one topic is brief; best used as a primer before the official MQL4/MQL5 reference docs.

## Who it is for

Traders with little or no programming background who want to automate a strategy in MetaTrader 4 and need a plain-language, example-driven starting point before diving into MetaQuotes' own documentation.
