---
stage: 7
title: The Session
slug: 07-the-session
goal: Read the shape of a single trading day and say, at any point in it, what phase it is in and what that implies.
builds_on: [1, 2, 3, 4, 5, 6]
diagram: opening-range
diagram_caption: The first N minutes of a session set a mini-range; what happens to it next tells you the day's character.
---

## What you will be able to do

Look at an intraday chart and name which part of the day you are in — opening auction, midday rotation, or
closing positioning — and say what that implies about how much weight to give the last thirty minutes of
price action. You will be able to build a short list of levels before the open, read what an opening range
breakout or failure is telling you, and state, without hedging, why trading more often costs more.

## The lesson

### Why a day has a shape at all

Everything up to this stage treated a chart as a sequence of bars with no particular respect for the clock. That
was the right simplification while you were learning to read structure. It stops being accurate the moment you
trade intraday, because a trading session is not a random walk sampled at fixed intervals — it is a single auction
with a beginning, a middle, and an end, and each part does different work.

The open exists to reprice everything that happened while the market was closed or thin: overnight news, an
earnings release, a shift in a related market, or simply the accumulated opinion of everyone who did not get to
trade at yesterday's close. That repricing is often violent and directionless for the first few minutes, because a
large number of participants are all trying to establish a position at once with very little agreement yet on
where the new fair price sits. The middle of the session is rotation: having roughly repriced, the market spends
most of its time testing the edges of a range it has provisionally accepted, probing whether yesterday's structure
still holds. The close is positioning — funds squaring exposure, index-related flows executing on schedule, and
short-term traders deciding whether to carry a position overnight. None of this is mysticism; it is simply
different populations of participants dominating at different times, and it means the same-looking break of a
level means different things depending on when in the day it happens.

### The opening range

The opening range is the high and low made in the first stretch of the session — five minutes, fifteen, thirty,
whatever you choose. There is nothing magic about any of those numbers; you are choosing a trade-off. A short
window gives you an earlier read but more false signals, because a five-minute range is a tiny sample of a
volatile part of the day. A longer window is more reliable but tells you less that you didn't already learn from
watching the first hour unfold. Pick one, stay consistent with it, and treat it as a lens, not a rulebook — this is a
structure concept from stage 3 applied to a specific slice of time, not a system with an edge built in.

Two things can happen to that range once it is set. Price can hold it and eventually break out of it with
continuation — the market printing new highs or lows and staying there, which tells you the early two-sided
argument has resolved and one side is now in control. Or price can push outside the range and then fail,
snapping back inside within a few bars. That failure pattern usually means the breakout was driven by orders
that had to trade — stops triggering, not genuine new conviction — and once those are used up, the range
reasserts itself. Reading which of the two happened is exactly the structure-and-sequence skill from stages 2 and
3; you are just applying it to the day's first move instead of a swing high.

### Rotation and the handoff between sessions

Once the opening range resolves, most of the day is rotation: price moving between the edges of whatever range
has formed, testing each edge, sometimes rejecting it and sometimes extending it a little further. This is the
same test-and-reject behavior you already read in support and resistance zones — it is just happening on a
faster clock. What is new at this stage is that the levels being tested were often not built today at all. In any
market that trades outside a single exchange's regular hours — futures, forex, and increasingly stocks with
active pre-market sessions — the overnight or pre-market period quietly builds a range before the main session
even opens, and the first hour of the day session is frequently just a test of levels someone else already put in
place while you were asleep. A break of a round-looking level during a thin, low-participation stretch of the
overnight session carries far less weight than the identical break during the busiest hour of the regular session,
because fewer independent participants are behind it. Before you react to any intraday break, it is worth asking
who was actually trading when it happened.

### Gaps

