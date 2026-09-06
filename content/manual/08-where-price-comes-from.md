---
stage: 8
title: Where Price Comes From
slug: 08-where-price-comes-from
goal: See the machinery that produces every price you have been reading since stage 1, and know what a retail trader can and cannot actually observe in it.
builds_on: [1, 2, 3, 4, 5, 6, 7]
diagram: order-book
diagram_caption: Every price you have read since stage 1 is the output of resting bids and offers meeting in a limit order book.
---

## What you will be able to do

Explain what actually happens between a bid and an offer to produce the single number a candle plots. You
will be able to say why a support or resistance zone from stage 3 is often the same place a volume profile
would mark as heavily traded, distinguish resting liquidity from aggressive orders and say which one moves
price, and describe honestly what order-flow tools can and cannot tell you about the future.

## The lesson

### The machine underneath the chart

Since stage 1 you have been reading price as if it were a single, agreed-upon fact ticking along a line. It isn't. A
market is a continuous double auction: many buyers and many sellers simultaneously quoting prices they are
willing to transact at, with no auctioneer and no single item changing hands. At every instant there is a highest
price someone will pay (the bid) and a lowest price someone will accept (the ask, or offer); the gap between
them is the spread. The full list of every other resting order waiting above and below that spread — organized
by price, and within a price, by the order in which each order arrived — is the limit order book. That book is
matched by software called a matching engine, applying a fixed rule almost everywhere: the best-priced order
is matched first, and among orders at the same price, whoever arrived first is filled first — a resting order
placed a fraction of a second earlier than an identical one has a real, mechanical advantage, simply by being
ahead in the queue.

The last traded price, which is the only thing a plain candlestick chart shows you, is a receipt from a
transaction that has already finished. It tells you what happened, not what is about to. The book is the actual
standing state of supply and demand; price is just its most recent output. Closing that gap is the point of this
stage.

### Aggressor and passive: the whole foundation

Every trade has exactly two counterparties playing structurally different roles. The aggressor sends an order
that is willing to transact immediately at the best available opposing price — a market order, or a limit order
priced aggressively enough to cross the spread — and by doing so causes the trade to happen right now. The
passive side is whoever was already resting in the book and simply got hit or lifted. This distinction matters
because only the aggressor can move price: consuming all the resting size at a price level is what forces the
next trade to happen at a worse price, pushing the market up or down. A passive order, no matter how large,
does not move price by sitting there — it can only absorb aggression directed at it. A market that prints heavy
volume at the ask but fails to advance is telling you something specific: passive sellers are absorbing buying
pressure as fast as it arrives, refilling as quickly as they get taken out. That pattern is called absorption, and
it is often the earliest sign that a level is going to hold.

An order sized larger than what is resting at the best price does not get one clean fill — it walks the book,
consuming the next price level, then the next, at progressively worse prices, until it is filled. The average price
it pays is worse than where it started; that gap is market impact, and it is the direct, mechanical reason large
participants break size into many small orders over time instead of sending it all at once. A large market order
arriving into a thin book can move price sharply on its own for exactly this reason — the move was caused by
the order consuming liquidity, not by anyone learning anything new.

### The auction, not the ticker

![[diagram:auction-rotation|The two-way auction: probes that get rejected, and one that gets accepted.]]

Auction Market Theory takes this machinery and asks a bigger question: what is the market actually trying to
do? Its answer, developed by Peter Steidlmayer and later systematized by James Dalton, is that a two-sided
market exists purely to facilitate trade — to search, continuously, for the price at which the largest number of
buyers and sellers currently agree to transact. Price is not a target the market is converging on; it is the
byproduct of that search. This reframes "value" precisely: value is not a price that looks cheap or expensive to
you, but a price the market has already demonstrated, through real time and volume spent there, that
two-sided trade is willing to happen at. A price outside that demonstrated range is not yet accepted, regardless
of how it looks on a chart.

The classic tool for recording this is the Time Price Opportunity, or TPO, profile: the session is divided into
fixed time intervals, and every price the market trades at during a given interval gets a mark. Rotate the result
so price runs vertically and the shape of the day emerges — wide rows are prices that attracted repeat
participation across many time periods, thin rows are prices merely passed through once and abandoned. A
TPO profile is, literally, a record of where the auction spent its time, independent of how much size traded
there, which is why time and volume need to be read together rather than as substitutes for each other — a
single enormous order can sweep through a price in a moment and leave almost no time footprint at all.

### Where the zones came from

![[diagram:volume-profile|The same chart turned on its side. This is what stage 3 was pointing at.]]

This is the moment the course closes its own loop. Back in stage 3 you learned to draw support and resistance
as zones, not lines, and you were told that a zone is a region where price has previously reversed or stalled. A
volume profile is the tool that explains, mechanically, why those zones exist and where they sit precisely. It is a
histogram built directly from the trade tape: for every price a session (or any window you choose) traded at,
sum the total volume that changed hands there, and plot it as a horizontal bar. The point of control is simply
the single price with the most volume — the level both sides transacted at more than any other, which is why it
behaves like a magnet that price tends to return to once it wanders away. The value area is the band of prices,
built outward from the point of control, that together account for roughly the bulk of the session's volume — a
formal, measurable version of "where the market accepted this instrument as fairly priced."

