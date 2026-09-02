---
layout: post
title: "Stablecoin Payments- Infrastructure, Adoption, and the Future of Global Finance"
description: "1 How Stablecoin Payments Work · 2 Key Blockchain Networks · 3 The Scalability Challenge · Market Data and Evidence"
date: 2026-02-28 21:45:00 +0800
type: post
published: true
status: publish
categories: []
tags:
- Stablecoin Payments
keywords: [Stablecoin Payments]
permalink: /Stablecoin Payments- Infrastructure, Adoption, and the Future of Global Finance/
---
# Stablecoin Payments: Infrastructure, Adoption, and the Future of Global Finance

**Technical Report | February 2026**

---

## Executive Summary

Stablecoins — digital assets pegged to fiat currencies, principally the US dollar — have undergone a fundamental transformation from speculative instruments to core payment infrastructure. In 2024, stablecoins facilitated an estimated **$27.6 trillion** in total transaction value, surpassing the combined processing volume of Visa and Mastercard. By mid-2025, the total market capitalisation of fiat-backed stablecoins reached approximately **$290 billion**, growing more than 60-fold since 2020.

This report assesses the current technical landscape of stablecoin payments, the regulatory environment taking shape across major jurisdictions, key use cases driving adoption, risks and limitations, and strategic implications for financial institutions, fintechs, and businesses.

**Key findings:**

- B2B stablecoin payments are projected to reach **$390 billion in 2025**, more than doubling 2024 volumes.
- Regulatory clarity — through the US GENIUS Act and the EU's MiCA framework — has accelerated institutional adoption.
- Major payment networks including Visa and Mastercard have launched stablecoin-integrated products, signalling mainstream convergence.
- Cross-border payments and treasury management are the primary enterprise use cases, particularly in emerging-market corridors.
- Challenges remain around scalability, consumer-facing UX, interest-bearing restrictions, and the quality of organic transaction data.

---

## 1. Introduction and Background

The global payments infrastructure — built on correspondent banking, SWIFT messaging, and card networks — was largely designed in the 1960s and 1970s. Its limitations are well-documented: cross-border transactions can take two to five business days, carry fees of 2–7%, and operate only within banking hours. Stablecoins represent a structural challenge to these incumbents by leveraging blockchain rails to deliver near-instant, low-cost, programmable value transfer on a 24/7 basis.

A **stablecoin** is a cryptographic token whose value is pegged to an external reference asset — most commonly the US dollar, though euro- and other currency-denominated stablecoins are emerging. The most widely used variants are **fiat-collateralised stablecoins**, meaning each token is backed 1:1 by reserves held in cash, short-term government securities, or equivalent instruments.

The collapse of the algorithmic stablecoin TerraUSD in 2022 served as a pivotal cautionary episode, refocusing the market on reserve-backed models. Today, Tether (USDT) and Circle's USDC dominate the market. By September 2025, stablecoin market capitalisation had surged from roughly $5 billion in 2020 to $290 billion, with initial estimates projecting $310 billion by year-end.

---

## 2. Technical Overview

### 2.1 How Stablecoin Payments Work

A stablecoin payment involves the transfer of a token on a public or permissioned blockchain from a sender's wallet address to a recipient's. The transaction is validated by the network's consensus mechanism (typically proof-of-stake on modern chains), recorded immutably on the ledger, and finalised within seconds to minutes. Settlement is direct and peer-to-peer — there is no intermediary bank updating a proprietary ledger.

**Smart contracts** extend this baseline functionality, enabling programmable payments: escrow arrangements, conditional releases, recurring transfers, and multi-party settlement — all executable without a trusted third party.

### 2.2 Key Blockchain Networks

Stablecoin activity is spread across several Layer-1 blockchains and Layer-2 scaling solutions:

| Network | Key Feature | Stablecoin Share (2025) | Throughput |
|---|---|---|---|
| Ethereum | Largest ecosystem; smart contract pioneer | ~60% of stablecoin market | ~15–30 TPS (L1); thousands via L2 |
| Solana | High speed, low fees; fast growth | ~4.5% (growing rapidly) | ~65,000 TPS |
| Tron | High USDT volume; popular in Asia | Significant USDT share | ~2,000 TPS |
| Layer-2 (Arbitrum, Base, Optimism) | Ethereum scalability via rollups | Growing | Thousands TPS |

