# FL-04 MCP Evidence

## Status

The repo now has a verified local MCP path for evidence collection: a tiny workspace-scoped JSON-RPC server that exposes file-reading and directory-listing tools, plus a direct client transcript that exercised those tools. The browser inspector was flaky in this environment, so the evidence below records the actual tool calls and outputs that were proven end to end.

The explainer is complete, and this file records the connector setup and the three verified tasks so the assignment stays grounded in tool use rather than ordinary chat.

## Recommended connector

Use the official filesystem MCP server with Claude Desktop or another MCP-compatible client.

Suggested server configuration:

```json
{
  "mcpServers": {
    "flyrank-filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/home/farhankabirsifat/Desktop/flyrank-ml-internship"
      ]
    }
  }
}
```

Restrict the server to the project directory. Do not expose the home directory or unrelated personal files.

## Verified local evidence

To keep the evidence reproducible in this workspace, I also used a tiny local MCP server that exposes three tools:

- `read_file`
- `list_dir`
- `compare_files`

The direct MCP client transcript proved all three calls worked:

1. `read_file` on `work/FL-02_automation_workflow_v2.md`

- Returned the weekly brief workflow and its section headings.

2. `list_dir` on `.`

- Returned the top-level repository structure.

3. `compare_files` on `work/FL-02_automation_workflow_v2_submission.md` and `work/FL-04_agent_concepts_mcp_explainer.md`

- Returned excerpts from both files so the workflow-versus-agent distinction could be checked against the actual write-up.

The direct transcript is the important proof here: it shows initialize, tool listing, and three separate tool calls returning live workspace data.

## Three tasks to run and screenshot

After the client shows the server as connected, run these as separate tasks. Each screenshot should include the visible tool call and the returned result.

### Task 1: Read a local project file

Prompt:

> Use the connected filesystem MCP server to read `work/FL-02_automation_workflow_v2.md`. Tell me the workflow's four stages and cite the section headings you found.

Evidence to capture:

- the filesystem tool name
- the requested path
- returned file content or an excerpt

Why chat alone cannot do it:

- The file is local context that was not pasted into the conversation.

### Task 2: Inspect the repository structure

Prompt:

> Use the connected filesystem MCP server to list the top-level files and directories in the FlyRank project. Group the result into documentation, data, notebooks, scripts, and work artifacts.

Evidence to capture:

- the directory-listing tool call
- returned repository entries

Why chat alone cannot do it:

- The client is obtaining a current directory listing from the local filesystem.

### Task 3: Read and compare two local artifacts

Prompt:

> Use the connected filesystem MCP server to read `work/FL-02_automation_workflow_v2_submission.md` and `work/FL-04_agent_concepts_mcp_explainer.md`. Identify one place where the automation workflow is fixed and one change that would make it agentic.

Evidence to capture:

- both file-read tool calls, or one tool call per file
- the returned passages used for the comparison

Why chat alone cannot do it:

- The client is retrieving two current local files and comparing their contents through tool results.

## Screenshot checklist

- [ ] Client name and connected MCP server are visible.
- [ ] Tool call is visible, not only the final prose answer.
- [ ] Returned result is visible for all three tasks.
- [ ] No private paths, secrets, raw client data, or unrelated home-directory files appear.
- [ ] Save screenshots beside this file or attach them to the track submission.
- [x] Fallback proof captured in direct MCP transcripts when the browser inspector timed out in this environment.

## Verified local preparation

- Node.js and `npx` are available in the environment.
- No Python `mcp` package is installed.
- The repository `.mcp.json` remains available for MCP client configuration.
- The explainer is saved as `work/FL-04_agent_concepts_mcp_explainer.md`.
