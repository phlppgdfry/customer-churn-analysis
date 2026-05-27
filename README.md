# 📉 Customer Churn Analysis — SaaS Platform

![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Type](https://img.shields.io/badge/Type-Data%20Analysis-blue)
![Domain](https://img.shields.io/badge/Domain-SaaS%20%7C%20B2B-purple)

> **Problem statement:** 31% of SaaS customers cancel their subscription within 90 days. Annual revenue impact: €240,000. This analysis identifies the root causes, quantifies the impact per segment, and provides prioritized recommendations expected to reduce churn by 40%.

---

## 📌 Business Context

**Company profile:** B2B SaaS platform — project management tool for SMEs (10–200 employees).  
**Pricing model:** Monthly subscription (€29 / €79 / €199 per tier).  
**Churn definition:** No active subscription after 90 days from signup.

**Why this matters:**

| Impact | Value |
|---|---|
| Monthly churn rate | 10.3% |
| Annual churn rate | 31% |
| Estimated ARR at risk | €240,000 |
| Cost to acquire 1 new customer (CAC) | €180 |
| Cost to retain 1 existing customer | €22 |
| Retention ROI vs acquisition | **8.2x** |

Retaining an existing customer is 8x cheaper than acquiring a new one. Every 1% improvement in 30-day retention = ~€7,800 in recovered annual revenue.

---

## 🔍 Methodology

```
1. DATA COLLECTION
   └── Export: 12 months of subscription events (signup, upgrade, downgrade, cancel)
   └── Source: Stripe + internal CRM + NPS exit surveys (n=412)

2. SEGMENTATION
   └── By tier (Starter / Pro / Business)
   └── By company size (1–10 / 11–50 / 51–200 employees)
   └── By signup channel (organic / paid / referral)
   └── By cohort (monthly, 6 cohorts analyzed)

3. ROOT CAUSE ANALYSIS
   └── 5 Why's framework on top churn segments
   └── Exit survey clustering (NLP on free-text, n=412)
   └── Usage pattern analysis (feature adoption vs churn correlation)

4. PRIORITIZATION
   └── Impact × Effort matrix
   └── Quick wins vs strategic initiatives separated

5. RECOMMENDATIONS
   └── Validated against comparable SaaS benchmarks (OpenView, ChurnZero 2024 report)
```

---

## 📊 Key Findings

### Finding 1 — Churn is front-loaded

```
Day 1–30:   ████████████████  47% of all churners
Day 31–60:  ████████          24% of all churners
Day 61–90:  ██████████        29% of all churners
```

**Conclusion:** If a customer doesn't find value in the first 30 days, they're unlikely to stay. Onboarding is the critical window.

### Finding 2 — Root Cause Breakdown

| Root Cause | % of Churners | Segment Most Affected | Effort to Fix |
|---|---|---|---|
| Onboarding too complex | 44% | Starter tier, 1–10 employees | Medium |
| Feature-expectation mismatch at signup | 28% | Pro tier, paid channel | Low |
| Price/value imbalance | 18% | Starter tier | High |
| Poor customer support experience | 10% | All tiers | Medium |

### Finding 3 — Feature Adoption Predicts Retention

Customers who used **3+ core features** in their first 14 days churned at only **8%** vs **41%** for those who used 0–1 features.

**Core features correlated with retention:**
1. Team invitation (sent ≥1 invite in Week 1) → 3.2x retention lift
2. First project created within 24h → 2.1x retention lift
3. Integration connected (Slack, Jira, etc.) → 1.8x retention lift

---

## ✅ Recommendations (Prioritized)

### P1 — Simplify Onboarding (Quick Win | 30-day impact)

**Problem:** Current onboarding has 12 steps before reaching the core product.  
**Solution:** Reduce to 3 steps ("Jobs to be done" framework). Guide user to first value moment within 5 minutes.

**Implementation:**
- Step 1: "What's your main goal?" (3 options — project tracking / team collaboration / client reporting)
- Step 2: Create first project (template-guided)
- Step 3: Invite one team member

**Expected impact:** −18% churn in 30-day segment. Validated against Intercom's onboarding benchmark study (2024).

---

### P2 — Fix Feature-Expectation Mismatch (Strategic | 60-day impact)

**Problem:** 28% of churners from paid channels expected features not in their tier.  
**Root cause:** Pricing page doesn't clearly differentiate tiers; sales/marketing overpromises.

**Solution:**
- Rewrite pricing page with "This plan is for you if..." use-case framing
- Add persona-based signup flow (choose your role → see relevant features highlighted)
- Implement upgrade nudge when user tries a Pro feature on Starter plan

**Expected impact:** −12% churn in paid-channel segment.

---

### P3 — Predictive Churn Scoring (Strategic | Q2 implementation)

**Problem:** Churn is reactive — we only know after they cancel.  
**Solution:** Build a simple churn risk score using these signals:

| Signal | Weight |
|---|---|
| Login frequency drop (>50% vs Week 1) | 35% |
| 0 team invites sent by Day 7 | 25% |
| No project created by Day 3 | 20% |
| Support ticket opened (unanswered >24h) | 20% |

**Action:** Auto-trigger CSM outreach when score > 70. Offer 15-min onboarding call. Track conversion rate of at-risk → retained.

---

## 📈 Expected Outcome

| Timeframe | Intervention | Expected Churn Reduction |
|---|---|---|
| Month 1 | Onboarding simplification | −18% |
| Month 2 | Pricing page + signup flow | −12% |
| Month 4 | Predictive scoring + CSM | −10% |
| **Combined** | **All three** | **~−35% to −40% total** |

If 35% churn reduction achieved:  
→ Monthly churn drops from 10.3% to ~6.7%  
→ ARR recovered: ~€84,000  
→ Payback on implementation (est. €18,000): **< 3 months**

---

## 📁 Repository Structure

```
customer-churn-analysis/
│
├── README.md                        ← You are here
├── StakeholderBrief.md              ← One-pager for exec presentation
│
├── notebooks/
│   ├── 01_data_exploration.ipynb    ← Cohort analysis + descriptive stats
│   ├── 02_root_cause_analysis.ipynb ← 5 Why's + exit survey clustering
│   └── 03_churn_scoring_model.ipynb ← Logistic regression churn predictor
│
└── recommendations/
    ├── P1_onboarding_redesign.md
    ├── P2_pricing_page_brief.md
    └── P3_churn_scoring_spec.md
```

---

## 🔗 Data Sources Used

- Stripe subscription events (12 months)
- Internal CRM export (HubSpot)
- NPS exit survey (n=412 responses)
- Feature usage logs (Mixpanel export)
- Industry benchmarks: OpenView SaaS Benchmarks 2024, ChurnZero Churn Index

---

*Case study by Philippe Godfroy — Business Analyst Portfolio*
