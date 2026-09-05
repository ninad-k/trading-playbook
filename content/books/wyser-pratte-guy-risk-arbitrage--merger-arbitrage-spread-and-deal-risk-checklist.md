---
title: "Merger Arbitrage Spread Calculation and Deal-Risk Checklist"
author: Guy P. Wyser-Pratte
year: 2009
slug: wyser-pratte-guy-risk-arbitrage--merger-arbitrage-spread-and-deal-risk-checklist
tier: A
category: "Options, Futures & Derivatives"
tags: [risk-arbitrage, merger-arbitrage, spread-calculation, deal-risk, hedging]
difficulty: advanced
doc_type: system
parent: wyser-pratte-guy-risk-arbitrage
pages: 305
one_liner: "How to calculate merger parity, spread, and annualized return, and the enumerated risks that must be weighed before taking a long-target/short-acquirer arbitrage position."
related: [armelle-guizot-the-hedge-fund-compliance-and-risk-management-guide, article-market-neutral-investing-long-short-hedge-fund-strategies-joseph-g-nicholas-2000]
source_file: "Wyser-Pratte, Guy - Risk Arbitrage.pdf"
---

## What it is

The procedure a risk arbitrageur uses to decide whether, and how large, a position to take in an announced stock-for-stock (or securities-package) merger: calculate what the offered package is really worth (parity), compare it to the target's current price (the spread), estimate how long capital will be tied up, annualize the return, and weigh that return against an enumerated list of deal-specific risks before committing capital.

## Rules

**1. Gather deal information before valuing anything.** Confirm the exchange ratio and security types, shareholder-meeting dates, and which regulatory approvals apply (SEC, IRS tax ruling, antitrust). Verify independently (proxy actually filed, tax-ruling application actually filed) rather than trusting company or press statements — "a deal is worth neither what the newspapers nor what the merger parties say it is worth... generally worth much less."

**2. Calculate parity.** Parity = Σ (exchange ratio for each offered security × its current market price). Example: Canteen Corp. merging into ITT at 0.2686 ITT common + 0.1930 Series K convertible preferred per share, ITT common at $52.75, K preferred at $98.75: Parity = 0.2686×$52.75 + 0.1930×$98.75 = $14.17 + $19.06 = $33.23.

**3. Calculate the spread.** Spread = Parity − current target price, after adjusting the cost basis for net carrying cost (financing cost of the long leg minus the dividend differential between legs). Example: buy target at $45, short acquirer at $50, 1-for-1, 3-month close, 7% financing, target pays $1 dividend, acquirer $0.50. Carrying cost = ¼×7%×$45 = $0.79; net carrying cost = $0.79 − $1.00 + $0.50 = $0.29; adjusted cost = $45.29; spread = $50 − $45.29 = $4.71.

**4. Estimate time to close** via the standard approval sequence: preliminary agreement → definitive agreement → audit → simultaneous IRS tax-ruling application and antitrust (Hart-Scott-Rodino) filing → SEC proxy clearance (4-6 weeks) → proxy mailed, meeting set (~3 weeks' notice) → shareholder vote → IRS tax ruling (simple ~90-100 days, complex ~100-120+ days) → legal closing. Deals needing extra regulatory approval (FCC, ICC, Federal Reserve, CAB) can add months to years.

**5. Annualize the return.** Annualized ROI = (Spread ÷ Adjusted cost) × (12 ÷ months to close). Example: $4.71 ÷ $45.29 × 4 = 41.6% per annum before taxes.

**6. Set a required-return threshold and walk away below it.** Period rule of thumb: aim for ~40% annualized, settle for ~30% given inevitable delays; a lower spread may be acceptable if risk is very low, a high headline spread may not be enough if antitrust intervention is plausible or standalone value is far below the current price.

**7. Deal-risk checklist — weigh each before sizing a position:**
- **Double price risk** — premium (10-100%) in the long price can evaporate on a broken deal; a short-covering rally in the acquirer can hit the short leg at the same time.
- **Alteration of terms** — a changed exchange ratio or security mix can eliminate the projected spread.
- **Sharp acquirer price move (either direction)** — a rise raises the effective premium paid and renegotiation risk; a fall risks target-side pushback.
- **Competing bids** — favorable long the target, but can force a costly short-cover on the original acquirer leg.
- **Shareholder dissent / appraisal rights** — nuisance suits and, where material, a real chance of termination if too many shareholders exercise appraisal rights.
- **Financial-warranty breaches** — a "no material adverse change" clause triggered by target-financial deterioration between signing and closing.
- **Tax-ruling risk** — a small chance of an unfavorable IRS ruling, or insider tax problems affecting a key vote.
- **Governmental intervention** — a DOJ/FTC injunction, often sought at the "11th hour"; usually fatal to the deal.
- **Unusual delay, personality clashes, freeze-in risk** — administrative/procedural delay, management friction over post-merger roles, or a controlling shareholder squeezing out minority holders unfavorably.

**8. Take the position with the short leg as the hedge.** Buying the target and shorting the acquirer converts market-direction exposure into deal-completion exposure only. Sequence the legs by market conditions: short first in a falling or static market, buy the target first in a rising market. Trade small lots (300-500 shares, the book's period example) rather than large blocks unless the offsetting leg is immediately available in matching size.

**9. Turn (close) the position early when most of the spread is captured.** If the spread narrows to capture most of the expected profit well before the scheduled close, closing out and redeploying into a fresh spread usually beats holding for the smaller remaining annualized gain.

## Risk

The position is sized to be "at risk of the deal, not at risk of the market" — the short leg exists to remove general market exposure so P&L reflects only the deal's completion probability and timing. No formal percent-of-capital rule is given; sizing is bounded by short-borrow availability, liquidity in both legs, and the checklist above. The single most severe risk event is a DOJ/FTC injunction: both parties are typically unwilling to fight a prolonged court battle, so an injunction is close to deal-killing regardless of the deal's merits.

## Caveats

Every timeline here (IRS turnaround, SEC proxy clearance, Hart-Scott-Rodino waiting periods, "short exempt" margin treatment) reflects the regulatory environment of the book's source periods (1960s-2000s) and must be re-verified against current rules. The 40%/30% return targets are tied to the interest-rate and deal-supply environment described in the text ("spread squeezing" when many arbitrageurs compete for few deals), not a fixed benchmark. The method assumes a conventional friendly stock-for-stock or cash merger; hostile deals and complex multi-security packages (convertibles, contingent value rights) need the adjustments covered elsewhere in the source book, not this base procedure alone.
