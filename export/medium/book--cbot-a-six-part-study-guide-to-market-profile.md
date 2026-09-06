# A Six-Part Study Guide to Market Profile: the trader's summary

*The CBOT's own seminar-based home-study course on reading the Market Profile graphic, value area, day types, and Liquidity Data Bank volume.*

**Chicago Board of Trade** · 1996 · Market Structure & Price Action · intermediate

*Source coverage: partial. PDF pages inspected: 5-6, 15, 21-22 (profile construction, the initial balance, the 70% value area and the day-type definitions). These are study notes, not verified trading results.*

## Overview

This is the Chicago Board of Trade's own home-study course on Peter Steidlmayer's Market Profile, built from a seminar CBOT ran for its members. It is organized in six parts: reading the daily Market Profile graphic (Part I), monitoring longer-term trends with daily data (Part II), why the market's perception of value drives every decision (Part III), how activity distributes over time in daily and long-term views (Part IV), combining activity and value to analyze a developing session (Part V), and reading Liquidity Data Bank (LDB) volume to gauge strength or weakness (Part VI). The guide deliberately teaches the underlying auction concept rather than packaged trading strategies, on the premise that traders who understand the concept will build strategies that fit their own style.

## Core thesis

Markets are a continuous two-sided auction whose job is to facilitate trade by finding a price at which buyers and sellers are willing to transact. Price is not the object of analysis on its own; it is the byproduct of two groups with different behavior: a short-term ("day time frame") trader who needs a fair price today, and a longer-term ("other time frame") trader who can wait for an advantageous price. Volume distributed across price and time reveals which group is active and where, and that distribution tends toward a bell-shaped (normal) curve once a "unit" of market activity is complete. Reading the shape of that distribution as it forms — not just the closing price — tells a trader whether the current move is likely to continue, stall, or reverse.

## Key concepts

