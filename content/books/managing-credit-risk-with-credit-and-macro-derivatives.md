---
title: "Managing Credit Risk with Credit and Macro Derivatives"
author: "Udo Broll, Gerhard Schweimayer & Peter Welzel"
year: 2003
slug: managing-credit-risk-with-credit-and-macro-derivatives
tier: B
category: Quant, Microstructure & Academic Research
tags: [credit-risk, credit-default-swap, macro-derivatives, hedging, banking-theory, academic-research]
difficulty: advanced
doc_type: paper
pages: 21
one_liner: "An academic banking-theory paper deriving optimal hedge rules for a risk-averse bank using credit default swaps and macro derivatives to hedge loan-portfolio credit risk."
related: [credit-risk-modeling-and-valuation-an-introduction, credit-derivatives, derivatives-pricing-and-financial-modelling]
source_file: "Managing Credit Risk With Credit And Macro Derivatives.pdf"
---

## Summary

Question: how should a large, risk-averse commercial bank use credit derivatives (credit default swaps) and "macro derivatives" (contracts on macroeconomic indices) to hedge the credit risk in its loan book, and how does derivative design affect the bank's optimal deposit, loan, and hedge decisions? Data: none — a theoretical model, not an empirical study. Method: the authors extend the industrial-organization microeconomics-of-banking framework (a monopolist bank setting deposit and loan rates) by adding risk aversion, an uncertain default/loss-given-default variable, and a hedge instrument, then solve the bank's expected-utility maximization problem under three CDS designs plus a macro derivative. Finding: whether a bank can neatly separate its deposit/loan decisions from its hedging decisions — and how much of its credit risk it should hedge — depends critically on how closely the derivative's payoff tracks the bank's actual credit losses ("basis risk").

## Key points

- Credit risk is split into two components: the probability of default and the loss given default (LGD); their product is the loss variable the bank actually cares about.
- **Case 1 — CDS with no basis risk** (payoff perfectly negatively correlated with the bank's credit losses): the bank can fully separate its deposit/loan decisions from its hedge decision ("strong separation"), and if the CDS market is unbiased (fairly priced) the bank optimally hedges 100% of its credit exposure.
- **Case 2 — CDS with basis risk** (imperfect correlation): only "weak separation" holds — the bank can still set deposit/loan volumes first and then hedge — but the optimal hedge ratio depends on risk preferences and probabilities, following a beta-style partial-hedge rule.
- **Case 3 — CDS with a fixed, pre-determined payout** (rather than a payout tied to realized losses): no simple hedge rule exists at all; the optimal hedge depends on the bank's degree of "prudence" (third-derivative property of the utility function), and neither strong nor weak separation holds.
- **Macro derivatives** — hedge only the *systematic* (economy-wide) component of credit risk via a macro index (e.g., non-farm payrolls, a retail sales index); mathematically equivalent to a basis-risk CDS (Case 2), yielding a "beta-hedge rule": the bank hedges a fraction β of its risky position, where β is how strongly its loan book's risk loads on the systematic factor.
- Macro derivatives cannot fully hedge credit risk because they deliberately leave the specific (idiosyncratic) risk with the bank — which the authors argue is desirable, since it preserves the bank's incentive to properly monitor its own borrowers (an information-asymmetry argument).
- The authors sketch how a bank-specific macro index could be built from standardized single-indicator products via a linear aggregation function, estimated in practice with a logistic regression of historical default rates on macro variables.
- Real-world context cited: the credit derivatives market grew from about $118 billion (mid-1998) to $693 billion (mid-2001) notional, with credit default swaps the dominant instrument; Deutsche Bank and Goldman Sachs began auctioning macro derivatives on U.S. economic indices in October 2002.

## Actionable rules

None given — this is a theoretical banking-economics model, not a trading or hedging system with numeric parameters. The transferable idea for a credit or macro trader: hedge ratios should be scaled down (a beta-hedge, not a 1:1 hedge) whenever the hedging instrument's payoff is imperfectly correlated with the actual exposure, and a hedge instrument with a fixed/binary payout structure requires a materially more complex (prudence-dependent) sizing decision than one with a payout proportional to realized loss.

## Caveats

Purely theoretical, closed-form banking model (monopolistic bank, single period, no empirical calibration or backtest); conclusions are derived from utility-maximization proofs, not tested against real bank data. Written in 2003, before the 2008 financial crisis reshaped credit derivatives markets and regulation; the optimism about macro derivatives as a hedging innovation did not play out — this market never developed meaningful liquidity.

## Who it is for

Academic and quant readers interested in the theory of bank credit-risk hedging and optimal hedge-ratio derivation; not a practical trading guide.
