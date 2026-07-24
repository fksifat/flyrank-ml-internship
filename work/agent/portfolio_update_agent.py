#!/usr/bin/env python3
"""Portfolio Update Concierge MVP.

Generates a short, evidence-based weekly update from repository artifacts.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import pathlib
import subprocess
import textwrap
import urllib.error
import urllib.request
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUTPUT_DIR = ROOT / "work" / "outputs"


def run_git(args: list[str]) -> str:
    """Run a git command and return stdout, or empty string on failure."""
    try:
        proc = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        return proc.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def recent_files(days: int, max_files: int) -> list[str]:
    out = run_git(["log", f"--since={days}.days", "--name-only", "--pretty=format:"])
    if not out:
        return []

    allowed_prefixes = ("work/", "docs/", "outputs/", "submission/")
    allowed_suffixes = (".md", ".html", ".json", ".ipynb", ".txt", ".csv")
    seen: list[str] = []
    for raw in out.splitlines():
        rel = raw.strip()
        if not rel:
            continue
        if not rel.startswith(allowed_prefixes):
            continue
        if not rel.endswith(allowed_suffixes):
            continue
        if rel not in seen:
            seen.append(rel)
        if len(seen) >= max_files:
            break
    return seen


def read_json(path: pathlib.Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def read_text_excerpt(path: pathlib.Path, max_chars: int = 700) -> str:
    if not path.exists() or path.suffix.lower() in {".ipynb", ".csv"}:
        return ""
    raw = path.read_text(encoding="utf-8", errors="ignore")
    cleaned = " ".join(raw.split())
    return cleaned[:max_chars]


def build_evidence(days: int, max_files: int) -> dict[str, Any]:
    files = recent_files(days=days, max_files=max_files)
    summary = read_json(ROOT / "outputs" / "summary.json")
    results = read_json(ROOT / "outputs" / "model_results.json")

    top_metrics: dict[str, Any] = {}
    if summary:
        keys = ["best_model", "rows_scored", "top_queue_score", "final_score_p80"]
        top_metrics.update({k: summary.get(k) for k in keys if k in summary})
    if results:
        rf = (results.get("models") or {}).get("random_forest") or {}
        base = results.get("baseline") or {}
        if rf:
            top_metrics["rf_precision_at_50"] = rf.get("precision_at_50")
        if base:
            top_metrics["baseline_precision_at_50"] = base.get("baseline_precision_at_50")
        if "split_strategy" in results:
            top_metrics["split_strategy"] = results.get("split_strategy")

    snippets: list[dict[str, str]] = []
    for rel in files:
        excerpt = read_text_excerpt(ROOT / rel)
        if excerpt:
            snippets.append({"file": rel, "excerpt": excerpt})

    return {
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "lookback_days": days,
        "files": files,
        "top_metrics": top_metrics,
        "snippets": snippets,
    }


def simple_draft(evidence: dict[str, Any], audience: str) -> str:
    metrics = evidence.get("top_metrics", {})
    files = evidence.get("files", [])
    main_file = files[0] if files else "the repository"

    best_model = metrics.get("best_model", "current model")
    rf_p50 = metrics.get("rf_precision_at_50")
    base_p50 = metrics.get("baseline_precision_at_50")
    split = metrics.get("split_strategy", "holdout")

    metric_line = ""
    if rf_p50 is not None and base_p50 is not None:
        metric_line = (
            f"on the {split} split, precision@50 is {rf_p50:.2f} versus "
            f"{base_p50:.2f} for the baseline"
        )

    if audience == "linkedin":
        final_sentence = (
            "Next I will tighten this into a shorter public post, attach direct "
            "evidence links, and ask for one external reaction so the next update "
            "is both clearer and more credible."
        )
    elif audience == "meeting":
        final_sentence = (
            "Next I will align with the team on the highest-impact follow-up, lock "
            "the review checklist, and confirm ownership for the next iteration "
            "before we publish another status update."
        )
    else:
        final_sentence = (
            "Next I will improve the public write-up with clearer section labeling, "
            "add one outside feedback note, and keep each claim traceable to a "
            "specific artifact before capstone review."
        )

    text = (
        f"This week I shipped portfolio updates grounded in {main_file} and nearby "
        "artifacts, including a clearer public project page and a written DNS "
        "walkthrough so the hosting and domain steps are reviewable by a "
        "non-technical teammate. "
        f"The strongest model is still {best_model}, and the latest evidence favors "
        f"ranking metrics over raw accuracy because {metric_line} and the queue "
        "outputs stay consistent with the prior validation pattern. "
        "I learned that pairing concise narrative with explicit evidence lists and "
        "guardrails reduces ambiguity, lowers hallucination risk, and makes the "
        "work faster for others to validate without back-and-forth. "
        f"{final_sentence}"
    )
    return " ".join(text.split())


def call_openai(prompt: str, model: str) -> str:
    key = os.getenv("OPENAI_API_KEY", "").strip()
    if not key:
        raise RuntimeError("OPENAI_API_KEY is not set")

    payload = {
        "model": model,
        "input": [
            {
                "role": "system",
                "content": [
                    {
                        "type": "input_text",
                        "text": (
                            "You are a personal portfolio-update agent. Use only the "
                            "provided evidence. Do not invent facts or metrics. Return "
                            "JSON with keys: draft, shipped, learned, next_step."
                        ),
                    }
                ],
            },
            {
                "role": "user",
                "content": [{"type": "input_text", "text": prompt}],
            },
        ],
        "text": {"format": {"type": "json_object"}},
    }

    req = urllib.request.Request(
        url="https://api.openai.com/v1/responses",
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.URLError as exc:
        raise RuntimeError(f"OpenAI API call failed: {exc}") from exc

    text_out = body.get("output_text", "").strip()
    if not text_out:
        raise RuntimeError("OpenAI API returned empty output_text")

    try:
        parsed = json.loads(text_out)
    except json.JSONDecodeError as exc:
        raise RuntimeError("OpenAI response was not valid JSON") from exc

    required = ["draft", "shipped", "learned", "next_step"]
    missing = [k for k in required if k not in parsed]
    if missing:
        raise RuntimeError(f"OpenAI JSON missing keys: {', '.join(missing)}")

    bullets = textwrap.dedent(
        f"""
        - What shipped: {parsed['shipped']}
        - What I learned: {parsed['learned']}
        - Next step: {parsed['next_step']}
        """
    ).strip()

    return f"{parsed['draft']}\n\n{bullets}"


def compose_prompt(evidence: dict[str, Any], audience: str) -> str:
    return textwrap.dedent(
        f"""
        Audience: {audience}
        Task: Write a 120-180 word weekly update in 4 sentences.
        Evidence JSON:
        {json.dumps(evidence, indent=2)}

        Output requirements:
        1) Sentence 1: what shipped.
        2) Sentence 2: what changed or improved.
        3) Sentence 3: what I learned.
        4) Sentence 4: what I will do next.
        5) Then provide three bullets: What shipped, What I learned, Next step.
        """
    ).strip()


def format_output(
    evidence: dict[str, Any],
    draft: str,
    audience: str,
    mode: str,
    run_id: str,
) -> str:
    files = evidence.get("files", [])
    basis = "\n".join(f"- {f}" for f in files) if files else "- No recent files found"
    metrics = json.dumps(evidence.get("top_metrics", {}), indent=2)

    return textwrap.dedent(
        f"""
