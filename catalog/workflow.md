# Workflow

> Generated from README.md on 2026-01-29
## Index
- [langgraph](#langgraph)
- [cc-wf-studio](#cc-wf-studio)

---

## langgraph

**TL;DR:** Graph-based framework для building agent workflows от LangChain team. State machines, cycles, persistence, human-in-the-loop. The orchestration layer for LangChain. LangGraph Studio для visual debugging. 24k stars.

### Быстрый выбор
- ✅ Используй если:
  - Complex agent workflows as graphs
  - Durable execution: Build agents that persist through failures and can run for extended periods, automatically resuming from exactly where they left off.
  - Human-in-the-loop: Seamlessly incorporate human oversight by inspecting and modifying agent state at any point during execution.
- ❌ Не используй если:
  - Simple LLM
  - Нужны входные данные/доступы: API keys

### 🚀 Запуск
```bash
pip install langgraph
```

### 🧩 Архитектура
- **Category:** Workflow
- **Stack:** Python, JavaScript
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Complex agent workflows as graphs
- Durable execution: Build agents that persist through failures and can run for extended periods, automatically resuming from exactly where they left off.
- Human-in-the-loop: Seamlessly incorporate human oversight by inspecting and modifying agent state at any point during execution.
- Comprehensive memory: Create truly stateful agents with both short-term working memory for ongoing reasoning and long-term persistent memory across sessions.

### ⚠️ Ограничения
- Simple LLM
- Нужны данные/доступы: API keys

### 🧭 Fit / Maturity / Ops
- **Fit:** Complex agent workflows as graphs
- **Maturity:** active
- **Latency/Cost:** balanced
- **Data constraints:** API keys
- **Ops friction:** low

### Full links
- Repo: https://github.com/langchain-ai/langgraph
- Original README: https://github.com/langchain-ai/langgraph/blob/main/README.md
- Docs: https://langchain-ai.github.io/langgraph/
- Studio: https://studio.langchain.com
- Discord: https://discord.gg/langchain
- Stars: 23,791
- Maturity: active

---



## cc-wf-studio

**TL;DR:** Creative Compute Workflow Studio. A graph-based visual editor for building AI workflows. Similar to ComfyUI but focused on general compute and agent orchestration. Enables visual programming for complex AI pipelines. 3k stars.

### Быстрый выбор
- ✅ Используй если:
  - CC Workflow Studio
  - Claude Code: .claude/agents/ and .claude/commands/
  - GitHub Copilot Chat<a href="#github-copilot-support">(※1)</a>: .github/prompts/
- ❌ Не используй если:
  - Simple tasks
  - Нужны входные данные/доступы: —

### 🚀 Запуск
```bash
# См. документацию: https://github.com/breaking-brake/cc-wf-studio/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** Workflow
- **Stack:** React
- **Entrypoints:** См. README

### 🧪 Примеры задач
- CC Workflow Studio
- Claude Code: .claude/agents/ and .claude/commands/
- GitHub Copilot Chat<a href="#github-copilot-support">(※1)</a>: .github/prompts/
- GitHub Copilot CLI<a href="#github-copilot-support">(※1)</a>: .github/skills/

### ⚠️ Ограничения
- Simple tasks
- Нужны данные/доступы: —

### 🧭 Fit / Maturity / Ops
- **Fit:** CC Workflow Studio
- **Maturity:** active
- **Latency/Cost:** balanced
- **Data constraints:** —
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/breaking-brake/cc-wf-studio
- Original README: https://github.com/breaking-brake/cc-wf-studio/blob/main/README.md
- Stars: ~3,193
- Maturity: active


---
