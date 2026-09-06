# New Twist on an Old Indicator: the trader's summary

*Futures Magazine article on turning the lagging moving average into a leading signal via Louis Mendelsohn's neural-network intermarket 'predicted' moving average (VantagePoint).*

**Joe Krutsinger** · 2005 · Indicators · intermediate

*Source coverage: partial. PDF pages inspected: 1-4 (the predicted-moving-average method and the 18-week euro test results). These are study notes, not verified trading results.*

## Summary

A September 2005 Futures Magazine article by trading consultant Joe Krutsinger, framed around a client ("Bob") who wanted an edge beyond standard lagging moving averages. Krutsinger revisits Louis Mendelsohn's VantagePoint software, which uses five neural networks to perform intermarket analysis across ten related markets and produce a "predicted" moving average for one target market days into the future, rather than only reporting today's average. The article explains why ordinary moving averages inherently lag price, introduces the displaced moving average as a simpler do-it-yourself partial fix, then describes how comparing a predicted future moving average to today's actual moving average can generate earlier trend and reversal signals, plus how predicted next-day highs/lows can be used to place trailing stops more effectively than fixed-dollar or trendline-based stops.

## Key points

- Ordinary moving averages are inherently lagging: the average for today is plotted against today's price, so it trails price during trend changes and can even keep rising briefly after price has already turned down.
- A displaced moving average shifts a moving average's plotted value forward in time (e.g., a 5-day MA calculated today plotted 2 days ahead — TradeStation syntax `C,5,2`) as a simple way to reduce visible lag, though the author notes it's a simplistic forecast, not a true prediction, and "more research is needed" before recommending it outright.
- VantagePoint's neural-network approach instead predicts a future moving average value using intermarket data (nine related markets feeding into the euro's forecast, for example: British pound, US dollar index, Eurodollar, euro cash, Comex Gold, Japanese yen, Swiss franc, S&P 500, 10-year Treasury notes).
- Signal logic: when the predicted moving average (e.g., 10-day, 4 days forward) exceeds today's actual 10-day average, the market is expected to rise; when the gap between predicted and actual reaches a maximum and starts shrinking, it signals the trend is losing strength and a top/reversal may be near; an actual crossover (predicted average crossing from above to below actual, or vice versa) confirms the reversal.
- The same underlying technology can also predict next-day high/low ranges, which the article recommends using to set trailing stops (e.g., a few ticks below the predicted low for a long position) instead of clustering stops at obvious support/resistance trendlines where "too many traders" already have orders.
- A cited 18-week test (Oct 1, 2004 – Feb 10, 2005) on the euro using the predicted-moving-average crossover strategy produced 4 trades (one huge winner, one big winner, one small winner, one small loser) netting about $12,000 trading one contract/cross.
- The article explicitly warns there is no indicator that can predict the market with complete accuracy and that "the Holy Grail... doesn't exist" — the tool is framed as an edge-improving aid, not a certainty.

## Actionable rules

1. When using a predicted-vs-actual moving average crossover system: go long when the predicted future moving average exceeds today's actual moving average, and go short (or exit) when it falls below.
2. Treat a shrinking gap between the predicted and actual moving average (after it has been widening) as an early warning that the current trend is losing strength, before the crossover itself confirms a reversal.
3. For stop placement, use predicted next-day high/low levels rather than a fixed dollar amount or a widely-watched trendline; place a long's stop a few ticks below the predicted low.
4. As a simpler DIY partial substitute (without neural-network software), consider a displaced moving average (shifting the plotted MA value forward by a few bars) to reduce visible lag, while recognizing this is a much simpler and less validated technique.

## Caveats

The article's supporting evidence is a single 18-week, 4-trade sample on one instrument (euro), which is far too small to establish a statistical edge; results are presented as a case study, not a backtest. VantagePoint is a specific commercial software product from Mendelsohn (Market Technologies); the article does not disclose the neural-network architecture or training methodology in enough detail to independently replicate the "predicted" moving average. The displaced-moving-average alternative is explicitly flagged by the author as needing more research before being recommended.

## Who it is for

Futures/forex traders already using moving-average crossover systems who want to understand the concept of a "predicted" or forward-shifted moving average as a way to reduce lag, and who are evaluating (or already use) intermarket neural-network forecasting tools like VantagePoint.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: moving-average, displaced-moving-average, neural-network, intermarket-analysis, stop-placement
