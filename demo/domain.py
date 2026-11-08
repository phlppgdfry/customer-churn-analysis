from demo.contracts import text, record, metric


from datetime import date

AS_OF = date(2026, 6, 30)


CONFIG = {
    "columns": [
        ["name", "Account"],
        ["status", "Lifecycle"],
        ["value", "Risk / 100"],
        ["context", "Monthly revenue"],
    ],
    "title": "Retain / Churn Analysis",
    "heading": "Understand the risk. Act with context.",
    "subtitle": "Explore mature cohorts, inspect an explainable risk rule, and turn warning signals into a concrete outreach task.",
    "section": "Retention intelligence",
    "list_title": "Account watchlist",
    "theme": "churn",
    "port": 8114,
    "clock": "Analysis cutoff · 30 June 2026 UTC",
}


ACTIONS = frozenset(["outreach"])


def seed():
    names = [
        "Atelier North",
        "Dockside Labs",
        "Studio Flux",
        "Meridian Works",
        "Canal Digital",
        "Maple Systems",
        "Orbit Partners",
        "Lighthouse Co",
        "Forma Team",
        "Common Ground",
        "Scale Studio",
        "Evergreen Ops",
    ]
    return [
        dict(
            id=f"ACC-{i + 1:03}",
            name=n,
            tier=["Starter", "Pro", "Business"][i % 3],
            mrr=[29, 79, 199][i % 3],
            signup=["2026-01-05", "2026-02-10", "2026-03-15", "2026-06-01"][i % 4],
            cancelled="2026-03-01" if i == 0 else "2026-04-01" if i == 1 else None,
            login_drop=[0.65, 0.2, 0.8, 0.1][i % 4],
            invites=i % 3,
            project=i % 4 != 0,
            support_hours=[30, 2, 0, 48][i % 4],
            outreach=False,
        )
        for i, n in enumerate(names)
    ]


def signals(r):
    return {
        "Login decline > 50%": 35 if r["login_drop"] > 0.5 else 0,
        "No team invitations": 25 if r["invites"] == 0 else 0,
        "No project created": 20 if not r["project"] else 0,
        "Support unanswered > 24h": 20 if r["support_hours"] > 24 else 0,
    }


def risk(r):
    return sum(signals(r).values())


def status(r):
    if r["cancelled"]:
        return "Churned"
    if r["outreach"]:
        return "Outreach planned"
    if risk(r) > 70:
        return "High risk"
    return "Monitor"


def cohorts(records):
    result = []
    for month in sorted({r["signup"][:7] for r in records}):
        members = [r for r in records if r["signup"][:7] == month]
        eligible = [
            r for r in members if (AS_OF - date.fromisoformat(r["signup"])).days >= 90
        ]
        churned = [
            r
            for r in eligible
            if r["cancelled"]
            and (
                date.fromisoformat(r["cancelled"]) - date.fromisoformat(r["signup"])
            ).days
            <= 90
        ]
        result.append(
            {
                "month": month,
                "size": len(members),
                "eligible": len(eligible),
                "churned": len(churned),
                "rate": round(len(churned) / len(eligible) * 100, 1)
                if eligible
                else None,
            }
        )
    return result


def present(records):
    return [
        r
        | {
            "status": status(r),
            "value": risk(r),
            "context": f"€{r['mrr']}",
            "signals": signals(r),
        }
        for r in sorted(records, key=risk, reverse=True)
    ]


def metrics(records):
    active = [r for r in records if not r["cancelled"]]
    high = [r for r in active if risk(r) > 70]
    groups = cohorts(records)
    eligible = sum(c["eligible"] for c in groups)
    churned = sum(c["churned"] for c in groups)
    return [
        metric("Active accounts", len(active), "Cancelled accounts excluded"),
        metric(
            "High-risk MRR",
            f"€{sum(r['mrr'] for r in high):,}",
            "Active accounts with score > 70; not ARR",
        ),
        metric(
            "90-day churn",
            f"{churned / eligible * 100:.1f}%" if eligible else "N/A",
            f"{churned} churned / {eligible} mature accounts",
        ),
        metric(
            "Outreach tasks",
            sum(r["outreach"] for r in active),
            "Planned contact, not a retention outcome",
        ),
    ]


def analysis(records):
    return {
        "title": "Risk is a prompt for a conversation.",
        "headline": "Explain the score before acting on it.",
        "description": "A deterministic four-signal rule, not a trained prediction model. Cohorts exclude accounts with less than 90 days of follow-up. All customers and revenue are synthetic.",
        "bars_title": "90-day churn by signup cohort",
        "bars": [
            {
                "label": c["month"],
                "value": c["rate"] or 0,
                "display": f"{c['rate']:g}%" if c["rate"] is not None else "N/A",
            }
            for c in cohorts(records)
        ],
        "cohorts": cohorts(records),
    }


def execute(records, p):
    r = record(records, p)
    if p["action"] != "outreach":
        raise ValueError("Unknown action")
    if r["cancelled"]:
        raise ValueError("Cancelled accounts cannot enter active outreach")
    if r["outreach"]:
        raise ValueError("Outreach already planned")
    r["outreach_note"] = text(p, "note", 500)
    r["outreach"] = True
    return r