A gap is the difference between where the prior session closed and where today opens. Two flavors behave
differently. A gap into prior value opens beyond yesterday's close but still inside the range yesterday actually
traded and accepted — today's open is not really "new," it's a re-entry into territory the market already agreed
was fair, and it commonly gets revisited during the session because doing so doesn't require the market to
accept anything unfamiliar. A full gap opens entirely outside yesterday's whole range, into territory with zero
recent history of acceptance — this kind of gap is a genuinely new auction, and whether it gets filled or holds
depends on whether the opening range extends with conviction (evidence the new price is being accepted) or
fails and rotates back (evidence it isn't). Neither type comes with a promised outcome; the gap's type tells you
which question to ask, and the opening range's behavior gives you the answer for that specific day.

### VWAP

![[diagram:vwap-bands|VWAP through a session, with the bands widening as dispersion grows.]]

VWAP — volume-weighted average price — is the running average price of the session, weighted by how much
volume traded at each price, computed from a fixed starting point (almost always the session open). It is not a
moving average of price; it is a moving average of where the money actually traded. Institutions reference it
because it is the standard yardstick for execution quality: a desk instructed to buy "at VWAP" is graded after the
fact on whether its average fill beat that number, which means large volume-weighted execution algorithms are
themselves built to trade around it — turning VWAP from a passive statistic into a level that other orders
actively react to. Its standard-deviation bands measure how far current price has traded from that
volume-weighted average, in statistical units, which gives you a consistent way to say "unusually far" across
different instruments and different days rather than guessing at a fixed number of points or ticks. Price sitting
above a rising VWAP is a rough read on who currently holds the advantage in the session's auction; price sitting
below a falling one is the mirror image. Combine that with where price sits relative to yesterday's accepted
range and you get the premium/discount framing: trading above yesterday's value while below today's VWAP is
a different, more contested location than trading above both, and the two readings should agree before you
treat a location as strong.

### Building the map before the bell

Everything above is more useful before the open than during it. The professional habit is to mark the relevant
levels — yesterday's high, low, and close, the edges of yesterday's value, the overnight high and low, VWAP's
anchor point — on the chart before the session starts, so that when price arrives at one of them you are
checking a plan against reality instead of improvising a decision under time pressure. Reacting live, with no
prior map, is how a reasonable read of one bar turns into a decision made on adrenaline.

### The cost of trading more often

Stage 6 gave you expectancy: average win times win rate, minus average loss times loss rate. Every additional
trade also subtracts the spread and the commission paid to enter and exit it, and intraday trading means many
more entries and exits per unit of edge captured than swing trading does. A strategy that trades a handful of
times a week can absorb a fixed cost per trade against a comparatively large expected move. A strategy that
trades ten times a day is paying that same fixed cost ten times as often against moves that are, by necessity,
much smaller — because there simply isn't room in a single session for ten large moves. This does not make
intraday trading impossible; it means a high-frequency approach needs a proportionally larger edge per trade to
survive its own costs, and you should be honest with yourself about whether you have identified one before you
start trading that often.

## Worked example

A stock closes at 100.00. Overnight it drifts to 101.50 on light volume and opens the regular session at 101.40 —
a gap into prior value if yesterday's range extended up to 102, a full gap if yesterday never traded above 101. Say
yesterday's high was 101.20: this is a full gap, genuinely new territory. The first fifteen minutes print a range of
101.30 to 101.90 — the opening range. At 10:00 price pushes to 102.10, a new high, but by 10:08 it has rotated
back inside 101.90 and is drifting toward 101.30. That is an opening-range failure: the breakout print did not
hold, which is evidence the push to 102.10 was driven by triggered orders rather than genuine new buying.
Session VWAP, anchored at the 9:30 open, sits at 101.55 by this point; price trading back below it after failing to
hold new highs tells you sellers, not buyers, currently have the advantage in this session's auction. Nothing here
promises a further decline — it tells you which side of the argument is currently winning and why, which is
exactly the information you need before deciding whether to act.

## Practice

<div class="drill">

### Drill: Build the pre-market map, five days running

Pick one instrument you can watch during its regular session. Before each of the next five sessions opens, write
down: yesterday's high, low, and close; the overnight or pre-market high and low; and where you expect the
opening range to be measured (pick one window — 5, 15, or 30 minutes — and use it every day). After the
session, record what actually happened to the opening range (held and extended, or broke and failed), where
price closed relative to VWAP, and whether the day's move stayed inside yesterday's range or left it entirely. No
trades — this is a map-building and observation habit, not an entry signal.

</div>

## Self-check

1. Why does the same break of a level mean something different at the New York open than during a thin
   overnight hour?
2. What is the practical difference between an opening-range breakout and an opening-range failure, and what
   does each imply about who was behind the move?
3. Why does a gap into prior value behave differently, on average, from a full gap outside the prior range?
4. Why does an intraday approach need a larger edge per trade than a swing approach to survive its own costs?
