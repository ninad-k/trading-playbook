---
title: "The Stock Trader: How I Make a Living Trading Stocks"
author: Tony Oz
year: 2000
slug: tony-oz-how-i-make-a-living-trading-stocks
tier: A
category: Day Trading & Scalping
tags: [support-resistance, day-trading, scanning, level-ii, risk-reward-ratio, trading-diary, nasdaq]
difficulty: beginner
doc_type: book
pages: 146
one_liner: "A real-time, 116-trade trading diary from the April 2000 Nasdaq crash showing a long-only support/resistance day-trading system, its scan formulas, and every stop and target used."
related: [jack-schwager-stock-market-wizards, reminiscences-of-a-stock-operator-by-edwin-lefevre-to-jesse-livermore, elder-alexander-trading-for-a-living, come-into-my-trading-room-elder-alexander, john-j-murphy-charting-made-easy]
source_file: "Tony Oz - How I Make A Living Trading Stocks.pdf"
---

## Overview

This is a real-time trading diary, not a conventional instructional text. Tony Oz, a short-term equities trader, accepted a public challenge from the organizers of the International Online Trading Expo to open a fresh $50,000 brokerage account with a broker he had never used (MB Trading) and document every trade for four weeks — March 20 to April 14, 2000 — including entries, exits, stop placements, and running profit-and-loss, published without cherry-picking results after the fact. The four-week window happened to coincide with the start of the dot-com Nasdaq crash, so the diary doubles as a case study in trading a long-only, support/resistance-based day-trading system through a fast, sustained decline. The book assumes readers already know the setups and Level II mechanics from Oz's earlier book, Stock Trading Wizard, and functions as a worked application of that system rather than a from-scratch course.

## Core thesis

A simple, disciplined trading system — built entirely on support and resistance, with a fixed risk/reward filter and predefined stop-loss rules — can be traded profitably on the long side even during a severe bear market, provided the trader follows the plan without deviation. Oz repeatedly frames the book's central lesson as behavioral rather than technical: his stated "secret to success" is treating every trade as if he had to justify it afterward to his own students, which forced consistent rule-following. The specific chart patterns matter less than the discipline of predefining entry, stop, and target before pulling the trigger, and of recording and reviewing every trade afterward.

## Key concepts

- **Support and resistance as the entire system** — Oz states plainly that his system is "made of two words: Support and Resistance," deliberately avoiding indicators beyond a simple moving average overlay.
- **Reversal Day** — a stock opens, trades meaningfully lower, then reverses and breaks out to a new intraday high on above-average volume; used as a long-entry trigger.
- **Constant watch list** — a maintained roster of roughly 24–40 liquid (1.5M+ average daily volume), typically higher-priced (generally over $50/share), low-dividend stocks tracked every day; Oz reports it generated the majority of his trades during the challenge.
- **Overnight scan vs. real-time scan** — a batch of formula-driven screens run after the close (for next-day candidates) and again intraday (for live setups), each with explicit volume, price, and range criteria (see Rules and setups).
- **Risk/reward filter** — a trade is only taken if the potential reward is at least three times the risk (e.g., risking 1 point to make 3); trades that don't meet this ratio are skipped regardless of how good the pattern looks.
- **Trailing stop discipline** — once a trade is working, the stop is walked up (for longs) behind new support levels rather than left at the original level, to lock in profit without exiting the position early.
- **Breakeven syndrome (implicit)** — moving a stop to breakeven as soon as a position is "in the money" (a volatility-dependent threshold that differs per stock) so a winner never turns into a loser.
- **Basket diversification** — pre-built sector baskets (biotech, semiconductors, internet, telecom, etc.) used to trade a "hot sector" as a group rather than picking single names.
- **Win/loss ratio vs. performance table** — Oz explicitly warns that win rate alone (64.6% in this book) is a weak metric; he instead tracks a monthly profit/loss distribution table to see whether big winners meaningfully outweigh big losers.

