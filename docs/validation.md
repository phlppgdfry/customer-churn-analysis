# Validation evidence

Validation date: 15 November 2026. Fixtures represent June 2026 and are intentionally frozen. No historical business outcomes are inferred from this validation.

## Recorded local result

Python 3.15.2: **19 tests passed**. Chromium: **8 tests passed**. JavaScript syntax checks and Python compilation passed. The report command reproduced the committed synthetic baseline.

## Automated checks

- `make check`: Python unit/integration tests, HTTP round trips, invalid input, read/export round trip, durable state, stale-write rejection, simultaneous updates and audit-failure rollback; Python compilation; JavaScript syntax checks.
- `npm run test:e2e`: eight Chromium tests covering served brand assets, filters/empty state, responsive layouts at 390/768/1440 px, the domain workflow with reload persistence, and the public showcase.
- `make report`: baseline JSON and CSV generated from the same domain calculations used by the browser.

Domain coverage: Mature/immature cohorts, exact 90-day boundary, late cancellations, strict risk thresholds, duplicate outreach and unchanged risk after outreach.

## Browser review

The Browser plugin is not available in this environment, so the final review uses the repository Playwright suite and the shared Playwright browser. The core flow was exercised through real forms and buttons against the local Python server. Reload persistence, visible success and rejection messages, record selection and mobile document width were checked. Screenshots are actual rendered pages, not design mockups.

1. Review the cohort panel: nine mature accounts and two cancellations within 90 days produce 22.2% 90-day churn. June is N/A.
2. Select Canal Digital and inspect the four risk contributions. Create an outreach task with a fictional conversation brief.
3. Reload and verify the task persists. Risk and churn metrics remain unchanged: planned contact is not a measured retention outcome.

See [desktop screenshot](preview.png), [mobile screenshot](mobile.png), and the current [GitHub Actions run](https://github.com/phlppgdfry/customer-churn-analysis/actions/workflows/demo.yml). The badge reports the remote result; this document describes the checks, not an invented production certification.

## Final release checks

The final pass adds regression coverage for negative numeric CSV values, formula-leading text and a failed snapshot refresh after a version conflict. The conflict error remains visible, form inputs survive and controls are re-enabled without a script error. The versioned release is linked from the public setup section.

## Limits of the evidence

The suite tests a local single-workspace product with synthetic records. It does not establish external integration reliability, real user outcomes, scale, production security, legal compliance or clinical validity. All 12 accounts, feature signals and monetary amounts are synthetic. No Stripe, HubSpot, Mixpanel or survey data was accessed. The original −40% churn reduction, €240k impact and customer research are unverified concept assumptions, not outcomes.
