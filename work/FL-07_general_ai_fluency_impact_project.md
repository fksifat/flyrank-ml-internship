# General AI Fluency Impact Project

## Project goal

Master practical AI workflow skills, publish a clear personal brand website, and ship a working personal agent with verifiable run evidence.

## 1) Master the AI stack (evidence)

The following artifacts show end-to-end AI workflow capability in this repo:

- Workflow and quality process: `work/FL-01_workflow_audit.md`
- Prompt iteration and improvements: `work/FL-03_prompt_iteration_log.md`
- Agent and MCP concepts: `work/FL-04_agent_concepts_mcp_explainer.md`
- MCP evidence notes: `work/FL-04_mcp_evidence.md`
- Build log and execution receipts: `work/FL-06_build_log.md`
- Capstone narrative and outcomes: `work/notebooks/capstone.ipynb`

## 2) Build a personal brand website (evidence)

The personal site is implemented as a static deployment in `docs/`:

- Main site page: `docs/personal-site.html`
- Styles: `docs/assets/site.css`
- Live interactive feature script: `docs/assets/refresh-demo.js`
- Public research paper page: `docs/index.html`
- Submission URL record: `submission/paper_url.txt`

### What is shipped on the website

- Clear personal positioning and proof statement
- Portfolio case-study cards
- Public profile links (LinkedIn, GitHub, CV, booking)
- One real interactive feature: refresh opportunity scoring demo
- Plain-language feature data-flow explanation for non-technical readers

## 3) Ship a personal agent (evidence)

The personal agent MVP is implemented in:

- Agent spec: `work/personal_agent_spec.md`
- Agent code: `work/agent/portfolio_update_agent.py`
- Agent usage docs: `work/agent/README.md`

### Fresh run artifacts generated

- `work/outputs/portfolio_agent_run_20260729_114441_537431_portfolio.md`
- `work/outputs/portfolio_agent_run_20260729_114445_614208_linkedin.md`

These runs demonstrate that the agent executes successfully, reads evidence from the repo, and outputs audience-specific update drafts.

## 4) Reproducibility

From repo root:

```bash
python3 work/agent/portfolio_update_agent.py --audience portfolio
python3 work/agent/portfolio_update_agent.py --audience linkedin
python3 work/agent/portfolio_update_agent.py --audience meeting
```

Optional API-backed mode (falls back safely to heuristic mode if unavailable):

```bash
export OPENAI_API_KEY="<your_key>"
export OPENAI_MODEL="gpt-5.1-mini"
python3 work/agent/portfolio_update_agent.py --audience portfolio --prefer-openai
```

## 5) Honest framing

- Outputs are observational and decision-support oriented.
- No private client names, domains, URLs, or raw query data are exposed.
- The portfolio agent drafts updates; it does not auto-publish.

## 6) Completion checklist

- [x] AI workflow evidence documented
- [x] Personal brand website shipped with interactive feature
- [x] Personal agent implemented and run successfully
- [x] Run artifacts saved in `work/outputs/`
- [x] Public-safe language and data handling preserved