Solana's stablecoin supply grew **40%** in the three months following passage of the GENIUS Act, outpacing Ethereum's 27% expansion in the same period. Circle's USDC commands 77.4% of Solana's stablecoin market.

### 2.3 The Scalability Challenge

Mainstream payment adoption requires transaction throughput comparable to or exceeding Visa's ~24,000 transactions per second (TPS) peak capacity. Most Layer-1 blockchains fall short of this threshold. Solutions being deployed include **Layer-2 rollups** (which batch transactions off-chain before settling on-chain), sharding, and application-specific blockchain lanes. Stripe's forthcoming Tempo blockchain and Circle's Arc blockchain — designed with sub-second finality and stablecoin-denominated transaction fees — reflect this trend toward payment-optimised infrastructure.

---

## 3. Market Data and Evidence

### 3.1 Volume and Growth

Stablecoin transaction volumes have grown dramatically across all segments:

| Metric | Value | Source / Period |
|---|---|---|
| Total stablecoin transaction value (2024) | $27.6 trillion | NY Federal Reserve / Visa Onchain Analytics |
| Fiat-backed stablecoin supply (Aug 2025) | ~$238 billion | Visa Onchain Analytics |
| Market cap (Sept 2025) | ~$290 billion | VettaFi / TRM Labs |
| B2B stablecoin payments (2025 projection) | $390 billion | Artemis & Stablecon joint report |
| Year-over-year B2B growth rate | +730% | Artemis & Stablecon |
| Debit/credit card-linked stablecoin transactions YoY | +840% | Artemis & Stablecon |
| Monthly US stablecoin inflows (cross-border) | ~$127 billion | Artemis data |
| Adjusted 'real' user stablecoin payments (2025) | >$9 trillion | a16z report, Oct 2025 |
| Projected market supply by 2030 (base case) | $1.6 trillion | Citi Institute, Apr 2025 |

> **Methodological note:** Research by Visa and Allium Labs suggests that fewer than 10% of raw on-chain stablecoin transaction volumes are organic (i.e., initiated by real users rather than bots, arbitrageurs, or DeFi protocol loops). The $9 trillion figure cited by a16z reflects an adjusted, 'real-payment' methodology.

### 3.2 Institutional Adoption

A March 2025 survey of 295 payments executives by Fireblocks found that stablecoins already accounted for nearly half of transaction volume on its platform. Fireblocks processes 15% of global stablecoin volume — more than 35 million transactions per month — across over 300 banks and payment providers. Notably, **88% of respondents said regulation was no longer a barrier to adoption**.

---

## 4. Regulatory Landscape

### 4.1 United States: The GENIUS Act

The Guiding and Establishing National Innovation for US Stablecoins (GENIUS) Act established a federal framework for 'payment stablecoins' in the United States. Key provisions:

- Require **1:1 reserve backing** with high-quality liquid assets
- Mandate regular audits and AML/CFT compliance
- **Prohibit stablecoin issuers from paying interest** to holders
- Establish federal licensing requirements for large issuers (>$10B in circulation)

The Act has been widely credited with unlocking institutional participation, as banks that had previously watched from the sidelines began designing their own stablecoin products.

### 4.2 European Union: MiCA

The EU's Markets in Crypto-Assets Regulation (MiCA), fully implemented in December 2024, requires that issuers of **e-money tokens** (the MiCA term for fiat-backed stablecoins) be regulated e-money institutions or credit institutions. Only 18% of European survey respondents view regulation as a barrier to adoption — the lowest of any major region — reflecting MiCA's success in providing compliance clarity. Circle obtained a CASP (Crypto-Asset Service Provider) licence in France, becoming a reference entity for MiCA compliance. Société Générale's EURI is among the first MiCA-compliant euro-denominated stablecoins.

### 4.3 Hong Kong and Asia-Pacific

Hong Kong passed a **Stablecoin Ordinance** in May 2025, requiring all issuers of Hong Kong dollar-backed stablecoins to obtain a licence from the Hong Kong Monetary Authority (HKMA). Key requirements mirror the GENIUS Act's structure: high-quality liquid reserve assets, AML/CFT compliance, and regular audits.

