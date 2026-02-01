# Trading

> Generated from README.md on 2026-01-29
## Index
- [alris](#alris)
- [woody](#woody)
- [Thin-Floor-Strategy](#thin-floor-strategy)
- [MEMETOOL-V0.3](#memetool-v0-3)
- [Growtradebot](#growtradebot)
- [Pump-Fun-API](#pump-fun-api)
- [QuantMuse](#quantmuse)
- [solana-trader-proto](#solana-trader-proto)

---

## alris

**TL;DR:** Alris is an AI-powered platform designed to dynamically optimize yield and automate trading strategies on the Solana blockchain.

### Быстрый выбор
- ✅ Используй если:
  - AI yield optimizer
  - Fetches real-time data from CoinGecko and Orca API.
  - Leverages Solana Agent Kit for transaction execution and updates.
- ❌ Не используй если:
  - Manual trading
  - Нужны входные данные/доступы: wallet

### 🚀 Запуск
```bash
npm run dev
```

### 🧩 Архитектура
- **Category:** Trading
- **Stack:** Node.js, Next.js, Solana
- **Entrypoints:** См. README

### 🧪 Примеры задач
- AI yield optimizer
- Fetches real-time data from CoinGecko and Orca API.
- Leverages Solana Agent Kit for transaction execution and updates.
- Process market data through GPTv4 to determine optimal trading and yield strategies.

### ⚠️ Ограничения
- Manual trading
- Нужны данные/доступы: wallet

### 🧭 Fit / Maturity / Ops
- **Fit:** AI yield optimizer
- **Maturity:** experimental
- **Latency/Cost:** balanced
- **Data constraints:** wallet
- **Ops friction:** medium

### Full links
- Repo: https://github.com/maushish/alris
- Original README: https://github.com/maushish/alris/blob/main/README.md

---



## woody

**TL;DR:** Woody — AI‑assisted on‑chain trading framework. Поддержка множества LLM (OpenAI, Anthropic, Grok, Llama и др.), коннекторы Telegram/Twitter, расширяемые action‑модули и стратегии. Node.js 23+ и pnpm; на Windows нужен WSL2.

### Быстрый выбор
- ✅ Используй если:
  - AI copy trading
  - 🤖 AI-assisted trade with on-chain
  - 🔗 Supports many models (Llama, Grok, OpenAI, Anthropic, etc.)
- ❌ Не используй если:
  - Manual strategies
  - Нужны входные данные/доступы: wallet

### 🚀 Запуск
```bash
# См. документацию: https://github.com/softrug/woody/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** Trading
- **Stack:** Node.js
- **Entrypoints:** См. README

### 🧪 Примеры задач
- AI copy trading
- 🤖 AI-assisted trade with on-chain
- 🔗 Supports many models (Llama, Grok, OpenAI, Anthropic, etc.)
- 🛠️ Full-featured Telegram, Twitter and reset api connectors

### ⚠️ Ограничения
- Manual strategies
- Нужны данные/доступы: wallet

### 🧭 Fit / Maturity / Ops
- **Fit:** AI copy trading
- **Maturity:** experimental
- **Latency/Cost:** balanced
- **Data constraints:** wallet
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/softrug/woody
- Original README: https://github.com/softrug/woody/blob/main/README.md

---



## Thin-Floor-Strategy

**TL;DR:** Концепт автоматизированной NFT‑стратегии для Magic Eden. Ищет коллекции с “thin floor” (мало listings на floor) и высоким спросом, затем автоматизирует buy/flip через Solana.

### Быстрый выбор
- ✅ Используй если:
  - Magic Eden NFT trading
  - Focus on High-Value Opportunities: Identify thin floors to maximize profitability.
  - Save Time: Automate complex analysis and trading workflows.
- ❌ Не используй если:
  - Fungible tokens
  - Нужны входные данные/доступы: wallet

### 🚀 Запуск
```bash
# См. документацию: https://github.com/amibars/Thin-Floor-Strategy/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** Trading
- **Stack:** Solana
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Magic Eden NFT trading
- Focus on High-Value Opportunities: Identify thin floors to maximize profitability.
- Save Time: Automate complex analysis and trading workflows.
- Stay Ahead: Act on real-time data with blazing speed and accuracy.

### ⚠️ Ограничения
- Fungible tokens
- Нужны данные/доступы: wallet

### 🧭 Fit / Maturity / Ops
- **Fit:** Magic Eden NFT trading
- **Maturity:** experimental
- **Latency/Cost:** fast
- **Data constraints:** wallet
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/amibars/Thin-Floor-Strategy
- Original README: https://github.com/amibars/Thin-Floor-Strategy/blob/main/README.md

---



## MEMETOOL-V0.3

**TL;DR:** Next.js‑платформа для мониторинга и анализа мемкоинов в Solana: цены, social sentiment, bundle checker через Telegram‑бота, портфель, торговые сигналы, комьюнити‑фичи.

### Быстрый выбор
- ✅ Используй если:
  - Solana memecoin analytics dashboard
  - Real-time memecoin price tracking
  - Social sentiment analysis
- ❌ Не используй если:
  - Нет TG token
  - Нужны входные данные/доступы: TG token

### 🚀 Запуск
```bash
npm run dev
```

### 🧩 Архитектура
- **Category:** Trading
- **Stack:** TypeScript, Node.js, React, Next.js, Solana
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Solana memecoin analytics dashboard
- Real-time memecoin price tracking
- Social sentiment analysis
- Bundle checker integration with @TrenchScannerBot

### ⚠️ Ограничения
- Нет TG token
- Нужны данные/доступы: TG token

### 🧭 Fit / Maturity / Ops
- **Fit:** Solana memecoin analytics dashboard
- **Maturity:** early
- **Latency/Cost:** fast
- **Data constraints:** TG token
- **Ops friction:** medium

### Full links
- Repo: https://github.com/amibars/MEMETOOL-V0.3
- Original README: https://github.com/ulifrom843/MEMETOOL-V0.3/blob/main/README.md

---



## Growtradebot

**TL;DR:** Telegram Solana trading bot. Buy/sell SPL tokens через Telegram commands. Jito bundles для fast execution, Raydium SDK интеграция, Jupiter API для swaps, Pump.fun support. TypeScript кодовая база.

### Быстрый выбор
- ✅ Используй если:
  - Telegram Solana bot
- ❌ Не используй если:
  - Non-Telegram
  - Нужны входные данные/доступы: wallet, TG bot

### 🚀 Запуск
```bash
# См. документацию: https://github.com/amibars/Growtradebot
```

### 🧩 Архитектура
- **Category:** Trading
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Telegram Solana bot

### ⚠️ Ограничения
- Non-Telegram
- Нужны данные/доступы: wallet, TG bot

### 🧭 Fit / Maturity / Ops
- **Fit:** Telegram Solana bot
- **Maturity:** experimental
- **Latency/Cost:** fast
- **Data constraints:** wallet, TG bot
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/amibars/Growtradebot
- Maturity: experimental

---



## Pump-Fun-API

**TL;DR:** Trade on Pump.fun programmatically. API для программного трейдинга.

### Быстрый выбор
- ✅ Используй если:
  - Pump.fun programmatic trading
- ❌ Не используй если:
  - Analytics only
  - Нужны входные данные/доступы: wallet

### 🚀 Запуск
```bash
# См. документацию: https://github.com/amibars/Pump-Fun-API
```

### 🧩 Архитектура
- **Category:** Trading
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Pump.fun programmatic trading

### ⚠️ Ограничения
- Analytics only
- Нужны данные/доступы: wallet

### 🧭 Fit / Maturity / Ops
- **Fit:** Pump.fun programmatic trading
- **Maturity:** unknown
- **Latency/Cost:** fast
- **Data constraints:** wallet
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/amibars/Pump-Fun-API
- Maturity: unknown

---



## QuantMuse

**TL;DR:** Comprehensive quantitative trading systems with AI-powered analysis. Open-source framework for backtesting, strategy development, and deploying trading bots using modern AI/ML techniques. 2k stars.

### Быстрый выбор
- ✅ Используй если:
  - AI-powered quant trading
  - Overview
  - Features
- ❌ Не используй если:
  - Manual trading
  - Нужны входные данные/доступы: —

### 🚀 Запуск
```bash
# См. документацию: https://github.com/0xemmkty/QuantMuse/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** Trading
- **Stack:** Python, C++, PostgreSQL, Redis, FastAPI
- **Entrypoints:** См. README

### 🧪 Примеры задач
- AI-powered quant trading
- Overview
- Features
- Architecture

### ⚠️ Ограничения
- Manual trading
- Нужны данные/доступы: —

### 🧭 Fit / Maturity / Ops
- **Fit:** AI-powered quant trading
- **Maturity:** active
- **Latency/Cost:** balanced
- **Data constraints:** —
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/0xemmkty/QuantMuse
- Original README: https://github.com/0xemmkty/QuantMuse/blob/main/README.md
- Stars: 1,562
- Maturity: active

---



## solana-trader-proto

**TL;DR:** Protobuf definitions для bloXroute Solana Trader API. gRPC schema для high-frequency trading на Solana через bloXroute infrastructure. Типы для orders, quotes, streams. Используй для генерации клиентов на любом языке. Official от bloXroute Labs.

### Быстрый выбор
- ✅ Используй если:
  - bloXroute Solana trader proto
- ❌ Не используй если:
  - Non-Solana
  - Нужны входные данные/доступы: —

### 🚀 Запуск
```bash
# См. документацию: https://github.com/bloXroute-Labs/solana-trader-proto
```

### 🧩 Архитектура
- **Category:** Trading
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- bloXroute Solana trader proto

### ⚠️ Ограничения
- Non-Solana
- Нужны данные/доступы: —

### 🧭 Fit / Maturity / Ops
- **Fit:** bloXroute Solana trader proto
- **Maturity:** active
- **Latency/Cost:** fast
- **Data constraints:** —
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/bloXroute-Labs/solana-trader-proto
- Stars: 45
- Maturity: active

---
