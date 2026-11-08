export function inspect(r) {
  return {
    fields: [
      ["Plan", `${r.tier} · €${r.mrr}/month`],
      ["Signup date", r.signup],
      ["Cancelled", r.cancelled || "Active subscription"],
      ...Object.entries(r.signals).map(([k, v]) => [k, `${v} risk points`]),
      ...(r.outreach ? [["Planned outreach", r.outreach_note]] : []),
    ],
    forms:
      !r.cancelled && !r.outreach
        ? [
            {
              title: "Plan a conversation",
              help: "Create a local task with context for the account owner. No message is sent.",
              action: "outreach",
              button: "Create outreach task",
              fields: [
                {
                  key: "note",
                  label: "What should the account owner discuss?",
                  type: "textarea",
                  maxLength: 500,
                },
              ],
            },
          ]
        : [],
    note: "A risk score is not a calibrated probability. Planning outreach does not lower the score or count as a saved customer.",
  };
}