## Rules and setups

Oz discloses four scan formulas verbatim (originally published in Stock Trading Wizard) and a small set of concrete entry/exit rules:

1. **Volume Spike Scan**: average volume > 750,000 shares; today's volume > 1.5x its 20-day average; net change ≥ 5/8 point; price between $40–$200.
2. **Breakout Scan**: average volume > 400,000 shares; today's volume > 1.7x average; net change ≥ 5/8 point; price $40–$200; last trade must be a four-week high.
3. **Pullback Swing Trade Scan** (his primary overnight scan): average 20-day volume > 350,000 (also stated as >750,000 for the general version); the stock has closed lower for three straight days (each day's close below the prior day's close); the last trade is above the prior day's low; price $40–$200. Coded as: `VolAvg20 > 350,000 AND Last > PrevLow AND PrevClose1 < PrevClose2 < PrevClose3 < PrevClose4`.
4. **Power Scan**: average volume > 350,000 shares; today's volume > 1.5x average; net change ≥ 5/8 point; price $40–$200; last trade in the top 13% of the day's range.
5. **Entry — support-level buy**: identify intraday or multi-day support (a price level tested and held more than once); buy on a confirmed bounce off that level.
6. **Entry — breakout buy**: buy once price trades above the prior day's high (or a defined resistance level); alternatively buy the pullback to that former-resistance-now-support level after the breakout.
7. **Risk/reward filter**: only take a setup where the reward target is at least 3x the dollar/point risk to the stop; otherwise pass on the trade.
8. **Stop-loss placement** (use whichever applies): below today's low; below yesterday's low; below a secondary intraday support level; below a multi-day intraday support level; below a 50% retracement of the last rally; or below a relevant index's day low/support level.
9. **Trailing stop**: once price moves favorably, walk the stop up behind the newest local support (for longs), and once a position is meaningfully "in the money" (a volatility-scaled threshold, e.g., 1–2 points for a low-volatility stock vs. much more for a high-volatility one), move the stop to breakeven at minimum.
10. **Time stop**: exit a position that has stagnated too long, to avoid tying up capital at zero opportunity cost.
11. **No shorting**: for the duration of the diary, Oz traded long-only by the challenge's own rule, to prove the system could work on the long side even in a downtrend.

## Risk and money management

Position and account-level risk rules are stated explicitly at the outset: risk capital fixed at $50,000, with margin extending buying power to $100,000; no single non-index position may exceed $30,000 (aggressive) or roughly $25,000 (typical), to avoid concentration, though index-tracking products (SPY, QQQ, DIA) are exempt from this cap since they are inherently diversified. Realized profits are swept out of the account at the end of each week (no compounding within the challenge), and losing weeks are not replenished — the account trades back up to $50,000 before further withdrawals resume, capping the compounding of losses. Per-trade risk is governed by the 3:1 reward-to-risk filter and the stop-placement menu above; no fixed percent-of-equity per-trade cap is stated beyond the implicit ceiling from position-size limits. Over the four-week test, the account returned $16,277.25 (32.55%) on $50,000 while the Nasdaq fell 30.78% (1,476 points) over the same span — a result Oz attributes entirely to discipline in following the stop and target rules rather than to a novel edge.

## Psychology and discipline

The book's psychological throughline is rule adherence under pressure. Oz's recurring self-check — imagining having to explain each trade's entry, risk management, and exit to his own trading students — is offered as a practical discipline tool. He documents his own emotional reactions in real time (nervousness before the first trade, frustration on days when no setup triggered, the temptation to chase gapped-up stocks) and repeatedly stops himself from deviating from predefined stops and targets even when a trade "should" have made more (e.g., manually exiting a winning trade at a planned level only to watch the stock continue higher after a Fed announcement). He explicitly warns that a stop-loss order does not guarantee an exit at the stop price during a fast market (citing real examples of stocks gapping 50+ points below stop levels in minutes) and frames this as a reason to size positions conservatively rather than to trust stops blindly.

