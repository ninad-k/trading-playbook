---
title: "Range-Bound Premium Spread System (Butterfly, Condor, Calendar, Collar)"
author: George A. Fontanills
year: 2005
slug: fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed--range-bound-premium-spreads
tier: A
category: Options, Futures & Derivatives
tags: [options, butterfly, condor, calendar-spread, diagonal-spread, collar, time-decay]
difficulty: intermediate
doc_type: system
parent: fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed
pages: 592
related: []
one_liner: "A family of defined-risk spreads (butterfly, condor, calendar, diagonal, collar) built to profit from time decay when a stock is expected to stay inside a range, each with a numbered entry-to-exit road map."
source_file: "Fontanills - The Options Course - High Profit And Low Stress Trading Methods, 2nd Ed.pdf"
---

## What it is

A set of limited-risk, limited-reward structures for markets expected to trade sideways, all sharing the same underlying logic: sell time-decaying premium near the current price, buy cheaper options further away to cap the risk, and let time erosion do the work. The **long butterfly** buys one lower-strike option, sells two middle-strike options, and buys one higher-strike option (all calls or all puts, same expiration) — maximum profit sits at the middle (short) strike. The **long condor** widens the body into two separate short strikes instead of one, trading a smaller maximum profit for a wider profit zone. The **calendar spread** sells a near-term option and buys a longer-term option at the same strike, profiting from the front option's faster time decay; the **diagonal spread** does the same across different strikes. The **collar** is a stock-plus-options overlay (long stock, long protective put, short covered call) used mainly to hedge an existing holding rather than to speculate on a range.

## Rules

**Long butterfly (14-step road map)**
1. Look for a sideways-moving market expected to stay within the breakevens; confirm listed, liquid options with adequate premium relative to commissions.
2. Check implied volatility to see if the options are over- or under-priced, and review a year of price/volume history for context.
3. Construct: buy one lower-strike option (support level), sell two middle-strike options (equilibrium), buy one higher-strike option (resistance) — all calls or all puts, same expiration, options with ≤45 days to expiration.
4. Compute before placing: **max risk** = net debit paid; **max reward** = (difference between highest and short strike) − net debit, realized when the stock finishes exactly at the short strike; **upside breakeven** = highest strike − net debit; **downside breakeven** = lowest strike + net debit; reward/risk ratio.
5. Place the full multi-leg trade as one limit order — never leg in or out.
6. Plan the exit before entering: if price moves outside the breakevens, plan to cut losses.
7. **Exit:** below the downside breakeven — let expire worthless (loss = net premium paid); inside the breakevens — sell the long options and let the short options expire worthless, ideally right at the short strike; above the upside breakeven — exit or exercise the long options to offset an assignment on the shorts.

**Long condor**
8. Structure like a butterfly but with two separate short strikes instead of one (e.g., a 30-35-40-45 condor: buy the 30, sell the 35, sell the 40, buy the 45), widening the maximum-profit zone at the cost of a lower maximum reward-to-risk than a butterfly.
9. Same debit-is-max-risk framing as the butterfly; exit logic mirrors the butterfly's (let expire worthless outside the range, otherwise manage toward the profit zone as expiration nears).

**Calendar / diagonal spread**
10. Sell a shorter-term option and buy a longer-term option (calendar: same strike; diagonal: different strikes), both calls or both puts, aiming for the smallest possible net debit.
11. Best placed where a **time skew** exists (front-month IV elevated relative to back-month IV, often from a rumor or event) — buy the low-IV (longer-dated) option, sell the high-IV (shorter-dated) one.
12. Goal: the short-term option decays faster than the long-term option loses value, especially if the stock stays near the strike through the short option's expiration.
13. **Exit:** when the short-term option expires (worthless, ideally), evaluate the long option's remaining value against the original debit; either close for a profit or roll into a new calendar spread by selling another near-term option against the same long leg.

**Collar (hedge overlay on existing stock)**
14. On a stock already owned (or bought concurrently), buy an at-the-money or out-of-the-money protective put and sell an out-of-the-money covered call, sized so the call premium largely offsets the put's cost.
15. **Max risk** = initial stock price − put strike + net debit (or − net credit); **max profit** = (call strike − initial stock price) − net debit (or + net credit); **breakeven** = initial stock price + [(put premium − call premium) ÷ shares].
16. **Exit:** if the stock rallies to the strike of the short call and time value has fallen to roughly a quarter point or less, expect assignment — either let it happen or buy back the call to keep the shares. If the stock falls sharply, expect to exercise the put and close the (now-naked) short call rather than leave it open.
17. **Rebracketing (optional enhancement):** if the stock rallies to the short call's strike well before expiration, close the existing put and call, then open a new collar one strike level higher (sell the old put, buy back the old call, buy a new higher-strike put, sell a new higher-strike call) to lock in the gain and keep participating in further upside — repeatable as the stock continues climbing.

## Risk

All of these structures are defined-risk except the bare collar, whose downside is bounded by the put strike (not the stock going to zero) and whose upside is capped at the call strike. For the butterfly and condor, maximum loss is the net debit paid, realized if the underlying finishes outside the wings at expiration; maximum gain is capped and occurs only in a narrow zone near the short strike(s) — these are precision trades that need the underlying to stay range-bound, unlike the directional or backspread strategies elsewhere in this book. Calendar/diagonal spread risk is limited to the net debit paid but is harder to state as a fixed number at entry because the long leg's value at the short leg's expiration depends on where implied volatility sits at that future date — the book recommends using options analysis software rather than a closed-form estimate. As elsewhere in the source, position sizing should respect the account-level caps: no more than 5% of capital on one trade, no more than 50% deployed at once.

## Caveats

These are precision, narrow-profit-zone strategies — commissions on 3–4 leg spreads (butterfly, condor) can consume a meaningful share of the limited maximum profit, especially for retail-sized position counts, a cost the book's clean numeric examples don't fully stress-test. The road maps assume the trader can reliably judge "sideways" in advance; no systematic filter (e.g., a volatility or trend indicator threshold) is given for identifying range-bound candidates beyond "review price/volume history." The rebracketing collar technique is presented anecdotally with a single worked example (AIG) rather than validated across multiple trades or market regimes.
