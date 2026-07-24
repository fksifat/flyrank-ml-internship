# Portfolio Update Concierge (FL-07 MVP)

This is the Checkpoint 1 build of the FL-06 personal agent spec.

## Core job

Generate a short, evidence-based weekly update from real repository artifacts.

## Live tool/data connection

The agent uses:

- live Git history (`git log --name-only --since=...`) to discover recent work
- real project files (`outputs/*.json`, `work/*.md`, `docs/*.html`) for evidence

## Run

From repo root:

```bash
python3 work/agent/portfolio_update_agent.py --audience portfolio
```

Other audiences:

```bash
python3 work/agent/portfolio_update_agent.py --audience linkedin
python3 work/agent/portfolio_update_agent.py --audience meeting
```

Optional OpenAI Responses API mode:

```bash
export OPENAI_API_KEY="<your_key>"
export OPENAI_MODEL="gpt-5.1-mini"
python3 work/agent/portfolio_update_agent.py --audience portfolio --prefer-openai
```

If API mode fails, the script falls back to local heuristic mode and still completes end-to-end.

## Output

Each run writes a timestamped markdown artifact to:

- `work/outputs/portfolio_agent_run_YYYYMMDD_HHMMSS.md`

This file is the run evidence for submission.

## Raw capture (assignment requirement)

Record one unedited ~2 minute run while you:

1. run the command,
2. open the generated file,
3. read the draft and evidence list,
4. show one rerun with a different audience.

Suggested terminal capture command on Linux (if ffmpeg is installed):

```bash
ffmpeg -video_size 1920x1080 -framerate 30 -f x11grab -i :0.0 -codec:v libx264 -preset veryfast -crf 23 work/outputs/fl07_agent_raw_run.mp4
```

Stop recording with `q` in the terminal running ffmpeg.
