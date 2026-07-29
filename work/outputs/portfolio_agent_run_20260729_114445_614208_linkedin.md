# Portfolio Update Concierge Run

- Run ID: 20260729_114445_614208_linkedin
- Generated at: 2026-07-29T11:44:45
- Audience: linkedin
- Generation mode: heuristic

## Draft Update

This week I shipped portfolio updates grounded in docs/index.html and nearby artifacts, including a clearer public project page and a written DNS walkthrough so the hosting and domain steps are reviewable by a non-technical teammate. The strongest model is still random_forest, and the latest evidence favors ranking metrics over raw accuracy because on the client_holdout split, precision@50 is 0.68 versus 0.24 for the baseline and the queue outputs stay consistent with the prior validation pattern. I learned that pairing concise narrative with explicit evidence lists and guardrails reduces ambiguity, lowers hallucination risk, and makes the work faster for others to validate without back-and-forth. Next I will tighten this into a shorter public post, attach direct evidence links, and ask for one external reaction so the next update is both clearer and more credible.

- What shipped: Updated project artifacts with verifiable outputs.
- What I learned: Clear evidence mapping improves trust.
- Next step: Convert this into a publishable LinkedIn post with direct evidence links.

## Evidence Basis

- docs/index.html
- docs/personal-site.html
- docs/thanks.html
- work/notebooks/capstone.ipynb
- submission/paper_url.txt
- docs/week-07.html
- work/notebooks/w07_action_playbook.ipynb
- work/outputs/action_playbook_summary.json
- work/outputs/action_playbook_summary.md
- docs/week-05.html
- work/notebooks/w06_validation_audit.ipynb
- work/FL-06_build_log.md

## Metric Snapshot

```json
{
  "best_model": "random_forest",
  "rows_scored": 30000,
  "top_queue_score": 81.92846726727653,
  "final_score_p80": 63.68027543994317,
  "rf_precision_at_50": 0.68,
  "baseline_precision_at_50": 0.24,
  "split_strategy": "client_holdout"
}
```
