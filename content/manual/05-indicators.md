---
stage: 5
title: Indicators, and What They Actually Compute
slug: 05-indicators
goal: State, for any indicator you use, the exact arithmetic it performs on OHLCV data, and explain why loading a chart with several of them at once adds far less than it looks like it does.
builds_on: [1, 2, 3, 4]
diagram: divergence
diagram_caption: Price making a new high while an oscillator makes a lower high — the same swing-structure comparison applied to two series at once.
---

## What you will be able to do

You will be able to say, for a moving average, RSI, MACD, ADX, or Bollinger Bands, exactly what
arithmetic produces the line on your screen — not what it "means" in trader folklore, but what it
computes. You will be able to spot a genuine divergence between price and an oscillator, and you will be
able to explain why running five indicators at once is usually worse than running one.

## The lesson

### The central insight

Every indicator on your charting software is a function of the same open, high, low, close, and volume
you already have for every bar. An indicator does not observe the market independently and report back
something new; it takes numbers you already possess and rearranges them — averages them, divides one by
another, subtracts one from another, measures how spread out they are. That means no indicator can ever
contain information that was not already present in the price and volume series. What it can do is make
a pattern in that data easier to see than it is in the raw candles, by discarding some information (an
average discards the noise between individual bars) in exchange for revealing something else (the
average discards noise in exchange for revealing the drift). Keep that trade — information discarded for
a pattern revealed — in mind for every indicator in this lesson, because it is the whole story of what an
indicator is.

### Moving averages

A simple moving average (SMA) is the mean of the last N closes, recalculated on every new bar. A 20-period
SMA is just "the average close of the last 20 bars," sliding forward one bar at a time. The lookback, N,
controls a trade-off you can reason about directly: a short lookback tracks price closely but jumps
around with every swing; a long lookback is smooth but reacts slowly to a real change in direction. That
lag is not a flaw to be engineered away — it is the price you pay for smoothing, unavoidably, because an
average of the past N bars can only ever confirm a new direction after enough of those N bars reflect it.

An exponential moving average (EMA) computes the same kind of thing — a weighted average of past closes —
but weights recent bars more heavily than older ones, so it reacts faster to new information than an SMA
of the same length while still smoothing. It does not eliminate lag; it reduces it, and gives up some
smoothness to do so.

The crossover — buy when a fast average crosses above a slow one, sell when it crosses below — is the
simplest possible trading system built from this tool, and it is worth understanding precisely because it
is simple: it is a rule for detecting, with a deliberate delay, that the recent average price has moved
above the longer-run average price. It will always enter after a trend has already started and exit after
it has already turned, because that is what averaging does. That is not a defect in a particular version
of the rule; it is what a crossover of two averages structurally is.

### RSI

The Relative Strength Index measures, over a lookback period (conventionally 14 bars), the ratio of
average gains on up-bars to average losses on down-bars, scaled to sit between 0 and 100. A reading near
100 means the recent bars have been almost all gains with almost no losses to offset them; a reading near
0 means the opposite. This is why "overbought" does not mean "about to fall" and should never be read as
"sell": a strong, sustained trend produces a long run of up-bars with small pullbacks, which is exactly
the condition that pins RSI at a high reading for as long as the trend runs. RSI is telling you, correctly,
that gains have dominated losses recently — it is not telling you that the trend is exhausted. Traders who
sell every "overbought" reading are, in a real trend, selling into strength repeatedly and losing every
time, because they are misreading a measurement of recent gain-versus-loss ratio as a prediction of
reversal.

### MACD

The Moving Average Convergence Divergence indicator is two exponential moving averages — conventionally
12-period and 26-period — and their difference, plotted as a single line, plus a third EMA of that
difference (conventionally 9-period) plotted as a signal line. That is the entire computation: two
averages, subtracted, then smoothed again. Everything you can read off a MACD chart — the line crossing
zero, the line crossing its own signal line, the histogram widening or narrowing — is a description of how
two moving averages of the same closes are converging or diverging from each other. It is not a separate
measurement of anything; it is moving averages, restated.

### ADX

The Average Directional Index measures trend strength, not trend direction. A high ADX means price has
been moving persistently in some direction, up or down — it does not tell you which. A rising ADX with
price falling is just as valid a reading as a rising ADX with price rising; both say "this move is
sustained," not "this move is up." Traders new to ADX frequently misread a high reading as bullish, which
is simply wrong: check the direction from price itself, and use ADX only to answer the separate question
of whether a directional move currently has conviction behind it or is chopping without one.

### Bollinger Bands

