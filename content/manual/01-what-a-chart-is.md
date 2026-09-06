---
builds_on: []
diagram: ohlc-compression
diagram_caption: Everything that happened, and the four numbers that survive it.
goal: Look at any price chart and state plainly what it records, what it has already
  thrown away, and why the timeframe you are viewing is a choice you made rather than
  a fact about the market.
slug: 01-what-a-chart-is
stage: 1
title: What a Chart Actually Is
---

## What you will be able to do

Explain, for any chart on any timeframe, exactly what information survived into the picture and what was discarded before you ever saw it. Choose a timeframe for a stated reason instead of whatever your platform opened to by default. Stop expecting the chart to tell you what happens next.

## The lesson

### A chart is a record, not a forecast

Start with the single idea everything else in this course depends on. A price chart is a record of completed transactions — prices that buyers and sellers actually agreed to trade at, arranged in the order they happened. It is history. It is not a forecast, not a signal, not a message written for you to decode. When you look at a chart and think "this is telling me where price is going next," you have already made the mistake that produces most of the bad decisions beginners make. The chart cannot tell you that, because the people who traded at those prices did not know where price was going either. They just agreed on a number and traded.

This matters because almost every beginner error — chasing a breakout because "the chart looks like it wants to go up," refusing to sell because "it has to bounce here," redrawing a trendline until it fits — comes from treating the chart as something other than a record.

### What the chart keeps, and what it throws away

Every trade that happens in a market has a price, a size, and a moment in time. A chart is built by taking a slice of time — a minute, an hour, a day — and compressing everything that happened inside that slice down to a handful of numbers. That compression is not free. It is the whole story of what a chart is.

Inside any one bar or candle on your screen, dozens, thousands, sometimes millions of individual trades occurred. The chart does not show you any of them individually. It does not show you the order they happened in — whether the high came before the low or after. It does not show you who was buying and who was selling, or whether the volume came from one large participant or ten thousand small ones. Unless you have deliberately added a volume pane underneath, it does not even show you how much traded — a bar with a small range could represent ten trades or ten million. All of that detail is gone, folded into a single shape. What survives is a summary: four prices per bar, arranged into a picture.

That is not a flaw in charting — a summary is the entire point, since you could not usefully look at every individual trade in a day. But you have to know what you are looking at. A chart is a lossy compression of the truth, and the size of what gets lost grows with the length of the bar. A one-minute bar throws away relatively little. A monthly bar throws away almost everything that happened inside that month, keeping only four numbers to represent millions of decisions.

### The four numbers, and why they are a summary

Those four surviving numbers have names: open, high, low, and close — OHLC for short. The open is the first price traded in the period, the close is the last, and the high and low are the extremes reached at any point in between, however briefly. Together they tell you the range price covered and where it started and finished inside that range. That is genuinely useful information. It is also, unavoidably, a summary of a summary — four numbers standing in for everything that happened.

Of the four, the close deserves more weight than the other three, and it is worth understanding why. The close is the price that survived — the last price the market agreed on before the period ended, after every argument during the period had been settled one way or another. The high and low might have been touched for a single trade, by one impatient participant, and then immediately rejected; they tell you the extremes of the fight, not who won it. The close tells you who won. This is why so many technical rules — moving averages, most indicator calculations, the definition of a trend — are built on closing prices rather than highs, lows, or opens. It is also why you should pay attention when a period closes very differently from where it spent most of its time trading: that is the market changing its mind late.

### Line, bar, and candle: three ways to draw the same four numbers

The three common chart styles are not different data. They are different decisions about which of the four numbers to draw, and how visible to make the rest.

A line chart connects closing prices only, one dot per period, joined into a line. It throws away the open, high, and low entirely, keeping just the number that matters most. That sounds like a loss, and it is — but it is also why line charts are the clearest way to see the underlying trend without the visual noise of every period's internal wiggle.

A bar chart (sometimes called OHLC bars) draws a vertical line for the high-to-low range, with a small tick on the left for the open and a small tick on the right for the close. It keeps all four numbers but makes them fiddly to read at a glance — you have to look for the tick marks.

A candlestick chart draws the same four numbers but turns the open-to-close range into a thick "body" and colors it, typically one color if the close was higher than the open and another if it closed lower. The high and low become thin lines above and below the body, called wicks or shadows. Candles keep the same four numbers as a bar chart but present the balance of power within the period much faster to the eye, which is why most traders now default to them. You will use candles for the rest of this course, starting in the next stage.