## Chapter map

- Ch 1 — The Challenge: trading station setup, choosing a broker, and the $50,000/four-week rules of engagement.
- Ch 2 — Setting the Rules: risk management guidelines, bar and candlestick chart basics, support/resistance and supply/demand framework, sourcing trades (watch list, overnight scan, intraday scan).
- Ch 3 — Evaluating Risk/Reward Ratio: the 3:1 filter, stop-loss placement menu, and the final candidate list for Day One.
- Ch 4–23 (Days One–Twenty) — the trading diary itself: each chapter narrates that day's market context, scan results, and every trade executed with entry, stop, target, and outcome, spanning the initial Nasdaq weakness through the April 2000 crash.
- Ch 24 — Thank You, But No Champagne for Me: closing reflections on the final trading day.
- Ch 25 — The Secret to Success: discipline as the core lesson, plus the challenge's aggregate results (116 trades, win/loss ratio, performance-distribution methodology).
- Ch 26 — Challenge Summary and Epilogue: final P&L ($16,277.25 during the challenge; $28,133.75 including two post-challenge days), comparison to the Nasdaq's decline.
- Bonus Pack — a condensed checklist of the book's tips, entry-point types, and time-of-day trading patterns, plus an in-depth AMZN case study.
- Appendixes A–H — trade-record and performance-table templates; building a Constant watch list; sector baskets; the four scan formulas; Level II quote mechanics; order-routing systems (SOES, SelectNet, ISLD, ARCA); MBTrader order types; further resources and a glossary.

## Strengths and caveats

The book's core strength is radical transparency: every trade (116 in total) is shown with real entry/exit prices, dated and time-stamped, including losing trades and moments where Oz second-guesses himself in hindsight — a rarer format than most curated "best trades" retrospectives. The scan formulas and stop-placement rules are concrete and immediately usable.

Major caveats: this is a single trader's four-week track record during one specific, unusually volatile historical episode (the early dot-com crash), not a multi-year backtest — 116 trades is a small sample, and the book itself does not claim statistical robustness beyond that window. All prices are quoted in pre-decimalization fractions (e.g., "16 1/2"), and the order-routing mechanics (SOES, SelectNet, ISLD, ARCA specifics) reflect Nasdaq market structure from 2000 that has since been substantially replaced by different execution systems and decimalized pricing — the tactical order-routing appendixes are the most dated part of the book. The trading system itself is intentionally simple (support/resistance plus volume/range scans) and assumes familiarity with setups detailed in Oz's earlier book; readers looking for original chart-pattern theory will find mostly application rather than derivation here.

## Who should read it

Best suited to short-term equity/day traders who want to see a rules-based support-and-resistance system applied trade-by-trade in real market conditions, including how a disciplined trader handles a losing trade, a missed entry, or a stop that fills far worse than expected. Less useful as a first introduction to chart patterns or Level II mechanics (better covered in dedicated texts), and the specific order-routing appendixes are primarily of historical interest given how Nasdaq market structure has changed since 2000.

## Related books in this library

- [[jack-schwager-stock-market-wizards]] — interview-format complement covering how other short-term and swing traders think about risk and discipline.
- [[reminiscences-of-a-stock-operator-by-edwin-lefevre-to-jesse-livermore]] — Oz's own recommended reading; a classic narrative on speculation psychology that pairs with this book's real-time diary format.
- [[elder-alexander-trading-for-a-living]] — a more systematic treatment of the psychology, method, and money-management triad this diary illustrates anecdotally.
- [[come-into-my-trading-room-elder-alexander]] — another day-in-the-life-style trading text with a similar diary/case-study structure.
- [[john-j-murphy-charting-made-easy]] — a more thorough treatment of the chart patterns (double tops/bottoms, triangles) Oz references only briefly via his glossary.
