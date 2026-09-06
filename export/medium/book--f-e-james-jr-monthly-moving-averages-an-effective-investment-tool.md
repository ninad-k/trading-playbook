# Monthly Moving Averages—An Effective Investment Tool?: the trader's summary

*A 1926-1960 test finds little evidence that monthly moving-average timing improves individual-stock wealth over buy-and-hold once dividends are included.*

**F. E. James, Jr.** · 1968 · Quant, Microstructure & Academic Research · intermediate

*Source coverage: full. PDF pages inspected: 1-13. These are study notes, not verified trading results.*

## Summary

James tests monthly moving-average rules on NYSE common stocks using CRSP month-end price relatives from 1926 through 1960 (pp. 2-4). One data series reinvests cash and property dividends; the other ignores dividends and certain distributions. The study compares each timed portfolio with buying and holding the same stock from the first moving-average signal (pp. 8-10).

The unweighted rule uses a seven-month average, selected as the monthly analogue of a 200-day average, and trades when price moves 2% above or below it. Exponentially smoothed variants use 5% bands, several smoothing constants, and either long-only or long-and-short positions (pp. 6-9). Each simulation begins with $100 and, after its initialization period, switches positions at month-end signal prices (p. 9).

All five experiments using dividend-adjusted data produce lower average terminal wealth than buy-and-hold. The largest reported shortfall is $1,059 for the exponentially smoothed long-and-short rule across 798 stocks. Results that ignore dividends are positive but small and not statistically significant (pp. 11-12). James concludes that the monthly rules showed little reason to expect an investor benefit when the real-world dividend condition was retained (pp. 12-13).

## Key points

- Monthly prices cover stocks only while they were NYSE listed; some experiments require long listing histories (pp. 3-4, 9).
- The comparison aligns each buy-and-hold start with the timed strategy’s first transaction (p. 10).
- Avoiding stocks during cash periods sacrifices dividends and exposure to the sample’s secular rise; shorts also owe dividends (p. 13).
- The study does not test daily or weekly averages, transaction costs, taxes, or risk-adjusted returns (p. 13).

## Actionable rules

1. Include dividends when testing equity timing rules; conclusions reverse when the source uses price-only data (pp. 4, 12-13).
2. Align benchmark and strategy start dates and state signal bands, execution timing, and position constraints before comparison (pp. 8-10).
3. Do not infer that monthly moving averages reduce risk from this study: portfolio-return variance was not compared (p. 13).

## Caveats

The sample ends in 1960 and favors securities with long histories. Month-end fills, costless reinvestment, and omitted trading frictions are simplifying assumptions. The negative result applies to the tested monthly specifications, not every moving-average design.

## Who it is for

System testers and investors studying benchmark design, dividend treatment, and early empirical evidence on moving-average timing.

---
*Educational summary of ideas from the book, written in my own words. Not financial advice. Please buy the book if these notes are useful.*

More notes like this: [https://ninad-k.github.io/trading-playbook/](https://ninad-k.github.io/trading-playbook/) · Tags: moving-averages, market-timing, buy-and-hold, dividends
