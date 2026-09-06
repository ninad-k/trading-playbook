---
stage: 6
title: The Trade
slug: 06-the-trade
goal: Turn a chart opinion into a position with a stop chosen from structure, a size chosen from your account, and a size calculation you can do by hand before every trade.
builds_on: [1, 2, 3, 4, 5]
diagram: position-sizing
diagram_caption: The same stop distance in price producing different position sizes as the risk fraction changes — size comes from the account, not the chart.
---

## What you will be able to do

Given any chart opinion — a break of structure, a pattern, a divergence, anything from stages 3 through
5 — you will be able to state an entry, a stop, a target, and a position size, and show the arithmetic
behind the size. You will be able to convert a trade into R multiples, calculate the expectancy of a run
of trades, and explain why a system's win rate alone tells you almost nothing about whether it makes
money.

## The lesson

### Why this stage comes before any setup

Every stage before this one taught you to read a chart. Nothing about reading a chart well protects you
from a bad outcome, because reading is not risk-taking — sizing a position is. This is deliberately the
last stage before the course turns to setups, sessions, and order flow, because a trader who can read
structure perfectly and sizes positions carelessly will eventually be destroyed by one trade, while a
trader with a mediocre eye for structure and rigorous sizing will survive long enough to get better. Most
courses teach entries first and risk as an afterthought. That ordering produces people who can spot a
pattern and still lose everything, because by the time they think about risk, the position is already on
and the decision that mattered most has already been skipped.

### The four decisions

Every trade you will ever place is four decisions, and only four: where you enter, where you get out if
you are wrong (the stop), where you get out if you are right (the target), and how large the position is
(the size). Entry and target come from the chart — from structure, patterns, and the other tools this
course has given you. The stop also comes from the chart: it belongs at the price level that proves your
read of the structure was wrong, not at a distance that feels comfortable. Size is the one decision that
does not come from the chart at all. It comes from your account, and specifically from how much of that
account you are willing to lose if the stop is hit. Keeping this separation straight — stop from
structure, size from account — is the core discipline of this lesson.

### R: the unit that makes trades comparable

Call the distance from your entry to your stop one R. If you buy at 100 with a stop at 98, one R is 2
points on that trade. Every outcome can now be expressed as a multiple of R instead of as a dollar amount
or a percentage: a trade that hits a target 6 points above entry is a 3R winner; a trade stopped out at
the stop is a −1R loss, by definition, every time, regardless of how many shares or contracts were in it.
Expressing outcomes in R is what lets you compare a stock trade to a futures trade to an options trade, and
what lets you evaluate a run of forty trades as a distribution of R multiples instead of forty unrelated
dollar figures. Without this unit, "I made $400 today" tells you nothing about whether your process is
working, because it does not say how much you risked to make it.

### Position size, from the account outward

Once you have an entry and a stop, the stop distance in price is fixed. Size is the only remaining
variable, and it is calculated, not guessed:

position size = (account equity × risk fraction) ÷ stop distance per unit

If you have a 50,000 account and you are willing to risk 1% of it on this trade, that is 500. If your
stop is 2.50 away from your entry on a stock, 500 divided by 2.50 is 200 shares. That is the whole
calculation. Notice what it does not depend on: it does not depend on how confident you feel, how far the
target is, or how sure you are that the pattern will work. It depends on exactly two things — how much
you are willing to lose and how far away the level is that proves you wrong — and both of those are known
before you enter.

### Why the convention converges on small

The market convention is to risk a small fraction of the account per trade — commonly cited figures sit
around 1%, sometimes as low as a fraction of a percent for more volatile instruments, rarely more than 2%.
That convention exists for arithmetic reasons, not caution for its own sake, and the arithmetic is the
next section.

### The drawdown-recovery asymmetry

Losses and the gains required to recover from them are not symmetric, and the gap between them widens
fast. A 20% loss requires a 25% gain on the remaining capital just to get back to even, because losing 20
of 100 leaves 80, and 80 needs to grow by 25% to return to 100. A 50% loss requires a 100% gain — you have
to double what remains just to break even. A 65% loss requires roughly a 186% gain. This is not a special
property of any one of these numbers; it is what division does once the denominator has shrunk. The
practical consequence is that avoiding deep drawdowns is not a nicety, it is close to the entire game: a
trader who risks large fractions of the account per trade needs only a short losing streak, which will
happen to everyone eventually, to reach a hole that ordinary trading can no longer climb out of. Risking a
small, fixed fraction per trade is how you keep every plausible losing streak inside a hole you can still
climb out of.

