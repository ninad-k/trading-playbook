# Trading the Ross Hook: the trader's summary

*Joe Ross's book-length treatment of the Ross Hook, a trend-continuation correction pattern, with entry filters, natural-support stop placement, and money/trade management rules.*

**Joe Ross** · Trend Following & Mechanical Systems · intermediate

*Source coverage: partial. PDF pages inspected: 3-4, 43, 52, 56, 120, 125, 159, 176 (contents and index, the hook entry and stop chapters, the Keltner-channel filter and the S&P worked example). These are study notes, not verified trading results.*

## Overview

Joe Ross's dedicated book on the Ross Hook, a chart formation he named after noticing markets almost always leave behind a small "pointy" correction whenever a trend pauses, and that trading the breakout of that pointy place offers a low-risk way to join or rejoin a trend. The book traces the pattern's discovery from Ross's earlier "1-2-3"/"Law of Charts" work, gives a formal definition, and spends most of its pages on filtering which hooks are worth taking (CCI, Stochastics, Bollinger Bands, Keltner Channel), where to enter (the Traders Trick Entry and the "Slaughterbeck entry"), and where to place stops (natural support/resistance, cost-covering, volatility-based, trailing). Later chapters cover money/trade/risk management and situations to avoid ("Don't Take That Hook").

## Core thesis

A trending market's own corrections create tradable low-risk entry points: because other traders' stop and breakout orders cluster at the obvious high or low of a correction, buying (or selling) that level rides the order-flow momentum created when those orders trigger together. Ross argues the pattern works because enough traders' behavior around obvious levels is predictable, reinforced by Fibonacci/Gann retracement traders acting at similar zones. The book rejects "black box" indicator-only trading; oscillators are used strictly as filters layered on the price-based hook, never as standalone signals.

## Key concepts

