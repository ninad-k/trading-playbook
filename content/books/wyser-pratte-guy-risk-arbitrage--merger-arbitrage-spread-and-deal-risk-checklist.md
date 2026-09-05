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

**1. Gather deal information before valuing anything.** Confirm exchange ratio and security types, dates of shareholder meetings, where major stock blocks are held, and which regulatory approvals are required (SEC, IRS tax ruling, antitrust, and any industry-specific regulator). Verify claims independently (e.g., confirm the proxy has actually been filed with the SEC, the tax-ruling application actually filed with the IRS) rather than trusting company or press statements — "a deal is worth neither what the newspapers nor what the merger parties say it is worth... generally worth much less."

**2. Calculate parity.** Parity = Σ (exchange ratio for each offered security × that security's current market price).
Example from the text: Canteen Corp. merging into ITT at 0.2686 ITT common + 0.1930 Series K convertible preferred per Canteen share, with ITT common at $52.75 and K preferred at $98.75:
Parity = 0.2686 × $52.75 + 0.1930 × $98.75 = $14.17 + $19.06 = $33.23.

**3. Calculate the spread and gross return.** Spread = Parity − current target price. Adjust the cost basis for net carrying cost (financing cost of the long position minus any dividend differential between long and short legs) before computing the percentage spread.
Example: buy target (B) at $45, short acquirer (A) at $50, 1-for-1 exchange, 3-month expected close, 7% financing rate, target pays $1 dividend, acquirer pays $0.50. Carrying cost = 1/4 × 7% × $45 = $0.79; net carrying cost after dividend offset = $0.79 − $1.00 + $0.50 = $0.29; adjusted cost = $45.29; spread = $50 − $45.29 = $4.71.

**4. Estimate time to close** by walking the standard approval sequence: preliminary agreement → definitive agreement → audit → simultaneous IRS tax-ruling application and antitrust (Hart-Scott-Rodino) filing → SEC proxy clearance (4-6 weeks if no major deficiencies) → proxy mailed, shareholder meeting set (~3 weeks' notice) → shareholder vote → IRS tax ruling received (simple ruling ~90-100 days from application, complex ruling ~100-120+ days, backlog-dependent) → legal closing. Deals requiring additional regulatory approval (FCC, ICC, Federal Reserve, CAB, Federal Maritime Commission, etc.) can take many months to years longer.

**5. Annualize the return.**
Annualized ROI = (Spread ÷ Adjusted cost) × (12 ÷ estimated months to close).
Example: $4.71 spread ÷ $45.29 adjusted cost × 4 (three-month periods per year) = 41.6% per annum before taxes.

**6. Set a required-return threshold and walk away below it.** The book's period rule of thumb: aim for ~40% annualized, settle for ~30% given inevitable delays; a lower spread (e.g., ~20%) may still be acceptable if the assessed risk is very low, while a high headline spread (e.g., 60%) may not be enough if antitrust intervention is plausible or the standalone value without the deal is far below the current price.

**7. Deal-risk checklist — weigh each before sizing a position:**
- **Double price risk** — premium (10-100%) embedded in the long price can evaporate on a broken deal; a large short-covering rally in the acquirer on deal-break can hit the short leg simultaneously.
- **Alteration of terms** — a changed exchange ratio or security mix (e.g., common swapped for debentures + warrants) can eliminate the projected spread.
- **Sharp rise in acquirer's price** — increases parity and the effective premium being paid, straining the deal and raising renegotiation risk.
- **Sharp fall in acquirer's price** — reduces parity, risking target-side pushback or renegotiation.
- **Competing bids** — a bidding contest is favorable long the target but can force a costly short-cover on the original acquirer leg.
- **Shareholder dissent / appraisal rights** — nuisance suits and, where appraisal rights are material, a real chance of deal termination if too many shareholders exercise them.
- **Financial-warranty breaches** — a "no material adverse change" clause can be triggered by deterioration in the target's financials between signing and closing.
- **Tax-ruling risk** — a small but real chance of an unfavorable IRS ruling on tax-free status, or insider-specific tax problems affecting a key vote.
- **Governmental intervention** — Justice Department or FTC injunction request, often made at the "11th hour"; a granted injunction is usually fatal to the deal even without a full court fight.
- **Unusual delay** — administrative backlog, inexperienced staff, or extended SEC scrutiny.
- **Personality clashes** — friction between the two companies' management teams over post-merger roles and titles.
- **Freeze-in risk** — a controlling shareholder restructuring terms to squeeze out minority holders unfavorably.

**8. Take the position with the short leg as the hedge.** Buying the target and shorting the acquirer converts market-direction exposure into deal-completion exposure only. Sequence the two legs by market conditions: short the acquirer before buying the target in a falling market; buy the target before shorting the acquirer in a rising market; short first in a static market. Position in small lots (300-500 shares was the book's period example) rather than large blocks unless the offsetting leg is immediately available in matching size, to avoid uncompensated market risk from an unhedged interval.

**9. Turn (close) the position early when most of the spread is captured.** If, well before the scheduled close, the spread has narrowed to capture most of the expected profit, closing out and redeploying capital into a fresh spread is usually preferable to holding for the smaller remaining annualized gain.

## Risk

The position is explicitly sized to be "at risk of the deal, not at risk of the market" — the short leg exists specifically to remove general market exposure so that the P&L reflects only the deal's completion probability and timing. No formal percent-of-capital sizing rule is given; sizing is bounded practically by short-borrow availability, liquidity/supply in both legs, and the arbitrageur's own risk assessment of the checklist above. Historically, the most severe single risk event is a Justice Department or FTC injunction, since both parties are typically unwilling to fight a prolonged court battle, making an injunction close to a deal-killing event regardless of the deal's underlying merits.

## Caveats

Every timeline in this method (IRS ruling turnaround, SEC proxy clearance, Hart-Scott-Rodino waiting periods, margin/capital-charge treatment of "short exempt" positions) reflects the regulatory environment of the book's source periods (1960s-2000s) and must be re-verified against current rules before use — none of these procedural specifics should be assumed current. The 40%/30% annualized "rule of thumb" return target is tied to the interest-rate and deal-supply environment described in the text (spreads compress when many arbitrageurs compete for few deals, "spread squeezing") and is not a fixed benchmark independent of market conditions. The method assumes a conventional friendly or negotiated stock-for-stock or cash merger; hostile deals, all-cash deals, and complex multi-security packages (convertibles, contingent value rights) require the adjustments briefly covered elsewhere in the source book (tender offers, convertible-security treatment) rather than this base procedure alone.
