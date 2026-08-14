# FL-06 Build Log: Portfolio Update Concierge MVP

## Goal

Ship Checkpoint 1: a working MVP that completes the core FL-06 job end-to-end with at least one live tool/data connection.

## Starting spec reference

- Source: `work/personal_agent_spec.md`
- Core job kept: generate a 120-180 word update + bullets from real repo evidence.

## Iteration log

### Iteration 1 - Define narrowest runnable scope
- Planned: full OpenAI-only implementation via Responses API.
- Risk found: this environment may not always have API credentials available at run time.
- Change made: implemented a dual-path runner:
  - API mode when `OPENAI_API_KEY` is present
  - local fallback mode when not present
- Why: ensure end-to-end completion every run, with no mid-run hand-editing.

### Iteration 2 - Add live connection and evidence grounding
- Planned: scan static file list only.
- Limitation: static list can miss the newest work and feel stale.
- Change made: connected to live git history using `git log --name-only --since=<days>`.
- Why: dynamically detect recent artifacts and ground output in current evidence.

### Iteration 3 - Stabilize output format for evaluation
- Planned: freeform paragraph only.
- Limitation: assignment requires clear verification and consistent structure.
- Change made: enforced output sections:
  - Draft update
  - What shipped / What I learned / Next step bullets
  - Evidence basis file list
  - Metric snapshot JSON
- Why: easier evaluator review and lower hallucination risk.

### Iteration 4 - Capture-ready run artifacts
- Planned: print-only terminal output.
- Limitation: weak audit trail and hard to review after the run.
- Change made: every run writes a timestamped markdown artifact in `work/outputs/`.
- Why: reproducible evidence for submission and easier screen-capture walkthrough.

### Iteration 5 - Fix rapid-run overwrite and text quality
- Break observed: back-to-back runs generated the same filename timestamp and overwrote output.
- Change made: run IDs now include microseconds and audience suffix.
- Break observed: a wording artifact appeared in sentence 2 ("because On ...").
- Change made: normalized sentence casing and tuned audience-specific next-step bullets.
- Why: clean, non-overwritten evidence files and reviewer-friendly output quality.

## What was cut from the FL-06 spec (for MVP)

1. Optional meeting recap variants beyond 3 fixed audiences
- Cut reason: not needed for Checkpoint 1 core proof.

2. Web browsing integration
- Cut reason: unnecessary for core job and increases risk surface.

3. Database or external knowledge-base connectors
- Cut reason: not required for this assignment and not needed to prove end-to-end loop.

## What broke and how it was handled

- Potential break: missing or invalid OpenAI credentials.
- Handling: automatic fallback to local heuristic mode while preserving output structure.
- Result: run still completes without manual intervention.

## Final MVP files

- `work/agent/portfolio_update_agent.py`
- `work/agent/README.md`
- `work/outputs/portfolio_agent_run_<timestamp>.md` (generated per run)

## Current status

- Core job: implemented
- Live tool/data connection: implemented (git + repository files)
- End-to-end run: validated in this environment
- Raw unedited capture: manual recording still required by user at submission time
