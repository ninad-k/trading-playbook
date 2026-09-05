---
title: Market Neutral Equity Long-Short Portfolio Construction
author: Bruce I. Jacobs and Kenneth N. Levy (editors)
year: 2005
slug: marketneutralstrategies--equity-long-short-construction
tier: A
category: Quant, Microstructure & Academic Research
tags: [market-neutral, long-short, pairs-trading, portfolio-optimization, leverage]
difficulty: advanced
doc_type: system
parent: marketneutralstrategies
pages: 304
one_liner: "Jacobs and Levy's integrated long-short optimization: build one portfolio where longs and shorts are chosen jointly, not a long book plus a short book bolted together."
related: [wyser-pratte-guy-risk-arbitrage, paul-wilmott-quantitative-finance]
source_file: "Marketneutralstrategies.pdf"
---

## What it is

A method for constructing an equity portfolio with (approximately) zero sensitivity to the broad market — a portfolio beta near zero — so that its return reduces to the spread between securities held long (expected outperformers) and securities sold short (expected underperformers), independent of whether the market itself rises or falls. The key distinction the chapter draws is between a naive "long-plus-short" portfolio (a long-only book combined with a separately-built short-only book, each still constrained to move toward benchmark weights to control its own risk) and a true "integrated optimization," where the long and short legs are selected jointly in a single optimization using expected returns, return volatilities and cross-security correlations. Only the integrated version fully escapes benchmark-weight constraints and captures the real advantage of being able to short.

## Rules

1. **Initial capital deployment.** For $10 of initial capital, invest ~$9 long and simultaneously sell short ~$9 of other securities, retaining ~$1 (10%) as a cash liquidity buffer. This is comfortably inside Federal Reserve Regulation T's 50% initial-margin requirement for equity shorts (illustrated margin ≈ 55.6%).
2. **Security selection: joint, not sequential.** Do not build a long-only sub-portfolio and a short-only sub-portfolio separately. Select which names to hold long and which to sell short within one optimization that weighs each candidate's expected excess return, its volatility, and its correlation with every other candidate (long and short) simultaneously, plus the investor's risk tolerance.
3. **No benchmark-weight anchor.** Once a benchmark has been used only to estimate each security's systematic (market) sensitivity, discard it for position-sizing purposes. A 1% overweight and a 1% underweight both simply require allocating 1% of capital (long or short) — there is no need to hold "neutral" positions in stocks/sectors the investor has no view on, and no cap (like the ~0.01% weight of a median-cap stock) limiting how far the investor can underweight a disliked name, unlike in long-only.
4. **Neutrality condition.** True beta-neutrality requires that the *systematic risk sensitivities* (not just the dollar amounts) of the long and short books offset — equal dollar amounts long and short is not sufficient if their betas differ. Watch for and correct residual sector or factor tilts (e.g., longs overweight technology relative to shorts) unless deliberately chosen.
5. **Liquidity buffer sizing.** Hold roughly 10% of capital in cash as a liquidity buffer to absorb daily mark-to-market swings on the short book without breaching maintenance margin. Too small a buffer risks forced covering/selling or costly broker-call-rate borrowing; too large a buffer wastes deployable capital.
6. **Rebalancing trigger.** Rebalance back toward equal long/short dollar values (and matched systematic sensitivities) whenever: (a) the market moves enough to leave the account over- or under-collateralized on the short side (lenders return excess collateral on a decline; the account must post more on a rise), or (b) the long and short legs earn a differential return (a favorable spread still requires selling some longs and covering some shorts to restore balance and the target 10% liquidity buffer). A 2% realized long-short return spread on a $9M/$9M book required roughly $0.2M of rebalancing trades in the book's worked example.
7. **Leverage is optional.** The 50%-margin structure above uses no true leverage (equal dollars long/short from the same capital). An investor can choose $50 long/$50 short from $100 capital (unlevered, matching a $100 long-only bet's total capital at risk) up to Reg T's 2:1 maximum, or lever further outside Reg T (e.g., as a hedge fund) — but every added turn of leverage multiplies both expected active return and potential loss and drawdown speed.
8. **Prime broker and shorting mechanics.** Establish a margin account with a prime broker who arranges stock borrows, clears trades, and marks the short book to market daily. Diversify individual short positions across many small names rather than concentrating in a few, to reduce exposure to recall/buy-in risk and short squeezes, particularly in small-cap or hard-to-borrow names.

## Risk

Systematic risk is designed to be near zero, but residual (security-selection) risk, measured as the standard deviation of the long-short return spread, is retained by design — that is the source of the strategy's expected return and must be sized to the investor's risk tolerance via the optimization, not eliminated. Leverage, where used, multiplies this residual risk along with expected return; margin calls on the short book can force untimely covering. Short-specific costs reduce net return versus the gross long-short spread: the short rebate (interest on short-sale proceeds) is typically haircut 25–30bp below the Treasury-bill rate by the lender and prime broker (and can be more, or negative, for hard-to-borrow names); uptick-style restrictions on when a stock can be shorted can delay trade execution versus the model's intended timing; and shares can be recalled by the lender at any time, forcing a buy-in. A fully leveraged (2:1) portfolio incurs roughly double the trading costs of an unlevered long-only portfolio of the same gross capital, so expected returns must clear that higher cost hurdle.

## Caveats

The chapter presents this as a professional/institutional framework requiring prime-brokerage access, optimization software, and reliable factor-risk models — it is not a retail pairs-trading recipe with a specific entry/exit signal, and gives no security-selection alpha model of its own (it assumes the investor already has one). The worked numeric examples (margin percentages, liquidity buffer size, rebalancing amounts) use a hypothetical $10M account and stylized uniform return assumptions; real portfolios have heterogeneous position sizes and correlations that require actual optimization software, not the simplified arithmetic shown. The claimed advantage of "no benchmark-weight constraint" assumes the optimizer's risk model correctly captures each security's true factor exposures — a flawed or incomplete risk model (as in the Askin Capital Management case discussed in the parent book's Chapter 9) can leave a portfolio far less neutral than intended despite dollar-balanced longs and shorts.