---

## 5. Case Studies and Industry Examples

### 5.1 Visa and Mastercard: Network Integration

In April 2025, Visa announced a partnership with Bridge (a Stripe-acquired platform) enabling fintech developers globally to issue Visa-branded cards that **convert stablecoin balances to local fiat at the point of sale**. Mastercard partnered with MoonPay to allow users to link stablecoin-funded digital wallets to their Mastercards, enabling stablecoin spend at any Mastercard-accepting merchant worldwide. These integrations effectively extend stablecoin liquidity into the existing 100+ million merchant acceptance network.

### 5.2 Stripe: Stablecoin Financial Accounts

Stripe launched **Stablecoin Financial Accounts** for businesses in over 100 countries, facilitating USDC-denominated treasury management and cross-border settlement. Its forthcoming Tempo blockchain is purpose-built for payments, featuring dedicated payment lanes and high throughput. Stripe reported $1.9 trillion in total payment volume in 2025.

### 5.3 ALT 5 Sigma: B2B Cross-Border Growth

ALT 5 Sigma, a Nasdaq-listed B2B crypto payments processor, grew its transaction volume from $39 million in 2020 to over $2 billion in 2024, using stablecoins as the settlement layer. Working with Fireblocks' infrastructure for wallet security and high-throughput demands, ALT 5 serves as a concrete example of stablecoins enabling SME access to institutional-grade cross-border payment infrastructure.

### 5.4 Emerging Markets: Latin America and Africa

In high-inflation economies and markets with limited banking infrastructure, stablecoins are functioning as a store of value and remittance tool. Conduit reports growing B2B adoption among import/export businesses in Latin America and Africa, where dollar-pegged stablecoins allow businesses to avoid local currency volatility while moving funds across borders at a fraction of the cost of traditional wire transfers.

---

## 6. Challenges and Risks

- **Scalability:** Public blockchains have not yet demonstrated the throughput required for mass consumer payments. Layer-2 solutions are maturing but introduce additional complexity.
- **User Experience:** Wallet management, private key security, and on/off-ramp friction remain barriers to mainstream consumer adoption.
- **Data Quality:** Raw on-chain transaction data overstates genuine payment activity. Bots, DeFi loops, and wash activity inflate headline figures.
- **Interest-Bearing Restrictions:** The GENIUS Act prohibits stablecoin issuers from paying yield. This limits their attractiveness as a savings instrument and may drive demand toward yield-bearing tokenised money market funds instead.
- **Issuer Concentration Risk:** Circle's revenue is 95–99% derived from interest on USDC reserves. Rate cuts materially impact issuer viability without corresponding growth in stablecoin supply.
- **Counterparty and Reserve Risk:** Stablecoin holders are exposed to the credit quality of reserve assets and the operational soundness of the issuer. The TerraUSD collapse in 2022 demonstrated how quickly confidence can erode.
- **Regulatory Fragmentation:** While the US and EU have made significant progress, regulation varies sharply across Asia, Latin America, and Africa, creating compliance complexity for global operators.
- **CBDC Competition:** Central bank digital currencies — including China's e-CNY and the ECB's forthcoming digital euro — may compete for the same use cases and enjoy sovereign backing.

---

## 7. Discussion and Implications

2025 marks an inflection point for stablecoin payments. The convergence of regulatory clarity, institutional onboarding, and network integrations has moved stablecoins from 'experiment' to 'infrastructure' across multiple payment segments.

For banks, stablecoins represent both a competitive threat and a strategic opportunity. Fintechs were early movers in capturing payment flows that once ran through bank channels. A joint stablecoin consortium among major US banks — proposing a fully collateralised digital token redeemable through member banks — illustrates how incumbents are responding. The choice is no longer whether to participate, but how to do so within regulatory boundaries.

The emergence of **application-specific stablecoins** is particularly significant. Rather than a one-size-fits-all dollar token, 2025 saw the proliferation of purpose-built tokens targeting B2B invoicing, retail commerce, cross-border remittance, and institutional treasury. This fragmentation mirrors the diversity of payment use cases and suggests that the future payment landscape will be multi-stablecoin rather than dominated by a single token.

