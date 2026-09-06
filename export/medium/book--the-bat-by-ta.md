# The BAT: the trader's summary

*A forex ATR-trailing-stop breakout system (the BAT) that scales into trades at Fibonacci retracement levels once an ATR line is broken.*

**Team Aphid** · Day Trading & Scalping · intermediate

*Source coverage: full. PDF pages inspected: 1-9. These are study notes, not verified trading results.*

## Summary

A short forex strategy handout from "Team Aphid," built on a custom ATR trailing-stop indicator ("FF ATR Trailing Stop") on an hourly chart, combined with Fibonacci retracements. Core idea: price breaking through the current ATR line ("BAT line") signals a trade in that direction; the trader then draws a Fibonacci retracement from the breakout point to a recent swing extreme and places pending orders to scale in if price pulls back to the 38.2% and 61.8% levels, using the 161.8% extension as an invalidation point. The stop trails with the ATR line itself.

## Key points

- Setup: 1-hour chart, tested on GBPUSD, using ATR Period 5 / Factor 4.0, producing alternating blue/red "BAT lines."
- Fib tool levels: 0 ("Swing"), 0.382, 0.618, 1.0 ("Enter 1 lot"), 1.618.
- Entry: enter in the breakout direction as soon as price touches and breaks the current BAT line; the author suggests resting a pending order at that line so the entry is not missed.
- Scaling in: draw a Fib retracement from the breakout price to the recent swing extreme, then place pending orders — 1 unit at 61.8%, 2 units at 38.2%.
- Stop: initially ~10 pips beyond the swing extreme used for the Fib; once a new BAT line forms and passes the original stop, the stop tracks that new line continuously.
- Invalidation: cancel remaining pending orders if price reaches the 161.8% extension — a likely trend reversal signal.
- A "BAT Range Trade" variant re-enters repeatedly as price oscillates within the 161.8% boundary in a ranging market.

## Actionable rules

1. Enter (1 unit) as soon as price touches and breaks the current BAT line, ideally via a pending order resting at that line.
2. Draw a Fib retracement from entry to the nearest significant swing extreme in the trade direction.
3. Place pending orders for 1 unit at the 61.8% retracement and 2 units at the 38.2% retracement.
4. Set the initial stop ~10 pips beyond the swing extreme anchoring the Fib.
5. Once a new opposite-color BAT line forms and price passes the original stop, trail the stop to that new line.
6. Cancel unfilled pending orders if price reaches the 161.8% extension.
7. Exit the full position when price closes through the opposing BAT line — which simultaneously signals a new entry the other way.

## Caveats

An informal trading-community handout with no backtest, win rate, or sample size — only a few hand-picked chart examples, plus an admission that stop-hunting spikes cause losses the author can't distinguish in advance from real breakouts. Position sizing is stated in absolute lots, not risk percentage, so it needs adapting to account size.

## Who it is for

Discretionary forex traders already comfortable with ATR trailing stops and Fibonacci retracements who want a concrete way to combine the two for entries and scaled position-building.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: forex, atr-trailing-stop, fibonacci-retracement, breakout, scaling-in, mt4
