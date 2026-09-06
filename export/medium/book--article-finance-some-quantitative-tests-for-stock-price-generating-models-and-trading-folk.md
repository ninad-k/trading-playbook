# Some Quantitative Tests for Stock Price Generating Models and Trading Folklore: the trader's summary

*Osborne tests random-walk, smooth-price, and discrete-transient models with price-volume event coincidences in five historical stock sequences.*

**M. F. M. Osborne** · 1967 · Quant, Microstructure & Academic Research · advanced

*Source coverage: full. PDF pages inspected: 1-21. These are study notes, not verified trading results.*

## Summary

Osborne formalizes chart “folklore” as coincidences among price extrema, large changes, second differences, ranges, and unusually high volume. He compares observed coincidences with counts expected under independence, using Poisson approximations, across five daily, weekly, or monthly sequences (pp. 3-12). The tests offer some support for both random-walk and discrete-transient explanations and evidence against an everywhere smooth, continuously differentiable price process. Results are asymmetric: the discrete-transient and folklore predictions fit price minima better than maxima, individual stocks better than an index, and daily or weekly data better than monthly data (pp. 14-19).

The paper does not establish a trading system. Its strongest non-random findings occur in a deliberately selected, small collection of series, and Osborne acknowledges that the sample favored stocks or periods with enough major moves to analyze (p. 11). A predicted link between volume and large second price differences is weak overall, despite being expected by both models and folklore (pp. 15-16, 19-20).

## Key points

- The “coincident events” method tests whether defined chart events occur together more or less often than independence predicts (pp. 3-5).
- High volume coincides with large moves and ranges in much of the data, but the volume/second-difference result is not significant overall (pp. 14-16).
- Turning-point evidence is substantially stronger at minima than at maxima (pp. 15-17).
- Volume events slightly precede and tend not to follow major extrema, but the effect is small (pp. 17-19).
- Event definitions, graphical measurement, multiple comparisons, and sample selection limit generalization.

## Actionable rules

1. Treat the findings as model evidence rather than buy or sell signals; extrema are identifiable only after subsequent prices occur (pp. 5-8).
2. When reproducing the study, define every event and trial interval before counting coincidences and keep event probabilities sufficiently small for the approximation used (p. 4).
3. Separate results by sampling interval, individual security versus average, and minima versus maxima; the pooled conclusion hides important differences (pp. 14-20).

## Caveats

The five sequences are few, historically selected, and measured graphically. Statistical significance of summed events also assumes independence that the author calls debatable (p. 14). No transaction costs, executable timing, or out-of-sample trading performance are tested.

## Who it is for

Quantitative researchers studying early tests of market randomness, price-volume dependence, and technical-analysis claims.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: random-walk, market-models, volume, turning-points