### Expectancy

![[diagram:expectancy|A losing majority that still compounds. The arithmetic is illustrative, not a tested result.]]

Expectancy is what tells you whether a way of trading makes money over a run of trades, and it is
calculated as:

expectancy = (win rate × average win in R) − (loss rate × average loss in R)

This single formula is also where the most common misunderstanding in trading lives: people assume a
higher win rate means a better system. It does not, on its own, mean anything at all without knowing the
size of the wins and losses. A system that wins 40% of its trades, with average winners of 3R and average
losers of 1R, has an expectancy of (0.40 × 3) − (0.60 × 1) = 1.2 − 0.6 = +0.6R per trade — strongly
profitable, because the size of the wins more than compensates for losing on the majority of trades. A
system that wins 70% of its trades, with average winners of 0.5R and average losers of 3R, has an
expectancy of (0.70 × 0.5) − (0.30 × 3) = 0.35 − 0.9 = −0.55R per trade — a losing system, and by enough
margin that it will eventually ruin the account, despite winning on most of its trades. The win rate you
are told about a system tells you almost nothing by itself. The ratio of average win size to average loss
size is at least as important, and expectancy is the only number that combines them honestly.

### Why moving a stop is the most destructive habit in trading

A stop is the price level at which your read of the structure was wrong. Once it is placed, moving it
further away because price is approaching it is not managing the trade — it is refusing to accept that
you were wrong, and it converts a defined, planned loss of 1R into an undefined loss of unknown size. This
single habit does more damage to more accounts than any entry mistake, because an entry mistake costs you
one bad trade at a known size, while a moved stop can cost you an amount you never sized for and never
agreed to in advance. If new information genuinely changes your read of the structure — a level breaks,
the pattern is invalidated the way stage 4 taught you to check — that is a reason to exit, not a reason to
move the stop further from price and hope.

### What sizing does and does not do

No position sizing rule, however disciplined, creates an edge. If your entries and exits lose money on
average — if your expectancy is negative — sizing rigorously will not make the system profitable; it will
only slow down exactly how fast it loses, and let you survive long enough to notice the expectancy is
negative and stop. That is precisely its value. Sizing does not make a bad process good. It stops a losing
process from ending you before you have the evidence to recognize it is losing.

## Worked example

You are looking at a stock that broke a swing high the way stage 3 taught you to identify, entering long
at 52.00. The swing low that would invalidate this read sits at 50.50, so your stop is 50.50 and one R is
1.50. You are trading a 30,000 account and have decided in advance to risk 1% per trade, which is 300.
Position size is 300 divided by 1.50, which is 200 shares. If the stock reaches your target of 55.75,
that is a 3.75 gain on a 1.50 risk — a 2.5R winner. If it instead reverses and hits 50.50, that is a
defined, planned −1R loss of exactly 300, because you sized for it in advance. Now run this same process
across forty similar trades over a few months. Suppose eighteen of them (45%) are winners averaging 2R,
and twenty-two (55%) are losers averaging −1R. Expectancy is (0.45 × 2) − (0.55 × 1) = 0.90 − 0.55 =
+0.35R per trade. Across forty trades, that is roughly +14R — a real, positive result — built from a
system that lost more often than it won. None of that required a high win rate. It required winners
larger than losers, sized consistently enough that no single loss, or short run of losses, threatened the
account.

## Practice

<div class="drill">

### Drill: Size ten trades on paper

Find ten setups on historical charts — any instrument, any of the structure or pattern reads from stages
3 and 4. For each one, write down the entry, the stop (from structure, not from feel), the R distance,
and the position size for a hypothetical 10,000 account risking 1% per trade. Do not check what actually
happened to price afterward until you have written down all ten sizes. The point of the drill is making
the size calculation automatic and separating it completely from any opinion about whether the trade will
work.

</div>

## Self-check

1. Which of the four trade decisions comes from the account rather than the chart, and why does that
   separation matter?
2. Why does a 50% drawdown require a 100% gain to recover, and what does that imply about risking a large
   fraction of the account per trade?
3. Using the expectancy formula, why can a system with a 70% win rate still be a losing system?
4. Why does moving a stop further from price turn a defined loss into an undefined one?