Bollinger Bands are a moving average (conventionally 20-period) with two bands plotted a number of
standard deviations (conventionally 2) above and below it. Because a standard deviation is a measure of
how spread out recent prices have been, the bands widen when the market gets more volatile and narrow
when it gets quieter — the bands are a volatility measure wrapped around a moving average, not a
support-and-resistance tool, even though price touching a band is often read that way. A useful derived
number is %b: 100 × (last − lower) ÷ (upper − lower), which restates "where is price relative to the
bands" as a single percentage — 100 means price is at the upper band, 0 means it is at the lower band,
50 means it is sitting on the moving average. %b adds no new information over looking at the bands
directly; it just makes "where inside the bands is price right now" a single comparable number instead of
a visual judgment.

### Divergence, taught properly

Divergence is a comparison between the swing structure of price and the swing structure of an oscillator
(RSI and MACD are the two most commonly used for this). Regular bearish divergence is price making a
higher high while the oscillator makes a lower high at the same time — momentum, as the oscillator
measures it, failed to confirm the new price extreme. Regular bullish divergence is the mirror: price
makes a lower low while the oscillator makes a higher low. Read correctly, divergence is not a signal that
reverses a trend by itself — it is evidence that the move producing the current price extreme was made
with less force, by the oscillator's arithmetic, than the move that produced the previous extreme. That is
a genuinely different piece of information from price alone, because it compares the shape of two series,
not just the level of one. It still requires the same discipline as a pattern from stage 4: state what
would have to happen — typically a break of the most recent swing point — before divergence means
anything has actually changed in the structure itself.

### Why stacking indicators fails

Return to the central insight: every indicator here is a function of the same OHLCV data. RSI, MACD, and
a moving average crossover are three different arithmetic operations performed on the same closes. When
all three "agree" — RSI is falling, MACD is turning down, price is below its moving average — you have
not gathered three independent pieces of evidence. You have computed three different summaries of one
underlying fact: recent closes have been weak. Adding a fourth or fifth indicator to the same chart
multiplies the appearance of confirmation without multiplying the amount of actual information, because
none of them looked at anything except the price series you started with. This is the single most common
mistake in indicator use, and it is also the most reassuring-looking one, because a chart with five
aligned indicators feels far more convincing than a chart with one — even though it is not.

### Defaults, not discoveries

The periods used throughout this lesson — RSI 14, MACD 12/26/9, a 20-period moving average or Bollinger
band — are conventions that became standard decades ago, not numbers derived from some proof that they
are optimal. There is nothing wrong with using them; they are a reasonable, widely understood starting
point, and using an unusual period buys you nothing on its own. Where people get into trouble is running
software that tests hundreds of period combinations against past data and picking whichever one produced
the best-looking result. That process — optimization on historical data — will always find some parameter
combination that fit the past well, because with enough combinations tested, some will fit by chance
alone. It tells you almost nothing about how that same parameter will perform on data it has not seen,
and it is where most system-building goes wrong: not in choosing an indicator, but in tuning it until it
memorizes history instead of describing the market.

## Worked example

Take a chart where price has been in a clear uptrend for a month, and look at three things on it at once.
The 20-period EMA is sloping up and price is holding above it — that is the moving average confirming the
trend you can already see. RSI has been sitting between 55 and 70 for most of that month, occasionally
touching 72 without ever dropping below 45 on pullbacks — that is the "strong trends stay overbought"
behavior from this lesson, not a sell signal. Now suppose price makes a new high for the move, but RSI's
reading at that new high is only 61, lower than the 72 it hit two swings back at a lower price high. That
is regular bearish divergence: the new price extreme was produced with less relative strength than the
previous one, by RSI's arithmetic. On its own, that is one piece of evidence that the trend's momentum
has thinned — it is not a reason to act. What would have to happen for it to matter is the next thing to
check: a break of the most recent swing low, the same break-of-structure event from stage 3. Until that
happens, you have an observation, not a signal — and if you also glance at MACD and see its histogram
shrinking over the same stretch, notice that you have not found a second confirming signal. You have
found the same weakening-momentum fact, computed a second way from the same closes.

## Practice

<div class="drill">

### Drill: One indicator, no stacking

Pick one indicator from this lesson — RSI, MACD, or Bollinger %b — and put it on 15 charts with nothing
else added. For each chart, write one sentence stating what the indicator's arithmetic is actually
telling you (not what you think it predicts), and note whether price and the indicator agree or diverge.
Do not add a second indicator to any of the 15 charts. The point of the drill is training yourself to read
one indicator for exactly what it computes, before you are tempted to stack.

</div>

## Self-check

1. In one sentence, why can no indicator ever contain information that was not already in the OHLCV data?
2. Why does a strong trend keep RSI "overbought," and why does that make selling on an overbought reading
   a mistake?
3. What does ADX measure, and what does it explicitly not tell you?
4. Why does adding a third and fourth confirming indicator to a chart add far less evidence than it
   appears to?
