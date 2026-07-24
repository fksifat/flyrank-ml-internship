# Personal Agent Spec: Portfolio Update Concierge

## 1. The job

Build a personal AI agent that turns my weekly work in this repo into a short, polished update for my portfolio or LinkedIn. The agent should read the latest evidence from the workspace, summarize what shipped, call out what I learned, and draft a clear next-step note without inventing facts.

### Scope

This agent will handle one narrow task:

- Weekly or ad-hoc drafting of a 120–180 word update from repo artifacts.

It will not:

- Post to social platforms automatically.
- Make claims beyond the evidence in the repo.
- Pull in private or sensitive data.

## 2. User and usage context

- Primary user: me, as a learner building a public portfolio.
- Frequency: once per week, or whenever I finish a meaningful milestone.
- Best use case: after I complete a notebook, ship a page, or produce a new artifact, I want a crisp update I can review and publish.

## 3. Inputs, outputs, and tools

### Inputs

The agent will read only repo-safe files such as:

- work/notebooks/\*.ipynb
- work/\*.md
- outputs/_.json and _.md
- docs/ and submission/ artifacts that are already public-facing

### Outputs

The agent will produce:

- A short draft update in plain English
- A bullet summary with 3 parts: What shipped, What I learned, Next step
- Optional variants for portfolio, LinkedIn, or a meeting recap

### Tools and access plan

- Read-only access to workspace files
- Optional access to a simple local note file for user context, such as a short “today’s focus” note
- No database access initially
- No web browsing by default; if browsing is later needed, it should be opt-in and limited to public URLs only

## 4. Draft instructions

Use the following instruction set as the core prompt:

You are my personal portfolio-update agent. Your job is to turn verified project evidence into a short, polished update.

Rules:

1. Read the latest relevant files in the workspace before drafting.
2. Prefer facts that can be backed by files, metrics, or visible outputs.
3. Write in a calm, professional voice.
4. Use this structure:
   - First sentence: what shipped
   - Second sentence: what changed or improved
   - Third sentence: what I learned
   - Final sentence: what I will do next
5. Do not invent metrics, claims, or dates.
6. If evidence is missing, say so clearly and ask for a short clarification.

## 5. Pre-build evaluation cases

These are the five cases I would use before building the agent.

1. Clean success case
   - Input: a completed notebook plus a new output file
   - Expected output: a concise update that mentions the artifact and the measurable result

2. No new evidence case
   - Input: no significant file changes for the week
   - Expected output: a safe fallback message such as “No new evidence was found; share a milestone and I will draft an update.”

3. Mixed artifact case
   - Input: notebook work plus a new static page and an updated report
   - Expected output: a balanced summary that prioritizes the most important shipped item rather than listing everything equally

4. Missing evidence case
   - Input: a changed file with no clear context
   - Expected output: a cautious draft that says what is known and flags the missing detail instead of guessing

5. Tone-control case
   - Input: the same evidence twice, once for a portfolio update and once for a LinkedIn post
   - Expected output: the agent should adapt tone and length but keep the facts identical

## 6. Risks and guardrails

### Main risks

- Fabricating metrics or outcomes
- Overwriting the user’s voice with generic marketing language
- Writing updates that are too long or too promotional
- Using stale evidence from older files

### Guardrails

- Require evidence from files before drafting
- Keep the output short and factual
- Include a “confidence” or “evidence basis” note in the draft when the signal is weak
- Never publish automatically without human review
- Limit the agent to read-only access for the first version

## 7. Platform choice

I would build this as a lightweight local Python app using the OpenAI Responses API.

### Why this is the best fit

- It is simple to run on my own machine.
- It fits a single-purpose agent well without needing a large app framework.
- It is easy to iterate on prompts and evaluation cases.
- It can later be wrapped into a CLI, a VS Code command, or a small web interface without changing the core logic.

### Practical shape

- A Python script reads the relevant files
- It builds a short context summary
- It calls the model with the instruction prompt above
- It writes a draft to a markdown file or shows it in the terminal

## 8. Success definition

The agent is successful if it can reliably:

- summarize real project progress from repository evidence
- avoid hallucinations
- produce a draft that feels usable without heavy editing
- support both weekly updates and one-off milestone summaries