None of the three formats gives you more raw information than the others — a candle and a bar built from the same period contain identical numbers. What changes is how quickly you can read what you need, and what you are tempted to ignore. A line chart makes it easy to ignore intraperiod volatility. A candle chart makes it easy to overread a single bar's wick as more meaningful than it is. Neither is more "true."

### The timeframe is a decision you make, not a fact about the market

Here is the part beginners consistently underestimate. Every chart is drawn on some timeframe — the length of time each bar represents, whether that's one minute, one hour, one day, or one week. That length is not given to you by the market. It is a sampling choice, exactly like choosing how often to check the temperature outside. Check every second and you will see it jump around with every cloud passing over the sun. Check once a day and you will see a smooth seasonal curve. Neither reading is wrong. They are answers to different questions, taken at different resolutions of the same underlying reality.

The same market, over the same stretch of calendar time, can look like a clean uptrend on a daily chart and look like directionless chop on a one-minute chart of the same days. Both charts are accurate. Neither is lying. The daily chart is showing you where the closes ended up net of all the noise in between; the one-minute chart is showing you that noise in full. If you pick your timeframe by habit — because it's what your platform opened to, or what a video you watched happened to use — you are letting an accident decide what kind of question you're asking the market. Pick it on purpose instead: decide first how long you intend to hold a position, and choose the timeframe that answers that question. A trader planning to hold for days should not be making decisions from a one-minute chart, and a trader looking to act in the next ten minutes gets nothing useful from a weekly chart.

### Gaps: when the record itself has a hole in it

One more thing chart honesty requires you to notice: sometimes a market simply does not trade for a stretch of time — overnight, over a weekend, or during a halt — and when it reopens, the first trade is at a meaningfully different price from where it left off. On the chart this shows up as a gap: a visible empty space between one bar's range and the next, where no price was ever recorded because no trade happened there. A gap is not a glitch in your charting software. It is an honest report that the market's agreed-upon price moved while nobody was watching or trading, usually because new information arrived while the market was closed. You will meet gaps again as you go further, but for now the point is narrower: a chart's continuity is itself an assumption, and gaps are the moments that assumption breaks.

## Worked example

Picture a stock that traded in a narrow band all day around 50, then in the final hour a large piece of news broke and it spiked to 54 before drifting back to close at 52.

Look at that day on a daily chart, and you will see one candle: open near 50, high at 54, low near 50, close at 52. It reads as a solidly bullish day, buyers in control by the close. Nothing in that single candle tells you the entire move happened in the last hour, or that price gave back half its gain before the close, or that for six hours nothing happened at all.

Now look at the same day on a five-minute chart. You will see six-plus hours of nearly flat, boring bars, then a sudden run of large green candles as the news hits, then a handful of red candles as some of the move gets sold back. Same underlying trades, same market, same day — but the five-minute chart shows you the shape of the move and the daily chart shows you only its net result.

Neither chart is wrong. If you were deciding whether to hold this stock into next week, the daily candle's message — closed up, near the day's high half of its range — is exactly the summary you need and the five-minute detail would just be noise. If you were trying to understand why the stock moved, or you had been holding a position through that final hour, the five-minute chart is the only one that shows you what actually happened to you. The lesson is not that one chart is better. It's that you have to know which question you're asking before you pick which one to look at.

## Practice

<div class="drill">

### Drill: One day, three timeframes

Pick one stock or instrument you can get free chart data for. Find a single trading day that had a noticeably large move — up or down doesn't matter. Pull up that same day on three timeframes: daily (so this day is one candle among many), one-hour, and five-minute. Write down, in one sentence each, what story each timeframe tells about that day. Then write one more sentence: which timeframe you would have needed to be watching to actually experience the move as it happened, versus which one you'd check afterward to know how the day net out. Do this for three different days this week, ideally including at least one day with a gap at the open.

</div>

## Self-check

1. What does a chart record, and what does it discard, even before you choose a chart type?
2. Why does the close typically matter more than the open, high, or low when a rule has to pick just one price?
3. A line chart, a bar chart, and a candlestick chart built from the same data contain the same four numbers. What actually differs between them?
4. Why is timeframe a choice rather than a property of the market, and what should you base that choice on?
