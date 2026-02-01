# Infra

> Generated from README.md on 2026-01-29
## Index
- [exo](#exo)
- [swarmnode-python](#swarmnode-python)
- [portkey-gateway](#portkey-gateway)
- [cloudflare/agents](#cloudflare-agents)
- [LLMRouter](#llmrouter)
- [ezlocalai](#ezlocalai)

---

## exo

**TL;DR:** exo: Run frontier AI locally. Maintained by exo labs.

### Быстрый выбор
- ✅ Используй если:
  - Distributed AI inference across devices
  - Automatic Device Discovery: Devices running exo automatically discover each other - no manual configuration.
  - RDMA over Thunderbolt: exo ships with day-0 support for RDMA over Thunderbolt 5, enabling 99% reduction in latency between devices.
- ❌ Не используй если:
  - Single GPU
  - Нужны входные данные/доступы: devices

### 🚀 Запуск
```bash
pip install exo
```

### 🧩 Архитектура
- **Category:** Infra
- **Stack:** Python, Node.js, Rust
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Distributed AI inference across devices
- Automatic Device Discovery: Devices running exo automatically discover each other - no manual configuration.
- RDMA over Thunderbolt: exo ships with day-0 support for RDMA over Thunderbolt 5, enabling 99% reduction in latency between devices.
- Topology-Aware Auto Parallel: exo figures out the best way to split your model across all available devices based on a realtime view of your device topology. It takes into account device resources and network latency/bandwidth between each link.

### ⚠️ Ограничения
- Single GPU
- Нужны данные/доступы: devices

### 🧭 Fit / Maturity / Ops
- **Fit:** Distributed AI inference across devices
- **Maturity:** active
- **Latency/Cost:** quality
- **Data constraints:** devices
- **Ops friction:** low

### Full links
- Repo: https://github.com/exo-explore/exo
- Original README: https://github.com/exo-explore/exo/blob/main/README.md
- Docs: https://docs.exolabs.net

---



## swarmnode-python

**TL;DR:** The SwarmNode Python SDK provides convenient access to the SwarmNode REST API from any Python 3.8+ application. The SDK includes rich type definitions and enables receiving real-time executions via WebSockets.

### Быстрый выбор
- ✅ Используй если:
  - Serverless AI agents
- ❌ Не используй если:
  - Self-hosted only
  - Нужны входные данные/доступы: API key

### 🚀 Запуск
```bash
pip install swarmnode
```

### 🧩 Архитектура
- **Category:** Infra
- **Stack:** Python
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Serverless AI agents

### ⚠️ Ограничения
- Self-hosted only
- Нужны данные/доступы: API key

### 🧭 Fit / Maturity / Ops
- **Fit:** Serverless AI agents
- **Maturity:** active
- **Latency/Cost:** balanced
- **Data constraints:** API key
- **Ops friction:** low

### Full links
- Repo: https://github.com/amibars/swarmnode-python
- Original README: https://github.com/amibars/swarmnode-python/blob/main/README.md
- Docs: https://swarmnode.ai/docs/sdk/introduction
- API: https://swarmnode.ai/docs/api/v1/introduction

---



## portkey-gateway

**TL;DR:** Open‑source AI Gateway от Portkey: единый OpenAI‑совместимый API для 250+ LLM, routing, retries/fallbacks, guardrails, кэш и MCP Gateway.

### Быстрый выбор
- ✅ Используй если:
  - LLM gateway + routing/guardrails
  - [x] Blazing fast (<1ms latency) with a tiny footprint (122kb)
  - [x] Battle tested, with over 10B tokens processed everyday
- ❌ Не используй если:
  - Single provider
  - Нужны входные данные/доступы: Provider keys

### 🚀 Запуск
```bash
npx @portkey-ai/gateway
```

### 🧩 Архитектура
- **Category:** Infra
- **Stack:** Python, JavaScript, Node.js, Go, Docker
- **Entrypoints:** См. README

### 🧪 Примеры задач
- LLM gateway + routing/guardrails
- [x] Blazing fast (<1ms latency) with a tiny footprint (122kb)
- [x] Battle tested, with over 10B tokens processed everyday
- [x] Enterprise-ready with enhanced security, scale, and custom deployments

### ⚠️ Ограничения
- Single provider
- Нужны данные/доступы: Provider keys

### 🧭 Fit / Maturity / Ops
- **Fit:** LLM gateway + routing/guardrails
- **Maturity:** active
- **Latency/Cost:** fast
- **Data constraints:** Provider keys
- **Ops friction:** medium

### Full links
- Repo: https://github.com/galadriel-ai/portkey-gateway
- Original README: https://github.com/Portkey-AI/gateway/blob/main/README.md

---



## cloudflare/agents

**TL;DR:** Official framework for building and deploying AI Agents on Cloudflare Workers. Leverage Cloudflare's global edge network, serverless inference (Workers AI), and durable state (Durable Objects) for scalable, low-latency agents. 3k stars.

### Быстрый выбор
- ✅ Используй если:
  - AI Agents on Cloudflare
  - Maintain persistent state and memory
  - Engage in real-time communication
- ❌ Не используй если:
  - Non-Cloudflare
  - Нужны входные данные/доступы: —

### 🚀 Запуск
```bash
# См. документацию: https://github.com/cloudflare/agents/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** Infra
- **Stack:** React
- **Entrypoints:** См. README

### 🧪 Примеры задач
- AI Agents on Cloudflare
- Maintain persistent state and memory
- Engage in real-time communication
- Process and learn from interactions

### ⚠️ Ограничения
- Non-Cloudflare
- Нужны данные/доступы: —

### 🧭 Fit / Maturity / Ops
- **Fit:** AI Agents on Cloudflare
- **Maturity:** active
- **Latency/Cost:** fast
- **Data constraints:** —
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/cloudflare/agents
- Original README: https://github.com/cloudflare/agents/blob/main/README.md
- Stars: 3,048
- Maturity: active

---



## LLMRouter

**TL;DR:** LLMRouter is an intelligent routing system designed to optimize LLM inference by dynamically selecting the most suitable model for each query. To achieve intelligent routing, it defines:

### Быстрый выбор
- ✅ Используй если:
  - LLM routing library
  - ⭐ [2026-01]: LLMRouter just crossed 1K GitHub stars! We’ve also released llmrouter-lib v0.2.0. Updates include service-specific dict configs (OpenAI, Anthropic, etc.) and multimodal routing (Video/Image + Text) on Geometry3K, MathVista, and Charades-Ego—all in the first unified open-source LLM routing library with 16+ routers, a unified CLI, Gradio UI, and 11 datasets. Install via pip install llmrouter-lib. More updates soon! 🚀
- ❌ Не используй если:
  - Single LLM
  - Нужны входные данные/доступы: API keys

### 🚀 Запуск
```bash
pip install llmrouter
```

### 🧩 Архитектура
- **Category:** Infra
- **Stack:** Python, PyTorch, CUDA
- **Entrypoints:** См. README

### 🧪 Примеры задач
- LLM routing library
- ⭐ [2026-01]: LLMRouter just crossed 1K GitHub stars! We’ve also released llmrouter-lib v0.2.0. Updates include service-specific dict configs (OpenAI, Anthropic, etc.) and multimodal routing (Video/Image + Text) on Geometry3K, MathVista, and Charades-Ego—all in the first unified open-source LLM routing library with 16+ routers, a unified CLI, Gradio UI, and 11 datasets. Install via pip install llmrouter-lib. More updates soon! 🚀

### ⚠️ Ограничения
- Single LLM
- Нужны данные/доступы: API keys

### 🧭 Fit / Maturity / Ops
- **Fit:** LLM routing library
- **Maturity:** active
- **Latency/Cost:** fast
- **Data constraints:** API keys
- **Ops friction:** low

### Full links
- Repo: https://github.com/ulab-uiuc/LLMRouter
- Original README: https://github.com/ulab-uiuc/LLMRouter/blob/main/README.md
- Stars: 1,182
- Maturity: active

---



## ezlocalai

**TL;DR:** An easy-to-setup local AI server that exposes an OpenAI-compatible API. Supports LLMs (Llama, Mistral), Vision, Speech-to-Text (Whisper), and Text-to-Speech, aiming to be a "one-click" replacement for cloud providers. 90 stars.

### Быстрый выбор
- ✅ Используй если:
  - Local AI server, OpenAI style
- ❌ Не используй если:
  - Cloud APIs
  - Нужны входные данные/доступы: —

### 🚀 Запуск
```bash
# См. документацию: https://github.com/DevXT-LLC/ezlocalai
```

### 🧩 Архитектура
- **Category:** Infra
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Local AI server, OpenAI style

### ⚠️ Ограничения
- Cloud APIs
- Нужны данные/доступы: —

### 🧭 Fit / Maturity / Ops
- **Fit:** Local AI server, OpenAI style
- **Maturity:** active
- **Latency/Cost:** balanced
- **Data constraints:** —
- **Ops friction:** medium

### Full links
- Repo: https://github.com/DevXT-LLC/ezlocalai
- Stars: ~91
- Maturity: active

---
