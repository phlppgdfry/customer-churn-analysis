# Retain / Churn Analysis — delivery case study

## Problem and intended user

A retention team needs reproducible churn denominators and explainable account signals before deciding which customers to contact.

## Delivered vertical slice

A reproducible synthetic SaaS retention analysis with mature-cohort reporting, a transparent risk rule and persistent outreach planning.

1. Review the cohort panel: nine mature accounts and two cancellations within 90 days produce 22.2% 90-day churn. June is N/A.
2. Select Canal Digital and inspect the four risk contributions. Create an outreach task with a fictional conversation brief.
3. Reload and verify the task persists. Risk and churn metrics remain unchanged: planned contact is not a measured retention outcome.

## Acceptance criteria mapped to evidence

| Criterion | Verification |
| --- | --- |
| A reviewer can run the product without external credentials | `python3 -m demo.server`; standard-library runtime |
| Domain constraints are enforced on the server | `tests/test_demo_domain.py`; invalid transitions and boundary cases |
| Successful actions survive a new connection | `PersistenceTests.test_mutation_persists_and_is_audited` |
| A stale edit cannot overwrite newer state | Version conflict and simultaneous update tests |
| An audit write failure leaves the record unchanged | Fault-injected SQLite audit failure test |
| The main task works through the rendered interface | Domain workflow in `tests/browser/workspace.spec.cjs` |
| The interface works at mobile and desktop widths | 390, 768 and 1440 px browser tests; screenshots in `docs/` |
| Reported numbers can be reproduced | `python3 -m demo.report`; committed baseline JSON and CSV |

Domain-specific evidence: Mature/immature cohorts, exact 90-day boundary, late cancellations, strict risk thresholds, duplicate outreach and unchanged risk after outreach.

## What this demonstrates

Requirements are reduced to a coherent executable workflow, rather than a catalogue of disconnected features. Input contracts, state ownership, failure states, persistence and explanations are part of the product. Design choices and operational limits are recorded so another engineer can inspect the implementation and reproduce its behaviour.

## What it does not prove

All 12 accounts, feature signals and monetary amounts are synthetic. No Stripe, HubSpot, Mixpanel or survey data was accessed. The original −40% churn reduction, €240k impact and customer research are unverified concept assumptions, not outcomes.

No user study, commercial result, uptime, production scale, legal compliance or measured improvement is claimed. The historical concept is context, not evidence.
