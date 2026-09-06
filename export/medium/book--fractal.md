# The Fractal's Edge Basic User's Guide: the trader's summary

*A proprietary end-of-day system combining fractal breakouts, momentum crossovers, stability lines, and dynamic stops.*

**Ken Herbert Sr.** · 2006 · Market Structure & Price Action · intermediate

*Source coverage: partial. PDF pages inspected: 1-18, 31-75, 134-137, 149-153, 160-161 (the entry, stop-ladder, adverse-exit and money-management modules; the intervening pages are bar-by-bar chart illustrations of the same trades). These are study notes, not verified trading results.*

## Summary

Ken Herbert's manual for The Fractal's Edge (TFE), a proprietary end-of-day stock and futures program, taught as nine modules. Its chart stacks price with four "Gatekeeper" lines, a Momentum Oscillator (MO) and an Accelerometer (ACC). The Gatekeeper defines whether a trade is permissible and supplies stop references; fractal breakouts and momentum zero-crossings provide entries; a seven-step ladder walks the trailing stop from one stability line to the next as the Accelerometer decays. The text invokes chaos, wavelet and fractal ideas, but the usable content is a conventional rule hierarchy built from price extremes, moving-average-like lines, momentum and trailing stops.

## Key points

- Three Stability Lines (Wall, Tripwire, Fence) plus a 3-period Safety Line form the Gatekeeper.
- Initiating fractals mark breakout levels and remain valid until triggered; a MOXO signal is likewise valid until hit.
- MO represents major momentum waves; ACC is a faster warning of acceleration or deceleration.
- MOXO signals occur when MO crosses zero, subject to the Safety Line/Fence relationship.
- Entries use two-tick buffers beyond the signal bar.
- Initial stops use recent three-bar extremes and eligible Stability Lines; thereafter the stop climbs the Gatekeeper ladder (Modules 6-7).
- Module 8 supplies the money-management layer — equity reserve, a three-tier risk matrix and a volatility-based cap on per-trade risk.
- The manual is tied to proprietary software and does not disclose the formulas behind the Gatekeeper lines, MO or ACC.

## Actionable rules

1. For a fractal long, place the entry two ticks above the marked fractal bar's high; for a short, two ticks below its low. Keep the signal active until filled (PDF p. 41).
2. For a MOXO long, require MO to cross from negative to positive and the 3-period Safety Line to stand above the Fence; enter two ticks above the corresponding price bar. Reverse every condition for a short (PDF p. 41).
3. Set a long's first-day stop at the lower of the lowest low of the signal bar and prior two bars, or the lowest Stability Line that is below the signal-bar low (PDF pp. 42-43, 49).
4. Set a short's first-day stop at the higher of the highest high of those three bars, or the highest Stability Line above the signal-bar high (PDF pp. 43-45).
5. **Trailing stop ladder for a long** (PDF p. 49; mirror it for shorts):
   1. Start with the initial stop from rule 3.
   2. If the entry bar's low is below the farthest Stability Line, hold that initial stop until a bar's low prints above the farthest line, then move to step 3; if the entry bar's low is already above it, go straight to step 3.
   3. Follow a Stability Line chosen by trading style: aggressive follows the Wall (or the farthest line until it crosses the Wall); moderate follows the Tripwire on the same logic; conservative follows the Fence.
   4. While ACC is above zero, keep following the line chosen in step 3.
   5. Each time three consecutive red ACC bars print while ACC is still above zero, step the stop up one Stability Line (Wall to Tripwire, Tripwire to Fence, and so on) until stopped out.
   6. If ACC crosses the zero line from positive to negative, move the stop immediately to the 3-period Safety Line and follow that.
   7. After entry day, if the Safety Line crosses below the Fence so the Fence is above it, switch to the Safety Line and follow it until stopped out.
6. **Money management for stocks** (PDF pp. 149-151): keep 25% of the account in reserve and trade with 75%; split that trading equity across a risk matrix of 50% low-risk, 30% medium-risk and 20% speculative names, classified by share price and by how often the bars breach the Fence, Tripwire and Wall; and size each position so the volatility-based stop risks no more than 3% of total account equity (the manual's worked example risks $495, or 1.7% of a $30,000 account, and notes the same trade needs a $16,500 minimum account to stay inside the 3% cap).

## Caveats

This is a sales-oriented manual for a paid platform. Its strong performance claims are unsupported in the text, and the proprietary indicator formulas — the periods behind the three Stability Lines, the MO and the ACC — are never disclosed, so the entry and stop rules above can be followed only inside TFE's own software. "Fractal" language here is a framing device, not empirical validation, and the worked trades are single illustrative examples from 2005 rather than a tested track record.

## Who it is for

System traders evaluating historical commercial platforms, and readers who want a well-specified example of a stop-ladder that steps between multiple trailing references as momentum decays.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: fractals, momentum, trend-following, stops, position-sizing
