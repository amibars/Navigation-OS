# ML

> Generated from README.md on 2026-01-29
## Index
- [pyspur](#pyspur)
- [rig](#rig)
- [consistencydecoder](#consistencydecoder)
- [Search-R1](#search-r1)
- [gemini-browser (browserbase)](#gemini-browser-browserbase)
- [free-llm-api-resources](#free-llm-api-resources)
- [3FS (DeepSeek)](#3fs-deepseek)
- [Janus (DeepSeek)](#janus-deepseek)
- [imaginairy](#imaginairy)
- [awesome-full-stack-machine-learning-courses](#awesome-full-stack-machine-learning-courses)
- [auto-gpt](#auto-gpt)
- [moltbot](#moltbot)
- [git-sync](#git-sync)
- [goku (Saiyan-World)](#goku-saiyan-world)
- [csm (SesameAILabs)](#csm-sesameailabs)
- [llm_api_testing](#llm-api-testing)
- [python-sdk (agixt)](#python-sdk-agixt)
- [bolt.diy (amibars)](#bolt-diy-amibars)
- [portkey-gateway (amibars)](#portkey-gateway-amibars)

---

## pyspur

**TL;DR:** PySpur — визуальный playground для построения и отладки agentic workflows. Решает три боли AI-инженеров: prompt hell (бесконечные tweaking), workflow blindspots (невидимые failures между шагами), и terminal testing nightmare (парсинг JSON вручную). Human-in-the-loop breakpoints, multimodal support (PDF, video, audio, images), 100+ LLM провайдеров, встроенный RAG pipeline. One-click deploy как API.

### Быстрый выбор
- ✅ Используй если:
  - Visual LLM workflow editor
  - Prompt Hell: Hours of prompt tweaking and trial-and-error frustration.
  - Workflow Blindspots: Lack of visibility into step interactions causing hidden failures and confusion.
- ❌ Не используй если:
  - CLI-only workflows
  - Нужны входные данные/доступы: API keys

### 🚀 Запуск
```bash
docker compose up
```

### 🧩 Архитектура
- **Category:** ML
- **Stack:** Python, TypeScript, Docker, PostgreSQL
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Visual LLM workflow editor
- Prompt Hell: Hours of prompt tweaking and trial-and-error frustration.
- Workflow Blindspots: Lack of visibility into step interactions causing hidden failures and confusion.
- Terminal Testing Nightmare Squinting at raw outputs and manually parsing JSON.

### ⚠️ Ограничения
- CLI-only workflows
- Нужны данные/доступы: API keys

### 🧭 Fit / Maturity / Ops
- **Fit:** Visual LLM workflow editor
- **Maturity:** active
- **Latency/Cost:** balanced
- **Data constraints:** API keys
- **Ops friction:** medium

### Full links
- Repo: https://github.com/amibars/pyspur
- Original README: https://github.com/PySpur-Dev/pyspur/blob/main/README.md
- Stars: 13,500+
- Maturity: active

---



## rig

**TL;DR:** &nbsp; &nbsp; &nbsp;

### Быстрый выбор
- ✅ Используй если:
  - Rust LLM applications
  - Agentic workflows that can handle multi-turn streaming and prompting
  - Full GenAI Semantic Convention compatibility
- ❌ Не используй если:
  - Python projects
  - Нужны входные данные/доступы: —

### 🚀 Запуск
```bash
cargo add rig-core
```

### 🧩 Архитектура
- **Category:** ML
- **Stack:** Rust, Go, MongoDB, Solana
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Rust LLM applications
- Agentic workflows that can handle multi-turn streaming and prompting
- Full GenAI Semantic Convention compatibility
- 20+ model providers, all under one singular unified interface

### ⚠️ Ограничения
- Python projects
- Нужны данные/доступы: —

### 🧭 Fit / Maturity / Ops
- **Fit:** Rust LLM applications
- **Maturity:** active
- **Latency/Cost:** fast
- **Data constraints:** —
- **Ops friction:** low

### Full links
- Repo: https://github.com/0xPlaygrounds/rig
- Original README: https://github.com/0xPlaygrounds/rig/blob/main/README.md
- Docs: https://docs.rig.rs

---



## consistencydecoder

**TL;DR:** OpenAI Consistency Distilled Diff VAE. Улучшенный VAE decoder для image generation. Замена стандартного VAE в Stable Diffusion. Лучшее качество декодирования latents.

### Быстрый выбор
- ✅ Используй если:
  - OpenAI Consistency VAE
- ❌ Не используй если:
  - Non-image tasks
  - Нужны входные данные/доступы: images

### 🚀 Запуск
```bash
# См. документацию: https://github.com/amibars/consistencydecoder
```

### 🧩 Архитектура
- **Category:** ML
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- OpenAI Consistency VAE

### ⚠️ Ограничения
- Non-image tasks
- Нужны данные/доступы: images

### 🧭 Fit / Maturity / Ops
- **Fit:** OpenAI Consistency VAE
- **Maturity:** unknown
- **Latency/Cost:** quality
- **Data constraints:** images
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/amibars/consistencydecoder
- Maturity: unknown

---



## Search-R1

**TL;DR:** Efficient RL Training Framework combining Reasoning models (like R1) with Search Engine calls. Trains agents to "think, then search, then think". Scalable implementation of retrieval-augmented reasoning. 4k stars.

### Быстрый выбор
- ✅ Используй если:
  - RL for reasoning + search
  - Support local sparse retrievers (e.g., BM25). ✔️
  - Support local dense retrievers (both flat indexing and ANN indexing) ✔️
- ❌ Не используй если:
  - Simple search
  - Нужны входные данные/доступы: —

### 🚀 Запуск
```bash
# См. документацию: https://github.com/PeterGriffinJin/Search-R1/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** ML
- **Stack:** Python, FastAPI, PyTorch, CUDA
- **Entrypoints:** См. README

### 🧪 Примеры задач
- RL for reasoning + search
- Support local sparse retrievers (e.g., BM25). ✔️
- Support local dense retrievers (both flat indexing and ANN indexing) ✔️
- Support google search / bing search / brave search API and others. ✔️

### ⚠️ Ограничения
- Simple search
- Нужны данные/доступы: —

### 🧭 Fit / Maturity / Ops
- **Fit:** RL for reasoning + search
- **Maturity:** active
- **Latency/Cost:** quality
- **Data constraints:** —
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/PeterGriffinJin/Search-R1
- Original README: https://github.com/PeterGriffinJin/Search-R1/blob/main/README.md
- Stars: 3,868
- Maturity: active

---



## gemini-browser (browserbase)

**TL;DR:** A starter kit demonstrating "Computer Use" with Google's Gemini 2.0 Flash model running on Browserbase. Enables Gemini to control a headless browser, navigate websites, click elements, and extract data using natural language instructions. 300 stars.

### Быстрый выбор
- ✅ Используй если:
  - Try the new Gemini Computer Use model on Browserbase.
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/browserbase/gemini-browser
```

### 🧩 Архитектура
- **Category:** ML
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Try the new Gemini Computer Use model on Browserbase.

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** Try the new Gemini Computer Use model on Browserbase.
- **Maturity:** active
- **Latency/Cost:** quality
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/browserbase/gemini-browser
- Stars: ~314
- Maturity: active

---



## free-llm-api-resources

**TL;DR:** Curated list of free LLM inference resources via API — бесплатные способы использовать GPT-4, Claude, Llama, Mistral и другие модели. Включает rate limits, endpoint info, supported models. Essential resource для developers без бюджета на API. Regularly updated. 8k stars — go-to лист для бесплатных LLM. - Free API proxies: community-hosted endpoints - Free tiers: official provider free tiers (OpenRouter, Groq, etc.) - Rate limits: requests per day/minute info - Supported models: GPT-4, Claude, Llama, Mistral, Gemini - Endpoint formats: OpenAI-compatible, custom APIs - Ключевые секции: README.md — main list

### Быстрый выбор
- ✅ Используй если:
  - A list of free LLM inference resources accessible via API.
  - Free Providers
  - OpenRouter
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/cheahjs/free-llm-api-resources/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** ML
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- A list of free LLM inference resources accessible via API.
- Free Providers
- OpenRouter
- Google AI Studio

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** A list of free LLM inference resources accessible via API.
- **Maturity:** active
- **Latency/Cost:** quality
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/cheahjs/free-llm-api-resources
- Original README: https://github.com/cheahjs/free-llm-api-resources/blob/main/README.md
- See also: OpenRouter free tier, Groq free tier
- Stars: 8,014
- Maturity: curated list

---



## 3FS (DeepSeek)

**TL;DR:** High-performance distributed file system optimized для AI training/inference. Supports disaggregated storage с NVMe. Used internally by DeepSeek для training large models. Open source infrastructure. 10k stars.

### Быстрый выбор
- ✅ Используй если:
  - A high-performance distributed file system designed to address the challenges of AI training and inference workloads.
  - Performance and Usability
  - Disaggregated Architecture Combines the throughput of thousands of SSDs and the network bandwidth of hundreds of storage nodes, enabling applications to access storage resource in a locality-oblivious manner.
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/deepseek-ai/3FS/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** ML
- **Stack:** Rust, Docker
- **Entrypoints:** См. README

### 🧪 Примеры задач
- A high-performance distributed file system designed to address the challenges of AI training and inference workloads.
- Performance and Usability
- Disaggregated Architecture Combines the throughput of thousands of SSDs and the network bandwidth of hundreds of storage nodes, enabling applications to access storage resource in a locality-oblivious manner.
- Strong Consistency Implements Chain Replication with Apportioned Queries (CRAQ) for strong consistency, making application code simple and easy to reason about.

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** A high-performance distributed file system designed to address the challenges of AI training and inference workloads.
- **Maturity:** active
- **Latency/Cost:** quality
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/deepseek-ai/3FS
- Original README: https://github.com/deepseek-ai/3FS/blob/main/README.md
- Stars: 9,669
- Maturity: active

---



## Janus (DeepSeek)

**TL;DR:** Unified multimodal model от DeepSeek — и understanding, и generation в одной модели. Image understanding + image generation. More efficient than separate models. Open weights. 18k stars.

### Быстрый выбор
- ✅ Используй если:
  - Janus-Series: Unified Multimodal Understanding and Generation Models
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/deepseek-ai/Janus/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** ML
- **Stack:** Python, FastAPI, CUDA
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Janus-Series: Unified Multimodal Understanding and Generation Models

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** Janus-Series: Unified Multimodal Understanding and Generation Models
- **Maturity:** maintained
- **Latency/Cost:** quality
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/deepseek-ai/Janus
- Original README: https://github.com/deepseek-ai/Janus/blob/main/README.md
- DeepSeek: https://www.deepseek.com
- Stars: 17,687
- Maturity: active

---



## imaginairy

**TL;DR:** AI imagined images. Pythonic generation of stable diffusion images.

### Быстрый выбор
- ✅ Используй если:
  - AI imagined images. Pythonic generation of stable diffusion images.
  - mask descriptions must be lowercase
  - keywords (AND, OR, NOT) must be uppercase
- ❌ Не используй если:
  - Other stacks / needs review
  - Нужны входные данные/доступы: images

### 🚀 Запуск
```bash
# См. документацию: https://github.com/dexbotsdev/imaginAIry/blob/master/README.md
```

### 🧩 Архитектура
- **Category:** ML
- **Stack:** Python, Rust, Docker, PyTorch, CUDA
- **Entrypoints:** См. README

### 🧪 Примеры задач
- AI imagined images. Pythonic generation of stable diffusion images.
- mask descriptions must be lowercase
- keywords (AND, OR, NOT) must be uppercase
- parentheses are supported

### ⚠️ Ограничения
- Other stacks / needs review
- Нужны данные/доступы: images

### 🧭 Fit / Maturity / Ops
- **Fit:** AI imagined images. Pythonic generation of stable diffusion images.
- **Maturity:** stale
- **Latency/Cost:** balanced
- **Data constraints:** images
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/dexbotsdev/imaginAIry
- Original README: https://github.com/dexbotsdev/imaginAIry/blob/master/README.md

---



## awesome-full-stack-machine-learning-courses

**TL;DR:** Curated collection of ML engineering courses from top universities — CalTech, Columbia, Berkeley, MIT, Stanford, CMU. Covers practical ML engineering: MLOps, deployment, data pipelines, production systems. Not just theory — focus on full-stack practical skills. 500 stars — gold standard для ML engineering education. - Stanford: CS229, CS231n, practical courses - Berkeley: Full Stack Deep Learning - MIT: Applied ML courses - CMU: ML engineering, systems courses - Columbia: Applied ML, data engineering - CalTech: ML foundations, applications - Ключевые секции: organized by university

### Быстрый выбор
- ✅ Используй если:
  - Curated list of publicly accessible machine learning engineering courses from CalTech, Columbia, Berkeley, MIT, and Stanford.
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/leehanchung/awesome-full-stack-machine-learning-courses
```

### 🧩 Архитектура
- **Category:** ML
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Curated list of publicly accessible machine learning engineering courses from CalTech, Columbia, Berkeley, MIT, and Stanford.

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** Curated list of publicly accessible machine learning engineering courses from CalTech, Columbia, Berkeley, MIT, and Stanford.
- **Maturity:** active
- **Latency/Cost:** balanced
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/leehanchung/awesome-full-stack-machine-learning-courses
- Stars: 505
- Maturity: educational

---



## auto-gpt

**TL;DR:** Download the latest stable release from here: https://github.com/Significant-Gravitas/Auto-GPT/releases/latest. The master branch may often be in a broken state.

### Быстрый выбор
- ✅ Используй если:
  - An experimental open-source attempt to make GPT-4 fully autonomous.
  - 🌐 Internet access for searches and information gathering
  - 💾 Long-Term and Short-Term memory management
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/luofuli/Auto-GPT/blob/master/README.md
```

### 🧩 Архитектура
- **Category:** ML
- **Stack:** Python, Go, Docker, Redis
- **Entrypoints:** См. README

### 🧪 Примеры задач
- An experimental open-source attempt to make GPT-4 fully autonomous.
- 🌐 Internet access for searches and information gathering
- 💾 Long-Term and Short-Term memory management
- 🧠 GPT-4 instances for text generation

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** An experimental open-source attempt to make GPT-4 fully autonomous.
- **Maturity:** stale
- **Latency/Cost:** balanced
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/luofuli/Auto-GPT
- Original README: https://github.com/luofuli/Auto-GPT/blob/master/README.md

---



## moltbot

**TL;DR:** Moltbot is a *personal AI assistant* you run on your own devices. It answers you on the channels you already use (WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, Microsoft Teams, WebChat), plus extension channels like Blu?

### Быстрый выбор
- ✅ Используй если:
  - Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞
  - Anthropic (Claude Pro/Max)
  - OpenAI (ChatGPT/Codex)
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/moltbot/moltbot/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** ML
- **Stack:** TypeScript, Docker, Django
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞
- Anthropic (Claude Pro/Max)
- OpenAI (ChatGPT/Codex)

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** Your own personal AI assistant. Any OS. Any Platform. The lobster way. 🦞
- **Maturity:** active
- **Latency/Cost:** fast
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/moltbot/moltbot
- Original README: https://github.com/moltbot/moltbot/blob/main/README.md

---



## git-sync

**TL;DR:** A GitHub Action for syncing between two independent repositories using force push.

### Быстрый выбор
- ✅ Используй если:
  - A GitHub Action for syncing between two independent repositories using force push
  - Sync branches between two GitHub repositories
  - Sync branches to/from a remote repository
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/nshen/git-sync/blob/master/README.md
```

### 🧩 Архитектура
- **Category:** ML
- **Stack:** Docker
- **Entrypoints:** См. README

### 🧪 Примеры задач
- A GitHub Action for syncing between two independent repositories using force push
- Sync branches between two GitHub repositories
- Sync branches to/from a remote repository
- GitHub action can be triggered on a timer or on push

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** A GitHub Action for syncing between two independent repositories using force push
- **Maturity:** stale
- **Latency/Cost:** balanced
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/nshen/git-sync
- Original README: https://github.com/nshen/git-sync/blob/master/README.md

---



## goku (Saiyan-World)

**TL;DR:** CVPR 2025 Highlight. "Goku" - A Foundation Model for Video Generation. Capable of generating high-quality, physically plausible videos from text prompts. Focuses on motion consistency and visual fidelity. 3k stars.

### Быстрый выбор
- ✅ Используй если:
  - [CVPR2025 Highlight] Video Generation Foundation Models: https://saiyan-world.github.io/goku/
  - 📊 High-quality fine-grained image and video data curation.
  - 🔄 The pioneering use of rectified flow for enhanced interaction among video and image tokens.
- ❌ Не используй если:
  - Other stacks / needs review
  - Нужны входные данные/доступы: video

### 🚀 Запуск
```bash
# См. документацию: https://github.com/Saiyan-World/goku/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** ML
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- [CVPR2025 Highlight] Video Generation Foundation Models: https://saiyan-world.github.io/goku/
- 📊 High-quality fine-grained image and video data curation.
- 🔄 The pioneering use of rectified flow for enhanced interaction among video and image tokens.
- 🌟 Superior qualitative and quantitative performance in both image and video generation tasks.

### ⚠️ Ограничения
- Other stacks / needs review
- Нужны данные/доступы: video

### 🧭 Fit / Maturity / Ops
- **Fit:** [CVPR2025 Highlight] Video Generation Foundation Models: https://saiyan-world.github.io/goku/
- **Maturity:** maintained
- **Latency/Cost:** quality
- **Data constraints:** video
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/Saiyan-World/goku
- Original README: https://github.com/Saiyan-World/goku/blob/main/README.md
- Stars: ~3,000 (CVPR Highlight)
- Maturity: research

---



## csm (SesameAILabs)

**TL;DR:** Conversational Speech Generation Model. Continuous Speech Model — generation of long-form conversational speech. Open source. 14k stars.

### Быстрый выбор
- ✅ Используй если:
  - A Conversational Speech Generation Model
  - A CUDA-compatible GPU
  - The code has been tested on CUDA 12.4 and 12.6, but it may also work on other versions
- ❌ Не используй если:
  - Other stacks / needs review
  - Нужны входные данные/доступы: audio

### 🚀 Запуск
```bash
# См. документацию: https://github.com/SesameAILabs/csm/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** ML
- **Stack:** Python, CUDA
- **Entrypoints:** См. README

### 🧪 Примеры задач
- A Conversational Speech Generation Model
- A CUDA-compatible GPU
- The code has been tested on CUDA 12.4 and 12.6, but it may also work on other versions
- Similarly, Python 3.10 is recommended, but newer versions may be fine

### ⚠️ Ограничения
- Other stacks / needs review
- Нужны данные/доступы: audio

### 🧭 Fit / Maturity / Ops
- **Fit:** A Conversational Speech Generation Model
- **Maturity:** maintained
- **Latency/Cost:** quality
- **Data constraints:** audio
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/SesameAILabs/csm
- Original README: https://github.com/SesameAILabs/csm/blob/main/README.md
- Stars: 14,462
- Maturity: active

---



## llm_api_testing

**TL;DR:** 1. Ensure LiteLLM is installed and configured 2. Set your Deepseek API key as an environment variable: export DEEPSEEK_API_KEY='your_api_key_here'

### Быстрый выбор
- ✅ Используй если:
  - llm_api_testing
  - Measures response latency in milliseconds
  - Calculates tokens processed per second
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/tom-doerr/llm_api_testing/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** ML
- **Stack:** Python
- **Entrypoints:** См. README

### 🧪 Примеры задач
- llm_api_testing
- Measures response latency in milliseconds
- Calculates tokens processed per second
- Configurable monitoring intervals

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** llm_api_testing
- **Maturity:** maintained
- **Latency/Cost:** quality
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/tom-doerr/llm_api_testing
- Original README: https://github.com/tom-doerr/llm_api_testing/blob/main/README.md

---



## python-sdk (agixt)

**TL;DR:** This repository is for the AGiXT SDK for Python.

### Быстрый выбор
- ✅ Используй если:
  - AGiXT is a dynamic AI Automation Platform that seamlessly orchestrates instruction management and complex task execution across diverse AI providers. Combining adaptive memory, smart features, and a versatile plugin system, AGiXT delivers efficient and comprehensive AI solutions.
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/AGiXT/python-sdk/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** ML
- **Stack:** Python, TypeScript
- **Entrypoints:** См. README

### 🧪 Примеры задач
- AGiXT is a dynamic AI Automation Platform that seamlessly orchestrates instruction management and complex task execution across diverse AI providers. Combining adaptive memory, smart features, and a versatile plugin system, AGiXT delivers efficient and comprehensive AI solutions.

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** AGiXT is a dynamic AI Automation Platform that seamlessly orchestrates instruction management and complex task execution across diverse AI providers. Combining adaptive memory, smart features, and a versatile plugin system, AGiXT delivers efficient and comprehensive AI solutions.
- **Maturity:** active
- **Latency/Cost:** balanced
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/AGiXT/python-sdk
- Original README: https://github.com/AGiXT/python-sdk/blob/main/README.md

---



## bolt.diy (amibars)

**TL;DR:** Open-source AI coding assistant от StackBlitz. В браузере пишешь full-stack web-приложения с любой LLM (OpenAI, Claude, Ollama, DeepSeek и 19+ других). Есть desktop app, деплой на Netlify/Vercel, Git интеграция, MCP support.

### Быстрый выбор
- ✅ Используй если:
  - Prompt, run, edit, and deploy full-stack web applications using any LLM you want!
  - AI-powered full-stack web development for NodeJS based applications directly in your browser.
  - Support for 19+ LLMs with an extensible architecture to integrate additional models.
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://stackblitz-labs.github.io/bolt.diy/
```

### 🧩 Архитектура
- **Category:** ML
- **Stack:** TypeScript, Node.js, Go, Docker, React
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Prompt, run, edit, and deploy full-stack web applications using any LLM you want!
- AI-powered full-stack web development for NodeJS based applications directly in your browser.
- Support for 19+ LLMs with an extensible architecture to integrate additional models.
- Attach images to prompts for better contextual understanding.

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** Prompt, run, edit, and deploy full-stack web applications using any LLM you want!
- **Maturity:** maintained
- **Latency/Cost:** quality
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/amibars/bolt.diy
- Original README: https://github.com/stackblitz-labs/bolt.diy/blob/main/README.md
- Docs: https://stackblitz-labs.github.io/bolt.diy/
- Community: https://thinktank.ottomator.ai/

---



## portkey-gateway (amibars)

**TL;DR:** AI Gateway с 200+ LLMs и 50+ guardrails. Fallbacks, retries, load balancing, request timeouts. Multi-modal support, realtime APIs.

### Быстрый выбор
- ✅ Используй если:
  - A Blazing Fast AI Gateway with integrated Guardrails. Route to 200+ LLMs, 50+ AI Guardrails with 1 fast & friendly API.
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://portkey.ai/docs
```

### 🧩 Архитектура
- **Category:** ML
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- A Blazing Fast AI Gateway with integrated Guardrails. Route to 200+ LLMs, 50+ AI Guardrails with 1 fast & friendly API.

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** A Blazing Fast AI Gateway with integrated Guardrails. Route to 200+ LLMs, 50+ AI Guardrails with 1 fast & friendly API.
- **Maturity:** stale
- **Latency/Cost:** quality
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/amibars/portkey-gateway
- Docs: https://portkey.ai/docs
- Maturity: active

---
