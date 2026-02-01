# Scraping

> Generated from README.md on 2026-01-29
## Index
- [ds-top-traders](#ds-top-traders)
- [gmgn-scraper](#gmgn-scraper)
- [gmgn-scripts](#gmgn-scripts)
- [gmgn_smart](#gmgn-smart)
- [gmgn-api](#gmgn-api)
- [firecrawl](#firecrawl)
- [MediaCrawler](#mediacrawler)
- [Threads-Scraper](#threads-scraper)
- [Telegram_Scraper (Amirwpi)](#telegram-scraper-amirwpi)
- [scrapliz (azurespheredev)](#scrapliz-azurespheredev)
- [telegram-scraper](#telegram-scraper)
- [osinti4l-the-kitchen-sink](#osinti4l-the-kitchen-sink)
- [webscraper-ts (vignesh-chaturvedi)](#webscraper-ts-vignesh-chaturvedi)

---

## ds-top-traders

**TL;DR:** The cloudflare bypass code currently doesn't work, but still can use the rest of the code.

### Быстрый выбор
- ✅ Используй если:
  - Dexscreener top traders
- ❌ Не используй если:
  - Real-time data
  - Нужны входные данные/доступы: CA

### 🚀 Запуск
```bash
python main.py
```

### 🧩 Архитектура
- **Category:** Scraping
- **Stack:** Python, Solana
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Dexscreener top traders

### ⚠️ Ограничения
- Real-time data
- Нужны данные/доступы: CA

### 🧭 Fit / Maturity / Ops
- **Fit:** Dexscreener top traders
- **Maturity:** experimental
- **Latency/Cost:** fast
- **Data constraints:** CA
- **Ops friction:** medium

### Full links
- Repo: https://github.com/amibars/ds-top-traders
- Original README: https://github.com/ganarkf/ds-top-traders/blob/main/README.md

---



## gmgn-scraper

**TL;DR:** get data from gmgn.ai

### Быстрый выбор
- ✅ Используй если:
  - GMGN.ai data extraction
  - Node.js >= v18.20.3
- ❌ Не используй если:
  - Real-time trading
  - Нужны входные данные/доступы: —

### 🚀 Запуск
```bash
# См. документацию: https://github.com/amibars/gmgn-scraper/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** Scraping
- **Stack:** Node.js
- **Entrypoints:** См. README

### 🧪 Примеры задач
- GMGN.ai data extraction
- Node.js >= v18.20.3

### ⚠️ Ограничения
- Real-time trading
- Нужны данные/доступы: —

### 🧭 Fit / Maturity / Ops
- **Fit:** GMGN.ai data extraction
- **Maturity:** experimental
- **Latency/Cost:** fast
- **Data constraints:** —
- **Ops friction:** medium

### Full links
- Repo: https://github.com/amibars/gmgn-scraper
- Original README: https://github.com/amibars/gmgn-scraper/blob/main/README.md

---



## gmgn-scripts

**TL;DR:** Форк без README и без скриптов в корне: в репо только LICENSE и папка `stats/`. По факту — заглушка/архив.

### Быстрый выбор
- ✅ Используй если:
  - GMGN scripts (repo пустой)
- ❌ Не используй если:
  - Готовые скрипты
  - Нужны входные данные/доступы: —

### 🚀 Запуск
```bash
# См. документацию: — (отсутствует)
```

### 🧩 Архитектура
- **Category:** Scraping
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- GMGN scripts (repo пустой)

### ⚠️ Ограничения
- Готовые скрипты
- Нужны данные/доступы: —

### 🧭 Fit / Maturity / Ops
- **Fit:** GMGN scripts (repo пустой)
- **Maturity:** empty
- **Latency/Cost:** —
- **Data constraints:** —
- **Ops friction:** medium

### Full links
- Repo: https://github.com/amibars/gmgn-scripts
- Original README: — (отсутствует)

---



## gmgn_smart

**TL;DR:** Дизайн‑док по анализу “smart money” адресов в GMGN: rule‑based фильтры, скоринг, детект быстрых buy→sell (≤60 сек), кеширование market cap и trades.

### Быстрый выбор
- ✅ Используй если:
  - Smart‑money rules & scoring doc
  - 数据获取层：dao_gmgn.py
  - 存储层：service_gmgn_storage.py
- ❌ Не используй если:
  - Turnkey tool
  - Нужны входные данные/доступы: GMGN data, MySQL

### 🚀 Запуск
```bash
# См. документацию: https://github.com/zhaoqie/gmgn_smart/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** Scraping
- **Stack:** Python
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Smart‑money rules & scoring doc
- 数据获取层：dao_gmgn.py
- 存储层：service_gmgn_storage.py
- 服务层：service_gmgn.py

### ⚠️ Ограничения
- Turnkey tool
- Нужны данные/доступы: GMGN data, MySQL

### 🧭 Fit / Maturity / Ops
- **Fit:** Smart‑money rules & scoring doc
- **Maturity:** design‑doc
- **Latency/Cost:** medium
- **Data constraints:** GMGN data, MySQL
- **Ops friction:** medium

### Full links
- Repo: https://github.com/amibars/gmgn_smart
- Original README: https://github.com/zhaoqie/gmgn_smart/blob/main/README.md

---



## gmgn-api

**TL;DR:** Заготовка Python‑пакета `gmgn_api`. В README только заголовок, в коде есть лишь `hello()` — реальной реализации API нет.

### Быстрый выбор
- ✅ Используй если:
  - gmgn_api skeleton
- ❌ Не используй если:
  - Рабочий API
  - Нужны входные данные/доступы: —

### 🚀 Запуск
```bash
# См. документацию: https://github.com/ackness/gmgn-api/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** Scraping
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- gmgn_api skeleton

### ⚠️ Ограничения
- Рабочий API
- Нужны данные/доступы: —

### 🧭 Fit / Maturity / Ops
- **Fit:** gmgn_api skeleton
- **Maturity:** skeleton
- **Latency/Cost:** —
- **Data constraints:** —
- **Ops friction:** medium

### Full links
- Repo: https://github.com/amibars/gmgn-api
- Original README: https://github.com/ackness/gmgn-api/blob/main/README.md

---



## firecrawl

**TL;DR:** Web Data API for AI — превращает любой сайт в LLM-ready markdown или structured data. JavaScript rendering, anti-bot bypass, clean extraction. Self-hosted или cloud API. Идеален для RAG pipelines и AI agents. 77k stars.

### Быстрый выбор
- ✅ Используй если:
  - Web-to-markdown for LLMs
  - Scrape: scrapes a URL and gets its content in LLM-ready format (markdown, structured data via LLM Extract, screenshot, html)
  - Crawl: scrapes all the URLs of a web page and returns content in LLM-ready format
- ❌ Не используй если:
  - Simple HTML
  - Нужны входные данные/доступы: API key

### 🚀 Запуск
```bash
pip install firecrawl-py
```

### 🧩 Архитектура
- **Category:** Scraping
- **Stack:** Python, Rust, Go
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Web-to-markdown for LLMs
- Scrape: scrapes a URL and gets its content in LLM-ready format (markdown, structured data via LLM Extract, screenshot, html)
- Crawl: scrapes all the URLs of a web page and returns content in LLM-ready format
- Map: input a website and get all the website urls - extremely fast

### ⚠️ Ограничения
- Simple HTML
- Нужны данные/доступы: API key

### 🧭 Fit / Maturity / Ops
- **Fit:** Web-to-markdown for LLMs
- **Maturity:** active
- **Latency/Cost:** balanced
- **Data constraints:** API key
- **Ops friction:** low

### Full links
- Repo: https://github.com/firecrawl/firecrawl
- Original README: https://github.com/firecrawl/firecrawl/blob/main/README.md
- Docs: https://docs.firecrawl.dev
- Cloud: https://firecrawl.dev
- Stars: 77,517
- Maturity: active

---



## MediaCrawler

**TL;DR:** Powerful crawler for multiple Chinese social media platforms. Supports scraping data (videos, comments, posts) from Xiaohongshu, Douyin, Kuaishou, Bilibili, Weibo, and Zhihu. Uses Playwright and stealth techniques to bypass common anti-scraping measures. 43k stars.

### Быстрый выбор
- ✅ Используй если:
  - 小红书/抖音/微博 crawler
  - 核心技术：基于 Playwright 浏览器自动化框架登录保存登录态
  - 无需JS逆向：利用保留登录态的浏览器上下文环境，通过 JS 表达式获取签名参数
- ❌ Не используй если:
  - Non-Chinese
  - Нужны входные данные/доступы: —

### 🚀 Запуск
```bash
# См. документацию: https://github.com/NanmiCoder/MediaCrawler/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** Scraping
- **Stack:** Python, Node.js, Go
- **Entrypoints:** См. README

### 🧪 Примеры задач
- 小红书/抖音/微博 crawler
- 核心技术：基于 Playwright 浏览器自动化框架登录保存登录态
- 无需JS逆向：利用保留登录态的浏览器上下文环境，通过 JS 表达式获取签名参数
- 优势特点：无需逆向复杂的加密算法，大幅降低技术门槛

### ⚠️ Ограничения
- Non-Chinese
- Нужны данные/доступы: —

### 🧭 Fit / Maturity / Ops
- **Fit:** 小红书/抖音/微博 crawler
- **Maturity:** active
- **Latency/Cost:** fast
- **Data constraints:** —
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/NanmiCoder/MediaCrawler
- Original README: https://github.com/NanmiCoder/MediaCrawler/blob/main/README.md
- Stars: ~43,257
- Maturity: active

---



## Threads-Scraper

**TL;DR:** Python scraper для Meta Threads. Автоматизирует извлечение постов, профилей, комментариев с публичных страниц Threads. Использует client-side rendering ожидание для SPA. Локальный scraper без API — работает напрямую с веб-интерфейсом. Альтернатива Apify Threads pipelines.

### Быстрый выбор
- ✅ Используй если:
  - Threads.net data extraction
- ❌ Не используй если:
  - Non-Threads
  - Нужны входные данные/доступы: —

### 🚀 Запуск
```bash
# См. документацию: https://github.com/Zeeshanahmad4/Threads-Scraper
```

### 🧩 Архитектура
- **Category:** Scraping
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- Threads.net data extraction

### ⚠️ Ограничения
- Non-Threads
- Нужны данные/доступы: —

### 🧭 Fit / Maturity / Ops
- **Fit:** Threads.net data extraction
- **Maturity:** active
- **Latency/Cost:** fast
- **Data constraints:** —
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/Zeeshanahmad4/Threads-Scraper
- Stars: 80
- Maturity: active

---



## Telegram_Scraper (Amirwpi)

**TL;DR:** Python scraper для Telegram groups. Извлечение members, messages, media из групп через Telegram API. Telethon library based. Экспорт в JSON/CSV. Для research и data collection из публичных Telegram групп.

### Быстрый выбор
- ✅ Используй если:
  - A script that uses the Telegram API to scrape data from any group using your Telegram account, enabling efficient extraction of messages, user details, and more for data analysis purposes.
- ❌ Не используй если:
  - Other stacks / needs review
  - Нужны входные данные/доступы: data

### 🚀 Запуск
```bash
# См. документацию: https://github.com/Amirwpi/Telegram_Scraper
```

### 🧩 Архитектура
- **Category:** Scraping
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- A script that uses the Telegram API to scrape data from any group using your Telegram account, enabling efficient extraction of messages, user details, and more for data analysis purposes.

### ⚠️ Ограничения
- Other stacks / needs review
- Нужны данные/доступы: data

### 🧭 Fit / Maturity / Ops
- **Fit:** A script that uses the Telegram API to scrape data from any group using your Telegram account, enabling efficient extraction of messages, user details, and more for data analysis purposes.
- **Maturity:** stale
- **Latency/Cost:** fast
- **Data constraints:** data
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/Amirwpi/Telegram_Scraper
- Stars: 9
- Maturity: active

---



## scrapliz (azurespheredev)

**TL;DR:** Scraping: A little web scraping chrome extension.

### Быстрый выбор
- ✅ Используй если:
  - A little web scraping chrome extension
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/azurespheredev/scrapliz/blob/master/README.md
```

### 🧩 Архитектура
- **Category:** Scraping
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- A little web scraping chrome extension

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** A little web scraping chrome extension
- **Maturity:** stale
- **Latency/Cost:** fast
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/azurespheredev/scrapliz
- Original README: https://github.com/azurespheredev/scrapliz/blob/master/README.md

---



## telegram-scraper

**TL;DR:** A simple Telegram channel scraper

### Быстрый выбор
- ✅ Используй если:
  - A simple Telegram channel scraper
  - ✅ 0 Dependencies
  - ✅ No Authentication
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/dexbotsdev/telegram-scraper/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** Scraping
- **Stack:** JavaScript
- **Entrypoints:** См. README

### 🧪 Примеры задач
- A simple Telegram channel scraper
- ✅ 0 Dependencies
- ✅ No Authentication
- ✅ JSON Output

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** A simple Telegram channel scraper
- **Maturity:** stale
- **Latency/Cost:** fast
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/dexbotsdev/telegram-scraper
- Original README: https://github.com/dexbotsdev/telegram-scraper/blob/main/README.md

---



## osinti4l-the-kitchen-sink

**TL;DR:** Here you will find toolkits, learning, and practice resources for Open-Source Intelligence investigations. These resources have been gathered from all corners of the internet.

### Быстрый выбор
- ✅ Используй если:
  - osinti4l-the-kitchen-sink
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/Ferchoweb/OSINTI4L-The-Kitchen-Sink/blob/main/README.md
```

### 🧩 Архитектура
- **Category:** Scraping
- **Stack:** См. README
- **Entrypoints:** См. README

### 🧪 Примеры задач
- osinti4l-the-kitchen-sink

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** osinti4l-the-kitchen-sink
- **Maturity:** stale
- **Latency/Cost:** balanced
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/Ferchoweb/OSINTI4L-The-Kitchen-Sink
- Original README: https://github.com/Ferchoweb/OSINTI4L-The-Kitchen-Sink/blob/main/README.md

---



## webscraper-ts (vignesh-chaturvedi)

**TL;DR:** This TypeScript-based web scraper uses Puppeteer to extract unique links starting with https://x.com/ from a given webpage. The results are stored in a JSON file.

### Быстрый выбор
- ✅ Используй если:
  - webscraper-ts (vignesh-chaturvedi)
  - Extracts all links from a webpage.
  - Filters links to include only those starting with https://x.com/.
- ❌ Не используй если:
  - Other stacks / needs review

### 🚀 Запуск
```bash
# См. документацию: https://github.com/vignesh-chaturvedi/webscraper-ts/blob/master/README.md
```

### 🧩 Архитектура
- **Category:** Scraping
- **Stack:** TypeScript, JavaScript, Node.js
- **Entrypoints:** См. README

### 🧪 Примеры задач
- webscraper-ts (vignesh-chaturvedi)
- Extracts all links from a webpage.
- Filters links to include only those starting with https://x.com/.
- Removes duplicate links.

### ⚠️ Ограничения
- Other stacks / needs review

### 🧭 Fit / Maturity / Ops
- **Fit:** webscraper-ts (vignesh-chaturvedi)
- **Maturity:** stale
- **Latency/Cost:** fast
- **Data constraints:** ?
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/vignesh-chaturvedi/webscraper-ts
- Original README: https://github.com/vignesh-chaturvedi/webscraper-ts/blob/master/README.md

---