# Portfolio Update Concierge Run

- Run ID: {run_id}
- Generated at: {evidence.get('generated_at')}
- Audience: {audience}
- Generation mode: {mode}

## Draft Update

{draft}

## Evidence Basis

{basis}

## Metric Snapshot

```json
{metrics}
```
"""
    ).strip() + "\n"


def save_run(content: str, run_id: str) -> pathlib.Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / f"portfolio_agent_run_{run_id}.md"
    out_path.write_text(content, encoding="utf-8")
    return out_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Portfolio Update Concierge MVP")
    parser.add_argument("--audience", choices=["portfolio", "linkedin", "meeting"], default="portfolio")
    parser.add_argument("--days", type=int, default=14)
    parser.add_argument("--max-files", type=int, default=12)
    parser.add_argument("--prefer-openai", action="store_true")
    parser.add_argument("--model", default=os.getenv("OPENAI_MODEL", "gpt-5.1-mini"))
    args = parser.parse_args()

    evidence = build_evidence(days=args.days, max_files=args.max_files)
    prompt = compose_prompt(evidence=evidence, audience=args.audience)

    mode = "heuristic"
    if args.prefer_openai:
        try:
            draft = call_openai(prompt=prompt, model=args.model)
            mode = "openai_responses_api"
        except RuntimeError as exc:
            draft = simple_draft(evidence=evidence, audience=args.audience)
            draft += f"\n\n- Note: API mode unavailable, fallback used ({exc})."
    else:
        draft = simple_draft(evidence=evidence, audience=args.audience)

    if args.audience == "linkedin":
        next_step_bullet = "Convert this into a publishable LinkedIn post with direct evidence links."
    elif args.audience == "meeting":
        next_step_bullet = "Align owners and checklist items for the next iteration review."
    else:
        next_step_bullet = "Polish the portfolio narrative and add one verified external feedback note."

    if "- What shipped:" not in draft:
        draft += "\n\n"
        draft += "- What shipped: Updated project artifacts with verifiable outputs.\n"
        draft += "- What I learned: Clear evidence mapping improves trust.\n"
        draft += f"- Next step: {next_step_bullet}"

    run_id = dt.datetime.now().strftime("%Y%m%d_%H%M%S_%f") + f"_{args.audience}"
    content = format_output(evidence=evidence, draft=draft, audience=args.audience, mode=mode, run_id=run_id)
    out_path = save_run(content=content, run_id=run_id)

    print(f"Agent run complete: {out_path.relative_to(ROOT)}")
    print(f"Mode: {mode}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
