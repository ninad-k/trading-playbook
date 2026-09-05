---
title: A New Interpretation of Information Rate
author: J. L. Kelly Jr.
year: 1956
slug: kellybetting
tier: B
category: Money Management & Position Sizing
tags: [kelly-criterion, position-sizing, information-theory, bankroll-growth, probability, academic-paper]
difficulty: advanced
doc_type: paper
pages: 10
one_liner: "The original Bell System Technical Journal paper deriving the Kelly criterion: bet a fraction of capital proportional to your edge to maximize long-run exponential growth."
related: [money-management-report-van-tharp, forex-money-management]
source_file: "kellybetting.pdf"
---

## Summary

Question: if a gambler (or investor) has an information advantage over posted odds and can reinvest winnings repeatedly, how much of his capital should he bet on each event to grow his fortune fastest over the long run? Method: Kelly models a gambler receiving symbols over a noisy communication channel (an analogy for "inside information") who bets a fixed fraction of capital each round at given odds, and derives the betting fraction that maximizes the expected exponential growth rate, G, of capital as the number of bets goes to infinity. Data: purely mathematical/theoretical (information theory and probability), not an empirical market study. Finding: betting a fixed fraction ℓ = 2q−1 on a fair-odds even-money bet with win probability q (equivalently, the general Kelly fraction f* = edge/odds for arbitrary odds) maximizes long-run growth, and this maximum growth rate equals Shannon's channel transmission rate — i.e., the value of "inside information" to a reinvesting gambler is mathematically identical to its information-theoretic bit rate.

## Key points

- Betting the gambler's entire capital every round maximizes expected capital in a single step but leads to eventual ruin with probability one over repeated bets — expectation-maximizing and growth-maximizing are different objectives.
- The correct objective is to maximize the expected value of the logarithm of capital (not the expected capital itself), because log-capital is additive across repeated bets and obeys the law of large numbers.
- For a simple even-money bet with win probability q and loss probability p=1−q, the optimal fraction to bet is ℓ = q − p; betting this fraction each round yields the maximum growth rate G = 1 + p·log(p) + q·log(q), which equals Shannon's information rate R for that channel.
- For arbitrary "fair" odds (odds equal to 1/probability), the optimal betting fraction on each outcome equals the gambler's own estimated conditional probability of that outcome given his information — i.e., bet in proportion to true probability, ignoring the posted odds entirely.
- If odds are not fair (mispriced relative to true probabilities), any deviation from fair odds increases the gambler's achievable growth rate — mispricing is where the edge comes from.
- When there is a "track take" (a transaction cost / house edge deducted from the pool), the optimal strategy becomes more complex: bets are only placed on outcomes where the perceived edge (p(s)·odds) exceeds a threshold, and some capital may be optimally left unbet.
- The paper explicitly notes the model requires two conditions to apply beyond gambling: (1) the ability to reinvest profits, and (2) the ability to vary the amount invested across different opportunities — conditions satisfied by trading/investing generally, not just wagers.

## Actionable rules

1. Do not size a bet/position to maximize expected value alone; maximizing expected value each round leads to ruin with repeated bets — maximize expected log-capital instead.
2. For a binary bet at even odds, the growth-optimal fraction of capital to risk is ℓ = (probability of winning) − (probability of losing); e.g., a 60%/40% edge implies risking 20% of capital, not 100% or an arbitrary fixed amount.
3. In the general case (arbitrary payout odds), size each bet in proportion to your estimated true probability of that outcome, not the posted/market odds — this is the growth-maximizing allocation regardless of what the market is pricing.
4. Only take a bet/position where your edge is genuinely positive after costs; when a "track take" (transaction costs, spread, commission) is present, the model shows it is sometimes optimal to leave capital unbet on marginal-edge opportunities rather than force a bet.
5. No specific market-trading numbers (stops, entries, timeframes) are given — this is a mathematical foundation for position sizing that must be paired with an actual edge-estimation method to be applied to trading.

## Caveats

This is the original 1956 information-theory paper (not a trading book) — it uses the language of a gambler with a private communication channel as an analogy, and the math assumes known, stable probabilities and repeatable, independent bets, none of which hold exactly in real markets where edge estimates are themselves uncertain and returns are not simple win/loss outcomes. Full Kelly sizing is also known (from later literature, not stated here) to produce large drawdowns in practice, which is why traders commonly use a fraction of the full Kelly bet. Readers should treat this as the theoretical foundation for the wider Kelly-criterion literature applied to trading, not a ready-to-use position-sizing formula.

## Who it is for

Quantitatively-inclined traders and researchers who want the original derivation behind the Kelly criterion for position sizing; not a practical how-to guide on its own.
