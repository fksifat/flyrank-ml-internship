# FL-04 Agent Concepts and MCP Basics

## Workflow versus agent

An LLM workflow is a designed path. The builder decides the sequence, the prompts, the handoffs, and usually the stopping point before the run begins. The model may produce the content inside each step, but the surrounding system determines what happens next. This makes workflows predictable, testable, and easier to estimate for cost and latency.

An agent is a more open-ended system. It receives a goal, observes results from its environment, chooses which tool or action to use next, and keeps iterating until it reaches a stopping condition or needs human input. The important difference is not that an agent uses an LLM or that it has multiple prompts. The difference is who controls the process: a workflow follows a predefined path, while an agent dynamically directs its own path based on tool results.

My FL-04 reference pipeline is the weekly industry brief documented in the earlier automation workflow deliverable. Its path is fixed: NotebookLM gathers source-grounded notes, a Claude Project synthesizes signals, a drafting prompt writes the brief, and a human reviews it. That is a workflow, specifically a prompt-chain workflow with a human checkpoint. It is not an agent because it does not decide whether to search again, switch sources, ask for missing evidence, or revise its own plan. The fixed path is a strength here: a weekly brief has stable stages and benefits from consistency.

## What MCP is

The Model Context Protocol is an open standard for connecting an AI application to external systems. It is a shared interface between a client such as Claude and a server that exposes capabilities. The USB-C comparison is useful because the protocol standardizes the connection without requiring every AI application to invent a separate integration for every data source.

MCP has three important primitives. **Tools** are actions the model can call, such as reading a file, querying a database, searching a service, or creating a record. A tool has a name, description, input schema, and result. **Resources** are context that the client can retrieve, such as a document, database record, or file. A resource is about exposing information in a structured way rather than asking the model to perform an action. **Prompts** are reusable interaction templates supplied by the server. They can guide a task with the right context and instructions, such as a review prompt for a particular repository or dataset.

The distinction matters operationally. A normal chat response can only use what the user pasted or what the model already knows. An MCP connection lets the AI application request current information or take an authorized action through a defined interface. The model still needs permissions, clear tool descriptions, and human oversight. MCP does not make a model truthful or autonomous by itself; it makes external context and actions available in a common format.

## What the weekly brief would need to become an agent

The current workflow could become an agent by replacing its fixed source list and fixed sequence with a controlled research loop. The user would provide a topic and a time window. The agent would inspect available sources, choose which search or retrieval tool to use, compare the evidence, and decide whether the evidence is strong enough to draft. If sources conflict, it could retrieve another source or stop and ask the user a question. After drafting, it could call an evaluator tool, identify unsupported claims, revise the draft, and stop only when the evidence and format checks pass.

One concrete upgrade is an **evidence-gap loop**. Give the agent MCP tools for source search, source retrieval, citation checking, and saving a draft. Require every signal to carry a source reference. The agent can then: search for the topic, retrieve candidate sources, identify unsupported or conflicting claims, search again only when needed, draft the brief, run a citation check, and request human approval before publishing. A maximum number of search rounds and a mandatory approval checkpoint would control cost and prevent silent overreach.

That upgrade adds flexibility, but it also adds risk. Agents can take longer, call unnecessary tools, compound an early mistake, or make a weak source look authoritative. I would keep the existing fixed workflow for routine weekly briefs and use the agent version only when the topic is unfamiliar, source coverage is uncertain, or the brief needs iterative investigation. The simplest system that reliably answers the task should win.

## Sources

- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
- [What is the Model Context Protocol?](https://modelcontextprotocol.io/docs/getting-started/intro)
- [FL-02 automation workflow](FL-02_automation_workflow_v2.md)