- **TPO (Time/Price Opportunity)** — each letter/half-hour column in the Market Profile graphic; the basic unit of analysis, showing that a given price traded during a given time bracket.
- **Initial balance** — the price range established in the session's first hour (roughly), representing the short-term trader's attempt to find a fair, two-sided price.
- **Range extension** — price movement beyond the initial balance, driven by the longer-term trader entering with enough volume to move the market directionally.
- **Value area / 70% range** — the price range containing about 70% of a session's volume (approximately the first standard deviation); the more precise measure of value, calculated price-by-price outward from the highest-volume price until 70% of volume is captured.
- **TPO value area** — a cruder, visual proxy for the 70% range: the range bounded by two or more single prints on each side.
- **Single prints / unfair high / unfair low** — low-volume, rejected price extremes at the top and bottom of a distribution; they define the auction's boundaries until taken out.
- **Day types** — Normal (short-term trader controls, ≥85% of range in the initial balance), Normal Variation (range extension up to roughly double the initial balance, control shared), Trend (range extension considerably more than double, longer-term trader in control, close on the extreme), and Neutral (range extension in both directions, no net influence, signals uncertainty and possible reversal).
- **Initiating vs. responsive activity** — initiating activity is buying above value or selling below value (a new flow of money, i.e., range extension); responsive activity is selling above value or buying below value (fading back into the established range). Initiating activity is generally the stronger signal.
- **Control price / mean price** — the market's current opinion of fair value, the price around which a distribution's volume converges; located in the top, middle, or bottom third of a unit's range.
- **Distribution shapes** — 3-1-3 (bell-shaped, volume base in the middle, "normal"/"neutral" days), 1-2-3 and 3-2-1 (J-shaped/teardrop half-distributions with the volume base at one end, seen in trending markets).
- **Liquidity Data Bank (LDB)** — the CBOT's actual-volume-by-price report layered on top of the TPO graphic, broken out by CTI (Customer Trade Indicator) category.
- **CTI classification** — CTI1 (local floor traders trading their own account), CTI2 (commercial clearing members' house accounts), CTI3 (members filling for other members), CTI4 (members filling for the public/other customers). CTI2 is treated as a proxy for informed commercial behavior.
- **Facilitating trade** — the market's core function; rising volume as price moves in a direction shows the market is facilitating that move (favors continuation), while falling volume on a move suggests the move may be ending.
- **Long-term auction chart** — a vertical chart tracking daily value-area range, plotted against six columns of buyer/seller activity (extremes, range extension, value area, split by initiating/responsive) to monitor which side controls a multi-day trend.

## Rules and setups

This is a reading framework, not a signal-generating system, but its construction and classification rules are precise enough to be coded:

1. **Building the profile**: assign each half-hour bracket a letter; record every price traded in that bracket as a TPO at that price. Stack letters at each price level to form the profile's shape.
2. **Finding the initial balance**: the range covered by the first one to two brackets of the session (empirically about the first hour, more for longer 24-hour sessions); this is the "pioneer range."
3. **Classifying the day** by comparing range extension to the initial balance: no extension → Normal day; extension up to about 2x the initial balance in one direction → Normal Variation; extension considerably more than 2x in one direction with a close on the extreme → Trend day; extension in both directions → Neutral day.
4. **Calculating the 70% value area**: start at the price with the highest TPO/volume count; add the larger of the two adjacent prices (one above, one below) to the running total; repeat, always taking the larger side, until cumulative volume reaches approximately 70% of the day's total.
5. **Reading control**: if the day's high/low (the unfair high/unfair low set in the initial balance) holds through the session, the short-term trader is in control; if the longer-term trader extends the range and that extension holds, the longer-term trader is in control.
6. **Reading LDB volume**: relate volume at a price to whether it is buying or selling activity and to where price sits relative to the long-term trend — rising volume in the direction of the move confirms continuation; falling volume warns of exhaustion; heavy CTI2 (commercial) activity concentrated in the value area is normal, but commercial buying above value or selling below value signals a deviation from routine hedging behavior worth noting.
7. **Long-term trend monitoring**: plot each day's value-area range and classify daily activity (initiating/responsive, in each of extremes/range-extension/value-area) on the long-term auction chart; value moving vertically (up or down) signals a continuing trend, while value moving sideways signals the trend has stalled.

There are no numeric entry/exit/stop rules — the guide is explicit that it teaches the concept, not a mechanical trading strategy.

## Risk and money management

The guide does not address position sizing, stop placement, or money management directly. Its practical risk contribution is indirect: understanding whether the market is in balance (rangebound, short-term trader in control) or imbalance (trending, longer-term trader in control) is meant to inform how aggressively a trader sizes and holds a position, and neutral days / failed range extensions are flagged as high-uncertainty conditions where new positions warrant caution.

## Psychology and discipline

Not a focus of the text. The closest psychological content is procedural discipline: the guide repeatedly stresses relating any single data point (a volume print, a range extension) back to its context — the day's developing value area and the longer-term trend — rather than reacting to it in isolation, and includes "stop and test yourself" quizzes throughout to force active recall rather than passive reading.

## Chapter map

- Part I — Reading the Market Profile Graphic — the auction framework, TPOs, initial balance, day types (Normal/Normal Variation/Trend/Neutral), initiating vs. responsive activity, who is active in the value area.
- Part II — Monitoring Longer-Term Trends with Daily Data — the long-term auction chart, tracking value-area movement and buyer/seller activity across many sessions.
- Part III — The Perception of Value Fuels Market Activity — why price departs from value (likely, unlikely, and surprise events), and a framework for classifying news/events by their fundamental impact.
- Part IV — Market Profile Data and the Distribution Process — how daily and long-term activity builds up into distributions (3-1-3, 1-2-3, 3-2-1 shapes) as the market's natural trading units.
- Part V — Using Market Profile Tools to Support Trading Decisions — combining value, range development, and activity to analyze a session as it unfolds.
- Part VI — Liquidity Data Bank Volume Analysis — the structure of an LDB report, CTI categories, relating volume to buying/selling behavior, and worked examples of reading a full LDB report for continuation/change signals.

## Strengths and caveats

The framework is exchange-native and internally consistent, and its day-type/value-area classification scheme has been widely adopted well beyond CBOT pit trading. That said, the material is dated in obvious ways: it is built entirely around open-outcry pit sessions with half-hour brackets, single-session "normal" days, and the old CBOT time-bracket letters (later revised for 24-hour GLOBEX trading); the worked examples are 1980s–1990s grain, bond, and equity-index futures. The CTI-based LDB analysis assumes access to CBOT's proprietary hourly volume-by-price reports, which have no direct retail equivalent in modern electronic/OTC markets — a trader today must approximate "value area" and "initiating vs. responsive" activity from volume profile and order-flow tools rather than an official LDB feed. The guide also explicitly avoids giving trading rules, so it will disappoint readers looking for a packaged system; it must be paired with a trader's own entry/exit/risk rules to become tradable.

## Who should read it

Traders and analysts who want to understand order-flow and volume-based market structure (value area, initial balance, day types) at the source, rather than through a secondary Market Profile book; useful background for anyone building discretionary or systematic strategies around volume profile, auction market theory, or intraday range development.

## Related books in this library

- [Dynamic Trading](https://ninad-k.github.io/trading-playbook/books/dynamic-trading-by-robert-c-miner.html) — another structure-first, non-mechanical framework (time/price/pattern projection) for reading where a market is likely to reverse or continue, complementary to Market Profile's day-type classification.
- [Trading for a Living](https://ninad-k.github.io/trading-playbook/books/elder-alexander-trading-for-a-living.html) — pairs well as a general trading-method and risk-management reference to wrap around Market Profile's pure market-reading framework, which itself gives no entry, exit, or sizing rules.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: market-profile, tpo, value-area, auction-theory, order-flow, futures, volume
