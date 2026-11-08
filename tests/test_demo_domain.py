import unittest
from demo import domain


class CohortTests(unittest.TestCase):
    def test_immature_customers_are_excluded_from_denominator(self):
        cohorts = domain.cohorts(domain.seed())
        june = next(c for c in cohorts if c["month"] == "2026-06")
        self.assertEqual(june["eligible"], 0)
        self.assertIsNone(june["rate"])
        self.assertEqual(sum(c["eligible"] for c in cohorts), 9)
        self.assertEqual(sum(c["churned"] for c in cohorts), 2)

    def test_exact_90_day_boundary_and_late_cancellation(self):
        base = domain.seed()[0]
        r = base | dict(signup="2026-04-01", cancelled="2026-06-30")
        c = domain.cohorts([r])[0]
        self.assertEqual(c["rate"], 100)
        r = base | dict(signup="2026-01-01", cancelled="2026-06-30")
        self.assertEqual(domain.cohorts([r])[0]["rate"], 0)

    def test_risk_boundary_is_strict(self):
        r = domain.seed()[0] | dict(
            login_drop=0.5, invites=1, project=True, support_hours=24
        )
        self.assertEqual(domain.risk(r), 0)
        r.update(login_drop=0.51, invites=0, project=False, support_hours=25)
        self.assertEqual(domain.risk(r), 100)

    def test_outreach_is_not_counted_as_retention(self):
        r = domain.seed()[4]
        score = domain.risk(r)
        updated = domain.execute(
            [r], dict(id=r["id"], action="outreach", note="Offer onboarding help")
        )
        self.assertEqual(domain.risk(updated), score)
        self.assertTrue(updated["outreach"])
        with self.assertRaises(ValueError):
            domain.execute(
                [updated], dict(id=r["id"], action="outreach", note="Duplicate")
            )
        cancelled = domain.seed()[0]
        with self.assertRaises(ValueError):
            domain.execute(
                [cancelled], dict(id=cancelled["id"], action="outreach", note="No")
            )
