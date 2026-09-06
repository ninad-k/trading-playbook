# The Option Trader Handbook: Strategies and Trade Adjustments: the trader's summary

*A trade-management manual devoted entirely to adjusting existing stock and option positions — rolling, collars, ratio spreads, and repair strategies — as the underlying moves.*

**George M. Jabbour and Philip H. Budwick** · 2004 · Options, Futures & Derivatives · intermediate

*Source coverage: partial. PDF pages inspected: 8, 10 and the adjustment chapters checked against the note's repair, ratio-write and exit rules. These are study notes, not verified trading results.*

## Overview

Jabbour (a finance professor) and Budwick wrote this as a reference handbook, not an introductory options text — it assumes the reader already knows basic strategies (calls, puts, covered calls, spreads) and instead focuses entirely on what to do *after* a position is open. Each chapter takes one starting position (long stock, short stock, long call, long put, spreads, combinations) and walks through every direction the underlying can move, showing a specific numeric adjustment for each scenario: rolling into a different strike or spread, adding a collar, converting a spread into a ratio spread, or "repairing" a losing position back toward breakeven. Every example uses a worked numeric case (mostly a hypothetical stock like EBAY, YHOO, or COST) with exact strikes, premiums, and breakeven arithmetic, and each chapter builds on strategies introduced earlier.

## Core thesis

Strategy selection at entry is only half of trading; the other half — arguably the more overlooked half — is actively managing the position afterward through adjustments. Because options can be recombined in near-limitless ways, almost any losing or stalled position can be reshaped (not necessarily saved) into one with a better risk/reward profile than simply holding or closing outright. The authors frame this as "the art of trade adjustments": a disciplined trader first fixes risk management principles (know max risk, max reward, and breakeven before entering), then uses a repertoire of mechanical adjustment techniques — rolling, collaring, ratio-spreading, and repairing — to lock in gains, reduce losses, or restructure a position's risk profile as the underlying stock, time, or volatility changes.

## Key concepts

- **SCORE formula** — the book's five-step trading-success process: Select the investment, Choose the best strategy, Open the trade with a plan, Remember your plan and stick to it, Exit your trade.
- **Trading as a business** — treating a trading account like a company with start-up, growth, and mature phases; positions are "employees" that get "fired" (closed) when they underperform against a predetermined exit rule.
- **Trade adjustment** — any change made to an open position (adding, removing, or replacing legs) to alter its risk/reward profile in response to a stock move, time decay, or a change in outlook.
- **Rolling** — closing one option leg and opening another at a different strike and/or expiration on the same underlying position to reset the risk/reward profile (e.g., rolling a protective put into a bear put spread, or a long call into a bull call spread).
- **Call/put ratio spread adjustment** — converting a long option or a vertical spread into a ratio spread (selling additional out-of-the-money options against an existing long) to collect extra premium, boost profit around a target strike, or reduce cost basis — at the expense of unlimited/naked risk beyond a new breakeven.
- **Collar** — combining a protective put with a covered call (both usually one strike out-of-the-money) to cap both loss and gain, often for a small net credit or at no cost; a "profit collar" applies the same structure after a stock has already gained to lock in a minimum profit.
- **Stock/position repair strategy** — adding a 1:2 (or higher) call ratio spread to a losing long-stock or long-call position, structured for a net credit or zero cost, to lower the breakeven point without committing new capital; the short strike is chosen as the price target for where the stock is expected to recover to, not a runaway rally target.
- **Christmas tree spread** — a repair variant with short calls at two different (non-identical) strikes rather than the same strike, created by rolling a losing bull call spread down to a lower long strike.
- **Ratio write** — long stock plus more short calls than shares owned (e.g., 1:2 or 1:3), generating extra premium for a stock expected to trade in a range, at the cost of unlimited upside risk beyond a calculated breakeven.
- **Call/put replacement therapy** — selling a profitable long stock or option position and replacing it with a cheaper, farther out-of-the-money option to lock in gains while keeping exposure to further favorable movement.
- **Synthetic conversions** — recognizing that a long stock plus long put equals a synthetic long call, or a short stock plus long call equals a synthetic long put, so that adjustments to one position type can be re-expressed as another (e.g., rolling a losing long call into a synthetic straddle).

## Rules and setups

The book is organized as adjustment recipes rather than a single unified entry system; the most codeable, recurring numeric rules:

1. **Pre-trade risk quantification.** Before every trade, calculate maximum risk, maximum reward, and breakeven point(s), in that order, before committing capital.
2. **Predetermined exit rule.** Set an exit trigger before entry — a stock price, a percentage loss (the book's own worked example uses a 15% stop), or a technical support/resistance level — and follow it regardless of hope that "it has to come back."
3. **Repair/adjustment credit rule.** When adding a repair ratio spread or converting a spread into a ratio spread, only do so for a net credit or, at worst, a very small net debit; a repair that costs meaningful capital is not a true repair.
4. **Ratio spread sizing.** Do not exceed roughly a 1:3 ratio (one long option to three short options) on an initial adjustment; higher ratios (1:4+) are reserved for cases where an existing unrealized stock gain provides a buffer against the added naked risk, and even then are discouraged.
5. **Stock repair strike selection.** When repairing a losing long-stock position with a call ratio spread (e.g., buy 1 near-the-money call, sell 2 calls at a higher strike), set the short strike at the price you expect the stock to recover to — not necessarily back to the original purchase price — and keep the long call's strike near the current stock price so it generates value to offset the existing loss.
6. **Collar construction.** Sell a covered call and buy a protective put, typically both one strike out-of-the-money, sized so the position opens near breakeven or for a small credit; this caps both the maximum loss and maximum gain until expiration ("set and forget").
7. **Profit collar timing.** After a long stock position has an unrealized gain, add a collar (call sold above market, put bought below market) to lock in a minimum guaranteed profit while retaining limited further upside to the short call's strike.
8. **No naked legs in a repair.** When repairing a losing position, size the short option leg so it is fully covered by the long option and/or the underlying stock — never leave a naked leg, since that adds risk to an already-losing position instead of reducing it.
9. **Roll-down criterion for call verticals.** If a bull call spread's underlying has fallen and a recovery (but not a full round-trip) is expected, roll the long strike down (financed by selling the original long call and opening a lower-strike long call, funded by additional short calls at the original strikes) to lower the breakeven; choose between a multi-strike ("Christmas tree") ratio spread (lower breakeven, added naked-call risk above the upper short strike) or a straight lower-strike vertical (smaller debit added, no naked risk) based on risk tolerance.
10. **Time-based exit for time-decay strategies.** For adjustments that depend on selling premium (ratio writes, collars, repair spreads), prefer shorter-dated options so time decay works in the adjusted position's favor, and reassess or roll at expiration rather than letting the hedge silently expire.

## Risk and money management

There is no single portfolio-level position-sizing rule (no fixed "risk 2% per trade" prescription); risk management is taught instead as a discipline applied trade-by-trade: always derive maximum risk, maximum reward, and breakeven before entering, and always set a predetermined percentage- or price-based exit before capital is at risk. The book explicitly warns against selling naked/uncovered options without appreciating that "unlimited risk" is a real outcome, using Nick Leeson's 1995 Barings Bank collapse (from selling naked Nikkei options ahead of the Kobe earthquake, roughly $1.3 billion in losses) as a cautionary case. A recurring quantitative discipline throughout the adjustment chapters is that any defensive adjustment (repair spread, roll, collar) should be evaluated by its effect on the position's breakeven point and be entered for a net credit or minimal debit — adjustments that lock in a guaranteed loss regardless of a stock's recovery are explicitly flagged as poor risk management. Margin is treated qualitatively: ratio spreads and ratio writes with naked legs carry a margin requirement (and the naked exposure that comes with it) that covered structures (verticals, collars, stock-covered ratio spreads) do not.

## Psychology and discipline

The opening chapter frames risk management as psychological armor, using a boxing/martial-arts analogy ("defense wins championships") — most traders rush to learn offense (entries) and ignore defense (exits and adjustments) until a single bad trade erases a string of gains. The authors identify "trade freeze" (refusing to close a losing position out of hope it will recover — "the stock has to move back higher, it cannot just keep falling forever") as a named failure mode, and counter it with the principle that "the market will tell you which way the stock is moving, you cannot tell the market where you want it to move." Trading is framed as a business with distinct start-up, growth, and mature phases, in which positions are "employees" fired (closed) according to a predetermined performance standard rather than emotion; taking losses personally is described as leading to "revenge trading" that compounds the original loss. A trading journal — recording the thesis, strategy, max risk/reward/breakeven, exit plan, and lessons learned after the fact — is recommended as the practical tool for keeping this discipline consistent across trades.

## Chapter map

- Ch 1 — Trade and Risk Management: philosophy of risk and reward, breakeven points, trading as a business (start-up/growth/mature phases), and the SCORE formula for trading success.
- Ch 2 — Tools of the Trader: option pricing factors, time decay, early assignment, implied volatility, synthetic positions, and a review of basic-to-advanced strategies (verticals, straddles/strangles, ratio spreads, backspreads, butterflies) used as building blocks for later adjustments.
- Ch 3 — Long Stock: adjustments to a long stock position as it moves higher, lower, or sideways — protective puts, rolling between puts and bear put spreads, call replacement, covered calls (strike/expiration selection, scaling out), collars and profit collars, ratio writes, short straddles/strangles (including the stock-repair use case), call ratio spreads (including the stock repair ratio spread), and call calendar spreads.
- Ch 4 — Short Stock: the mirror-image adjustment set for short stock — protective calls and protective call spreads, put replacement, covered puts, short collars, put ratio writes, and put ratio spreads (including a short-position repair strategy).
- Ch 5 — Calls and Puts: adjustments to standalone long/short calls and puts — protective puts/calls added to calls, call/put replacement, rolling into verticals, ratio spreads (with the 1:2 vs. 1:3 YHOO worked examples), calendar spreads, synthetic straddles, and repair strategies for losing long calls and puts.
- Ch 6 — Spreads: adjustments to existing vertical and calendar spreads — adding protective legs, converting bull call/bear put spreads into ratio spreads or butterflies, and the Christmas tree repair technique for a losing bull call spread.
- Ch 7 — Combinations: adjustments to straddles and strangles — straps/strips, calendar straddles/strangles, rolling a long straddle into an iron butterfly (regular, diagonal, and partial variants), and defensive adjustments to short straddles/strangles.

## Strengths and caveats

The book's core strength is depth on a topic most options texts treat as an afterthought: every adjustment is shown with exact strikes, premiums, and breakeven math on a consistent example stock, which makes the logic easy to verify and reapply to other numbers. The tradeoff is that this makes the book dense and repetitive — the same handful of adjustment mechanics (roll, collar, ratio-spread, repair) recur across every chapter applied to a different starting position, so a reader can extract the general technique after two or three chapters. All profit/loss calculations assume options are held to expiration and ignore commissions, bid/ask spreads, and the time value of money, which understates real-world adjustment costs — a concern given how many of the strategies involve multiple sequential trades (each with its own slippage). The 2004 publication date means margin-requirement specifics (stated in qualitative "check with your broker" terms, appropriately) and any references to trading infrastructure should not be relied on as current. The book also does not provide backtested win-rate or expectancy statistics for any adjustment; effectiveness is demonstrated case-by-case rather than statistically.

## Who should read it

Best suited to an intermediate-to-advanced options trader who already trades directional and simple spread strategies and wants a systematic reference for what to do when a position moves against (or strongly in favor of) their thesis, rather than a first exposure to options mechanics. Less useful as an entry-strategy or stock-selection guide — it has almost nothing to say about how to pick the underlying trade in the first place, focusing entirely on the follow-up.

## Related books in this library

- [The Options Course: High Profit & Low Stress Trading Methods](https://ninad-k.github.io/trading-playbook/books/fontanills-the-options-course-high-profit-and-low-stress-trading-methods-2nd-ed.html) — broader options curriculum (Greeks, delta-neutral trading, spread construction) that this book's adjustment techniques assume as background knowledge.
- [The Options Course Workbook, 2nd Edition](https://ninad-k.github.io/trading-playbook/books/george-a-fontanills-the-option-course-with-exercise.html) — companion options-strategy primer from the same strategy family (spreads, straddles, ratio backspreads) referenced throughout this handbook's adjustment chains.
- [The Bible of Options Strategies](https://ninad-k.github.io/trading-playbook/books/guy-cohen-the-bible-of-options-strategies.html) — a reference catalog of the base strategies (verticals, collars, ratio spreads, straddles) this book assumes and then shows how to adjust.
- [Profit With Options](https://ninad-k.github.io/trading-playbook/books/lawrence-g-mcmillan-profit-with-options.html) — another practitioner-oriented options strategy and management text that overlaps on collars, spreads, and risk-defined structures.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: options, adjustments, rolling, collars, ratio-spreads, repair-strategies, risk-management, hedging
