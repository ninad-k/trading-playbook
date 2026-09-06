# The Fractal's Edge Futures Course: the trader's summary

*An archived online course for a proprietary futures system built around fractal breakouts and three dynamic stability lines.*

**Unknown** · 2002 · Trend Following & Mechanical Systems · intermediate

*Source coverage: partial. PDF pages inspected: 1-70, 100, 103, 129, 131, 133, 152, 154, 158, 164 (the complete tool and rule chapters plus sampled pages of the trading simulation). These are study notes, not verified trading results.*

## Summary

This archived 2002 online course teaches "The Fractal's Edge," a discretionary futures system built from seven components: the bar chart, five-bar price fractals, a three-line "Gatekeeper" of stability lines, the Psychometric Evaluators (a volume histogram plus a volume/range ratio histogram), the Accelerometer, the Momentum Oscillator and the E-Wave Oscillator. Although the course frames the method through chaos theory, its operational core is a filtered breakout process: define two-sided levels while the stability lines compress, enter when price escapes with the gate open, add contracts on oscillator signals, and trail a stop against faster stability lines. Chapters 1-10 lay out the tools; chapter 11 is a long bar-by-bar trading simulation.

## Key points

- A buy fractal has a middle high above the two highs on each side; a sell fractal reverses that arrangement (PDF pp. 13-21).
- The Gatekeeper comprises the Wall, Tripwire and Picket Fence, described as progressively faster moving-average-like stability lines whose periods are derived from fractal ratios (PDF pp. 22-24).
- Intertwined lines mark a closed gate or range. A price bar escaping across the Wall can indicate a developing trend (PDF pp. 24-25).
- The entry setup uses the latest buy and sell fractals lying at least two-thirds outside the nearest stability line (PDF p. 25).
- **Psychometric Evaluators** (PDF pp. 38-44) — two histograms read together: today's volume versus yesterday's, and the Volume:Range Ratio, `VRR = Range / Volume`, which the course credits to Bill Williams' Market Facilitation Index. Each bar is coloured green when today's reading exceeds yesterday's and red when it does not, and only the latest two bars matter. The four colour pairs are read as: green-green (rising volume and rising price facilitation — go with the current bar's direction), red-red (fewer participants, movement slowing), red-green (low volume with high facilitation — floor locals may be pushing price, unless higher volume follows within two bars), green-red (high volume with low facilitation — the combination the course says appears among the top or bottom three bars of almost every major move).
- **Accelerometer** (PDF pp. 45-55) — a histogram of the rate of change of momentum, described as a leading indicator that turns before the Momentum Oscillator does. Colour changes mark acceleration and deceleration; it generates add-on signals only.
- **Momentum Oscillator** (PDF pp. 56-63) — shows the strength and direction of momentum and generates two buy and two sell signals (an "ACDC" signal and a crossover signal). Like the Accelerometer, its signals are for adding contracts, not for entering or exiting.
- **E-Wave Oscillator** (PDF pp. 63-64) — similar in construction to the Momentum Oscillator but built on different ratios; its stated purpose is to confirm that momentum has turned and that it is time to be out of the market.
- Stops move daily when the market moves favourably. The course calls the faster Picket Fence stop conservative and the slower Tripwire stop aggressive because the latter keeps the position open longer (PDF pp. 29, 36-37).

## Actionable rules

1. In a range with intertwined stability lines, mark the latest eligible buy and sell fractals.
2. Place opposing entries two ticks above the buy-fractal high and two ticks below the sell-fractal low, and require the gate to open on the breakout (PDF pp. 26, 36). The reviewed entry checklist does not specify cancellation handling; that detail must be defined before implementation.
3. For a long, project the current bar's low to the chosen stability line and use that price as a sell stop; for a short, project from the current bar's high and use a buy stop. Recalculate after favourable movement (PDF pp. 29, 36-37).
4. Exit if the stop trades or if the current bar closes across the Tripwire into the zone between Tripwire and Wall (PDF pp. 31, 37).
5. **Adding contracts with the Accelerometer** (PDF pp. 47-52), permitted only when already in a position, and never a buy while the price bar is below the Wall or a sell while it is above the Wall:
   - Above the zero line, a buy signal forms on the third of three consecutive green bars following a red bar (buying with the momentum); place the order two ticks above the high of the corresponding price bar. No further buy signal is possible until another red bar prints.
   - Below the zero line, a buy signal needs the fourth of four consecutive green bars (buying against the momentum); a bar that crosses the zero line counts as two, so three bars suffice in that case.
   - Sells mirror this: three consecutive red bars below the zero line, four above it.
6. **Adding contracts with the Momentum Oscillator** — take the ACDC or the crossover signal, again only as an add-on to an existing position.
7. Treat an E-Wave Oscillator turn as confirmation to be flat if the stop has not already done the job.

## Caveats

The course depends on a proprietary spreadsheet: the Gatekeeper's periods, the Accelerometer's and the two oscillators' formulas are all described as "based on fractal ratios" without the ratios themselves being disclosed, so the system cannot be independently coded from this document. The colour and signal rules above are complete and reproducible; the indicator values they are computed from are not. Profit figures in the trading simulation are illustrative and the course presents no out-of-sample or robustness study. The material is a 2002 web capture, so the market context (pit trading, daily bars, phoned orders to a broker) is dated.

## Who it is for

Researchers studying historical commercial futures systems and rule-based breakout design, and readers who want to see how a chaos-theory framing maps onto an ordinary breakout-plus-oscillator method.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: futures, fractals, breakouts, momentum, trailing-stops
