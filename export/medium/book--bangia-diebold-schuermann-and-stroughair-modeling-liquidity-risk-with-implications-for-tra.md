# Modeling Liquidity Risk, With Implications for Traditional Market Risk Measurement and Management: the trader's summary

*Wharton working paper proposing a liquidity-adjusted VaR that adds a spread-based cost-of-liquidity term and a kurtosis correction to standard parametric VaR, showing large underestimation of risk in emerging-market FX without it.*

**Anil Bangia, Francis X. Diebold, Til Schuermann, John D. Stroughair** · 1998 · Quant, Microstructure & Academic Research · advanced

*Source coverage: partial. PDF pages inspected: 4, 7, 11-13, 15-16 (the liquidity-risk model and the currency spread and worst-case tables). These are study notes, not verified trading results.*

## Summary

Question: does ignoring the bid-ask spread cause standard Value-at-Risk (VaR) to understate market risk, especially in emerging markets? Method: the authors split market-value uncertainty into pure return volatility plus an exogenous liquidity-risk term (driven by bid-ask spread volatility), add a kurtosis-based fat-tail correction to parametric VaR, and test the combined model on FX (Yen vs. Thai Baht) and four backtested portfolios around the 1997-98 Asia crisis. Finding: liquidity risk is negligible for the highly liquid Yen (~1-1.5% of total VaR) but reached 16% of total VaR for the Baht pre-crisis; adding both adjustments moved all four backtested portfolios into the BIS "green zone" where the unadjusted model did not.

## Key points

- Standard VaR marks to the bid-ask midpoint; actual liquidation happens at the bid, so ignoring the spread understates realizable loss.
- Two liquidity types: exogenous (market-wide) and endogenous (position-size-driven); the paper models only exogenous risk, since it has available data.
- Cost of liquidity (COL) = price × ½(average relative spread + a × spread volatility); the scaling factor "a" ranges 2.0-4.5 empirically, since spread distributions are far from normal.
- Fat-tail correction θ = 1.0 + φ·ln(kurtosis/3), φ ≈ 0.4 for 1% VaR; θ=1 for a normal distribution.
- FX kurtosis varies widely: Japanese Yen 7.0, British Pound 5.4, up to Indian Rupee 23.2 and Mexican Peso 20.5 (1995-97 sample).
- Worked example: liquidity's share of total VaR was 1.5% (JPY) vs. 16% (THB) pre-crisis (May 1997), falling to 1.0% and 5% post-crisis as pure return volatility rose faster than spread volatility.
- Backtesting four portfolios over 240 days: the liquidity add-on cut VaR violations most in emerging-market portfolios; adding kurtosis on top moved all four into the BIS green zone.

## Actionable rules

1. Add a liquidity cost term (average spread plus ~2-4.5x spread volatility) to VaR rather than relying on the mid-price alone.
2. For thinly-traded or emerging-market instruments, expect liquidity risk to materially inflate true risk (up to ~16% in this paper) relative to liquid instruments.
3. Adjust standard-deviation-based VaR multiples upward for high-kurtosis return series instead of assuming normality.
4. Recompute liquidity and kurtosis adjustments after a regime change (e.g., a currency depegging), since both can shift sharply.

## Caveats

A technical 1998 working paper for bank risk managers, assuming familiarity with parametric VaR, EWMA/GARCH, and BIS backtesting. It models only exogenous liquidity risk (no position-size effects), and its constants (a = 2.0-4.5, φ ≈ 0.4) were fit to late-1990s FX data and are illustrative, not universal.

## Who it is for

Risk managers, quants, or advanced traders needing a concrete way to incorporate bid-ask spread risk and fat tails into VaR, especially for emerging-market or thinly-traded exposure.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: value-at-risk, liquidity-risk, bid-ask-spread, fat-tails, emerging-markets, var-backtesting
