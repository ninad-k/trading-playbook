---
title: Filtering False Breakouts
author: Kathy Lien
year: 2006
slug: day-trading-the-currency-market--filtering-false-breakouts
tier: A
category: Day Trading & Scalping
tags: [forex, day-trading, breakout, trend-following, 20-day-high-low]
difficulty: intermediate
doc_type: system
parent: day-trading-the-currency-market
pages: 259
one_liner: "A trend-continuation breakout that waits for a shakeout (a pullback to a fresh 2-day extreme) before re-entering in the direction of a fresh 20-day high or low, aiming to filter out weak-handed traders before the real move."
related: [day-trading-the-currency-market, day-trading-the-currency-market--inside-day-breakout]
source_file: "Day Trading the Currency Market.pdf"
---

## What it is

This strategy targets strongly trending markets that make a new 20-day extreme, then pull back and briefly reverse (taking out a short-term 2-day extreme, which flushes out weaker positions), before resuming the original trend and re-breaking the 20-day extreme. It is designed to have a high success rate because it enters after weaker traders have already been shaken out and only if the market proves the original breakout was real by pushing to a new high (or low) again within a short window.

## Rules

**Long setup**:
1. Identify a currency pair making a new 20-day high.
2. Watch for the pair to reverse over the following three days and make a new two-day low.
3. Buy the pair if it then retakes the 20-day high within three days of that two-day low.
4. Place the initial stop a few pips below the two-day low identified in step 2.
5. Protect profits with a trailing stop, or take profit at double the amount risked.

**Short setup** (mirror image):
1. Identify a currency pair making a new 20-day low.
2. Watch for the pair to reverse over the following three days and make a new two-day high.
3. Sell the pair if it trades below the 20-day low within three days of that two-day high.
4. Risk up to a few pips above the two-day high identified in step 2.
5. Protect profits with a trailing stop, or take profit at double the amount risked.

Worked examples (GBP/USD, USD/CAD, USD/JPY daily charts) show large realized gains (up to ~700+ pips) when a two-bar trailing stop was used instead of taking the fixed 2R target, at the cost of giving back some open profit versus locking in the smaller fixed target.

## Risk

The initial stop is set at the two-day extreme identified during the pullback, so risk size varies by trade (it is not a fixed pip count like several of the book's other strategies) and depends on how deep the shakeout pullback was. The strategy offers a choice at the 2R mark between locking in a fixed double-risk profit or switching to a trailing stop (e.g., a two-bar low/high) to capture a larger trend move — the book's examples show the trailing-stop approach capturing substantially more profit in strongly trending conditions, at the cost of increased variance.

## Caveats

Because the setup requires a specific three-stage sequence (new 20-day extreme, 2-day reversal extreme, re-break of the 20-day extreme within three days), valid setups are relatively infrequent compared to simpler breakout rules. The three worked examples are hand-selected illustrations from 2004–2005, not an audited backtest of the 20-day/2-day/3-day parameter combination across a broader sample or across currency pairs. As with the other technical strategies in the book, no slippage, spread, or commission is modeled in the reported pip results.
