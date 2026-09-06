# Liquidity Black Holes: the trader's summary

*A global-game model shows how private loss limits can make selling mutually reinforcing and create a sharp V-shaped liquidity event.*

**Stephen Morris and Hyun Song Shin** · 2003 · Quant, Microstructure & Academic Research · advanced

*Source coverage: full. PDF pages inspected: 1-28. These are study notes, not verified trading results.*

## Summary

Morris and Shin model short-horizon traders who hold a risky asset but face privately known loss limits. A risk-averse market-making sector supplies a downward-sloping residual demand curve, so aggregate selling lowers the execution price. When a trader fears that other traders’ sales will push price through their limits, selling becomes mutually reinforcing, analogous to a bank run (pp. 1–8). Global-game reasoning yields a unique trigger point rather than multiple self-fulfilling equilibria. The model predicts a sharp V-shaped price path, high turnover, and a stronger rebound when market illiquidity is high (pp. 20–22).

## Key points

- The market-maker price is `p = v − c·s`, where `s` is aggregate sales and `c = γσ²` measures illiquidity (p. 7).
- Each trader has a private stop price `qᵢ`; dismissal occurs when market price falls below that limit (pp. 7–8).
- A seller’s expected execution price declines with aggregate sales, making a rush to exit strategically contagious (pp. 8–10).
- With nearly common loss limits, the fraction selling jumps toward 1 below the trigger and toward 0 above it (pp. 15–20).
- The resulting event resembles a liquidity black hole: selling causes more selling even without new fundamental information (pp. 1–5, 20–22).
- The rebound is larger when `c` is larger because the market has less capacity to absorb order flow (pp. 20–21).
- Loss-limit changes create externalities: one trader’s limit can alter other traders’ optimal behavior and market volatility (p. 22).

## Actionable rules

1. None given. This is a theoretical model, not a signal or execution algorithm.
2. As a risk implication, stress-test positions against correlated stop-outs and price impact; the model’s trigger is endogenous to other traders’ exits (pp. 7–10, 20–22).

## Caveats

The model has two trading dates, stylized trader types, exogenous loss limits, and a linear residual demand curve (pp. 5–8). It does not calibrate the trigger to a live market or model order-book replenishment dynamics. The predicted V shape is an implication of assumptions, not a universal chart pattern.

## Who it is for

Systemic-risk researchers, portfolio managers, and execution traders designing stress tests for crowded positions and correlated stops.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: liquidity, market-stress, feedback, stop-loss, volatility