The **interest-bearing debate** — currently resolved against yield at the issuer level in the US — is likely to remain contested. Tokenised money market funds (such as BlackRock's BUIDL fund at $2.9 billion AUM) are emerging as a practical workaround: stablecoins for payments, tokenised T-bill funds for yield.

---

## 8. Recommendations and Conclusions

### For Financial Institutions

- Pilot stablecoin settlement for high-volume cross-border B2B corridors where traditional rails are slowest and most expensive.
- Engage with regulatory frameworks proactively — seek CASP licences under MiCA and monitor GENIUS Act compliance guidance.
- Invest in blockchain-compatible infrastructure: custody solutions, compliance APIs, and treasury management integrations.

### For Fintechs and Payment Processors

- Integrate with established stablecoin on/off-ramp infrastructure (Circle, Zero Hash, Fireblocks) rather than building from scratch.
- Target underserved cross-border corridors — particularly in Latin America, Sub-Saharan Africa, and Southeast Asia — where stablecoin advantages are most pronounced.
- Design for UX parity with traditional payments; the technical superiority of stablecoins is insufficient if the user experience is inferior.

### Conclusions

Stablecoins have crossed the threshold from niche crypto instrument to legitimate payment infrastructure. The $27.6 trillion in 2024 transaction volume, the engagement of Visa, Mastercard, Stripe, and major banks, and the passage of comprehensive legislation in the US, EU, and Hong Kong collectively confirm that the question is no longer *whether* stablecoins will reshape global payments — it is how quickly and in what form.

Financial institutions, payment processors, and businesses that begin building stablecoin capabilities now will be better positioned to capture the efficiency gains, new market access, and product innovation that this infrastructure enables. Those that delay risk ceding ground to more agile competitors in what may prove to be the most significant structural shift in payments since the introduction of electronic card networks.

---

## References

1. [Visa Onchain Analytics — How New Regulations Impact the Future of Stablecoins](https://corporate.visa.com/en/sites/visa-economic-empowerment-institute/how-new-regulations-impact-stablecoins.html)
2. [Fireblocks — Global Insights: Stablecoin Payments & Infrastructure Trends (May 2025)](https://www.fireblocks.com/report/state-of-stablecoins)
3. [McKinsey & Company — The Stable Door Opens: How Tokenized Cash Enables Next-Gen Payments (July 2025)](https://www.mckinsey.com/industries/financial-services/our-insights/the-stable-door-opens-how-tokenized-cash-enables-next-gen-payments)
4. [ETA Strategic Leadership Forum — Stablecoins Are Quietly Reshaping the Future of Payments (Sept 2025)](https://etaslf.com/stablecoins-are-quietly-reshaping-the-future-of-payments-is-your-business-ready/)
5. [VettaFi — Stablecoins: The Digital Assets Revolutionizing Global Payments](https://www.vettafi.com/insights/indexing-article-stablecoins-the-digital-assets-revolutionizing-global-payments)
6. [Phemex News — B2B Stablecoin Payments to Reach $390B in 2025 (Feb 2026)](https://phemex.com/news/article/b2b-stablecoin-payments-to-hit-390-billion-in-2025-doubling-2024-figures-62723)
7. [FinTech Weekly — Stablecoins in 2025: How Regulation, Banks, and Fintechs Turned Digital Money Into Global Infrastructure](https://www.fintechweekly.com/magazine/articles/stablecoins-2025-regulation-banks-fintech-digital-money-infrastructure)
8. [American Banker — What 2025's Big Stablecoin Trends Reveal About the Future of Payments (Dec 2025)](https://www.americanbanker.com/news/what-2025s-big-stablecoin-trends-reveal-about-the-future-of-payments)
9. [Euronews — As Stablecoins Rise, How Are Governments Responding Worldwide? (Jan 2026)](https://www.euronews.com/business/2026/01/17/stablecoins-are-growing-but-how-are-governments-responding)
10. [Federal Reserve Bank of New York — The Future of Payment Infrastructure Could Be Permissionless (Nov 2025)](https://libertystreeteconomics.newyorkfed.org/2025/11/the-future-of-payment-infrastructure-could-be-permissionless/)