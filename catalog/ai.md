# AI

> Generated from README.md on 2026-01-29
## Index
- [openagent](#openagent)
- [sentience](#sentience)
- [OpenTruthV1](#opentruthv1)
- [A2A (Agent-to-Agent Protocol)](#a2a-agent-to-agent-protocol)
- [agent-zero (amibars)](#agent-zero-amibars)
- [zerepy (amibars)](#zerepy-amibars)
- [goose (Block)](#goose-block)
- [UI-TARS-desktop (ByteDance)](#ui-tars-desktop-bytedance)
- [oasis (camel-ai)](#oasis-camel-ai)
- [eliza (elizaOS)](#eliza-elizaos)
- [AutoAgent (HKUDS)](#autoagent-hkuds)
- [agents-course (HuggingFace)](#agents-course-huggingface)
- [autogen (Microsoft)](#autogen-microsoft)
- [agent-zero](#agent-zero)
- [browser-use (amibars)](#browser-use-amibars)
- [cdp-agentkit-nodejs (amibars)](#cdp-agentkit-nodejs-amibars)
- [openagent (amibars)](#openagent-amibars)
- [web-ui (amibars)](#web-ui-amibars)
- [zerepy](#zerepy)
- [axium](#axium)

---

## openagent

**TL;DR:** OpenAgent is an innovative multi-agent AI platform leveraging blockchain technology. Our platform enables smart and strategic AI interactions within a decentralized ecosystem.

### Быстрый выбор
- ✅ Используй если:
  - Multi-agent battles on Solana
  - Intelligent AI Agents: Customizable agents powered by OpenAI GPT-4
  - Real-Time Communication: Instant messaging via WebSocket
- ❌ Не используй если:
  - Non-Solana
  - Нужны входные данные/доступы: wallet

### 🚀 Запуск
```bash
npm install
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** TypeScript, Node.js, PostgreSQL, React, Solana
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Multi-agent battles on Solana
- Intelligent AI Agents: Customizable agents powered by OpenAI GPT-4
- Real-Time Communication: Instant messaging via WebSocket
- Blockchain Integration: Secure transactions on the Solana network

### ⚠️ Ограничения
- Non-Solana
- Нужны данные/доступы: wallet

### 🧭 Fit / Maturity / Ops
- **Fit:** Multi-agent battles on Solana
- **Maturity:** experimental
- **Latency/Cost:** balanced
- **Data constraints:** wallet
- **Ops friction:** low

### Full links
- Repo: https://github.com/openagentoa/openagent
- Original README: https://github.com/openagentoa/openagent/blob/main/README.md

---



## sentience

**TL;DR:** Framework для создания cryptographically verifiable AI agents. "Unruggable" agents — их действия записываются on-chain, невозможен rug-pull от разработчиков. Proof of Sentience SDK делает LLM inferences верифицируемыми. Решает trust problem для AI agents с $10B+ market cap. От команды Galadriel AI.

### Быстрый выбор
- ✅ Используй если:
  - Unruggable verified AI agents
- ❌ Не используй если:
  - Quick prototypes
  - Нужны входные данные/доступы: TEE setup

### 🚀 Запуск
```bash
pip install galadriel
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Unruggable verified AI agents

### ⚠️ Ограничения
- Quick prototypes
- Нужны данные/доступы: TEE setup

### 🧭 Fit / Maturity / Ops
- **Fit:** Unruggable verified AI agents
- **Maturity:** active
- **Latency/Cost:** balanced
- **Data constraints:** TEE setup
- **Ops friction:** low

### Full links
- Repo: https://github.com/galadriel-ai/Sentience
- Stars: 62
- Maturity: active

---



## OpenTruthV1

**TL;DR:** Open‑source версия “terminal of truths”. Экспериментальная платформа для AI‑агента, который взаимодействует с соцсетями и крипторынками (meme‑экономика, DeFi, promotion). Требует OpenAI key, X/Twitter API и кошелёк.

### Быстрый выбор
- ✅ Используй если:
  - Terminal of Truths clone
  - Decentralized Financial Interaction: OpenTruth is equipped with capabilities to autonomously manage, promote, and interact with decentralized financial assets, allowing it to participate in cryptocurrency experiments.
  - Meme Token Analysis: As seen with the Terminal of Truths’ experience in promoting tokens like GOAT, OpenTruth provides a platform to explore the viral influence of meme culture on token success.
- ❌ Не используй если:
  - Production bots
  - Нужны входные данные/доступы: LLM key

### 🚀 Запуск
```bash
# См. документацию: https://github.com/amibars/OpenTruthV1/blob/main/readme.md
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** Python
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Terminal of Truths clone
- Decentralized Financial Interaction: OpenTruth is equipped with capabilities to autonomously manage, promote, and interact with decentralized financial assets, allowing it to participate in cryptocurrency experiments.
- Meme Token Analysis: As seen with the Terminal of Truths’ experience in promoting tokens like GOAT, OpenTruth provides a platform to explore the viral influence of meme culture on token success.
- Risk Analysis of AI-Driven Promotion: By analyzing OpenTruth’s impact on cryptocurrency projects, users can gain insights into how unsupervised AI-driven promotion can affect token valuation and market trends.

### ⚠️ Ограничения
- Production bots
- Нужны данные/доступы: LLM key

### 🧭 Fit / Maturity / Ops
- **Fit:** Terminal of Truths clone
- **Maturity:** experimental
- **Latency/Cost:** balanced
- **Data constraints:** LLM key
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/amibars/OpenTruthV1
- Original README: https://github.com/amibars/OpenTruthV1/blob/main/readme.md

---



## A2A (Agent-to-Agent Protocol)

**TL;DR:** Open protocol для inter-agent communication от Google. Стандартизирует как agents обнаруживают друг друга, обмениваются capabilities, и делегируют tasks. Companion to MCP (tools) — A2A для agent↔agent, MCP для agent↔tools. 22k stars.

### Быстрый выбор
- ✅ Используй если:
  - An open protocol enabling communication and interoperability between opaque agentic applications.
  - Standardized Communication: JSON-RPC 2.0 over HTTP(S).
  - Agent Discovery: Via "Agent Cards" detailing capabilities and connection info.
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/a2aproject/A2A/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** Python, Go, Java
- **Entrypoints:** См. README

### 🧪 Примеры задач
- An open protocol enabling communication and interoperability between opaque agentic applications.
- Standardized Communication: JSON-RPC 2.0 over HTTP(S).
- Agent Discovery: Via "Agent Cards" detailing capabilities and connection info.
- Flexible Interaction: Supports synchronous request/response, streaming (SSE), and asynchronous push notifications.

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** An open protocol enabling communication and interoperability between opaque agentic applications.
- **Maturity:** active
- **Latency/Cost:** balanced
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/a2aproject/A2A
- Original README: https://github.com/a2aproject/A2A/blob/main/README.md
- Spec: https://github.com/a2aproject/A2A/blob/main/spec.md
- Google Blog: https://developers.googleblog.com/a2a
- Stars: 21,608
- Maturity: active

---



## agent-zero (amibars)

**TL;DR:** Personal AI framework, который растёт и учится вместе с тобой. Использует OS как tool (терминал, код). Multi-agent кооперация — агенты создают subordinates. Полностью кастомизируемый через prompts/. Persistent memory.

### Быстрый выбор
- ✅ Используй если:
  - Agent Zero AI framework
  - Agent Zero is not a predefined agentic framework. It is designed to be dynamic, organically growing, and learning as you use it.
  - Agent Zero is fully transparent, readable, comprehensible, customizable, and interactive.
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/frdel/agent-zero/tree/main/docs
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** Python, Docker, React
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Agent Zero AI framework
- Agent Zero is not a predefined agentic framework. It is designed to be dynamic, organically growing, and learning as you use it.
- Agent Zero is fully transparent, readable, comprehensible, customizable, and interactive.
- Agent Zero uses the computer as a tool to accomplish its (your) tasks.

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** Agent Zero AI framework
- **Maturity:** stale
- **Latency/Cost:** balanced
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/amibars/agent-zero
- Original README: https://github.com/frdel/agent-zero/blob/main/README.md
- Docs: https://github.com/frdel/agent-zero/tree/main/docs
- Video: https://youtu.be/MdzLhWWoxEs

---



## zerepy (amibars)

**TL;DR:** ZerePy — open-source Python framework для деплоя AI агентов на Twitter/X и других платформах. Модульная архитектура: LLMs (OpenAI, Anthropic, Ollama, Galadriel, XAI/Grok), socials (X, Farcaster, Echochambers, Discord), onchain (Solana, EVM, GOAT, Monad). Построен на Zerebro backend. Fine-tuning нужен для creative outputs.

### Быстрый выбор
- ✅ Используй если:
  - ZerePy an open-source launch-pad for AI agents
  - CLI interface for managing agents
  - Modular connection system
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/blorm-network/ZerePy/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** Python, Go, React, Solana, Ethereum
- **Entrypoints:** См. README

### 🧪 Примеры задач
- ZerePy an open-source launch-pad for AI agents
- CLI interface for managing agents
- Modular connection system
- Blockchain integration

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** ZerePy an open-source launch-pad for AI agents
- **Maturity:** stale
- **Latency/Cost:** balanced
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/amibars/ZerePy
- Original README: https://github.com/blorm-network/ZerePy/blob/main/README.md
- Replit: https://replit.com/@blormdev/ZerePy?v=1
- Maturity: active

---



## goose (Block)

**TL;DR:** Open source AI agent от Block (Square/Cash App). Полноценный developer agent — не просто code suggestions, а install deps, execute, edit, test. Работает с любым LLM. CLI-first. MCP support. 29k stars.

### Быстрый выбор
- ✅ Используй если:
  - an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM
  - Quickstart
  - Installation
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://block.github.io/goose/
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM
- Quickstart
- Installation
- Tutorials

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** an open source, extensible AI agent that goes beyond code suggestions - install, execute, edit, and test with any LLM
- **Maturity:** active
- **Latency/Cost:** quality
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/block/goose
- Original README: https://github.com/block/goose/blob/main/README.md
- Docs: https://block.github.io/goose/
- Stars: 29,095
- Maturity: active

---



## UI-TARS-desktop (ByteDance)

**TL;DR:** Multimodal AI Agent Stack от ByteDance. Computer use агент для desktop automation. Vision + GUI interaction. Screen understanding, mouse/keyboard control, task execution. Electron app. 25k stars.

### Быстрый выбор
- ✅ Используй если:
  - The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra
  - 🤖 Natural language control powered by Vision-Language Model
  - 🖥️ Screenshot and visual recognition support
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/bytedance/UI-TARS-desktop/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** Node.js
- **Entrypoints:** См. README

### 🧪 Примеры задач
- The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra
- 🤖 Natural language control powered by Vision-Language Model
- 🖥️ Screenshot and visual recognition support
- 🎯 Precise mouse and keyboard control

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra
- **Maturity:** active
- **Latency/Cost:** quality
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/bytedance/UI-TARS-desktop
- Original README: https://github.com/bytedance/UI-TARS-desktop/blob/main/README.md
- Stars: 24,851
- Maturity: active

---



## oasis (camel-ai)

**TL;DR:** OASIS (Open Agent Social Interaction Simulations). A simulator for large-scale agent societies. Can simulate up to one million agents interacting in a virtual social network. Useful for researching social dynamics, spread of misinformation, and agent behaviors at scale. 2k stars.

### Быстрый выбор
- ✅ Используй если:
  - 🏝️ OASIS: Open Agent Social Interaction Simulations with One Million Agents.
  - Can 1,000,000 AI agents simulate social media?
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/camel-ai/oasis/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** Python
- **Entrypoints:** См. README

### 🧪 Примеры задач
- 🏝️ OASIS: Open Agent Social Interaction Simulations with One Million Agents.
- Can 1,000,000 AI agents simulate social media?

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** 🏝️ OASIS: Open Agent Social Interaction Simulations with One Million Agents.
- **Maturity:** active
- **Latency/Cost:** balanced
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/camel-ai/oasis
- Original README: https://github.com/camel-ai/oasis/blob/main/README.md
- Stars: 2,372
- Maturity: active

---



## eliza (elizaOS)

**TL;DR:** TypeScript multi-agent simulation framework. Autonomous agents с personality, memory, relationships. Discord, Twitter, Telegram integrations. Crypto/DeFi focus с wallet management. Originally for AI companions/characters. 17k stars.

### Быстрый выбор
- ✅ Используй если:
  - Autonomous agents for everyone
  - 🔌 Rich Connectivity: Out-of-the-box connectors for Discord, Telegram, Farcaster, and more.
  - 🧠 Model Agnostic: Supports all major models, including OpenAI, Gemini, Anthropic, Llama, and Grok.
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://elizaos.github.io/eliza/
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** Node.js, Go, React, Web3
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Autonomous agents for everyone
- 🔌 Rich Connectivity: Out-of-the-box connectors for Discord, Telegram, Farcaster, and more.
- 🧠 Model Agnostic: Supports all major models, including OpenAI, Gemini, Anthropic, Llama, and Grok.
- 🖥️ Modern Web UI: A professional dashboard for managing agents, groups, and conversations in real-time.

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** Autonomous agents for everyone
- **Maturity:** active
- **Latency/Cost:** balanced
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/elizaOS/eliza
- Original README: https://github.com/elizaOS/eliza/blob/main/README.md
- Docs: https://elizaos.github.io/eliza/
- Discord: https://discord.gg/elizaos
- Stars: 17,420
- Maturity: active

---



## AutoAgent (HKUDS)

**TL;DR:** Fully-automated zero-code LLM agent framework. Визуальный builder для agents без программирования. Natural language → working agent. Academic research project из HKU. 8k stars.

### Быстрый выбор
- ✅ Используй если:
  - "AutoAgent: Fully-Automated and Zero-Code LLM Agent Framework"
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/HKUDS/AutoAgent
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- "AutoAgent: Fully-Automated and Zero-Code LLM Agent Framework"

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** "AutoAgent: Fully-Automated and Zero-Code LLM Agent Framework"
- **Maturity:** maintained
- **Latency/Cost:** quality
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/HKUDS/AutoAgent
- Paper: linked in repo
- Stars: 8,486
- Maturity: active

---



## agents-course (HuggingFace)

**TL;DR:** HuggingFace Agents Course. Полный курс по AI agents от HuggingFace. От basics до advanced multi-agent systems. Hands-on notebooks, видео, практические проекты. 25k stars.

### Быстрый выбор
- ✅ Используй если:
  - This repository contains the Hugging Face Agents Course.
  - Basic knowledge of Python
  - Basic knowledge of LLMs
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/huggingface/agents-course/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** Python
- **Entrypoints:** См. README

### 🧪 Примеры задач
- This repository contains the Hugging Face Agents Course.
- Basic knowledge of Python
- Basic knowledge of LLMs

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** This repository contains the Hugging Face Agents Course.
- **Maturity:** active
- **Latency/Cost:** balanced
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/huggingface/agents-course
- Original README: https://github.com/huggingface/agents-course/blob/main/README.md
- Stars: 24,990
- Maturity: educational

---



## autogen (Microsoft)

**TL;DR:** Microsoft's flagship agentic AI framework. Multi-agent conversations с code execution, function calling, human-in-the-loop. Поддержка GPT-4, Claude, local models. AutoGen Studio для visual agent building. 54k stars — enterprise-grade от Microsoft Research.

### Быстрый выбор
- ✅ Используй если:
  - A programming framework for agentic AI
  - Core API implements message passing, event-driven agents, and local and distributed runtime for flexibility and power. It also support cross-language support for .NET and Python.
  - AgentChat API implements a simpler but opinionated API for rapid prototyping. This API is built on top of the Core API and is closest to what users of v0.2 are familiar with and supports common multi-agent patterns such as two-agent chat or group chats.
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://microsoft.github.io/autogen/
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** Python, Go
- **Entrypoints:** См. README

### 🧪 Примеры задач
- A programming framework for agentic AI
- Core API implements message passing, event-driven agents, and local and distributed runtime for flexibility and power. It also support cross-language support for .NET and Python.
- AgentChat API implements a simpler but opinionated API for rapid prototyping. This API is built on top of the Core API and is closest to what users of v0.2 are familiar with and supports common multi-agent patterns such as two-agent chat or group chats.
- Extensions API enables first- and third-party extensions continuously expanding framework capabilities. It support specific implementation of LLM clients (e.g., OpenAI, AzureOpenAI), and capabilities such as code execution.

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** A programming framework for agentic AI
- **Maturity:** active
- **Latency/Cost:** balanced
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/microsoft/autogen
- Original README: https://github.com/microsoft/autogen/blob/main/README.md
- Docs: https://microsoft.github.io/autogen/
- AutoGen Studio: https://autogen-studio.com
- Discord: https://discord.gg/autogen
- Stars: 53,937
- Maturity: active

---



## agent-zero

**TL;DR:** Personal assistant framework с long-term memory, tool usage, и multi-agent support. Runs locally или in Docker. Persistent memory across sessions. Terminal, browser, file access. Self-improving через learnings. 14k stars.

### Быстрый выбор
- ✅ Используй если:
  - Agent Zero AI framework
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/agent0ai/agent-zero
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Agent Zero AI framework

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** Agent Zero AI framework
- **Maturity:** active
- **Latency/Cost:** balanced
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/agent0ai/agent-zero
- Discord: https://discord.gg/agent0
- Stars: 13,900
- Maturity: active
---



## browser-use (amibars)

**TL;DR:** Python библиотека для browser automation с AI агентами. Агенты видят страницу (vision + HTML), могут кликать, вводить текст, навигировать. CLI для быстрого тестирования. Cloud sandbox для production.

### Быстрый выбор
- ✅ Используй если:
  - Make websites accessible for AI agents
  - default - Minimal setup to get started quickly
  - advanced - All configuration options with detailed comments
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://docs.browser-use.com
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** Python, Go
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Make websites accessible for AI agents
- default - Minimal setup to get started quickly
- advanced - All configuration options with detailed comments
- tools - Examples of custom tools and extending the agent

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** Make websites accessible for AI agents
- **Maturity:** stale
- **Latency/Cost:** balanced
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/amibars/browser-use
- Original README: https://github.com/browser-use/browser-use/blob/main/README.md
- Docs: https://docs.browser-use.com
- Cloud: https://cloud.browser-use.com

---



## cdp-agentkit-nodejs (amibars)

**TL;DR:** Coinbase Developer Platform AgentKit для Node.js. AI агенты для Base/EVM: deploy tokens, mint NFTs, Zora Wow, Basenames. LangChain.js + Twitter integration.

### Быстрый выбор
- ✅ Используй если:
  - The Coinbase Developer Platform (CDP) AgentKit for Node.js simplifies the process of bringing your AI agents on-chain.
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://docs.cdp.coinbase.com/agentkit
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- The Coinbase Developer Platform (CDP) AgentKit for Node.js simplifies the process of bringing your AI agents on-chain.

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** The Coinbase Developer Platform (CDP) AgentKit for Node.js simplifies the process of bringing your AI agents on-chain.
- **Maturity:** stale
- **Latency/Cost:** balanced
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/amibars/cdp-agentkit-nodejs
- Original README: https://github.com/coinbase/cdp-agentkit/blob/main/README.md
- Docs: https://docs.cdp.coinbase.com/agentkit
- CDP Portal: https://portal.cdp.coinbase.com
- Maturity: active

---



## openagent (amibars)

**TL;DR:** OpenAgent — платформа для создания, сражения и торговли AI агентами на Solana blockchain. Multi-agent AI platform с GPT-4 powered agents, WebSocket real-time communication, decentralized token economy. Frontend на React/TypeScript, backend на Node.js/Express, PostgreSQL датабаза. Wallet authentication через Solana, customizable agent behaviors.

### Быстрый выбор
- ✅ Используй если:
  - Create, Battle, and Trade Intelligent AI Agents
  - Intelligent AI Agents: Customizable agents powered by OpenAI GPT-4
  - Real-Time Communication: Instant messaging via WebSocket
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/openagentoa/openagent/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** TypeScript, Node.js, PostgreSQL, React, Solana
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Create, Battle, and Trade Intelligent AI Agents
- Intelligent AI Agents: Customizable agents powered by OpenAI GPT-4
- Real-Time Communication: Instant messaging via WebSocket
- Blockchain Integration: Secure transactions on the Solana network

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** Create, Battle, and Trade Intelligent AI Agents
- **Maturity:** stale
- **Latency/Cost:** balanced
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/amibars/openagent
- Original README: https://github.com/openagentoa/openagent/blob/main/README.md
- Website: https://openagentoa.com
- Twitter: https://x.com/OpenAgentOA
- Maturity: experimental

---



## web-ui (amibars)

**TL;DR:** Web интерфейс для browser-use. Локальная установка или Docker. VNC viewer для наблюдения за браузером. Поддержка собственного Chrome с cookies и auth.

### Быстрый выбор
- ✅ Используй если:
  - Run AI Agent in your browser.
  - Windows (Command Prompt):
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://docs.browser-use.com/quickstart
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** Python, Docker
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Run AI Agent in your browser.
- Windows (Command Prompt):

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** Run AI Agent in your browser.
- **Maturity:** stale
- **Latency/Cost:** balanced
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/amibars/web-ui
- Original README: https://github.com/browser-use/web-ui/blob/main/README.md
- Docs: https://docs.browser-use.com/quickstart
- VNC: порт 6080 (default password: youvncpassword)

---



## zerepy

**TL;DR:** An open-source framework specifically designed for building "Zere" (autonomous, social-media native) agents on Solana. Features built-in connectors for Twitter/X interactions and on-chain token management. 600 stars.

### Быстрый выбор
- ✅ Используй если:
  - ZerePy an open-source framework for AI agents written in Python
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/blorm-network/ZerePy
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- ZerePy an open-source framework for AI agents written in Python

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** ZerePy an open-source framework for AI agents written in Python
- **Maturity:** maintained
- **Latency/Cost:** balanced
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/blorm-network/ZerePy
- Stars: ~587
- Maturity: active

---



## axium

**TL;DR:** Axium AI is a sophisticated semi-automated cryptocurrency trading agent framework designed to enhance and streamline the trading process.

### Быстрый выбор
- ✅ Используй если:
  - axium
  - Docker: Provides a containerized environment for easy deployment and scaling.
  - CLI: Offers command-line commands to control the agent's operations.
- ❌ Не используй если:
  - Other stacks / needs review
  - Нужны входные данные/доступы: data

### 🚀 Запуск
```bash
# См. документацию: https://github.com/amibars/axium/blob/master/README.md
```

### 🧩 Архитектура
- **Category:** AI
- **Stack:** Python, Docker
- **Entrypoints:** См. README

### 🧪 Примеры задач
- axium
- Docker: Provides a containerized environment for easy deployment and scaling.
- CLI: Offers command-line commands to control the agent's operations.
- Data Sources: Modules to gather market data from platforms like Pumpfun and Raydium.

### ⚠️ Ограничения
- Other stacks / needs review
- Нужны данные/доступы: data

### 🧭 Fit / Maturity / Ops
- **Fit:** axium
- **Maturity:** stale
- **Latency/Cost:** fast
- **Data constraints:** data
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/amibars/axium
- Original README: https://github.com/amibars/axium/blob/master/README.md

---
