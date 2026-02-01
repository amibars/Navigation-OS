# LLM UI

> Generated from README.md on 2026-01-29
## Index
- [open-webui](#open-webui)
- [big-AGI](#big-agi)
- [ChatGemini](#chatgemini)

---

## open-webui

**TL;DR:** User-friendly ChatGPT-like web UI для локальных и cloud LLMs. Ollama, OpenAI, Claude, любые OpenAI-compatible APIs. Multi-user с RBAC, RAG на документах, voice input, image generation. 122k stars — стандарт для self-hosted LLM UI.

### Быстрый выбор
- ✅ Используй если:
  - Self-hosted ChatGPT-like UI
  - 🚀 Effortless Setup: Install seamlessly using Docker or Kubernetes (kubectl, kustomize or helm) for a hassle-free experience with support for both :ollama and :cuda tagged images.
  - 🤝 Ollama/OpenAI API Integration: Effortlessly integrate OpenAI-compatible APIs for versatile conversations alongside Ollama models. Customize the OpenAI API URL to link with LMStudio, GroqCloud, Mistral, OpenRouter, and more.
- ❌ Не используй если:
  - API-only
  - Нужны входные данные/доступы: Ollama/API

### 🚀 Запуск
```bash
docker run -p 3000:8080 ghcr.io/open-webui/open-webui:main
```

### 🧩 Архитектура
- **Category:** LLM UI
- **Stack:** Python, Docker, PostgreSQL, Redis, CUDA
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Self-hosted ChatGPT-like UI
- 🚀 Effortless Setup: Install seamlessly using Docker or Kubernetes (kubectl, kustomize or helm) for a hassle-free experience with support for both :ollama and :cuda tagged images.
- 🤝 Ollama/OpenAI API Integration: Effortlessly integrate OpenAI-compatible APIs for versatile conversations alongside Ollama models. Customize the OpenAI API URL to link with LMStudio, GroqCloud, Mistral, OpenRouter, and more.
- 🛡️ Granular Permissions and User Groups: By allowing administrators to create detailed user roles and permissions, we ensure a secure user environment. This granularity not only enhances security but also allows for customized user experiences, fostering a sense of ownership and responsibility amongst users.

### ⚠️ Ограничения
- API-only
- Нужны данные/доступы: Ollama/API

### 🧭 Fit / Maturity / Ops
- **Fit:** Self-hosted ChatGPT-like UI
- **Maturity:** active
- **Latency/Cost:** balanced
- **Data constraints:** Ollama/API
- **Ops friction:** medium

### Full links
- Repo: https://github.com/open-webui/open-webui
- Original README: https://github.com/open-webui/open-webui/blob/main/README.md
- Docs: https://docs.openwebui.com
- Demo: https://openwebui.com
- Discord: https://discord.gg/open-webui
- Stars: 121,944
- Maturity: active

---



## big-AGI

**TL;DR:** Personal AI suite — multi-model chat, image generation, voice, code execution. Supports 30+ LLM providers. Beautiful UI. Self-hosted. Best open ChatGPT alternative с full features. 7k stars.

### Быстрый выбор
- ✅ Используй если:
  - AGI suite, multi-model chat
  - Develop locally or self-host with Docker on your own infrastructure – guide
  - Or fork & run on Vercel:
- ❌ Не используй если:
  - Simple chat
  - Нужны входные данные/доступы: API keys

### 🚀 Запуск
```bash
docker compose up
```

### 🧩 Архитектура
- **Category:** LLM UI
- **Stack:** Go, Docker, MongoDB
- **Entrypoints:** См. README

### 🧪 Примеры задач
- AGI suite, multi-model chat
- Develop locally or self-host with Docker on your own infrastructure – guide
- Or fork & run on Vercel:

### ⚠️ Ограничения
- Simple chat
- Нужны данные/доступы: API keys

### 🧭 Fit / Maturity / Ops
- **Fit:** AGI suite, multi-model chat
- **Maturity:** active
- **Latency/Cost:** balanced
- **Data constraints:** API keys
- **Ops friction:** medium

### Full links
- Repo: https://github.com/enricoros/big-AGI
- Original README: https://github.com/enricoros/big-AGI/blob/main/README.md
- Demo: https://big-agi.com
- Stars: 6,830
- Maturity: active

---



## ChatGemini

**TL;DR:** Conversational Web Client for Google Gemini. A clean, responsive chat interface mimicking the ChatGPT experience, powered by the Gemini Pro API. Supports streaming, markdown rendering, and chat history. 1k stars.

### Быстрый выбор
- ✅ Используй если:
  - Web client for Gemini
- ❌ Не используй если:
  - Other LLMs
  - Нужны входные данные/доступы: API key

### 🚀 Запуск
```bash
# См. документацию: https://github.com/bclswl0827/ChatGemini/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** LLM UI
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Web client for Gemini

### ⚠️ Ограничения
- Other LLMs
- Нужны данные/доступы: API key

### 🧭 Fit / Maturity / Ops
- **Fit:** Web client for Gemini
- **Maturity:** active
- **Latency/Cost:** fast
- **Data constraints:** API key
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/bclswl0827/ChatGemini
- Original README: https://github.com/bclswl0827/ChatGemini/blob/main/README.md
- Stars: ~930
- Maturity: active

---
