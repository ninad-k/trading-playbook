---
author: Anat R. Admati and Paul Pfleiderer
category: Quant, Microstructure & Academic Research
difficulty: advanced
doc_type: paper
one_liner: A market-microstructure model showing why liquidity and informed traders
  both concentrate their trading in the same intraday period, producing the classic
  U-shaped volume/volatility curve.
pages: 38
related:
- persaud-liquidity-black-holes
reviewed_pdf_pages: 1-2 and the propositions checked against the note's summary of
  the model
slug: admati-and-pfleiderer-a-theory-of-intraday-patterns-volume-and-price-variability
source_file: Admati And Pfleiderer-A Theory Of Intraday Patterns - Volume And Price
  Variability.pdf
source_review: partial
tags:
- market-microstructure
- liquidity-trading
- informed-trading
- volume
- u-shape
- academic-paper
tier: B
title: 'A Theory of Intraday Patterns: Volume and Price Variability'
year: 1988
---

## Summary

**Question:** why is trading volume and return variability U-shaped intraday (heavy at the open and close, light at midday), as documented in 1981 NYSE/Exxon data? **Method:** a game-theoretic microstructure model (Kyle/Glosten-Milgrom tradition) with a risk-neutral market maker, informed traders, non-discretionary liquidity traders, and "discretionary" liquidity traders who can choose when to trade within a window. **Finding:** discretionary liquidity traders prefer to trade when the market is "thick" (low price impact), and informed traders are drawn to trade alongside them because competing informed traders benefit liquidity traders — so both groups converge on the same period, producing concentrated volume and, when information acquisition is endogenous, higher return variability and more informative prices there.

## Key points

- Two trader types drive volume: informed traders (private signals) and liquidity traders (needs unrelated to future payoffs).
- **Proposition 1:** equilibria with all discretionary liquidity trading concentrated in one period always exist and are the only ones robust to small parameter changes.
- Market depth (1/λ, "Kyle's lambda") increases with both the variance of liquidity trading and the number of informed traders (competing informed traders erode each other's profits, benefiting liquidity traders).
- With a **fixed** number of informed traders, concentrating liquidity trading raises volume but does not change price informativeness or price-change variance.
- With **endogenous** information acquisition, more traders become informed in the high-liquidity period, making prices more informative and increasing return variance there — matching the empirical U-shape in both volume and volatility.
- Results hold with risk-averse liquidity traders and with correlated liquidity demands, as long as the correlation isn't strongly positive.
- If liquidity traders can split a trade across periods, they concentrate more heavily in the earliest available one, since the market maker can infer later liquidity demand from earlier order flow.
- A numerical calibration to the 1981 Exxon data produces variance-of-price-change estimates close to the observed values.

## Actionable rules

None given — this is a theoretical model, not a trading system. Practical takeaways: (1) price impact is lowest when volume is naturally concentrated, so large discretionary orders are best executed near the open/close; (2) expect more informed-trader competition and faster price discovery at the open and close, so information-driven edges likely decay faster there than at midday.

## Caveats

A stylized theoretical model (risk neutrality assumed in the base case); results are illustrative, not empirically tested rigorously here. Testable hypotheses are proposed but not verified with new data — the Exxon 1981 example is cited only as a plausibility check.

## Who it is for

Quant/microstructure researchers and advanced traders who want the theoretical foundation for why volume and volatility cluster at the open and close, useful for building execution-timing or liquidity-provision strategies.