Inside that shape, high-volume nodes are local peaks — prices where resting size is thick, which is exactly why
price slows down and rotates as it passes through them, and exactly why they so often coincide with the support
and resistance zones you already know how to draw by eye. Low-volume nodes are the opposite: thin bands
the market crossed quickly without settling, which is why price accelerates through them rather than stalling,
and why they make natural targets once a level breaks rather than places to expect a pause. Volume profile and
your hand-drawn zones are two views of the same underlying fact about where size actually traded — one built
from the transaction record, the other from eyeballing where price reacted.

### Reading the fight inside a single bar

![[diagram:footprint-delta|One bar opened up: volume at the bid and at the ask, price by price.]]

A candle compresses an entire bar into four numbers: open, high, low, close. A footprint chart keeps the whole
transaction record intact, breaking a bar into rows — one per price it traded at — and showing how much
volume at that price was bought (crossed at the ask, an aggressor lifting a resting offer) against how much was
sold (crossed at the bid, an aggressor hitting a resting bid). Summing ask volume minus bid volume across a bar
gives you delta, a direct numerical read on which side currently holds the upper hand. An imbalance is a
sustained, lopsided delta at consecutive prices; absorption, introduced above, is the footprint's clearest
signature of the opposite — heavy volume at a price with delta that stays flat or reverses, meaning the
aggressive side is being consistently met and turned back by resting size rather than being allowed to push
through.

### The order book is not a crystal ball

The depth-of-market display — the live ladder of resting bids and offers — is the only place you can see supply
and demand queued up before a trade happens rather than after. It is also the least trustworthy layer of all this,
because every resting order shown on it can be cancelled in an instant, and some large orders are placed
specifically to be cancelled. Spoofing is the deliberate practice of resting a large, visible order with no intention
of ever letting it fill, purely to create a false impression of supply or demand and push other participants to
react to it; the order is pulled the moment price actually approaches. It is illegal in regulated markets, and it is
also common enough that you should never treat a large resting wall on the DOM as real until it either gets
traded through in size or holds while price presses directly against it. The only liquidity you can trust
completely is liquidity that has already executed — a print on the tape that has cleared and cannot be
un-traded.

Be honest, too, about what you specifically can see. A retail platform can generally show you the trade tape
and a reasonable depth of aggregated resting size — enough to build a usable footprint, a volume profile, or a
DOM ladder. It essentially never shows you the individual orders behind that aggregated size, the identity of
who is trading, or activity in dark pools that never touch the visible book at all — that is institutional-only
infrastructure, and no amount of studying this chapter closes the gap. What all of this machinery gives you, at
any level of access, is a record of what has already happened: who was aggressive, where size was defended,
where the auction spent its time. None of it predicts what happens next. It narrows your uncertainty about the
present moment; it does not remove it.

## Worked example

A stock has been trending up for a week and approaches 50.00 — a level you had already marked, using stage 3
methods, as a resistance zone from a prior swing high. Pulling up a volume profile for the last month shows a
dense high-volume node sitting almost exactly at 49.80–50.20: the same zone, arrived at from the transaction
record instead of from eyeballing wicks. As price grinds up into that zone on the footprint, you notice heavy
volume trading at the bid with delta flattening rather than continuing to climb — sellers stepping in, but buyers
absorbing what's offered rather than being pushed back. On the DOM, a large ask order appears at 50.10; two
minutes later, as price ticks up toward it, the order is cancelled in bulk with almost no volume printed against
it — a spoof, not real supply. Cumulative delta over the next several bars turns decisively positive, and price
closes through 50.20 on volume well above the session average. Nothing here guaranteed the break would hold.
What it gave you was a coherent, multi-layered read — structural zone, volume profile, footprint absorption,
an exposed fake wall, and confirming delta — all pointing the same direction, which is a materially better basis
for a decision than the breakout candle alone.

## Practice

<div class="drill">

### Drill: Overlay the zone

Pick a chart where you previously marked a support or resistance zone using stage 3's methods. Pull up a
volume profile (session or a fixed range covering the relevant history — most charting platforms have this
built in, even free ones) over the same period, and mark the point of control and the nearest high- and
low-volume nodes. Write down whether your hand-drawn zone lines up with a high-volume node, and if it
doesn't, look at what actually happened at your zone versus at the node. Separately, watch a liquid instrument's
DOM for ten minutes and note any large resting order that appears and then gets pulled as price nears it before
it ever trades.

</div>

## Self-check

1. Why does only the aggressor in a trade move price, while the passive side can only absorb it?
2. What does a high-volume node explain about a support or resistance zone that eyeballing candle wicks alone
   does not?
3. What is the specific, two-part behavior that distinguishes a spoofed order from a genuine resting order?
4. What can order-flow tools tell you about the market, and what can they never tell you, no matter how good
   your data access is?