- **1-2-3 formation** — point 1 is a high/low where the prior move fails, point 2 is the correction's extreme, point 3 is the breakout that retakes point 1 and defines (or re-establishes) the trend.
- **Ross Hook (Rh)** — whenever a trend is interrupted by a correction, no matter how slight, it leaves a hook: failure to make a new high (uptrend) or new low (downtrend). A double top followed by a lower high, or double bottom followed by a higher low, also counts.
- **Reverse Ross Hook (RRh)** — a hook-type pattern used as an early warning of possible trend reversal rather than continuation.
- **Congestion** — four-plus bars with no directional progress (alternating closes, dojis, ^/V shapes); a pointy place inside congestion is not a valid hook.
- **Defined vs. established trend** — "defined" once an emerging move's extreme is taken out; "established" once the following correction's extreme is also taken out.
- **Trader's Trick Entry (TTE)** — entering ahead of the hook's own breakout on the violation of a smaller correcting bar (full rules in [The Traders Trick Entry (TTE)](https://ninad-k.github.io/trading-playbook/books/tte.html)).
- **Slaughterbeck entry** — a more conservative alternative: wait for a higher low (or lower high) confirmation bar before entering.
- **Natural support/resistance stop, cost-covering stop, volatility stop** — three stop-placement techniques, respectively: one tick beyond real prior structure; sized so a loss roughly breaks even after costs; derived from a rolling volatility study rather than a fixed tick count.

## Rules and setups

1. Trade hooks only inside a defined or established trend; a pointy place inside congestion is not tradable.
2. Standard entry: buy one tick above the hook's high (long) or sell one tick below its low (short).
3. TTE entry: enter earlier on a correcting bar's violation, if there is enough room to cover costs before the hook's own breakout, and no more than three correcting bars have formed (see [The Traders Trick Entry (TTE)](https://ninad-k.github.io/trading-playbook/books/tte.html)).
4. Slaughterbeck entry: wait for a confirming higher low/lower high bar, then enter its breakout.
5. Stops: place at natural support/resistance (one tick beyond real structure), or a cost-covering distance, or a volatility-study-derived distance; trail behind each new correcting bar's extreme once profitable (a 50% trailing stop is one variant).
6. S&P 500 example: on a 40-bar Keltner Channel (multiplier 5) on a 3-minute chart, take partial profit around 40-50 points and move the remaining stop to breakeven; Ross reports a majority of trades reach 50 points, and says the stop can be held back if the market is still moving strongly at that level.
7. Filter with CCI (30-bar, ±150 lines) to avoid an already-overextended hook; with Stochastics, only the %K/%D crossover matters, not overbought/oversold level.
8. Filter with a channel study (Bollinger Bands, 40-bar Keltner, or ~39–40 bar moving-average bands): skip breakouts starting outside the channel unless price has been trading predominantly on that side already.
9. Capitalization rule: trade only markets where at least two contracts can be afforded; a one-contract trader is effectively gambling.
10. Skip the hook when: the market is too volatile around it; hooks come too close together (more than roughly one-to-three correction bars suggests exhaustion); the hook is too far from the anticipated level; volume has dried up; or the preceding congestion ran too long. A hook forming just before congestion is flagged as the highest-risk case.

No explicit percent-of-equity risk formula is given in the sampled pages; risk control is expressed through stop-placement technique rather than a stated percentage.

## Risk and money management

The risk framework is almost entirely about *where* to place the stop rather than *how much* equity to risk. Ross layers the stop techniques above and picks among them by market conditions and how much profit he wants to protect versus how much room to give the trade. The only explicit account-level rule sampled is the two-contract minimum capitalization requirement — a single-contract trader is treated as gambling. Ross also describes strict order-execution discipline (writing out and tape-recording every order, verbally confirming the recording, using price/limit orders rather than accepting slippage) as risk control at the execution level.

## Psychology and discipline

Ross frames disciplined execution as inseparable from the system: he tape-records and double-checks every order against a script, and insists on getting his price "or no fill," refusing to chase a market that moves away. He states this book assumes prior trading experience — the trend- and congestion-identification concepts took him years to internalize, so a single reading is not expected to be enough. He also warns against crowd psychology: because the hook relies on other traders' orders clustering at obvious levels, popular-indicator behavior is something to trade against once it becomes widely used, not follow.

## Chapter map

- Ch 1–2 — An Evolution / I Discover the Hook; Philosophy (capitalization, order discipline).
- Ch 3–4 — Trading Cycle: formal Ross Hook Definition; relating hooks to 1-2-3's and Reverse Ross Hooks.
- Ch 5–8 — Trading Anticipation: anticipating hooks, correction length, trend resumption; identifying congestion and trend.
- Ch 9 — The Trader's Trick: entering ahead of the hook breakout (full detail in [The Traders Trick Entry (TTE)](https://ninad-k.github.io/trading-playbook/books/tte.html)).
- Ch 10 — Confirmation filters: CCI, Stochastics.
- Ch 11–13 — Stops: natural support/resistance, cost-covering, volatility, trailing, and automation.
- Ch 14–17 — Filtering with Bollinger Bands, Keltner Channel, moving-average bands.
- Ch 18–20 — Don't Take That Hook: too volatile, too close together, too far away, volume dried up, congestion too long.
- Ch 21 — Money, Risk, and Trade Management ("Plain Vanilla" approach): order-ticket and tape-recording discipline.
- Ch 22–23 — Worked chart examples; closing/contact material.

## Strengths and caveats

This is a scanned book with OCR run only on a sample of pages, so these notes reflect the chapters and passages actually recovered; large stretches (particularly extended chart walkthroughs) were not sampled and could contain rule detail not reflected here. Within what was recovered, the material is unusually concrete about entries and stops, but Ross gives almost no formal backtest statistics for the hook itself — the evidence is worked chart examples, not a system-wide track record. The book assumes the reader already knows Ross's proprietary 1-2-3/Law-of-Charts definition from his other writings. Content reflects late-1990s charting software (CQG, Aspen, Ensign) and floor-broker order execution norms since superseded by electronic execution.

## Who should read it

Traders who already use price-action, trend-continuation methods and want a fully worked, filter-heavy approach to timing entries after a pullback, along with several concrete stop-placement techniques (natural support/resistance, cost-covering, volatility-based) rather than a single fixed-percentage rule. Not a starting point for beginners, since it assumes familiarity with Ross's earlier 1-2-3/Law-of-Charts material.

## Related books in this library

- [The Traders Trick Entry (TTE)](https://ninad-k.github.io/trading-playbook/books/tte.html) — Ross's own slide-deck detailing the Traders Trick Entry referenced throughout this book as the preferred early-entry technique.
- [Mechanical Trading Systems: Pairing Trader Psychology with Technical Analysis](https://ninad-k.github.io/trading-playbook/books/richard-l-weissman-mechanical-trading-systems.html) — for contrast, a fully mechanical/backtested approach to trend continuation versus Ross's discretionary, filter-layered hook method.
- [Trend Following](https://ninad-k.github.io/trading-playbook/books/michael-covel-trend-following.html) — broader trend-following context and track records from other practitioners.
- [Way of the Turtle](https://ninad-k.github.io/trading-playbook/books/curtis-faith-way-of-the-turtle.html) — another discretion-light, breakout-based trend system for comparison against the hook's more pattern-driven entries.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: ross-hook, 1-2-3-formation, traders-trick-entry, natural-support-resistance, stop-placement, trend-continuation, filters, joe-ross
