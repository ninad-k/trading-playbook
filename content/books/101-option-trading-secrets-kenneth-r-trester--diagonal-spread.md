---
title: The Diagonal Spread (Trester's Credit Time Spread)
author: Kenneth R. Trester
year: 2004
slug: 101-option-trading-secrets-kenneth-r-trester--diagonal-spread
tier: A
category: Options, Futures & Derivatives
tags: [options, diagonal-spread, calendar-spread, credit-spread, time-decay]
difficulty: intermediate
doc_type: system
parent: 101-option-trading-secrets-kenneth-r-trester
pages: 336
one_liner: "A time-and-strike spread entered only for a net credit: write a near-term out-of-the-money option and buy a longer-dated, further out-of-the-money option, aiming to keep the credit and end up owning a free longer-term option."
related: [101-option-trading-secrets-kenneth-r-trester, guy-cohen-the-bible-of-options-strategies, lawrence-g-mcmillan-profit-with-options]
source_file: "101 Option Trading Secrets - Kenneth.R.Trester.pdf"
---

## What it is

Trester describes the diagonal spread — a combined strike-and-time (calendar) spread — as one of his favorite trades and one of the book's two headline "Power Plays." Unlike a typical calendar spread, this version is entered only when it can be done for a net credit: the trader writes a near-term, out-of-the-money option and buys a longer-dated option at a further out-of-the-money strike. If the underlying stays below (for calls) the written strike through the short option's expiration, the trader pockets the credit and is left holding the longer-term option for free — a two-way win.

## Rules

**Structure**: sell (write) a near-term call (or put) that is out-of-the-money; buy a longer-term call (or put) on the same underlying that is priced further out-of-the-money, with an expiration at least one month later than the written option.

**Entry criteria**:
1. Write an option with a strike roughly 3 to 5 points out-of-the-money.
2. Buy an option expiring one month or more after the written option, at a strike 2.5 to 5 points beyond the strike you wrote.
3. Only enter the trade if it produces a net credit, or at worst a very small net debit.
4. Prefer strike spacing of about 5 points between the two legs where possible.
5. Select a written option with less than two months to its own expiration, so time decay works quickly on the short leg.
6. The longer-dated bought option should be as far out in time as reasonably available — the extra time favors the buyer's leg holding value.

**Stop-loss**: set a stop slightly in-the-money of the strike you wrote (example given: a written 55 call gets a stop around 56).

**Worked example given in the text** (Anheuser-Busch, Sept 26, 2002, stock at 52.2): buy the Jan 60 call at 0.6, sell the Nov 55 call at 0.9, for a net credit of 0.30; stop set at 56.1. If BUD stayed below 55 through November expiration without hitting the 56.1 stop, the trader kept the 0.30 credit and still held the Jan 60 call (valued around 0.20 at that point), for a total gain of about 0.50 ($50) on the position while still owning a live long-dated option.

**Exit rules**:
- Close the full spread at expiration of the written (short) option, unless that option has lost most of its value already — in which case it can be left to expire.
- If the stop-loss is triggered before the short option's expiration, exit — but note the position may still show a net profit even after a stop-out, because the longer-dated bought option typically gains value as the underlying rises toward it.
- After the short leg expires or is closed, the trader may choose to continue holding the remaining long-dated option (the "free option" kept from the credit generated), rather than closing it immediately, especially if it still has meaningful time value and the underlying could move favorably ("surprise volatility may give you a surprise payoff").

**Reported results**: the author cites 18 diagonal spreads recommended during 2002, of which 15 (about 83%) were profitable, with the three losses described as small.

## Risk

Maximum loss is bounded by the width between the two strikes minus the net credit received (or plus the small net debit paid, in the rare case a small debit was accepted). Because the position is entered for a credit, a worst-case outcome where the underlying stays flat or declines still typically returns the credit as profit. The main risk is the underlying rallying sharply through and beyond the written strike before the short option's expiration, which can trigger the stop-loss; because the long leg is further out-of-the-money and shorter in relative time-value cushion at that point, the stop-loss may still be taken at a net loss on the combined position despite the long leg's partial offset. As with all multi-leg strategies, execution risk (getting filled at the desired net credit) and slippage on the two legs reduce the realized edge relative to the theoretical numbers in the examples.

## Caveats

The 83% (15-of-18) win rate is a single-year, small-sample, non-audited figure drawn from the author's own newsletter recommendations rather than an independently verified track record, and should not be treated as an expected win rate for the strategy in general. The specific strike/time offsets (3–5 points, 2.5–5 points, one-month-plus expiration gap) are the author's personal guidelines rather than a mathematically derived optimum, and were calibrated to 2002-era option premiums and typical implied volatility levels, which may not transfer directly to other volatility regimes. The strategy assumes the trader can identify strike/time combinations that produce a net credit — in low-volatility environments or on thinly-traded underlyings, suitable diagonal credit spreads may not be available.
