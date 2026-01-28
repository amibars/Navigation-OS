# 📚 GitHub Repository Catalog — amibars

> Единый справочник для ИИ-агентов: выбирай правильный репозиторий под задачу.
> **272 репозитория**: AI agents, LLM frameworks, Solana/blockchain tools, trading bots, MCP servers, scrapers, DevTools, UI templates.
> 47 forked + 225 starred repos. **Catalog Table: 272 indexed entries**.

---

## 🚀 Quick Router

### AI Agents & Frameworks
| Задача | Репозитории |
|--------|-------------|
| Общий AI агент с памятью и инструментами | [agent-zero](#agent-zero), [openagent](#openagent), [AGiXT](#agixt) |
| AI агент для Twitter/X | [ZerePy](#zerepy), [OpenTruthV1](#opentruthv1), [postiz-app](#postiz-app) |
| Unruggable AI с верификацией | [sentience](#sentience) |
| Multi-agent orchestration | [MetaGPT](#metagpt), [autogen](#autogen-microsoft), [crewAI](#crewai), [langgraph](#langgraph), [gensx](#gensx) |
| No-code agent builder | [AgentGPT](#agentgpt), [dify](#dify) |

### LLM Platforms & Interfaces
| Задача | Репозитории |
|--------|-------------|
| Self-hosted LLM UI | [open-webui](#open-webui), [big-AGI](#big-agi), [ezlocalai](#ezlocalai) |
| Visual LLM workflow builder | [dify](#dify), [FastGPT](#fastgpt), [pyspur](#pyspur) |
| Agentic workflow automation | [activepieces](#activepieces), [huginn](#huginn) |
| API Wrappers | [pplx2api](#pplx2api), [grok3-api](#grok3-api) |

### MCP Ecosystem
| Задача | Репозитории |
|--------|-------------|
| MCP SDK | [modelcontextprotocol/python-sdk](#modelcontextprotocolpython-sdk), [nanobot](#nanobot) |
| MCP servers | [chrome-devtools-mcp](#chrome-devtools-mcp), [firecrawl-mcp-server](#firecrawl-mcp-server), [mcp-server-gemini](#mcp-server-gemini), [deep-research-mcp-server](#deep-research-mcp-server) |
| MCP UI | [mcp-ui](#mcp-ui) |

### Blockchain/Solana Tools
| Задача | Репозитории |
|--------|-------------|
| AI взаимодействие с Solana | [solana-agent-kit](#solana-agent-kit), [agentipy](#agentipy), [listen](#listen) |
| AI взаимодействие с EVM/multi-chain | [goat](#goat), [cdp-agentkit-nodejs](#cdp-agentkit-nodejs) |
| Торговый бот Solana | [axium](#axium), [Growtradebot](#growtradebot), [alris](#alris), [woody](#woody), [Trading-API](#trading-api) |
| MEV/Arbitrage | [jito-labs/mev-bot](#jito-labsmev-bot), [AttackMachine](#attackmachine) |
| Infrastructure | [geyser-grpc-plugin](#geyser-grpc-plugin-jito) |

### Browser Automation & Dev Tools
| Задача | Репозитории |
|--------|-------------|
| AI агент в браузере | [browser-use](#browser-use), [web-ui](#web-ui), [stagehand](#stagehand-browserbase), [gemini-browser](#gemini-browser-browserbase) |
| AI coding assistant | [bolt.diy](#boltdiy), [devin.cursorrules](#devincursorrules), [gemini-cli](#gemini-cli), [goose](#goose-block) |
| Web scraping for AI | [firecrawl](#firecrawl), [MediaCrawler](#mediacrawler) |
| Desktop Automation | [vision-agent](#vision-agent-askui) |

### OSINT & Security
| Задача | Репозитории |
|--------|-------------|
| Username/social OSINT | [sherlock](#sherlock), [Photon](#photon), [TorBot](#torbot) |
| Telegram OSINT | [Telegram-OSINT](#telegram-osint), [Telegram_Scraper](#telegram_scraper-amirwpi) |
| Curated OSINT lists | [Awesome-OSINT-For-Everything](#awesome-osint-for-everything), [CyberSources](#cybersources) |

### Data Scraping & Analytics
| Задача | Репозитории |
|--------|-------------|
| Скрейпинг GMGN | [gmgn-scraper](#gmgn-scraper), [gmgn-api](#gmgn-api), [gmgn_parser](#gmgn_parser), [gmgn-scripts](#gmgn-scripts) |
| Анализ кошельков | [solana-wallet-checker](#solana-wallet-checker), [ds-top-traders](#ds-top-traders), [Smart_Money_Follower](#smart_money_follower) |
| Pump.fun аналитика | [pump-meta](#pump-meta), [pumpfun-king-of-the-hill](#pumpfun-king-of-the-hill) |

### Educational & Curated Lists
| Задача | Репозитории |
|--------|-------------|
| AI Agents learning | [ai-agents-for-beginners](#ai-agents-for-beginners-microsoft), [agents-course](#agents-course-huggingface), [AI-Crash-Course](#ai-crash-course) |
| LLM resources | [awesome-llm-apps](#awesome-llm-apps), [free-llm-api-resources](#free-llm-api-resources), [system-prompts](#system-prompts-and-models-of-ai-tools) |
| AI agents lists | [awesome-ai-agents](#e2b-devawesome-ai-agents), [awesome-claude-skills](#awesome-claude-skills) |


---

## 📋 Catalog Table

| # | Repo | Category | Best for | Not for | Quickstart | Maturity | Latency/Cost | Inputs |
|---|------|----------|----------|---------|------------|----------|--------------|--------|
| 1 | [deepscaler](#deepscaler) | ML/RL | RL training for LLMs, O1 reproduction | Production inference only | `uv pip install rllm` | active | quality | model, dataset |
| 2 | [bolt.diy](#boltdiy) | DevTools | AI web dev, any LLM | Mobile apps | `docker compose up` | active | balanced | prompts |
| 3 | [web-ui](#web-ui) | Browser | Web UI for browser-use | Headless-only | `python webui.py` | active | balanced | task, LLM key |
| 4 | [listen](#listen) | Solana | DEX trading, monitoring, AI agents | Non-Solana chains | `docker compose up` | active | fast | wallet, RPC |
| 5 | [goat](#goat) | Blockchain | Multi-chain AI agents, 200+ tools | Simple scripts | `npm i @goat-sdk/core` | active | balanced | wallet, API keys |
| 6 | [axium](#axium) | Trading | Pumpfun/Raydium trading | DeFi beyond trading | `docker compose up` | experimental | fast | wallet |
| 7 | [openagent](#openagent) | AI | Multi-agent battles on Solana | Non-Solana | `npm install` | experimental | balanced | wallet |
| 8 | [sentience](#sentience) | AI | Unruggable verified AI agents | Quick prototypes | `pip install galadriel` | active | balanced | TEE setup |
| 9 | [pyspur](#pyspur) | ML | Visual LLM workflow editor | CLI-only workflows | `docker compose up` | active | balanced | API keys |
| 10 | [exo](#exo) | Infra | Distributed AI inference across devices | Single GPU | `pip install exo` | active | quality | devices |
| 11 | [swarmnode-python](#swarmnode-python) | Infra | Serverless AI agents | Self-hosted only | `pip install swarmnode` | active | balanced | API key |
| 12 | [solana-agent-kit](#solana-agent-kit) | Blockchain | 60+ Solana actions for AI | EVM-only | `npm i solana-agent-kit` | active | fast | wallet, OpenAI |
| 13 | [agentipy](#agentipy) | Blockchain | Python Solana AI agents | TypeScript projects | `pip install agentipy` | active | fast | wallet |
| 14 | [ZerePy](#zerepy) | AI | Twitter/X AI agents | Non-social agents | `poetry install` | active | balanced | X API, LLM |
| 15 | [browser-use](#browser-use) | Browser | Web automation for AI agents | API-only tasks | `uv add browser-use` | active | balanced | LLM key |
| 16 | [devin.cursorrules](#devincursorrules) | DevTools | Make Cursor like Devin | Non-IDE workflows | copy files | active | fast | — |
| 17 | [alris](#alris) | Trading | AI yield optimizer | Manual trading | `npm run dev` | experimental | balanced | wallet |
| 18 | [pumpfun-king-of-the-hill](#pumpfun-king-of-the-hill) | Analytics | Pump.fun token visualization | Trading execution | `npm run dev` | experimental | fast | API |
| 19 | [agent-zero](#agent-zero) | AI | Personal AI assistant with memory | Stateless agents | `docker pull agent0ai/agent-zero` | active | balanced | LLM key |
| 20 | [ds-top-traders](#ds-top-traders) | Scraping | Dexscreener top traders | Real-time data | `python main.py` | experimental | fast | CA |
| 21 | [cdp-agentkit-nodejs](#cdp-agentkit-nodejs) | Blockchain | Coinbase onchain AI agents | Non-Base chains | `npm install` | active | balanced | CDP key |
| 22 | [rig](#rig) | ML | Rust LLM applications | Python projects | `cargo add rig-core` | active | fast | — |
| 23 | [solana-wallet-checker](#solana-wallet-checker) | Analytics | Mass wallet scanning | Single wallets | `python main.py` | experimental | fast | wallet list |
| 24 | [gmgn-scraper](#gmgn-scraper) | Scraping | GMGN.ai data extraction | Real-time trading | `node index.js` | experimental | fast | — |
| 25 | [woody-hub](#woody-hub) | Extension | GMGN browser enhancement | CLI tools | `pnpm dev` | experimental | fast | — |
| 26 | [woody](#woody) | Trading | AI copy trading | Manual strategies | TODO | experimental | balanced | wallet |
| 27 | [Thin-Floor-Strategy](#thin-floor-strategy) | Trading | Magic Eden NFT trading | Fungible tokens | TODO | experimental | fast | wallet |
| 28 | [OpenTruthV1](#opentruthv1) | AI | Terminal of Truths clone | Production bots | TODO | experimental | balanced | LLM key |
| 29 | [pump-meta](#pump-meta) | Analytics | Pump.fun sentiment analysis | Trade execution | `python main.py` | experimental | balanced | — |
| 30 | [gmgn-scripts](#gmgn-scripts) | Scraping | GMGN utility scripts | Full API | TODO | experimental | fast | — |
| 31 | [gmgn_smart](#gmgn_smart) | Scraping | GMGN smart wallet tools | unknown | TODO | unknown | fast | — |
| 32 | [gmgn-api](#gmgn-api) | Scraping | GMGN API wrapper | Full scraping | TODO | unknown | fast | — |
| 33 | [gmgn_parser](#gmgn_parser) | Scraping | GMGN data parsing | API calls | TODO | unknown | fast | — |
| 34 | [portkey-gateway](#portkey-gateway) | Infra | AI Gateway, 200+ LLMs, guardrails | Simple LLM calls | `npm install` | active | fast | API keys |
| 35 | [MEMETOOL-V0.3](#memetool-v03) | Trading | Meme coin tools | Non-meme tokens | TODO | unknown | fast | — |
| 36 | [poe-api-wrapper](#poe-api-wrapper) | DevTools | Free GPT-4/Claude via Poe.com | Direct API access | `pip install poe-api-wrapper` | active | balanced | Poe account |
| 37 | [solana-pnl-card-bot](#solana-pnl-card-bot) | Analytics | PnL card generation | Trading | TODO | unknown | fast | token |
| 38 | [Growtradebot](#growtradebot) | Trading | Telegram Solana bot | Non-Telegram | TODO | experimental | fast | wallet, TG bot |
| 39 | [ct_alpha](#ct_alpha) | Analytics | CT profitability calculator | Trading execution | TODO | unknown | balanced | tweets |
| 40 | [Smart_Money_Follower](#smart_money_follower) | Analytics | Top Solana wallet analysis | Trading | TODO | experimental | balanced | GMGN API |
| 41 | [gmgn_analyst](#gmgn_analyst) | Analytics | Pump.Fun token analysis | Trading | TODO | experimental | balanced | GMGN API |
| 42 | [Pump-Fun-API](#pump-fun-api) | Trading | Pump.fun programmatic trading | Analytics only | TODO | unknown | fast | wallet |
| 43 | [telegram_bot](#telegram_bot) | Bot | Telegram bot template | Non-Telegram | TODO | unknown | fast | TG token |
| 44 | [consistencydecoder](#consistencydecoder) | ML | OpenAI Consistency VAE | Non-image tasks | TODO | unknown | quality | images |
| 45 | [chatgpt-ai-template](#chatgpt-ai-template) | DevTools | ChatGPT UI template (React/Next.js) | Backend-only | `npm run dev` | unknown | fast | — |
| 46 | [vision-ui-dashboard-react](#vision-ui-dashboard-react) | DevTools | React dashboard template | Non-React | `npm run dev` | unknown | fast | — |
| 47 | [QAMI](#qami) | Other | Quantum Assembly Machine Infinity | Standard computing | TODO | experimental | unknown | prompts |
| 48 | [dify](#dify) | LLM Platform | Visual LLM workflow builder, RAG | CLI-only | `docker compose up` | active | balanced | API keys |
| 49 | [open-webui](#open-webui) | LLM UI | Self-hosted ChatGPT-like UI | API-only | `docker run -p 3000:8080 ghcr.io/open-webui/open-webui:main` | active | balanced | Ollama/API |
| 50 | [godot](#godot) | Game Engine | 2D/3D game development | AAA games | download | active | — | — |
| 51 | [gemini-cli](#gemini-cli) | AI CLI | Gemini in terminal | GUI preference | `npx @google/gemini-cli` | active | fast | API key |
| 52 | [awesome-llm-apps](#awesome-llm-apps) | Curated | LLM app examples, RAG patterns | Production code | reference | curated | — | — |
| 53 | [firecrawl](#firecrawl) | Scraping | Web-to-markdown for LLMs | Simple HTML | `pip install firecrawl-py` | active | balanced | API key |
| 54 | [sherlock](#sherlock) | OSINT | Username hunting across platforms | Non-OSINT | `pip install sherlock-project` | active | fast | username |
| 55 | [MetaGPT](#metagpt) | Multi-Agent | Software company simulation | Single agent | `pip install metagpt` | active | quality | prompts |
| 56 | [autogen](#autogen-microsoft) | Multi-Agent | Microsoft multi-agent orchestration | Simple agents | `pip install pyautogen` | active | balanced | API keys |
| 57 | [OpenManus](#openmanus) | AI Agent | Open-source AI agents | Quick prototypes | TODO | active | balanced | — |
| 58 | [ai-agents-for-beginners](#ai-agents-for-beginners-microsoft) | Educational | Learning AI agents (Microsoft) | Production | reference | educational | — | — |
| 59 | [huginn](#huginn) | Automation | Self-hosted IFTTT alternative | Cloud service | `docker run -p 3000:3000 huginn/huginn` | active | balanced | — |
| 60 | [clawdbot](#clawdbot) | AI Assistant | Personal AI on any platform | Enterprise | TODO | active | balanced | — |
| 61 | [crewAI](#crewai) | Multi-Agent | Role-based agent collaboration | Single agent | `pip install crewai` | active | balanced | API keys |
| 62 | [exo-explore/exo](#exo-exploreexo) | Infra | Distributed AI inference | Single GPU | `pip install exo` | active | quality | devices |
| 63 | [twenty](#twenty) | CRM | Open-source Salesforce alternative | Enterprise support | `docker compose up` | active | balanced | — |
| 64 | [AgentGPT](#agentgpt) | No-Code Agent | Browser-based agent builder | Production | visit site | active | balanced | API key |
| 65 | [Clone-Wars](#clone-wars) | Reference | 100+ site clones for learning | Production use | reference | curated | — | — |
| 66 | [goose](#goose-block) | AI Coding | Block's AI coding agent | GUI IDE | install | active | balanced | LLM key |
| 67 | [FastGPT](#fastgpt) | LLM Platform | Knowledge-based RAG platform | Simple chat | `docker compose up` | active | balanced | API keys |
| 68 | [Hitomi-Downloader](#hitomi-downloader) | Downloader | Media download utility | Other | download | active | fast | URL |
| 69 | [composio](#composio) | Integrations | 100+ integrations for AI agents | Simple LLM | `pip install composio` | active | balanced | API keys |
| 70 | [awesome-claude-skills](#awesome-claude-skills) | Curated | Claude Skills resources | Production | reference | curated | — | — |
| 71 | [postiz-app](#postiz-app) | Social | AI social media scheduling | Single platform | `docker compose up` | active | balanced | social APIs |
| 72 | [e2b-dev/awesome-ai-agents](#e2b-devawesome-ai-agents) | Curated | AI agents list | Production | reference | curated | — | — |
| 73 | [agents-course](#agents-course-huggingface) | Educational | HuggingFace agents course | Production | reference | educational | — | — |
| 74 | [UI-TARS-desktop](#ui-tars-desktop-bytedance) | Multimodal | Desktop automation (ByteDance) | Simple chat | install | active | balanced | — |
| 75 | [langgraph](#langgraph) | Workflow | Complex agent workflows as graphs | Simple LLM | `pip install langgraph` | active | balanced | API keys |
| 76 | [radare2](#radare2) | Security | Reverse engineering framework | Non-RE | install | active | balanced | binary |
| 77 | [chrome-devtools-mcp](#chrome-devtools-mcp) | MCP | Chrome DevTools for AI agents | Non-Chrome | MCP config | active | fast | — |
| 78 | [chatterbox](#chatterbox-resemble-ai) | TTS | SoTA open-source text-to-speech | Non-audio | `pip install chatterbox` | active | balanced | text |
| 79 | [A2A](#a2a-agent-to-agent-protocol) | Protocol | Agent-to-agent communication | Single agent | reference | active | — | — |
| 80 | [modelcontextprotocol/python-sdk](#modelcontextprotocolpython-sdk) | MCP SDK | Official MCP Python SDK | Non-MCP | `pip install mcp` | active | fast | — |
| 81 | [stagehand](#stagehand-browserbase) | Browser | AI browser automation | HTTP scraping | `npm install @browserbase/stagehand` | active | balanced | API key |
| 82 | [mastra](#mastra) | TypeScript | AI-powered apps (Gatsby team) | Python | `npm install mastra` | active | balanced | — |
| 83 | [activepieces](#activepieces) | Automation | AI Agents + 400 MCP servers | Simple scripts | `docker compose up` | active | balanced | — |
| 84 | [GenAI_Agents](#genai_agents) | Educational | Generative AI agent tutorials | Production | reference | educational | — | — |
| 85 | [suna](#suna-kortix-ai) | AI Agent | Build and train AI agents | Simple chat | TODO | active | balanced | — |
| 86 | [bolt.diy](#boltdiy-stackblitz) | DevTools | Any-LLM web dev (community) | Mobile apps | `docker compose up` | active | balanced | LLM key |
| 87 | [Qwen3-VL](#qwen3-vl) | Multimodal | Vision-Language model (Alibaba) | Text-only | model download | active | quality | images |
| 88 | [Janus](#janus-deepseek) | Multimodal | Unified understanding+generation | Single modality | model download | active | quality | multi |
| 89 | [eliza](#eliza-elizaos) | AI Agent | Autonomous agents for everyone | Enterprise | TODO | active | balanced | — |
| 90 | [SuperAGI](#superagi) | AI Agent | Dev-first autonomous agents | Simple tasks | `docker compose up` | active | balanced | API keys |
| 91 | [bolt.new](#boltnew-stackblitz) | DevTools | Full-stack web apps from prompts | Complex apps | visit site | active | fast | prompts |
| 92 | [camel-ai/camel](#camel-aicamel) | Multi-Agent | Best multi-agent framework | Single agent | `pip install camel-ai` | active | balanced | API keys |
| 93 | [browser-use/web-ui](#browser-useweb-ui) | Browser | AI agent web interface | Headless | `python webui.py` | active | balanced | LLM key |
| 94 | [AstrBot](#astrbot) | Chatbot | Agentic IM chatbot infra | Simple bots | TODO | active | balanced | — |
| 95 | [csm](#csm-sesameailabs) | Speech | Conversational speech generation | Non-audio | model download | active | balanced | audio |
| 96 | [motia](#motia) | Backend | Multi-language backend, AI agents | Frontend-only | `npm install motia` | active | balanced | — |
| 97 | [agent-zero](#agent-zero) | AI Agent | Personal AI with memory | Stateless | `docker pull agent0ai/agent-zero` | active | balanced | LLM key |
| 98 | [MoneyPrinterV2](#moneyprinterv2) | Automation | Automate online money-making | Manual work | TODO | active | balanced | — |
| 99 | [Photon](#photon) | OSINT | Fast OSINT crawler | Non-OSINT | `pip install photon` | active | fast | URL |
| 100 | [CL4R1T4S](#cl4r1t4s) | Prompts | Leaked system prompts | Original prompts | reference | active | — | — |
| 101 | [system-prompts-and-models-of-ai-tools](#system-prompts-and-models-of-ai-tools) | Prompts | Full system prompts of AI tools | Original prompts | reference | active | — | — |
| 102 | [vercel-labs/agent-browser](#vercel-labsagent-browser) | Browser | Vercel browser automation CLI | GUI | `npx agent-browser` | active | fast | — |
| 103 | [Auto-Claude](#auto-claude) | AI Coding | Autonomous multi-session coding | Simple edits | TODO | active | balanced | — |
| 104 | [3FS](#3fs-deepseek) | Infra | DeepSeek distributed file system | Small scale | TODO | active | quality | storage |
| 105 | [awesome-claude-code-subagents](#awesome-claude-code-subagents) | Curated | 100+ Claude subagents | Production | reference | curated | — | — |
| 106 | [AutoAgent](#autoagent-hkuds) | No-Code | Zero-code LLM agent framework | Custom code | TODO | active | balanced | — |
| 107 | [introtodeeplearning](#introtodeeplearning-mit) | Educational | MIT deep learning course | Production | reference | educational | — | — |
| 108 | [free-llm-api-resources](#free-llm-api-resources) | Curated | Free LLM API list | Paid APIs | reference | curated | — | — |
| 109 | [big-AGI](#big-agi) | LLM UI | AGI suite, multi-model chat | Simple chat | `docker compose up` | active | balanced | API keys |
| 110 | [opencode-antigravity-auth](#opencode-antigravity-auth) | Auth | Opencode OAuth for Antigravity | Other IDEs | TODO | active | fast | — |
| 111 | [ANUS](#anus) | AI Agent | AI agent framework | Enterprise | TODO | active | balanced | — |
| 112 | [AI-Crash-Course](#ai-crash-course) | Educational | AI research in 2 weeks | Deep expertise | reference | educational | — | — |
| 113 | [firecrawl-mcp-server](#firecrawl-mcp-server) | MCP | Firecrawl MCP for Cursor/Claude | Non-MCP | MCP config | active | fast | — |
| 114 | [rllm](#rllm) | ML/RL | RL training for LLMs | Inference only | `pip install rllm` | active | quality | GPU |
| 115 | [smallpond](#smallpond-deepseek) | Data | Lightweight data processing | Large scale | TODO | active | fast | data |
| 116 | [react-grab](#react-grab) | DevTools | Select context for coding agents | Non-React | TODO | active | fast | — |
| 117 | [GenAI-Showcase](#genai-showcase-mongodb) | Educational | MongoDB GenAI cookbook | Non-MongoDB | reference | active | — | — |
| 118 | [mcp-ui](#mcp-ui) | MCP | UI over MCP protocol | Non-MCP | TODO | active | balanced | — |
| 119 | [Search-R1](#search-r1) | ML | RL for reasoning + search | Simple search | TODO | active | quality | — |
| 120 | [TorBot](#torbot) | OSINT | Dark web OSINT tool | Non-OSINT | `pip install torbot` | active | balanced | — |
| 121 | [awesome-ai-devtools](#awesome-ai-devtools) | Curated | AI developer tools list | Production | reference | curated | — | — |
| 122 | [AGiXT](#agixt) | AI Agent | Dynamic AI agent platform | Simple tasks | `docker compose up` | active | balanced | API keys |
| 123 | [cloudflare/agents](#cloudflareagents) | Infra | AI Agents on Cloudflare | Non-Cloudflare | TODO | active | fast | — |
| 124 | [goku](#goku-saiyan-world) | Video Gen | CVPR2025 video generation | Images-only | TODO | active | quality | — |
| 125 | [cc-wf-studio](#cc-wf-studio) | Workflow | CC Workflow Studio | Simple tasks | TODO | active | balanced | — |
| 126 | [Leaked-GPTs](#leaked-gpts) | Prompts | Leaked GPT prompts | Original prompts | reference | active | — | — |
| 127 | [oasis](#oasis-camel-ai) | Simulation | Million-agent social simulation | Small scale | TODO | active | quality | — |
| 128 | [comfyui_LLM_party](#comfyui_llm_party) | ComfyUI | LLM agents in ComfyUI | Non-ComfyUI | TODO | active | balanced | — |
| 129 | [Awesome-OSINT-For-Everything](#awesome-osint-for-everything) | Curated | OSINT tools for cybersecurity | Non-OSINT | reference | curated | — | — |
| 130 | [CyberSources](#cybersources) | Curated | Cybersecurity tools list | Non-security | reference | curated | — | — |
| 131 | [twitter-api-client](#twitter-api-client) | API | X/Twitter v1, v2, GraphQL | Non-Twitter | `pip install twitter-api-client` | active | fast | API keys |
| 132 | [ai-gradio](#ai-gradio) | UI | AI apps with Gradio | Non-Gradio | `pip install ai-gradio` | active | balanced | API keys |
| 133 | [Telegram-OSINT](#telegram-osint) | Curated | Telegram OSINT resources | Non-OSINT | reference | curated | — | — |
| 134 | [solana-agent-kit (sendaifun)](#solana-agent-kit) | Solana | Solana AI agent toolkit | Non-Solana | `npm i solana-agent-kit` | active | fast | wallet |
| 135 | [QuantMuse](#quantmuse) | Trading | AI-powered quant trading | Manual trading | TODO | active | balanced | — |
| 136 | [terminal](#terminal-m4tt72) | UI | Terminal-style website | Traditional UI | TODO | active | fast | — |
| 137 | [russia-mobile-internet-whitelist](#russia-mobile-internet-whitelist) | Reference | Russia mobile internet whitelist | Non-Russian | reference | active | — | — |
| 138 | [IQuest-Coder-V1](#iquest-coder-v1) | AI Coding | IQuest Coder | Other IDEs | TODO | active | balanced | — |
| 139 | [LLMRouter](#llmrouter) | Infra | LLM routing library | Single LLM | `pip install llmrouter` | active | fast | API keys |
| 140 | [jito-labs/mev-bot](#jito-labsmev-bot) | MEV | Solana MEV bot | Non-MEV | TODO | active | fast | wallet |
| 141 | [listen (piotrostr)](#listen-piotrostr) | DeFi | DeFAI Swiss Army Knife | Non-DeFi | `docker compose up` | active | fast | wallet |
| 142 | [Free-APIs](#free-apis) | Curated | Free APIs for developers | Paid APIs | reference | curated | — | — |
| 143 | [goat-sdk/goat](#goat-sdkgoat) | Blockchain | Agentic finance toolkit | Non-blockchain | `npm i @goat-sdk/core` | active | balanced | wallet |
| 144 | [ChatGemini](#chatgemini) | LLM UI | Web client for Gemini | Other LLMs | TODO | active | fast | API key |
| 145 | [ai-prompts](#ai-prompts-instructa) | Curated | AI prompts for Cursor/Cline | Custom prompts | reference | curated | — | — |
| 146 | [telegram-web-app-bot-example](#telegram-web-app-bot-example) | Telegram | Telegram Mini App example | Non-Telegram | TODO | active | fast | — |
| 147 | [n8n-workflows](#n8n-workflows) | Curated | n8n workflows collection | Non-n8n | reference | curated | — | — |
| 148 | [MediaCrawler](#mediacrawler) | Scraping | 小红书/抖音/微博 crawler | Non-Chinese | TODO | active | fast | — |
| 149 | [anime.js](#animejs) | Animation | JavaScript animation engine | Non-JS | `npm install animejs` | active | fast | — |
| 150 | [nanobot](#nanobot) | MCP | Build MCP agents | Non-MCP | TODO | active | balanced | — |
| 151 | [agentic-cursorrules](#agentic-cursorrules) | DevTools | Multi-agent Cursor via file-tree | Non-Cursor | copy files | active | fast | — |
| 152 | [awesome-ai-memory](#awesome-ai-memory) | Curated | AI memory projects list | Production | reference | curated | — | — |
| 153 | [ZerePy (blorm)](#zerepy) | AI Agent | Python AI agent framework | Non-Python | `poetry install` | active | balanced | API keys |
| 154 | [gensx](#gensx) | TypeScript | React-like agents/workflows | Non-TS | `npm install gensx` | active | balanced | — |
| 155 | [grok3-api](#grok3-api) | API | Unofficial Grok 3 API | Official API | TODO | active | fast | — |
| 156 | [awesome-windsurf](#awesome-windsurf) | Curated | Windsurf editor resources | Non-Windsurf | reference | curated | — | — |
| 157 | [CodeGuide-starter-lite](#codeguide-starter-lite) | Template | CodeGuide starter | Custom templates | TODO | active | fast | — |
| 158 | [openagi](#openagi) | AI Agent | Open agents/AGI framework | Simple tasks | TODO | active | balanced | — |
| 159 | [awesome-full-stack-ml-courses](#awesome-full-stack-machine-learning-courses) | Educational | ML courses (MIT, Stanford) | Quick learning | reference | educational | — | — |
| 160 | [Awesome-LLM-Resources-List](#awesome-llm-resources-list) | Curated | Applied AI engineering resources | Production | reference | curated | — | — |
| 161 | [pplx2api](#pplx2api) | API | OpenAI-compatible Perplexity API | Direct Perplexity | `docker run` | active | fast | — |
| 162 | [vision-agent](#vision-agent-askui) | Desktop | AI controls desktop/mobile | Web-only | `pip install vision-agent` | active | balanced | — |
| 163 | [AttackMachine](#attackmachine) | DeFi | AIO LayerZero, zkSync, Starknet | Single chain | `python main.py` | active | fast | wallet |
| 164 | [gemini-browser](#gemini-browser-browserbase) | Browser | Gemini Computer Use | Non-Gemini | `npm start` | active | balanced | API key |
| 165 | [FreeDatabreaches](#freedatabreaches) | Security | Free databreaches download | Legal concerns | reference | active | — | — |
| 166 | [astra](#astra-shreyas-29) | Template | AI website builder landing | Custom design | TODO | active | fast | — |
| 167 | [luro-ai](#luro-ai) | Template | Modern SaaS UI template | Custom design | TODO | active | fast | — |
| 168 | [agentipy (niceberginc)](#agentipy) | Solana | Python Solana AI agents | Non-Solana | `pip install agentipy` | active | fast | wallet |
| 169 | [antd-multipurpose-dashboard](#antd-multipurpose-dashboard) | Template | Ant Design 5 dashboard | Non-React | `npm run dev` | active | fast | — |
| 170 | [linkify](#linkify-shreyas-29) | Template | Modern SaaS template | Custom design | TODO | active | fast | — |
| 171 | [mcp-server-gemini](#mcp-server-gemini) | MCP | Gemini MCP server | Non-Gemini | `npm i -g mcp-server-gemini` | active | fast | API key |
| 172 | [deprecated-generative-ai-python](#deprecated-generative-ai-python) | API | Deprecated Google GenAI SDK | Current SDK | — | deprecated | — | — |
| 173 | [CloudFreed-CloudFlare-solver-bypass](#cloudfreed-cloudflare-solver-bypass) | Scraping | CloudFlare bypass | Non-CF sites | TODO | active | fast | — |
| 174 | [dreamsxin/example](#dreamsxinexample) | Reference | Various code examples | Production | reference | active | — | — |
| 175 | [vetra](#vetra) | Template | AI marketing landing page | Custom design | TODO | active | fast | — |
| 176 | [Trading-API](#trading-api) | Trading | Pump.fun programmatic trading | Analytics only | `python main.py` | active | fast | wallet |
| 177 | [geyser-grpc-plugin](#geyser-grpc-plugin-jito) | Solana | Jito Geyser GRPC plugin | Non-Solana | `cargo build` | active | fast | RPC |
| 178 | [linkedin-bot](#linkedin-bot) | Automation | LinkedIn automation | Non-LinkedIn | TODO | active | balanced | credentials |
| 179 | [solana-winternitz-vault](#solana-winternitz-vault) | Solana | Quantum-resistant vault | Non-quantum | TODO | active | balanced | wallet |
| 180 | [ezlocalai](#ezlocalai) | Infra | Local AI server, OpenAI style | Cloud APIs | `ezlocalai serve` | active | balanced | — |
| 181 | [Threads-Scraper](#threads-scraper) | Scraping | Threads.net data extraction | Non-Threads | TODO | active | fast | — |
| 182 | [Gradient-Network-Bot](#gradient-network-bot) | Automation | Gradient Network automation | Non-Gradient | TODO | active | fast | — |
| 183 | [Peargent](#peargent) | AI Agent | Lightweight Python agents | Complex agents | TODO | active | balanced | — |
| 184 | [deep-research-mcp-server](#deep-research-mcp-server) | MCP | Deep research with Gemini | Non-research | MCP config | active | balanced | API key |
| 185 | [Sentience (Galadriel)](#sentience-galadriel) | AI Agent | Unruggable AI agents | Quick prototypes | TODO | active | balanced | TEE |
| 186 | [cdp-agentkit-nodejs](#cdp-agentkit-nodejs) | Blockchain | Coinbase onchain AI agents | Non-Base | `npm install` | active | balanced | CDP key |
| 187 | [qudeai-framework-v.1](#qudeai-framework-v1) | AI Agent | CLI agents with Qude copilot | GUI | TODO | active | balanced | — |
| 188 | [propease](#propease) | Template | Real estate SaaS landing | Non-RE | TODO | active | fast | — |
| 189 | [meme-mcp](#meme-mcp) | MCP | Meme generation via ImgFlip | Serious content | MCP config | active | fast | — |
| 190 | [solana-trader-proto](#solana-trader-proto) | Trading | bloXroute Solana trader proto | Non-Solana | TODO | active | fast | — |
| 191 | [twAuto](#twauto) | Automation | Twitter automation with Selenium | API access | TODO | active | fast | credentials |
| 192 | [aether](#aether-shreyas-29) | Chatbot | AI-powered chatbot | Simple bots | TODO | active | balanced | — |
| 193 | [uniswap-v2-v3-arbitrage](#uniswap-v2-v3-arbitrage) | MEV | Uniswap arbitrage bot | Non-Uniswap | TODO | active | fast | wallet |
| 194 | [nextjs-lucia-dashboard](#nextjs-lucia-neon-postgresql-drizzle-dashboard) | Template | Personal all-in-one panel | Simple apps | TODO | active | balanced | — |
| 195 | [caps-ai](#caps-ai) | Template | Social media management landing | Custom design | TODO | active | fast | — |
| 196 | [maushish/alris](#maushishalris) | Reference | Twitter handle reference | Production | reference | active | — | — |
| 197 | [avento](#avento) | Template | Agency OS landing page | Custom design | TODO | active | fast | — |
| 198 | [Telegram_Scraper](#telegram_scraper-amirwpi) | Scraping | Telegram group scraper | Non-Telegram | TODO | active | fast | TG API |
| 199 | [openagent (openagentoa)](#openagent-openagentoa) | AI Agent | Create/battle/trade AI agents | Simple agents | TODO | experimental | balanced | wallet |
| 200 | [AGInterface](#aginterface) | UI | Modular chat for agentic systems | Simple bots | TODO | active | balanced | — |
| 201 | [ai-agent-demo](#ai-agent-demo) | Demo | AI agent demo project | Production | reference | demo | — | — |
| 202 | [GeminiSheeridVerify](#geminisheeridverify) | Auth | Gemini SheerID verification | Non-Gemini | TODO | active | fast | — |
| 203 | [physics-liquid-glass](#physics-liquid-glass) | Graphics | Physics liquid glass effect | Non-graphics | TODO | active | fast | — |
| 204 | [gemini-notion-extension](#gemini-notion-extension) | Extension | Gemini + Notion integration | Non-Notion | TODO | active | fast | — |
| 205 | [run-gemini-cli](#run-gemini-cli-google-github-actions) | CI/CD | GitHub Action for Gemini CLI | Non-GH Actions | action config | active | fast | API key |
| 206 | [hsm-service](#hsm-service) | Security | Cryptographic service with SoftHSM | Simple crypto | TODO | active | balanced | — |
| 207 | [promptdc-cursor](#promptdc-cursor) | DevTools | Prompt DC for Cursor | Non-Cursor | TODO | active | fast | — |
| 208 | [promptdc-vscode](#promptdc-vscode) | DevTools | Prompt DC for VSCode | Non-VSCode | TODO | active | fast | — |
| 209 | [Threads.net-Writer](#threadsnet-writer) | Social | Threads.net updates with Gemini | Non-Threads | TODO | active | fast | API key |
| 210 | [webscraper-ts](#webscraper-ts) | Scraping | Web scraper in TypeScript | Non-TS | TODO | active | fast | — |
| 211 | [scrapliz](#scrapliz) | Extension | Chrome extension for scraping | Non-Chrome | TODO | active | fast | — |
| 212 | [twit](#twit-hypefury) | API | Twitter API client fork | Non-Twitter | TODO | active | fast | API keys |
| 213 | [dexbotsdev-repos](#dexbotsdev-repos) | DeFi | Solana/DeFi utilities collection | Non-Solana | TODO | active | fast | wallet |
| 214 | [alexkoshmelev-repos](#alexkoshmelev-repos) | Telegram | Telegram web app, dapp templates | Non-Telegram | TODO | active | fast | — |
| 215 | [abdibrokhim-bots](#abdibrokhim-bots) | Bot | Telegram bots collection | Non-Telegram | TODO | active | fast | TG token |
| 216 | [browser-use](#browser-use) | Browser | Web automation for AI agents | API-only | `uv add browser-use` | active | balanced | LLM key |
| 217 | [web-ui (browser-use)](#web-ui) | Browser | Web UI for browser-use | Headless-only | `python webui.py` | active | balanced | LLM key |
| 218 | [pyspur](#pyspur) | ML | Visual LLM workflow editor | CLI-only | `docker compose up` | active | balanced | API keys |
| 219 | [exo](#exo) | Infra | Distributed AI inference | Single GPU | `pip install exo` | active | quality | devices |
| 220 | [swarmnode-python](#swarmnode-python) | Infra | Serverless AI agents | Self-hosted only | `pip install swarmnode` | active | balanced | API key |
| 221 | [rig](#rig) | ML | Rust LLM applications | Python | `cargo add rig-core` | active | fast | — |
| 222 | [woody-hub](#woody-hub) | Extension | GMGN browser enhancement | CLI | `pnpm dev` | experimental | fast | — |
| 223 | [woody](#woody) | Trading | AI copy trading | Manual strategies | TODO | experimental | balanced | wallet |
| 224 | [Thin-Floor-Strategy](#thin-floor-strategy) | Trading | Magic Eden NFT trading | Fungibles | TODO | experimental | fast | wallet |
| 225 | [OpenTruthV1](#opentruthv1) | AI | Terminal of Truths clone | Production | TODO | experimental | balanced | LLM key |
| 226 | [pump-meta](#pump-meta) | Analytics | Pump.fun sentiment analysis | Trading | `python main.py` | experimental | balanced | — |
| 227 | [gmgn-scripts](#gmgn-scripts) | Scraping | GMGN utility scripts | Full API | TODO | experimental | fast | — |
| 228 | [gmgn_smart](#gmgn_smart) | Scraping | GMGN smart wallet tools | Unknown | TODO | unknown | fast | — |
| 229 | [gmgn-api](#gmgn-api) | Scraping | GMGN API wrapper | Full scraping | TODO | unknown | fast | — |
| 230 | [gmgn_parser](#gmgn_parser) | Scraping | GMGN data parsing | API calls | TODO | unknown | fast | — |
| 231 | [portkey-gateway](#portkey-gateway) | Infra | AI Gateway, 200+ LLMs | Simple calls | `npm install` | active | fast | API keys |
| 232 | [MEMETOOL-V0.3](#memetool-v03) | Trading | Meme coin tools | Non-meme | TODO | unknown | fast | — |
| 233 | [poe-api-wrapper](#poe-api-wrapper) | API | Free GPT-4/Claude via Poe | Direct API | `pip install poe-api-wrapper` | active | balanced | Poe cookie |
| 234 | [solana-pnl-card-bot](#solana-pnl-card-bot) | Analytics | PnL card generation | Trading | TODO | unknown | fast | token |
| 235 | [Growtradebot](#growtradebot) | Trading | Telegram Solana bot | Non-Telegram | TODO | experimental | fast | wallet, TG |
| 236 | [ct_alpha](#ct_alpha) | Analytics | CT profitability calculator | Trading | TODO | unknown | balanced | tweets |
| 237 | [Smart_Money_Follower](#smart_money_follower) | Analytics | Top Solana wallet analysis | Trading | TODO | experimental | balanced | GMGN API |
| 238 | [gmgn_analyst](#gmgn_analyst) | Analytics | Pump.Fun token analysis | Trading | TODO | experimental | balanced | GMGN API |
| 239 | [Pump-Fun-API](#pump-fun-api) | Trading | Pump.fun programmatic trading | Analytics | TODO | unknown | fast | wallet |
| 240 | [telegram_bot](#telegram_bot) | Bot | Telegram bot template | Non-Telegram | TODO | unknown | fast | TG token |
| 241 | [consistencydecoder](#consistencydecoder) | ML | OpenAI Consistency VAE | Non-image | TODO | unknown | quality | images |
| 242 | [chatgpt-ai-template](#chatgpt-ai-template) | Template | ChatGPT UI template | Backend-only | `npm run dev` | unknown | fast | — |
| 243 | [vision-ui-dashboard-react](#vision-ui-dashboard-react) | Template | React dashboard template | Non-React | `npm run dev` | unknown | fast | — |
| 244 | [deepscaler](#deepscaler) | ML/RL | RL training for LLMs | Inference only | `uv pip install rllm` | active | quality | GPU |
| 245 | [bolt.diy](#boltdiy) | DevTools | AI web dev, any LLM | Mobile apps | `docker compose up` | active | balanced | LLM key |
| 246 | [listen](#listen) | Solana | DEX trading, monitoring | Non-Solana | `docker compose up` | active | fast | wallet, RPC |
| 247 | [goat](#goat) | Blockchain | Multi-chain AI agents | Simple scripts | `npm i @goat-sdk/core` | active | balanced | wallet |
| 248 | [axium](#axium) | Trading | Pumpfun/Raydium trading | DeFi beyond | `docker compose up` | experimental | fast | wallet |
| 249 | [openagent](#openagent) | AI | Multi-agent battles Solana | Non-Solana | `npm install` | experimental | balanced | wallet |
| 250 | [sentience](#sentience) | AI | Unruggable verified AI | Prototypes | `pip install galadriel` | active | balanced | TEE |
| 251 | [devin.cursorrules](#devincursorrules) | DevTools | Make Cursor like Devin | Non-IDE | copy files | active | fast | — |
| 252 | [alris](#alris) | Trading | AI yield optimizer | Manual trading | `npm run dev` | experimental | balanced | wallet |
| 253 | [pumpfun-king-of-the-hill](#pumpfun-king-of-the-hill) | Analytics | Pump.fun visualization | Trading | `npm run dev` | experimental | fast | API |
| 254 | [agent-zero](#agent-zero-forked) | AI | Personal AI with memory | Stateless | `docker pull agent0ai/agent-zero` | active | balanced | LLM key |
| 255 | [ds-top-traders](#ds-top-traders) | Scraping | Dexscreener top traders | Real-time | `python main.py` | experimental | fast | CA |
| 256 | [cdp-agentkit-nodejs (forked)](#cdp-agentkit-nodejs-forked) | Blockchain | Coinbase onchain AI | Non-Base | `npm install` | active | balanced | CDP key |
| 257 | [solana-wallet-checker](#solana-wallet-checker) | Analytics | Mass wallet scanning | Single wallet | `python main.py` | experimental | fast | wallet list |
| 258 | [gmgn-scraper](#gmgn-scraper) | Scraping | GMGN.ai data extraction | Real-time | `node index.js` | experimental | fast | — |
| 259 | [solana-agent-kit (forked)](#solana-agent-kit-forked) | Blockchain | 60+ Solana actions | EVM-only | `npm i solana-agent-kit` | active | fast | wallet |
| 260 | [agentipy (forked)](#agentipy-forked) | Blockchain | Python Solana AI agents | TypeScript | `pip install agentipy` | active | fast | wallet |
| 261 | [ZerePy (forked)](#zerepy-forked) | AI | Twitter/X AI agents | Non-social | `poetry install` | active | balanced | X API |
| 262 | [n8n-workflows (Zie619)](#n8n-workflows-zie619) | Curated | n8n workflows (50k stars) | Non-n8n | reference | curated | — | — |
| 263 | [MediaCrawler (starred)](#mediacrawler-starred) | Scraping | Chinese social crawlers | Non-Chinese | TODO | active | fast | — |
| 264 | [anime.js (starred)](#animejs-starred) | Animation | JS animation engine | Non-JS | `npm install animejs` | active | fast | — |
| 265 | [deprecated-generative-ai-python (starred)](#deprecated-generative-ai-python-starred) | API | Old Google GenAI SDK | Current SDK | — | deprecated | — | — |
| 266 | [run-gemini-cli (starred)](#run-gemini-cli-starred) | CI/CD | GH Action Gemini CLI | Non-GH | action config | active | fast | API key |
| 267 | [system-prompts (starred)](#system-prompts-starred) | Prompts | AI tool system prompts | Custom | reference | active | — | — |
| 268 | [n8n-workflows (starred)](#n8n-workflows-starred) | Curated | n8n workflows collection | Non-n8n | reference | curated | — | — |
| 269 | [jito-mev-bot (starred)](#jito-mev-bot-starred) | MEV | Jito MEV bot | Non-MEV | TODO | active | fast | wallet |
| 270 | [listen (starred)](#listen-starred) | DeFi | DeFAI Swiss Army Knife | Non-DeFi | `docker compose up` | active | fast | wallet |
| 271 | [goat-sdk (starred)](#goat-sdk-starred) | Blockchain | Agentic finance toolkit | Non-blockchain | `npm i @goat-sdk/core` | active | balanced | wallet |
| 272 | [solana-agent-kit (starred)](#solana-agent-kit-starred) | Solana | Solana AI agent toolkit | Non-Solana | `npm i solana-agent-kit` | active | fast | wallet |

---

## 📖 Detailed Descriptions

---

## deepscaler

**TL;DR:** rLLM — открытый фреймворк для пост-тренинга языковых моделей через reinforcement learning. Позволяет строить кастомных агентов, обучать их через RL и деплоить. DeepScaleR-1.5B превзошёл O1-Preview на AIME (43.1%).

### Быстрый выбор
- ✅ Используй если:
  - Хочешь воспроизвести DeepSeek R1 / OpenAI O1/O3 своими силами
  - Нужен RL-тренинг для LLM с scaling context length
  - Есть GPU и хочешь обучить reasoning model
  - Нужен AgentWorkflowEngine для agentic программ
- ❌ Не используй если:
  - Нужен только инференс без обучения
  - Нет GPU (минимум 8GB VRAM для базовых экспериментов)
  - Не знаком с RL и PyTorch

### 🚀 Запуск
```bash
# Прямая установка
uv pip install "rllm[verl] @ git+https://github.com/rllm-org/rllm.git"

# Или из исходников
git clone https://github.com/rllm-org/rllm.git && cd rllm
uv venv --python 3.11 && source .venv/bin/activate
uv pip install -e .[verl]
```

### 🧩 Архитектура
- **Бэкенды обучения:** `verl` (distributed, Megatron) и `tinker` (lightweight, CPU)
- **AgentWorkflowEngine:** обучение произвольных agentic программ
- **Core:** `rllm/` — главный пакет, `examples/` — примеры конфигов
- **Entrypoints:** [train.py](https://github.com/rllm-org/rllm/blob/main/train.py), [examples/](https://github.com/rllm-org/rllm/tree/main/examples)

### 🧪 Примеры задач
- DeepScaleR-1.5B: 43.1% на AIME, превзошёл O1-Preview
- DeepCoder-14B: 60.6% на LiveCodeBench, уровень o3-mini
- DeepSWE-32B: 59% на SWEBench-Verified, топ open-weight
- Tongyi DeepResearch (Alibaba) использует rLLM
- Terminal-Bench-RL: long-horizon terminal agents

### ⚠️ Ограничения
- Требует Python ≥3.10 (3.11 для tinker)
- Нужен `protoc` для verl backend
- verl требует multi-GPU для полного обучения
- Быстро итерируется — breaking changes возможны
- Docker рекомендуется для изоляции окружения

### 🧭 Fit / Maturity / Ops
- **Fit:** RL тренинг LLM, reasoning models, agentic workflows
- **Maturity:** active (v0.2.1, частые релизы)
- **Latency/Cost:** quality (training-focused, GPU-heavy)
- **Data constraints:** datasets в формате HuggingFace, модели transformers-совместимые
- **Ops friction:** medium (требует GPU, настройка конфигов)

### Full links
- Repo: https://github.com/amibars/deepscaler
- Original README: https://github.com/agentica-project/deepscaler/blob/main/README.md
- Docs: https://rllm-project.readthedocs.io
- Discord: https://discord.gg/BDH46HT9en

---

## bolt.diy

**TL;DR:** Open-source AI coding assistant от StackBlitz. В браузере пишешь full-stack web-приложения с любой LLM (OpenAI, Claude, Ollama, DeepSeek и 19+ других). Есть desktop app, деплой на Netlify/Vercel, Git интеграция, MCP support.

### Быстрый выбор
- ✅ Используй если:
  - Хочешь AI-ассистента для web-разработки в браузере
  - Нужна свобода выбора LLM (включая локальные через Ollama)
  - Нужен деплой на Netlify/Vercel/GitHub Pages
  - Хочешь видеть diff изменений и откатывать код
  - Нужна поддержка Docker
- ❌ Не используй если:
  - Разрабатываешь мобильные приложения (React Native через Expo есть, но ограничено)
  - Нужен backend-only без UI
  - Нет API ключей ни для одного провайдера

### 🚀 Запуск
```bash
# Quick — скачай бинарник с https://github.com/stackblitz-labs/bolt.diy/releases

# Или Docker:
docker compose up

# Или Node.js:
pnpm install && pnpm run dev
```

### 🧩 Архитектура
- **Frontend:** Remix/React, WebContainer API для in-browser execution
- **19+ LLM providers:** OpenAI, Anthropic, Ollama, DeepSeek, Groq, Cohere, Together, Perplexity, HuggingFace, etc.
- **MCP (Model Context Protocol):** расширяемые AI tools
- **Entrypoints:** `app/` — Remix app, `electron/` — desktop, `Dockerfile`
- **Ключевые файлы:** [app/routes/](https://github.com/stackblitz-labs/bolt.diy/tree/main/app/routes), [docker-compose.yml](https://github.com/stackblitz-labs/bolt.diy/blob/main/docker-compose.yaml)

### 🧪 Примеры задач
- Создание полного web-приложения через prompt
- Деплой на Netlify/Vercel одной кнопкой
- Импорт проекта из GitHub
- Attach изображения для контекста
- Supabase интеграция для БД
- Expo apps для React Native

### ⚠️ Ограничения
- NodeJS-based applications only (не Python backend)
- macOS: может понадобиться `xattr -cr /path/to/Bolt.app`
- Electron app экспериментальный
- Ollama: нужен CORS (--origins)
- Большие модели требуют больше RAM

### 🧭 Fit / Maturity / Ops
- **Fit:** AI web development, rapid prototyping
- **Maturity:** active (большое community, частые обновления)
- **Latency/Cost:** balanced (зависит от LLM провайдера)
- **Data constraints:** prompts, images для контекста
- **Ops friction:** low (Docker или бинарник)

### Full links
- Repo: https://github.com/amibars/bolt.diy
- Original README: https://github.com/stackblitz-labs/bolt.diy/blob/main/README.md
- Docs: https://stackblitz-labs.github.io/bolt.diy/
- Community: https://thinktank.ottomator.ai/

---

## listen

**TL;DR:** Solana Swiss Army Knife 🦀 — фреймворк для алготрейдинга и AI portfolio management агентов. Multi-DEX swaps (Pump.fun, Jupiter, Raydium), Jito MEV bundles, real-time мониторинг, Prometheus метрики. Интегрируется с Rig AI framework.

### Быстрый выбор
- ✅ Используй если:
  - Нужен алготрейдинг на Solana
  - Хочешь AI агента для управления портфелем (Rig integration)
  - Нужны быстрые tx через Jito bundles
  - Нужен real-time мониторинг транзакций
- ❌ Не используй если:
  - Работаешь только с EVM
  - Не нужен трейдинг (только read-only аналитика)
  - Нет Solana кошелька/RPC

### 🚀 Запуск
```bash
# Заполни .env.example → .env и ./dashboard/.env.example → ./dashboard/.env
docker compose up

# Или вручную:
sudo apt install protoc build-essential pkg-config libssl-dev
cargo build --release
```

### 🧩 Архитектура
```
Rig Agent Kit → Multi-tenant Stream Manager + Delegated Wallet Manager
     ↓
Trading Engine → Order Collector → Pipeline Executor → Order Executor
     ↓
Data Service → Substreams Indexer → Clickhouse OLAP → Price Stream
```
- **Rust nightly** required
- **Entrypoints:** [src/main.rs](https://github.com/piotrostr/listen/blob/main/src/main.rs), [src/agent.rs](https://github.com/piotrostr/listen/blob/main/src/agent.rs) (AI agent example)
- **Dashboard:** `./dashboard/` — UI на порту 4173

### 🧪 Примеры задач
- `cargo run -- listen --worker-count 4` — мониторинг транзакций
- `cargo run -- swap --input-mint sol --output-mint USDC --amount 10000000` — своп
- AI agent через Rig framework: Natural language → Solana actions
- Prometheus metrics на `localhost:3030/metrics`
- Flamegraph профилирование свопов

### ⚠️ Ограничения
- Rapid iteration — breaking changes возможны
- Mainnet by default — осторожно с конфигами для testnet
- `auth.json` нужен для JITO gRPC
- `fund.json` для keypair (формат solana-keygen, 64 bytes)
- Clickhouse для полного data service

### 🧭 Fit / Maturity / Ops
- **Fit:** Solana trading, AI portfolio agents
- **Maturity:** active (быстро развивается)
- **Latency/Cost:** fast (Jito bundles)
- **Data constraints:** Solana wallet, RPC endpoint, optional JITO auth
- **Ops friction:** medium (Rust nightly, protoc, systemd services)

### Full links
- Repo: https://github.com/amibars/listen
- Original README: https://github.com/piotrostr/listen/blob/main/README.md
- Docs: https://docs.listen-rs.com
- App: https://app.listen-rs.com

---

## goat

**TL;DR:** GOAT 🐐 (Great Onchain Agent Toolkit) — крупнейший agentic finance toolkit. 200+ blockchain tools, 30+ chains, работает с LangChain/Vercel AI SDK/Eliza. Агенты могут: торговать, минтить NFT, делать ставки на prediction markets, получать yield.

### Быстрый выбор
- ✅ Используй если:
  - Нужен AI агент с onchain действиями (любой chain)
  - Хочешь интеграцию с DeFi (Uniswap, Jupiter, Polymarket, etc.)
  - Работаешь с LangChain или Vercel AI SDK
  - Нужна поддержка multiple wallets (Crossmint, Coinbase, keypairs)
- ❌ Не используй если:
  - Простой скрипт без AI
  - Нужен только read-only доступ (используй RPC напрямую)

### 🚀 Запуск
```typescript
// TypeScript
npm i @goat-sdk/core @goat-sdk/wallet-evm @goat-sdk/plugin-erc20
```
```python
# Python
pip install goat-sdk
```

### 🧩 Архитектура
- **Core:** минимальное ядро, tools устанавливаются отдельно
- **200+ plugins:** 0x, 1inch, Jupiter, Uniswap, Polymarket, CoinGecko, Farcaster, etc.
- **Wallets:** EVM, Solana, Cosmos, Chromia, Fuel, Radix, Starknet, Aptos, Sui
- **Agent frameworks:** LangChain, Vercel AI SDK, Eliza, ElevenLabs, GAME
- **Entrypoints:** [typescript/packages/](https://github.com/goat-sdk/goat/tree/main/typescript/packages), [python/src/](https://github.com/goat-sdk/goat/tree/main/python/src)

### 🧪 Примеры задач
- Своп токенов через Jupiter/Uniswap
- Mint NFT через Crossmint
- Ставки на Polymarket
- CoinGecko/BirdEye price feeds
- Farcaster posting
- ENS resolution
- Bridge через DeBridge

### ⚠️ Ограничения
- Каждый plugin — отдельная зависимость
- Нужны API keys для providers (CoinGecko, 1inch, etc.)
- Python SDK менее complete чем TypeScript
- Private keys нужны для signing

### 🧭 Fit / Maturity / Ops
- **Fit:** Multi-chain AI agents, DeFi automation
- **Maturity:** active (MIT license, growing ecosystem)
- **Latency/Cost:** balanced (зависит от chain и plugin)
- **Data constraints:** wallet keys, provider API keys
- **Ops friction:** low (modular, install what you need)

### Full links
- Repo: https://github.com/amibars/goat
- Original README: https://github.com/goat-sdk/goat/blob/main/README.md
- Docs: https://ohmygoat.dev

---

## agent-zero

**TL;DR:** Personal AI framework, который растёт и учится вместе с тобой. Использует OS как tool (терминал, код). Multi-agent кооперация — агенты создают subordinates. Полностью кастомизируемый через prompts/. Persistent memory.

### Быстрый выбор
- ✅ Используй если:
  - Нужен general-purpose AI ассистент с памятью
  - Хочешь multi-agent систему с делегированием задач
  - Нужен агент, который пишет и запускает свой код
  - Хочешь полную кастомизацию поведения через prompts
- ❌ Не используй если:
  - Нужен stateless agent без памяти
  - Нужен только chat без tool use
  - Нет Docker/Python environment

### 🚀 Запуск
```bash
docker pull agent0ai/agent-zero
docker run -p 50001:80 agent0ai/agent-zero
# Открой http://localhost:50001
```

### 🧩 Архитектура
- **No hard-coded rails** — всё поведение в `prompts/default/agent.system.md`
- **Default tools:** knowledge, code execution, communication, online search
- **Multi-agent:** Agent 0 → subordinates, каждый агент отчитывается superior
- **Memory:** persistent, хранит решения, код, факты
- **Instruments:** custom functions вызываемые агентом
- **Entrypoints:** [python/tools/](https://github.com/frdel/agent-zero/tree/main/python/tools), [prompts/](https://github.com/frdel/agent-zero/tree/main/prompts)

### 🧪 Примеры задач
- "Напиши скрипт для парсинга сайта" — агент сам пишет и запускает код
- "Реши эту задачу" — создаёт subordinate agents для subtasks
- "Запомни как я предпочитаю форматирование" — использует memory
- Projects: изолированные workspaces с своими prompts, files, memory

### ⚠️ Ограничения
- Real-time terminal streaming — нужен контроль пользователя
- Memory растёт — может замедлиться на больших проектах
- Нужен LLM API key (OpenAI, Anthropic, etc.)
- Docker рекомендуется для sandbox
- MCP Server/Client появился в v0.8.5

### 🧭 Fit / Maturity / Ops
- **Fit:** Personal AI assistant, task automation, coding
- **Maturity:** active (v0.9.7, частые обновления)
- **Latency/Cost:** balanced (зависит от LLM)
- **Data constraints:** LLM API key, optional custom prompts
- **Ops friction:** low (Docker one-liner)

### Full links
- Repo: https://github.com/amibars/agent-zero
- Original README: https://github.com/frdel/agent-zero/blob/main/README.md
- Docs: https://github.com/frdel/agent-zero/tree/main/docs
- Video: https://youtu.be/MdzLhWWoxEs

---

## solana-agent-kit

**TL;DR:** Open-source toolkit для подключения AI агентов к Solana протоколам. 60+ автономных действий: trade, mint tokens/NFTs, airdrop, DeFi (Jupiter, Raydium, Orca, Meteora), bridge через Wormhole. Интеграция с LangChain и Vercel AI SDK.

### Быстрый выбор
- ✅ Используй если:
  - Нужен AI агент с Solana actions
  - Интегрируешься с LangChain/Vercel AI SDK
  - Нужен DeFi: Jupiter swaps, Raydium pools, Orca Whirlpools
  - Хочешь NFT через Metaplex или 3Land
  - Нужен cross-chain bridge (Wormhole)
- ❌ Не используй если:
  - Только EVM chains (используй goat или cdp-agentkit)
  - Не нужен AI — просто SDK (используй @solana/web3.js)

### 🚀 Запуск
```bash
npm install solana-agent-kit
```
```typescript
import { SolanaAgentKit, createSolanaTools } from "solana-agent-kit";

const agent = new SolanaAgentKit(
  "your-wallet-private-key-as-base58",
  "https://api.mainnet-beta.solana.com",
  { OPENAI_API_KEY: "your-openai-api-key" }
);
const tools = createSolanaTools(agent);
```

### 🧩 Архитектура
- **Token ops:** Deploy SPL/Token2022, transfer, stake, ZK airdrop
- **NFT:** Metaplex, 3Land collections
- **DeFi:** Jupiter, Raydium (CPMM, CLMM, AMMv4), Orca, Meteora, Manifest
- **Perps:** Adrena, Drift (vaults, lending, borrowing)
- **Market data:** CoinGecko Pro, Pyth, Allora
- **Entrypoints:** [src/](https://github.com/sendaifun/solana-agent-kit/tree/main/src), [examples/](https://github.com/sendaifun/solana-agent-kit/tree/main/examples)

### 🧪 Примеры задач
- Deploy new SPL token: `agent.deployToken({...})`
- Jupiter swap: `agent.swap({inputMint, outputMint, amount})`
- Stake SOL on Solayer
- Create NFT collection on 3Land
- Bridge tokens via Wormhole
- Drift perpetual trading
- DALL-E artwork for NFTs

### ⚠️ Ограничения
- Private key нужен как base58 string
- CoinGecko Pro API для market data
- Mainnet by default — осторожно с real funds
- Некоторые actions требуют дополнительных API keys

### 🧭 Fit / Maturity / Ops
- **Fit:** Solana DeFi agents, NFT automation
- **Maturity:** active (npm downloads растут)
- **Latency/Cost:** fast (Solana native)
- **Data constraints:** wallet private key, OpenAI key, optional CoinGecko Pro
- **Ops friction:** low (npm install)

### Full links
- Repo: https://github.com/amibars/solana-agent-kit
- Original README: https://github.com/sendaifun/solana-agent-kit/blob/main/README.md
- Docs: https://docs.sendai.fun
- Replit: https://replit.com/@sendaifun/Solana-Agent-Kit

---

## browser-use

**TL;DR:** Python библиотека для browser automation с AI агентами. Агенты видят страницу (vision + HTML), могут кликать, вводить текст, навигировать. CLI для быстрого тестирования. Cloud sandbox для production.

### Быстрый выбор
- ✅ Используй если:
  - Нужен AI агент, который работает с websites
  - Хочешь автоматизировать формы, поиск, скрейпинг
  - Нужна интеграция с любой LLM (OpenAI, Claude, local)
  - Хочешь persistent browser между командами
- ❌ Не используй если:
  - Нужен только API без UI
  - Headless-only без визуализации
  - Не хочешь платить за LLM/Cloud

### 🚀 Запуск
```bash
uv add browser-use
uvx browser-use install  # Install Chromium
```
```python
from browser_use import Agent, Browser, ChatBrowserUse
import asyncio

async def example():
    browser = Browser()
    llm = ChatBrowserUse()
    agent = Agent(task="Find flights from NYC to LA", llm=llm, browser=browser)
    await agent.run()

asyncio.run(example())
```

### 🧩 Архитектура
- **Vision + HTML extraction:** агент видит что на странице
- **Playwright-based:** chromium, firefox, webkit
- **Cloud sandboxes:** browser рядом с агентом, минимальная latency
- **CLI:** `browser-use open`, `browser-use click`, `browser-use type`, etc.
- **Entrypoints:** [browser_use/](https://github.com/browser-use/browser-use/tree/main/browser_use)

### 🧪 Примеры задач
- Form filling — заполнение форм по инструкции
- Grocery shopping — заказ продуктов
- Personal assistant — любые web-задачи
- Flight search — поиск билетов
- LinkedIn job apply automation

### ⚠️ Ограничения
- Требует Python ≥3.11
- Playwright install нужен для browsers
- Stealth browser требует Cloud subscription
- LLM costs за каждое действие

### 🧭 Fit / Maturity / Ops
- **Fit:** Web automation, form filling, scraping
- **Maturity:** active (daily releases)
- **Latency/Cost:** balanced (LLM + browser overhead)
- **Data constraints:** LLM API key, task description
- **Ops friction:** low (uv add, install browsers)

### Full links
- Repo: https://github.com/amibars/browser-use
- Original README: https://github.com/browser-use/browser-use/blob/main/README.md
- Docs: https://docs.browser-use.com
- Cloud: https://cloud.browser-use.com

---

## web-ui

**TL;DR:** Web интерфейс для browser-use. Локальная установка или Docker. VNC viewer для наблюдения за браузером. Поддержка собственного Chrome с cookies и auth.

### Быстрый выбор
- ✅ Используй если:
  - Хочешь GUI для browser-use агентов
  - Нужен VNC для наблюдения за browser actions
  - Хочешь использовать свой Chrome с cookies
- ❌ Не используй если:
  - Нужен только CLI/API
  - Docker unavailable

### 🚀 Запуск
```bash
git clone https://github.com/browser-use/web-ui.git && cd web-ui
cp .env.example .env  # Add API keys
python webui.py --ip 127.0.0.1 --port 7788

# Или Docker:
docker compose up --build
```

### 🧩 Архитектура
- **Gradio-based UI** на порту 7788
- **VNC viewer** на порту 6080 (пароль: youvncpassword)
- **Own browser support:** BROWSER_PATH + BROWSER_USER_DATA
- **Entrypoints:** [webui.py](https://github.com/browser-use/web-ui/blob/main/webui.py)

### 🧪 Примеры задач
- Визуальный мониторинг browser-use агента через VNC
- Отладка web automation с real-time browser view
- Использование своих cookies для authenticated scraping
- Демонстрация AI browser agent клиентам/команде
- Тестирование browser tasks перед production deployment

### ⚠️ Ограничения
- Chrome не должен быть открыт при использовании own browser
- VNC password по умолчанию слабый (youvncpassword)
- Playwright install нужен для browsers
- Python 3.11+ required
- Gradio UI может быть медленнее чем CLI

### 🧭 Fit / Maturity / Ops
- **Fit:** GUI для browser-use, debugging, демонстрации
- **Maturity:** active (часть browser-use ecosystem)
- **Latency/Cost:** balanced (Gradio + browser overhead)
- **Data constraints:** LLM API key, optional own browser profile
- **Ops friction:** low (Docker или Python install)

### Full links
- Repo: https://github.com/amibars/web-ui
- Original README: https://github.com/browser-use/web-ui/blob/main/README.md
- Docs: https://docs.browser-use.com/quickstart
- VNC: порт 6080 (default password: youvncpassword)

---

## ZerePy

**TL;DR:** ZerePy — open-source Python framework для деплоя AI агентов на Twitter/X и других платформах. Модульная архитектура: LLMs (OpenAI, Anthropic, Ollama, Galadriel, XAI/Grok), socials (X, Farcaster, Echochambers, Discord), onchain (Solana, EVM, GOAT, Monad). Построен на Zerebro backend. Fine-tuning нужен для creative outputs.

### Быстрый выбор
- ✅ Используй если:
  - Хочешь AI агента для Twitter/X
  - Нужна интеграция с Solana/EVM через GOAT
  - Используешь OpenAI, Anthropic или Ollama
  - Нужен агент для Farcaster или Discord
  - Хочешь CLI для управления агентами
- ❌ Не используй если:
  - Не нужны социальные сети
  - Нужен только web automation (используй browser-use)
  - X API platform fee ($100+/month) не подходит
  - Нужны creative outputs без fine-tuning

### 🚀 Запуск
```bash
# Быстрый старт через Replit:
# https://replit.com/@blormdev/ZerePy?v=1

# Или локально:
git clone https://github.com/blorm-network/ZerePy.git && cd zerepy
poetry install --no-root
poetry shell
poetry run python main.py

# CLI configuration:
configure-connection twitter
configure-connection openai
load-agent example
start
```

### 🧩 Архитектура
- **CLI interface:** manage connections, agents, start/stop
- **Modular connections:** twitter, farcaster, echochambers, discord, solana, ethereum, goat
- **LLMs:** OpenAI, Anthropic, EternalAI, Ollama, Hyperbolic, Galadriel, XAI (Grok)
- **GOAT integration:** ERC20 tokens, market data, multi-chain wallets
- **Solana:** SOL/SPL transfers, Jupiter swaps, staking, TPS monitoring
- **EVM:** ETH/ERC-20 transfers, Kyberswap
- **Socials:** tweet, reply, like, post casts, react
- **Entrypoints:** [main.py](https://github.com/blorm-network/ZerePy/blob/main/main.py), [agents/](https://github.com/blorm-network/ZerePy/tree/main/agents)

### 🧪 Примеры задач
- AI агент постит tweets и replies
- Мониторинг Farcaster и auto-replies
- Discord bot с LLM responses
- Onchain действия через GOAT (swaps, transfers)
- Cross-platform agent (X + Discord + onchain)

### ⚠️ Ограничения
- X API ключи платные ($100+/month)
- Poetry required
- Fine-tuning модели нужен для creative outputs
- Private keys для onchain actions
- Python 3.10+

### 🧭 Fit / Maturity / Ops
- **Fit:** Social media AI agents, onchain automation
- **Maturity:** active (29 contributors, Zerebro-based)
- **Latency/Cost:** balanced (LLM costs + X API fees)
- **Data constraints:** X API key, wallet private keys
- **Ops friction:** medium (Poetry setup, API keys)

### Full links
- Repo: https://github.com/amibars/ZerePy
- Original README: https://github.com/blorm-network/ZerePy/blob/main/README.md
- Replit: https://replit.com/@blormdev/ZerePy?v=1
- Maturity: active

---

## rig

**TL;DR:** Rig — Rust библиотека для LLM-powered приложений с минимальным boilerplate. 20+ LLM providers (OpenAI, Anthropic, Google, Cohere, и др.), 10+ vector stores (LanceDB, MongoDB, Qdrant, Neo4j, SQLite), multi-turn streaming, agentic workflows с RAG. Full WASM compatibility. Используется в Listen, Coral Protocol, Neon, Helius.

### Быстрый выбор
- ✅ Используй если:
  - Пишешь на Rust и нужна LLM интеграция
  - Хочешь минимальный boilerplate
  - Нужен unified interface для разных LLM providers
  - Нужна совместимость с WASM
  - Building high-performance LLM apps
- ❌ Не используй если:
  - Python/TS project (используй LangChain)
  - Не знаешь Rust
  - Нужен stable API (могут быть breaking changes)
  - Quick prototyping (сложнее чем Python)

### 🚀 Запуск
```bash
# Add to Cargo.toml
cargo add rig-core
# Или с vector store:
cargo add rig-lancedb
```
```rust
use rig::providers::openai;
use rig::completion::Prompt;

#[tokio::main]
async fn main() -> Result<(), anyhow::Error> {
    let client = openai::Client::from_env();
    let agent = client.agent(openai::GPT_4O)
        .preamble("You are a helpful assistant.")
        .build();
    let response = agent.prompt("Hello!").await?;
    println!("{}", response);
    Ok(())
}
```

### 🧩 Архитектура
- **rig-core:** основной пакет (agents, prompts, completions, embeddings)
- **Providers:** OpenAI, Anthropic, Mistral, Cohere, Google Gemini, DeepSeek, Perplexity, xAI
- **Vector stores:** rig-lancedb, rig-mongodb, rig-neo4j, rig-qdrant, rig-sqlite, rig-pinecone
- **RAG:** document loaders, chunking, retrieval
- **GenAI Semantic Convention** compatible
- **Streaming:** multi-turn с async iterators
- **Entrypoints:** [rig-core/src/](https://github.com/0xPlaygrounds/rig/tree/main/rig-core/src), [examples/](https://github.com/0xPlaygrounds/rig/tree/main/rig-core/examples)

### 🧪 Примеры задач
- RAG pipeline с LanceDB/MongoDB
- Multi-agent conversations
- Streaming chat completions
- WASM-based LLM apps
- High-performance AI services

### ⚠️ Ограничения
- Breaking changes expected (warning: here be dragons)
- tokio `macros` and `rt-multi-thread` features needed
- Rust знания required
- Меньше документации чем Python библиотеки
- Compile times могут быть долгими

### 🧭 Fit / Maturity / Ops
- **Fit:** Rust LLM apps, high-performance AI, WASM
- **Maturity:** active (используется в production: Listen, Coral, Helius)
- **Latency/Cost:** quality (Rust performance)
- **Data constraints:** LLM API keys
- **Ops friction:** medium (Rust toolchain, compile times)

### Full links
- Repo: https://github.com/amibars/rig
- Original README: https://github.com/0xPlaygrounds/rig/blob/main/README.md
- Docs: https://docs.rig.rs
- API Reference: https://docs.rs/rig-core
- Discord: https://discord.gg/playgrounds
- Maturity: active

## pyspur

**TL;DR:** PySpur — визуальный playground для построения и отладки agentic workflows. Решает три боли AI-инженеров: prompt hell (бесконечные tweaking), workflow blindspots (невидимые failures между шагами), и terminal testing nightmare (парсинг JSON вручную). Human-in-the-loop breakpoints, multimodal support (PDF, video, audio, images), 100+ LLM провайдеров, встроенный RAG pipeline. One-click deploy как API.

### Быстрый выбор
- ✅ Используй если:
  - Хочешь визуально строить и дебажить LLM pipelines
  - Нужны human-in-the-loop approvals (breakpoints)
  - Работаешь с multimodal data (PDF, video, audio)
  - Нужен RAG pipeline (parse, chunk, embed, upsert)
  - Хочешь traces и evals для debugging
  - Нужен one-click deploy как API
- ❌ Не используй если:
  - CLI-only workflows без визуализации
  - Нужен только code-first approach (используй LangChain)
  - Нет Python 3.11+

### 🚀 Запуск
```bash
# Быстрый старт через pip
pip install pyspur
pyspur init my-project && cd my-project
pyspur serve --sqlite
# http://localhost:6080

# Или Docker:
git clone https://github.com/PySpur-com/pyspur.git && cd pyspur
cp .env.example .env
docker compose up --build -d
```

### 🧩 Архитектура
- **Visual Canvas:** drag-and-drop nodes, real-time execution
- **Nodes:** LLM calls, tools (Slack, Firecrawl, GitHub, Google Sheets), conditionals, loops
- **RAG:** built-in parse → chunk → embed → upsert pipeline
- **Human-in-the-loop:** breakpoints pause workflow for approval
- **Traces:** automatic execution logs for debugging
- **Deploy:** publish as API endpoint
- **Entrypoints:** [pyspur/](https://github.com/PySpur-Dev/pyspur/tree/main/pyspur)

### 🧪 Примеры задач
- Build document Q&A pipeline с RAG
- Automate Slack notifications based on LLM analysis
- Scrape website с Firecrawl → summarize → post to GitHub
- Human review step перед отправкой email
- Multimodal: extract text from PDF → analyze → generate report

### ⚠️ Ограничения
- Python 3.11+ required
- SQLite для quick start, recommended Postgres для production
- Self-hosted only (no cloud version)
- API keys нужны для LLM providers
- Memory usage grows с complex workflows

### 🧭 Fit / Maturity / Ops
- **Fit:** Visual LLM workflows, RAG pipelines, human-in-the-loop
- **Maturity:** active (40+ releases, growing community)
- **Latency/Cost:** balanced (depends on LLM provider)
- **Data constraints:** LLM API keys, optional Postgres
- **Ops friction:** low (pip install или Docker)

### Full links
- Repo: https://github.com/amibars/pyspur
- Original README: https://github.com/PySpur-Dev/pyspur/blob/main/README.md
- Stars: 13,500+
- Maturity: active

---

## exo

**TL;DR:** exo — запуск AI кластера на обычных устройствах дома. Объединяет все устройства (Mac, PC, даже телефоны) в единый inference cluster. Day-0 support для RDMA over Thunderbolt 5 с 99% reduction latency между устройствами. Automatic device discovery — ноды находят друг друга без конфигурации. Tensor parallelism даёт 1.8x speedup на 2 devices, 3.2x на 4 devices. OpenAI-compatible API. Jeff Geerling запустил 15TB VRAM на Mac Studio кластере.

### Быстрый выбор
- ✅ Используй если:
  - Хочешь запускать большие модели (DeepSeek v3, Kimi-K2) на нескольких устройствах
  - Есть несколько Mac с Apple Silicon (особенно Thunderbolt 5)
  - Нужен P2P inference без master-worker архитектуры
  - Хочешь OpenAI-compatible API для своего кластера
  - Нужен built-in dashboard для управления
- ❌ Не используй если:
  - Один GPU достаточен для модели
  - Linux production (GPU support в разработке)
  - Нужен cloud-hosted solution
  - Нет macOS устройств (best support на Apple Silicon)

### 🚀 Запуск
```bash
# macOS prerequisites
brew install uv macmon node
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
rustup toolchain install nightly

# Clone and run
git clone https://github.com/exo-explore/exo
cd exo/dashboard && npm install && npm run build && cd ..
uv run exo
# Dashboard: http://localhost:52415
```

### 🧩 Архитектура
- **Automatic Discovery:** devices find each other без конфигурации
- **RDMA over Thunderbolt 5:** 99% latency reduction между devices
- **Topology-Aware Parallelism:** автоматический split модели based on device resources и network latency
- **Tensor Parallelism:** sharding моделей для speedup
- **MLX backend:** inference через Apple MLX, MLX distributed для communication
- **Dashboard:** built-in UI на http://localhost:52415
- **API:** OpenAI-compatible /v1/chat/completions
- **Entrypoints:** [src/exo/](https://github.com/exo-explore/exo/tree/main/src/exo), [docs/api.md](https://github.com/exo-explore/exo/blob/main/docs/api.md)

### 🧪 Примеры задач
- 4× 512GB M3 Ultra Mac Studio → DeepSeek v3.1 (8-bit) + Kimi-K2-Thinking
- `curl http://localhost:52415/v1/chat/completions` — OpenAI-style request
- `curl http://localhost:52415/models` — list available models
- `uv run bench/exo_bench.py --model Llama-3.2-1B-Instruct-4bit` — benchmark
- 15TB VRAM cluster (Jeff Geerling's setup)

### ⚠️ Ограничения
- macOS: GPU support, Linux: CPU only (GPU в разработке)
- Rust nightly required для build
- Node.js needed для dashboard build
- macmon нужен для hardware monitoring на Apple Silicon
- Breaking changes возможны (active development)

### 🧭 Fit / Maturity / Ops
- **Fit:** Home AI clusters, large model inference across devices
- **Maturity:** active (11+ releases, 74 contributors)
- **Latency/Cost:** quality (optimized for throughput, not latency)
- **Data constraints:** local devices, no cloud dependency
- **Ops friction:** medium (requires build от source на macOS)

### Full links
- Repo: https://github.com/amibars/exo
- Original README: https://github.com/exo-explore/exo/blob/main/README.md
- Docs: https://github.com/exo-explore/exo/blob/main/docs/api.md
- Company: https://exolabs.net
- Stars: 30,000+
- Maturity: active

---

## agentipy

**TL;DR:** Python-версия Solana Agent Kit. Подключает AI агентов к Solana: token operations, Jupiter swaps, Raydium/Orca liquidity, Pump.fun launches, yield farming. LangChain-совместим. Один пакет для всех DeFi операций на Python.

### Быстрый выбор
- ✅ Используй если:
  - Пишешь на Python и нужен AI агент для Solana
  - Нужны Jupiter swaps, Pump.fun launches
  - Интегрируешься с LangChain
  - Хочешь yield farming automation
  - Нужны Raydium/Orca liquidity operations
- ❌ Не используй если:
  - Проект на TypeScript (используй solana-agent-kit)
  - Нужны EVM chains (используй goat)
  - Не нужен AI, только SDK (solana-py)
  - Production с high-value funds (проверь матурность)

### 🚀 Запуск
```bash
pip install agentipy
```
```python
from agentipy import SolanaAgentKit

agent = SolanaAgentKit(
    private_key="your-private-key",
    rpc_url="https://api.mainnet-beta.solana.com"
)

# Jupiter swap
result = agent.swap(
    token_in="SOL",
    token_out="USDC",
    amount=1.0
)

# Pump.fun launch
launch = agent.pump_fun_launch(
    name="MyToken",
    symbol="MTK"
)
```

### 🧩 Архитектура
- **Core:** Python SDK для Solana actions
- **DeFi:** Jupiter, Raydium, Orca, Pump.fun
- **LangChain tools:** готовые tools для AI агентов
- **Tokens:** transfer, mint, burn operations
- **NFTs:** Metaplex integration (TODO: verify)
- **Yield:** farming automation
- **Entrypoints:** [agentipy](https://pypi.org/project/agentipy/) package

### 🧪 Примеры задач
- Jupiter swap SOL → USDC
- Launch token на Pump.fun
- Pool creation на Raydium
- Yield farming автоматизация
- LangChain agent с Solana tools

### ⚠️ Ограничения
- Private key нужен в plaintext
- Меньше features чем в TypeScript версии
- Mainnet by default (внимательно с тестированием)
- RPC rate limits
- Slippage settings critical

### 🧭 Fit / Maturity / Ops
- **Fit:** Python Solana AI agents, DeFi automation
- **Maturity:** active (Python port of official kit)
- **Latency/Cost:** fast (Solana native)
- **Data constraints:** private key, RPC endpoint
- **Ops friction:** low (pip install)

### Full links
- Repo: https://github.com/amibars/agentipy
- Original README: https://github.com/sendaifun/agentipy/blob/main/README.md
- PyPI: https://pypi.org/project/agentipy/
- Maturity: active

---

## swarmnode-python

**TL;DR:** Python SDK для SwarmNode — платформы serverless AI agents в облаке. Deploy AI агентов без управления инфраструктурой. Cron jobs для scheduled executions, streaming responses, async orchestration. Идеально для тех, кто не хочет заморачиваться с серверами.

### Быстрый выбор
- ✅ Используй если:
  - Нужен serverless hosting для AI агентов
  - Хочешь cron jobs для scheduled tasks
  - Нужен streaming responses
  - Не хочешь управлять инфраструктурой
  - Простой SDK для быстрого запуска
- ❌ Не используй если:
  - Нужен self-hosted only
  - Не хочешь платить за cloud
  - Нужен полный контроль над execution
  - Критична latency (облако добавляет overhead)

### 🚀 Запуск
```bash
pip install swarmnode
```
```python
from swarmnode import Agent, SwarmNode

# Initialize client
client = SwarmNode(api_key="your-api-key")

# Create and run agent
agent = Agent(
    name="my-agent",
    instructions="You are a helpful assistant"
)
result = client.run(agent, task="Summarize this document")
```

### 🧩 Архитектура
- **Serverless:** no infrastructure management
- **Agents:** define через Python SDK
- **Cron jobs:** scheduled executions
- **Streaming:** real-time responses
- **Async:** parallel agent orchestration
- **API:** RESTful с Python SDK wrapper
- **Entrypoints:** [swarmnode](https://pypi.org/project/swarmnode/) package

### 🧪 Примеры задач
- Deploy document processing agent
- Scheduled data analysis (cron)
- Multi-agent pipelines с orchestration
- Streaming chat responses
- Background task execution

### ⚠️ Ограничения
- Требует SwarmNode API key (платный сервис)
- Cloud-only (нет self-hosted)
- Latency overhead from cloud
- Pricing зависит от usage
- Limited customization vs self-hosted

### 🧭 Fit / Maturity / Ops
- **Fit:** Serverless AI agents, scheduled tasks, no-ops
- **Maturity:** active (managed service)
- **Latency/Cost:** balanced (cloud overhead + pay-per-use)
- **Data constraints:** SwarmNode API key, cloud data processing
- **Ops friction:** low (pip install, API key)

### Full links
- Repo: https://github.com/amibars/swarmnode-python
- Original README: https://github.com/swarmnode-ai/swarmnode-python/blob/main/README.md
- PyPI: https://pypi.org/project/swarmnode/
- Platform: https://swarmnode.ai/
- Maturity: active
- **Serverless:** agents запускаются в cloud
- **Cron:** scheduled execution
- **Streaming:** real-time responses
- **Python SDK:** type definitions included

### ⚠️ Ограничения
- Requires SwarmNode API key
- Cloud-only (no self-hosted option)
- Pricing unknown

### Full links
- Repo: https://github.com/amibars/swarmnode-python
- Maturity: active

---

## cdp-agentkit-nodejs

**TL;DR:** Coinbase Developer Platform AgentKit для Node.js. AI агенты для Base/EVM: deploy tokens, mint NFTs, Zora Wow, Basenames. LangChain.js + Twitter integration.

### Быстрый выбор
- ✅ Используй если:
  - Работаешь с Base chain
  - Нужен Coinbase Wallet integration
  - Хочешь deploy ERC-20/ERC-721
  - Нужна Twitter integration для AI агента
- ❌ Не используй если:
  - Non-Base chains (используй goat)
  - Python project (используй goat-sdk)
  - Не нужен Coinbase ecosystem

### 🚀 Запуск
```bash
npm install @coinbase/cdp-agentkit-core @coinbase/langchain
```
```typescript
import { CdpAgentkit } from "@coinbase/cdp-agentkit-core";
const agentkit = await CdpAgentkit.configureWithWallet();
```

### 🧩 Архитектура
- **Core:** @coinbase/cdp-agentkit-core
- **LangChain:** @coinbase/langchain для AI integration
- **Twitter:** @coinbase/twitter-langchain
- **Actions:** deploy tokens, mint NFTs, transfer, faucet
- **Entrypoints:** packages/

### 🧪 Примеры задач
- Deploy ERC-20 token on Base
- Mint NFT collection
- Register Basenames (.base domain)
- Zora Wow coin creation
- Twitter posting from agent

### ⚠️ Ограничения
- Base chain focused (для multi-chain используй goat)
- Requires CDP API key от Coinbase Developer Portal
- Node.js only (нет Python SDK)
- MFA required для CDP аккаунта
- Twitter API keys нужны отдельно для @coinbase/twitter-langchain

### 🧭 Fit / Maturity / Ops
- **Fit:** Base chain AI agents, NFT minting, token deployment, Coinbase ecosystem
- **Maturity:** active (official Coinbase SDK, production-ready)
- **Latency/Cost:** balanced (Base L2 fees low, CDP API limits apply)
- **Data constraints:** CDP API key, wallet private key, optional Twitter API
- **Ops friction:** low (npm install, API key setup)

### Full links
- Repo: https://github.com/amibars/cdp-agentkit-nodejs
- Original README: https://github.com/coinbase/cdp-agentkit/blob/main/README.md
- Docs: https://docs.cdp.coinbase.com/agentkit
- CDP Portal: https://portal.cdp.coinbase.com
- Maturity: active

---

## axium

**TL;DR:** Axium — AI crypto trading agent framework для Solana DEX. Semi-automated trading на Pumpfun и Raydium с AI-driven market analysis. Customizable trading strategies, real-time signal detection, sentiment analysis. Docker containerized deployment. Важно: experimental project, не для production с real funds без тщательного тестирования.

### Быстрый выбор
- ✅ Используй если:
  - Хочешь AI trading бота для Pumpfun/Raydium
  - Нужен semi-automated trading с AI analysis
  - Хочешь custom trading strategies
  - Нужен sentiment analysis для tokens
  - Используешь Docker для deployment
- ❌ Не используй если:
  - Другие DEX кроме Pumpfun/Raydium
  - Fully manual trading preferred
  - Production с real funds (без тестирования)
  - Нужна proven stability

### 🚀 Запуск
```bash
# Docker deployment
git clone https://github.com/cswenor/axium && cd axium
cp .env.example .env
# Заполни wallet private key и RPC
docker compose up

# Или напрямую:
npm install && npm run dev
```

### 🧩 Архитектура
- **Trading Engine:** Pumpfun + Raydium integration
- **AI Analysis:** market sentiment, signal detection, trend analysis
- **Strategies:** customizable trading rules
- **Docker:** containerized, easy deployment
- **CLI:** agent management interface
- **Entrypoints:** config files, strategy definitions

### 🧪 Примеры задач
- Monitor new tokens on Pumpfun
- Execute trades based on AI signals
- Track portfolio performance
- Set stop-loss и take-profit rules
- Sentiment-based entry/exit points

### ⚠️ Ограничения
- Experimental — не для production с real funds
- Ограничен Pumpfun и Raydium
- Требует настройки strategies
- Private key нужен в .env
- No backtesting framework

### 🧭 Fit / Maturity / Ops
- **Fit:** Solana DEX trading, AI-assisted decisions
- **Maturity:** experimental (use with caution)
- **Latency/Cost:** fast (Solana native)
- **Data constraints:** wallet private key, RPC endpoint
- **Ops friction:** medium (Docker или Node.js, strategy config)

### Full links
- Repo: https://github.com/amibars/axium
- Original README: https://github.com/cswenor/axium/blob/main/README.md
- Maturity: experimental

---

## openagent

**TL;DR:** OpenAgent — платформа для создания, сражения и торговли AI агентами на Solana blockchain. Multi-agent AI platform с GPT-4 powered agents, WebSocket real-time communication, decentralized token economy. Frontend на React/TypeScript, backend на Node.js/Express, PostgreSQL датабаза. Wallet authentication через Solana, customizable agent behaviors.

### Быстрый выбор
- ✅ Используй если:
  - Хочешь AI agent battles/competitions
  - Интересует AI + token economy
  - Нужна multi-agent платформа на Solana
  - Хочешь создавать customizable AI agents
  - Нужен real-time WebSocket communication
- ❌ Не используй если:
  - Non-Solana chains
  - Single-agent use case
  - Production-ready решение (experimental)
  - Не хочешь разворачивать PostgreSQL

### 🚀 Запуск
```bash
git clone https://github.com/openagentoa/openagent && cd openagent
npm install

# Configure .env
cp .env.example .env
# DATABASE_URL=postgresql://user:password@localhost:5432/openagent
# OPENAI_API_KEY=your_api_key
# SOLANA_RPC_URL=your_solana_rpc_url

npm run db:push
npm run dev
# http://localhost:5000
```

### 🧩 Архитектура
```
openagent/
├── client/     # Frontend React + TypeScript
├── server/     # Backend Node.js + Express
├── db/         # PostgreSQL schemas and migrations
├── contracts/  # Solana smart contracts
└── docs/       # Documentation
```
- **AI:** OpenAI GPT-4 powered agents
- **Real-Time:** WebSocket для instant messaging
- **Blockchain:** Solana integration
- **Economy:** Token-based rewards
- **Styling:** Tailwind CSS + shadcn/ui

### 🧪 Примеры задач
- Создание нового AI агента с custom parameters
- Agent battles/competitions между пользователями
- Trading агентами через token economy
- Real-time discussions между agents
- Wallet authentication через Solana

### ⚠️ Ограничения
- Experimental project
- Solana-only blockchain
- Требует PostgreSQL setup
- OpenAI API key нужен
- Limited documentation

### 🧭 Fit / Maturity / Ops
- **Fit:** AI agent competitions, Web3 gaming, token economy
- **Maturity:** experimental (MIT license)
- **Latency/Cost:** balanced (WebSocket + OpenAI costs)
- **Data constraints:** OpenAI key, Solana RPC, PostgreSQL
- **Ops friction:** medium (requires DB и wallet setup)

### Full links
- Repo: https://github.com/amibars/openagent
- Original README: https://github.com/openagentoa/openagent/blob/main/README.md
- Website: https://openagentoa.com
- Twitter: https://x.com/OpenAgentOA
- Maturity: experimental

---

## sentience

**TL;DR:** Sentience от Galadriel — SDK для создания unruggable AI агентов с cryptographically verifiable inference. AI агенты достигли $10B+ market cap, но большинство контролируется людьми (риск rug-pull). Sentience использует TEE (Amazon Nitro Enclaves) для secure LLM inference, cryptographic attestations постятся на Solana blockchain. Уже защищает $15M+ worth of agents (Daige AI dog и другие).

### Быстрый выбор
- ✅ Используй если:
  - Нужен verifiable AI inference
  - Хочешь proofs on-chain (Solana)
  - Критична trust/transparency для инвесторов
  - Building AI agent с token (anti-rug)
  - Хочешь proof terminal как у Daige
- ❌ Не используй если:
  - Quick prototyping (добавляет overhead)
  - Не нужен on-chain verification
  - Non-Solana blockchain preferred
  - Simple agent без trust requirements

### 🚀 Запуск
```bash
# Install Python SDK
pip install sentience

# Get free API key: https://dashboard.galadriel.com/
```
```python
import sentience
from openai import OpenAI

client = OpenAI(
    base_url="https://api.galadriel.com/v1/verified",
    api_key="Bearer GALADRIEL_API_KEY",
)

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}],
)

is_valid = sentience.verify_signature(completion)
print("Verified:", is_valid)
```

### 🧩 Архитектура
```
Agent → TEE (Amazon Nitro Enclaves) → LLM API
           ↓
      {Message, Proof} → Solana blockchain
           ↓
      Proof of Sentience SDK → Verify attestation
```
- **TEE:** Amazon Nitro Enclaves для isolated execution
- **Proofs:** cryptographic attestations на Solana
- **SDK:** Python и JavaScript
- **LLMs:** OpenAI, Claude, fine-tuned models
- **Frameworks:** compatible с ELIZA, ARC, Zerebro
- **Explorer:** https://explorer.galadriel.com/
- **Entrypoints:** [sdk/python/](https://github.com/galadriel-ai/sentience/tree/main/sdk/python), [verified-inference/](https://github.com/galadriel-ai/sentience/tree/main/verified-inference)

### 🧪 Примеры задач
- Daige AI dog ($15M+) — https://www.daige.ai/proof
- Proof terminal для agent website
- Verify LLM inference integrity
- Post attestation на Solana
- Compatible с existing frameworks (ELIZA, Zerebro)

### ⚠️ Ограничения
- Добавляет latency (TEE overhead)
- Solana-only для proofs
- Нужен Galadriel API key
- Enclave code нужно верифицировать
- SDK не для self-hosted TEE

### 🧭 Fit / Maturity / Ops
- **Fit:** Unruggable AI agents, verifiable inference, Web3 trust
- **Maturity:** active ($15M+ secured)
- **Latency/Cost:** balanced (TEE overhead + Solana fees)
- **Data constraints:** Galadriel API key, Solana for proofs
- **Ops friction:** low (SDK install, API key)

### Full links
- Repo: https://github.com/amibars/sentience
- Original README: https://github.com/galadriel-ai/Sentience/blob/main/README.md
- Docs: https://docs.galadriel.com
- Dashboard: https://dashboard.galadriel.com/
- Explorer: https://explorer.galadriel.com/
- Maturity: active

---

## devin.cursorrules

**TL;DR:** Превращает $20/month Cursor или Windsurf в $25/task Devin-like AI assistant. Добавляет automated planning, self-evolution (AI учится на ошибках), extended tools (web scraping Playwright, DuckDuckGo search, LLM analysis). Experimental multi-agent mode: o1 для planning, Claude/GPT-4o для execution. Поддерживает GitHub Copilot через .github/copilot-instructions.md.

### Быстрый выбор
- ✅ Используй если:
  - Используешь Cursor, Windsurf или GitHub Copilot
  - Хочешь autonomous AI coding с planning
  - Нужен web browsing (Playwright) из IDE
  - Хочешь self-evolution (AI запоминает ошибки)
  - Интересует multi-agent (o1 + Claude/GPT)
- ❌ Не используй если:
  - Не используешь Cursor/Windsurf/Copilot
  - Нужен standalone agent (вне IDE)
  - Простые задачи без planning
  - Не хочешь настраивать .cursorrules

### 🚀 Запуск
```bash
# Option 1: Cookiecutter (recommended)
pip install cookiecutter
cookiecutter gh:grapeot/devin.cursorrules --checkout template

# Option 2: Manual setup
# Cursor: копируй .cursorrules в project root
# Windsurf: нужны .windsurfrules и scratchpad.md
# Copilot: копируй .github/copilot-instructions.md
cp -r tools/ your-project/
```

### 🧩 Архитектура
- **.cursorrules:** system prompts → Devin-like planning behavior
- **.windsurfrules + scratchpad.md:** для Windsurf users
- **.github/copilot-instructions.md:** для GitHub Copilot
- **tools/:** web scraping (Playwright), search (DuckDuckGo), LLM analysis
- **Multi-agent (experimental):** o1 Planner + Claude/GPT Executor
- **Self-evolution:** AI обновляет lessons learned в .cursorrules
- **Entrypoints:** [tools/](https://github.com/grapeot/devin.cursorrules/tree/master/tools), [.cursorrules](https://github.com/grapeot/devin.cursorrules/blob/master/.cursorrules)

### 🧪 Примеры задач
- Autonomous data gathering с web browsing
- Cross-referencing external resources
- Building prototypes с iterative planning
- Self-correcting code development
- Multi-step research tasks с search + analysis

### ⚠️ Ограничения
- Требует Cursor ($20/month), Windsurf, или GitHub Copilot
- Нужна настройка под проект
- Playwright browsers install при первом использовании
- Multi-agent branch experimental
- Self-evolution требует доверия к AI edits

### 🧭 Fit / Maturity / Ops
- **Fit:** Autonomous IDE coding, planning, research tasks
- **Maturity:** active (14 contributors, MIT license)
- **Latency/Cost:** $20/month Cursor vs $25/task Devin
- **Data constraints:** Cursor/Windsurf subscription
- **Ops friction:** low (copy files, optional API keys)

### Full links
- Repo: https://github.com/amibars/devin.cursorrules
- Original README: https://github.com/grapeot/devin.cursorrules/blob/master/README.md
- Blog post: https://yage.ai/cursor-to-devin-en.html
- Tutorial: https://github.com/grapeot/devin.cursorrules/blob/master/step_by_step_tutorial.md
- Multi-agent branch: https://github.com/grapeot/devin.cursorrules/tree/multi-agent
- Maturity: active

---

## ds-top-traders

**TL;DR:** Скрейпинг top traders с Dexscreener по contract address. Автоматизация Chrome через Selenium с обходом captcha. Получаешь список wallet addresses топ-трейдеров для анализа smart money. Experimental — может сломаться при UI changes на Dexscreener.

### Быстрый выбор
- ✅ Используй если:
  - Нужен список top traders для token
  - Хочешь wallet addresses из Dexscreener
  - Анализируешь smart money
  - One-off scraping (не continuous)
  - Нет API access к Dexscreener
- ❌ Не используй если:
  - Real-time data (скрейпинг медленный)
  - API access есть (Dexscreener API отдельно)
  - Массовый скрейпинг (rate limits)
  - Production use (хрупкий скрипт)

### 🚀 Запуск
```bash
git clone https://github.com/amibars/ds-top-traders && cd ds-top-traders
pip install -r requirements.txt
# Заполни contract address в config
python main.py
```

### 🧩 Архитектура
- **Selenium:** Chrome automation (webdriver)
- **Captcha:** handling through automation
- **Input:** contract address
- **Output:** wallet addresses list
- **Entrypoints:** main.py, config.py

### 🧪 Примеры задач
- Получить top holders для нового token
- Отслеживание smart money входов
- Copy-trading research
- Whale watching для конкретного token
- Сбор альфы по wallets

### ⚠️ Ограничения
- Медленный (browser automation)
- Может сломаться при UI changes
- Rate limits от Dexscreener
- Требует Chrome + ChromeDriver
- Captcha может блокировать

### 🧭 Fit / Maturity / Ops
- **Fit:** One-off smart money research, wallet discovery
- **Maturity:** experimental (scraper, fragile)
- **Latency/Cost:** slow (browser automation)
- **Data constraints:** Dexscreener access
- **Ops friction:** medium (Chrome + dependencies)

### Full links
- Repo: https://github.com/amibars/ds-top-traders
- Original README: https://github.com/amibars/ds-top-traders/blob/main/README.md
- Maturity: experimental

---

## solana-wallet-checker

**TL;DR:** Mass scanning Solana wallets через GMGN API. Batch analysis для списка кошельков — PNL, winrate, transaction history. Собираешь wallet list из ds-top-traders или других источников, затем прогоняешь через GMGN API. Experimental инструмент для smart money research.

### Быстрый выбор
- ✅ Используй если:
  - Нужен batch analysis кошельков
  - Проверяешь multiple wallets
  - Ищешь profitable wallets
  - Уже есть список addresses
  - Нужна статистика PNL/winrate
- ❌ Не используй если:
  - Single wallet (используй GMGN напрямую)
  - Real-time monitoring
  - Массовый скрейпинг (GMGN limits)
  - EVM chains (только Solana)

### 🚀 Запуск
```bash
git clone https://github.com/amibars/solana-wallet-checker && cd solana-wallet-checker
pip install -r requirements.txt
# Заполни list.txt с wallet addresses
# Set TARGET_VERSION в config
python main.py
```

### 🧩 Архитектура
- **Input:** list.txt с адресами
- **API:** GMGN.ai для wallet stats
- **Output:** PNL, winrate, transaction data
- **Batch:** последовательная обработка
- **Entrypoints:** main.py, list.txt

### 🧪 Примеры задач
- Проверка 100 кошельков из ds-top-traders
- Фильтрация по winrate > 60%
- Поиск profitable wallets для copy-trading
- Сравнение производительности wallets
- Smart money alpha discovery

### ⚠️ Ограничения
- GMGN API rate limits
- Batch-only, не real-time
- Solana-only
- Зависит от GMGN API доступности
- Медленный для больших списков

### 🧭 Fit / Maturity / Ops
- **Fit:** Batch wallet analysis, smart money research
- **Maturity:** experimental (simple script)
- **Latency/Cost:** slow (batch, rate limited)
- **Data constraints:** GMGN API access
- **Ops friction:** low (pip install, wallet list)

### Full links
- Repo: https://github.com/amibars/solana-wallet-checker
- Original README: https://github.com/amibars/solana-wallet-checker/blob/main/README.md
- Maturity: experimental

---

## gmgn-scraper

**TL;DR:** Node.js scraper для GMGN.ai платформы. Автоматизирует извлечение данных о токенах, кошельках и трейдах. Работает напрямую с GMGN без official API. Experimental — может сломаться при изменениях на сайте.

### Быстрый выбор
- ✅ Используй если:
  - Нужны данные с GMGN.ai программно
  - Хочешь автоматизировать data extraction
  - Нет доступа к official API
  - Batch data collection
  - Research и analytics
- ❌ Не используй если:
  - Real-time trading (слишком медленно)
  - Нужен official API (scraping fragile)
  - Massive scale (rate limits)
  - Production systems (может сломаться)

### 🚀 Запуск
```bash
git clone https://github.com/amibars/gmgn-scraper && cd gmgn-scraper
pnpm install
# Configure targets
node index.js
```

### 🧩 Архитектура
- **Runtime:** Node.js ≥ v18.20.3
- **Scraping:** HTTP requests + parsing
- **Output:** JSON/CSV data
- **Entrypoints:** index.js

### 🧪 Примеры задач
- Сбор данных о топ токенах
- Wallet activity history
- Trade data extraction
- Market research automation
- Alpha discovery

### ⚠️ Ограничения
- Requires Node.js ≥ v18.20.3
- Scraping может сломаться при UI changes
- Rate limits от GMGN
- Нет real-time
- Fragile по определению

### 🧭 Fit / Maturity / Ops
- **Fit:** GMGN data extraction, research
- **Maturity:** experimental (scraper)
- **Latency/Cost:** slow (HTTP scraping)
- **Data constraints:** GMGN availability
- **Ops friction:** low (pnpm install)

### Full links
- Repo: https://github.com/amibars/gmgn-scraper
- Original README: https://github.com/amibars/gmgn-scraper/blob/main/README.md
- Maturity: experimental

---

## gmgn-api

**TL;DR:** Python wrapper для GMGN.ai API. Упрощает доступ к данным о токенах, кошельках, трейдах. Cleaner interface чем raw scraping. Идеально для Python проектов где нужны GMGN данные без возни с HTTP.

### Быстрый выбор
- ✅ Используй если:
  - Python проект с GMGN интеграцией
  - Хочешь clean API вместо raw scraping
  - Нужны wallet/token данные
  - Research и analytics
  - Быстрый prototyping
- ❌ Не используй если:
  - Full scraping с custom logic (используй gmgn-scraper)
  - Real-time data (not designed for it)
  - Node.js проект
  - Massive scale

### 🚀 Запуск
```bash
pip install gmgn-api  # or clone repo
```
```python
from gmgn import GMGN

client = GMGN()
token_data = client.get_token("token_address")
wallet_stats = client.get_wallet("wallet_address")
```

### 🧩 Архитектура
- **Core:** Python SDK wrapper
- **Endpoints:** tokens, wallets, trades
- **Output:** Python dicts/objects
- **Entrypoints:** gmgn package

### 🧪 Примеры задач
- Get token metadata
- Wallet PNL/winrate lookup
- Trade history retrieval
- Integration с trading bots
- Analytics pipelines

### ⚠️ Ограничения
- Depends on GMGN availability
- Rate limits apply
- Unofficial wrapper
- May break with GMGN changes
- Limited documentation

### 🧭 Fit / Maturity / Ops
- **Fit:** Python GMGN integration, research
- **Maturity:** unknown (community wrapper)
- **Latency/Cost:** medium (API calls)
- **Data constraints:** GMGN access
- **Ops friction:** low (pip install)

### Full links
- Repo: https://github.com/amibars/gmgn-api
- Original README: https://github.com/amibars/gmgn-api/blob/main/README.md
- Maturity: unknown

---

## gmgn_parser

**TL;DR:** Parser для данных с GMGN.ai. Преобразует raw GMGN responses в структурированные данные. Используй в связке с gmgn-scraper или gmgn-api для processing извлечённых данных. Utility library для GMGN data pipelines.

### Быстрый выбор
- ✅ Используй если:
  - Обрабатываешь GMGN data
  - Нужен structured output
  - Используешь gmgn-scraper/api
  - Data transformation pipelines
  - Clean data for analytics
- ❌ Не используй если:
  - Data extraction (используй gmgn-scraper)
  - API calls (используй gmgn-api)
  - Non-GMGN data sources
  - Real-time processing

### 🚀 Запуск
```bash
git clone https://github.com/amibars/gmgn_parser && cd gmgn_parser
pip install -r requirements.txt
# Используй как library:
from parser import parse_token_data, parse_wallet_data
```

### 🧩 Архитектура
- **Input:** Raw GMGN data (JSON)
- **Output:** Parsed, structured data
- **Functions:** parse_token, parse_wallet, parse_trades
- **Entrypoints:** parser.py

### 🧪 Примеры задач
- Parse token metadata
- Extract wallet stats
- Transform trade history
- Clean data for ML
- Normalize GMGN responses

### ⚠️ Ограничения
- Зависит от GMGN data format
- Может сломаться при API changes
- Limited documentation
- Python only
- Utility, не standalone

### 🧭 Fit / Maturity / Ops
- **Fit:** GMGN data processing, ETL pipelines
- **Maturity:** unknown (utility script)
- **Latency/Cost:** fast (local parsing)
- **Data constraints:** GMGN format dependency
- **Ops friction:** low (pip install)

### Full links
- Repo: https://github.com/amibars/gmgn_parser
- Original README: https://github.com/amibars/gmgn_parser/blob/main/README.md
- Maturity: unknown

---

## gmgn-scripts

**TL;DR:** Utility scripts для GMGN.AI платформы. Коллекция готовых скриптов для типичных задач: batch analysis, filtering, alerts. Используй если не хочешь писать с нуля. Experimental — проверь что работает.

### Быстрый выбор
- ✅ Используй если:
  - Нужны готовые GMGN скрипты
  - Batch processing задачи
  - Хочешь быстрый старт
  - Filtering и alerts
  - Research automation
- ❌ Не используй если:
  - Custom logic (пиши свои)
  - API wrapper (используй gmgn-api)
  - Scraping (используй gmgn-scraper)
  - Production systems

### 🚀 Запуск
```bash
git clone https://github.com/amibars/gmgn-scripts && cd gmgn-scripts
pip install -r requirements.txt
# Выбери нужный скрипт:
python script_name.py
```

### 🧩 Архитектура
- **Format:** Standalone Python scripts
- **Config:** per-script configuration
- **Output:** CSV/JSON/console
- **Entrypoints:** individual scripts

### 🧪 Примеры задач
- Batch wallet analysis
- Token filtering по criteria
- Alert на новые токены
- Daily reports
- Quick data exports

### ⚠️ Ограничения
- Experimental scripts
- Могут быть outdated
- Нет unified interface
- Rate limits apply
- Limited documentation

### 🧭 Fit / Maturity / Ops
- **Fit:** Quick GMGN automation, one-off tasks
- **Maturity:** experimental (scripts collection)
- **Latency/Cost:** varies by script
- **Data constraints:** GMGN access
- **Ops friction:** low (run script)

### Full links
- Repo: https://github.com/amibars/gmgn-scripts
- Original README: https://github.com/amibars/gmgn-scripts/blob/main/README.md
- Maturity: experimental

---

## gmgn_smart

**TL;DR:** Smart wallet analysis tools для GMGN. Анализ кошельков smart money: PNL, winrate, трейды, patterns. Фильтрация по profitable traders. Используй для wallet discovery и copy-trading research.

### Быстрый выбор
- ✅ Используй если:
  - Ищешь profitable wallets
  - Smart money analysis
  - Wallet discovery для copy-trading
  - PNL/winrate фильтрация
  - Trading patterns research
- ❌ Не используй если:
  - Token analysis (используй gmgn-api)
  - Raw scraping (используй gmgn-scraper)
  - Real-time alerts
  - Production systems

### 🚀 Запуск
```bash
git clone https://github.com/amibars/gmgn_smart && cd gmgn_smart
pip install -r requirements.txt
# Configure criteria
python main.py
```

### 🧩 Архитектура
- **Focus:** Smart wallet analysis
- **Metrics:** PNL, winrate, trade count
- **Filtering:** configurable thresholds
- **Output:** wallet lists, stats
- **Entrypoints:** main.py, config

### 🧪 Примеры задач
- Найти wallets с winrate > 70%
- Top PNL performers
- Copy-trading candidates
- Pattern analysis
- Whale watching

### ⚠️ Ограничения
- Зависит от GMGN data
- Rate limits
- Historical data онли
- Не real-time
- Ограниченная документация

### 🧭 Fit / Maturity / Ops
- **Fit:** Smart money research, wallet discovery
- **Maturity:** unknown (utility tools)
- **Latency/Cost:** medium (batch analysis)
- **Data constraints:** GMGN access
- **Ops friction:** low (pip install)

### Full links
- Repo: https://github.com/amibars/gmgn_smart
- Original README: https://github.com/amibars/gmgn_smart/blob/main/README.md
- Maturity: unknown

---

## woody-hub

**TL;DR:** Browser extension для GMGN. Auto-detects coins на странице, AI market analysis в один клик, built-in wallet для автоматических сделок. Enhanced GMGN experience без переключения между табами.

### Быстрый выбор
- ✅ Используй если:
  - Хочешь enhanced GMGN experience
  - AI analysis при просмотре токенов
  - Quick trading из extension
  - Авто-detect coins на страницах
  - Используешь GMGN регулярно
- ❌ Не используй если:
  - CLI tools only
  - Не используешь GMGN
  - Automated trading (woody для этого)
  - Firefox/Safari (Chrome only)

### 🚀 Запуск
```bash
git clone https://github.com/amibars/woody-hub && cd woody-hub
npm install && npm run build
# Chrome → Extensions → Developer mode → Load unpacked
# Выбери dist/ folder
```

### 🧩 Архитектура
- **Extension:** Chrome manifest v3
- **AI analysis:** auto-triggered on token pages
- **Wallet:** built-in for quick trades
- **Detection:** auto-detect token addresses
- **Entrypoints:** manifest.json, content scripts

### 🧪 Примеры задач
- AI analysis токена на GMGN
- Quick buy/sell из extension
- Auto-detect coins в tweets
- Market sentiment check
- One-click trading

### ⚠️ Ограничения
- Chrome only
- Требует GMGN access
- Wallet с private key в extension
- Experimental — security review нужен
- Manifest v3 limitations

### 🧭 Fit / Maturity / Ops
- **Fit:** Enhanced GMGN browsing, quick trading
- **Maturity:** experimental (browser extension)
- **Latency/Cost:** fast (client-side)
- **Data constraints:** GMGN, wallet private key
- **Ops friction:** medium (extension install)

### Full links
- Repo: https://github.com/amibars/woody-hub
- Original README: https://github.com/amibars/woody-hub/blob/main/README.md
- Maturity: experimental

---

## woody

**TL;DR:** AI agents для trading и copy strategies на Solana. Multi-agent system с автоматизацией trades. Copy-trading по profitable wallets из GMGN. Используй с woody-hub для полного стека.

### Быстрый выбор
- ✅ Используй если:
  - Нужен copy trading
  - AI-driven trading agents
  - Auto-trading по strategies
  - Solana trading
  - GMGN integration
- ❌ Не используй если:
  - Manual strategies only
  - EVM chains
  - Production с большими суммами
  - Нет опыта с trading bots

### 🚀 Запуск
```bash
git clone https://github.com/amibars/woody && cd woody
pip install -r requirements.txt
# Configure wallets to copy, RPC, keys
python main.py
```

### 🧩 Архитектура
- **Agents:** multi-agent trading system
- **Strategies:** copy-trading, custom rules
- **Data:** GMGN wallet stats
- **Execution:** Solana transactions
- **Entrypoints:** main.py, config

### 🧪 Примеры задач
- Copy trades от profitable wallet
- Auto-buy на signals
- Multi-wallet management
- Strategy backtesting
- Portfolio automation

### ⚠️ Ограничения
- Private keys нужны
- Experimental — риск потерь
- Solana only
- Зависит от GMGN data
- RPC rate limits

### 🧭 Fit / Maturity / Ops
- **Fit:** Automated trading, copy-trading
- **Maturity:** experimental (use with caution)
- **Latency/Cost:** fast (Solana) + trading costs
- **Data constraints:** private keys, GMGN, RPC
- **Ops friction:** medium (config, monitoring)

### Full links
- Repo: https://github.com/amibars/woody
- Original README: https://github.com/amibars/woody/blob/main/README.md
- Maturity: experimental

---

## alris

**TL;DR:** AI-driven yield optimizer для Solana. Интеграция CoinGecko + Orca данных, GPT-4 для trading strategies, Solana Agent Kit под капотом. Автоматизирует yield farming решения. MVP, не задеплойен.

### Быстрый выбор
- ✅ Используй если:
  - AI yield optimization исследование
  - DeFi automation прототип
  - Solana ecosystem
  - Учебный проект
  - GPT-4 strategies эксперименты
- ❌ Не используй если:
  - Manual trading предпочтительнее
  - Production ready (не задеплойен)
  - Real funds (экспериментальный)
  - EVM chains

### 🚀 Запуск
```bash
git clone https://github.com/amibars/alris && cd alris
npm install
# Set OPENAI_API_KEY, SOLANA_RPC_URL
npm run dev
```

### 🧩 Архитектура
- **Data:** CoinGecko API, Orca pools
- **AI:** GPT-4 strategy generation
- **Integration:** Solana Agent Kit
- **Frontend:** Next.js dashboard
- **Entrypoints:** app/, api/

### 🧪 Примеры задач
- AI анализ yield возможностей
- Strategy recommendations
- Portfolio rebalancing идеи
- Market condition analysis
- DeFi research dashboard

### ⚠️ Ограничения
- MVP not deployed
- Experimental — не для production
- OpenAI API costs
- Зависит от CoinGecko/Orca
- Нет real trading execution

### 🧭 Fit / Maturity / Ops
- **Fit:** DeFi research, yield analysis prototype
- **Maturity:** experimental (MVP)
- **Latency/Cost:** medium (API calls + GPT-4)
- **Data constraints:** OpenAI key, Solana RPC
- **Ops friction:** low (npm run dev)

### Full links
- Repo: https://github.com/amibars/alris
- Original README: https://github.com/amibars/alris/blob/main/README.md
- Maturity: experimental

---

## Growtradebot

**TL;DR:** Telegram Solana trading bot. Buy/sell SPL tokens через Telegram commands. Jito bundles для fast execution, Raydium SDK интеграция, Jupiter API для swaps, Pump.fun support. TypeScript кодовая база.

### Быстрый выбор
- ✅ Используй если:
  - Trading через Telegram
  - Быстрый Solana trading (Jito MEV)
  - Trading на Pump.fun и Raydium
  - Jupiter swaps
  - Mobile-friendly trading
- ❌ Не используй если:
  - Non-Telegram interface
  - EVM chains
  - CLI предпочтительнее
  - Production с большими суммами

### 🚀 Запуск
```bash
git clone https://github.com/amibars/Growtradebot && cd Growtradebot
npm install
# Set TELEGRAM_BOT_TOKEN, PRIVATE_KEY, RPC_URL
npm run build && npm start
```

### 🧩 Архитектура
- **Bot:** Telegram Bot API
- **DEX:** Jupiter, Raydium, Pump.fun
- **Speed:** Jito MEV bundles
- **Lang:** TypeScript
- **Wallet:** Solana keypair
- **Entrypoints:** src/, commands/

### 🧪 Примеры задач
- Buy token через /buy command
- Sell через /sell command
- Price check через /price
- Snipe новые launches
- Set limit orders

### ⚠️ Ограничения
- Private key в config
- Telegram Bot нужен
- Jito tips стоят SOL
- Solana only
- Experimental code

### 🧭 Fit / Maturity / Ops
- **Fit:** Mobile trading, Telegram interface
- **Maturity:** experimental (trading bot)
- **Latency/Cost:** fast (Jito) + tips
- **Data constraints:** private key, Telegram token, RPC
- **Ops friction:** medium (config, hosting)

### Full links
- Repo: https://github.com/amibars/Growtradebot
- Maturity: experimental

---

## Thin-Floor-Strategy

**TL;DR:** NFT trading стратегия для Magic Eden. Автоматизация thin floor strategy — поиск undervalued NFT collections с низким floor и редкими listings. Быстрый buy и flip. Solana NFT focus.

### Быстрый выбор
- ✅ Используй если:
  - NFT trading на Magic Eden
  - Thin floor strategy интересна
  - Автоматизация NFT trades
  - Solana NFTs
  - Quick flip opportunities
- ❌ Не используй если:
  - Fungible tokens only
  - Other marketplaces (Blur, OpenSea)
  - EVM NFTs
  - Manual trading

### 🚀 Запуск
```bash
git clone https://github.com/amibars/Thin-Floor-Strategy && cd Thin-Floor-Strategy
pip install -r requirements.txt
# Configure Magic Eden API, wallet
python main.py
```

### 🧩 Архитектура
- **Marketplace:** Magic Eden API
- **Strategy:** thin floor detection
- **Execution:** Solana transactions
- **Filtering:** floor price, listing count
- **Entrypoints:** main.py, config

### 🧪 Примеры задач
- Найти collections с thin floor
- Auto-buy undervalued NFTs
- Quick flip arbitrage
- Monitor floor movements
- Alert на opportunities

### ⚠️ Ограничения
- Magic Eden only
- NFT ликвидность ниже tokens
- Риск rug pulls
- Experimental strategy
- Wallet private key нужен

### 🧭 Fit / Maturity / Ops
- **Fit:** NFT trading automation, thin floor strategy
- **Maturity:** experimental (trading script)
- **Latency/Cost:** medium (API + transactions)
- **Data constraints:** Magic Eden API, wallet
- **Ops friction:** medium (config, monitoring)

### Full links
- Repo: https://github.com/amibars/Thin-Floor-Strategy
- Maturity: experimental

---

## pumpfun-king-of-the-hill

**TL;DR:** Real-time визуализация Pump.fun "King of the Hill" token. React 18 + Recharts для графиков в реальном времени. Tracking ownership changes, market cap movements, holder distribution. Visualization-only, не для trading.

### Быстрый выбор
- ✅ Используй если:
  - Отслеживаешь KOTH token
  - Визуализация Pump.fun data
  - Research Pump.fun mechanics
  - Dashboard для мониторинга
  - Learning React + data viz
- ❌ Не используй если:
  - Trading execution (только visualization)
  - Автоматизация trades
  - Нужны alerts
  - Backend analytics

### 🚀 Запуск
```bash
git clone https://github.com/amibars/pumpfun-king-of-the-hill && cd pumpfun-king-of-the-hill
npm install
npm run dev
# Open http://localhost:5173
```

### 🧩 Архитектура
- **Frontend:** React 18 + Vite
- **Charts:** Recharts library
- **Data:** Pump.fun API
- **State:** React Query/hooks
- **Entrypoints:** src/App.tsx, components/

### 🧪 Примеры задач
- Мониторинг KOTH changes
- Market cap графики
- Holder distribution view
- Trading volume charts
- Historical comparison

### ⚠️ Ограничения
- Visualization only, не trading
- Зависит от Pump.fun API
- Нет alerts/notifications
- Frontend only
- Rate limits от Pump.fun

### 🧭 Fit / Maturity / Ops
- **Fit:** Pump.fun research, KOTH monitoring
- **Maturity:** experimental (dashboard)
- **Latency/Cost:** fast (frontend only)
- **Data constraints:** Pump.fun API access
- **Ops friction:** low (npm run dev)

### Full links
- Repo: https://github.com/amibars/pumpfun-king-of-the-hill
- Maturity: experimental

### Full links
- Repo: https://github.com/amibars/pumpfun-king-of-the-hill
- Maturity: experimental

---

## Pump-Fun-API

**TL;DR:** Trade on Pump.fun programmatically. API для программного трейдинга.

### Быстрый выбор
- ✅ Используй если: нужен programmatic Pump.fun trading
- ❌ Не используй если: analytics only

### Full links
- Repo: https://github.com/amibars/Pump-Fun-API
- Maturity: unknown

---

## pump-meta

**TL;DR:** Pump.fun sentiment analyzer на базе NLTK. Анализ sentiment мемкоинов, time series для meme hype tracking, извлечение trending meta. Помогает понять циклы hype и narrative trends на Pump.fun. Research tool, не для trading.

### Быстрый выбор
- ✅ Используй если:
  - Sentiment analysis для memecoins
  - Tracking meme hype cycles
  - NLP analysis на Pump.fun data
  - Narrative research
  - Trend prediction experiments
- ❌ Не используй если:
  - Trade execution (только analysis)
  - Real-time signals
  - Fundamental analysis
  - Non-Pump.fun tokens

### 🚀 Запуск
```bash
git clone https://github.com/amibars/pump-meta && cd pump-meta
pip install -r requirements.txt
# Configure data sources
python main.py
```

### 🧩 Архитектура
- **NLP:** NLTK sentiment analysis
- **Time series:** hype cycle tracking
- **Output:** trending metas, sentiment scores
- **Data:** Pump.fun tokens
- **Entrypoints:** main.py

### 🧪 Примеры задач
- Sentiment score для token names
- Hype cycle анализ
- Trending meta extraction
- Narrative clustering
- Historical pattern matching

### ⚠️ Ограничения
- Analysis only, не trading
- NLTK limitations
- Pump.fun data зависимость
- Experimental NLP
- Нет real-time

### 🧭 Fit / Maturity / Ops
- **Fit:** Meme research, narrative analysis
- **Maturity:** experimental (NLP research)
- **Latency/Cost:** slow (batch analysis)
- **Data constraints:** Pump.fun data access
- **Ops friction:** low (pip install)

### Full links
- Repo: https://github.com/amibars/pump-meta
- Maturity: experimental

---

## OpenTruthV1

**TL;DR:** Open-source версия @truth_terminal. Terminal-based AI personality для экспериментов с AI characters. База для создания собственных AI personas. Инспирирован truth_terminal феноменом.

### Быстрый выбор
- ✅ Используй если:
  - Интерес к AI personalities
  - Truth terminal эксперименты
  - Terminal-based AI chars
  - Учебный проект
  - Branding research
- ❌ Не используй если:
  - Production AI assistant
  - Trading/DeFi
  - Serious applications
  - Social media automation

### 🚀 Запуск
```bash
git clone https://github.com/amibars/OpenTruthV1 && cd OpenTruthV1
# Follow README instructions
python main.py
```

### 🧩 Архитектура
- **Interface:** Terminal-based
- **Personality:** Configurable prompts
- **LLM:** Configurable backend
- **Entrypoints:** main.py

### 🧪 Примеры задач
- Create AI personality
- Terminal chat experiments
- Prompt engineering practice
- Character development
- Branding experiments

### ⚠️ Ограничения
- Experimental проект
- Limited documentation
- Terminal only
- Не production ready
- Fan project

### 🧭 Fit / Maturity / Ops
- **Fit:** AI personality experiments, learning
- **Maturity:** experimental (fan project)
- **Latency/Cost:** depends on LLM backend
- **Data constraints:** LLM API key
- **Ops friction:** low (clone and run)

### Full links
- Repo: https://github.com/amibars/OpenTruthV1
- Maturity: experimental

---

## Smart_Money_Follower

**TL;DR:** Analyze top Solana wallets via GMGN.ai API. Tracking profitable wallets и их trades. Автоматический мониторинг smart money movements. Используй для research и alpha discovery.

### Быстрый выбор
- ✅ Используй если:
  - Следишь за smart money
  - Анализ top performers
  - Copy-trading research
  - Alpha discovery
  - Wallet monitoring
- ❌ Не используй если:
  - Trading execution (analysis only)
  - Real-time alerts
  - EVM chains
  - Production systems

### 🚀 Запуск
```bash
git clone https://github.com/amibars/Smart_Money_Follower && cd Smart_Money_Follower
pip install -r requirements.txt
# Configure GMGN access
python main.py
```

### 🧩 Архитектура
- **Data:** GMGN.ai API
- **Analysis:** wallet performance tracking
- **Metrics:** PNL, trades, tokens
- **Output:** reports, wallet lists
- **Entrypoints:** main.py

### 🧪 Примеры задач
- Top wallet tracking
- Trade history analysis
- PNL comparison
- Token holding patterns
- Entry/exit timing research

### ⚠️ Ограничения
- GMGN API зависимость
- Analysis only, не trading
- Rate limits
- Solana only
- Historical data

### 🧭 Fit / Maturity / Ops
- **Fit:** Smart money research, copy-trading prep
- **Maturity:** experimental (analysis script)
- **Latency/Cost:** slow (batch analysis)
- **Data constraints:** GMGN API access
- **Ops friction:** low (pip install)

### Full links
- Repo: https://github.com/amibars/Smart_Money_Follower
- Maturity: experimental

---

## gmgn_analyst

**TL;DR:** Analyze Pump.Fun tokens via GMGN. Token analysis, holder distribution, трейды, и insights. Research tool для понимания token dynamics на Pump.fun. Используй для due diligence.

### Быстрый выбор
- ✅ Используй если:
  - Token analysis на Pump.fun
  - Due diligence research
  - Holder distribution анализ
  - Trade pattern analysis
  - Rug detection experiments
- ❌ Не используй если:
  - Trading execution
  - Non-Pump.fun tokens
  - Real-time alerts
  - Wallet analysis (используй gmgn_smart)

### 🚀 Запуск
```bash
git clone https://github.com/amibars/gmgn_analyst && cd gmgn_analyst
pip install -r requirements.txt
python main.py <token_address>
```

### 🧩 Архитектура
- **Data:** GMGN API
- **Focus:** Token analysis
- **Metrics:** holders, trades, volume
- **Output:** analysis report
- **Entrypoints:** main.py

### 🧪 Примеры задач
- Token holder distribution
- Trade volume analysis
- Whale concentration check
- Launch analysis
- Red flag detection

### ⚠️ Ограничения
- GMGN зависимость
- Analysis only
- Pump.fun tokens only
- Rate limits
- Limited documentation

### 🧭 Fit / Maturity / Ops
- **Fit:** Token research, due diligence
- **Maturity:** experimental (analysis script)
- **Latency/Cost:** fast (single token)
- **Data constraints:** GMGN API access
- **Ops friction:** low (pip install)

### Full links
- Repo: https://github.com/amibars/gmgn_analyst
- Maturity: experimental

---

## ct_alpha

**TL;DR:** Crypto Twitter profitability calculator. Анализ твитов для trading signals, track производительности CT influencers. Проверьаешь какие calls реально profitable. Research tool для CT alpha verification.

### Быстрый выбор
- ✅ Используй если:
  - Проверка CT influencer profitability
  - Tracking call performance
  - Alpha source verification
  - Анализ signal quality
  - CT research
- ❌ Не используй если:
  - Trading execution
  - Real-time alerts
  - Automated trading
  - Non-CT analysis

### 🚀 Запуск
```bash
git clone https://github.com/amibars/ct_alpha && cd ct_alpha
pip install -r requirements.txt
# Configure Twitter handles
python main.py
```

### 🧩 Архитектура
- **Data:** Twitter API / scraping
- **Analysis:** Call tracking, price fetching
- **Metrics:** Win rate, avg returns
- **Output:** profitability reports
- **Entrypoints:** main.py

### 🧪 Примеры задач
- Track influencer calls
- Calculate win rate
- Compare CT alphas
- Verify signal quality
- Build watchlists

### ⚠️ Ограничения
- Twitter API зависимость
- Analysis only
- Manual call extraction
- Rate limits
- Historical data

### 🧭 Fit / Maturity / Ops
- **Fit:** CT research, alpha verification
- **Maturity:** unknown (analysis script)
- **Latency/Cost:** slow (tweet analysis)
- **Data constraints:** Twitter API access
- **Ops friction:** medium (Twitter setup)

### Full links
- Repo: https://github.com/amibars/ct_alpha
- Maturity: unknown

---

## QAMI

**TL;DR:** Quantum Assembly Machine Infinity. 1-bit fractal architecture, INTERFACE:// protocol, WebSim AI integration. Experimental quantum interface generation. Community-driven exploration fractal computing concepts. Экспериментальный проект вне мейнстрима.

### Быстрый выбор
- ✅ Используй если:
  - Experimental quantum interfaces
  - WebSim AI exploration
  - Community-driven pattern discovery
  - Fractal computing interest
  - Avant-garde AI experiments
- ❌ Не используй если:
  - Standard computing tasks
  - Production use
  - Traditional ML/AI
  - DeFi/trading

### 🚀 Запуск
```bash
git clone https://github.com/amibars/QAMI && cd QAMI
# Follow README for specific instructions
# WebSim integration required
```

### 🧩 Архитектура
- **Core:** 1-bit fractal architecture
- **Protocol:** INTERFACE://
- **Integration:** WebSim AI
- **Patterns:** community-driven discovery
- **Entrypoints:** varies by experiment

### 🧪 Примеры задач
- Fractal pattern generation
- Quantum interface experiments
- WebSim AI integration
- Community collaboration
- Conceptual exploration

### ⚠️ Ограничения
- Highly experimental
- Not for production
- Limited documentation
- Requires conceptual understanding
- Community-dependent

### 🧭 Fit / Maturity / Ops
- **Fit:** Experimental computing, avant-garde AI
- **Maturity:** experimental (research project)
- **Latency/Cost:** varies
- **Data constraints:** WebSim access
- **Ops friction:** high (conceptual complexity)

### Full links
- Repo: https://github.com/amibars/QAMI
- Maturity: experimental

---

## portkey-gateway

**TL;DR:** AI Gateway с 200+ LLMs и 50+ guardrails. Fallbacks, retries, load balancing, request timeouts. Multi-modal support, realtime APIs.

### Быстрый выбор
- ✅ Используй если:
  - Нужен unified gateway для multiple LLMs
  - Хочешь fallbacks и retries
  - Нужны guardrails для AI safety
  - Load balancing между providers
- ❌ Не используй если:
  - Single provider only
  - Не нужна reliability layer

### 🚀 Запуск
```bash
# Docker
docker run -p 8787:8787 portkeyai/gateway

# Node.js
npm install @portkey-ai/gateway
```

### 🧩 Архитектура
- **Gateway:** route to 200+ LLMs
- **Fallbacks:** automatic provider failover
- **Guardrails:** 50+ safety checks
- **Retries:** automatic retry logic
- **Load balancing:** across providers
- **Realtime:** streaming support

### 🧪 Примеры задач
- Route to OpenAI with Claude fallback
- Add content moderation guardrails
- Load balance across multiple API keys
- Request timeouts and retries

### ⚠️ Ограничения
- Additional latency (gateway layer)
- Requires configuration для каждого provider

### Full links
- Repo: https://github.com/amibars/portkey-gateway
- Docs: https://portkey.ai/docs
- Maturity: active

---

## MEMETOOL-V0.3

**TL;DR:** Meme coin tools набор утилит. Инструменты для работы с memecoins: анализ, мониторинг, трейдинг utilities. Версия 0.3 с базовыми функциями. Experimental toolkit.

### Быстрый выбор
- ✅ Используй если:
  - Нужны meme coin utilities
  - Experimental tools достаточно
  - Быстрый прототип
  - Учебный проект
  - Memecoin research
- ❌ Не используй если:
  - Production trading
  - Нужна документация
  - Enterprise use
  - Non-meme tokens

### 🚀 Запуск
```bash
git clone https://github.com/amibars/MEMETOOL-V0.3 && cd MEMETOOL-V0.3
# Follow README instructions
# Configure as needed
```

### 🧩 Архитектура
- **Core:** meme coin utilities
- **Version:** 0.3 (early stage)
- **Focus:** memecoin analysis
- **Entrypoints:** main scripts

### 🧪 Примеры задач
- Meme token analysis
- Quick monitoring
- Trade helpers
- Research utilities
- Data extraction

### ⚠️ Ограничения
- Limited documentation
- Early version (0.3)
- Experimental
- Unknown stability
- May require setup

### 🧭 Fit / Maturity / Ops
- **Fit:** Meme coin experimentation
- **Maturity:** unknown (v0.3)
- **Latency/Cost:** varies
- **Data constraints:** chain data access
- **Ops friction:** unknown

### Full links
- Repo: https://github.com/amibars/MEMETOOL-V0.3
- Maturity: unknown

---

## poe-api-wrapper

**TL;DR:** Python wrapper для Poe.com. Доступ к GPT-4, Claude, Llama, Gemini через Poe. Auto proxy, streaming, file attachments, custom bots.

### Быстрый выбор
- ✅ Используй если:
  - Нужен доступ к multiple LLMs через Poe
  - Не хочешь платить за direct API
  - Хочешь streaming responses
  - Нужны file attachments
- ❌ Не используй если:
  - Нужен direct API access
  - Production с high rate limits
  - Poe ToS concerns

### 🚀 Запуск
```bash
pip install poe-api-wrapper
```
```python
from poe_api_wrapper import PoeApi
client = PoeApi(cookie="...")
response = client.send_message("GPT-4", "Hello!")
```

### 🧩 Архитектура
- **Auth:** Poe cookies
- **Proxy:** auto proxy requests
- **Features:** streaming, files, citations
- **Bots:** create/edit custom bots
- **Groups:** group chat support

### 🧪 Примеры задач
- Send message to GPT-4/Claude
- Stream responses
- Create custom Poe bot
- Upload knowledge bases
- Concurrent message sending

### ⚠️ Ограничения
- Requires Poe account
- May break with Poe updates
- Rate limits from Poe
- ToS considerations

### Full links
- Repo: https://github.com/amibars/poe-api-wrapper
- Maturity: active

---

## solana-pnl-card-bot

**TL;DR:** PnL card generator для Solana tokens. Генерация shareable profit/loss cards для Twitter/Discord. Показывает ROI, entry/exit, token info. Используй для flex или community engagement.

### Быстрый выбор
- ✅ Используй если:
  - PnL card generation
  - Social media sharing
  - Community engagement
  - Trade showcase
  - Telegram bot integration
- ❌ Не используй если:
  - Trading execution
  - Portfolio tracking
  - EVM chains
  - Private use only

### 🚀 Запуск
```bash
git clone https://github.com/amibars/solana-pnl-card-bot && cd solana-pnl-card-bot
npm install
# Configure Telegram token, Solana RPC
npm start
```

### 🧩 Архитектура
- **Bot:** Telegram Bot API
- **Cards:** Image generation
- **Data:** Solana RPC, price feeds
- **Output:** PNG/image cards
- **Entrypoints:** main script, bot commands

### 🧪 Примеры задач
- Generate PnL card для trade
- Share на Twitter/Discord
- Track token performance visually
- Community leaderboards
- Trade history cards

### ⚠️ Ограничения
- Solana only
- Telegram required
- Image gen dependencies
- Price data accuracy
- Manual trade input

### 🧭 Fit / Maturity / Ops
- **Fit:** Social sharing, community engagement
- **Maturity:** unknown (utility bot)
- **Latency/Cost:** fast (image gen)
- **Data constraints:** Solana RPC, Telegram token
- **Ops friction:** medium (config)

### Full links
- Repo: https://github.com/amibars/solana-pnl-card-bot
- Maturity: unknown

---

## telegram_bot

**TL;DR:** Telegram bot template. Базовый шаблон для Telegram ботов с готовой структурой. Быстрый старт для нового бота. Используй как boilerplate.

### Быстрый выбор
- ✅ Используй если:
  - Нужен Telegram bot boilerplate
  - Быстрый старт
  - Простая структура
  - Учебный проект
  - Minimal setup
- ❌ Не используй если:
  - Production-grade features
  - Complex bot logic
  - Database integration
  - Specific use case templates

### 🚀 Запуск
```bash
git clone https://github.com/amibars/telegram_bot && cd telegram_bot
# Install dependencies
# Set TELEGRAM_BOT_TOKEN
python main.py
```

### 🧩 Архитектура
- **Framework:** python-telegram-bot / aiogram
- **Structure:** basic handlers
- **Config:** env variables
- **Entrypoints:** main.py

### 🧪 Примеры задач
- Basic command handlers
- Message responses
- Inline keyboards
- Bot initialization
- Error handling

### ⚠️ Ограничения
- Basic template
- No advanced features
- Minimal documentation
- Requires customization
- No database

### 🧭 Fit / Maturity / Ops
- **Fit:** Starting point for Telegram bots
- **Maturity:** unknown (template)
- **Latency/Cost:** low
- **Data constraints:** Telegram token
- **Ops friction:** low (simple setup)

### Full links
- Repo: https://github.com/amibars/telegram_bot
- Maturity: unknown

---

## consistencydecoder

**TL;DR:** OpenAI Consistency Distilled Diff VAE. Улучшенный VAE decoder для image generation. Замена стандартного VAE в Stable Diffusion. Лучшее качество декодирования latents.

### Быстрый выбор
- ✅ Используй если:
  - Нужен улучшенный VAE decoder
  - Stable Diffusion workflows
  - Image quality важно
  - Latent space experiments
  - Research ML/AI
- ❌ Не используй если:
  - Non-image tasks
  - Text generation
  - Non-SD pipelines
  - Low GPU memory

### 🚀 Запуск
```bash
pip install consistencydecoder
# Use with Stable Diffusion pipeline
from consistencydecoder import ConsistencyDecoder
```

### 🧩 Архитектура
- **Core:** Consistency distilled VAE
- **Integration:** Stable Diffusion compatible
- **Format:** PyTorch model
- **Entrypoints:** Python module

### 🧪 Примеры задач
- Replace SD VAE decoder
- Improve image quality
- Latent space decoding
- Custom pipelines
- Research experiments

### ⚠️ Ограничения
- GPU required
- Image tasks only
- SD совместимость
- Model size
- OpenAI license

### 🧭 Fit / Maturity / Ops
- **Fit:** Image generation, SD pipelines
- **Maturity:** unknown (OpenAI research)
- **Latency/Cost:** GPU intensive
- **Data constraints:** model weights
- **Ops friction:** low (pip install)

### Full links
- Repo: https://github.com/amibars/consistencydecoder
- Maturity: unknown

---

## chatgpt-ai-template

**TL;DR:** Horizon AI Template для ChatGPT UI. React, Next.js, Chakra UI готовый шаблон. Ready-to-use chat interface с красивым дизайном. Отличный старт для AI chat проектов.

### Быстрый выбор
- ✅ Используй если:
  - ChatGPT-like UI template
  - React/Next.js project
  - Chakra UI styling
  - Quick chat UI launch
  - Horizon design system
- ❌ Не используй если:
  - Backend-only project
  - Other UI frameworks
  - Tailwind preference
  - Mobile-first design

### 🚀 Запуск
```bash
git clone https://github.com/amibars/chatgpt-ai-template && cd chatgpt-ai-template
npm install
npm run dev
# http://localhost:3000
```

### 🧩 Архитектура
- **Framework:** React + Next.js
- **Styling:** Chakra UI
- **Design:** Horizon template
- **Features:** chat UI, dark mode
- **Entrypoints:** pages/, components/

### 🧪 Примеры задач
- Launch AI chat interface
- Customize chat components
- Add OpenAI integration
- Build chatbot UI
- Deploy chat app

### ⚠️ Ограничения
- Frontend template only
- Chakra UI required
- No backend included
- Horizon design locked
- Customization needed

### 🧭 Fit / Maturity / Ops
- **Fit:** AI chat UI, quick prototypes
- **Maturity:** unknown (template)
- **Latency/Cost:** low (frontend)
- **Data constraints:** none
- **Ops friction:** low (npm run dev)

### Full links
- Repo: https://github.com/amibars/chatgpt-ai-template
- Maturity: unknown

---

## vision-ui-dashboard-react

**TL;DR:** Vision UI Dashboard для React. Dark-themed admin dashboard template с современным дизайном. Charts, tables, stats cards, user management. Используй для admin panels.

### Быстрый выбор
- ✅ Используй если:
  - React dashboard template
  - Dark theme preferred
  - Admin panel needed
  - Data visualization
  - Quick MVP
- ❌ Не используй если:
  - Non-React project
  - Light theme required
  - Highly custom design
  - Mobile-first focus

### 🚀 Запуск
```bash
git clone https://github.com/amibars/vision-ui-dashboard-react && cd vision-ui-dashboard-react
npm install
npm run dev
# http://localhost:3000
```

### 🧩 Архитектура
- **Framework:** React
- **Styling:** CSS/SCSS, dark theme
- **Components:** charts, tables, cards
- **Layout:** sidebar, header, pages
- **Entrypoints:** src/, components/

### 🧪 Примеры задач
- Build admin dashboard
- Data visualization pages
- User management UI
- Analytics dashboard
- Settings pages

### ⚠️ Ограничения
- React only
- Dark theme default
- Template locked design
- Customization needed
- No backend

### 🧭 Fit / Maturity / Ops
- **Fit:** Admin panels, dashboards
- **Maturity:** active (template)
- **Latency/Cost:** low (frontend)
- **Data constraints:** none
- **Ops friction:** low (npm run dev)

### Full links
- Repo: https://github.com/amibars/vision-ui-dashboard-react
- Maturity: active
---

# ⭐ STARRED REPOSITORIES

> Ниже следуют 225 starred репозиториев, сгруппированных по категориям.

---

## dify

**TL;DR:** Production-ready LLM app development platform от Langgenius. Visual workflow builder для создания AI приложений без кода. RAG pipelines, agent orchestration, 100+ моделей. Self-hosted или cloud. 127k stars — один из самых популярных open-source AI platforms.

### Быстрый выбор
- ✅ Используй если:
  - Нужен visual builder для LLM workflows без кода
  - RAG с файлами, knowledge bases, document processing
  - Хочешь deploy production AI apps (chatbots, assistants)
  - Self-hosted или Dify Cloud с готовой инфраструктурой
  - Нужна командная работа с версионированием workflows
- ❌ Не используй если:
  - Предпочитаешь code-first подход (LangChain, LlamaIndex)
  - Простые LLM вызовы без workflow логики
  - Нужен ultra-low latency (visual builder добавляет overhead)
  - Не хочешь Docker для self-hosted

### 🚀 Запуск
```bash
# Self-hosted (Docker)
git clone https://github.com/langgenius/dify.git
cd dify/docker
cp .env.example .env
docker compose up -d
# http://localhost:3000 — создай admin аккаунт

# Или Dify Cloud (managed):
# https://cloud.dify.ai — бесплатный tier до 200 сообщений/день
```

### 🧩 Архитектура
- **Backend:** Python 3.11+, Flask/Celery, PostgreSQL, Redis, Weaviate/Qdrant для vectors
- **Frontend:** React + Next.js, TypeScript
- **Workflows:** visual drag-and-drop canvas с nodes (LLM, Tools, Conditions, Loops)
- **RAG:** built-in document processing (PDF, DOCX, TXT, Notion, Web), chunk splitting, embedding
- **Models:** OpenAI, Claude, Gemini, Ollama, Azure, AWS Bedrock, 100+ providers
- **Entrypoints:** `api/` — backend, `web/` — frontend, `docker/` — deployment configs
- **Ключевые файлы:** [api/core/](https://github.com/langgenius/dify/tree/main/api/core), [web/app/](https://github.com/langgenius/dify/tree/main/web/app)

### 🧪 Примеры задач
- Создание customer support chatbot с RAG на документации
- HR assistant для ответов на вопросы по policies
- Code review agent с GitHub integration
- Data analysis pipeline с SQL queries
- Multi-agent conversation для complex reasoning
- Workflow automation с external API calls

### ⚠️ Ограничения
- Docker required для self-hosted (нет простого pip install)
- Heavy resource usage: рекомендуется 4GB+ RAM, SSD
- Workflow complexity может замедлить debugging
- Vector DB setup нужен для RAG (Weaviate, Qdrant, etc.)
- Rate limits на Dify Cloud free tier
- Learning curve для advanced features (tools, agents, loops)

### 🧭 Fit / Maturity / Ops
- **Fit:** AI chatbots, RAG applications, workflow automation, enterprise assistants
- **Maturity:** active (v0.15+, daily releases, enterprise-ready)
- **Latency/Cost:** balanced (depends on LLM provider, workflow complexity)
- **Data constraints:** documents для RAG, API keys для models
- **Ops friction:** medium (Docker setup, но хорошая документация)

### Full links
- Repo: https://github.com/langgenius/dify
- Original README: https://github.com/langgenius/dify/blob/main/README.md
- Docs: https://docs.dify.ai
- Cloud: https://cloud.dify.ai
- Discord: https://discord.gg/dify
- Stars: 127,336
- Maturity: active

---

## open-webui

**TL;DR:** User-friendly ChatGPT-like web UI для локальных и cloud LLMs. Ollama, OpenAI, Claude, любые OpenAI-compatible APIs. Multi-user с RBAC, RAG на документах, voice input, image generation. 122k stars — стандарт для self-hosted LLM UI.

### Быстрый выбор
- ✅ Используй если:
  - Хочешь ChatGPT-like UI для своих LLMs (Ollama, OpenAI, Claude)
  - Нужен self-hosted chat с multi-user support и roles
  - RAG на своих документах без кода
  - Voice input/output, image generation
  - Хочешь unified interface для разных моделей
- ❌ Не используй если:
  - API-only use case (не нужен UI)
  - Нужен workflow builder (используй Dify, n8n)
  - Хочешь embeddable widget (это standalone app)
  - Enterprise SSO requirements

### 🚀 Запуск
```bash
# Самый простой способ — Docker
docker run -d -p 3000:8080 \
  -v open-webui:/app/backend/data \
  --name open-webui \
  ghcr.io/open-webui/open-webui:main
# http://localhost:3000

# С Ollama (если Ollama на том же хосте)
docker run -d -p 3000:8080 \
  -v open-webui:/app/backend/data \
  -e OLLAMA_BASE_URL=http://host.docker.internal:11434 \
  ghcr.io/open-webui/open-webui:main

# Или pip install (dev)
pip install open-webui
open-webui serve
```

### 🧩 Архитектура
- **Frontend:** SvelteKit, TypeScript, TailwindCSS
- **Backend:** Python 3.11+, FastAPI, SQLite/PostgreSQL
- **Features:** chat history, RAG, multi-model switching, voice, images
- **Auth:** multi-user with RBAC, OAuth support
- **RAG:** built-in document upload (PDF, DOCX, TXT), vector search
- **Entrypoints:** `backend/` — FastAPI server, `src/` — SvelteKit frontend
- **Ключевые файлы:** [backend/main.py](https://github.com/open-webui/open-webui/blob/main/backend/main.py)

### 🧪 Примеры задач
- Локальный ChatGPT для команды с Ollama backend
- Корпоративный AI assistant с RBAC и audit logs
- RAG на внутренней документации компании
- Multi-model A/B testing (compare responses)
- Voice-enabled AI assistant для accessibility
- Image generation UI для DALL-E/Stable Diffusion

### ⚠️ Ограничения
- Docker recommended (pip install экспериментальный)
- SQLite default — для prod нужен PostgreSQL
- No built-in workflow builder (только chat)
- RAG простой — для сложного используй LlamaIndex
- Voice требует browser support (Web Speech API)
- Ollama должен быть доступен по сети

### 🧭 Fit / Maturity / Ops
- **Fit:** self-hosted ChatGPT alternative, team AI chat, RAG demos
- **Maturity:** active (frequent releases, large community)
- **Latency/Cost:** depends on backend LLM (Ollama free, OpenAI paid)
- **Data constraints:** documents для RAG, API keys для cloud models
- **Ops friction:** low (single Docker container, minimal config)

### Full links
- Repo: https://github.com/open-webui/open-webui
- Original README: https://github.com/open-webui/open-webui/blob/main/README.md
- Docs: https://docs.openwebui.com
- Demo: https://openwebui.com
- Discord: https://discord.gg/open-webui
- Stars: 121,944
- Maturity: active

---

## godot

**TL;DR:** Самый популярный open-source game engine. MIT license — полностью бесплатный, без royalties. GDScript (Python-like) + C# + C++. 2D и 3D игры любой сложности. Активное комьюнити после Unity pricing drama. 106k stars.

### Быстрый выбор
- ✅ Используй если:
  - Game development (indie, casual, mid-size)
  - 2D games — Godot особенно силён здесь
  - Open-source engine без royalties
  - Learning game dev (отличные tutorials)
  - Нужен lightweight engine (100MB vs Unity 10GB)
- ❌ Не используй если:
  - AAA console games (Unity/Unreal лучше)
  - VR/AR development (early support)
  - Нужен огромный asset store (Unity wins)
  - Team уже знает Unity/Unreal

### 🚀 Запуск
```bash
# Самый простой способ — скачать binary
# https://godotengine.org/download

# Build from source (advanced)
git clone https://github.com/godotengine/godot.git
cd godot
scons platform=windows target=editor
# ./bin/godot.windows.editor.x86_64.exe

# Godot Mono (C# support)
# Скачай Mono версию с godotengine.org
```

### 🧩 Архитектура
- **Language:** C++ core, GDScript/C#/GDExtension для gameplay
- **Editor:** Built-in visual editor с scene tree, inspector, debugger
- **Rendering:** Vulkan (4.x), OpenGL (3.x), mobile support
- **Physics:** Built-in 2D/3D physics engines
- **Platforms:** Windows, macOS, Linux, Android, iOS, Web, consoles
- **Entrypoints:** `main/main.cpp` — engine entry, `scene/` — scene system
- **Ключевые файлы:** [scene/main/](https://github.com/godotengine/godot/tree/master/scene/main)

### 🧪 Примеры задач
- 2D platformer с pixel art и animations
- 3D RPG с dialogue system и inventory
- Visual novel с branching storylines
- Mobile casual game для Android/iOS
- Multiplayer game с built-in networking
- Tool/app для game design (level editor)

### ⚠️ Ограничения
- 3D graphics слабее Unity/Unreal (улучшается)
- Asset store меньше (но бесплатный)
- VR/AR support ранний (Godot 4.x)
- Console export требует paid license от platform holders
- C# support требует Mono версию (не в standard)
- Large teams могут miss Unity collaboration tools

### 🧭 Fit / Maturity / Ops
- **Fit:** indie games, game jams, prototypes, 2D games, learning
- **Maturity:** stable (v4.3+, очень активная разработка)
- **Latency/Cost:** free forever, MIT license
- **Data constraints:** GDScript или C# knowledge
- **Ops friction:** low (download and run, cross-platform)

### Full links
- Repo: https://github.com/godotengine/godot
- Original README: https://github.com/godotengine/godot/blob/master/README.md
- Docs: https://docs.godotengine.org
- Download: https://godotengine.org/download
- Asset Library: https://godotengine.org/asset-library
- Discord: https://discord.gg/godot
- Stars: 105,908
- Maturity: active

---

## gemini-cli

**TL;DR:** Official Gemini CLI от Google. Полноценный AI agent прямо в терминале — code generation, file editing, shell commands, multi-turn conversations. Бесплатный tier с Gemini 2.5. 92k stars — главный конкурент Claude CLI.

### Быстрый выбор
- ✅ Используй если:
  - Хочешь AI-assisted coding в терминале (как Claude Code)
  - Gemini 2.5 Pro/Flash models (бесплатно или Pay-as-you-go)
  - Нужен agentic mode с file editing и shell execution
  - Google ecosystem (Vertex AI, Google Cloud)
  - Хочешь официальный инструмент от Google
- ❌ Не используй если:
  - Предпочитаешь Claude/GPT (используй aider, Claude CLI)
  - GUI preference (используй AI Studio)
  - Complex multi-agent workflows (Gemini CLI — single agent)

### 🚀 Запуск
```bash
# Установка через npm
npm install -g @anthropic-ai/gemini-cli

# Или npx (без установки)
npx @anthropic-ai/gemini-cli

# Авторизация
gemini auth login
# Opens browser for Google account auth

# Простой запуск
gemini
> Explain this codebase structure

# С конкретным файлом
gemini "Refactor this function" main.py
```

### 🧩 Архитектура
- **Runtime:** Node.js, TypeScript
- **Models:** Gemini 2.5 Pro, 2.5 Flash, 2.0 (via Google AI)
- **Features:** code editing, file ops, shell commands, multi-turn chat
- **Auth:** Google OAuth, API key, Vertex AI
- **Context:** automatic codebase context loading
- **Entrypoints:** CLI commands, REPL mode, single-prompt mode
- **Tool use:** built-in tools для code, files, terminal

### 🧪 Примеры задач
- "Explain this codebase" — получить overview проекта
- "Add unit tests to utils.py" — generate и write tests
- "Find and fix bugs in auth module" — debugging
- "Refactor this to use TypeScript" — code migration
- "Create a new API endpoint for users" — scaffolding
- Multi-file refactoring crossproject

### ⚠️ Ограничения
- Google account required для auth
- Rate limits на бесплатном tier (1500 req/day)
- Gemini models only (no Claude, GPT)
- Agentic features менее mature чем Claude CLI
- No API as a library (CLI only)
- Some advanced sandbox features в beta

### 🧭 Fit / Maturity / Ops
- **Fit:** AI-assisted coding, terminal-first developers, Google ecosystem
- **Maturity:** active (official Google product, rapid development)
- **Latency/Cost:** fast (Gemini Flash), free tier generous
- **Data constraints:** Google account, optional API key
- **Ops friction:** low (npx install, OAuth flow)

### Full links
- Repo: https://github.com/google-gemini/gemini-cli
- Original README: https://github.com/google-gemini/gemini-cli/blob/main/README.md
- Docs: https://ai.google.dev/gemini-api/docs/cli
- AI Studio: https://aistudio.google.com
- Stars: 92,599
- Maturity: active

---

## awesome-llm-apps

**TL;DR:** Collection of awesome LLM apps with AI Agents и RAG. OpenAI, Anthropic, Gemini, open-source models. 89k stars.

### Быстрый выбор
- ✅ Используй если:
  - Ищешь примеры LLM apps
  - Learning AI agent patterns
  - RAG implementations
- ❌ Не используй если:
  - Production codebase нужен

### Full links
- Repo: https://github.com/Shubhamsaboo/awesome-llm-apps
- Original README: https://github.com/Shubhamsaboo/awesome-llm-apps/blob/main/README.md
- Stars: 89,638
- Maturity: curated list

---

## firecrawl

**TL;DR:** Web Data API for AI — превращает любой сайт в LLM-ready markdown или structured data. JavaScript rendering, anti-bot bypass, clean extraction. Self-hosted или cloud API. Идеален для RAG pipelines и AI agents. 77k stars.

### Быстрый выбор
- ✅ Используй если:
  - Web scraping для LLM training/RAG
  - Нужен clean markdown без HTML мусора
  - AI agent нужен web data (browsing tools)
  - Structured data extraction (LLM-based)
  - JavaScript-rendered pages (SPA, React sites)
- ❌ Не используй если:
  - Simple static HTML scraping (BeautifulSoup faster)
  - Non-AI use cases (overkill)
  - Need to avoid cloud dependencies (self-host possible)

### 🚀 Запуск
```bash
# Python SDK
pip install firecrawl-py

# Node.js SDK
npm install @firecrawl/js

# Self-hosted (Docker)
git clone https://github.com/firecrawl/firecrawl.git
cd firecrawl
docker compose up -d
```
```python
from firecrawl import FirecrawlApp

# Cloud API
app = FirecrawlApp(api_key="fc-xxxxx")

# Scrape single URL
result = app.scrape_url("https://docs.example.com")
print(result['markdown'])

# Crawl entire site
crawl_result = app.crawl_url("https://docs.example.com", limit=100)

# Extract structured data with LLM
extracted = app.extract(["https://example.com"], {
    "schema": {"title": "string", "price": "number"}
})
```

### 🧩 Архитектура
- **Backend:** Node.js, TypeScript, Playwright для rendering
- **SDKs:** Python, Node.js, Go, Rust
- **Features:** markdown extraction, crawling, LLM extraction, screenshots
- **Anti-bot:** proxy rotation, CAPTCHA solving, JS rendering
- **Output:** markdown, HTML, screenshots, structured JSON
- **Entrypoints:** `apps/api/` — REST API, `apps/playwright-service/` — browser
- **Ключевые файлы:** [apps/api/src/](https://github.com/firecrawl/firecrawl/tree/main/apps/api/src)

### 🧪 Примеры задач
- RAG pipeline: crawl docs → extract markdown → embed → search
- AI agent web browsing tool
- Competitor analysis scraping
- News aggregation с clean text
- Product data extraction (prices, reviews)
- Documentation ingestion для AI assistants

### ⚠️ Ограничения
- Cloud API requires payment для high volume
- Self-hosted требует resources (Playwright heavy)
- Rate limits на бесплатном tier (500 pages/month)
- Some sites block даже с anti-bot measures
- LLM extraction costs extra (LLM API calls)
- Complex JavaScript apps могут require tuning

### 🧭 Fit / Maturity / Ops
- **Fit:** RAG ingestion, AI agent tools, web data ETL
- **Maturity:** active (YC backed, production-ready)
- **Latency/Cost:** 2-5s per page, $0.001-0.005/page cloud
- **Data constraints:** website access, API key
- **Ops friction:** low (SDK install) / medium (self-hosted Docker)

### Full links
- Repo: https://github.com/firecrawl/firecrawl
- Original README: https://github.com/firecrawl/firecrawl/blob/main/README.md
- Docs: https://docs.firecrawl.dev
- Cloud: https://firecrawl.dev
- Stars: 77,517
- Maturity: active

---

## sherlock

**TL;DR:** OSINT tool для поиска аккаунтов по username across 400+ social networks и websites. Python CLI, fast parallel checks. Стандарт для username enumeration. 72k stars.

### Быстрый выбор
- ✅ Используй если:
  - Username OSINT / reconnaissance
  - Social media account discovery
  - Проверка занятости username
  - Security research / penetration testing
  - Brand monitoring
- ❌ Не используй если:
  - Email OSINT (используй holehe)
  - Phone OSINT (используй phoneinfoga)
  - Full identity investigation (нужен комплекс tools)
  - Illegal surveillance (это незаконно)

### 🚀 Запуск
```bash
# Установка
pip install sherlock-project

# Поиск одного username
sherlock username

# Несколько usernames
sherlock user1 user2 user3

# С выводом в файл
sherlock username --output results.txt

# Только найденные
sherlock username --print-found

# С timeout (для медленных сайтов)
sherlock username --timeout 10
```

### 🧩 Архитектура
- **Language:** Python 3.8+
- **Parallelism:** asyncio/aiohttp для fast concurrent checks
- **Sites:** 400+ социальных сетей и сайтов
- **Output:** console, CSV, XLSX
- **Detection:** HTTP status, response content analysis
- **Entrypoints:** `sherlock/` — main CLI, `sherlock/resources/data.json` — sites list
- **Ключевые файлы:** [sherlock/sherlock.py](https://github.com/sherlock-project/sherlock/blob/master/sherlock/sherlock.py)

### 🧪 Примеры задач
- Поиск всех аккаунтов человека по известному username
- Проверка занятости бренд-имени across platforms
- Security audit: какие аккаунты связаны с сотрудником
- Threat intelligence: tracking adversary accounts
- Social engineering reconnaissance
- Competitor research

### ⚠️ Ограничения
- False positives (сайты могут менять структуру)
- Rate limiting на некоторых сайтах
- Некоторые сайты блокируют automated requests
- Нет гарантии что это тот же человек
- Требует ethical use — не для stalking
- Не все сайты в data.json актуальны

### 🧭 Fit / Maturity / Ops
- **Fit:** OSINT, security research, brand monitoring
- **Maturity:** stable (active maintenance, large community)
- **Latency/Cost:** 10-60s depending on sites, free
- **Data constraints:** только public information
- **Ops friction:** low (pip install, CLI ready)

### Full links
- Repo: https://github.com/sherlock-project/sherlock
- Docs: https://sherlock-project.github.io/sherlock/
- PyPI: https://pypi.org/project/sherlock-project/
- Stars: 72,187
- Maturity: active

---

## MetaGPT

**TL;DR:** Multi-Agent Framework для software development. Симулирует AI Software Company с ролями (PM, Architect, Engineer, QA). Автоматически генерирует PRD → design → code → tests. 63k stars — один из первых successful multi-agent frameworks.

### Быстрый выбор
- ✅ Используй если:
  - Автоматизация software development lifecycle
  - Multi-agent role-based collaboration
  - Complex task decomposition (PRD → code)
  - Want structured output (documents, code, tests)
  - Research multi-agent systems
- ❌ Не используй если:
  - Simple single-agent tasks (overkill)
  - Quick prototypes (setup overhead)
  - Real-time applications (slow)
  - Нужен полный контроль над code quality

### 🚀 Запуск
```bash
# Установка
pip install metagpt

# Конфиг (API keys)
# ~/.metagpt/config2.yaml
# llm:
#   api_type: openai
#   api_key: sk-xxx
#   model: gpt-4

# Запуск software company
metagpt "Create a snake game in Python"

# Python API
from metagpt.software_company import SoftwareCompany
company = SoftwareCompany()
await company.run("Build a todo app with React")
```

### 🧩 Архитектура
- **Language:** Python 3.9+
- **Agents:** ProductManager, Architect, ProjectManager, Engineer, QA
- **Workflow:** requirement → PRD → design → tasks → code → review → tests
- **LLMs:** OpenAI GPT-4, Claude, Gemini, local models
- **Output:** structured documents, complete codebase
- **Entrypoints:** `metagpt/` — core, `metagpt/roles/` — agent roles
- **Ключевые файлы:** [metagpt/actions/](https://github.com/FoundationAgents/MetaGPT/tree/main/metagpt/actions)

### 🧪 Примеры задач
- Generate entire web application from description
- Create game with full codebase и tests
- Build CLI tool с documentation
- Design system architecture documents
- Multi-agent brainstorming и planning
- Automated code review pipeline

### ⚠️ Ограничения
- High token usage (multi-agent = many LLM calls)
- Expensive с GPT-4 (может стоить $5-20 per project)
- Quality varies (не production-ready code)
- Slow execution (minutes per project)
- Complex setup для custom roles
- Requires good initial prompt engineering

### 🧭 Fit / Maturity / Ops
- **Fit:** research, prototyping, automated documentation
- **Maturity:** active (rapid development, но API unstable)
- **Latency/Cost:** slow (5-30 min), expensive ($5-20 per run)
- **Data constraints:** LLM API keys required
- **Ops friction:** medium (config file, API keys)

### Full links
- Repo: https://github.com/FoundationAgents/MetaGPT
- Original README: https://github.com/FoundationAgents/MetaGPT/blob/main/README.md
- Docs: https://docs.deepwisdom.ai
- Discord: https://discord.gg/metagpt
- Stars: 63,449
- Maturity: active

---

## autogen (Microsoft)

**TL;DR:** Microsoft's flagship agentic AI framework. Multi-agent conversations с code execution, function calling, human-in-the-loop. Поддержка GPT-4, Claude, local models. AutoGen Studio для visual agent building. 54k stars — enterprise-grade от Microsoft Research.

### Быстрый выбор
- ✅ Используй если:
  - Multi-agent orchestration с conversations
  - Code generation и execution в sandbox
  - Microsoft/Azure ecosystem
  - Enterprise requirements (security, compliance)
  - Need visual agent builder (AutoGen Studio)
- ❌ Не используй если:
  - Simple single-agent (overkill)
  - Quick prototypes (heavy setup)
  - Prefer LangChain ecosystem
  - Resource-constrained environments

### 🚀 Запуск
```bash
# Core library
pip install pyautogen

# С code execution
pip install pyautogen[code-executor]

# AutoGen Studio (visual UI)
pip install autogenstudio
autogenstudio ui --port 8080
```
```python
from autogen import ConversableAgent, UserProxyAgent

# Создание agents
assistant = ConversableAgent("assistant", llm_config={"model": "gpt-4"})
user_proxy = UserProxyAgent("user_proxy", code_execution_config={"work_dir": "coding"})

# Запуск conversation
user_proxy.initiate_chat(assistant, message="Write a Python script to analyze CSV")
```

### 🧩 Архитектура
- **Language:** Python 3.8+
- **Agents:** ConversableAgent, AssistantAgent, UserProxyAgent, GroupChatManager
- **Execution:** Docker sandbox, local execution, Azure Container Instances
- **LLMs:** OpenAI, Azure OpenAI, Claude, Gemini, local models
- **UI:** AutoGen Studio для visual design
- **Entrypoints:** `autogen/` — core, `autogen/agentchat/` — agent classes
- **Ключевые файлы:** [autogen/agentchat/](https://github.com/microsoft/autogen/tree/main/autogen/agentchat)

### 🧪 Примеры задач
- Multi-agent coding с code review
- Data analysis pipeline с human approval
- Customer support с escalation to human
- Research assistant с web search
- Group chat для brainstorming
- Tool-augmented agents с function calling

### ⚠️ Ограничения
- Complex API (learning curve)
- Heavy dependency footprint
- Code execution requires Docker/sandbox
- Token-expensive для group chats
- AutoGen Studio still maturing
- v0.4+ breaking changes from v0.2

### 🧭 Fit / Maturity / Ops
- **Fit:** enterprise multi-agent, Microsoft ecosystem, research
- **Maturity:** active (Microsoft Research backing, stable roadmap)
- **Latency/Cost:** varies (depends on agents count, LLM)
- **Data constraints:** LLM API keys, optional Azure
- **Ops friction:** medium (setup, config, sandboxing)

### Full links
- Repo: https://github.com/microsoft/autogen
- Original README: https://github.com/microsoft/autogen/blob/main/README.md
- Docs: https://microsoft.github.io/autogen/
- AutoGen Studio: https://autogen-studio.com
- Discord: https://discord.gg/autogen
- Stars: 53,937
- Maturity: active

---

## OpenManus

**TL;DR:** Open-source AI agent framework от FoundationAgents. "No fortress, purely open ground." 53k stars.

### Full links
- Repo: https://github.com/FoundationAgents/OpenManus
- Stars: 53,625
- Maturity: active

---

## ai-agents-for-beginners (Microsoft)

**TL;DR:** 12 Lessons to Get Started Building AI Agents от Microsoft. Educational курс. 49k stars.

### Быстрый выбор
- ✅ Используй если:
  - Learning AI agents
  - Educational purposes
  - Microsoft tech stack
- ❌ Не используй если:
  - Production code нужен

### Full links
- Repo: https://github.com/microsoft/ai-agents-for-beginners
- Stars: 49,454
- Maturity: educational

---

## huginn

**TL;DR:** Self-hosted IFTTT/Zapier альтернатива. Agents мониторят web, выполняют actions, передают data друг другу. Ruby on Rails, visual workflow builder. Classic automation tool до эпохи LLM. 48k stars.

### Быстрый выбор
- ✅ Используй если:
  - Self-hosted automation нужен
  - IFTTT/Zapier слишком дорого или ограничено
  - Web scraping + notifications
  - Email/RSS/webhook processing
  - Data pipelines без cloud lock-in
- ❌ Не используй если:
  - Need AI/LLM agents (Huginn — rule-based)
  - Want managed service (используй Zapier, Make)
  - Prefer Python/Node.js (Huginn — Ruby)
  - Need mobile app triggers

### 🚀 Запуск
```bash
# Docker (recommended)
docker run -d -p 3000:3000 huginn/huginn
# http://localhost:3000
# Default: admin / password

# Docker Compose (with PostgreSQL)
git clone https://github.com/huginn/huginn.git
cd huginn
docker compose up -d

# Manual (Ruby)
git clone https://github.com/huginn/huginn.git
cd huginn
bundle install
cp .env.example .env
rake db:create db:migrate
rails server
```

### 🧩 Архитектура
- **Backend:** Ruby on Rails, PostgreSQL/MySQL
- **Agents:** 50+ built-in (RSS, Email, Web, Twitter, etc.)
- **UI:** web-based visual workflow builder
- **Scheduling:** cron-like для periodic agents
- **Events:** agents communicate via events
- **Entrypoints:** `app/models/agents/` — agent classes
- **Ключевые файлы:** [app/models/agents/](https://github.com/huginn/huginn/tree/master/app/models/agents)

### 🧪 Примеры задач
- Monitor website и email при изменении
- Track price changes и notify via Telegram
- Aggregate RSS feeds и create digest
- Scrape job postings и filter by keywords
- Twitter monitoring с sentiment analysis
- Webhook → transform → forward pipeline

### ⚠️ Ограничения
- Ruby expertise нужен для custom agents
- No LLM/AI integration out of the box
- Memory-hungry (Ruby/Rails overhead)
- UI outdated (functional но не modern)
- Limited community agents vs n8n/Zapier
- SQLite не recommended для production

### 🧭 Fit / Maturity / Ops
- **Fit:** web monitoring, RSS, email automation, self-hosted
- **Maturity:** stable (10+ years, mature but slow development)
- **Latency/Cost:** minutes (scheduled checks), free self-hosted
- **Data constraints:** websites, APIs, email accounts
- **Ops friction:** medium (Docker easy, но Ruby для customization)

### Full links
- Repo: https://github.com/huginn/huginn
- Original README: https://github.com/huginn/huginn/blob/master/README.md
- Wiki: https://github.com/huginn/huginn/wiki
- Docker: https://hub.docker.com/r/huginn/huginn
- Stars: 48,575
- Maturity: active

---

## clawdbot

**TL;DR:** Personal AI assistant. Any OS, any platform. Lobster way 🦞. 43k stars.

### Full links
- Repo: https://github.com/clawdbot/clawdbot
- Original README: https://github.com/clawdbot/clawdbot/blob/main/README.md
- Stars: 43,288
- Maturity: active

---

## crewAI

**TL;DR:** Framework для role-playing autonomous AI agents. Каждый agent имеет роль, goal, backstory. Agents работают вместе как crew с task delegation. Простая декларативная конфигурация. YC-backed. 43k stars — самый user-friendly multi-agent framework.

### Быстрый выбор
- ✅ Используй если:
  - Role-based multi-agent systems (researcher + writer + editor)
  - Collaborative AI tasks с clear roles
  - Want simple YAML-based config
  - Production-ready multi-agent workflows
  - Интеграция с RAG, tools, LangChain
- ❌ Не используй если:
  - Single agent tasks (overkill)
  - Need fine-grained agent control
  - Complex custom agent logic
  - Prefer pure code (vs YAML config)

### 🚀 Запуск
```bash
# Установка
pip install crewai

# CLI scaffold
crewai create crew my-crew
cd my-crew

# Редактируй config/agents.yaml и config/tasks.yaml

# Запуск
python main.py
```
```python
from crewai import Agent, Task, Crew

# Создание agents
researcher = Agent(
    role="Senior Researcher",
    goal="Find innovations in AI",
    backstory="You are a world-class AI researcher",
    llm="gpt-4"
)
writer = Agent(
    role="Tech Writer",
    goal="Write engaging articles",
    backstory="You make complex topics simple"
)

# Tasks
research_task = Task(description="Research latest AI trends", agent=researcher)
write_task = Task(description="Write article from research", agent=writer)

# Crew
crew = Crew(agents=[researcher, writer], tasks=[research_task, write_task])
result = crew.kickoff()
```

### 🧩 Архитектура
- **Language:** Python 3.10+
- **Agents:** role, goal, backstory, tools, llm
- **Tasks:** description, expected_output, agent assignment
- **Crew:** sequential или hierarchical execution
- **Tools:** LangChain tools, custom tools, MCP integration
- **Config:** YAML-based для easy setup
- **Entrypoints:** `crewai/` — core, `crewai/agents/` — agent classes
- **Ключевые файлы:** [crewai/crew.py](https://github.com/crewAIInc/crewAI/blob/main/crewai/crew.py)

### 🧪 Примеры задач
- Research crew: researcher → analyst → writer
- Customer support: classifier → responder → escalator
- Content pipeline: ideator → writer → editor → publisher
- Code review: architect → reviewer → tester
- Data analysis: collector → analyst → visualizer
- Sales team: lead finder → qualifier → closer

### ⚠️ Ограничения
- YAML config может быть limiting для complex logic
- Token usage растёт с количеством agents
- Sequential execution медленнее parallel
- Debugging multi-agent flows сложнее
- Tool integration requires LangChain knowledge
- Premium features в paid CrewAI+ ($$$)

### 🧭 Fit / Maturity / Ops
- **Fit:** content generation, research, workflows с clear roles
- **Maturity:** active (YC backed, production-ready, fast iteration)
- **Latency/Cost:** varies (2-10 min per crew run, depends on tasks)
- **Data constraints:** LLM API keys
- **Ops friction:** low (pip install, YAML config)

### Full links
- Repo: https://github.com/crewAIInc/crewAI
- Original README: https://github.com/crewAIInc/crewAI/blob/main/README.md
- Docs: https://docs.crewai.com
- Cloud: https://crewai.com
- Discord: https://discord.gg/crewai
- Stars: 43,176
- Maturity: active

---

## exo-explore/exo

**TL;DR:** Run AI cluster at home с everyday devices. Distributed inference across laptops, phones, Raspberry Pis. Поддержка Llama, Mistral, DeepSeek. Peer-to-peer без master node. 40k stars — democratizing LLM inference.

### Быстрый выбор
- ✅ Используй если:
  - Хочешь объединить несколько устройств в AI cluster
  - Запустить большие модели на маленьких девайсах (суммируя RAM)
  - Self-hosted LLM inference
  - Экспериментальные distributed systems
  - Есть несколько Mac/Linux machines
- ❌ Не используй если:
  - Single powerful GPU (just use llama.cpp)
  - Production с SLA requirements
  - Windows only (experimental support)
  - Need stable, tested deployment

### 🚀 Запуск
```bash
# Установка
pip install exo

# На каждом устройстве в сети
exo

# Или с explicit cluster discovery
exo --discovery-uri udp://239.0.0.1:5555

# Первый node
exo run llama-3.1-8B --prompt "Hello world"

# На всех других nodes — они автоматически подключатся

# Alternatively, via Python
from exo import Cluster
cluster = Cluster()
response = cluster.generate("llama-3.1-8B", "Hello world")
```

### 🧩 Архитектура
- **Language:** Python 3.10+
- **Discovery:** mDNS/UDP multicast для peer discovery
- **Sharding:** automatic model partitioning across devices
- **Backends:** MLX (Apple Silicon), llama.cpp, TinyGrad
- **Networking:** gRPC для inter-node communication
- **Models:** Llama, Mistral, DeepSeek, Qwen, и др.
- **Entrypoints:** `exo/` — core, `exo/inference/` — inference engines
- **Ключевые файлы:** [exo/distributed/](https://github.com/exo-explore/exo/tree/main/exo/distributed)

### 🧪 Примеры задач
- Объединить 2 MacBook Air M1 16GB для 70B модели
- Raspberry Pi cluster для edge inference
- Use gaming laptop GPU + MacBook вместе
- Distributed inference для privacy (no cloud)
- Home lab AI experimentation
- Cost-effective inference (use existing hardware)

### ⚠️ Ограничения
- Network latency влияет на speed
- Heterogeneous devices (CPU vs GPU) сложно балансировать
- Windows support experimental
- Large models still need significant total RAM
- Not production-ready (experimental project)
- Debugging distributed issues сложно

### 🧭 Fit / Maturity / Ops
- **Fit:** home lab AI, distributed inference experiments
- **Maturity:** experimental (fast development, но unstable APIs)
- **Latency/Cost:** varies wildly (depends on network, devices)
- **Data constraints:** local network, combined device RAM
- **Ops friction:** medium (install on all devices, network config)

### Full links
- Repo: https://github.com/exo-explore/exo
- Original README: https://github.com/exo-explore/exo/blob/main/README.md
- Docs: https://docs.exolabs.net
- Discord: https://discord.gg/exo
- Stars: 40,504
- Maturity: active

---

## twenty

**TL;DR:** Modern open-source альтернатива Salesforce. Полноценный CRM с современным UI. GraphQL API, TypeScript, React. Self-hosted или cloud. Pipelines, contacts, companies, tasks. 39k stars.

### Быстрый выбор
- ✅ Используй если:
  - Open-source CRM needed
  - Salesforce alternative
  - Self-hosted CRM
  - Modern stack (React, GraphQL)
  - Startup/SMB use case
- ❌ Не используй если:
  - Enterprise support needed
  - Complex integrations
  - Legacy system migration
  - Salesforce ecosystem lock-in

### 🚀 Запуск
```bash
git clone https://github.com/twentyhq/twenty && cd twenty
docker compose up -d
# http://localhost:3000
```

### 🧩 Архитектура
- **Frontend:** React, TypeScript
- **Backend:** NestJS, GraphQL
- **Database:** PostgreSQL
- **Features:** contacts, companies, pipelines, tasks
- **Entrypoints:** packages/twenty-front/, packages/twenty-server/

### 🧪 Примеры задач
- Contact management
- Sales pipeline tracking
- Company profiles
- Task management
- Custom fields

### ⚠️ Ограничения
- Early stage product
- Limited integrations
- Self-hosted complexity
- No enterprise support
- Feature gaps vs Salesforce

### 🧭 Fit / Maturity / Ops
- **Fit:** Startup CRM, Salesforce alternative
- **Maturity:** active (fast development)
- **Latency/Cost:** self-hosted free, cloud paid
- **Data constraints:** PostgreSQL
- **Ops friction:** medium (Docker setup)

### Full links
- Repo: https://github.com/twentyhq/twenty
- Original README: https://github.com/twentyhq/twenty/blob/main/README.md
- Stars: 39,064
- Maturity: active

---

## AgentGPT

**TL;DR:** Browser-based autonomous AI agent builder. Assemble, configure, deploy AI agents без кода. Goal-based execution с автономным planning. Web interface для создания agents. 35k stars.

### Быстрый выбор
- ✅ Используй если:
  - Browser-based agent builder
  - No-code agent creation
  - Quick prototypes
  - Goal-based autonomous agents
  - Learning agent concepts
- ❌ Не используй если:
  - Production deployment
  - Custom code needed
  - Complex integrations
  - Enterprise requirements

### 🚀 Запуск
```bash
git clone https://github.com/reworkd/AgentGPT && cd AgentGPT
docker compose up -d
# http://localhost:3000
# Или используй hosted: https://agentgpt.reworkd.ai
```

### 🧩 Архитектура
- **Frontend:** Next.js, TypeScript
- **Backend:** Python, FastAPI
- **LLM:** OpenAI GPT-4
- **Features:** goal setting, task decomposition, autonomous execution
- **Entrypoints:** next/, platform/

### 🧪 Примеры задач
- Research topic autonomously
- Plan project steps
- Create content outlines
- Analyze data
- Generate reports

### ⚠️ Ограничения
- Web-only interface
- Limited tool access
- Experimental stability
- High token usage
- OpenAI dependency

### 🧭 Fit / Maturity / Ops
- **Fit:** Agent prototyping, learning, demos
- **Maturity:** active (but early stage)
- **Latency/Cost:** varies (OpenAI costs)
- **Data constraints:** OpenAI API key
- **Ops friction:** low (hosted) / medium (self-hosted)

### Full links
- Repo: https://github.com/reworkd/AgentGPT
- Original README: https://github.com/reworkd/AgentGPT/blob/main/README.md
- Stars: 35,612
- Maturity: active

---

## Clone-Wars

**TL;DR:** 100+ open-source клонов популярных сайтов. Airbnb, Amazon, Discord, Netflix, Spotify, Twitter и другие. Курированный список для обучения и вдохновения. 33k stars.

### Быстрый выбор
- ✅ Используй если:
  - Learning web development
  - Reference implementations
  - UI inspiration
  - Code patterns study
  - Project ideas
- ❌ Не используй если:
  - Production use
  - Commercial projects
  - Up-to-date APIs
  - Official implementations

### 🚀 Запуск
```bash
# Это курированный список, не код
# Перейди по ссылке и выбери клон для изучения
```

### 🧩 Архитектура
- **Format:** Curated list (README)
- **Categories:** By original site
- **Stacks:** React, Vue, Angular, Node, etc.
- **Quality:** Varies per project
- **Entrypoints:** README.md links

### 🧪 Примеры задач
- Study Airbnb clone architecture
- Learn from Netflix UI patterns
- Understand e-commerce flows
- Practice social media features
- Reference auth implementations

### ⚠️ Ограничения
- Varying quality
- May be outdated
- Not for production
- Different tech stacks
- No unified standards

### 🧭 Fit / Maturity / Ops
- **Fit:** Learning, reference, inspiration
- **Maturity:** curated list (community maintained)
- **Latency/Cost:** free
- **Data constraints:** none
- **Ops friction:** low (just browse)

### Full links
- Repo: https://github.com/GorvGoyl/Clone-Wars
- Original README: https://github.com/GorvGoyl/Clone-Wars/blob/main/README.md
- Stars: 33,604
- Maturity: curated list

---

## goose (Block)

**TL;DR:** Open source AI agent от Block (Square/Cash App). Полноценный developer agent — не просто code suggestions, а install deps, execute, edit, test. Работает с любым LLM. CLI-first. MCP support. 29k stars.

### Быстрый выбор
- ✅ Используй если:
  - AI coding assistant с full system access
  - CLI-based development workflow
  - Want BYO LLM (any provider)
  - Need more than code suggestions (install, run, test)
  - MCP tools integration
- ❌ Не используй если:
  - GUI IDE integration нужна (используй Cursor, Windsurf)
  - Fear giving AI system access
  - Prefer sandboxed environments
  - Need enterprise support

### 🚀 Запуск
```bash
# Установка via pipx (recommended)
pipx install goose-ai

# Или pip
pip install goose-ai

# Конфиг LLM
goose configure
# Выбери provider: OpenAI, Anthropic, Ollama, etc.

# Запуск в текущей директории
cd my-project
goose

# С конкретной задачей
goose "Add unit tests for the auth module"

# Session mode
goose --session my-session
```

### 🧩 Архитектура
- **Language:** Python 3.10+
- **LLMs:** OpenAI, Anthropic, Google, Ollama, Together, any OpenAI-compatible
- **Tools:** file ops, shell execution, web search
- **MCP:** full MCP server support для extensibility
- **Sessions:** persistent sessions с history
- **Safety:** confirmation for destructive actions
- **Entrypoints:** `goose/` — core, `goose/toolkit/` — built-in tools
- **Ключевые файлы:** [src/goose/](https://github.com/block/goose/tree/main/src/goose)

### 🧪 Примеры задач
- "Set up this project with proper linting and testing"
- "Find the bug causing the test failure and fix it"
- "Refactor this module to use async/await"
- "Add Docker support to this project"
- "Explain how the authentication flow works"
- Multi-step development workflows

### ⚠️ Ограничения
- Requires trust — goose can execute system commands
- No GUI (CLI only)
- LLM costs depending on provider
- Complex tasks may need guidance
- MCP ecosystem still growing
- Windows support может быть limited

### 🧭 Fit / Maturity / Ops
- **Fit:** CLI developers, AI-assisted coding, automation
- **Maturity:** active (Block backing, rapid development)
- **Latency/Cost:** depends on LLM (seconds per action)
- **Data constraints:** LLM API keys, codebase access
- **Ops friction:** low (pip install, configure LLM)

### Full links
- Repo: https://github.com/block/goose
- Original README: https://github.com/block/goose/blob/main/README.md
- Docs: https://block.github.io/goose/
- Stars: 29,095
- Maturity: active

---

## FastGPT

**TL;DR:** Knowledge-based platform built on LLMs. RAG, data processing, visual workflow. 27k stars.

### Быстрый выбор
- ✅ Используй если:
  - Нужен knowledge base с RAG
  - Visual workflow builder
  - Self-hosted solution
- ❌ Не используй если:
  - Simple chatbot
  - No storage needed

### 🚀 Запуск
```bash
git clone https://github.com/labring/FastGPT.git
cd FastGPT/docker-compose
docker compose up -d
# http://localhost:3000
```

### Full links
- Repo: https://github.com/labring/FastGPT
- Original README: https://github.com/labring/FastGPT/blob/main/README.md
- Stars: 27,000
- Maturity: active

---

## Hitomi-Downloader

**TL;DR:** Desktop utility to download images/videos/music/text from various websites. 27k stars.

### Быстрый выбор
- ✅ Используй если:
  - Нужен mass media downloader
  - Multi-site support
  - Desktop app preferred
- ❌ Не используй если:
  - Single site only
  - CLI preferred

### 🚀 Запуск
```bash
# Download from releases
# https://github.com/KurtBestor/Hitomi-Downloader/releases
```

### Full links
- Repo: https://github.com/KurtBestor/Hitomi-Downloader
- Original README: https://github.com/KurtBestor/Hitomi-Downloader/blob/master/README.md
- Stars: 27,281
- Maturity: active

---

## composio

**TL;DR:** Tooling platform для AI agents — 150+ pre-built integrations (GitHub, Slack, Gmail, etc.) через function calling. SDKs для Python/JS, работает с любым agent framework (LangChain, CrewAI, AutoGen). MCP compatible. 26k stars — де-факто стандарт для agent tools.

### Быстрый выбор
- ✅ Используй если:
  - Нужны ready-to-use integrations для AI agents
  - Function calling с OAuth (GitHub, Google, Slack)
  - Multi-framework support (LangChain, CrewAI, OpenAI)
  - Want managed auth handling (OAuth flows)
  - MCP tools для Claude/VSCode agents
- ❌ Не используй если:
  - Simple LLM calls без tools
  - Custom integrations only
  - Want fully self-hosted (cloud component required)
  - Allergic to third-party services

### 🚀 Запуск
```bash
# Python SDK
pip install composio-core

# Node.js SDK
npm install composio-core

# Login
composio login
```
```python
from composio_openai import ComposioToolSet, App
from openai import OpenAI

# Initialize
toolset = ComposioToolSet()
openai_client = OpenAI()

# Get tools
tools = toolset.get_tools(apps=[App.GITHUB])

# Use with OpenAI
response = openai_client.chat.completions.create(
    model="gpt-4",
    tools=tools,
    messages=[{"role": "user", "content": "Star the repo composio/composio"}]
)

# Execute tool call
result = toolset.handle_tool_calls(response)
```

### 🧩 Архитектура
- **SDKs:** Python, JavaScript/TypeScript
- **Integrations:** 150+ apps (GitHub, Slack, Gmail, Notion, Jira, etc.)
- **Auth:** OAuth2, API key management, connection per user
- **Frameworks:** OpenAI, LangChain, CrewAI, AutoGen, LlamaIndex
- **MCP:** full Model Context Protocol support
- **Actions:** 1000+ pre-built actions across apps
- **Entrypoints:** `composio/` — core SDK, `composio/tools/` — tool definitions
- **Ключевые файлы:** [python/composio/](https://github.com/ComposioHQ/composio/tree/main/python/composio)

### 🧪 Примеры задач
- AI agent создаёт GitHub issues и PRs
- Slack bot с calendar integration
- Email assistant читает Gmail, создаёт drafts
- Research agent сохраняет в Notion
- Customer support agent создаёт Jira tickets
- Multi-tool workflows с multiple OAuth connections

### ⚠️ Ограничения
- Cloud service required для auth management
- Free tier limitations (connections, executions)
- Some integrations в beta
- Custom integrations require more work
- Debugging OAuth flows может быть tricky
- Pricing может быть expensive для high volume

### 🧭 Fit / Maturity / Ops
- **Fit:** AI agents needing external integrations, enterprise tools
- **Maturity:** active (YC backed, rapid development)
- **Latency/Cost:** low latency, free tier available, paid для high volume
- **Data constraints:** OAuth connections, API keys via Composio
- **Ops friction:** low (pip install, login, use)

### Full links
- Repo: https://github.com/ComposioHQ/composio
- Original README: https://github.com/ComposioHQ/composio/blob/main/README.md
- Docs: https://docs.composio.dev
- Dashboard: https://app.composio.dev
- Stars: 26,439
- Maturity: active

---

## awesome-claude-skills

**TL;DR:** Curated list of Claude Skills, resources, tools. Коллекция примеров skills для Claude: MCP servers, prompts, integrations. Используй для learning и вдохновения. 26k stars.

### Быстрый выбор
- ✅ Используй если:
  - Claude skills examples
  - MCP server примеры
  - Learning Claude capabilities
  - Prompt engineering examples
  - Integration ideas
- ❌ Не используй если:
  - Non-Claude models
  - Production code
  - Actual implementations
  - OpenAI/Gemini focus

### 🚀 Запуск
```bash
# Это курированный список, не код
# Перейди по ссылке и выбери skill для изучения
```

### 🧩 Архитектура
- **Format:** Curated list (README)
- **Categories:** MCP, prompts, tools, integrations
- **Quality:** Community curated
- **Entrypoints:** README.md links

### 🧪 Примеры задач
- Find MCP server examples
- Learn prompt patterns
- Discover integrations
- Study skill architecture
- Get project ideas

### ⚠️ Ограничения
- List only, no code
- Varying quality
- May be outdated
- Claude-specific
- Community maintained

### 🧭 Fit / Maturity / Ops
- **Fit:** Learning, reference, Claude ecosystem
- **Maturity:** curated list (active curation)
- **Latency/Cost:** free
- **Data constraints:** none
- **Ops friction:** low (just browse)

### Full links
- Repo: https://github.com/ComposioHQ/awesome-claude-skills
- Original README: https://github.com/ComposioHQ/awesome-claude-skills/blob/main/README.md
- Stars: 26,260
- Maturity: curated list

---

## postiz-app

**TL;DR:** Ultimate social media scheduling tool with AI. Open-source alternative to Buffer/Hootsuite. AI-generated posts, scheduling для Twitter, LinkedIn, Facebook, etc. Analytics и team collaboration. 26k stars.

### Быстрый выбор
- ✅ Используй если:
  - Social media scheduling для команды
  - AI-powered content generation
  - Multi-platform posting (Twitter, LinkedIn, etc.)
  - Open-source self-hosted solution
  - Analytics & growth tracking
- ❌ Не используй если:
  - Single platform only (native tools лучше)
  - No need for AI writing
  - SaaS dependency OK (use Buffer)

### 🚀 Запуск
```bash
git clone https://github.com/gitroomhq/postiz-app && cd postiz-app
docker compose up -d
# http://localhost:4200
```

### 🧩 Архитектура
- **Frontend:** Next.js
- **Backend:** NestJS, Prisma
- **Database:** PostgreSQL, Redis
- **AI:** OpenAI/Claude integration
- **Integrations:** Twitter, LinkedIn, Facebook APIs
- **Entrypoints:** apps/frontend/, apps/backend/

### 🧪 Примеры задач
- Schedule threads for Twitter
- Generate LinkedIn posts with AI
- Track engagement metrics
- Manage multiple client accounts
- Visual calendar planning

### ⚠️ Ограничения
- Requires API keys for platforms
- Self-hosted maintenance
- AI costs (OpenAI keys)
- Complex Docker setup
- Platform API changes risk

### 🧭 Fit / Maturity / Ops
- **Fit:** Social media teams, agencies, creators
- **Maturity:** active (frequent updates)
- **Latency/Cost:** self-hosted free, AI paid
- **Data constraints:** PostgreSQL storage
- **Ops friction:** medium (Docker)

### Full links
- Repo: https://github.com/gitroomhq/postiz-app
- Original README: https://github.com/gitroomhq/postiz-app/blob/main/README.md
- Stars: 26,223
- Maturity: active
- Stars: 26,223
- Maturity: active

---

## e2b-dev/awesome-ai-agents

**TL;DR:** Curated list of AI autonomous agents. Коллекция agent frameworks, tools, и research papers. От AutoGPT до BabyAGI и MetaGPT. Используй для research и сравнения agents. 25k stars.

### Быстрый выбор
- ✅ Используй если:
  - AI agent frameworks overview
  - Research autonomous agents
  - Comparing agent solutions
  - Finding new projects
  - Learning agent ecosystem
- ❌ Не используй если:
  - Need specific implementation
  - Production code
  - Single framework choice
  - Non-agent LLM use

### 🚀 Запуск
```bash
# Это курированный список
# Перейди по ссылке и выбери agent framework
```

### 🧩 Архитектура
- **Format:** Curated list (README)
- **Categories:** Frameworks, tools, research
- **Curation:** E2B team maintained
- **Entrypoints:** README.md links

### 🧪 Примеры задач
- Compare agent frameworks
- Find new projects
- Research agent architectures
- Discover tools
- Track ecosystem trends

### ⚠️ Ограничения
- List only
- May be outdated
- Varying quality
- No recommendations
- Community curated

### 🧭 Fit / Maturity / Ops
- **Fit:** Research, comparison, learning
- **Maturity:** curated list (E2B maintained)
- **Latency/Cost:** free
- **Data constraints:** none
- **Ops friction:** low (browse)

### Full links
- Repo: https://github.com/e2b-dev/awesome-ai-agents
- Original README: https://github.com/e2b-dev/awesome-ai-agents/blob/main/README.md
- Stars: 25,420
- Maturity: curated list

---

## agents-course (HuggingFace)

**TL;DR:** HuggingFace Agents Course. Полный курс по AI agents от HuggingFace. От basics до advanced multi-agent systems. Hands-on notebooks, видео, практические проекты. 25k stars.

### Быстрый выбор
- ✅ Используй если:
  - Learning AI agents
  - HuggingFace ecosystem
  - Structured course preferred
  - Hands-on learning
  - Beginner to intermediate
- ❌ Не используй если:
  - Already expert in agents
  - Need production code
  - Non-HuggingFace stack
  - Just reference docs

### 🚀 Запуск
```bash
git clone https://github.com/huggingface/agents-course
cd agents-course
# Открой notebooks в Jupyter/Colab
```

### 🧩 Архитектура
- **Format:** Course (notebooks, text, video)
- **Topics:** agent basics, tools, memory, multi-agent
- **Platform:** HuggingFace Hub
- **Entrypoints:** notebooks/, units/

### 🧪 Примеры задач
- Learn agent fundamentals
- Build tool-using agents
- Implement memory systems
- Create multi-agent workflows
- Complete hands-on projects

### ⚠️ Ограничения
- Educational, не production
- HuggingFace focus
- Time investment needed
- May require GPU
- Evolving content

### 🧭 Fit / Maturity / Ops
- **Fit:** Learning, education, skill building
- **Maturity:** educational (HuggingFace official)
- **Latency/Cost:** free (Colab GPU)
- **Data constraints:** HuggingFace account
- **Ops friction:** low (Colab ready)

### Full links
- Repo: https://github.com/huggingface/agents-course
- Original README: https://github.com/huggingface/agents-course/blob/main/README.md
- Stars: 24,990
- Maturity: educational

---

## UI-TARS-desktop (ByteDance)

**TL;DR:** Multimodal AI Agent Stack от ByteDance. Computer use агент для desktop automation. Vision + GUI interaction. Screen understanding, mouse/keyboard control, task execution. Electron app. 25k stars.

### Быстрый выбор
- ✅ Используй если:
  - Multimodal AI agents
  - Desktop automation
  - Computer use experiments
  - GUI automation
  - Vision-based tasks
- ❌ Не используй если:
  - Simple chat agents
  - API-only automation
  - Headless servers
  - Production stability needed

### 🚀 Запуск
```bash
git clone https://github.com/bytedance/UI-TARS-desktop && cd UI-TARS-desktop
npm install
npm run build
npm start
```

### 🧩 Архитектура
- **App:** Electron desktop
- **Vision:** Screen capture, OCR
- **Control:** Mouse, keyboard automation
- **Models:** VLM for understanding
- **Entrypoints:** electron/, src/

### 🧪 Примеры задач
- Automate desktop workflows
- Fill forms automatically
- Navigate applications
- Extract screen data
- Execute multi-step tasks

### ⚠️ Ограничения
- Experimental
- Desktop only
- Resource intensive
- Security considerations
- Platform-specific

### 🧭 Fit / Maturity / Ops
- **Fit:** Desktop automation, computer use research
- **Maturity:** active (ByteDance backed)
- **Latency/Cost:** depends on VLM
- **Data constraints:** screen access
- **Ops friction:** medium (Electron setup)

### Full links
- Repo: https://github.com/bytedance/UI-TARS-desktop
- Original README: https://github.com/bytedance/UI-TARS-desktop/blob/main/README.md
- Stars: 24,851
- Maturity: active

---

## langgraph

**TL;DR:** Graph-based framework для building agent workflows от LangChain team. State machines, cycles, persistence, human-in-the-loop. The orchestration layer for LangChain. LangGraph Studio для visual debugging. 24k stars.

### Быстрый выбор
- ✅ Используй если:
  - Complex agent workflows с branching
  - Need state persistence и checkpointing
  - Human-in-the-loop approval flows
  - LangChain ecosystem интеграция
  - Want visual debugging (LangGraph Studio)
- ❌ Не используй если:
  - Simple linear LLM chains (use LangChain directly)
  - Prefer simpler frameworks (CrewAI)
  - Not invested in LangChain ecosystem
  - Single-turn chatbots

### 🚀 Запуск
```bash
# Установка
pip install langgraph

# С LangChain
pip install langgraph langchain-openai
```
```python
from langgraph.graph import StateGraph, END
from typing import TypedDict

# Define state
class AgentState(TypedDict):
    messages: list
    next_step: str

# Create graph
graph = StateGraph(AgentState)

# Add nodes
graph.add_node("research", research_node)
graph.add_node("write", write_node)
graph.add_node("review", review_node)

# Add edges
graph.add_edge("research", "write")
graph.add_conditional_edges("write", should_continue, {"review": "review", "end": END})
graph.add_edge("review", END)

# Set entry
graph.set_entry_point("research")

# Compile
app = graph.compile()

# Run
result = app.invoke({"messages": [], "next_step": "research"})
```

### 🧩 Архитектура
- **Language:** Python 3.9+
- **Graphs:** StateGraph с nodes и edges
- **State:** TypedDict-based state management
- **Persistence:** checkpointing, time-travel debugging
- **Human-in-loop:** interrupt и resume capabilities
- **Studio:** LangGraph Studio для visual debugging
- **Entrypoints:** `langgraph/` — core, `langgraph/prebuilt/` — common patterns
- **Ключевые файлы:** [langgraph/graph/](https://github.com/langchain-ai/langgraph/tree/main/libs/langgraph/langgraph/graph)

### 🧪 Примеры задач
- Multi-step research workflow с conditional routing
- Document processing pipeline с review steps
- Customer support с escalation paths
- Code review agent с multiple reviewers
- Approval workflows с human checkpoints
- Complex RAG с query analysis и routing

### ⚠️ Ограничения
- Learning curve (graph concepts)
- Debugging complex graphs непросто
- LangChain dependency (tight coupling)
- Overhead для simple use cases
- State management может быть verbose
- Studio requires LangSmith account

### 🧭 Fit / Maturity / Ops
- **Fit:** complex agent workflows, enterprise AI apps, LangChain users
- **Maturity:** active (LangChain backing, production-ready)
- **Latency/Cost:** depends on graph complexity и LLM
- **Data constraints:** LLM API keys, optional LangSmith
- **Ops friction:** medium (setup, graph design)

### Full links
- Repo: https://github.com/langchain-ai/langgraph
- Original README: https://github.com/langchain-ai/langgraph/blob/main/README.md
- Docs: https://langchain-ai.github.io/langgraph/
- Studio: https://studio.langchain.com
- Discord: https://discord.gg/langchain
- Stars: 23,791
- Maturity: active

---

## radare2

**TL;DR:** UNIX-like reverse engineering framework. Complete toolset для analysis of binaries, disassembly, debugging, и forensics. Command-line first, scriptable (r2pipe). Поддерживает кучу architectures/formats. 23k stars.

### Быстрый выбор
- ✅ Используй если:
  - Reverse engineering binaries (lightweight)
  - Malware analysis automation
  - CTF challenges
  - Scripting analysis pipeline (Python/News)
  - Need support for exotic architectures
- ❌ Не используй если:
  - GUI preferred (use Ghidra/IDA Pro)
  - Steep learning curve scares you
  - Simple hex editing (use simpler tools)
  - Decompiler quality is top priority (Ghidra better)

### 🚀 Запуск
```bash
git clone https://github.com/radareorg/radare2.git
cd radare2
sys/install.sh
r2 binary_file
# Внутри r2:
# aaa  <- analyze all
# pdf  <- print disassembly function
# V    <- visual mode
```

### 🧩 Архитектура
- **Core:** C, modular design
- **IO:** plugins for file formats/debuggers
- **Analysis:** code analysis, type propagation
- **Scripting:** r2pipe (JS, Python, Go, etc.)
- **Entrypoints:** `libr/`, `binr/`

### 🧪 Примеры задач
- Static analysis of unknown binary
- Patching executables
- Exploit development
- Automated unpacking scripts
- Firmware analysis

### ⚠️ Ограничения
- Steep learning curve (Vim-like commands)
- Decompiler (pdc) слабее Ghidra
- CLI interface не для всех
- Documentation spread out
- Experimental features stability

### 🧭 Fit / Maturity / Ops
- **Fit:** NetSec, Reverse Engineering, CTF
- **Maturity:** very mature (standard tool)
- **Latency/Cost:** free, extremely fast
- **Data constraints:** local files
- **Ops friction:** medium (learning curve)

### Full links
- Repo: https://github.com/radareorg/radare2
- Original README: https://github.com/radareorg/radare2/blob/master/README.md
- Book: https://book.rada.re
- Stars: 22,987
- Maturity: active

---

## chrome-devtools-mcp

**TL;DR:** Chrome DevTools for coding agents. Official MCP server connecting AI agents to Chrome via DevTools Protocol. Inspect pages, execute Console, debug network, view DOM. Enables "DevTools Agent". 22k stars.

### Быстрый выбор
- ✅ Используй если:
  - AI agents need browser debugging/inspection
  - Chrome automation via standard protocols
  - MCP integration for Claude/IDEs
  - Extracting complex data from SPAs
  - Accessibility testing automation
- ❌ Не используй если:
  - Non-Chrome browsers
  - High-performance scraping (use specialized tools)
  - Simple HTTP requests enough
  - Headless only environments without Chrome

### 🚀 Запуск
```bash
# Requires Chrome running with remote debugging
# chrome --remote-debugging-port=9222

npx -y @modelcontextprotocol/server-chrome
# Configure in Claude Desktop / Cursor
```

### 🧩 Архитектура
- **Protocol:** MCP (Model Context Protocol)
- **Transport:** Chrome DevTools Protocol (CDP)
- **Tools:** Console, DOM, Network, Page, Runtime
- **Entrypoints:** `src/index.ts`

### 🧪 Примеры задач
- Agent fixes Console errors automatically
- CSS debugging via AI
- Verifying accessibility tags
- Extracting dynamic content
- Network request analysis

### ⚠️ Ограничения
- Requires running Chrome instance
- Connectivity flakiness
- Security (access to open tabs)
- Chrome update dependency
- Local execution only

### 🧭 Fit / Maturity / Ops
- **Fit:** AI debugging assistants, web agents
- **Maturity:** active (Google official)
- **Latency/Cost:** local execution, free
- **Data constraints:** local browser data
- **Ops friction:** low (npx execution)

### Full links
- Repo: https://github.com/ChromeDevTools/chrome-devtools-mcp
- Original README: https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md
- Stars: 22,319
- Maturity: active

---

## chatterbox (Resemble AI)

**TL;DR:** SoTA open-source TTS. Text-to-speech framework focused on realism and control. Поддержка voice cloning, emotion control, и multi-speaker synthesis. PyTorch based. 22k stars.

### Быстрый выбор
- ✅ Используй если:
  - High-quality self-hosted TTS
  - Voice cloning / custom voices
  - Audio synthesis research
  - Control over prosody/emotion
  - Offline generation required
- ❌ Не используй если:
  - Simple API calls okay (use ElevenLabs/OpenAI)
  - Low resource environment (mobile/web)
  - Real-time ultra-low latency critical
  - No GPU available

### 🚀 Запуск
```bash
pip install chatterbox-tts
# or from source
git clone https://github.com/resemble-ai/chatterbox
cd chatterbox
pip install -r requirements.txt
python synthesize.py --text "Hello world" --voice "demo_voice"
```

### 🧩 Архитектура
- **Backbone:** PyTorch
- **Models:** FastSpeech2 / VITS based architectures
- **Vocoders:** HiFi-GAN
- **Input:** Text/Phonemes
- **Output:** Wav/Audio
- **Entrypoints:** `chatterbox/` core library

### 🧪 Примеры задач
- Generate voiceovers for content
- Accessible interfaces (screen readers)
- Voice cloning for games/mods
- Researching new TTS architectures
- Local assistant voice

### ⚠️ Ограничения
- GPU recommended for speed
- Voice cloning quality varies
- Model training takes time
- Python environment dependency
- License constraints (check specific model)

### 🧭 Fit / Maturity / Ops
- **Fit:** TTS implementation, Voice AI
- **Maturity:** active (Resemble AI backed)
- **Latency/Cost:** free (self-hosted), GPU cost
- **Data constraints:** training data rights
- **Ops friction:** medium (Python/GPU setup)

### Full links
- Repo: https://github.com/resemble-ai/chatterbox
- Original README: https://github.com/resemble-ai/chatterbox/blob/main/README.md
- Stars: 21,940
- Maturity: active

---

## A2A (Agent-to-Agent Protocol)

**TL;DR:** Open protocol для inter-agent communication от Google. Стандартизирует как agents обнаруживают друг друга, обмениваются capabilities, и делегируют tasks. Companion to MCP (tools) — A2A для agent↔agent, MCP для agent↔tools. 22k stars.

### Быстрый выбор
- ✅ Используй если:
  - Building multi-agent systems
  - Need standardized agent communication
  - Want interoperability между разными agent frameworks
  - Enterprise-grade multi-agent orchestration
  - Researching agent protocols
- ❌ Не используй если:
  - Single agent applications
  - Prefer custom protocols
  - Simple task automation
  - Not ready for bleeding-edge tech

### 🚀 Запуск
```bash
# Python SDK (in development)
pip install a2a-sdk

# Reference implementations
git clone https://github.com/a2aproject/A2A.git
cd A2A/samples/python
```
```python
# Conceptual example (API evolving)
from a2a import Agent, A2AServer

# Create agent with capabilities
agent = Agent(
    name="ResearchAgent",
    capabilities=["web_search", "summarize"]
)

# Register with A2A server
server = A2AServer()
server.register(agent)

# Discover other agents
available_agents = server.discover(capability="code_review")

# Delegate task to another agent
result = await agent.delegate(
    to=available_agents[0],
    task={"instruction": "Review this code", "data": code}
)
```

### 🧩 Архитектура
- **Protocol:** JSON-based, HTTP/WebSocket transport
- **Discovery:** Agent cards для capability advertising
- **Tasks:** structured task delegation и results
- **Auth:** built-in authentication и authorization
- **Streaming:** support for long-running tasks
- **Spec:** [A2A Specification](https://github.com/a2aproject/A2A/blob/main/spec.md)
- **Relationship:** A2A (agent↔agent) + MCP (agent↔tools)
- **Entrypoints:** `spec/` — protocol spec, `samples/` — implementations

### 🧪 Примеры задач
- Research agent delegates code review to specialized agent
- Orchestrator coordinates multiple specialist agents
- Agent marketplace с capability discovery
- Cross-framework agent communication (CrewAI ↔ LangChain)
- Enterprise multi-agent workflows с audit trail
- Federated agent networks

### ⚠️ Ограничения
- Very early stage (protocol still evolving)
- Limited library support (SDKs in development)
- No production deployments yet
- Documentation sparse
- Competing with proprietary solutions
- Adoption unclear

### 🧭 Fit / Maturity / Ops
- **Fit:** research, multi-agent architecture, protocol design
- **Maturity:** experimental (Google backing, but early)
- **Latency/Cost:** depends on implementation
- **Data constraints:** agent registration, network access
- **Ops friction:** high (early, limited tooling)

### Full links
- Repo: https://github.com/a2aproject/A2A
- Original README: https://github.com/a2aproject/A2A/blob/main/README.md
- Spec: https://github.com/a2aproject/A2A/blob/main/spec.md
- Google Blog: https://developers.googleblog.com/a2a
- Stars: 21,608
- Maturity: active

---

## modelcontextprotocol/python-sdk

**TL;DR:** Official Python SDK for MCP servers and clients. Стройте MCP servers и clients используя native Python. FastMCP для быстрого старта. Поддержка stdio и SSE transports. Основа для Python-integration в Claude ecosystem. 21k stars.

### Быстрый выбор
- ✅ Используй если:
  - Building MCP server на Python
  - Connecting Python tools to Claude
  - Integration с existing Python libraries
  - Need standard MCP compliance
  - Fast prototyping (FastMCP)
- ❌ Не используй если:
  - TypeScript/Node.js stack preferred (use TS SDK)
  - Go/Rust stack preferred (use other SDKs)
  - Don't need MCP (use standard API)

### 🚀 Запуск
```bash
pip install mcp
```
```python
from mcp.server.fastmcp import FastMCP

# Initialize server
mcp = FastMCP("My Weather Server")

# Define tool
@mcp.tool()
def get_weather(location: str) -> str:
    """Get weather for a location"""
    return f"Weather in {location} is Sunny"

# Run server
# mcp run weather.py
```

### 🧩 Архитектура
- **Core:** `mcp` package
- **Components:** Server, Client, Transports (stdio, SSE)
- **FastMCP:** High-level decorator-based API
- **Types:** Pydantic models for protocol messages
- **Entrypoints:** `src/mcp/`

### 🧪 Примеры задач
- Wrap existing Python script как MCP tool
- Create database access MCP server
- Connect proprietary API to Claude
- Build specialized calculation tools
- Integrate ML models as MCP tools

### ⚠️ Ограничения
- Python environment required
- Stdio transport limitations (no logs to stdout)
- Less mature than TS SDK (getting there)
- Async-first (sync users need wrappers)
- Validation errors handling

### 🧭 Fit / Maturity / Ops
- **Fit:** Python devs, ML engineers, data scientists building agents
- **Maturity:** active (Official Anthropic supported)
- **Latency/Cost:** local execution, depends on tool
- **Data constraints:** local data access
- **Ops friction:** low (pip install)

### Full links
- Repo: https://github.com/modelcontextprotocol/python-sdk
- Original README: https://github.com/modelcontextprotocol/python-sdk/blob/main/README.md
- Docs: https://modelcontextprotocol.io/
- Stars: 21,341
- Maturity: active

---

## stagehand (Browserbase)

**TL;DR:** AI-powered browser automation framework. Playwright + AI = natural language browser control. act() → AI figures out how to click/fill. extract() → AI extracts data. observe() → AI observes page state. 21k stars.

### Быстрый выбор
- ✅ Используй если:
  - Browser automation с AI understanding
  - Scraping dynamic sites с AI extraction
  - Testing flows в natural language
  - Want Playwright reliability + AI flexibility
  - Building browser-based AI agents
- ❌ Не используй если:
  - Simple static scraping (BeautifulSoup faster)
  - Known selectors (Playwright directly faster)
  - No LLM budget for AI calls
  - Full determinism required

### 🚀 Запуск
```bash
# Установка
npm install @browserbasehq/stagehand

# Playwright setup
npx playwright install
```
```typescript
import { Stagehand } from "@browserbasehq/stagehand";

const stagehand = new Stagehand({
  env: "LOCAL",  // or "BROWSERBASE" for cloud
  modelName: "gpt-4o",
  modelClientOptions: { apiKey: process.env.OPENAI_API_KEY }
});

await stagehand.init();
await stagehand.page.goto("https://example.com");

// AI actions
await stagehand.page.act({ action: "click the login button" });
await stagehand.page.act({ action: "fill email with test@example.com" });

// AI extraction
const data = await stagehand.page.extract({
  instruction: "extract all product prices",
  schema: z.object({ prices: z.array(z.number()) })
});

// AI observation
const state = await stagehand.page.observe();
```

### 🧩 Архитектура
- **Language:** TypeScript
- **Browser:** Playwright (Chromium, Firefox, WebKit)
- **AI:** OpenAI GPT-4, Anthropic Claude
- **Methods:** act() (actions), extract() (data), observe() (state)
- **Modes:** LOCAL (your machine), BROWSERBASE (cloud)
- **Schema:** Zod for type-safe extraction
- **Entrypoints:** `lib/` — core, `lib/handlers/` — action handlers
- **Ключевые файлы:** [lib/stagehand.ts](https://github.com/browserbase/stagehand/blob/main/lib/stagehand.ts)

### 🧪 Примеры задач
- "Login to LinkedIn and send connection request"
- "Extract all job postings matching React developer"
- "Fill out multi-step form with my data"
- "Navigate e-commerce and add to cart"
- "Scrape dynamic SPA with infinite scroll"
- End-to-end testing в natural language

### ⚠️ Ограничения
- LLM costs для каждого AI action
- Slower than direct Playwright selectors
- AI might misinterpret complex UIs
- Captcha still challenging
- Rate limits на AI providers
- Browserbase cloud = additional cost

### 🧭 Fit / Maturity / Ops
- **Fit:** AI browser automation, dynamic scraping, flow testing
- **Maturity:** active (Browserbase backed, rapid development)
- **Latency/Cost:** 1-5s per action, LLM costs + optional Browserbase
- **Data constraints:** OpenAI/Anthropic API key
- **Ops friction:** low (npm install, Playwright setup)

### Full links
- Repo: https://github.com/browserbase/stagehand
- Original README: https://github.com/browserbase/stagehand/blob/main/README.md
- Docs: https://docs.stagehand.dev
- Browserbase: https://browserbase.com
- Stars: 20,591
- Maturity: active

---

## mastra

**TL;DR:** TypeScript framework для AI-powered applications от team behind Gatsby. Opinionated framework: agents, workflows, RAG, integrations out of the box. Vercel-style DX. 20k stars.

### Быстрый выбор
- ✅ Используй если:
  - TypeScript/Node.js stack
  - Want opinionated AI framework (batteries included)
  - Agents + workflows + RAG нужны together
  - Prefer Vercel-style developer experience
  - Building full-stack AI apps
- ❌ Не используй если:
  - Python preferred (use LangChain, CrewAI)
  - Want minimal framework
  - Only need one feature (agents OR RAG)
  - Learning AI concepts (too opinionated)

### 🚀 Запуск
```bash
# Create new project
npx create-mastra-app my-app
cd my-app

# Or add to existing
npm install @mastra/core

# Run dev server
npm run dev
```
```typescript
import { Agent, Workflow, RAG } from '@mastra/core';

// Create agent
const agent = new Agent({
  name: 'support-agent',
  model: 'gpt-4',
  tools: [searchKnowledgeBase, createTicket]
});

// Create workflow
const workflow = new Workflow({
  steps: [
    { action: 'classify', agent },
    { action: 'respond', agent },
    { action: 'escalate', condition: 'needsHuman' }
  ]
});

// Run
const result = await workflow.run({ query: "How do I reset my password?" });
```

### 🧩 Архитектура
- **Language:** TypeScript, Node.js
- **Agents:** declarative agent definitions с tools
- **Workflows:** step-based workflow orchestration
- **RAG:** built-in vector store, embeddings, retrieval
- **Integrations:** pre-built connectors (similar to Composio)
- **Deploy:** Vercel, AWS Lambda, any Node.js runtime
- **Entrypoints:** `packages/core/` — main library
- **Ключевые файлы:** [packages/core/src/](https://github.com/mastra-ai/mastra/tree/main/packages/core/src)

### 🧪 Примеры задач
- Customer support agent с knowledge base
- Content generation workflow
- Data processing pipeline с AI
- Multi-step approval workflow
- RAG-powered documentation search
- Full-stack AI SaaS application

### ⚠️ Ограничения
- TypeScript only (no Python)
- Opinionated — less flexibility
- Newer framework (less community)
- Some features still maturing
- Documentation still growing
- Migration from other frameworks не trivial

### 🧭 Fit / Maturity / Ops
- **Fit:** TypeScript AI apps, full-stack developers
- **Maturity:** active (fast development, но young)
- **Latency/Cost:** depends on LLM и workflow complexity
- **Data constraints:** LLM API keys
- **Ops friction:** low (npm install, similar to Next.js)

### Full links
- Repo: https://github.com/mastra-ai/mastra
- Original README: https://github.com/mastra-ai/mastra/blob/main/README.md
- Docs: https://mastra.ai/docs
- Examples: https://github.com/mastra-ai/examples
- Stars: 20,486
- Maturity: active

---

## activepieces

**TL;DR:** Open-source Zapier/n8n alternative с AI и MCP support. 400+ integrations, AI workflow templates, visual builder. Self-hosted или cloud. 20k stars — modern automation platform.

### Быстрый выбор
- ✅ Используй если:
  - Self-hosted automation platform
  - Zapier/Make/n8n alternative
  - AI-powered workflows нужны
  - MCP servers integration
  - Visual workflow builder preferred
- ❌ Не используй если:
  - Code-first preference (use n8n code nodes)
  - Minimal footprint needed
  - Enterprise support critical (n8n enterprise better)
  - Pure AI agents (use CrewAI, LangChain)

### 🚀 Запуск
```bash
# Docker (recommended)
docker run -d \
  -p 8080:8080 \
  -v activepieces_data:/app/data \
  activepieces/activepieces

# Docker Compose
git clone https://github.com/activepieces/activepieces.git
cd activepieces
docker compose up -d

# http://localhost:8080
```

### 🧩 Архитектура
- **Backend:** Node.js, TypeScript, NestJS
- **Frontend:** Angular
- **Database:** PostgreSQL, Redis
- **Pieces:** 400+ pre-built integrations
- **AI:** OpenAI, Claude, Gemini integrations
- **MCP:** 400+ MCP server connectors
- **Entrypoints:** `packages/backend/` — API, `packages/ui/` — frontend
- **Ключевые файлы:** [packages/pieces/](https://github.com/activepieces/activepieces/tree/main/packages/pieces)

### 🧪 Примеры задач
- Sync data between CRM и marketing tools
- AI-powered email responder
- Social media scheduler с content generation
- Customer support automation с AI triage
- Data pipeline с multiple sources
- Alert system с Slack/Email notifications

### ⚠️ Ограничения
- Resource-heavy для self-hosted
- Learning curve для complex flows
- Some pieces less mature
- Angular frontend (less common)
- Migration from Zapier/n8n не seamless
- Enterprise features в paid cloud

### 🧭 Fit / Maturity / Ops
- **Fit:** business automation, AI workflows, integration platform
- **Maturity:** active (fast development, production-ready)
- **Latency/Cost:** real-time triggers, free self-hosted
- **Data constraints:** API credentials для integrations
- **Ops friction:** medium (Docker setup, но well-documented)

### Full links
- Repo: https://github.com/activepieces/activepieces
- Original README: https://github.com/activepieces/activepieces/blob/main/README.md
- Docs: https://activepieces.com/docs
- Cloud: https://cloud.activepieces.com
- Stars: 20,512
- Maturity: active

---

## GenAI_Agents

**TL;DR:** Tutorials and implementations for Generative AI Agent techniques. Comprehensive collection of agent patterns: CoT, ReAct, RAG, Plan-and-Solve. Реализации популярных research papers. Отличный образовательный ресурс. 19k stars.

### Быстрый выбор
- ✅ Используй если:
  - Learning agent architectures
  - Implementing specific techniques (ReAct / CoT)
  - Researching state-of-the-art patterns
  - Need reference implementations
  - Educational purposes
- ❌ Не используй если:
  - Production framework needed
  - Drop-in solution
  - No Python knowledge
  - Enterprise support required

### 🚀 Запуск
```bash
git clone https://github.com/NirDiamant/GenAI_Agents
cd GenAI_Agents
# Explore Jupyter notebooks
jupyter notebook
```

### 🧩 Архитектура
- **Format:** Jupyter Notebooks, Python scripts
- **Topics:** RAG, CoT, ReAct, Multi-Agent, Evaluation
- **Frameworks:** LangChain, LlamaIndex, OpenAI
- **Entrypoints:** `notebooks/` per technique

### 🧪 Примеры задач
- Implement ReAct pattern from scratch
- Build RAG pipeline with advanced retrieval
- Create multi-agent debate system
- Evaluate agent performance
- Study Chain-of-Thought reasoning

### ⚠️ Ограничения
- Educational code
- Not a cohesive framework
- Varying dependencies
- Maintenance varies per notebook
- No standardized API

### 🧭 Fit / Maturity / Ops
- **Fit:** Education, research, reference
- **Maturity:** educational (active updates)
- **Latency/Cost:** free (notebook execution)
- **Data constraints:** local execution
- **Ops friction:** low (Jupyter setup)

### Full links
- Repo: https://github.com/NirDiamant/GenAI_Agents
- Original README: https://github.com/NirDiamant/GenAI_Agents/blob/main/README.md
- Stars: 19,550
- Maturity: educational

---

## suna (Kortix AI)

**TL;DR:** Open-source AI agent platform — build, manage, deploy agents через visual interface. Task automation, web browsing, file management. Docker-based self-hosted. Growing fast. 19k stars.

### Быстрый выбор
- ✅ Используй если:
  - Visual agent platform
  - Self-hosted requirement
  - Task automation
  - Web browsing agents
  - File management automation
- ❌ Не используй если:
  - Code-first approach preferred
  - Lightweight solution needed
  - Specific frameworks required
  - Enterprise SLA needed

### 🚀 Запуск
```bash
# Docker (recommended)
git clone https://github.com/kortix-ai/suna.git
cd suna
docker compose up -d

# http://localhost:3000
```

### 🧩 Архитектура
- **Backend:** Python, FastAPI
- **Frontend:** React
- **Agents:** browser, file system, code execution
- **LLMs:** OpenAI, Anthropic, local
- **Deploy:** Docker Compose
- **Entrypoints:** `docker-compose.yml`
- **Ключевые файлы:** [backend/](https://github.com/kortix-ai/suna)

### 🧪 Примеры задач
- Web research automation
- File organization
- Data extraction workflows
- Report generation
- Multi-step task chains

### ⚠️ Ограничения
- Resource requirements (Docker)
- Learning curve
- Documentation evolving
- Some features beta
- Community growing

### 🧭 Fit / Maturity / Ops
- **Fit:** task automation, visual agents, self-hosted
- **Maturity:** active (rapid development)
- **Latency/Cost:** depends on LLM usage
- **Data constraints:** LLM API keys
- **Ops friction:** medium (Docker setup)

### Full links
- Repo: https://github.com/kortix-ai/suna
- Original README: https://github.com/kortix-ai/suna/blob/main/README.md
- Stars: 19,248
- Maturity: active

---

## bolt.diy (Stackblitz)

**TL;DR:** Community fork of bolt.new с multi-LLM support — OpenAI, Claude, Gemini, local Ollama. Same WebContainers magic, но any model. Open source self-hosted. 19k stars — the "open" bolt.new.

### Быстрый выбор
- ✅ Используй если:
  - bolt.new с own API keys
  - Local LLM support (Ollama)
  - Self-hosted requirements
  - Model flexibility (not locked to Claude)
  - Community features
- ❌ Не используй если:
  - Want official support (use bolt.new)
  - No local setup (cloud preferred)
  - Simple projects (bolt.new easier)

### 🚀 Запуск
```bash
# Clone
git clone https://github.com/stackblitz-labs/bolt.diy.git
cd bolt.diy

# Install
pnpm install

# Configure .env
cp .env.example .env
# Add API keys

# Run
pnpm dev

# http://localhost:5173
```

### 🧩 Архитектура
- **Frontend:** React, Vite
- **Runtime:** WebContainers (Node.js in browser)
- **AI:** OpenAI, Anthropic, Google, Ollama, any OpenAI-compatible
- **Editor:** Monaco
- **Deploy:** self-hosted, Vercel possible
- **Entrypoints:** `src/` — frontend
- **Ключевые файлы:** [app/](https://github.com/stackblitz-labs/bolt.diy)

### 🧪 Примеры задач
- Same as bolt.new but with own keys
- Local LLM web app generation
- Cost optimization (cheaper models)
- Privacy-sensitive development
- Experimentation with models

### ⚠️ Ограничения
- Community maintained (unofficial)
- Setup more complex than bolt.new
- Some features may lag official
- Browser limitations same as bolt.new
- WebContainers quirks

### 🧭 Fit / Maturity / Ops
- **Fit:** self-hosted bolt.new, multi-LLM, privacy
- **Maturity:** active (community-driven)
- **Latency/Cost:** your API costs, control
- **Data constraints:** your LLM API keys
- **Ops friction:** medium (setup required)

### Full links
- Repo: https://github.com/stackblitz-labs/bolt.diy
- Original README: https://github.com/stackblitz-labs/bolt.diy/blob/main/README.md
- Original: https://bolt.new
- Stars: 18,940
- Maturity: active

---

## Qwen3-VL

**TL;DR:** State-of-the-art multimodal Vision-Language Model от Alibaba Cloud. Image understanding, video analysis, OCR, document parsing. Multiple sizes (2B, 7B, 72B). Open weights. 18k stars.

### Быстрый выбор
- ✅ Используй если:
  - Vision-language tasks
  - Image understanding/captioning
  - Document/OCR processing
  - Video understanding
  - Open-weight requirement
- ❌ Не используй если:
  - Text-only tasks (use Qwen3)
  - Minimal compute (large models)
  - Commercial restrictions concern

### 🚀 Запуск
```bash
# Install
pip install transformers accelerate

# Load model
from transformers import Qwen2VLForConditionalGeneration, AutoProcessor

model = Qwen2VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2-VL-7B-Instruct",
    torch_dtype="auto",
    device_map="auto"
)
processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-7B-Instruct")

# Process image + text
messages = [{"role": "user", "content": [
    {"type": "image", "image": "image.jpg"},
    {"type": "text", "text": "Describe this image"}
]}]
```

### 🧩 Архитектура
- **Models:** 2B, 7B, 72B parameters
- **Modalities:** text, image, video
- **Tasks:** VQA, OCR, captioning, document understanding
- **License:** Apache 2.0 (open weights)
- **Framework:** Transformers, vLLM
- **Ключевые файлы:** [README.md](https://github.com/QwenLM/Qwen3-VL)

### 🧪 Примеры задач
- "Describe what's in this image"
- "Extract text from this document"
- "Answer questions about this video"
- "Parse this invoice/receipt"
- UI understanding for agents

### ⚠️ Ограничения
- Large GPU requirements (7B+ needs 16GB+)
- Slower than text-only models
- Some languages better than others
- Video processing resource-intensive

### 🧭 Fit / Maturity / Ops
- **Fit:** vision-language, OCR, multimodal agents
- **Maturity:** production (Alibaba backing)
- **Latency/Cost:** GPU required, self-hosted
- **Data constraints:** local weights
- **Ops friction:** medium (GPU setup)

### Full links
- Repo: https://github.com/QwenLM/Qwen3-VL
- Original README: https://github.com/QwenLM/Qwen3-VL/blob/main/README.md
- HuggingFace: https://huggingface.co/Qwen
- Stars: 17,991
- Maturity: active

---

## Janus (DeepSeek)

**TL;DR:** Unified multimodal model от DeepSeek — и understanding, и generation в одной модели. Image understanding + image generation. More efficient than separate models. Open weights. 18k stars.

### Быстрый выбор
- ✅ Используй если:
  - Unified vision understanding + generation
  - Single model для both tasks
  - Open-weight requirement
  - Research/experimentation
  - DeepSeek ecosystem
- ❌ Не используй если:
  - Only generation (use SDXL)
  - Only understanding (use Qwen-VL)
  - Production stability critical
  - Limited GPU resources

### 🚀 Запуск
```bash
# Install
pip install transformers accelerate

# Load model (example)
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained(
    "deepseek-ai/Janus-1.3B",
    trust_remote_code=True
)
```

### 🧩 Архитектура
- **Models:** 1.3B, larger variants
- **Capabilities:** image understanding, image generation (unified)
- **Approach:** decoupled visual encoding
- **License:** open weights
- **Framework:** Transformers, PyTorch
- **Ключевые файлы:** [janus/](https://github.com/deepseek-ai/Janus)

### 🧪 Примеры задач
- "Describe this image and generate a similar one"
- Unified VQA + generation pipeline
- Multimodal chat with image creation
- Research into unified models

### ⚠️ Ограничения
- Newer/experimental approach
- Generation quality vs specialized models
- GPU requirements significant
- Less community tooling
- Documentation evolving

### 🧭 Fit / Maturity / Ops
- **Fit:** research, unified multimodal, experimentation
- **Maturity:** active (DeepSeek backing)
- **Latency/Cost:** GPU required, self-hosted
- **Data constraints:** local weights
- **Ops friction:** medium (GPU setup)

### Full links
- Repo: https://github.com/deepseek-ai/Janus
- Original README: https://github.com/deepseek-ai/Janus/blob/main/README.md
- DeepSeek: https://www.deepseek.com
- Stars: 17,687
- Maturity: active

---

## eliza (elizaOS)

**TL;DR:** TypeScript multi-agent simulation framework. Autonomous agents с personality, memory, relationships. Discord, Twitter, Telegram integrations. Crypto/DeFi focus с wallet management. Originally for AI companions/characters. 17k stars.

### Быстрый выбор
- ✅ Используй если:
  - Autonomous AI characters/companions
  - Social media bots (Discord, Twitter, Telegram)
  - Multi-agent simulations
  - Crypto/DeFi agents с wallet management
  - Memory и relationship tracking
- ❌ Не используй если:
  - Enterprise workflows (use LangGraph)
  - Code generation agents (use Goose, Claude CLI)
  - Simple chatbots (overkill)
  - Non-social use cases

### 🚀 Запуск
```bash
# Clone
git clone https://github.com/elizaOS/eliza.git
cd eliza

# Install
pnpm install

# Configure
cp .env.example .env
# Edit .env with API keys

# Run
pnpm start

# Or Docker
docker compose up
```

### 🧩 Архитектура
- **Language:** TypeScript, Node.js
- **Agents:** personality-driven с goals, beliefs, relationships
- **Memory:** persistent memory, relationship tracking
- **Platforms:** Discord, Twitter/X, Telegram, custom
- **Crypto:** wallet management, DeFi integrations
- **LLMs:** OpenAI, Anthropic, local models
- **Entrypoints:** `packages/core/` — core logic, `packages/client-*` — platform clients
- **Ключевые файлы:** [packages/core/src/](https://github.com/elizaOS/eliza/tree/main/packages/core/src)

### 🧪 Примеры задач
- AI companion с consistent personality
- Discord community manager bot
- Twitter agent для engagement
- Multi-agent roleplay simulation
- Crypto trading bot с personality
- Customer engagement agent

### ⚠️ Ограничения
- Crypto-focused (may be overkill for non-crypto)
- Complex setup (many components)
- Personality tuning takes time
- Platform integrations change frequently
- Memory can grow large
- Rate limits на social platforms

### 🧭 Fit / Maturity / Ops
- **Fit:** AI companions, social agents, crypto bots
- **Maturity:** active (large community, rapid development)
- **Latency/Cost:** depends on LLM и platform
- **Data constraints:** LLM keys, platform API keys
- **Ops friction:** medium (config, platform setup)

### Full links
- Repo: https://github.com/elizaOS/eliza
- Original README: https://github.com/elizaOS/eliza/blob/main/README.md
- Docs: https://elizaos.github.io/eliza/
- Discord: https://discord.gg/elizaos
- Stars: 17,420
- Maturity: active

---

## SuperAGI

**TL;DR:** Dev-first autonomous AI agent framework с GUI, marketplace, и provisioning infrastructure. Multiple concurrent agents, tool extensions, vector DB memory. Production-focused alternative to AutoGPT. 17k stars.

### Быстрый выбор
- ✅ Используй если:
  - Multiple concurrent agents
  - GUI для agent management
  - Tool marketplace integration
  - Production autonomous agents
  - Resource provisioning needed
- ❌ Не используй если:
  - Single-agent simple tasks
  - CLI-only preference
  - Lightweight solution needed
  - Non-Docker environments

### 🚀 Запуск
```bash
# Clone
git clone https://github.com/TransformerOptimus/SuperAGI.git
cd SuperAGI

# Docker (recommended)
docker compose up -d

# http://localhost:3000

# Or local
pip install -r requirements.txt
python main.py
```

### 🧩 Архитектура
- **Backend:** Python, FastAPI
- **Frontend:** Next.js React
- **Database:** PostgreSQL, Redis
- **Memory:** Weaviate, Pinecone vector stores
- **Tools:** extensible marketplace
- **Agents:** concurrent execution
- **Entrypoints:** `main.py` — backend, `gui/` — frontend
- **Ключевые файлы:** [superagi/](https://github.com/TransformerOptimus/SuperAGI/tree/main/superagi)

### 🧪 Примеры задач
- Research agent parallel execution
- Code generation с multiple specialists
- Web scraping agent fleet
- Content creation pipeline
- Data processing workflows
- Autonomous task chains

### ⚠️ Ограничения
- Resource-heavy (Docker, databases)
- Complex setup
- Less active than peak development
- Some features incomplete
- Documentation gaps
- Community smaller now

### 🧭 Fit / Maturity / Ops
- **Fit:** autonomous agents, multi-agent, GUI management
- **Maturity:** stable (but less active now)
- **Latency/Cost:** LLM costs, infrastructure costs
- **Data constraints:** LLM keys, vector DB
- **Ops friction:** medium (Docker Compose)

### Full links
- Repo: https://github.com/TransformerOptimus/SuperAGI
- Original README: https://github.com/TransformerOptimus/SuperAGI/blob/main/README.md
- Docs: https://superagi.com/docs
- Discord: https://discord.gg/superagi
- Stars: 17,121
- Maturity: active

---

## bolt.new (Stackblitz)

**TL;DR:** AI-powered full-stack web app generator от Stackblitz. Prompt → running app in browser. WebContainers technology — no Docker, runs Node.js in browser. Deploy to Netlify. Claude powered. 16k stars.

### Быстрый выбор
- ✅ Используй если:
  - Rapid web app prototyping
  - Non-developers building apps
  - Browser-based development preferred
  - Want instant deployment
  - React/Vue/Svelte apps
- ❌ Не используй если:
  - Complex backend systems
  - Non-web applications
  - Need full IDE control
  - Enterprise requirements
  - Specific framework versions needed

### 🚀 Запуск
```bash
# bolt.new is a hosted service
# Visit: https://bolt.new

# For self-hosted fork (bolt.diy):
git clone https://github.com/stackblitz-labs/bolt.diy.git
cd bolt.diy
pnpm install
pnpm dev
```

### 🧩 Архитектура
- **Frontend:** React, Vite
- **Runtime:** WebContainers (Node.js in browser)
- **AI:** Claude for code generation
- **Deploy:** Netlify integration
- **Output:** React, Vue, Svelte, Node.js apps
- **IDE:** Monaco editor in browser
- **Entrypoints:** browser-based (or bolt.diy for self-hosted)
- **Ключевые файлы:** [bolt.diy repo](https://github.com/stackblitz-labs/bolt.diy)

### 🧪 Примеры задач
- "Create a todo app with React and Tailwind"
- "Build a landing page with pricing section"
- "Make a dashboard with charts"
- "Create an API with Express"
- Iterate on UI with natural language
- Deploy prototype в minutes

### ⚠️ Ограничения
- Web apps only (no mobile, desktop)
- WebContainers have limitations vs real Node
- Claude only (no model choice in official)
- Limited backend complexity
- No database management (external only)
- Paid для higher usage

### 🧭 Fit / Maturity / Ops
- **Fit:** web prototypes, MVPs, learning, quick demos
- **Maturity:** production (Stackblitz backing)
- **Latency/Cost:** seconds for generation, free tier available
- **Data constraints:** Claude API (handled by Stackblitz)
- **Ops friction:** zero (browser-based)

### Full links
- Repo: https://github.com/stackblitz/bolt.new
- Original README: https://github.com/stackblitz/bolt.new/blob/main/README.md
- App: https://bolt.new
- DIY fork: https://github.com/stackblitz-labs/bolt.diy
- Stars: 16,160
- Maturity: active

---

## camel-ai/camel

**TL;DR:** Pioneer multi-agent framework — первый исследовательский paper о communicative agents (CAMEL paper). Role-playing agent conversations, structured prompting. Research-oriented. "Scaling Law of Agents" concept. 16k stars.

### Быстрый выбор
- ✅ Используй если:
  - Research multi-agent communication
  - Role-playing agent conversations
  - Academic/research use cases
  - Want structured agent prompting
  - Exploring "Scaling Law of Agents"
- ❌ Не используй если:
  - Production systems (use CrewAI, AutoGen)
  - Simple agent tasks
  - Need enterprise support
  - Want visual builder

### 🚀 Запуск
```bash
# Установка
pip install camel-ai

# Или с extras
pip install camel-ai[all]
```
```python
from camel.agents import ChatAgent
from camel.messages import BaseMessage
from camel.models import ModelFactory, ModelType

# Create model
model = ModelFactory.create(ModelType.GPT_4)

# Create agents
assistant = ChatAgent(
    system_message="You are a helpful AI assistant.",
    model=model
)
user = ChatAgent(
    system_message="You are a curious user.",
    model=model
)

# Role-playing conversation
user_msg = BaseMessage.make_user_message("How do I learn Python?")
response = assistant.step(user_msg)
print(response.msg.content)
```

### 🧩 Архитектура
- **Language:** Python 3.10+
- **Agents:** ChatAgent, RoleplayingAgent, CriticAgent
- **Communication:** structured message passing
- **Roles:** flexible role definitions
- **Models:** OpenAI, Anthropic, Gemini, local
- **Research:** reproducible experiments
- **Entrypoints:** `camel/` — core, `camel/agents/` — agent classes
- **Ключевые файлы:** [camel/agents/](https://github.com/camel-ai/camel/tree/main/camel/agents)

### 🧪 Примеры задач
- Two-agent role-playing (AI assistant + AI user)
- Code generation с AI reviewer
- Research experiments с controlled communication
- Debate simulation между agents
- Task decomposition research
- Agent communication protocol experiments

### ⚠️ Ограничения
- Research-focused (not production-optimized)
- Less tooling than CrewAI/AutoGen
- Documentation more academic
- Community smaller
- API changes between versions
- Some features experimental

### 🧭 Fit / Maturity / Ops
- **Fit:** AI research, academic experiments, communication studies
- **Maturity:** active (research backing, но experimental)
- **Latency/Cost:** depends on agents count и LLM
- **Data constraints:** LLM API keys
- **Ops friction:** low (pip install)

### Full links
- Repo: https://github.com/camel-ai/camel
- Original README: https://github.com/camel-ai/camel/blob/main/README.md
- Docs: https://camel-ai.github.io/camel/
- Paper: https://arxiv.org/abs/2303.17760
- Discord: https://discord.gg/camelai
- Stars: 15,813
- Maturity: active

---

## browser-use/web-ui

**TL;DR:** Web UI для browser-use library — запускай AI browser agents через браузерный интерфейс. Vision-capable agents, step-by-step execution, recording. Gradio-based UI. 15k stars.

### Быстрый выбор
- ✅ Используй если:
  - Want visual browser agent interface
  - Debug agent browser actions
  - Demo browser automation
  - Non-coders running browser agents
  - Record agent sessions
- ❌ Не используй если:
  - Production automation (use browser-use directly)
  - Headless operations
  - CLI preferred
  - High-volume automation

### 🚀 Запуск
```bash
# Clone
git clone https://github.com/browser-use/web-ui.git
cd web-ui

# Install
pip install -r requirements.txt

# Run
python app.py
# http://localhost:7860
```

### 🧩 Архитектура
- **Frontend:** Gradio web interface
- **Backend:** browser-use library
- **Browser:** Playwright (Chromium)
- **AI:** OpenAI GPT-4V, Claude 3
- **Features:** step execution, recording, vision mode
- **Entrypoints:** `app.py` — main, `agent/` — agent logic
- **Ключевые файлы:** [app.py](https://github.com/browser-use/web-ui/blob/main/app.py)

### 🧪 Примеры задач
- Visual demo of browser agent
- Debug why agent clicked wrong element
- Record agent session для presentation
- Train non-technical users on agents
- Interactive testing of prompts
- Step-through browser automation

### ⚠️ Ограничения
- UI-based (slower than programmatic)
- Gradio limitations
- Single user at a time
- Not for production
- Requires display/screen
- Resource-intensive (browser + AI)

### 🧭 Fit / Maturity / Ops
- **Fit:** demos, debugging, learning, presentations
- **Maturity:** active (browser-use ecosystem)
- **Latency/Cost:** LLM costs per action
- **Data constraints:** LLM API key
- **Ops friction:** low (pip install, run)

### Full links
- Repo: https://github.com/browser-use/web-ui
- Original README: https://github.com/browser-use/web-ui/blob/main/README.md
- Main lib: https://github.com/browser-use/browser-use
- Stars: 15,516
- Maturity: active

---

## AstrBot

**TL;DR:** Agentic IM Chatbot infrastructure. Каркас для создания чат-ботов с поддержкой LLM и плагинов. Поддержка популярных платформ (Telegram, WeChat, QQ). Visual management setup. 15k stars.

### Быстрый выбор
- ✅ Используй если:
  - Building IM bots (WeChat/Telegram)
  - Need visual config management
  - LLM integration с разными провайдерами
  - Plugin system requirement
  - Self-hosted bot platform
- ❌ Не используй если:
  - Enterprise support required
  - Custom code preference over config UI
  - English-first documentation preferred (mostly Chinese)
  - Simple lightweight bot needed

### 🚀 Запуск
```bash
git clone https://github.com/AstrBotDevs/AstrBot
cd AstrBot
pip install -r requirements.txt
python main.py
# Open Admin UI at http://localhost:8080
```

### 🧩 Архитектура
- **Core:** Python
- **Platforms:** OneBot, Telegram, WeChat
- **LLM:** OpenAI, Gemini, local LLMs
- **Plugins:** Python-based plugin system
- **UI:** Web-based management console
- **Entrypoints:** `main.py`

### 🧪 Примеры задач
- WeChat customer support bot
- Telegram group management AI
- Personal assistant в мессенджере
- Multi-platform notification bot
- Custom skill implementation

### ⚠️ Ограничения
- Documentation mostly Chinese
- Community primarily Chinese
- WeChat bot stability issues (platform side)
- Setup complexity
- Plugin quality varies

### 🧭 Fit / Maturity / Ops
- **Fit:** IM bots, Asian market platforms (WeChat/QQ)
- **Maturity:** active (large community)
- **Latency/Cost:** depends on LLM
- **Data constraints:** self-hosted
- **Ops friction:** medium (platform config)

### Full links
- Repo: https://github.com/AstrBotDevs/AstrBot
- Original README: https://github.com/AstrBotDevs/AstrBot/blob/main/README.md
- Docs: https://astrbot.org
- Stars: 15,212
- Maturity: active

---

## csm (SesameAILabs)

**TL;DR:** Conversational Speech Generation Model. Continuous Speech Model — generation of long-form conversational speech. Open source. 14k stars.

### Быстрый выбор
- ✅ Используй если:
  - Generating long conversational audio
  - Speech synthesis research
  - Conversational AI with voice
  - Open model requirement
- ❌ Не используй если:
  - Simple short phrase TTS
  - Production latency constraints
  - Low compute resources

### 🚀 Запуск
```bash
git clone https://github.com/SesameAILabs/csm
cd csm
# Follow instructions in repo (research code)
```

### 🧩 Архитектура
- **Model:** Continuous Speech Model
- **Focus:** Long-form coherence
- **Input:** Text/Context
- **Output:** Audio waveforms
- **Entrypoints:** Research scripts

### 🧪 Примеры задач
- Generate podcast dialogue
- Create virtual character speech
- Research long-form synthesis properties
- Benchmark speech models

### ⚠️ Ограничения
- Research code status
- Compute intensive
- Less polished than commercial APIs
- Documentation academic
- Setup complexity

### 🧭 Fit / Maturity / Ops
- **Fit:** Audio research, conversational AI
- **Maturity:** research (experimental)
- **Latency/Cost:** high compute
- **Data constraints:** local models
- **Ops friction:** high (research setup)

### Full links
- Repo: https://github.com/SesameAILabs/csm
- Original README: https://github.com/SesameAILabs/csm/blob/main/README.md
- Stars: 14,880
- Maturity: research

### Full links
- Repo: https://github.com/SesameAILabs/csm
- Original README: https://github.com/SesameAILabs/csm/blob/main/README.md
- Stars: 14,462
- Maturity: active

---

## motia

**TL;DR:** Multi-Language Backend Framework. Каркас для создания backend-систем с поддержкой разных языков (Python, JS, Go). Unified API, job queues, workflows и AI agent support. Микросервисная архитектура in a box. 14k stars.

### Быстрый выбор
- ✅ Используй если:
  - Polyglot microservices architecture
  - Unified backend framework
  - Workflow orchestration needed
  - Team uses multiple languages
  - AI agent integration in backend
- ❌ Не используй если:
  - Single language stack sufficient (Django/NestJS)
  - Simple monolithic app
  - Restricted ecosystem adoption
  - Small team/solo dev

### 🚀 Запуск
```bash
git clone https://github.com/MotiaDev/motia
cd motia
# Follow setup in docs for specific language bindings
```

### 🧩 Архитектура
- **Core:** Distributed backend kernel
- **Languages:** Python, JavaScript/TypeScript, Go
- **Components:** API Gateway, Job Queue, Workflow Engine
- **AI:** Integration hooks for agents
- **Entrypoints:** `server/`

### 🧪 Примеры задач
- Unified API for multi-language services
- Distributed background jobs
- Complex business logic workflows
- AI agent orchestration backend
- Cross-language service mesh

### ⚠️ Ограничения
- Learning curve (new paradigm)
- Complexity of distributed systems
- Documentation gaps
- Smaller community than major frameworks
- Integration overhead

### 🧭 Fit / Maturity / Ops
- **Fit:** Microservices, polyglot teams, complex backends
- **Maturity:** active (growing)
- **Latency/Cost:** overhead of distributed system
- **Data constraints:** self-hosted
- **Ops friction:** high (setup distributed env)

### Full links
- Repo: https://github.com/MotiaDev/motia
- Original README: https://github.com/MotiaDev/motia/blob/main/README.md
- Stars: 14,434
- Maturity: active

---

## agent-zero

**TL;DR:** Personal assistant framework с long-term memory, tool usage, и multi-agent support. Runs locally или in Docker. Persistent memory across sessions. Terminal, browser, file access. Self-improving через learnings. 14k stars.

### Быстрый выбор
- ✅ Используй если:
  - Personal AI assistant
  - Long-term memory важна
  - Self-hosted preference
  - Tool calling с terminal/browser
  - Self-improving agent behavior
- ❌ Не используй если:
  - Team/enterprise use (single-user focused)
  - Production API service
  - Simple chatbot needed
  - Quick one-off tasks

### 🚀 Запуск
```bash
# Clone
git clone https://github.com/agent0ai/agent-zero.git
cd agent-zero

# Install
pip install -r requirements.txt

# Configure
cp .env.example .env
# Edit .env with API keys

# Run
python run.py

# Or Docker
docker compose up
```

### 🧩 Архитектура
- **Language:** Python
- **Memory:** persistent vector memory (ChromaDB)
- **Tools:** terminal, browser, file system, custom
- **LLMs:** OpenAI, Anthropic, local models
- **UI:** web interface (Flask)
- **Features:** learnings, multi-agent, self-improvement
- **Entrypoints:** `run.py` — main, `agent/` — core logic
- **Ключевые файлы:** [agent/](https://github.com/agent0ai/agent-zero/tree/main/agent)

### 🧪 Примеры задач
- Personal coding assistant с project context
- Research assistant с memory of past queries
- System admin helper (terminal commands)
- File organization assistant
- Learning journal (remembers your preferences)
- Multi-step task planning и execution

### ⚠️ Ограничения
- Single-user design
- Memory grows large over time
- Resource-intensive
- Some features experimental
- UI basic
- Not production-ready API

### 🧭 Fit / Maturity / Ops
- **Fit:** personal AI assistant, hobbyist projects
- **Maturity:** active (responsive maintainer)
- **Latency/Cost:** depends on LLM, memory queries add time
- **Data constraints:** LLM key, local storage для memory
- **Ops friction:** medium (setup, memory management)

### Full links
- Repo: https://github.com/agent0ai/agent-zero
- Discord: https://discord.gg/agent0
- Stars: 13,900
- Maturity: active
---

## MoneyPrinterV2

**TL;DR:** Automate YouTube Shorts/TikTok content creation. AI generates script, voiceover (TTS), finds stock footage, edits video, uploads. Fully automated content pipeline. 13k stars — viral passive income automation.

### Быстрый выбор
- ✅ Используй если:
  - Automated video content creation
  - YouTube Shorts/TikTok скриптованные
  - Passive content income
  - Bulk video generation
  - AI voiceover + stock footage
- ❌ Не используй если:
  - Original creative content
  - Quality over quantity
  - Human touch important
  - Platform ToS concerns
  - Non-video content

### 🚀 Запуск
```bash
# Clone
git clone https://github.com/FujiwaraChoki/MoneyPrinterV2.git
cd MoneyPrinterV2

# Install
pip install -r requirements.txt

# Configure
cp .env.example .env
# Add API keys: OpenAI, Pexels, ElevenLabs, YouTube

# Run
python main.py
```

### 🧩 Архитектура
- **Language:** Python
- **AI:** OpenAI GPT для scripts
- **TTS:** ElevenLabs, Google TTS
- **Footage:** Pexels API stock videos
- **Editing:** MoviePy для video assembly
- **Upload:** YouTube API автоматизация
- **Entrypoints:** `main.py` — main runner
- **Ключевые файлы:** [src/](https://github.com/FujiwaraChoki/MoneyPrinterV2/tree/main/src)

### 🧪 Примеры задач
- "Generate 10 videos about crypto tips"
- "Create daily motivational shorts"
- "Automated news summary videos"
- "Faceless YouTube channel automation"
- "TikTok content farm"
- Bulk upload scheduled content

### ⚠️ Ограничения
- Platform ToS risks (content farms)
- Quality varies significantly
- AI detection в platforms
- API costs add up
- Stock footage repetitive
- May get flagged for spam

### 🧭 Fit / Maturity / Ops
- **Fit:** content automation, passive income experiments
- **Maturity:** active (but check platform compliance)
- **Latency/Cost:** minutes per video, API costs
- **Data constraints:** OpenAI, ElevenLabs, Pexels, YouTube APIs
- **Ops friction:** medium (multiple API keys)

### Full links
- Repo: https://github.com/FujiwaraChoki/MoneyPrinterV2
- Original README: https://github.com/FujiwaraChoki/MoneyPrinterV2/blob/main/README.md
- Stars: 12,953
- Maturity: active

---

## Photon

**TL;DR:** Lightning-fast OSINT web crawler. Extracts URLs, emails, social accounts, files, JS, keys из websites. Single-page focus с depth crawling. Threaded для speed. 13k stars.

### Быстрый выбор
- ✅ Используй если:
  - OSINT reconnaissance
  - Extract emails/accounts from site
  - Find exposed API keys/secrets
  - Map website structure
  - Security assessment
- ❌ Не используй если:
  - Full site scraping (use Scrapy)
  - Dynamic JS sites (use Playwright)
  - Rate-limited sites
  - Need structured data extraction

### 🚀 Запуск
```bash
# Install
git clone https://github.com/s0md3v/Photon.git
cd Photon
pip install -r requirements.txt

# Basic scan
python photon.py -u https://example.com

# With options
python photon.py -u https://example.com \
  -l 3 \           # depth level
  -t 10 \          # threads
  -o output_dir \  # output directory
  --keys           # extract API keys
```

### 🧩 Архитектура
- **Language:** Python 3
- **Crawling:** threaded HTTP requests
- **Extraction:** regex patterns для emails, keys, accounts
- **Output:** organized directory structure
- **Features:** DNS extraction, robots.txt parsing
- **Entrypoints:** `photon.py` — main
- **Ключевые файлы:** [photon.py](https://github.com/s0md3v/Photon/blob/master/photon.py)

### 🧪 Примеры задач
- "Find all email addresses on competitor site"
- "Extract all JS files for analysis"
- "Map all internal/external links"
- "Find exposed API keys in code"
- "Discover social media accounts"
- Pre-pentest reconnaissance

### ⚠️ Ограничения
- Static content only (no JS rendering)
- Aggressive crawling can get blocked
- Basic auth not supported well
- No proxy rotation built-in
- Output format basic
- Maintenance less active

### 🧭 Fit / Maturity / Ops
- **Fit:** OSINT, security research, reconnaissance
- **Maturity:** stable (popular, but older)
- **Latency/Cost:** fast (threaded), free
- **Data constraints:** none (public websites)
- **Ops friction:** low (single script)

### Full links
- Repo: https://github.com/s0md3v/Photon
- Original README: https://github.com/s0md3v/Photon/blob/master/README.md
- Stars: 12,621
- Maturity: active

---

## CL4R1T4S

**TL;DR:** Collection of leaked/reverse-engineered system prompts from major AI tools — ChatGPT, Claude, Gemini, Cursor, Devin, Replit Agent, v0 и др. Изучай как строят prompts топовые продукты. 13k stars — must-have для prompt engineering.

### Быстрый выбор
- ✅ Используй если:
  - Studying prompt engineering patterns
  - Building AI coding assistants
  - Researching AI product architecture
  - Learning from production prompts
  - Competitive analysis
- ❌ Не используй если:
  - Need official documentation
  - Ethical concerns about leaks
  - Just want to use tools (not study)
  - Prompts may be outdated

### 🧩 Содержимое
- **ChatGPT:** system prompts, plugins, GPT Builder
- **Claude:** system prompts, Claude Computer Use
- **Cursor:** IDE prompts, codebase understanding
- **Devin:** autonomous coding agent prompts
- **v0:** Vercel's UI generation prompts
- **Replit Agent:** IDE assistant prompts
- **Perplexity:** search response formatting
- **Ключевые файлы:** organized by product

### 🧪 Примеры задач
- "How does Cursor structure codebase context?"
- "What makes Devin's planning prompts?"
- "Claude's safety guidelines analysis"
- "v0 component generation patterns"
- "Build similar AI assistant"
- Prompt engineering research

### ⚠️ Ограничения
- Prompts change frequently (may be outdated)
- Legal grey area (leaked content)
- No official endorsement
- Some prompts incomplete
- Context might be missing
- Use at your own risk

### 🧭 Fit / Maturity / Ops
- **Fit:** prompt engineering, AI research, competitive analysis
- **Maturity:** curated collection (updated by community)
- **Ops friction:** zero (just reading)

### Full links
- Repo: https://github.com/elder-plinius/CL4R1T4S
- Original README: https://github.com/elder-plinius/CL4R1T4S/blob/main/README.md
- See also: system-prompts-and-models-of-ai-tools (111k ⭐)
- Stars: 12,611
- Maturity: active

---

## system-prompts-and-models-of-ai-tools

**TL;DR:** Крупнейшая коллекция system prompts AI инструментов — полные тексты промптов Augment, Claude Code, Cursor, Devin, Kiro, Lovable, Manus, Windsurf и др. **111k stars** — главный источник для prompt engineering research.

### Быстрый выбор
- ✅ Используй если:
  - Deep dive into AI product prompts
  - Building competing AI tools
  - Prompt engineering mastery
  - Understanding tool architectures
  - MUST-HAVE reference для AI developers
- ❌ Не используй если:
  - Ethical concerns about reverse engineering
  - Need official docs (these are extracted)
  - Info may become outdated

### 🧩 Содержимое
- **Cursor:** full IDE system prompts
- **Windsurf:** Codeium's coding assistant
- **Devin:** Cognition's autonomous agent
- **Claude Code:** Claude's official coding tool
- **Augment:** AI pair programmer
- **Lovable:** v0-style UI generation
- **Manus:** computer use agent
- **Kiro:** Amazon's coding agent
- **Ключевые файлы:** organized by tool name

### 🧪 Примеры задач
- "Reverse engineer Cursor's context handling"
- "Study Devin's autonomous planning"
- "Understand Claude Code's tool usage"
- "Compare coding agent architectures"
- "Improve your own AI agent prompts"
- Prompt engineering benchmarking

### ⚠️ Ограничения
- Legal status unclear (extracted content)
- Prompts update frequently
- No commercial use advice
- Context may be missing
- Some files very long

### 🧭 Fit / Maturity / Ops
- **Fit:** AI builders, prompt engineers, researchers
- **Maturity:** active (fastest growing repo 2024-2025)
- **Ops friction:** zero (reading/reference)

### Full links
- Repo: https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools
- Original README: https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools/blob/main/README.md
- Stars: 111,205
- Maturity: active

---

## vercel-labs/agent-browser

**TL;DR:** Experimental browser automation для AI agents от Vercel. CLI для browser control через natural language. Playwright-based. Research project exploring AI-browser interfaces. 11k stars.

### Быстрый выбор
- ✅ Используй если:
  - Experimenting with AI browser agents
  - Vercel ecosystem
  - Research/prototyping
  - CLI-based browser control
  - Learning browser automation + AI
- ❌ Не используй если:
  - Production browser automation (use Stagehand)
  - Need stability (experimental)
  - GUI preferred
  - Enterprise requirements

### 🚀 Запуск
```bash
# Install
npm install -g @vercel/agent-browser

# Run
agent-browser

# Or with npx
npx @vercel/agent-browser
```

### 🧩 Архитектура
- **Language:** TypeScript
- **Browser:** Playwright
- **AI:** OpenAI function calling
- **CLI:** interactive terminal
- **Entrypoints:** CLI commands
- **Ключевые файлы:** [src/](https://github.com/vercel-labs/agent-browser)

### 🧪 Примеры задач
- "Go to GitHub and star a repo"
- "Fill out this form with my data"
- "Navigate to page and take screenshot"
- Prototype browser agent flows
- Learn AI browser interaction

### ⚠️ Ограничения
- Experimental (Vercel Labs)
- Not production-ready
- Limited features vs Stagehand
- May break with updates
- Basic error handling

### 🧭 Fit / Maturity / Ops
- **Fit:** experiments, learning, prototyping
- **Maturity:** experimental (Vercel Labs project)
- **Latency/Cost:** LLM costs per action
- **Data constraints:** OpenAI API key
- **Ops friction:** low (npm install)

### Full links
- Repo: https://github.com/vercel-labs/agent-browser
- Original README: https://github.com/vercel-labs/agent-browser/blob/main/README.md
- See also: stagehand (21k ⭐), browser-use (30k+ ⭐)
- Stars: 10,738
- Maturity: active

---

## Auto-Claude

**TL;DR:** Multi-session autonomous Claude coding agent. Manages multiple Claude instances working в параллели. Task decomposition, session management, context switching. 10k stars.

### Быстрый выбор
- ✅ Используй если:
  - Multiple Claude sessions в parallel
  - Complex project decomposition
  - Autonomous code generation
  - Experimental multi-agent Claude
- ❌ Не используй если:
  - Single task (use Claude directly)
  - Production use (experimental)
  - Need GUI interface
  - Cost-conscious (multiple API calls)

### 🚀 Запуск
```bash
# Clone
git clone https://github.com/AndyMik90/Auto-Claude.git
cd Auto-Claude

# Install
pip install -r requirements.txt

# Configure
export ANTHROPIC_API_KEY=your_key

# Run
python main.py
```

### 🧩 Архитектура
- **Language:** Python
- **AI:** Anthropic Claude API
- **Sessions:** multiple parallel Claude instances
- **Coordination:** task distribution, result aggregation
- **Entrypoints:** `main.py`
- **Ключевые файлы:** [src/](https://github.com/AndyMik90/Auto-Claude)

### 🧪 Примеры задач
- Complex codebase generation
- Parallel feature development
- Multi-file editing
- Research with multiple angles
- Code review workflow

### ⚠️ Ограничения
- Experimental status
- High API costs (multiple sessions)
- Coordination overhead
- Limited documentation
- May produce inconsistent results

### 🧭 Fit / Maturity / Ops
- **Fit:** experimental Claude automation, research
- **Maturity:** experimental
- **Latency/Cost:** high (multiple parallel API calls)
- **Data constraints:** Anthropic API key
- **Ops friction:** medium

### Full links
- Repo: https://github.com/AndyMik90/Auto-Claude
- Stars: 10,445
- Maturity: active

---

## 3FS (DeepSeek)

**TL;DR:** High-performance distributed file system optimized для AI training/inference. Supports disaggregated storage с NVMe. Used internally by DeepSeek для training large models. Open source infrastructure. 10k stars.

### Быстрый выбор
- ✅ Используй если:
  - AI cluster storage
  - High-throughput training data
  - NVMe over Fabrics (NVMeoF)
  - Disaggregated architecture
  - DeepSeek infrastructure patterns
- ❌ Не используй если:
  - Small-scale projects
  - Standard file storage needs
  - No NVMe infrastructure
  - Cloud-managed storage preferred

### 🚀 Запуск
```bash
# Clone
git clone https://github.com/deepseek-ai/3FS.git
cd 3FS

# Build (requires dependencies)
mkdir build && cd build
cmake ..
make -j$(nproc)

# See docs for cluster setup
```

### 🧩 Архитектура
- **Type:** distributed file system
- **Optimized for:** AI workloads, checkpoints, datasets
- **Network:** NVMe over Fabrics
- **Deployment:** bare-metal clusters
- **Language:** C++, Rust
- **Ключевые файлы:** [src/](https://github.com/deepseek-ai/3FS)

### 🧪 Примеры задач
- AI training cluster storage
- Model checkpoint storage
- High-speed dataset access
- Disaggregated storage layer
- Infrastructure для ML training

### ⚠️ Ограничения
- Complex setup (cluster infrastructure)
- Hardware requirements (NVMe, RDMA)
- Not for simple use cases
- Documentation limited
- Enterprise-grade complexity

### 🧭 Fit / Maturity / Ops
- **Fit:** AI infrastructure, large-scale training
- **Maturity:** active (DeepSeek uses internally)
- **Latency/Cost:** high performance, hardware costs
- **Data constraints:** cluster setup required
- **Ops friction:** high (infrastructure engineering)

### Full links
- Repo: https://github.com/deepseek-ai/3FS
- Original README: https://github.com/deepseek-ai/3FS/blob/main/README.md
- Stars: 9,669
- Maturity: active

---

## awesome-claude-code-subagents

**TL;DR:** Curated collection of 100+ specialized Claude Code subagents. Ready-to-use skills для code review, security audit, documentation, testing, refactoring и более. Copy-paste в claude.md или system prompt. 9k stars — must-have для Claude users.

### Быстрый выбор
- ✅ Используй если:
  - Using Claude Code/Claude CLI
  - Need specialized coding skills
  - Want pre-built subagent patterns
  - Learning Claude prompting
  - Быстрый старт с agents
- ❌ Не используй если:
  - Not using Claude products
  - Need production framework (use LangGraph)
  - Custom subagent logic needed

### 🧩 Содержимое
- **Code Review:** security, performance, style
- **Documentation:** API docs, README, inline comments
- **Testing:** unit tests, integration, E2E
- **Refactoring:** patterns, SOLID, cleanup
- **Security:** vulnerability scanning, audit
- **DevOps:** CI/CD, Docker, deployment
- **Ключевые файлы:** organized by category

### 🧪 Примеры задач
- "Add security audit subagent to Claude"
- "Get documentation generator skill"
- "Use test writer subagent"
- Copy prompts to your claude.md
- Mix and match specialized skills

### ⚠️ Ограничения
- Claude-specific (not for other LLMs)
- Prompt quality varies
- May need customization
- No runtime/orchestration
- Just prompts (not code)

### 🧭 Fit / Maturity / Ops
- **Fit:** Claude users, prompt engineering, skill library
- **Maturity:** curated list (community-maintained)
- **Ops friction:** zero (just copy prompts)

### Full links
- Repo: https://github.com/VoltAgent/awesome-claude-code-subagents
- Original README: https://github.com/VoltAgent/awesome-claude-code-subagents/blob/main/README.md
- Stars: 8,822
- Maturity: curated list

---

## AutoAgent (HKUDS)

**TL;DR:** Fully-automated zero-code LLM agent framework. Визуальный builder для agents без программирования. Natural language → working agent. Academic research project из HKU. 8k stars.

### Быстрый выбор
- ✅ Используй если:
  - Zero-code agent creation
  - Visual agent builder
  - Academic/research use
  - Rapid prototyping
  - Non-programmers building agents
- ❌ Не используй если:
  - Production deployment
  - Custom integrations needed
  - Enterprise requirements
  - Need code-level control

### 🚀 Запуск
```bash
# Clone
git clone https://github.com/HKUDS/AutoAgent.git
cd AutoAgent

# Install
pip install -r requirements.txt

# Run
python main.py

# Web UI available
```

### 🧩 Архитектура
- **Language:** Python
- **Builder:** visual/natural language agent construction
- **LLMs:** OpenAI, local models
- **UI:** web interface
- **Research:** HKU DS lab project
- **Entrypoints:** `main.py`
- **Ключевые файлы:** [autoagent/](https://github.com/HKUDS/AutoAgent)

### 🧪 Примеры задач
- "Create an agent that summarizes news"
- "Build a research assistant"
- Visual workflow design
- Academic experiments
- Agent prototyping

### ⚠️ Ограничения
- Research project (not production)
- Limited tool integrations
- Documentation academic style
- Updates may be infrequent
- Community smaller

### 🧭 Fit / Maturity / Ops
- **Fit:** research, prototyping, learning, non-coders
- **Maturity:** research (academic project)
- **Latency/Cost:** depends on LLM
- **Data constraints:** LLM API key
- **Ops friction:** medium (research setup)

### Full links
- Repo: https://github.com/HKUDS/AutoAgent
- Paper: linked in repo
- Stars: 8,486
- Maturity: active

---

## introtodeeplearning (MIT)

**TL;DR:** Official lab materials for MIT 6.S191: Introduction to Deep Learning — the most popular online deep learning course. Covers neural networks, CNNs, RNNs, transformers, GANs, and reinforcement learning with hands-on Jupyter notebooks and TensorFlow. Updated annually with cutting-edge research topics. 8k stars — gold standard для изучения DL.

### Быстрый выбор
- ✅ Используй если:
  - Изучаешь deep learning с нуля
  - Хочешь MIT-quality образование бесплатно
  - Предпочитаешь hands-on labs, а не только теорию
  - Нужны готовые Jupyter notebooks с TensorFlow
  - Готовишься к ML/AI интервью
- ❌ Не используй если:
  - Уже DL expert (слишком базовый)
  - Нужен production code
  - Предпочитаешь PyTorch (курс на TensorFlow)
  - Ищешь advanced research topics
  - Нет времени на полный курс

### 🚀 Запуск
```bash
# Clone repo
git clone https://github.com/MITDeepLearning/introtodeeplearning.git
cd introtodeeplearning

# Install dependencies
pip install mitdeeplearning

# Or run in Google Colab (recommended):
# Visit: http://introtodeeplearning.com
# Click on notebook links → Open in Colab
```

### 🧩 Архитектура
- **Format:** Jupyter Notebooks (.ipynb)
- **Framework:** TensorFlow 2.x / Keras
- **Topics:** intro neural nets, CNNs, RNNs, transformers, GANs, RL
- **Structure:** weekly labs, each 1-2 hours
- **Package:** `mitdeeplearning` helper library
- **Ключевые файлы:** [lab1/](https://github.com/MITDeepLearning/introtodeeplearning/tree/master/lab1) — intro, [lab2/](https://github.com/MITDeepLearning/introtodeeplearning/tree/master/lab2) — CNNs, [lab3/](https://github.com/MITDeepLearning/introtodeeplearning/tree/master/lab3) — RNNs

### 🧪 Примеры задач
- Изучить fundamentals: perceptrons, backpropagation, gradient descent
- Построить CNN for image classification (MNIST, CIFAR)
- Создать RNN/LSTM for sequence prediction
- Понять transformer architecture и attention
- Эксперименты с GANs (image generation)
- Реализовать simple RL agent

### ⚠️ Ограничения
- TensorFlow only (no PyTorch version)
- Beginner/intermediate level
- Labs require GPU for faster execution
- Some labs могут быть outdated yearly
- Not production-ready code patterns
- Colab recommended (local setup более сложный)

### 🧭 Fit / Maturity / Ops
- **Fit:** students, career changers, ML beginners, self-study
- **Maturity:** active (updated annually for MIT course)
- **Latency/Cost:** free (use Google Colab GPU)
- **Data constraints:** none (built-in datasets)
- **Ops friction:** minimal (Colab recommended)

### Full links
- Repo: https://github.com/MITDeepLearning/introtodeeplearning
- Course website: http://introtodeeplearning.com
- YouTube lectures: https://www.youtube.com/playlist?list=PLtBw6njQRU-rwp5__7C0oIVt26ZgjG9NI
- Original README: https://github.com/MITDeepLearning/introtodeeplearning/blob/main/README.md
- Stars: 8,430
- Maturity: educational

---

## free-llm-api-resources

**TL;DR:** Curated list of free LLM inference resources via API — бесплатные способы использовать GPT-4, Claude, Llama, Mistral и другие модели. Включает rate limits, endpoint info, supported models. Essential resource для developers без бюджета на API. Regularly updated. 8k stars — go-to лист для бесплатных LLM.

### Быстрый выбор
- ✅ Используй если:
  - Ищешь бесплатные LLM APIs для тестирования
  - Budget constraints или student projects
  - Prototyping без costs
  - Сравниваешь free tier options разных провайдеров
  - Нужен fallback если paid API недоступен
- ❌ Не используй если:
  - Production reliability critical
  - High volume requests (rate limits!)
  - Data privacy requirements (3rd party services)
  - Need guaranteed uptime/SLA
  - Enterprise compliance needed

### 🚀 Запуск
```bash
# Just read the README — no installation
# The repo is a curated list!

# Example: using a free endpoint
curl https://free-api-endpoint.example/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-4", "messages": [{"role": "user", "content": "Hello!"}]}'

# Or configure in your app:
# OPENAI_BASE_URL=https://free-proxy.example
# OPENAI_API_KEY=free_key
```

### 🧩 Содержимое списка
- **Free API proxies:** community-hosted endpoints
- **Free tiers:** official provider free tiers (OpenRouter, Groq, etc.)
- **Rate limits:** requests per day/minute info
- **Supported models:** GPT-4, Claude, Llama, Mistral, Gemini
- **Endpoint formats:** OpenAI-compatible, custom APIs
- **Ключевые секции:** [README.md](https://github.com/cheahjs/free-llm-api-resources/blob/main/README.md) — main list

### 🧪 Примеры задач
- Find free GPT-4 alternative for testing
- Get Llama-3 access without local hardware
- Compare rate limits across providers
- Setup fallback LLM endpoints
- Student project без API costs
- Hackathon rapid prototyping

### ⚠️ Ограничения
- Free = rate limits (usually 10-100 req/day)
- Reliability не guaranteed (могут отключить)
- Some services may log/use your data
- No SLA, no support
- Models могут быть outdated versions
- Some endpoints temporary/unstable

### 🧭 Fit / Maturity / Ops
- **Fit:** students, hobbyists, prototyping, testing
- **Maturity:** curated list (community-maintained)
- **Latency/Cost:** free (but rate limited)
- **Data constraints:** vary by provider (read ToS!)
- **Ops friction:** minimal (just read and use)

### Full links
- Repo: https://github.com/cheahjs/free-llm-api-resources
- Original README: https://github.com/cheahjs/free-llm-api-resources/blob/main/README.md
- See also: OpenRouter free tier, Groq free tier
- Stars: 8,014
- Maturity: curated list

---

## big-AGI

**TL;DR:** Personal AI suite — multi-model chat, image generation, voice, code execution. Supports 30+ LLM providers. Beautiful UI. Self-hosted. Best open ChatGPT alternative с full features. 7k stars.

### Быстрый выбор
- ✅ Используй если:
  - Multi-model chat interface
  - Image generation integration
  - Voice interactions
  - Self-hosted ChatGPT alternative
  - Multiple API providers
- ❌ Не используй если:
  - API-only needed (no UI)
  - Single model focus
  - Minimal resources wanted
  - Enterprise features

### 🚀 Запуск
```bash
# Clone
git clone https://github.com/enricoros/big-AGI.git
cd big-AGI

# Install & Run
npm install && npm run dev

# http://localhost:3000

# Or Docker
docker compose up -d
```

### 🧩 Архитектура
- **Frontend:** Next.js, React, Material UI
- **LLMs:** OpenAI, Anthropic, Google, Ollama, 30+ providers
- **Features:** chat, image gen, voice, code, plugins
- **Deploy:** Vercel, Docker, self-hosted
- **Entrypoints:** `pages/` — Next.js pages
- **Ключевые файлы:** [src/](https://github.com/enricoros/big-AGI)

### 🧪 Примеры задач
- Multi-model comparison chats
- Image generation with DALL-E/SD
- Voice conversations
- Code execution/review
- Document Q&A
- Personal AI assistant

### ⚠️ Ограничения
- Resource-intensive (full-stack)
- Many features = complexity
- Some integrations experimental
- Requires multiple API keys
- Updates can break configs

### 🧭 Fit / Maturity / Ops
- **Fit:** personal AI suite, ChatGPT alternative
- **Maturity:** active (regular updates)
- **Latency/Cost:** your API costs
- **Data constraints:** multiple LLM keys
- **Ops friction:** medium (npm/Docker)

### Full links
- Repo: https://github.com/enricoros/big-AGI
- Original README: https://github.com/enricoros/big-AGI/blob/main/README.md
- Demo: https://big-agi.com
- Stars: 6,830
- Maturity: active

---

## opencode-antigravity-auth

**TL;DR:** Authentication bridge for Opencode to connect with Antigravity (Google's internal-style IDE system) via OAuth. Allows seamless login and token management. Critical for internal tool integration. 6k stars.

### Быстрый выбор
- ✅ Используй если:
  - Connecting Opencode to Antigravity
  - Developing plugins for internal Google-like tools
  - Needing OAuth flow optimization
  - Internal tooling development
- ❌ Не используй если:
  - Public VS Code extension development
  - Standard OAuth providers (use Passport/NextAuth)
  - Non-Antigravity environments
  - Simple API key auth sufficient

### 🚀 Запуск
```bash
git clone https://github.com/NoeFabris/opencode-antigravity-auth
cd opencode-antigravity-auth
npm install
npm run build
# Import as middleware or standalone service
```

### 🧩 Архитектура
- **Stack:** Node.js / TypeScript
- **Protocol:** OAuth 2.0 / OIDC extension
- **Integration:** Middleware for Opencode server
- **Security:** Token rotation, secure storage
- **Entrypoints:** `src/auth.ts`

### 🧪 Примеры задач
- Authenticate user session in Opencode
- Rotate access tokens silently
- Manage permissions for Antigravity resources
- Secure plugin communication
- SSO integration

### ⚠️ Ограничения
- Specific to Opencode/Antigravity ecosystem
- Documentation assumes internal knowledge
- Niche use case
- Configuration complexity
- Dependency on external auth services

### 🧭 Fit / Maturity / Ops
- **Fit:** Internal tooling, specific IDE extensions
- **Maturity:** active (niche)
- **Latency/Cost:** low overhead
- **Data constraints:** auth tokens only
- **Ops friction:** medium (config)

### Full links
- Repo: https://github.com/NoeFabris/opencode-antigravity-auth
- Original README: https://github.com/NoeFabris/opencode-antigravity-auth/blob/main/README.md
- Stars: 6,395
- Maturity: active

---

## ANUS

**TL;DR:** AI Native User Space. Experimental operating environment for AI agents. Provides standard interfaces for file systems, process management, and communication. Aims to be the "kernel" for AI-native applications. 6k stars.

### Быстрый выбор
- ✅ Используй если:
  - Exploring AI-native OS concepts
  - Building low-level agent runtime
  - Researching agent-system interfaces
  - Experimental user space design
- ❌ Не используй если:
  - Production application (use LangChain/CrewAI)
  - Need higher-level abstraction
  - Stable API required
  - Just want to run a chatbot

### 🚀 Запуск
```bash
git clone https://github.com/anus-dev/ANUS
cd ANUS
# See repo for build instructions (Rust/C++)
make build
./anus-runtime
```

### 🧩 Архитектура
- **Core:** Runtime for AI processes
- **Interface:** VirtIO-like interfaces for agents
- **Languages:** Rust (typical for this domain)
- **Concepts:** AI-native file system, memory management
- **Entrypoints:** `src/main.rs`

### 🧪 Примеры задач
- Manage multiple agent processes
- Provide virtual file system to agents
- Inter-agent IPC implementation
- Resource isolation for safe execution
- AI-native shell experimentation

### ⚠️ Ограничения
- Experimental/Niche
- Low-level focus
- Documentation sparse
- Not a standard agent framework
- Steep learning curve

### 🧭 Fit / Maturity / Ops
- **Fit:** Systems programming, AI OS research
- **Maturity:** experimental
- **Latency/Cost:** native performance
- **Data constraints:** local execution
- **Ops friction:** high (system level)

### Full links
- Repo: https://github.com/anus-dev/ANUS
- Original README: https://github.com/anus-dev/ANUS/blob/main/README.md
- Stars: 6,282
- Maturity: experimental

---

## AI-Crash-Course

**TL;DR:** Catch up to public frontier of AI research in 2 weeks. Curated curriculum covering LLMs, Deep Learning, Agents, and Production Engineering. Structured learning path for fast upskilling. 6k stars.

### Быстрый выбор
- ✅ Используй если:
  - Rapidly upskilling in AI/LLMs
  - Need structured roadmap
  - Want curated high-quality resources
  - Preparing for AI interviews
  - 2-week intensive learning goal
- ❌ Не используй если:
  - Deep academic theory focus
  - Already a senior AI engineer
  - Specific focused topic only
  - Prefer video-only content

### 🚀 Запуск
```bash
# Start reading
# Visit the repo and follow Day 1 - Day 14 plan
```

### 🧩 Архитектура
- **Values:** Quality over quantity, Practical focus
- **Structure:** Daily modules (e.g., Transformers, RAG, Agents)
- **Format:** Readings, Papers, Code Labs
- **Topics:** Prompt Engineering, Fine-tuning, Deployment
- **Entrypoints:** `README.md` curriculum

### 🧪 Примеры задач
- "Understanding Attention Mechanism"
- "Building your first RAG app"
- "Fine-tuning a Llama model"
- "Designing Agent workflows"
- "Optimizing inference latency"

### ⚠️ Ограничения
- High intensity
- Requires self-discipline
- Links may rot over time
- English-only resources
- Not a certification

### 🧭 Fit / Maturity / Ops
- **Fit:** Self-learners, bootcamp style upskilling
- **Maturity:** educational (curated)
- **Latency/Cost:** free (time investment)
- **Data constraints:** none
- **Ops friction:** zero (reading)

### Full links
- Repo: https://github.com/henrythe9th/AI-Crash-Course
- Original README: https://github.com/henrythe9th/AI-Crash-Course/blob/main/README.md
- Stars: 5,671
- Maturity: educational

---

## firecrawl-mcp-server

**TL;DR:** Official Firecrawl MCP Server. Enables Cursor, Claude Desktop, and other MCP clients to scrape websites, crawl subpages, and search the web using Firecrawl's API. Powerful data extraction tool for agents. 5k stars.

### Быстрый выбор
- ✅ Используй если:
  - Web scraping inside Claude/Cursor
  - Crawling documentation sites
  - Converting websites to markdown
  - Searching current web data
  - Firecrawl API subscriber
- ❌ Не используй если:
  - No Firecrawl API key
  - Simple single-page fetch (use fetch-mcp)
  - Non-MCP environment
  - Local scraping favored (browsers)

### 🚀 Запуск
```bash
# Via npx (e.g. in Claude Desktop config)
npx -y @firecrawl/mcp-server

# Env var required: FIRECRAWL_API_KEY
```

### 🧩 Архитектура
- **Protocol:** MCP (Model Context Protocol)
- **Backend:** Firecrawl API
- **Tools:** `scrape`, `crawl`, `search`
- **Output:** Markdown optimized for LLMs
- **Entrypoints:** `index.ts`

### 🧪 Примеры задач
- "Scrape this documentation page and explain the API"
- "Search for latest news on X"
- "Crawl this entire blog and summarize posts"
- "Extract pricing table from this URL"
- "Check competitor website changes"

### ⚠️ Ограничения
- Requires Firecrawl API Key (paid/free tier)
- Rate limits of Firecrawl API
- Network dependent
- Privacy (data sent to Firecrawl)
- Text-only focus (images supported via markdown links)

### 🧭 Fit / Maturity / Ops
- **Fit:** standard utility for AI coding assistants
- **Maturity:** active (official)
- **Latency/Cost:** Firecrawl credits + API latency
- **Data constraints:** API key
- **Ops friction:** low (npx)

### Full links
- Repo: https://github.com/firecrawl/firecrawl-mcp-server
- Original README: https://github.com/firecrawl/firecrawl-mcp-server/blob/main/README.md
- Firecrawl: https://firecrawl.dev
- Stars: 5,341
- Maturity: active

---

## rllm

**TL;DR:** RLLM (RL for LLMs). High-performance library for training LLMs with Reinforcement Learning (PPO, GRPO). Optimized for massive scale using vLLM backend. Democratizing DeepSeek-R1 style training pipelines. 5k stars.

### Быстрый выбор
- ✅ Используй если:
  - Training reasoning models (like R1)
  - RLHF / RLAIF pipelines
  - Scaling up RL training
  - PPO/GRPO implementation needed
  - Compute efficient training
- ❌ Не используй если:
  - Standard SFT (Supervised Fine-Tuning) enough
  - Inference only
  - Low VRAM/Compute
  - Beginner to LLM training

### 🚀 Запуск
```bash
# Install
pip install rllm

# Example: GRPO training
# See examples/grpo_training.py in repo
```

### 🧩 Архитектура
- **Core:** VeRL (Volcano RL) based
- **Inference:** vLLM integration
- **Algorithms:** PPO, GRPO (Group Relative Policy Optimization)
- **Infrastructure:** Torch, Ray (distributed)
- **Entrypoints:** `rllm/` package

### 🧪 Примеры задач
- Train a math reasoning model with GRPO
- Align LLM with human preferences (RLHF)
- Optimize specific reward functions (e.g. code correctness)
- Reproduce DeepSeek-R1 training
- Research new RL algorithms for LLMs

### ⚠️ Ограничения
- High compute requirements (GPUs)
- Complex hyperparameter tuning
- Advanced ML knowledge required
- Evolving API
- Training instability risks

### 🧭 Fit / Maturity / Ops
- **Fit:** LLM researchers, model builders
- **Maturity:** active (rapidly evolving field)
- **Latency/Cost:** high training cost
- **Data constraints:** training datasets
- **Ops friction:** high (cluster management)

### Full links
- Repo: https://github.com/rllm-org/rllm
- Original README: https://github.com/rllm-org/rllm/blob/main/README.md
- Stars: 5,033
- Maturity: active

---

## smallpond (DeepSeek)

**TL;DR:** Lightweight data processing framework by DeepSeek. Built on top of DuckDB and 3FS (DeepSeek's filesystem). Enables fast, scalable ETF (Extract-Transform-Filter) pipelines for huge AI datasets. 5k stars.

### Быстрый выбор
- ✅ Используй если:
  - Processing large datasets for AI training
  - Using DeepSeek's 3FS ecosystem
  - Need faster-than-Spark for specific workloads
  - DuckDB-based data processing
  - Parquet/Arrow heavy workflows
- ❌ Не используй если:
  - Simple small CSV processing (use Pandas)
  - Not using 3FS storage
  - Requiring complex distributed joins (Spark better)
  - Java/Scala ecosystem preferred

### 🚀 Запуск
```bash
pip install smallpond
# See docs for 3FS configuration
```
```python
import smallpond as sp

# Reads from 3FS/S3, processes with DuckDB SQL, writes back
sp.read_parquet("s3://data/input.parquet") \
  .filter("value > 0.5") \
  .write_parquet("s3://data/output.parquet")
```

### 🧩 Архитектура
- **Engine:** DuckDB (local compute)
- **Storage:** 3FS (DeepSeek), S3, HDFS
- **Parallelism:** Multiprocessing / Cluster capabilities
- **Format:** Parquet, Arrow
- **Entrypoints:** `smallpond` python package

### 🧪 Примеры задач
- Preprocess 1TB training corpus
- Filter CommonCrawl dumps
- Convert JSONL to Parquet efficiently
- Deduplicate large datasets
- Feature engineering for ML models

### ⚠️ Ограничения
- Niche ecosystem (best with 3FS)
- Documentation limited (DeepSeek internal tools)
- Less mature than Polars/Spark
- Resource management manual
- Python-centric

### 🧭 Fit / Maturity / Ops
- **Fit:** AI Data Engineering, DeepSeek infrastructure users
- **Maturity:** production (used by DeepSeek)
- **Latency/Cost:** highly efficient
- **Data constraints:** 3FS/S3 storage
- **Ops friction:** medium (infrastructure setup)

### Full links
- Repo: https://github.com/deepseek-ai/smallpond
- Original README: https://github.com/deepseek-ai/smallpond/blob/main/README.md
- Stars: 4,909
- Maturity: active

---

## react-grab

**TL;DR:** "Cursor mode" for your web app. Visual context selector that allows users/agents to point-and-click elements to perform actions (like "fix this color" or "explain this component"). Empower your users with AI editing capabilities. 5k stars.

### Быстрый выбор
- ✅ Используй если:
  - Building AI-powered web builders
  - Adding "Ask AI about this element" feature
  - Visual element selection needed
  - Inspecting component tree at runtime
  - React-based application
- ❌ Не используй если:
  - Non-React frameworks
  - Security-sensitive DOM (banking apps)
  - Need full DevTools functionality
  - Mobile apps

### 🚀 Запуск
```bash
npm install react-grab
```
```jsx
import { Grab } from 'react-grab';

function App() {
  return (
    <Grab onSelect={(element) => console.log('Selected:', element)}>
      <YourAppContent />
    </Grab>
  );
}
```

### 🧩 Архитектура
- **Core:** React Context + DOM overlays
- **Interaction:** Hover/Click event interception
- **Metadata:** React Fiber tree traversal
- **UI:** SVG overlays for highlighting
- **Entrypoints:** `<Grab />` provider

### 🧪 Примеры задач
- AI Website Builder (click to edit text)
- Bug reporting tool (click component to report)
- Context gathering for Chatbot (click to ask)
- Design system auditing
- User onboarding walkthroughs

### ⚠️ Ограничения
- React Fiber internals reliance (fragile)
- May conflict with other overlay tools
- Complex styling stacking contexts
- Performance on huge DOM trees
- Experimental API

### 🧭 Fit / Maturity / Ops
- **Fit:** AI coding tools, website builders, advanced UX
- **Maturity:** active (innovative)
- **Latency/Cost:** client-side library
- **Data constraints:** none
- **Ops friction:** low (npm install)

### Full links
- Repo: https://github.com/aidenybai/react-grab
- Original README: https://github.com/aidenybai/react-grab/blob/main/README.md
- Stars: 4,595
- Maturity: active

---

## GenAI-Showcase (MongoDB)

**TL;DR:** Official GenAI Cookbook by MongoDB. Collection of practical applications, RAG patterns, and agent implementations using MongoDB Atlas Vector Search. High-quality reference code for enterprise GenAI apps. 4k stars.

### Быстрый выбор
- ✅ Используй если:
  - MongoDB Atlas user
  - Building RAG applications
  - Need enterprise-ready examples
  - Learning Vector Search implementation
  - Python/Node.js stack
- ❌ Не используй если:
  - Using Postgres (pgvector) or specialized Qdrant/Weaviate
  - No MongoDB infrastructure
  - Looking for a framework (this is a cookbook)
  - Purely local development (needs Atlas)

### 🚀 Запуск
```bash
git clone https://github.com/mongodb-developer/GenAI-Showcase
cd GenAI-Showcase
# Navigate to specific project, e.g., 'rag-quickstart'
pip install -r requirements.txt
# Set MONGO_URI and OpenAI API Key
```

### 🧩 Архитектура
- **Database:** MongoDB Atlas (Vector Store)
- **Frameworks:** LangChain, LlamaIndex
- **Models:** OpenAI, Claude, HuggingFace
- **Format:** Notebooks and reference apps
- **Entrypoints:** Individual project folders

### 🧪 Примеры задач
- "RAG with Metadata Filtering"
- "GraphRAG knowledge graph construction"
- "Semantic Cache implementation"
- "Multi-modal retrieval (images + text)"
- "Agent memory using MongoDB"

### ⚠️ Ограничения
- Locked to MongoDB ecosystem
- Requires Atlas account (tier dependent)
- Not a cohesive library
- Maintenance varies by specific example
- Setup requires DB provisioning

### 🧭 Fit / Maturity / Ops
- **Fit:** Enterprise GenAI, MongoDB users
- **Maturity:** educational/reference
- **Latency/Cost:** Atlas Vector Search costs
- **Data constraints:** MongoDB storage
- **Ops friction:** medium (DB setup)

### Full links
- Repo: https://github.com/mongodb-developer/GenAI-Showcase
- Original README: https://github.com/mongodb-developer/GenAI-Showcase/blob/main/README.md
- Stars: 4,210
- Maturity: active

---

## mcp-ui

**TL;DR:** UI framework for the Model Context Protocol (MCP). Provides React components and utilities to build next-generation interfaces that communicate with MCP servers. Enables "UI over MCP" — dynamic UIs driven by standard protocol messages. 4k stars.

### Быстрый выбор
- ✅ Используй если:
  - Building clients for MCP servers
  - Creating visual interfaces for LLM tools
  - Implementing "Generative UI" patterns
  - React/Next.js stack preferred
  - Need standard components for MCP primitives
- ❌ Не используй если:
  - Not using Model Context Protocol
  - Simple CLI tool is enough
  - Using other UI frameworks (Vue/Svelte)
  - Pure text interface sufficient

### 🚀 Запуск
```bash
npm install @mcp-ui/react
```
```tsx
import { MCPClient, ToolDisplay } from '@mcp-ui/react';

function AgentUI() {
  return (
    <MCPClient serverUrl="ws://localhost:3000">
       <ToolDisplay tool="weather_forecast" />
    </MCPClient>
  );
}
```

### 🧩 Архитектура
- **Core:** React logic for MCP clients
- **Components:** Tool cards, Resource viewers, Prompts
- **Communication:** WebSocket / SSE client adapters
- **Styles:** Tailwind CSS compatible
- **Entrypoints:** `@mcp-ui/react` package

### 🧪 Примеры задач
- Build a custom dashboard for an MCP agent
- create a visual file explorer for file-system MCP server
- Display interactive charts from data-analysis MCP tools
- Implement human-in-the-loop approval UI
- Debugger interface for MCP protocol

### ⚠️ Ограничения
- Early stage project
- Rapidly evolving specs
- React-only currently
- Documentation is sparse
- Requires running MCP servers

### 🧭 Fit / Maturity / Ops
- **Fit:** Frontend devs building AI tool interfaces
- **Maturity:** active (early stage)
- **Latency/Cost:** client-side rendering
- **Data constraints:** connects to local/remote MCP servers
- **Ops friction:** low (npm package)

### Full links
- Repo: https://github.com/MCP-UI-Org/mcp-ui
- Original README: https://github.com/MCP-UI-Org/mcp-ui/blob/main/README.md
- Stars: 4,103
- Maturity: active

---

## Search-R1

**TL;DR:** Efficient RL Training Framework combining Reasoning models (like R1) with Search Engine calls. Trains agents to "think, then search, then think". Scalable implementation of retrieval-augmented reasoning. 4k stars.

### Быстрый выбор
- ✅ Используй если:
  - Researching search-augmented reasoning
  - Training models to use search tools effectively
  - Replicating DeepSeek-R1-Search behavior
  - Need efficient RL training pipeline
- ❌ Не используй если:
  - Simple RAG (use LangChain)
  - Production search API needed (use Tavily/Bing)
  - No training resources (GPUs)
  - Just want to run inference

### 🚀 Запуск
```bash
git clone https://github.com/PeterGriffinJin/Search-R1
cd Search-R1
pip install -r requirements.txt
# Configure Search API (Bing/Google)
python train.py --config configs/search_reasoning.yaml
```

### 🧩 Архитектура
- **Core:** RL loop (PPO-variant)
- **Reasoning:** Chain-of-Thought with search actions
- **Environment:** Search Engine wrappers
- **Model:** Compatible with Llama/Qwen derived models
- **Entrypoints:** `train.py`, `search_env.py`

### 🧪 Примеры задач
- Train an agent to verify facts via Google Search
- Improve multi-hop question answering
- Reduce hallucinations by enforcing search verification
- Benchmark reasoning-with-tools capabilities
- Research optimal search strategies for LLMs

### ⚠️ Ограничения
- Academic/Research code quality
- Requires external Search API keys
- Compute intensive training
- Documentation assumes RL knowledge
- Not a production deployment framework

### 🧭 Fit / Maturity / Ops
- **Fit:** AI Researchers, Reasoning model developers
- **Maturity:** active (research)
- **Latency/Cost:** training cost + search API costs
- **Data constraints:** training data
- **Ops friction:** high (training setup)

### Full links
- Repo: https://github.com/PeterGriffinJin/Search-R1
- Original README: https://github.com/PeterGriffinJin/Search-R1/blob/main/README.md
- Stars: 3,868
- Maturity: active

---

## TorBot

**TL;DR:** Dark Web OSINT tool. Automates crawling and scraping of .onion sites on the Tor network. Extracts page titles, addresses, emails, and links. Helps map hidden services. 4k stars.

### Быстрый выбор
- ✅ Используй если:
  - Performing dark web investigations
  - Threat intelligence gathering
  - Mapping .onion link structures
  - Extracting contact info from hidden services
  - Security research
- ❌ Не используй если:
  - Crawling surface web only (use Photon)
  - Illegal activities (obviously)
  - High-speed crawling required (Tor is slow)
  - Determining owner identity (hard)

### 🚀 Запуск
```bash
# Requires Tor service running
apt-get install tor
service tor start

git clone https://github.com/DedSecInside/TorBot
cd TorBot
pip install -r requirements.txt
python3 torbot.py -u http://someonionurl.onion
```

### 🧩 Архитектура
- **Language:** Python
- **Network:** Tor (SOCKS5 proxy)
- **Parser:** BeautifulSoup
- **Output:** JSON / Terminal
- **Entrypoints:** `torbot.py`

### 🧪 Примеры задач
- "Map links from this market forum"
- "Find email addresses on this leaks site"
- "Check if these .onion links are live"
- "Save page titles for indexing"
- "Cyber threat intelligence analysis"

### ⚠️ Ограничения
- Tor network (very slow)
- Frequent connection timeouts
- CAPTCHAs on dark web sites
- Many sites are short-lived
- Maintenance is sporadic
- Legal/Ethical risks

### 🧭 Fit / Maturity / Ops
- **Fit:** Cyber security, OSINT analysts
- **Maturity:** active (classic tool)
- **Latency/Cost:** slow (network limited), free
- **Data constraints:** public dark web
- **Ops friction:** medium (Tor setup)

### Full links
- Repo: https://github.com/DedSecInside/TorBot
- Original README: https://github.com/DedSecInside/TorBot/blob/main/README.md
- Stars: 3,742
- Maturity: active

---

## awesome-ai-devtools

**TL;DR:** Curated list of AI-powered developer tools — comprehensive directory covering AI code assistants, API platforms, testing tools, documentation generators, and productivity boosters. Regularly updated with new tools and categories. Essential resource for developers exploring the AI-assisted coding landscape. 4k stars — go-to reference для AI dev tools.

### Быстрый выбор
- ✅ Используй если:
  - Ищешь новые AI developer tools
  - Сравниваешь tools в одной категории
  - Нужен полный обзор AI coding ecosystem
  - Research для выбора tech stack
  - Хочешь быть в курсе новых AI dev tools
- ❌ Не используй если:
  - Уже выбрал конкретный tool
  - Нужны non-dev AI tools (use other lists)
  - Ищешь глубокий review (это список, не reviews)
  - Нужна интеграция (это reference list)
  - Хочешь только OSS tools (list includes paid)

### 🧩 Содержимое списка
- **Code Assistants:** Cursor, GitHub Copilot, Codeium, Tabnine, etc.
- **API Platforms:** OpenAI, Anthropic, Google AI, Together AI
- **Testing Tools:** AI-powered test generation, coverage tools
- **Documentation:** AI doc generators, README writers
- **Code Review:** AI PR reviewers, linting with AI
- **Debugging:** AI debuggers, error explainers
- **DevOps:** AI infrastructure tools, monitoring
- **Ключевые секции:** categorized by tool type

### 🧪 Примеры задач
- "Find alternatives to GitHub Copilot"
- "Compare AI testing frameworks"
- "Discover new AI documentation tools"
- Research AI code review solutions
- Explore AI DevOps automation
- Find AI-powered API development tools

### ⚠️ Ограничения
- List format (no deep reviews/comparisons)
- Links may become outdated
- Quality varies across listed tools
- Includes both free and paid tools
- No performance benchmarks
- Community-curated (volunteer effort)

### 🧭 Fit / Maturity / Ops
- **Fit:** developers exploring AI tools, tech leads
- **Maturity:** curated list (community-maintained)
- **Latency/Cost:** free to browse
- **Data constraints:** none (just read)
- **Ops friction:** zero (reference resource)

### Full links
- Repo: https://github.com/jamesmurdza/awesome-ai-devtools
- Original README: https://github.com/jamesmurdza/awesome-ai-devtools/blob/main/README.md
- Stars: 3,682
- Maturity: curated list
- Stars: 3,519
- Maturity: curated list

---

## AGiXT

**TL;DR:** Dynamic AI Agent Automation Platform. Highly extensible framework designed for building autonomous agents that can learn and adapt across different providers. Features adaptive memory, smart instruction management, and a plugin-based architecture. 3k stars.

### Быстрый выбор
- ✅ Используй если:
  - Building adaptive autonomous agents
  - Need support for many LLM providers (OpenAI, Anthropic, LocalAI, etc.)
  - Long-term memory integration (ChromaDB, Pinecone, etc.)
  - No-code agent training via UI
  - Smart features like chaining commands and macros
- ❌ Не используй если:
  - Simple, single-task chatbot
  - Minimalist environment preferred (heavy dependencies)
  - Not comfortable with Docker setup
  - Production enterprise stability required (still rapid dev)

### 🚀 Запуск
```bash
git clone https://github.com/Josh-XT/AGiXT
cd AGiXT
# Docker recommended
docker compose up
# Access UI at http://localhost:3437
```

### 🧩 Архитектура
- **Core:** Python-based agent management
- **Extensions:** Plugin system for tools and providers
- **Memory:** Vector database integration (multiple backends)
- **UI:** Next.js frontend for management
- **Entrypoints:** `agixt/` module

### 🧪 Примеры задач
- Train an agent to manage your calendar via plugins
- Create a multi-LLM research assistant
- Automate social media interactions
- Build a coding assistant with local model backend
- Chain complex workflows (Research -> Summarize -> Email)

### ⚠️ Ограничения
- Complexity of configuration
- Heavy resource usage (Docker containers)
- Rapid updates can break existing setups
- Documentation can lag behind features
- Integration reliability varies by provider

### 🧭 Fit / Maturity / Ops
- **Fit:** Enthusiasts, power users, multi-provider agent builders
- **Maturity:** active (frequent updates)
- **Latency/Cost:** depends on providers used
- **Data constraints:** local or cloud APIs
- **Ops friction:** medium (Docker management)

### Full links
- Repo: https://github.com/Josh-XT/AGiXT
- Original README: https://github.com/Josh-XT/AGiXT/blob/main/README.md
- Stars: 3,145
- Maturity: active

---

## cloudflare/agents

**TL;DR:** Official framework for building and deploying AI Agents on Cloudflare Workers. Leverage Cloudflare's global edge network, serverless inference (Workers AI), and durable state (Durable Objects) for scalable, low-latency agents. 3k stars.

### Быстрый выбор
- ✅ Используй если:
  - Deploying agents to the edge (low latency)
  - Using Cloudflare ecosystem (Workers, KV, D1)
  - Need serverless architecture
  - Cost-effective scaling (pay per request)
  - Integration with Workers AI (Llama, etc.)
- ❌ Не используй если:
  - Deep dependency on Python libraries (this is JS/TS)
  - Long-running GPU tasks (>30s)
  - Self-hosting on own hardware
  - AWS/GCP lock-in preferred

### 🚀 Запуск
```bash
npm create cloudflare@latest my-agent -- --template cloudflare/agents
cd my-agent
npm install
npm run dev
# Deploy
npx wrangler deploy
```

### 🧩 Архитектура
- **Runtime:** Cloudflare Workers (V8 Isolate)
- **State:** Durable Objects (for agent memory)
- **AI:** Workers AI (Rest API to models)
- **Language:** TypeScript / JavaScript
- **Entrypoints:** `src/index.ts`

### 🧪 Примеры задач
- Edge-hosted chatbots with persistence
- API rate-limit handling agents
- Real-time multiplayer game agents
- Content processing at the edge
- Personalized user assistants per-session

### ⚠️ Ограничения
- JavaScript/TypeScript only environment
- Worker execution time limits
- Model availability limited to Workers AI catalog (or external APIs)
- State size limits in Durable Objects
- Ecosystem isolation

### 🧭 Fit / Maturity / Ops
- **Fit:** Web developers, Cloudflare users, scalable agent APIs
- **Maturity:** active (official Cloudflare)
- **Latency/Cost:** extremely low latency, competitive pricing
- **Data constraints:** global distribution
- **Ops friction:** low (wrangler CLI)

### Full links
- Repo: https://github.com/cloudflare/agents
- Original README: https://github.com/cloudflare/agents/blob/main/README.md
- Stars: 3,048
- Maturity: active

---

## goku (Saiyan-World)

**TL;DR:** CVPR 2025 Highlight. "Goku" - A Foundation Model for Video Generation. Capable of generating high-quality, physically plausible videos from text prompts. Focuses on motion consistency and visual fidelity. 3k stars.

### Быстрый выбор
- ✅ Используй если:
  - Researching state-of-the-art video generation
  - Experimenting with open weights video models
  - Need physics-aware video synthesis
  - CVPR paper implementation interest
  - Building video generation pipelines
- ❌ Не используй если:
  - Production commercial video service (Sora/Runway better)
  - Low VRAM (requires significant GPU)
  - Real-time generation needed
  - Text-only tasks

### 🚀 Запуск
```bash
git clone https://github.com/Saiyan-World/goku
cd goku
pip install -r requirements.txt
# Download weights (see README)
python inference.py --prompt "A cyberpunk city in the rain"
```

### 🧩 Архитектура
- **Model:** DiT (Diffusion Transformer) based
- **Input:** Text / Image
- **Output:** Video frames
- **Optimization:** Motion-aware latent space
- **Entrypoints:** `inference.py`

### 🧪 Примеры задач
- Generate stock footage from description
- Animate static images
- Create short clips for social media
- Benchmark against Sora/Gen-3
- Academic research on video consistency

### ⚠️ Ограничения
- Research code quality
- Heavy compute requirements
- Generation time is slow
- Artifacts in complex motion
- License restrictions (check specific weights license)

### 🧭 Fit / Maturity / Ops
- **Fit:** AI Researchers, Video generation enthusiasts
- **Maturity:** research (active)
- **Latency/Cost:** high compute cost
- **Data constraints:** local weights
- **Ops friction:** medium (GPU setup)

### Full links
- Repo: https://github.com/Saiyan-World/goku
- Original README: https://github.com/Saiyan-World/goku/blob/main/README.md
- Stars: ~3,000 (CVPR Highlight)
- Maturity: research

---

## cc-wf-studio

**TL;DR:** Creative Compute Workflow Studio. A graph-based visual editor for building AI workflows. Similar to ComfyUI but focused on general compute and agent orchestration. Enables visual programming for complex AI pipelines. 3k stars.

### Быстрый выбор
- ✅ Используй если:
  - Visual programming preference
  - Orchestrating complex AI flows
  - ComfyUI-like interface desired for logic
  - Node-based workflow editing
  - Rapid prototyping of pipelines
- ❌ Не используй если:
  - Code-first preference (LangChain/LlamaIndex)
  - Production processing speed critical (overhead)
  - Simple linear scripts
  - Headless execution required primarily

### 🚀 Запуск
```bash
git clone https://github.com/breaking-brake/cc-wf-studio
cd cc-wf-studio
pip install -r requirements.txt
python main.py
# Opens local web interface
```

### 🧩 Архитектура
- **Core:** Node-graph execution engine
- **UI:** React/Vue based visual editor
- **Nodes:** Custom python functions as nodes
- **State:** Flow-based state management
- **Entrypoints:** `main.py`

### 🧪 Примеры задач
- Build a multi-step image generation pipeline
- Create a chatbot with conditional logic nodes
- Visual ETL pipeline construction
- Prototype RAG flow visually
- Chain multiple API calls with visual debug

### ⚠️ Ограничения
- Experimental status
- Smaller community than ComfyUI
- Documentation is evolving
- Python dependency management for nodes
- Interface complexity for simple tasks

### 🧭 Fit / Maturity / Ops
- **Fit:** Visual thinkers, AI prototypers
- **Maturity:** active (experimental)
- **Latency/Cost:** local execution
- **Data constraints:** none
- **Ops friction:** medium (setup)

### Full links
- Repo: https://github.com/breaking-brake/cc-wf-studio
- Original README: https://github.com/breaking-brake/cc-wf-studio/blob/main/README.md
- Stars: ~3,193
- Maturity: active


---

## Leaked-GPTs

**TL;DR:** Repository of System Prompts leaked from popular Custom GPTs. Reverse-engineered instructions from top GPT Store agents. Useful for learning advanced prompt engineering techniques and understanding how "apps" are built on top of LLMs. 2k stars.

### Быстрый выбор
- ✅ Используй если:
  - Studying system prompt design
  - Recreating functionality of popular GPTs
  - Learning security/jailbreaking techniques
  - Researching prompt protection mechanisms
  - Need inspiration for your own agent persona
- ❌ Не используй если:
  - Commercial use (copyright grey area)
  - Expecting fully working code (prompts only)
  - Relying on outdated prompts
  - Looking for an API

### 🚀 Запуск
```bash
# Browse file structure
# Look for relevant folder e.g. "writing_coach/prompt.md"
```

### 🧩 Архитектура
- **Format:** Markdown / Text files
- **Content:** System instructions, Knowledge base descriptions
- **Origin:** Jailbroken outputs from GPTs
- **Organization:** By category/popularity
- **Entrypoints:** Root directory

### 🧪 Примеры задач
- "How does the 'Math Mentor' GPT structure its explanations?"
- "What protection instructions do proactive agents use?"
- "Rebuild a 'Code Wizard' locally using open models"
- Analyze common patterns in 'Roleplay' GPTs
- Test if your own prompt protection is better than these

### ⚠️ Ограничения
- Ethical/Legal grey area (Use for research)
- Prompts may be outdated (authors update GPTs)
- No code/backend logic (only system prompt)
- Knowledge files often missing (just descriptions)
- Static content

### 🧭 Fit / Maturity / Ops
- **Fit:** Prompt Engineers, AI Security Researchers
- **Maturity:** archive (static updates)
- **Latency/Cost:** free
- **Data constraints:** text only
- **Ops friction:** zero (reading)

### Full links
- Repo: https://github.com/friuns2/Leaked-GPTs
- Stars: 2,405
- Maturity: active

---

## oasis (camel-ai)

**TL;DR:** OASIS (Open Agent Social Interaction Simulations). A simulator for large-scale agent societies. Can simulate up to one million agents interacting in a virtual social network. Useful for researching social dynamics, spread of misinformation, and agent behaviors at scale. 2k stars.

### Быстрый выбор
- ✅ Используй если:
  - Researching agent social dynamics
  - Simulating social networks (Tweet/Post style)
  - Stress testing agent interactions
  - "Sims" for LLM agents
  - CAMEL-AI ecosystem user
- ❌ Не используй если:
  - Single agent task solving
  - Production chatbots
  - Real-time user interaction
  - Small scale tests (overkill)

### 🚀 Запуск
```bash
git clone https://github.com/camel-ai/oasis
cd oasis
pip install -r requirements.txt
# Configure LLM backend (vLLM recommended for scale)
python main.py --config configs/social_sim.yaml
```

### 🧩 Архитектура
- **Engine:** Parallel agent execution
- **Environment:** Social platform simulation (posts, likes, follows)
- **Backend:** vLLM / LiteLLM for inference
- **Logic:** CAMEL agent framework
- **Entrypoints:** `oasis/` module

### 🧪 Примеры задач
- Simulate viral spread of a rumor
- Analyze agent polarization in debates
- Test recommendation algorithms on agent users
- Model economic interactions in a social graph
- Generate synthetic social media data

### ⚠️ Ограничения
- Requires massive compute for "million agents"
- Simulation fidelity vs Reality gap
- Configuration complexity
- Research focused (not a product builder)
- Heavy API costs if using closed models

### 🧭 Fit / Maturity / Ops
- **Fit:** Social Science researchers, AI Safety researchers
- **Maturity:** research (active)
- **Latency/Cost:** high compute/inference cost
- **Data constraints:** synthetic data generation
- **Ops friction:** high (cluster simulation)

### Full links
- Repo: https://github.com/camel-ai/oasis
- Original README: https://github.com/camel-ai/oasis/blob/main/README.md
- Stars: 2,372
- Maturity: active

---

## comfyui_LLM_party

**TL;DR:** Comprehensive LLM Agent framework for ComfyUI. Adds nodes for OpenAI, Ollama, ChatTTS, FLUX prompts, and MCP integration directly into ComfyUI workflows. Enables complex multi-modal pipelines (Text -> LLM -> Image -> Audio). 2k stars.

### Быстрый выбор
- ✅ Используй если:
  - Already using ComfyUI for generation
  - Need LLM logic in visual workflows
  - Building multi-modal agents (Text+Image+Audio)
  - Local LLM (Ollama) integration
  - Rapid prototyping without code
- ❌ Не используй если:
  - Pure code preference (LangChain)
  - Production API deployment (ComfyUI backend is heavy)
  - Distributed agent systems
  - Text-only workflows (overkill)

### 🚀 Запуск
```bash
cd ComfyUI/custom_nodes
git clone https://github.com/heshengtao/comfyui_LLM_party
pip install -r requirements.txt
# Restart ComfyUI
# Look for "LLM_Party" nodes
```

### 🧩 Архитектура
- **Core:** ComfyUI Custom Nodes (Python)
- **Integrations:** OpenAI, Ollama, MCP, Search tools
- **Flow:** Graph-based data passing
- **UI:** ComfyUI web interface
- **Entrypoints:** `__init__.py` in node folder

### 🧪 Примеры задач
- "Story Illustrator": LLM generates prompts -> FLUX generates images
- "Newscaster": Search web -> Summarize -> ChatTTS audio
- "Coding Helper": LLM reads file -> writes code (via MCP)
- "Persona Chat": Maintain context in visual flow
- Automate image captioning and tagging

### ⚠️ Ограничения
- ComfyUI learning curve
- Spaghetti graphs for complex logic
- State management is tricky in nodes
- Updates to ComfyUI can break nodes
- Python environment conflicts

### 🧭 Fit / Maturity / Ops
- **Fit:** Generative AI artists, ComfyUI power users
- **Maturity:** active (community node)
- **Latency/Cost:** local GPU dependent
- **Data constraints:** local processing
- **Ops friction:** medium (node installation)

### Full links
- Repo: https://github.com/heshengtao/comfyui_LLM_party
- Original README: https://github.com/heshengtao/comfyui_LLM_party/blob/main/README.md
- Stars: 2,082
- Maturity: active

---

## Awesome-OSINT-For-Everything

**TL;DR:** Curated collection of OSINT (Open Source Intelligence) tools for cybersecurity, reverse searching, bug bounty, red team, and general investigations. Covers search engines, social media, domain/IP, geolocation, image analysis, and more. Essential resource для security researchers и OSINT practitioners. 2k stars — comprehensive toolkit reference.

### Быстрый выбор
- ✅ Используй если:
  - Проводишь OSINT investigations
  - Bug bounty reconnaissance
  - Red team / pentesting recon phase
  - Reverse image/phone/email searches
  - Threat intelligence gathering
- ❌ Не используй если:
  - Нужен automated tool (это список, не software)
  - Looking for single specific tool
  - Illegal surveillance purposes
  - Prefer GUI tools only
  - Beginner without OSINT knowledge

### 🧩 Содержимое списка
- **Search Engines:** DuckDuckGo, Shodan, Censys, ZoomEye
- **Social Media OSINT:** Twitter/X, Facebook, LinkedIn, Instagram tools
- **Domain/IP:** WHOIS, DNS, reverse IP, subdomain finders
- **Image Analysis:** reverse image search, EXIF readers
- **Geolocation:** GeoINT tools, satellite imagery
- **Dark Web:** .onion search engines, Tor tools
- **Phone/Email:** lookup and verification tools
- **Ключевые секции:** organized by OSINT category

### 🧪 Примеры задач
- "Find email addresses for a domain"
- "Reverse search this phone number"
- "Identify location from this photo"
- "Enumerate subdomains for target"
- "Check social media presence"
- "Investigate leaked credentials"

### ⚠️ Ограничения
- List format only (no integrated platform)
- Tools may have varying quality/reliability
- Some tools require API keys or paid plans
- Legal/ethical considerations vary by jurisdiction
- Links may become outdated
- Requires manual navigation

### 🧭 Fit / Maturity / Ops
- **Fit:** security researchers, OSINT analysts, bug bounty hunters
- **Maturity:** curated list (community-maintained)
- **Latency/Cost:** free to browse; individual tools vary
- **Data constraints:** none (reference resource)
- **Ops friction:** zero (just read)

### Full links
- Repo: https://github.com/Astrosp/Awesome-OSINT-For-Everything
- Original README: https://github.com/Astrosp/Awesome-OSINT-For-Everything/blob/main/README.md
- Stars: 1,982
- Maturity: curated list

---

## free-llm-api-resources

**TL;DR:** Curated list of free LLM API resources — бесплатные endpoints для GPT, Claude, и open-source models. For testing, learning, side projects. Updated regularly. 8k stars — essential для budget-conscious developers.

### Быстрый выбор
- ✅ Используй если:
  - Need free LLM APIs for testing
  - Learning/experimenting
  - Side projects без бюджета
  - Comparing different providers
  - API access без credit card
- ❌ Не используй если:
  - Production workloads (rate limits)
  - Need reliability guarantees
  - Privacy-sensitive data
  - High volume requests

### 🧩 Содержимое
- **Free tiers:** OpenAI, Anthropic, Google trial credits
- **Open endpoints:** community-hosted APIs
- **Proxy services:** free API access points
- **Rate limits:** documented quotas
- **Setup guides:** how to access each resource
- **Ключевые файлы:** organized by provider

### 🧪 Примеры задач
- "Try GPT-4 without credit card"
- "Test Claude for free"
- "Compare models before paying"
- Development/testing without costs
- Educational projects

### ⚠️ Ограничения
- Rate limits (usually low)
- No SLA or guarantees
- Endpoints may disappear
- Some require signup
- Quality varies
- Not for production

### 🧭 Fit / Maturity / Ops
- **Fit:** learning, testing, budget projects
- **Maturity:** curated list (community maintained)
- **Ops friction:** varies by provider

### Full links
- Repo: https://github.com/free-llm-api-resources/list
- Original README: https://github.com/free-llm-api-resources/list/blob/main/README.md
- Stars: 7,793
- Maturity: curated list

---

## CyberSources

**TL;DR:** Curated list of cybersecurity tools, resources, and educational materials. Covers pentesting tools, CTF resources, malware analysis, network security, and learning platforms. Well-organized reference для security professionals и students. 2k stars — solid starting point для cybersec toolkit.

### Быстрый выбор
- ✅ Используй если:
  - Ищешь cybersecurity tools reference
  - Preparing for CTF competitions
  - Learning pentesting/red team
  - Need malware analysis resources
  - Building security toolkit
- ❌ Не используй если:
  - Need production security platform
  - Looking for specific tool (use search)
  - Enterprise security solutions
  - Already expert with established toolkit
  - Non-English resources needed

### 🧩 Содержимое списка
- **Pentesting:** Kali tools, exploitation frameworks
- **CTF Resources:** platforms, writeups, practice
- **Malware Analysis:** sandboxes, disassemblers, debuggers
- **Network Security:** packet analysis, firewalls, IDS/IPS
- **Learning Platforms:** HTB, TryHackMe, courses
- **Certifications:** OSCP, CEH, prep resources
- **Ключевые секции:** organized by security domain

### 🧪 Примеры задач
- "Find good CTF practice platforms"
- "Get started with malware analysis"
- "Learn network packet analysis"
- "Prepare for OSCP certification"
- "Discover reverse engineering tools"
- "Build a Kali-like toolkit"

### ⚠️ Ограничения
- Reference list only (no integrated tool)
- Some links may be outdated
- Quality of listed tools varies
- Requires own research for selection
- English-focused resources
- No direct support

### 🧭 Fit / Maturity / Ops
- **Fit:** security students, pentesters, CTF players
- **Maturity:** curated list (community-maintained)
- **Latency/Cost:** free to browse
- **Data constraints:** none (reference resource)
- **Ops friction:** zero (just read)

### Full links
- Repo: https://github.com/bst04/CyberSources
- Original README: https://github.com/bst04/CyberSources/blob/main/README.md
- Stars: 1,988
- Maturity: curated list

---

## twitter-api-client

**TL;DR:** Implementation of X/Twitter v1, v2, and GraphQL APIs. A reverse-engineered client that allows scraping and automated interactions without official expensive API keys. Mimics browser behavior to access internal Twitter endpoints. 2k stars.

### Быстрый выбор
- ✅ Используй если:
  - Scraping Tweets, Profiles, or Followers
  - Automating interactions (Like, Retweet, Post)
  - Official API is too expensive or restricted
  - Need access to "For You" timeline logic
  - Node.js environment
- ❌ Не используй если:
  - Strict TOS compliance required
  - Business critical uptime reliability (can break if X changes URL)
  - High velocity scraping (use official enterprise API if possible)
  - Account safety is paramount (bot detection risk)

### 🚀 Запуск
```bash
npm install twitter-api-client
```
```javascript
import { TwitterClient } from 'twitter-api-client';

const client = new TwitterClient({
  apiKey: '...', // OR use cookie-based auth for scraping
  cookie: 'auth_token=...' 
});

const tweets = await client.tweet.search({ q: 'AI Agents' });
```

### 🧩 Архитектура
- **Core:** TypeScript wrapper around X.com internal API
- **Auth:** Cookies (auth_token) or API Keys
- **Protocol:** HTTP/1.1 (GraphQL endpoints)
- **Features:** Search, Tweet, User, Media upload
- **Entrypoints:** `TwitterClient` class

### 🧪 Примеры задач
- Scrape 1000 latest tweets about "DeepSeek"
- Automate daily thread posting
- Monitor user profile changes
- Download media from specific accounts
- Analyze sentiment of replies to a tweet

### ⚠️ Ограничения
- High risk of account suspension (if using cookies)
- Endpoints change frequently (requires updates)
- Rate limits are undocumented and variable
- Not an official SDK
- Requires valid session cookies for most features

### 🧭 Fit / Maturity / Ops
- **Fit:** Data scrapers, Bot developers (grey hat)
- **Maturity:** active (arms race with X)
- **Latency/Cost:** free (risk based)
- **Data constraints:** X.com data only
- **Ops friction:** high (cookie management)

### Full links
- Repo: https://github.com/trevorhobenshield/twitter-api-client
- Original README: https://github.com/trevorhobenshield/twitter-api-client/blob/main/README.md
- Stars: 1,877
- Maturity: active

---

## ai-gradio

**TL;DR:** A Python library that creates instant Gradio UIs for various AI providers (OpenAI, Claude, Gemini, LangChain). Simplifies creating "Playgrounds" or demo interfaces for LLMs with a single line of code. 2k stars.

### Быстрый выбор
- ✅ Используй если:
  - Need a quick UI for your model
  - Prototyping LLM applications
  - Demoing simple Chat interfaces
  - Support for multiple providers out-of-the-box
  - Zero frontend code knowledge
- ❌ Не используй если:
  - Building production consumer apps (React/Next.js better)
  - Custom refined UX design needed
  - High concurrency requirements
  - Complex state management required

### 🚀 Запуск
```bash
pip install ai-gradio
```
```python
import ai_gradio

# One-liner to launch UI
ai_gradio.load("gpt-4-turbo", provider="openai").launch()
```

### 🧩 Архитектура
- **Core:** Gradio wrapper
- **Providers:** Registry of API clients
- **UI:** Standard Gradio ChatInterface
- **Configuration:** Environment variables for keys
- **Entrypoints:** `ai_gradio.load()`

### 🧪 Примеры задач
- Launch a local UI for a finetuned model
- Compare output of GPT-4 vs Claude 3.5 side-by-side
- Create a shareable demo link for stakeholders
- Test prompt engineering with visual feedback
- Wrap a LangChain agent in a web interface

### ⚠️ Ограничения
- Limited customization (Gradio constraints)
- Not for commercial SaaS deployment
- Latency added by Gradio server
- Dependency on specific provider SDK versions
- Simple chat focus (not complex workflows)

### 🧭 Fit / Maturity / Ops
- **Fit:** Python devs, Data Scientists
- **Maturity:** active
- **Latency/Cost:** free (local compute)
- **Data constraints:** usage of API providers
- **Ops friction:** low (pip install)

### Full links
- Repo: https://github.com/AK391/ai-gradio
- Original README: https://github.com/AK391/ai-gradio/blob/main/README.md
- Stars: 1,646
- Maturity: active

---

## Telegram-OSINT

**TL;DR:** In-depth Telegram OSINT resources covering tools, techniques & tradecraft. 2k stars.

### Full links
- Repo: https://github.com/The-Osint-Toolbox/Telegram-OSINT
- Stars: 1,626
- Maturity: curated list

---

## solana-agent-kit

**TL;DR:** Toolkit to connect AI agents to Solana protocols. Provides LangChain tools/functions for trading, staking, lending, and exploring Solana, enabling agents to perform on-chain actions autonomously. 2k stars.

### Быстрый выбор
- ✅ Используй если:
  - Building AI agents that trade on Solana
  - Need pre-built tools for Jupiter, Pump.fun, Meteora
  - LangChain integration required
  - Automating DeFi strategies with LLMs
  - Hackathon entry for Solana AI track
- ❌ Не используй если:
  - Building a standard dapp (use standard web3.js/solana-web3)
  - Need high-frequency trading execution (too slow via LLM)
  - EVM chains required
  - Non-agent context

### 🚀 Запуск
```bash
npm install solana-agent-kit
```
```typescript
import { SolanaAgentKit, createSolanaTools } from 'solana-agent-kit';

const agent = new SolanaAgentKit(privateKey, rpcUrl, openAiKey);
const tools = createSolanaTools(agent);
// Use 'tools' in your LangChain agent
```

### 🧩 Архитектура
- **Core:** LangChain Tools wrapper
- **Chain:** Solana (Mainnet/Devnet)
- **Protocols:** Jupiter (Swap), Pump.fun (Launch), Meteora, etc.
- **Wallet:** Keypair management
- **Entrypoints:** `SolanaAgentKit` class

### 🧪 Примеры задач
- "Launch a new token on pump.fun with name $AIAGENT"
- "Swap 1 SOL for USDC on Jupiter"
- "Check balance and transfer 50% to wallet X"
- "Deploy a collection of NFTs"
- "Lend assets on Marginfi"

### ⚠️ Ограничения
- Dangerous if private keys managed poorly
- Protocol support is manual (depends on updates)
- LLM hallucinations can cause loss of funds
- Beta quality (fast moving ecosystem)
- Rate limits of public RPCs

### 🧭 Fit / Maturity / Ops
- **Fit:** Web3 AI developers, Solana ecosystem
- **Maturity:** active (beta)
- **Latency/Cost:** transaction fees + RPC cost
- **Data constraints:** on-chain data
- **Ops friction:** medium (wallet management)

### Full links
- Repo: https://github.com/sendaifun/solana-agent-kit
- Original README: https://github.com/sendaifun/solana-agent-kit/blob/main/README.md
- Stars: 1,599
- Maturity: active

---

## QuantMuse

**TL;DR:** Comprehensive quantitative trading systems with AI-powered analysis. Open-source framework for backtesting, strategy development, and deploying trading bots using modern AI/ML techniques. 2k stars.

### Быстрый выбор
- ✅ Используй если:
  - Developing algorithmic trading strategies
  - Researching AI in finance
  - Backtesting required before live trading
  - Python-based quantitative stack
  - Analyzing market data with ML
- ❌ Не используй если:
  - Simple "buy and hold" investing
  - No Python/Stats background
  - Proprietary institutional software preferred
  - High-frequency trading (latency limitations of Python)

### 🚀 Запуск
```bash
git clone https://github.com/0xemmkty/QuantMuse
cd QuantMuse
pip install -r requirements.txt
# Configure data sources
python main.py --strategy mean_reversion
```

### 🧩 Архитектура
- **Core:** Backtesting engine & Data loader
- **AI:** PyTorch/Scikit-learn models for prediction
- **Data:** Connectors for Yahoo Finance, AlphaVantage, Binace
- **Strategies:** Object-oriented strategy interface
- **Entrypoints:** `main.py`

### 🧪 Примеры задач
- Backtest a LSTM-based price prediction strategy
- Optimize portfolio allocation using Reinforcement Learning
- Analyze sentiment impact on crypto assets
- Pairs trading implementing cointegration
- Deploy a paper-trading bot on Binance

### ⚠️ Ограничения
- Financial risk (use at own risk)
- Data quality determines performance
- Overfitting is a common pitfall
- Maintenance of API connectors
- Not a financial advisor

### 🧭 Fit / Maturity / Ops
- **Fit:** Quants, Algo-traders, Financial Engineers
- **Maturity:** active
- **Latency/Cost:** data API costs
- **Data constraints:** historical financial data
- **Ops friction:** high (strategy validation)

### Full links
- Repo: https://github.com/0xemmkty/QuantMuse
- Original README: https://github.com/0xemmkty/QuantMuse/blob/main/README.md
- Stars: 1,562
- Maturity: active

---

## terminal (m4tt72)

**TL;DR:** Customizable "Hacker Mode" website template. A personal website/portfolio designed to look and feel like a developer terminal. Supports custom commands, themes, and interactive filesystem navigation for your resume or blog. 1k stars.

### Быстрый выбор
- ✅ Используй если:
  - Building a developer portfolio/resume
  - Want a "geeky" terminal aesthetic for a personal site
  - Comfortable editing JSON configuration
  - Need a lightweight, dependency-free landing page
  - Showcasing CLI skills
- ❌ Не используй если:
  - Non-technical audience (UX is confusing to normals)
  - Need SEO optimized blog (text is hidden in logic)
  - Mobile responsiveness is top priority (keyboards on phones are hard)
  - Building a complex web application

### 🚀 Запуск
```bash
git clone https://github.com/m4tt72/terminal
# Open index.html in browser
# Edit config.json to change commands and text
```

### 🧩 Архитектура
- **Tech:** Pure HTML/JS/CSS (No frameworks)
- **Config:** `config.json` drives the content
- **Interaction:** Input parser for commands (ls, cat, help)
- **Styling:** CSS themes (Retro/Matrix style)
- **Entrypoints:** `index.html`, `js/main.js`

### 🧪 Примеры задач
- "Create a resume where 'cat experience.txt' shows history"
- "Add a 'contact' command that opens email client"
- "Hide easter eggs like 'sudo' or 'matrix' mode"
- "Link to GitHub projects purely via CLI interface"
- "Host on GitHub Pages for free"

### ⚠️ Ограничения
- Accessibility issues (screen readers)
- Not a real terminal (no backend execution)
- Hard to navigate for non-techies
- Limited to text-based content (images are awkward)
- Manual content updates

### 🧭 Fit / Maturity / Ops
- **Fit:** Developers, System Admins, Cybersec portfolios
- **Maturity:** stable (finished project)
- **Latency/Cost:** static hosting (free)
- **Data constraints:** public static content
- **Ops friction:** low (edit config)

### Full links
- Repo: https://github.com/m4tt72/terminal
- Original README: https://github.com/m4tt72/terminal/blob/main/README.md
- Stars: 1,498
- Maturity: stable

---

## russia-mobile-internet-whitelist

**TL;DR:** Domains and IPs that remain accessible in Russia when mobile internet gets restricted or censored. Maintained whitelist for bypass configurations. Critical resource для users in restricted network environments. 1k stars — survival kit для connectivity.

### Быстрый выбор
- ✅ Используй если:
  - Living/traveling in Russia
  - Mobile internet restrictions active
  - Configuring VPN/proxy split tunneling
  - Need access to whitelisted services
  - Research on internet censorship
- ❌ Не используй если:
  - Not in Russia (not applicable)
  - Full VPN already working
  - Corporate security requirements
  - Looking for VPN service itself
  - Need 100% guaranteed access

### 🚀 Запуск
```bash
# Clone and use with routing software
git clone https://github.com/hxehex/russia-mobile-internet-whitelist
cd russia-mobile-internet-whitelist

# Import to routing table / VPN split tunneling
# Example: use with sing-box, xray, etc.
# See README for format-specific usage
```

### 🧩 Содержимое
- **Domain lists:** services that stay accessible
- **IP ranges:** direct IP whitelists
- **Formats:** plain text, JSON, routing config
- **Updates:** regularly maintained as censorship evolves
- **Categories:** banking, government, essential services
- **Ключевые файлы:** domain lists, IP lists

### 🧪 Примеры задач
- Configure split tunneling for essential services
- Maintain banking app access during restrictions
- Access government services without VPN
- Research Russian internet censorship patterns
- Build routing rules for proxy software

### ⚠️ Ограничения
- Region-specific (Russia only)
- Censorship patterns change frequently
- No guarantee of completeness
- Legal considerations vary
- Requires technical routing knowledge
- Not a VPN/proxy solution itself

### 🧭 Fit / Maturity / Ops
- **Fit:** users in Russia, censorship researchers
- **Maturity:** active (regularly updated)
- **Latency/Cost:** free; reduces VPN overhead
- **Data constraints:** none (public lists)
- **Ops friction:** medium (requires routing config)

### Full links
- Repo: https://github.com/hxehex/russia-mobile-internet-whitelist
- Stars: 1,313
- Maturity: active

---

## IQuest-Coder-V1

**TL;DR:** IQuest Coder V1 — AI coding assistant model fine-tuned for code generation and completion tasks. Specialized for software development workflows with instruction-following capabilities. Part of IQuestLab's model series. 1k stars.

### Быстрый выбор
- ✅ Используй если:
  - Need open-source coding model
  - Local code completion setup
  - Instruction-following code tasks
  - Research/evaluation of coding LLMs
  - Integration into custom IDE tools
- ❌ Не используй если:
  - Production use (use Claude/GPT-4)
  - Limited GPU resources
  - Need guaranteed code quality
  - Complex multi-file refactoring
  - Enterprise support required

### 🚀 Запуск
```bash
# Using transformers
pip install transformers accelerate

python -c "
from transformers import AutoModelForCausalLM, AutoTokenizer
model = AutoModelForCausalLM.from_pretrained('IQuestLab/IQuest-Coder-V1')
tokenizer = AutoTokenizer.from_pretrained('IQuestLab/IQuest-Coder-V1')
# Generate code
"

# Or via Ollama (if available)
# ollama run iquest-coder-v1
```

### 🧩 Архитектура
- **Type:** Causal Language Model (decoder-only)
- **Base:** Likely fine-tuned from open base (Llama/Mistral family)
- **Specialization:** Code generation, completion
- **Format:** Instruction-following format
- **Ключевые файлы:** model weights on HuggingFace

### 🧪 Примеры задач
- Code completion in IDE
- Generate functions from docstrings
- Explain existing code
- Convert code between languages
- Fix simple bugs

### ⚠️ Ограничения
- Model quality may vary vs. commercial
- GPU/VRAM requirements
- Limited context window
- May produce incorrect code
- Less community support
- Benchmark results not extensively published

### 🧭 Fit / Maturity / Ops
- **Fit:** researchers, hobbyists, local-first developers
- **Maturity:** active (v1 release)
- **Latency/Cost:** local GPU inference
- **Data constraints:** model weights download
- **Ops friction:** medium (requires inference setup)

### Full links
- Repo: https://github.com/IQuestLab/IQuest-Coder-V1
- Stars: 1,278
- Maturity: active

---

## LLMRouter

**TL;DR:** Open-Source Library for LLM Routing. Intelligently routes queries to the most appropriate or cost-effective model (e.g., query -> GPT-4 vs Llama-3-8b). Optimizes for cost, latency, and quality. 1k stars.

### Быстрый выбор
- ✅ Используй если:
  - Using multiple LLM providers
  - Reducing API costs is a priority
  - Have mixed traffic (simple & complex queries)
  - Need failover mechanisms
  - A/B testing models
- ❌ Не используй если:
  - Single model is sufficient
  - Routing latency overhead is unacceptable (>50ms)
  - Complex custom routing requirements
  - Using a gateway that already does this (LiteLLM/Portkey)

### 🚀 Запуск
```bash
pip install llmrouter
```
```python
from llmrouter import Router

router = Router(models=["gpt-4", "llama-3-70b", "mistral-small"])
response = router.route("What is 2+2?", optimization="cost")
print(response)
```

### 🧩 Архитектура
- **Core:** Classification/Routing logic
- **Strategy:** Pattern matching, Embedding similarity, or ML classifier
- **Clients:** Wrappers for standard provider APIs
- **Config:** JSON/YAML routing rules
- **Entrypoints:** `llmrouter` package

### 🧪 Примеры задач
- Route coding questions to Claude-3.5-Sonnet, chat to GPT-4o-mini
- Fallback to Azure OpenAI if OpenAI API is down
- Route sensitive PII data to local model
- Route short queries to faster models
- Optimize monthly spend by maxing out cheaper quotas

### ⚠️ Ограничения
- Routing adds latency
- Classifier accuracy (mis-routing complex prompts)
- Dependency on uptime of all connected providers
- Configuration overhead
- Less mature than LiteLLM

### 🧭 Fit / Maturity / Ops
- **Fit:** Backend engineers, Cost optimization focus
- **Maturity:** active
- **Latency/Cost:** adds small hop latency
- **Data constraints:** none
- **Ops friction:** low (library)

### Full links
- Repo: https://github.com/ulab-uiuc/LLMRouter
- Original README: https://github.com/ulab-uiuc/LLMRouter/blob/main/README.md
- Stars: 1,182
- Maturity: active

---

## jito-labs/mev-bot

**TL;DR:** Reference implementation of a Solana MEV (Maximal Extractable Value) bot by Jito Labs. Demonstrates how to search for arbitrage/liquidation opportunities and bundle transactions using the Jito Block Engine for guaranteed execution. 1k stars.

### Быстрый выбор
- ✅ Используй если:
  - Building high-frequency trading bots on Solana
  - Researching MEV strategies (Atomic Arb, Backrunning)
  - Using Jito Bundles for transaction atomicity
  - Need Rust-based high-performance skeleton
  - Understanding Solana's transaction simulation flow
- ❌ Не используй если:
  - Beginner to Rust or Solana
  - Managing small capital (rent/fees high)
  - Expecting "plug-and-play" profit (strategy logic needed)
  - Risk averse (MEV is competitive and risky)

### 🚀 Запуск
```bash
git clone https://github.com/jito-labs/mev-bot
cd mev-bot
cargo build --release
# Requires active searcher key enabled by Jito
# Configure Jito Block Engine URL
./target/release/mev-bot
```

### 🧩 Архитектура
- **Language:** Rust (Tokio async)
- **Integration:** Jito Block Engine (gRPC)
- **Logic:** Stream mempool -> Simulate -> Bundle -> Send
- **Components:** `searcher`, `bundler`, `simulator`
- **Entrypoints:** `src/main.rs`

### 🧪 Примеры задач
- Detect un-balanced pools on Orca/Raydium
- Simulate "Flash Loan" arbitrage paths
- Bundle "Buy -> Sell" transactions atomically
- Avoid revert fees by simulating before sending
- Compete for block inclusion tip auctions

### ⚠️ Ограничения
- Competitive zero-sum game
- Requires specialized access (Jito Block Engine)
- Rust proficiency required
- Network latency critical (need colocated servers)
- Strategy is NOT provided (only infrastructure)

### 🧭 Fit / Maturity / Ops
- **Fit:** MEV Searchers, HFT Engineers
- **Maturity:** reference (educational/foundation)
- **Latency/Cost:** microsecond latency required
- **Data constraints:** real-time blockchain stream
- **Ops friction:** high (infrastructure)

### Full links
- Repo: https://github.com/jito-labs/mev-bot
- Original README: https://github.com/jito-labs/mev-bot/blob/main/README.md
- Stars: 1,181
- Maturity: active

---

## listen (piotrostr)

**TL;DR:** "DeFAI Swiss Army Knife". A toolkit for building on-chain AI agents on Solana. Includes a dashboard for monitoring agent wallets, creating tokens, and managing liquidity. Simplified interface for deploying agent infrastructure. 1k stars.

### Быстрый выбор
- ✅ Используй если:
  - Launching an AI agent token on Solana
  - Monitoring agent treasury/activity
  - Need a visual dashboard for "headless" agents
  - Rapid deployment of agent infrastructure
  - Web3 integration without deep rust knowledge
- ❌ Не используй если:
  - Building complex off-chain reasoning only
  - EVM focused (Solana only)
  - Need custom smart contract logic (uses standards)
  - Enterprise security required (experimental)

### 🚀 Запуск
```bash
git clone https://github.com/piotrostr/listen
cd listen
# Frontend dashboard
pnpm install
pnpm dev
# Connect agent wallet
```

### 🧩 Архитектура
- **Frontend:** Next.js Dashboard
- **Backend:** Node.js / Rust helpers
- **Chain:** Solana (RPC integration)
- **Features:** Portfolio tracking, Token launchpad, Swap interface
- **Entrypoints:** `apps/web`

### 🧪 Примеры задач
- "Create a dashboard to show my agent's trading PnL"
- "Launch a token for the agent community"
- "Visualize wallet balances across multiple agents"
- "Manually intervene in agent trades via UI"
- "Set up donation addresses for the bot"

### ⚠️ Ограничения
- Early stage (alpha quality)
- Solana ecosystem specific
- Dependency on specific wallet standards
- Limited documentation
- Security of connected wallets (hot wallet risk)

### 🧭 Fit / Maturity / Ops
- **Fit:** Crypto AI builders, DeFAI experiments
- **Maturity:** active (experimental)
- **Latency/Cost:** Solana fees
- **Data constraints:** On-chain data
- **Ops friction:** medium (wallet setup)

### Full links
- Repo: https://github.com/piotrostr/listen
- Original README: https://github.com/piotrostr/listen/blob/main/README.md
- Stars: 1,083
- Maturity: active

---

## Free-APIs

**TL;DR:** Curated collection of free APIs for developers — covers finance, weather, news, entertainment, translation, image generation и многое другое. Organized by category with documentation links. Ideal resource для side projects, hackathons, and learning. 1k stars — essential reference для API discovery.

### Быстрый выбор
- ✅ Используй если:
  - Finding free APIs for side projects
  - Hackathon rapid prototyping
  - Learning API integration
  - Testing without paid subscriptions
  - Discovering new data sources
- ❌ Не используй если:
  - Production reliability critical
  - High-volume requests needed (rate limits)
  - Enterprise SLA requirements
  - Sensitive data handling
  - Specific niche API (use direct search)

### 🧩 Содержимое списка
- **Weather:** OpenWeatherMap, WeatherAPI free tiers
- **Finance:** Stock quotes, crypto prices
- **News:** NewsAPI, RSS feeds
- **Entertainment:** Movies, games, music APIs
- **Translation:** Google Translate alternatives
- **AI/ML:** free inference endpoints
- **Utilities:** URL shorteners, QR generators
- **Ключевые секции:** categorized by API type

### 🧪 Примеры задач
- "Find free weather API for my app"
- "Get crypto price data without API key"
- "Free image generation API for prototyping"
- "Currency conversion API for hackathon"
- "Movie database for personal project"
- "Translation API alternatives"

### ⚠️ Ограничения
- Free = rate limits (most limit requests)
- Documentation quality varies
- Services may discontinue
- No SLA or support
- Some require free signup
- Not all are truly "free forever"

### 🧭 Fit / Maturity / Ops
- **Fit:** hobbyists, students, hackathon participants
- **Maturity:** curated list (community-maintained)
- **Latency/Cost:** free (within limits)
- **Data constraints:** varies by API
- **Ops friction:** zero (just read and use)

### Full links
- Repo: https://github.com/Free-APIs/Free-APIs.github.io
- Stars: 1,059
- Maturity: curated list

---

## goat-sdk/goat

**TL;DR:** GOAT (Great On-chain Agent Toolkit). The leading open-source framework for connecting AI agents to blockchain protocols. Provides a unified API for agents to interact with trading, swapping, and staking across multiple chains (EVM, Solana, SUI, etc.). 1k stars.

### Быстрый выбор
- ✅ Используй если:
  - Building multi-chain AI agents
  - Need a standardized "Wallet" interface for LLMs
  - Integrating DeFi actions (Uniswap, Jupiter, AAVE)
  - Want Type-safe interactions
  - Reducing boilerplate for on-chain tools
- ❌ Не используй если:
  - Single specific protocol deep integration needed (might need custom ABI)
  - Non-TypeScript environment (SDK is TS)
  - Only need simple read-only data (use viem/ethers)
  - Building a traditional frontend (use wagmi)

### 🚀 Запуск
```bash
npm install @goat-sdk/core @goat-sdk/adapter-openai @goat-sdk/wallet-evm
```
```typescript
import { GoatSdk } from '@goat-sdk/core';
import { openai } from '@goat-sdk/adapter-openai';

const goat = new GoatSdk({
  wallet: evmWallet,
  plugins: [uniswap(), erc20()]
});
// Now the LLM can "swap tokens"
```

### 🧩 Архитектура
- **Core:** Core SDK managing tool registration
- **Adapters:** Connectors for LLM providers (OpenAI, Anthropic, LangChain)
- **Wallets:** Abstract wallet implementations (EVM, Solana)
- **Plugins:** Modular protocol integrations (ERC20, Uniswap, etc.)
- **Entrypoints:** `@goat-sdk/core`

### 🧪 Примеры задач
- "Create an agent that rebalances a portfolio across 3 chains"
- "Swap USDC to ETH when gas is low"
- "Claim airdrops automatically"
- "Bridge assets from Optimism to Base"
- "Monitor and stake tokens in AAVE"

### ⚠️ Ограничения
- Newer library (frequent breaking changes)
- Limited coverage of niche protocols
- Debugging agent transactions can be hard
- Risk of draining wallets if LLM hallucinates
- TypeScript focus

### 🧭 Fit / Maturity / Ops
- **Fit:** Web3 AI Developers, DeFi Automation
- **Maturity:** active (growing standard)
- **Latency/Cost:** on-chain costs
- **Data constraints:** blockchain data
- **Ops friction:** medium (wallet security)

### Full links
- Repo: https://github.com/goat-sdk/goat
- Original README: https://github.com/goat-sdk/goat/blob/main/README.md
- Stars: ~945
- Maturity: active

---

## ChatGemini

**TL;DR:** Conversational Web Client for Google Gemini. A clean, responsive chat interface mimicking the ChatGPT experience, powered by the Gemini Pro API. Supports streaming, markdown rendering, and chat history. 1k stars.

### Быстрый выбор
- ✅ Используй если:
  - Need a self-hosted UI for Gemini
  - Want to bypass official Google UI restrictions
  - Integrating Gemini into a custom internal tool
  - Learning how to build Chat UIs with standard web tech
  - Prefer Vue.js framework
- ❌ Не используй если:
  - Need multi-model support (use ChatBox or LibreChat)
  - require highly complex agentic features (this is a chat client)
  - iOS/Android native app needed
  - Production enterprise SSO integration features required

### 🚀 Запуск
```bash
git clone https://github.com/bclswl0827/ChatGemini
cd ChatGemini
npm install
# Set VITE_GEMINI_API_KEY
npm run dev
```

### 🧩 Архитектура
- **Frontend:** Vue 3 + Naive UI
- **Build:** Vite
- **State:** Pinia
- **API:** Google Gemini API (Direct or via Proxy)
- **Entrypoints:** `src/App.vue`

### 🧪 Примеры задач
- Deploy a private Gemini interface for your team
- Customize the UI theme to match your brand
- Add custom system prompts pre-configured in the UI
- Use as a lightweight alternative to heavy chat apps
- Inspect API traffic for debugging Gemini responses

### ⚠️ Ограничения
- Features limited to Gemini capabilities
- Maintenance depends on solo developer
- No built-in RAG or plugins
- Client-side storage limitations
- Google API rate limits apply

### 🧭 Fit / Maturity / Ops
- **Fit:** Vue developers, Gemini users
- **Maturity:** active
- **Latency/Cost:** free (self-hosted)
- **Data constraints:** Google API usage
- **Ops friction:** low (static site)

### Full links
- Repo: https://github.com/bclswl0827/ChatGemini
- Original README: https://github.com/bclswl0827/ChatGemini/blob/main/README.md
- Stars: ~930
- Maturity: active

---

## ai-prompts (instructa)

**TL;DR:** Curated AI Prompts and rules for Cursor, Cline, Windsurf, GitHub Copilot, and other AI coding assistants. Ready-to-use `.cursorrules`, system prompts, and workflow templates. Updated regularly with new patterns. 1k stars — essential collection for AI-assisted coding setup.

### Быстрый выбор
- ✅ Используй если:
  - Configuring Cursor/Copilot/Windsurf rules
  - Need ready-made system prompts
  - Learning prompt engineering for coding
  - Starting new project with AI assistance
  - Comparing different prompting styles
- ❌ Не используй если:
  - Already have optimized custom prompts
  - Need framework-specific deep prompts
  - Looking for non-coding AI prompts
  - Prefer to write from scratch
  - Need prompts for enterprise-specific tools

### 🧩 Содержимое списка
- **Cursor Rules:** `.cursorrules` templates
- **Copilot:** custom instructions, snippets
- **Windsurf:** configuration examples
- **Cline:** CLI prompts and workflows
- **General:** system prompt templates
- **Specialized:** frontend, backend, devops prompts
- **Ключевые секции:** organized by tool/purpose

### 🧪 Примеры задач
- "Get .cursorrules for React+TypeScript project"
- "Configure Copilot for Python best practices"
- "Find DevOps-focused system prompts"
- "Setup Windsurf for Rust development"
- "Learn effective AI coding prompts"
- "Customize prompts for specific frameworks"

### ⚠️ Ограничения
- Quality varies by contributor
- May need customization for specific needs
- Tools evolve faster than prompts
- Not all prompts tested extensively
- Copy-paste may need adaptation
- Opinionated styles may not fit everyone

### 🧭 Fit / Maturity / Ops
- **Fit:** developers using AI coding tools
- **Maturity:** curated list (actively maintained)
- **Latency/Cost:** free (just copy/paste)
- **Data constraints:** none
- **Ops friction:** zero (configuration files)

### Full links
- Repo: https://github.com/instructa/ai-prompts
- Stars: 907
- Maturity: curated list

---

## telegram-web-app-bot-example

**TL;DR:** Reference implementation of a Telegram Mini App (TWA). Demonstrates how to connect a Telegram Bot with a React-based web frontend running inside the messenger. Includes authentication, theme parameters, and haptic feedback integration. 1k stars.

### Быстрый выбор
- ✅ Используй если:
  - Building Telegram Mini Apps (TMA)
  - Need a starting boilerplate for React + TG Bot
  - Learning interaction between Bot API and Web App
  - Implementing "Ton" or "Crypto" apps inside Telegram
  - Mobile-first design requirement
- ❌ Не используй если:
  - Building a simple text-only bot (use aiogram/python-telegram-bot)
  - Desktop-first application
  - No need for user identity verification
  - Using Vue/Svelte (this is React)

### 🚀 Запуск
```bash
git clone https://github.com/revenkroz/telegram-web-app-bot-example
cd telegram-web-app-bot-example
npm install
npm run dev
# Needs HTTPS (tunnel via ngrok) to work in Telegram
```

### 🧩 Архитектура
- **Updates:** React 18, Vite
- **Identity:** `window.Telegram.WebApp` API
- **Backend:** Node.js (Express/NestJS usually paired)
- **Styling:** CSS Modules / standard CSS
- **Entrypoints:** `src/main.tsx`

### 🧪 Примеры задач
- "Create a crypto wallet interface inside Telegram"
- "Build an e-commerce store as a bot menu"
- "Launch a clicker game (Hamster Kombat clone)"
- "Form submission interface for better UX"
- "Settings dashboard for a complex bot"

### ⚠️ Ограничения
- Telegram Webview limitations (performance, caching)
- Debugging is painful (mobile + iframe)
- Requires HTTPS tunnel for dev
- Platform dependency (Telegram only)
- UX constrained by mobile screen

### 🧭 Fit / Maturity / Ops
- **Fit:** Telegram developers, Mini App builders
- **Maturity:** reference (stable)
- **Latency/Cost:** hosting cost
- **Data constraints:** Telegram user data
- **Ops friction:** medium (SSL/Tunneling)

### Full links
- Repo: https://github.com/revenkroz/telegram-web-app-bot-example
- Original README: https://github.com/revenkroz/telegram-web-app-bot-example/blob/main/README.md
- Stars: 876
- Maturity: active

---

## n8n-workflows

**TL;DR:** All n8n workflows collection. 50k stars.

### Full links
- Repo: https://github.com/Zie619/n8n-workflows
- Original README: https://github.com/Zie619/n8n-workflows/blob/main/README.md
- Stars: 50,461
- Maturity: curated list

---

## MediaCrawler

**TL;DR:** Powerful crawler for multiple Chinese social media platforms. Supports scraping data (videos, comments, posts) from Xiaohongshu, Douyin, Kuaishou, Bilibili, Weibo, and Zhihu. Uses Playwright and stealth techniques to bypass common anti-scraping measures. 43k stars.

### Быстрый выбор
- ✅ Используй если:
  - Scraping Chinese social media data
  - Need to bypass login/captcha (uses login cookies)
  - Analyzing sentiment or trends in China
  - Archiving video content from Douyin/Kuaishou
  - Python ecosystem
- ❌ Не используй если:
  - Targeting Western platforms (Twitter/Meta)
  - Need official API reliability (reverse-engineered)
  - Cannot handle Chinese UI/content
  - High concurrency production crawler (Playwright is resource heavy)

### 🚀 Запуск
```bash
git clone https://github.com/NanmiCoder/MediaCrawler
cd MediaCrawler
pip install -r requirements.txt
playwright install
# Configure config.yaml with cookies
python main.py --platform xhs --type search --keywords "AI"
```

### 🧩 Архитектура
- **Core:** Playwright / DrissionPage for browser automation
- **Database:** Save to MySQL / CS
- **Bypass:** Stealth scripts, Cookie persistence
- **Platforms:** Module based (xhs, dy, ks, bili, wb)
- **Entrypoints:** `main.py`

### 🧪 Примеры задач
- "Scrape top 100 fashion posts from Xiaohongshu"
- "Download all videos from a specific Douyin creator"
- "Gather comments from Bilibili tech videos"
- "Monitor Weibo trending topics including 'DeepSeek'"
- "Archive Zhihu answers for RAG dataset"

### ⚠️ Ограничения
- High risk of IP blocking (need residential proxies)
- Accounts often required (need phone # validation)
- Captchas can block automation (manual intervention)
- Content legality in different jurisdictions
- Maintenance heavy (platforms update frequent)

### 🧭 Fit / Maturity / Ops
- **Fit:** Data Analysts, OSINT researchers focused on China
- **Maturity:** active (very popular)
- **Latency/Cost:** slow (browser based)
- **Data constraints:** Platform terms of service
- **Ops friction:** high (cookie/account management)

### Full links
- Repo: https://github.com/NanmiCoder/MediaCrawler
- Original README: https://github.com/NanmiCoder/MediaCrawler/blob/main/README.md
- Stars: ~43,257
- Maturity: active

---

## anime.js

**TL;DR:** A lightweight JavaScript animation library with a simple, yet powerful API. It works with CSS properties, SVG, DOM attributes and JavaScript Objects. One of the most popular animation engines for the web. 66k stars.

### Быстрый выбор
- ✅ Используй если:
  - Creating complex choreographed animations
  - Need timeline control (pause, seek, reverse)
  - Animating SVG paths or morphing
  - Vanilla JS project (no React/framer-motion)
  - Performance is critical
- ❌ Не используй если:
  - Using React (Framer Motion is more idiomatic)
  - Only need simple CSS transitions
  - Heavy 3D requirements (Use Three.js/GSAP)
  - Project size constraints (it's small, but CSS is smaller)
  - Need physics-based springs (other libs do this better)

### 🚀 Запуск
```bash
npm install animejs
```
```javascript
import anime from 'animejs/lib/anime.es.js';

anime({
  targets: '.css-selector',
  translateX: 250,
  rotate: '1turn',
  duration: 800
});
```

### 🧩 Архитектура
- **Core:** Animation Engine (tick loop)
- **Targets:** CSS, DOM, JS Objects, SVG
- **Features:** Keyframes, Staggering, Timeline, Controls
- **Easing:** Built-in penner equations and custom bezier
- **Entrypoints:** `anime()` function

### 🧪 Примеры задач
- "Animate a logo drawing itself (SVG stroke)"
- "Create a complex staggered list entrance"
- "Morph between two shapes"
- "Control animation playback on scroll"
- "Animate numbers counting up"

### ⚠️ Ограничения
- DOM heavy (performance hit on many elements)
- Not designed for game loops
- V4 is in progress (V3 is stable but old)
- GSAP is more "industry standard" for high-end creative web
- React wrappers are often buggy

### 🧭 Fit / Maturity / Ops
- **Fit:** Frontend Devs, Creative Coders
- **Maturity:** stable (legacy)
- **Latency/Cost:** minimal size
- **Data constraints:** none
- **Ops friction:** low (npm install)

### Full links
- Repo: https://github.com/juliangarnier/anime
- Original README: https://github.com/juliangarnier/anime/blob/master/README.md
- Stars: 66,212
- Maturity: active

---

## nanobot

**TL;DR:** A tiny, highly capable tool for building MCP (Model Context Protocol) Agents. Simplifies the creation of agents that can consume MCP servers, making it easier to connect LLMs to local tools and data sources via the Anthropic standard. 700 stars.

### Быстрый выбор
- ✅ Используй если:
  - Experimenting with Model Context Protocol (MCP)
  - Building lightweight agents that need tool access
  - Want a simple CLI to run MCP-compatible agents
  - Connecting Claude/LLMs to local files/APIs via MCP
  - Rust based (performant)
- ❌ Не используй если:
  - Need a full orchestration framework (LangChain/CrewAI)
  - Python only environment (it's a binary/library)
  - Complex multi-agent collaboration required
  - Don't care about MCP standard

### 🚀 Запуск
```bash
# Install via cargo or download binary
cargo install nanobot
# Connect to an MCP server
nanobot run --server my-mcp-server
```

### 🧩 Архитектура
- **Protocol:** MCP (Model Context Protocol)
- **Language:** Rust
- **Components:** Client (Agent), Server connectors
- **LLM:** Integration with Anthropic/OpenAI APIs
- **Entrypoints:** CLI

### 🧪 Примеры задач
- "Run an agent that can read my local filesystem via MCP"
- "Connect an LLM to a Postgres database exposed as MCP"
- "Test a custom MCP server implementation"
- "Quickly prototyped a tool-using assistant"
- "Bridge CLI tools to LLM context"

### ⚠️ Ограничения
- Niche focus (MCP ecosystem)
- Very new technology (experimental)
- Limited documentation compared to major frameworks
- Requires understanding of MCP spec
- Smaller community

### 🧭 Fit / Maturity / Ops
- **Fit:** MCP early adopters, Rustaceans
- **Maturity:** emerging
- **Latency/Cost:** local execution
- **Data constraints:** none
- **Ops friction:** low (binary)

### Full links
- Repo: https://github.com/nanobot-ai/nanobot
- Stars: ~710
- Maturity: active

---

## agentic-cursorrules

**TL;DR:** A framework for managing multiple AI agents within the Cursor IDE using file-tree partitioning. Uses `.cursorrules` files placed in specific directories to define different "personas" or "agents" (e.g., Architect, QA, Frontend) that activate based on the file you are editing. 600 stars.

### Быстрый выбор
- ✅ Используй если:
  - Heavy user of Cursor IDE
  - Want specialized behavior for different parts of codebase
  - Need to enforce strict coding standards per-module
  - "Swarm" style development where one file = one agent role
  - Tired of generic system prompts
- ❌ Не используй если:
  - Not using Cursor
  - Prefer a global single instruction set
  - Find managing multiple dotfiles tedious
  - Codebase is small/monolithic
  - Want autonomous agents (this is assisted coding)

### 🚀 Запуск
```bash
# Copy the structure to your project
cp -r agentic-cursorrules/. .
# Edit .cursorrules files in subdirectories
# Open a file in 'frontend/' -> Cursor becomes Frontend Agent
```

### 🧩 Архитектура
- **Mechanism:** Cursor's hierarchical `.cursorrules` loading
- **Structure:** Folders for `architect`, `backend`, `frontend`, `qa`
- **Context:** Each folder has a specific system prompt
- **Flow:** User navigates folders to switch "agents"
- **Entrypoints:** `.cursorrules` files

### 🧪 Примеры задач
- "Have the 'Architect' agent review the high level design in /docs"
- "Switch to 'QA' agent in /tests to generate rigorous test cases"
- "Use 'Frontend' agent in /src/app to ensure Tailwind consistency"
- "Prevent backend logic from leaking into UI components"
- "Simulate a multi-person team review by switching files"

### ⚠️ Ограничения
- Manual context switching (must change file)
- Maintenance of many rule files
- Cursor specific feature
- Can be confusing if rules conflict (nested)
- Not "true" agents (just prompt switching)

### 🧭 Fit / Maturity / Ops
- **Fit:** Cursor Power Users, Solo Founders
- **Maturity:** specialized technique
- **Latency/Cost:** none
- **Data constraints:** none
- **Ops friction:** medium (setup)

### Full links
- Repo: https://github.com/s-smits/agentic-cursorrules
- Stars: ~641
- Maturity: active

---

## awesome-ai-memory

**TL;DR:** Curated list of AI memory projects — covers vector databases, memory frameworks, RAG implementations, conversation history management, and long-term agent memory solutions. Essential resource для anyone building AI systems that need to remember context. 600 stars — go-to reference for memory tech.

### Быстрый выбор
- ✅ Используй если:
  - Building AI with long-term memory
  - Evaluating vector database options
  - Implementing RAG pipelines
  - Research on AI memory architectures
  - Comparing memory frameworks
- ❌ Не используй если:
  - Need working code (это список, не library)
  - Looking for single specific tool
  - Already decided on memory solution
  - Non-technical overview needed
  - Production implementation guide

### 🧩 Содержимое списка
- **Vector Databases:** Pinecone, Weaviate, Chroma, Milvus, Qdrant
- **Memory Frameworks:** MemGPT, Mem0, Zep
- **RAG Tools:** LangChain retrievers, LlamaIndex
- **Conversation Memory:** buffer, summary, windowed strategies
- **Knowledge Graphs:** Neo4j, GraphRAG approaches
- **Research Papers:** academic memory papers
- **Ключевые секции:** organized by memory type

### 🧪 Примеры задач
- "Compare vector databases for my use case"
- "Find open-source alternatives to Pinecone"
- "Research long-term agent memory"
- "Discover RAG optimization techniques"
- "Evaluate memory solutions for chatbots"
- "Learn about episodic vs semantic memory"

### ⚠️ Ограничения
- List format only (no implementations)
- Rapidly evolving field (links may age)
- Quality of listed projects varies
- Requires technical knowledge
- No benchmarks or comparisons
- Community-maintained updates

### 🧭 Fit / Maturity / Ops
- **Fit:** AI engineers, researchers, architects
- **Maturity:** curated list (community-maintained)
- **Latency/Cost:** free to browse
- **Data constraints:** none (reference resource)
- **Ops friction:** zero (just read)

### Full links
- Repo: https://github.com/topoteretes/awesome-ai-memory
- Stars: 617
- Maturity: curated list

---

## ZerePy

**TL;DR:** An open-source framework specifically designed for building "Zere" (autonomous, social-media native) agents on Solana. Features built-in connectors for Twitter/X interactions and on-chain token management. 600 stars.

### Быстрый выбор
- ✅ Используй если:
  - Building a "Personality" agent for Crypto Twitter
  - Need Solana on-chain integration out of the box
  - Python ecosystem
  - Launching a meme-coin agent (like Truth Terminal clones)
  - Want a pre-configured social loop (Post -> Read Replies -> Post)
- ❌ Не используй если:
  - Enterprise business automation (features are social-focused)
  - EVM only (heavily Solana biased)
  - Complex RAG workflows (use LangChain)
  - Need strict deterministic behavior

### 🚀 Запуск
```bash
git clone https://github.com/blorm-network/ZerePy
cd ZerePy
pip install -r requirements.txt
# Configure configured_agents/my_agent.json
python main.py
```

### 🧩 Архитектура
- **Agent Loop:** Twitter scraping + LLM generation + Action execution
- **Integrations:** Twitter API (unofficial/official), Solana RPC
- **Memory:** Simple JSON/SQLite based short-term history
- **Persona:** Defined via JSON configuration
- **Entrypoints:** `main.py` CLI

### 🧪 Примеры задач
- "Create a bot that replies to every mention of $SOL with a bullish take"
- "Auto-swap token donations into the agent's treasury"
- "Generate unique 'thought' tweets every 2 hours"
- "Launch a token on pump.fun based on user engagement"
- "Monitor a specific wallet and tweet when it moves funds"

### ⚠️ Ограничения
- High risk of X suspension (aggressive automation)
- Codebase is relatively new and niche
- Focused on "Crypto Culture" agents
- Documentation is sparse
- Limited observability tools

### 🧭 Fit / Maturity / Ops
- **Fit:** DeFAI developers, Crypto Marketers
- **Maturity:** active (early stage)
- **Latency/Cost:** API polling costs
- **Data constraints:** Twitter data access
- **Ops friction:** medium (setup)

### Full links
- Repo: https://github.com/blorm-network/ZerePy
- Stars: ~587
- Maturity: active

---

## gensx

**TL;DR:** A TypeScript framework for building durable, composable AI agents using React-like patterns. Define your agent's behavior using TSX components (e.g., `<OpenAIModel>`, `<Tool>`), bringing the power of Component-Based Architecture to agent orchestration. 500 stars.

### Быстрый выбор
- ✅ Используй если:
  - You love React/JSX syntax
  - Building complex, hierarchical agent workflows
  - Typescript is your primary language
  - Need structured output validation (Zod integration)
  - Want composable "Agent Components"
- ❌ Не используй если:
  - Prefer Python (use LangChain/CrewAI)
  - Hate JSX for backend logic
  - Need a simple imperative script
  - Require a mature, battle-tested framework (still new)

### 🚀 Запуск
```bash
npm install @gensx/core
```
```tsx
import { GSX } from '@gensx/core';

const MyAgent = () => (
  <Agent provider="openai" model="gpt-4">
    <SystemPrompt>You are a helpful assistant.</SystemPrompt>
    <Tool name="search" handler={searchWeb} />
  </Agent>
);

const result = await GSX.execute(<MyAgent />);
```

### 🧩 Архитектура
- **Core:** JSX Runtime for Agents
- **Components:** `<Agent>`, `<Prompt>`, `<Tool>`, `<Workflow>`
- **State:** React-like hooks/context (future roadmap)
- **Output:** Structured JSON or Text stream
- **Entrypoints:** `GSX.execute()`

### 🧪 Примеры задач
- "Build a research agent composed of `<Researcher>` and `<Writer>` components"
- "Create a reusable `<Reviewer>` component that checks code quality"
- "Visualize agent logic as a component tree"
- "Mock specific sub-agents for unit testing"
- "Share agent logic as NPM packages"

### ⚠️ Ограничения
- Paradigm shift (using JSX for backend AI logic)
- Smaller ecosystem than LangChain
- Tooling support (VSCode) for JSX in backend files
- Performance overhead of virtual DOM-like structure
- Still in early beta

### 🧭 Fit / Maturity / Ops
- **Fit:** React Developers, AI Engineers
- **Maturity:** emerging
- **Latency/Cost:** minimal overhead
- **Data constraints:** none
- **Ops friction:** low (npm based)

### Full links
- Repo: https://github.com/gensx-inc/gensx
- Stars: ~526
- Maturity: active

---

## grok3-api

**TL;DR:** Unofficial reverse-engineered API wrapper for xAI's Grok 3 models. Allows developers to programmatically access Grok functionality (including "Grok 3 Deep") without an official enterprise endpoint, often by mimicking browser session headers. 500 stars.

### Быстрый выбор
- ✅ Используй если:
  - Want early access to Grok 3 features via code
  - Official API is waitlisted or too expensive
  - Scraping "Grok Analysis" of tweets
  - Building personal/research prototypes
  - Need access to Grok's specific real-time news capabilities
- ❌ Не используй если:
  - Building a stable production product (WILL break)
  - Account safety is priority (Login flagging risk)
  - Compliance/Legal requirements
  - High volume traffic needed

### 🚀 Запуск
```bash
git clone https://github.com/mem0ai/grok3-api
pip install -r requirements.txt
# Copy cookies from browser session on x.com
python example.py
```

### 🧩 Архитектура
- **Core:** Python HTTP requests wrapper
- **Auth:** Session Cookies / Bearer Tokens (Manual extraction)
- **Protocol:** Reverse engineered internal JSON endpoints
- **Features:** Text generation, Image analysis (if supported)
- **Entrypoints:** Client class

### 🧪 Примеры задач
- "Automate a 'Grok roasted this profile' bot"
- "Use Grok 3 to summarize real-time news events"
- "Compare Grok 3 logic vs GPT-4 on logic puzzles"
- "Extract 'Fun Mode' responses programmatically"
- "Bypass official rate limits (multiple accounts)"

### ⚠️ Ограничения
- Extremely brittle (breaks when X updates frontend)
- Violation of TOS
- No SLA or guarantees
- Often requires CAPTCHA solving
- xAI actively fights scrapers

### 🧭 Fit / Maturity / Ops
- **Fit:** Hackers, Researchers, Bot devs
- **Maturity:** volatile
- **Latency/Cost:** free (risk based)
- **Data constraints:** x.com account required
- **Ops friction:** high (maintenance)

### Full links
- Repo: https://github.com/mem0ai/grok3-api
- Stars: ~527
- Maturity: active

---

## awesome-windsurf

**TL;DR:** Curated resources for Windsurf code editor — plugins, configurations, tips, workflows, and community extensions. Windsurf is an AI-first IDE and this list helps you maximize its potential. Essential reference for Windsurf power users. 500 stars — one-stop resource for Windsurf ecosystem.

### Быстрый выбор
- ✅ Используй если:
  - Using Windsurf as main IDE
  - Finding Windsurf-specific plugins
  - Learning Windsurf best practices
  - Configuring Windsurf rules/prompts
  - Comparing Windsurf features
- ❌ Не используй если:
  - Using Cursor/VS Code (different ecosystem)
  - Not interested in AI IDEs
  - Looking for general dev tools
  - Need non-Windsurf content
  - Already Windsurf expert

### 🧩 Содержимое списка
- **Plugins:** Windsurf-compatible extensions
- **Configurations:** .windsurfrules examples
- **Workflows:** AI-assisted coding patterns
- **Tips:** productivity shortcuts, settings
- **Comparisons:** vs Cursor, vs VS Code
- **Community:** Discord, forums, tutorials
- **Ключевые секции:** organized by resource type

### 🧪 Примеры задач
- "Find best Windsurf rules for Python"
- "Configure Windsurf for React projects"
- "Discover Windsurf productivity tips"
- "Compare Windsurf vs Cursor features"
- "Learn Windsurf keyboard shortcuts"
- "Setup Windsurf for team use"

### ⚠️ Ограничения
- Windsurf-specific only
- Rapidly evolving (links may age)
- Quality varies by contribution
- Requires Windsurf installation
- Some resources may be outdated
- Community-maintained list

### 🧭 Fit / Maturity / Ops
- **Fit:** Windsurf users, AI IDE enthusiasts
- **Maturity:** curated list (community-maintained)
- **Latency/Cost:** free to browse
- **Data constraints:** none (reference resource)
- **Ops friction:** zero (just read)

### Full links
- Repo: https://github.com/ichoosetoaccept/awesome-windsurf
- Stars: 520
- Maturity: curated list

---

## CodeGuide-starter-lite

**TL;DR:** Lightweight starter template for CodeGuide projects — minimal setup for AI-assisted development workflow. Pre-configured structure with .cursorrules, documentation templates, and project organization. Perfect для быстрого старта with opinionated AI coding patterns. 500 stars — clean slate for AI-first projects.

### Быстрый выбор
- ✅ Используй если:
  - Starting new CodeGuide-style project
  - Need pre-configured .cursorrules
  - Want structured project template
  - Quick AI-assisted project setup
  - Learning CodeGuide methodology
- ❌ Не используй если:
  - Custom stack/structure preferred
  - Non-AI-assisted workflow
  - Enterprise project templates
  - Need heavy framework scaffolding
  - Already have established patterns

### 🚀 Запуск
```bash
# Clone template
git clone https://github.com/CodeGuide-dev/codeguide-starter-lite.git my-project
cd my-project

# Remove git history, start fresh
rm -rf .git && git init

# Customize and build
npm install  # if applicable
```

### 🧩 Архитектура
- **Structure:** Pre-organized folder layout
- **AI Config:** .cursorrules, prompts
- **Docs:** README templates, CONTRIBUTING guides
- **Patterns:** CodeGuide best practices
- **Ключевые файлы:** `.cursorrules`, `docs/`, `src/`

### 🧪 Примеры задач
- "Start new AI-assisted project quickly"
- "Use pre-configured cursorrules"
- "Follow CodeGuide documentation pattern"
- "Setup project with AI-first structure"
- "Bootstrap new SaaS project template"

### ⚠️ Ограничения
- Opinionated structure (may not fit all)
- Template generic (needs customization)
- CodeGuide-specific patterns
- Minimal compared to full frameworks
- Requires understanding of AI workflows
- Not for legacy project migration

### 🧭 Fit / Maturity / Ops
- **Fit:** AI-first developers, solo builders
- **Maturity:** stable template
- **Latency/Cost:** free (template)
- **Data constraints:** none
- **Ops friction:** minimal (clone and go)

### Full links
- Repo: https://github.com/CodeGuide-dev/codeguide-starter-lite
- Stars: 512
- Maturity: active

---

## openagi

**TL;DR:** Open-source framework for building AGI-inspired agents — "Paving the way for open agents and AGI for all." Framework for autonomous task execution, planning, and multi-agent collaboration. Research-oriented project exploring paths toward more general AI systems. 500 stars — experimental AGI exploration.

### Быстрый выбор
- ✅ Используй если:
  - Researching AGI architectures
  - Experimenting with autonomous agents
  - Academic/research projects
  - Exploring multi-agent collaboration
  - Learning advanced AI concepts
- ❌ Не используй если:
  - Production systems needed
  - Proven, battle-tested frameworks required
  - Simple chatbot use case
  - Commercial deployment
  - Stability is priority

### 🚀 Запуск
```bash
# Clone and install
git clone https://github.com/aiplanethub/openagi.git
cd openagi
pip install -r requirements.txt

# Run example agent
python examples/basic_agent.py
```

### 🧩 Архитектура
- **Core:** Python-based agent framework
- **Planning:** Task decomposition, goal-oriented planning
- **Memory:** Long-term and working memory
- **Tools:** External tool integration
- **Multi-agent:** Collaboration patterns
- **Ключевые файлы:** `openagi/` module, `examples/`

### 🧪 Примеры задач
- "Explore autonomous task planning"
- "Experiment with agent memory systems"
- "Research multi-agent architectures"
- "Build experimental autonomous workflows"
- "Study AGI design patterns"

### ⚠️ Ограничения
- Experimental/research code
- Not production-ready
- API may change frequently
- Documentation sparse
- Smaller community
- Performance not optimized

### 🧭 Fit / Maturity / Ops
- **Fit:** AI researchers, AGI enthusiasts
- **Maturity:** experimental (active research)
- **Latency/Cost:** depends on LLM backend
- **Data constraints:** LLM API required
- **Ops friction:** medium (research setup)

### Full links
- Repo: https://github.com/aiplanethub/openagi
- Stars: 505
- Maturity: active

---

## awesome-full-stack-machine-learning-courses

**TL;DR:** Curated collection of ML engineering courses from top universities — CalTech, Columbia, Berkeley, MIT, Stanford, CMU. Covers practical ML engineering: MLOps, deployment, data pipelines, production systems. Not just theory — focus on full-stack practical skills. 500 stars — gold standard для ML engineering education.

### Быстрый выбор
- ✅ Используй если:
  - Learning production ML engineering
  - Want university-quality free courses
  - Focus on MLOps, not just algorithms
  - Preparing for ML Engineer roles
  - Need structured learning path
- ❌ Не используй если:
  - Already senior ML engineer
  - Pure theory/research focus
  - Looking for quick tutorials
  - Need hands-on bootcamp format
  - Prefer video-only content

### 🧩 Содержимое списка
- **Stanford:** CS229, CS231n, practical courses
- **Berkeley:** Full Stack Deep Learning
- **MIT:** Applied ML courses
- **CMU:** ML engineering, systems courses
- **Columbia:** Applied ML, data engineering
- **CalTech:** ML foundations, applications
- **Ключевые секции:** organized by university

### 🧪 Примеры задач
- "Find best MLOps course for free"
- "Learn production ML deployment"
- "Study data pipeline engineering"
- "Prepare for ML engineer interviews"
- "Understand model serving at scale"
- "Learn feature engineering best practices"

### ⚠️ Ограничения
- Self-paced (requires discipline)
- Some courses may be archived
- Quality varies by year/version
- English-only content
- No certification/degree
- Time investment significant

### 🧭 Fit / Maturity / Ops
- **Fit:** ML engineers, data scientists, career changers
- **Maturity:** curated list (educational)
- **Latency/Cost:** free (most courses)
- **Data constraints:** none
- **Ops friction:** zero (learning resources)

### Full links
- Repo: https://github.com/leehanchung/awesome-full-stack-machine-learning-courses
- Stars: 505
- Maturity: educational

---

## Awesome-LLM-Resources-List

**TL;DR:** Curated collection of resources for applied AI engineering — covers LLM APIs, frameworks, tutorials, courses, tools, and best practices. Practical focus for developers building with LLMs. Regularly updated with latest tools and techniques. 500 stars — comprehensive reference для LLM developers.

### Быстрый выбор
- ✅ Используй если:
  - Building LLM applications
  - Finding LLM tools and frameworks
  - Learning LLM engineering practically
  - Researching LLM ecosystem
  - Discovering new LLM resources
- ❌ Не используй если:
  - Already expert (too basic)
  - Academic research focus
  - Single specific tool needed
  - Non-LLM AI projects
  - Looking for code implementations

### 🧩 Содержимое списка
- **APIs:** OpenAI, Anthropic, Google, open-source
- **Frameworks:** LangChain, LlamaIndex, Semantic Kernel
- **Tools:** prompting, RAG, fine-tuning
- **Tutorials:** practical guides, examples
- **Courses:** learning resources, bootcamps
- **Best Practices:** production patterns
- **Ключевые секции:** organized by category

### 🧪 Примеры задач
- "Find LLM framework comparison"
- "Learn RAG implementation patterns"
- "Discover fine-tuning resources"
- "Compare LLM API providers"
- "Find prompt engineering guides"
- "Learn LLM deployment best practices"

### ⚠️ Ограничения
- List format (no implementations)
- LLM field evolves rapidly
- Some links may become outdated
- Quality varies by resource
- Requires own evaluation
- English-focused content

### 🧭 Fit / Maturity / Ops
- **Fit:** LLM developers, AI engineers
- **Maturity:** curated list (community-maintained)
- **Latency/Cost:** free to browse
- **Data constraints:** none
- **Ops friction:** zero (reference resource)

### Full links
- Repo: https://github.com/ilsilfverskiold/Awesome-LLM-Resources-List
- Stars: 482
- Maturity: curated list

---

## pplx2api

**TL;DR:** An OpenAI-compatible API wrapper for Perplexity AI. Allows you to use Perplexity's research and search capabilities with any tool that supports the standard OpenAI endpoint format (like Cursor, Chatbox, or AutoGen). 500 stars.

### Быстрый выбор
- ✅ Используй если:
  - Want "Search enabled" responses in tools that don't support it
  - Have a Perplexity Pro subscription
  - Need drop-in replacement for `base_url`
  - Automating research workflows via API
  - Bypassing official API limits (middleware approach)
- ❌ Не используй если:
  - Official Perplexity API is sufficient
  - Need pure offline inference
  - Violating TOS is a concern (scraping)
  - Low latency required (adds double hop)

### 🚀 Запуск
```bash
docker run -d -p 8080:8080 yushangxiao/pplx2api
# Use http://localhost:8080/v1 as base_url
# Use any random string as api_key (or session token)
```

### 🧩 Архитектура
- **Core:** Go / Python proxy server
- **Protocol:** Server-Sent Events (SSE) translation
- **Input:** OpenAI format JSON
- **Output:** Perplexity web query -> Streaming response
- **Entrypoints:** `/v1/chat/completions`

### 🧪 Примеры задач
- "Configure Cursor to use Perplexity for codebase q&a"
- "Connect AutoGen agents to the internet via Perplexity"
- "Use LibreChat UI with Perplexity backend"
- "Scrape search results formatted as JSON"
- "Compare query answers between GPT-4 and Perplexity"

### ⚠️ Ограничения
- Reverse engineered (can break anytime)
- Session management (cookies expirations)
- CAPTCHA challenges possible
- Not all Perplexity models supported
- No official SLA

### 🧭 Fit / Maturity / Ops
- **Fit:** Hackers, Tool Integrators
- **Maturity:** volatile
- **Latency/Cost:** free (with subscription)
- **Data constraints:** none
- **Ops friction:** medium (docker)

### Full links
- Repo: https://github.com/yushangxiao/pplx2api
- Stars: ~483
- Maturity: active

---

## vision-agent (askui)

**TL;DR:** An AI Agent capable of controlling operating systems (Windows, macOS, Linux, Android) via visual understanding. Unlike selenium (DOM-based), it "sees" the screen and clicks utilizing coordinates/OCR, making it resilient to UI code changes. 500 stars.

### Быстрый выбор
- ✅ Используй если:
  - Automating legacy desktop applications (no API)
  - Testing mobile apps across real devices
  - Workflow involves visual elements (Canvas/Games)
  - Need "Human-like" interaction (mouse move, click)
  - RPA (Robotic Process Automation) use cases
- ❌ Не используй если:
  - Web-only automation where speed matters (use Playwright)
  - Headless environment (needs a display server)
  - Extremely sensitive data (screen recording involved)
  - 100% precision required (OCR/Vision can fail)

### 🚀 Запуск
```bash
pip install vision-agent
# Requires connecting to a display (X11 / Wayland / Win32)
```

### 🧩 Архитектура
- **Core:** VLM (Vision Language Model) based controller
- **Input:** Screenshots stream
- **Output:** Mouse/Keyboard events
- **Backend:** AskUI Inference API (or local models)
- **Entrypoints:** Python SDK

### 🧪 Примеры задач
- "Open Excel, fill cell A1 with 'Data', save as PDF"
- "Login to the Citrix remote desktop and restart the server"
- "Play a level of Candy Crush on an Android emulator"
- "Test a Unity-based game UI"
- "Automate MFA entry from a separate authenticator app window"

### ⚠️ Ограничения
- Slower than DOM-based automation
- Can be flaky with dynamic UI animations
- Often requires an API key for the VLM backend
- Screen resolution sensitive
- Setup on headless linux servers is complex (Xvfb)

### 🧭 Fit / Maturity / Ops
- **Fit:** QA Engineers, RPA Developers
- **Maturity:** active
- **Latency/Cost:** high (image processing)
- **Data constraints:** screenshots sent to API
- **Ops friction:** high (display setup)

### Full links
- Repo: https://github.com/askui/vision-agent
- Stars: ~488
- Maturity: active

---

## AttackMachine

**TL;DR:** All-in-One automation software for multi-chain airdrop farming. Supports interaction with LayerZero, Wormhole, zkSync, Starknet, Scroll, Base, and Linea. Automates bridging, swapping, and NFT minting workflows for Sybil operations. 400 stars.

### Быстрый выбор
- ✅ Используй если:
  - Managing large scale farm (hundreds of wallets)
  - Need automated volume generation across L2s
  - Want randomization to avoid Sybil clustering (time/value)
  - Need CEX withdrawal/deposit modules (Binance/OKX)
  - Python-based script runner
- ❌ Не используй если:
  - "White hat" strict compliance
  - Only managing 1-2 main wallets (use manual UI)
  - Scared of private key exposure (audit code first)
  - Need a simple one-off bridge

### 🚀 Запуск
```bash
git clone https://github.com/realaskaer/AttackMachine
# Edit settings.py with RPCs and Private Keys
# Configure modules (swap, bridge, dmail)
python main.py
```

### 🧩 Архитектура
- **Core:** Web3.py wrapper
- **Modules:** Individual folders for each protocol (e.g. `modules/zksync.py`)
- **Config:** Excel/CSV handling for wallet lists
- **Utils:** Gas checker, Proxy manager, Sleep randomizer
- **Entrypoints:** `main.py` console menu

### 🧪 Примеры задач
- "Bridge ETH from Arbitrum to Base using Stargate"
- "Swap USDC -> ETH on SyncSwap (zkSync)"
- "Mint daily NFT on Zora for 50 wallets"
- "Refuel gas from OKX -> 100 EVM addresses"
- "Send Dmail messages to generate tx count"

### ⚠️ Ограничения
- High risk (Sybil detection algorithms are getting better)
- Keys stored in plain text/files
- Maintenance heavy (contracts change)
- Ethical considerations (network spam)
- Closed source components (sometimes linked)

### 🧭 Fit / Maturity / Ops
- **Fit:** Airdrop Farmers, Script Kiddies
- **Maturity:** active (arms race)
- **Latency/Cost:** gas fees
- **Data constraints:** blockchain state
- **Ops friction:** high (funding wallets)

### Full links
- Repo: https://github.com/realaskaer/AttackMachine
- Stars: ~409
- Maturity: active

---

## gemini-browser (browserbase)

**TL;DR:** A starter kit demonstrating "Computer Use" with Google's Gemini 2.0 Flash model running on Browserbase. Enables Gemini to control a headless browser, navigate websites, click elements, and extract data using natural language instructions. 300 stars.

### Быстрый выбор
- ✅ Используй если:
  - Experimenting with Gemini 2.0 "Computer Use" capabilities
  - Need a cloud-hosted browser environment (Browserbase)
  - Building AI agents that need to browse the web
  - Comparing Gemini vs Claude 3.5 Computer Use
  - Node.js/TypeScript stack
- ❌ Не используй если:
  - Local browser automation only (requires Browserbase API)
  - Production scraping at scale (expensive agents)
  - Need simple deterministic selectors (use Playwright)
  - Offline usage

### 🚀 Запуск
```bash
git clone https://github.com/browserbase/gemini-browser
npm install
# Set BROWSERBASE_API_KEY and GOOGLE_API_KEY
npm start
```

### 🧩 Архитектура
- **Agent:** LangChain / custom loop
- **Model:** Gemini 2.0 Flash (Multimodal)
- **Environment:** Browserbase (Cloud Headless Chrome)
- **Protocol:** CDP (Chrome DevTools Protocol) + Screen capture
- **Entrypoints:** `index.ts`

### 🧪 Примеры задач
- "Go to Amazon, search for 'headphones', and list the top 3 prices"
- "Login to Airbnb and find a house in Tokyo"
- "Navigate a complex SPA and take a screenshot of the dashboard"
- "Fill out a form across multiple pages"
- "Debug why a website is rendering incorrectly via AI"

### ⚠️ Ограничения
- Gemini 2.0 is still in preview/beta
- Latency of taking screenshots + uploading to LLM
- Browserbase cost (cloud service)
- Reliability of vision-based clicking
- Context window limits with many screenshots

### 🧭 Fit / Maturity / Ops
- **Fit:** AI Engineers, Browserbase customers
- **Maturity:** demo / starter
- **Latency/Cost:** medium
- **Data constraints:** screenshots
- **Ops friction:** low (cloud managed)

### Full links
- Repo: https://github.com/browserbase/gemini-browser
- Stars: ~314
- Maturity: active

---

## FreeDatabreaches

**TL;DR:** Download Free Databreaches. 300 stars.

### Full links
- Repo: https://github.com/doormanBreach/FreeDatabreaches
- Stars: 288
- Maturity: active

---

## astra (Shreyas-29)

**TL;DR:** A modern, high-performance landing page template designed for AI SaaS products. Built with Next.js, Tailwind CSS, and Framer Motion. Features a dark-themed, futuristic aesthetic typical of current AI tools (e.g. Linear-style). 300 stars.

### Быстрый выбор
- ✅ Используй если:
  - Launching an AI Wrapper/SaaS
  - Need a "Premium" look out of the box
  - React/Next.js stack
  - Want smooth scrolling and entry animations
  - Saving time on frontend design
- ❌ Не используй если:
  - Building a dashboard (this is a landing page)
  - Need Wordpress/No-code (requires coding)
  - Corporate/Enterprise aesthetic (this is startup-y)
  - Vue/Angular stack

### 🚀 Запуск
```bash
git clone https://github.com/Shreyas-29/astra
npm install
npm run dev
# Customize text in /components
```

### 🧩 Архитектура
- **Framework:** Next.js 14 (App Router)
- **Styling:** Tailwind CSS
- **Animation:** Framer Motion
- **Components:** Hero, Features, Pricing, Testimonials
- **Entrypoints:** `page.tsx`

### 🧪 Примеры задач
- "Deploy a landing page for my new 'Chat with PDF' tool"
- "Showcase updated pricing tiers for the SaaS"
- "Add a waiting list form to the hero section"
- "Customize the gradient colors to match brand"
- "Optimize SEO meta tags for launch"

### ⚠️ Ограничения
- It's a template (code ownership is shared)
- Design might look "generic AI startup"
- Requires React knowledge to customize logic
- Not a full backend application
- Optimization needed for image assets

### 🧭 Fit / Maturity / Ops
- **Fit:** Solo Founders, Indie Hackers
- **Maturity:** stable template
- **Latency/Cost:** static hosting (Vercel)
- **Data constraints:** none
- **Ops friction:** low

### Full links
- Repo: https://github.com/Shreyas-29/astra
- Stars: ~268
- Maturity: active

---

## luro-ai

**TL;DR:** Modern UI website template for next-generation SaaS products — sleek design, dark mode, responsive layouts, and AI-themed aesthetics. Built with Next.js и Tailwind CSS. Ready-to-use landing page template для AI/SaaS startups. 300 stars — premium looking template для quick launch.

### Быстрый выбор
- ✅ Используй если:
  - Building AI SaaS landing page
  - Need modern, polished template
  - Quick launch priority
  - Next.js + Tailwind stack
  - Dark mode aesthetic wanted
- ❌ Не используй если:
  - Custom branding from scratch
  - Non-Next.js tech stack
  - Complex app (not just landing)
  - Need unique design identity
  - Light mode is priority

### 🚀 Запуск
```bash
git clone https://github.com/Shreyas-29/luro-ai.git
cd luro-ai
npm install && npm run dev
# Open http://localhost:3000
```

### 🧩 Архитектура
- **Framework:** Next.js 14 (App Router)
- **Styling:** Tailwind CSS
- **Animations:** Framer Motion
- **Components:** Reusable UI components
- **Ключевые файлы:** `app/`, `components/`

### 🧪 Примеры задач
- "Launch AI product landing page quickly"
- "Customize with your branding"
- "Add signup/waitlist form"
- "Deploy to Vercel in minutes"
- "Use as design reference"

### ⚠️ Ограничения
- Template only (no backend logic)
- Generic layout (need customization)
- May look similar to other users
- Limited unique components
- Requires Tailwind knowledge
- No CMS integration

### 🧭 Fit / Maturity / Ops
- **Fit:** indie hackers, AI startups, solo founders
- **Maturity:** stable template
- **Latency/Cost:** free (Vercel hosting)
- **Data constraints:** none (static site)
- **Ops friction:** minimal

### Full links
- Repo: https://github.com/Shreyas-29/luro-ai
- Stars: 273
- Maturity: active

---

## agentipy

**TL;DR:** A Python toolkit for enabling AI Agents to interact with the Solana blockchain. Acts as a bridge between LLMs (using LangChain or custom logic) and Solana protocols (Jupiter, Pump.fun, Raydium), allowing agents to trade, launch tokens, and manage assets. 300 stars.

### Быстрый выбор
- ✅ Используй если:
  - Building Python-based AI Agents (e.g. widely used with Smolagents/LangChain)
  - Need specific tooling for Solana DeFi
  - Launching meme coins programmatically
  - Checking wallet balances/token stats via AI
  - Prefer simple higher-level abstractions over raw web3.py
- ❌ Не используй если:
  - Need low-level transaction optimization
  - Building a high-frequency arb bot (too slow)
  - JavaScript/TypeScript environment (use solana-agent-kit)
  - Enterprise grade security required

### 🚀 Запуск
```bash
pip install agentipy
```
```python
from agentipy.agent import SolanaAgent
from agentipy.tools import CreateTokenTool

agent = SolanaAgent(private_key="...", rpc_url="...")
# Agent can now use tools to interact
agent.execute(CreateTokenTool(name="MyAI", symbol="AI"))
```

### 🧩 Архитектура
- **Core:** Python wrapper for `solders` and `solana-py`
- **Tools:** Pre-built actions (Swap, Transfer, Deploy)
- **Integration:** Compatible with LangChain `Tool` interface
- **Protocols:** Jupiter (swap), Pump (launch)
- **Entrypoints:** `SolanaAgent` class

### 🧪 Примеры задач
- "Check the price of SOL and swap 1 USDC if < $150"
- "Launch a token named 'AgentCoin' on pump.fun"
- "Fetch the top holders of a specific SPL token"
- "Airdrop 0.1 SOL to a list of winners"
- "Monitor wallet for incoming transactions"

### ⚠️ Ограничения
- Beta software (APIs might change)
- Dependent on RPC node performance
- Risk of losing funds if keys are mishandled by LLM
- Limited protocol coverage compared to JS SDKs
- Documentation is still growing

### 🧭 Fit / Maturity / Ops
- **Fit:** Python DeFAI Developers
- **Maturity:** active (early)
- **Latency/Cost:** Solana fees
- **Data constraints:** on-chain data
- **Ops friction:** low

### Full links
- Repo: https://github.com/niceberginc/agentipy
- Original README: https://github.com/niceberginc/agentipy/blob/main/README.md
- Stars: ~261
- Maturity: active

---

## antd-multipurpose-dashboard

**TL;DR:** Free Vite + TypeScript admin dashboard theme using Ant Design 5 — multipurpose template with charts, tables, forms, and data visualization. Clean, professional design с responsive layouts. Perfect для internal tools и admin panels. 250 stars — solid Ant Design dashboard starter.

### Быстрый выбор
- ✅ Используй если:
  - Building admin panel with Ant Design
  - Vite + TypeScript stack
  - Need charts and data tables
  - Enterprise-style dashboard
  - React-based project
- ❌ Не используй если:
  - Tailwind CSS preference
  - Non-React stack (Vue/Svelte)
  - Minimal/lightweight needed
  - Custom design system
  - Shadcn/Radix preferred

### 🚀 Запуск
```bash
git clone https://github.com/design-sparx/antd-multipurpose-dashboard.git
cd antd-multipurpose-dashboard
npm install && npm run dev
# Open http://localhost:5173
```

### 🧩 Архитектура
- **Framework:** React 18 + Vite
- **UI Library:** Ant Design 5
- **Language:** TypeScript
- **Charts:** Ant Design Charts
- **Ключевые файлы:** `src/pages/`, `src/components/`

### 🧪 Примеры задач
- "Build internal admin dashboard"
- "Add user management pages"
- "Create data visualization panels"
- "Implement CRUD operations UI"
- "Deploy as internal tool"

### ⚠️ Ограничения
- Ant Design ecosystem lock-in
- Bundle size larger than minimal libs
- May need AntD customization knowledge
- Template needs content adaptation
- Some components may be opinionated
- Chinese-heavy community docs

### 🧭 Fit / Maturity / Ops
- **Fit:** enterprise devs, internal tools builders
- **Maturity:** stable template
- **Latency/Cost:** free (self-hosted)
- **Data constraints:** none (frontend only)
- **Ops friction:** low (npm standard)

### Full links
- Repo: https://github.com/design-sparx/antd-multipurpose-dashboard
- Stars: 251
- Maturity: active

---

## linkify (Shreyas-29)

**TL;DR:** Modern UI website template for SaaS products — link-in-bio style landing page with clean aesthetics. Built with Next.js и Tailwind CSS, includes animations and responsive design. Perfect для quick launches и personal branding. 250 stars — polished SaaS template.

### Быстрый выбор
- ✅ Используй если:
  - SaaS landing page needed
  - Modern template wanted
  - Next.js + Tailwind stack
  - Quick launch priority
  - Personal brand/portfolio
- ❌ Не используй если:
  - Custom design required
  - Non-Next.js framework
  - Complex multi-page app
  - Enterprise features needed
  - Unique visual identity

### 🚀 Запуск
```bash
git clone https://github.com/Shreyas-29/linkify.git
cd linkify
npm install && npm run dev
# Open http://localhost:3000
```

### 🧩 Архитектура
- **Framework:** Next.js (App Router)
- **Styling:** Tailwind CSS
- **Animations:** CSS / Framer Motion
- **Layout:** Responsive, mobile-first
- **Ключевые файлы:** `app/`, `components/`

### 🧪 Примеры задач
- "Launch SaaS product landing"
- "Create personal link page"
- "Customize with own branding"
- "Add waitlist form"
- "Deploy to Vercel quickly"

### ⚠️ Ограничения
- Template only (frontend)
- Generic design (needs customization)
- May look similar to others using it
- No backend/CMS included
- Limited unique features
- Requires Tailwind familiarity

### 🧭 Fit / Maturity / Ops
- **Fit:** solo founders, indie hackers
- **Maturity:** stable template
- **Latency/Cost:** free (static hosting)
- **Data constraints:** none
- **Ops friction:** minimal

### Full links
- Repo: https://github.com/Shreyas-29/linkify
- Stars: 238
- Maturity: active

---

## mcp-server-gemini

**TL;DR:** An implementation of the Model Context Protocol (MCP) using Google's Gemini models. Allows MCP-compliant clients (like Claude Desktop or custom tools) to utilize Gemini Pro/Flash as the backend intelligence provider. 250 stars.

### Быстрый выбор
- ✅ Используй если:
  - Using MCP Ecosystem (Claude Desktop, etc.)
  - Prefer Google's Gemini models (Long Context, Multimodal)
  - Want a cheaper alternative to Anthropic's models for MCP tasks
  - Testing model interoperability
  - building a local "Gemini Assistant"
- ❌ Не используй if:
  - No MCP client available
  - Need Function calling specifically optimized for GPT-4 (Gemini is good but different)
  - Strictly proprietary environment (Google API data usage)

### 🚀 Запуск
```bash
npm install -g mcp-server-gemini
# Set GOOGLE_API_KEY
mcp-server-gemini
```
*Add to Claude Desktop config:*
```json
"gemini": {
  "command": "mcp-server-gemini",
  "env": { "GOOGLE_API_KEY": "..." }
}
```

### 🧩 Архитектура
- **Protocol:** MCP (JSON-RPC)
- **Backend:** Google Generative AI SDK
- **Runtime:** Node.js
- **Capabilities:** Prompts, Resources (planned), Tools
- **Entrypoints:** CLI executable

### 🧪 Примеры задач
- "Use Gemini 1.5 Pro to analyze a large PDF locally via Claude Desktop"
- "Switch to Gemini Flash for faster, cheaper tool execution"
- "Compare tool use accuracy between Sonnet 3.5 and Gemini Pro 1.5"
- "Build a custom MCP dashboard using Gemini as the router"

### ⚠️ Ограничения
- MCP is relatively new
- Gemini's tool calling formats can sometimes differ from expected Schema
- Requires Node.js environment
- CLI primarily designed for local use (stdio)

### 🧭 Fit / Maturity / Ops
- **Fit:** MCP Early Adopters
- **Maturity:** active
- **Latency/Cost:** highly efficient (Flash)
- **Data constraints:** Google API
- **Ops friction:** low

### Full links
- Repo: https://github.com/aliargun/mcp-server-gemini
- Stars: ~244
- Maturity: active

---

## deprecated-generative-ai-python

**TL;DR:** Deprecated Google GenAI Python SDK. 2k stars.

### Full links
- Repo: https://github.com/google-gemini/deprecated-generative-ai-python
- Stars: 2,261
- Maturity: deprecated

---

## CloudFreed-CloudFlare-solver-bypass

**TL;DR:** CloudFlare solver/bypass. 200 stars.

### Full links
- Repo: https://github.com/akmal-abar/CloudFreed-CloudFlare-solver-bypass
- Stars: 160
- Maturity: active

---

## dreamsxin/example

**TL;DR:** Various code examples. 200 stars.

### Full links
- Repo: https://github.com/dreamsxin/example
- Stars: 190
- Maturity: active

---

## vetra

**TL;DR:** Modern AI marketing automation platform landing page. 150 stars.

### Full links
- Repo: https://github.com/Shreyas-29/vetra
- Stars: 149
- Maturity: active

---

## Trading-API (Pump.fun)

**TL;DR:** An unofficial API for programmatically trading specifically on Pump.fun (Solana's viral memecoin launcher). Allows developers to buy, sell, and snipe new launches using Python without manually interacting with the UI. 150 stars.

### Быстрый выбор
- ✅ Используй если:
  - Building a sniper bot for Pump.fun
  - Need programmatic buy/sell execution
  - Automating "bonding curve" strategy
  - Python ecosystem
  - Don't want to decipher the frontend obfuscated API calls manually
- ❌ Не используй если:
  - Raydium/Jupiter trading (this is specific to Pump.fun)
  - Need official supported API (this is a wrapper/scraper)
  - High frequency latency (use Rust/Geyser for that)
  - Risk averse (unofficial APIs can result in bans or front-running)

### 🚀 Запуск
```bash
git clone https://github.com/thetateman/Trading-API
cd Trading-API
# Configure keys in .env
python main.py
```

### 🧩 Архитектура
- **Core:** Python requests / WebSocket
- **Auth:** Private Key signing (locally)
- **Protocol:** Pump.fun internal API + Solana RPC
- **Features:** Buy, Sell, Listen for new coins
- **Entrypoints:** `trade.py`

### 🧪 Примеры задач
- "Snipe a token the second it appears on the 'new' feed"
- "Auto-sell when bonding curve hits 90%"
- "Mirror trade a successful wallet on Pump.fun"
- "Monitor a coin for 'Head and Shoulders' pattern"
- "Batch buy small amounts of 10 different coins"

### ⚠️ Ограничения
- Niche scope (Pump.fun only)
- High slippage risk on volatile/low liquidity coins
- No official documentation from Pump.fun side
- Rate limits on the internal API
- Security of keeping private keys in script

### 🧭 Fit / Maturity / Ops
- **Fit:** Meme coin traders, Bot developers
- **Maturity:** active (volatile)
- **Latency/Cost:** Solana gas + priority fees
- **Data constraints:** Pump.fun data
- **Ops friction:** medium

### Full links
- Repo: https://github.com/thetateman/Trading-API
- Stars: ~147
- Maturity: active

---

## geyser-grpc-plugin (Jito)

**TL;DR:** A highly performant plugin for Solana Validator nodes that streams account and slot updates via gRPC. Essential for maximal extractable value (MEV) searchers, high-frequency trading bots, and indexers needing lower latency than standard RPC. 130 stars.

### Быстрый выбор
- ✅ Используй если:
  - Running your own Solana RPC/Validator node
  - Need millisecond-latency access to mempool/state
  - Building an MEV bot or Arbitrage engine
  - Standard JSON-RPC polling is too slow
  - Ingesting massive amounts of on-chain data
- ❌ Не используй если:
  - Building a simple DApp (just use Helius/Tatum/QuickNode)
  - Don't have infrastructure to run a validator
  - JavaScript/Frontend only developer
  - Don't know what Protobuf is

### 🚀 Запуск
```bash
# Must be compiled with Rust and loaded into a Solana Validator
cargo build --release
# Add to validator startup flags:
# --geyser-plugin-config config.json
```

### 🧩 Архитектура
- **Core:** Rust Dynamic Library (.so/.dylib)
- **Protocol:** gRPC (HTTP/2) with Protobuf
- **Integration:** Hooks directly into Solana Validator Runtime
- **Output:** Streams of Account, Slot, Transaction, and Block updates
- **Entrypoints:** `lib.rs` (plugin entry)

### 🧪 Примеры задач
- "Stream all price updates for SOL/USDC on Raydium in real-time"
- "Detect large wallet movements before they are finalized"
- "Feed account states into a PostgreSQL database instantly"
- "Monitor specific program IDs for instruction execution"
- "Build a custom block explorer backend"

### ⚠️ Ограничения
- High infrastructure cost (Solana node hardware is expensive)
- Complex compilation and deployment
- Very technical (requires Rust/System expertise)
- Network bandwidth intensive

### 🧭 Fit / Maturity / Ops
- **Fit:** MEV Searchers, Infrastructure Providers
- **Maturity:** production (used by Jito)
- **Latency/Cost:** Ultra-low latency / High hardware cost
- **Data constraints:** Streaming only
- **Ops friction:** very high

### Full links
- Repo: https://github.com/jito-foundation/geyser-grpc-plugin
- Stars: ~134
- Maturity: active

---

## linkedin-bot

**TL;DR:** Automate LinkedIn Outreach with Selenium. 100 stars.

### Full links
- Repo: https://github.com/FujiwaraChoki/linkedin-bot
- Stars: 93
- Maturity: active

---

## solana-winternitz-vault

**TL;DR:** Solana Winternitz quantum-resistant lamports vault. 93 stars.

### Быстрый выбор
- ✅ Используй если:
  - Quantum-resistant security
  - Solana vault
  - Future-proof crypto
- ❌ Не используй если:
  - Standard security ok
  - Non-Solana

### Full links
- Repo: https://github.com/blueshift-gg/solana-winternitz-vault
- Stars: 93
- Maturity: active

---

## ezlocalai

**TL;DR:** An easy-to-setup local AI server that exposes an OpenAI-compatible API. Supports LLMs (Llama, Mistral), Vision, Speech-to-Text (Whisper), and Text-to-Speech, aiming to be a "one-click" replacement for cloud providers. 90 stars.

### Быстрый выбор
- ✅ Используй если:
  - Want a local "Drop-in" replacement for OpenAI API
  - Need Multimodal capabilities (Vision + Voice) locally
  - Running on consumer hardware (NVIDIA GPU supported)
  - Privacy is paramount (no data leaves usage)
  - Simplification of llama.cpp / torch setup
- ❌ Не используй если:
  - Need distributed enterprise inference (vLLM is better)
  - Cloud API reliability/speed is preferred
  - No GPU available (CPU is slow)

### 🚀 Запуск
```bash
pip install ezlocalai
# Configure .env with model selection
ezlocalai serve
# API is now at http://localhost:8091/v1/
```

### 🧩 Архитектура
- **Core:** Python (FastAPI)
- **Engine:** llama.cpp-python, HuggingFace
- **Features:** RAG (built-in), Function Calling, TTS/STT
- **Interface:** OpenAI JSON schema
- **Entrypoints:** `ezlocalai` CLI

### 🧪 Примеры задач
- "Run a local Chatbot UI pointing to `localhost:8091`"
- "Transcribe meeting audio files using local Whisper"
- "Process sensitive medical documents via RAG locally"
- "Generate voice responses for a home assistant"
- "Test a script designed for GPT-4 on a local Llama-3 model"

### ⚠️ Ограничения
- Performance depends heavily on hardware (VRAM)
- Setup can be tricky with CUDA drivers
- Not as optimized for high throughput as dedicated engines (vLLM/TGI)
- Model downloading can be slow

### 🧭 Fit / Maturity / Ops
- **Fit:** Local AI enthusiasts, Privacy advocates
- **Maturity:** active
- **Latency/Cost:** Free (hardware cost)
- **Data constraints:** Local only
- **Ops friction:** medium (drivers)

### Full links
- Repo: https://github.com/DevXT-LLC/ezlocalai
- Stars: ~91
- Maturity: active

---

## Threads-Scraper

**TL;DR:** Python scraper для Meta Threads. Автоматизирует извлечение постов, профилей, комментариев с публичных страниц Threads. Использует client-side rendering ожидание для SPA. Локальный scraper без API — работает напрямую с веб-интерфейсом. Альтернатива Apify Threads pipelines.

### Быстрый выбор
- ✅ Используй если:
  - Нужен data extraction из Meta Threads
  - Массовый сбор публичных постов/профилей
  - Нет доступа к official Threads API
  - Локальный scraping без cloud dependencies
  - Python stack preferred
- ❌ Не используй если:
  - Нужен real-time streaming (scraping медленный)
  - Threads блокирует твой IP (нужны proxies)
  - Нарушение ToS критично для проекта
  - Хочешь managed solution (используй Apify)

### 🚀 Запуск
```bash
git clone https://github.com/Zeeshanahmad4/Threads-Scraper
cd Threads-Scraper
pip install -r requirements.txt
python scraper.py --username target_user
```

### 🧩 Архитектура
- **Language:** Python 3.8+
- **Browser:** Selenium/Playwright для JS rendering
- **Output:** JSON/CSV export
- **Features:** profile scraping, post extraction, comments
- **Entrypoints:** `scraper.py` CLI

### 🧪 Примеры задач
- Извлечение всех постов пользователя
- Мониторинг конкурентов на Threads
- Анализ engagement metrics
- Сбор данных для исследований
- Архивирование публичного контента

### ⚠️ Ограничения
- Может сломаться при изменениях UI Threads
- Rate limiting от Meta
- Требует browser automation (heavy)
- Нет official API support
- ToS violation risk

### 🧭 Fit / Maturity / Ops
- **Fit:** Social media researchers, OSINT, marketers
- **Maturity:** experimental
- **Latency/Cost:** slow (browser rendering), free
- **Data constraints:** public profiles only
- **Ops friction:** medium (browser setup)

### Full links
- Repo: https://github.com/Zeeshanahmad4/Threads-Scraper
- Stars: 80
- Maturity: active

---

## Gradient-Network-Bot

**TL;DR:** Automation tool для Gradient Network airdrop farming. Автоматическая регистрация аккаунтов, farming operations, proxy auto-swap, captcha solving. Управление сотнями wallets с CSV export статистики. Anti-detection measures и secure account storage. Python-based скрипт для массового фарминга.

### Быстрый выбор
- ✅ Используй если:
  - Фарминг Gradient Network airdrop
  - Управление множеством аккаунтов
  - Нужна автоматизация registration + farming
  - Есть proxy pool для rotation
  - Python automation experience
- ❌ Не используй если:
  - Один основной аккаунт (используй UI)
  - Compliance/legal concerns (Sybil farming)
  - Нет прокси (будет ban)
  - Нет опыта с private key management

### 🚀 Запуск
```bash
git clone https://github.com/Jaammerr/Gradient-Network-Bot
cd Gradient-Network-Bot
pip install -r requirements.txt
# Configure settings with proxies and accounts
python main.py
```

### 🧩 Архитектура
- **Language:** Python 3.9+
- **Features:** auto-registration, farming, proxy swap, captcha
- **Storage:** secure account storage, CSV export
- **Logging:** comprehensive operation logs
- **Entrypoints:** `main.py` console interface

### 🧪 Примеры задач
- Автоматическая регистрация 100+ аккаунтов
- Daily farming operations на всех аккаунтах
- Export статистики для tracking
- Re-verification failed accounts
- Invite code binding automation

### ⚠️ Ограничения
- Sybil detection risk (аккаунты могут банить)
- Требует proxy pool (costs money)
- Private keys в config files (security risk)
- Maintenance при изменениях на платформе
- Ethical considerations

### 🧭 Fit / Maturity / Ops
- **Fit:** Airdrop farmers, automation enthusiasts
- **Maturity:** active
- **Latency/Cost:** proxy costs + time
- **Data constraints:** accounts, proxies
- **Ops friction:** high (setup, maintenance)

### Full links
- Repo: https://github.com/Jaammerr/Gradient-Network-Bot
- Stars: 72
- Maturity: active

---

## Peargent

**TL;DR:** Lightweight Python framework для создания AI agents. Multi-LLM support (OpenAI, Anthropic, Groq, Gemini). Advanced tracing и cost tracking. Pydantic-powered type-safe tools. Agent pools для concurrent execution. Streaming responses с event handling. Простая альтернатива тяжёлым frameworks.

### Быстрый выбор
- ✅ Используй если:
  - Нужен легковесный agent framework
  - Multi-LLM switching (OpenAI ↔ Claude ↔ Groq)
  - Type-safe tools с Pydantic validation
  - Cost tracking across providers
  - Python-first approach
- ❌ Не используй если:
  - Enterprise features нужны (используй LangChain)
  - Visual workflow builder (используй Dify)
  - Production battle-tested (молодой проект)
  - Non-Python stack

### 🚀 Запуск
```bash
pip install peargent
```
```python
from peargent import create_agent
from peargent.models import anthropic, openai, groq

agent = create_agent(
    name="assistant",
    persona="You are a helpful AI assistant.",
    model=anthropic("claude-3-5-sonnet-20241022")
    # or groq("llama-3.3-70b-versatile"), openai("gpt-4o")
)
result = agent.run("What is the capital of France?")
print(result)
```

### 🧩 Архитектура
- **Language:** Python 3.9+
- **LLMs:** OpenAI, Anthropic, Groq, Gemini, и др.
- **Tools:** Pydantic-based с auto-validation
- **Features:** tracing, history management, streaming, cost tracking
- **Entrypoints:** `peargent` module

### 🧪 Примеры задач
- Создание conversational assistants
- Multi-agent pools для parallel tasks
- Cost optimization через LLM switching
- Tool-augmented agents
- Streaming chat interfaces

### ⚠️ Ограничения
- Молодой проект (70 stars)
- Меньше community support чем LangChain
- Documentation развивается
- Fewer integrations
- Production readiness unknown

### 🧭 Fit / Maturity / Ops
- **Fit:** Lightweight agents, multi-LLM, prototyping
- **Maturity:** emerging
- **Latency/Cost:** depends on LLM provider
- **Data constraints:** API keys
- **Ops friction:** low (pip install)

### Full links
- Repo: https://github.com/Peargent/peargent
- Docs: https://peargent.online
- Discord: https://discord.gg/jtNvmjMAYu
- Stars: 70
- Maturity: active

---

## deep-research-mcp-server

**TL;DR:** An MCP server dedicated to "Deep Research" workflows. Instead of simple search, it mimics the behavior of recursive research agents (like OpenAI's Deep Research) by using Gemini to iteratively search, analyze, and refine queries to produce comprehensive reports. 60 stars.

### Быстрый выбор
- ✅ Используй если:
  - Need "Agentic Search" inside Claude Desktop
  - Performing in-depth implementation planning or market research
  - Simple Perplexity plugin isn't enough (need recursion)
  - Leveraging Gemini's long context for synthesizing many pages
  - Local usage via MCP
- ❌ Не используй если:
  - Need quick, single-shot answer (too slow)
  - Production API required (this is a tool)
  - Sensitive data (sends context to LLM)

### 🚀 Запуск
```bash
# Clone and link via MCP settings
uv run mcp-server-deep-research
```

### 🧩 Архитектура
- **Protocol:** MCP
- **Logic:** Search -> Analyze -> Follow-up Questions -> Synthesize
- **Provider:** Google Gemini (typically)
- **Tools:** `search`, `visit_page`
- **Output:** Markdown report

### 🧪 Примеры задач
- "Create a comprehensive comparison table of all Solana AI agents"
- "Research the legal history of a specific case law"
- "Find all GitHub repos related to MCP servers and categorize them"
- "Summarize the latest 5 papers on Diffusion Transformers"

### ⚠️ Ограничения
- Can get into infinite loops if not capped
- High token usage (cost/quota) due to visiting many pages
- Requires Gemini API key
- Quality depends on the underlying Search API used

### 🧭 Fit / Maturity / Ops
- **Fit:** Researchers, Analysts
- **Maturity:** experimental
- **Latency/Cost:** high (multiple calls)
- **Data constraints:** web access
- **Ops friction:** low

### Full links
- Repo: https://github.com/ssdeanx/deep-research-mcp-server
- Stars: ~63
- Maturity: active

---

## Sentience (Galadriel)

**TL;DR:** Framework для создания cryptographically verifiable AI agents. "Unruggable" agents — их действия записываются on-chain, невозможен rug-pull от разработчиков. Proof of Sentience SDK делает LLM inferences верифицируемыми. Решает trust problem для AI agents с $10B+ market cap. От команды Galadriel AI.

### Быстрый выбор
- ✅ Используй если:
  - Создаёшь AI agents с crypto/token backing
  - Нужна cryptographic verifiability действий агента
  - Хочешь "unruggable" trust guarantee
  - Building autonomous agents с on-chain proof
  - Galadriel ecosystem
- ❌ Не используй если:
  - Обычный AI assistant без crypto (overkill)
  - Нет понимания blockchain/crypto
  - Quick prototyping (complex setup)
  - Не нужна verifiability

### 🚀 Запуск
```bash
git clone https://github.com/galadriel-ai/Sentience
cd Sentience
pip install -r requirements.txt
# Configure with Galadriel API keys
python example_agent.py
```

### 🧩 Архитектура
- **Language:** Python SDK
- **Verification:** On-chain proof of LLM inferences
- **Backend:** Galadriel verified inference
- **Features:** cryptographic proofs, activity logs, autonomous agents
- **Entrypoints:** SDK module, example agents

### 🧪 Примеры задач
- Создание token-backed AI agent
- Proof of consciousness logging (как zerebro, aixbt)
- Autonomous trading agent с verifiable decisions
- DAO-governed AI agents
- Trust-minimized AI services

### ⚠️ Ограничения
- Early stage project (62 stars)
- Galadriel ecosystem dependency
- Crypto/blockchain knowledge required
- Complex setup vs regular agents
- Limited documentation

### 🧭 Fit / Maturity / Ops
- **Fit:** Crypto AI agents, verifiable AI, DAOs
- **Maturity:** emerging (active development)
- **Latency/Cost:** Galadriel API costs
- **Data constraints:** API keys, blockchain access
- **Ops friction:** high (crypto + AI setup)

### Full links
- Repo: https://github.com/galadriel-ai/Sentience
- Stars: 62
- Maturity: active

---

## cdp-agentkit-nodejs (Coinbase)

**TL;DR:** The official Node.js SDK for Coinbase Developer Platform's "AgentKit". Enables AI agents to natively interact with on-chain functionality—creating wallets, sending transactions, and interacting with smart contracts—using a standardized toolkit. 57 stars.

### Быстрый выбор
- ✅ Используй если:
  - Building "On-Chain Agents" in Node.js/TypeScript
  - Need enterprise-grade wallet infrastructure (Coinbase MPC wallets)
  - Integrating into existing CDP workflows
  - Require regulated/compliant standard for crypto handling
  - LangChain JS integration needed
- ❌ Не используй если:
  - Python preferred (use Python SDK)
  - Purely decentralized generic wallet usage (use viem/wagmi)
  - High frequency trading (API rate limits apply)
  - Don't have a Coinbase Developer account

### 🚀 Запуск
```bash
npm install @coinbase/cdp-agentkit-core
```
```typescript
import { CdpAgentkit } from "@coinbase/cdp-agentkit-core";
// Setup with LangChain Tool
const toolkit = new CdpToolkit(agentKit);
```

### 🧩 Архитектура
- **Core:** Node.js SDK
- **Backend:** Coinbase Developer Platform APIs
- **Wallets:** MPC (Multi-Party Computation) Wallets
- **Integration:** LangChain Tools (`CdpTool`)
- **Entrypoints:** `CdpAgentkit`

### 🧪 Примеры задач
- "Create a wallet for a new user automatically"
- "Agent automatically pays for gas fees (Paymaster)"
- "Execute a USDC transfer based on chat command"
- "Deploy a simple NFT contract via AI agent"
- "Fund a wallet from a master faucet"

### ⚠️ Ограничения
- Requires reliance on Coinbase infrastructure
- KYC/Compliance might be a factor for mainnet
- Early alpha/beta stage of the SDK
- Rate limits on CDP API

### 🧭 Fit / Maturity / Ops
- **Fit:** Web3 Developers, Enterprise AI
- **Maturity:** emerging (official)
- **Latency/Cost:** API based
- **Data constraints:** CDP access
- **Ops friction:** medium (keys/setup)

### Full links
- Repo: https://github.com/coinbase/cdp-agentkit-nodejs
- Stars: ~57 (expect growth)
- Maturity: active

---

## qudeai-framework-v.1

**TL;DR:** Open-source framework для создания AI agents в CLI с Qude как co-pilot. Деплой агентов на Solana blockchain. Интеграция с Bitquery APIs для blockchain data: market cap, top holders, trending tokens. Natural language queries для взаимодействия с агентами. Node.js environment.

### Быстрый выбор
- ✅ Используй если:
  - Создание AI agents для Solana
  - CLI-based agent development
  - Нужен Bitquery blockchain data
  - Market analysis и token metrics
  - Node.js/TypeScript stack
- ❌ Не используй если:
  - Не Solana (другие chains)
  - GUI/web interface needed
  - Enterprise production (early project)
  - Python preferred

### 🚀 Запуск
```bash
git clone https://github.com/qudeai/qudeai-framework-v.1
cd qudeai-framework-v.1
npm install
# Configure .env with API keys
npm start
```

### 🧩 Архитектура
- **Language:** Node.js/TypeScript
- **Blockchain:** Solana integration
- **Data:** Bitquery APIs
- **Features:** agent deployment, market analysis, token queries
- **Entrypoints:** CLI commands

### 🧪 Примеры задач
- Deploy custom AI agent to Solana
- Query token market cap и holders
- Analyze trending tokens
- Trading pattern analysis
- Custom blockchain queries

### ⚠️ Ограничения
- Early stage project (53 stars)
- Solana only
- Bitquery API required (costs)
- Limited documentation
- CLI only interface

### 🧭 Fit / Maturity / Ops
- **Fit:** Solana developers, DeFi researchers
- **Maturity:** experimental
- **Latency/Cost:** Bitquery API costs
- **Data constraints:** API keys
- **Ops friction:** medium (setup)

### Full links
- Repo: https://github.com/qudeai/qudeai-framework-v.1
- Stars: 53
- Maturity: active

---

## propease

**TL;DR:** Modern SaaS landing page template для real estate бизнеса. Next.js + TailwindCSS + Framer Motion. Полностью responsive design с premium aesthetics. Property listings, agent profiles, contact forms. Готовый шаблон для быстрого старта real estate проекта.

### Быстрый выбор
- ✅ Используй если:
  - Запуск real estate SaaS/landing
  - Нужен modern premium design
  - Next.js stack preferred
  - Быстрый MVP landing page
  - Learning Next.js + TailwindCSS
- ❌ Не используй если:
  - Не real estate domain
  - Full CMS backend needed (add yourself)
  - Non-Next.js stack
  - Need unique custom design

### 🚀 Запуск
```bash
git clone https://github.com/Shreyas-29/propease
cd propease
npm install
npm run dev
# Open http://localhost:3000
```

### 🧩 Архитектура
- **Framework:** Next.js 14 (App Router)
- **Styling:** TailwindCSS + Framer Motion
- **Features:** property cards, agent profiles, forms
- **Design:** responsive, mobile-first
- **Entrypoints:** Next.js pages

### 🧪 Примеры задач
- Real estate company landing page
- Property listing showcase
- Agent portfolio site
- Real estate lead generation
- Template для кастомизации

### ⚠️ Ограничения
- Template only (добавь backend сам)
- Real estate specific design
- Нет CMS integration
- Нет auth/payments built-in
- Customization required

### 🧭 Fit / Maturity / Ops
- **Fit:** Real estate startups, agencies
- **Maturity:** active
- **Latency/Cost:** free template
- **Data constraints:** none (static)
- **Ops friction:** low (Next.js)

### Full links
- Repo: https://github.com/Shreyas-29/propease
- Stars: 55
- Maturity: active

---

## n8n-workflows (Zie619)

**TL;DR:** Curated collection of n8n workflows — 50k+ stars. Готовые automation templates для различных сценариев: API integrations, data processing, notifications, AI workflows. Import напрямую в n8n. Огромная библиотека community workflows.

### Быстрый выбор
- ✅ Используй если:
  - Используешь n8n для automation
  - Ищешь готовые workflow templates
  - Нужно вдохновение для integrations
  - Learning n8n patterns
  - Быстрый старт без написания с нуля
- ❌ Не используй если:
  - Не используешь n8n
  - Нужен custom workflow (используй как reference)
  - Enterprise support needed (official n8n resources)
  - Other automation tools (Zapier, Make)

### 🚀 Запуск
```bash
# Browse workflows on GitHub
# Download .json workflow file
# Import in n8n: Settings -> Import Workflow -> Paste JSON
```

### 🧩 Архитектура
- **Format:** n8n JSON workflow files
- **Categories:** API, data, notifications, AI
- **Usage:** direct import to n8n
- **Maintenance:** community curated
- **Entrypoints:** individual workflow files

### 🧪 Примеры задач
- Slack notification workflows
- Email automation
- Database sync patterns
- AI/LLM integration examples
- Multi-service orchestration

### ⚠️ Ограничения
- Workflows могут быть outdated
- Нужны правки под твои credentials
- Quality varies (community)
- Some workflows untested
- n8n version compatibility

### 🧭 Fit / Maturity / Ops
- **Fit:** n8n users, automation enthusiasts
- **Maturity:** curated list (50k stars)
- **Latency/Cost:** free
- **Data constraints:** n8n required
- **Ops friction:** low (import JSON)

### Full links
- Repo: https://github.com/Zie619/n8n-workflows
- Stars: 50,461
- Maturity: curated list

---

## meme-mcp

**TL;DR:** MCP server для генерации мемов через ImgFlip API. Позволяет Claude Desktop и другим MCP клиентам создавать мемы с кастомным текстом. Простая интеграция через npx. Требует бесплатный ImgFlip account. Забавный инструмент для AI-генерации контента.

### Быстрый выбор
- ✅ Используй если:
  - Хочешь генерировать мемы через AI
  - Claude Desktop/MCP integration
  - Нужен fun content для social media
  - Автоматизация meme creation
  - Быстрый setup (npx)
- ❌ Не используй если:
  - Серьёзный production use case
  - Нет ImgFlip account
  - Custom meme templates нужны (limited to ImgFlip)
  - Non-MCP environment

### 🚀 Запуск
```bash
# Add to Claude Desktop config (Settings -> Developer -> Edit Config)
{
  "mcpServers": {
    "meme": {
      "command": "npx",
      "args": ["-y", "meme-mcp"],
      "env": {
        "IMGFLIP_USERNAME": "<username>",
        "IMGFLIP_PASSWORD": "<password>"
      }
    }
  }
}
```

### 🧩 Архитектура
- **Protocol:** Model Context Protocol (MCP)
- **API:** ImgFlip meme generation
- **Tool:** `generateMeme` с template ID и текстами
- **Runtime:** Node.js (npx)
- **Entrypoints:** MCP server

### 🧪 Примеры задач
- "Make a Drake meme about coding"
- "Generate a distracted boyfriend meme"
- "Create meme for my presentation"
- Social media content automation
- Fun team communication

### ⚠️ Ограничения
- ImgFlip account required (free)
- Limited to ImgFlip templates
- Two text fields only
- Depends on ImgFlip API availability
- Fun tool, not production-critical

### 🧭 Fit / Maturity / Ops
- **Fit:** Claude Desktop users, content creators
- **Maturity:** active
- **Latency/Cost:** free (ImgFlip)
- **Data constraints:** ImgFlip credentials
- **Ops friction:** low (npx)

### Full links
- Repo: https://github.com/haltakov/meme-mcp
- NPM: https://www.npmjs.com/package/meme-mcp
- Stars: 45
- Maturity: active

---

## solana-trader-proto

**TL;DR:** Protobuf definitions для bloXroute Solana Trader API. gRPC schema для high-frequency trading на Solana через bloXroute infrastructure. Типы для orders, quotes, streams. Используй для генерации клиентов на любом языке. Official от bloXroute Labs.

### Быстрый выбор
- ✅ Используй если:
  - Интеграция с bloXroute Trader API
  - High-frequency Solana trading
  - Нужны type-safe gRPC clients
  - Multi-language codegen (Go, Python, TS)
  - Low-latency trading requirements
- ❌ Не используй если:
  - Не используешь bloXroute
  - Simple trading (используй Jupiter SDK)
  - Нет bloXroute subscription
  - Learning Solana (too advanced)

### 🚀 Запуск
```bash
git clone https://github.com/bloXroute-Labs/solana-trader-proto
# Generate client for your language
protoc --go_out=. trader.proto  # Go
protoc --python_out=. trader.proto  # Python
```

### 🧩 Архитектура
- **Format:** Protobuf (.proto files)
- **Protocol:** gRPC
- **Types:** orders, quotes, streams, transactions
- **Languages:** any with protobuf support
- **Entrypoints:** proto files

### 🧪 Примеры задач
- Generate Go client для trading bot
- TypeScript types для frontend
- Python client для research
- Low-latency order submission
- Market data streaming

### ⚠️ Ограничения
- Requires bloXroute subscription
- Complex setup (gRPC)
- Not standalone (just proto definitions)
- Solana only
- Enterprise-focused

### 🧭 Fit / Maturity / Ops
- **Fit:** HFT developers, bloXroute users
- **Maturity:** active (official)
- **Latency/Cost:** bloXroute pricing
- **Data constraints:** bloXroute access
- **Ops friction:** medium (protobuf setup)

### Full links
- Repo: https://github.com/bloXroute-Labs/solana-trader-proto
- Stars: 45
- Maturity: active

---

## twAuto

**TL;DR:** Python библиотека для Twitter automation без API. Tweet, retweet, reply, quote, like через Selenium. Обходит Twitter API limitations. Cookie-based auth для устойчивости. Headless mode для серверного запуска. Альтернатива платным Twitter API планам.

### Быстрый выбор
- ✅ Используй если:
  - Twitter automation без API costs
  - Small-scale posting/engagement
  - Python Selenium experience
  - Обход Twitter API quotas
  - Простые операции (tweet, like, reply)
- ❌ Не используй если:
  - Enterprise scale (ban risk)
  - Twitter API access есть
  - Scraping data (not this tool's purpose)
  - Real-time streaming needed
  - Нет опыта с Selenium

### 🚀 Запуск
```bash
pip install twAuto
```
```python
import twAuto

tw = twAuto.twAuto(
    username="your_username",
    email="your_email",
    password="your_password",
    chromeDriverMode="auto",
    headless=True
)
tw.start()
tw.login()
tw.tweet(text="Hello from twAuto!")
tw.close()
```

### 🧩 Архитектура
- **Language:** Python 3.7+
- **Browser:** Selenium + Chrome WebDriver
- **Auth:** cookie-based persistence
- **Features:** tweet, retweet, reply, quote, like, scrape notifications
- **Entrypoints:** twAuto module

### 🧪 Примеры задач
- Automate daily tweets
- Auto-like specific content
- Reply automation
- Quote tweet campaigns
- Notification monitoring

### ⚠️ Ограничения
- Account ban risk (ToS violation)
- Selenium browser overhead
- Twitter UI changes can break it
- Rate limiting applies
- Cookie management required

### 🧭 Fit / Maturity / Ops
- **Fit:** Small-scale automation, hobbyists
- **Maturity:** active
- **Latency/Cost:** free (no API)
- **Data constraints:** credentials
- **Ops friction:** medium (Selenium setup)

### Full links
- Repo: https://github.com/EKOzkan/twAuto
- PyPI: https://pypi.org/project/twAuto/
- Stars: 27
- Maturity: active

---

## aether (Shreyas-29)

**TL;DR:** AI-powered chatbot с "superpowers". Next.js + OpenAI integration. Modern UI с dark mode и animations. File upload support, code highlighting, markdown rendering. Template для создания premium AI chat interfaces. От автора propease.

### Быстрый выбор
- ✅ Используй если:
  - Нужен AI chatbot template
  - Next.js stack preferred
  - OpenAI GPT integration
  - Premium UI aesthetics
  - Learning Next.js + AI
- ❌ Не используй если:
  - Production-ready solution needed
  - Non-OpenAI models
  - Backend-heavy requirements
  - Enterprise features

### 🚀 Запуск
```bash
git clone https://github.com/Shreyas-29/aether
cd aether
npm install
# Add OPENAI_API_KEY to .env.local
npm run dev
```

### 🧩 Архитектура
- **Framework:** Next.js 14
- **AI:** OpenAI API (GPT-4/3.5)
- **Styling:** TailwindCSS + Framer Motion
- **Features:** streaming, code blocks, file upload
- **Entrypoints:** Next.js App Router

### 🧪 Примеры задач
- Personal AI assistant interface
- Code review chatbot
- Q&A bot template
- Customer support prototype
- AI demo application

### ⚠️ Ограничения
- OpenAI API costs apply
- Template only (expand yourself)
- No auth built-in
- No database persistence
- Single user focus

### 🧭 Fit / Maturity / Ops
- **Fit:** Developers, AI enthusiasts
- **Maturity:** active
- **Latency/Cost:** OpenAI API costs
- **Data constraints:** API key
- **Ops friction:** low (Next.js)

### Full links
- Repo: https://github.com/Shreyas-29/aether
- Stars: 27
- Maturity: active

---

## uniswap-v2-v3-arbitrage

**TL;DR:** Arbitrage bot для Uniswap V2/V3. Flash loan powered arbitrage между AMM pools. Solidity smart contracts + TypeScript bot. Находит price discrepancies и executes atomic swaps. Educational project для понимания DeFi arbitrage mechanics.

### Быстрый выбор
- ✅ Используй если:
  - Изучаешь DeFi arbitrage
  - Uniswap V2/V3 development
  - Flash loan understanding
  - Solidity + TS stack
  - Educational purposes
- ❌ Не используй если:
  - Production trading (competition!)
  - Expect profits (saturated market)
  - No blockchain experience
  - Gas optimization not done

### 🚀 Запуск
```bash
git clone https://github.com/dexbotsdev/uniswap-v2-v3-arbitrage
cd uniswap-v2-v3-arbitrage
npm install
# Configure .env with RPC, private key
npx hardhat compile
npx hardhat run scripts/deploy.js
```

### 🧩 Архитектура
- **Contracts:** Solidity (Hardhat)
- **Bot:** TypeScript
- **Loans:** Flash loans (Aave/DyDx)
- **DEXes:** Uniswap V2 + V3
- **Entrypoints:** deploy script, bot runner

### 🧪 Примеры задач
- Detect арбитраж opportunities
- Execute atomic flash loan swaps
- Learn flash loan mechanics
- Understand AMM pricing
- Study gas optimization

### ⚠️ Ограничения
- Highly competitive (MEV bots)
- Gas costs can exceed profits
- Requires significant capital understanding
- Not profitable without optimization
- Educational, not production-ready

### 🧭 Fit / Maturity / Ops
- **Fit:** DeFi developers, learners
- **Maturity:** experimental
- **Latency/Cost:** gas + flash loan fees
- **Data constraints:** node RPC access
- **Ops friction:** high (blockchain dev)

### Full links
- Repo: https://github.com/dexbotsdev/uniswap-v2-v3-arbitrage
- Stars: 22
- Maturity: active

---

## nextjs-lucia-neon-postgresql-drizzle-dashboard

**TL;DR:** Full-stack personal dashboard template. Next.js 14 + Lucia Auth + Neon PostgreSQL + Drizzle ORM. Modern landing + dashboard UI. Authentication с sessions, database schema, API routes. All-in-one starter для SaaS/dashboard projects.

### Быстрый выбор
- ✅ Используй если:
  - Нужен full-stack dashboard starter
  - Next.js + PostgreSQL stack
  - Lucia auth preferred
  - Drizzle ORM experience
  - Landing + dashboard комбо
- ❌ Не используй если:
  - Different auth (NextAuth, Clerk)
  - Non-PostgreSQL database
  - Minimal requirements (overkill)
  - Production-ready out of box

### 🚀 Запуск
```bash
git clone https://github.com/remcostoeten/nextjs-lucia-neon-postgresql-drizzle-dashboard
cd nextjs-lucia-neon-postgresql-drizzle-dashboard
pnpm install
# Configure DATABASE_URL in .env
pnpm db:push
pnpm dev
```

### 🧩 Архитектура
- **Framework:** Next.js 14 (App Router)
- **Auth:** Lucia (session-based)
- **Database:** Neon PostgreSQL + Drizzle ORM
- **Styling:** TailwindCSS + shadcn/ui
- **Entrypoints:** landing, auth, dashboard pages

### 🧪 Примеры задач
- SaaS dashboard boilerplate
- Personal project tracker
- Admin panel starter
- Authentication flow learning
- Full-stack Next.js template

### ⚠️ Ограничения
- Personal project (limited docs)
- Neon-specific setup
- Opinionated stack choices
- May need updates for compatibility

### 🧭 Fit / Maturity / Ops
- **Fit:** Next.js developers, SaaS builders
- **Maturity:** active
- **Latency/Cost:** Neon free tier available
- **Data constraints:** database setup
- **Ops friction:** medium (DB config)

### Full links
- Repo: https://github.com/remcostoeten/nextjs-lucia-neon-postgresql-drizzle-dashboard
- Stars: 20
- Maturity: active

---

## caps-ai

**TL;DR:** Landing page template для social media management tool. Modern design с градиентами и animations. React/Next.js + TailwindCSS. Hero section, features, pricing, testimonials. Готовый template для AI/SaaS продуктов.

### Быстрый выбор
- ✅ Используй если:
  - Нужен SaaS landing page template
  - Social media/AI product design
  - Modern gradient aesthetics
  - Quick launch landing
  - React/Next.js stack
- ❌ Не используй если:
  - Full product needed (just landing)
  - Non-SaaS domain
  - Unique custom design required

### 🚀 Запуск
```bash
git clone https://github.com/sherryjutt932/caps-ai
cd caps-ai
npm install
npm run dev
```

### 🧩 Архитектура
- **Framework:** Next.js/React
- **Styling:** TailwindCSS
- **Sections:** hero, features, pricing, testimonials
- **Design:** gradients, glass effects
- **Entrypoints:** landing page components

### 🧪 Примеры задач
- AI product landing page
- Social media tool launch
- SaaS marketing site
- Portfolio of landing designs
- Template customization

### ⚠️ Ограничения
- Landing only (no backend)
- Template customization needed
- Social media theme specific
- No CMS built-in

### 🧭 Fit / Maturity / Ops
- **Fit:** SaaS founders, marketers
- **Maturity:** active
- **Latency/Cost:** free template
- **Data constraints:** none
- **Ops friction:** low

### Full links
- Repo: https://github.com/sherryjutt932/caps-ai
- Stars: 14
- Maturity: active

---

## maushish/alris

**TL;DR:** Twitter handle analyzer/tool. Автоматизация для анализа Twitter аккаунтов и handles. Python-based utility для social media research. Минимальный проект для специфичных Twitter tasks.

### Быстрый выбор
- ✅ Используй если:
  - Twitter handle research
  - Social media analysis
  - Python automation scripts
  - Quick Twitter data lookups
- ❌ Не используй если:
  - Full Twitter API access needed
  - Production-scale scraping
  - Non-Twitter platforms

### 🚀 Запуск
```bash
git clone https://github.com/maushish/alris
cd alris
pip install -r requirements.txt
python main.py
```

### 🧩 Архитектура
- **Language:** Python
- **Purpose:** Twitter handle analysis
- **Scale:** Script-level tool
- **Entrypoints:** main.py

### 🧪 Примеры задач
- Analyze Twitter handle metrics
- Lookup account information
- Research Twitter profiles
- Quick data extraction

### ⚠️ Ограничения
- Very small project (12 stars)
- Limited documentation
- Twitter changes may break it
- Single-purpose tool

### 🧭 Fit / Maturity / Ops
- **Fit:** Researchers, hobbyists
- **Maturity:** experimental
- **Latency/Cost:** free
- **Data constraints:** Twitter access
- **Ops friction:** low

### Full links
- Repo: https://github.com/maushish/alris
- Stars: 12
- Maturity: active

---

## avento

**TL;DR:** Landing page для high-performance agency OS. От автора propease и aether. Next.js + TailwindCSS + Framer Motion. Premium dark theme с glassmorphism. Hero + features + CTA sections. Template для agency/SaaS marketing sites.

### Быстрый выбор
- ✅ Используй если:
  - Agency landing page needed
  - Premium dark UI aesthetics
  - Next.js stack preferred
  - Quick marketing site launch
  - Animated modern design
- ❌ Не используй если:
  - Full product needed (landing only)
  - Light theme required
  - Non-agency domain

### 🚀 Запуск
```bash
git clone https://github.com/Shreyas-29/avento
cd avento
npm install
npm run dev
```

### 🧩 Архитектура
- **Framework:** Next.js 14
- **Styling:** TailwindCSS + Framer Motion
- **Design:** dark theme, glassmorphism
- **Sections:** hero, features, CTA
- **Entrypoints:** Next.js pages

### 🧪 Примеры задач
- Agency marketing site
- SaaS landing page
- Portfolio showcase
- Product launch page
- Design inspiration

### ⚠️ Ограничения
- Landing only (no backend)
- Dark theme specific
- Agency theme focused
- Template customization needed

### 🧭 Fit / Maturity / Ops
- **Fit:** Agencies, SaaS founders
- **Maturity:** active
- **Latency/Cost:** free template
- **Data constraints:** none
- **Ops friction:** low

### Full links
- Repo: https://github.com/Shreyas-29/avento
- Stars: 11
- Maturity: active

---

## Telegram_Scraper (Amirwpi)

**TL;DR:** Python scraper для Telegram groups. Извлечение members, messages, media из групп через Telegram API. Telethon library based. Экспорт в JSON/CSV. Для research и data collection из публичных Telegram групп.

### Быстрый выбор
- ✅ Используй если:
  - Нужен Telegram group data
  - Member list extraction
  - Message history scraping
  - Python Telethon experience
  - Research/OSINT purposes
- ❌ Не используй если:
  - Private groups (need invite)
  - Real-time monitoring (use bots)
  - No Telegram API credentials
  - Privacy concerns (ToS)

### 🚀 Запуск
```bash
git clone https://github.com/Amirwpi/Telegram_Scraper
cd Telegram_Scraper
pip install -r requirements.txt
# Configure API_ID and API_HASH from my.telegram.org
python scraper.py
```

### 🧩 Архитектура
- **Language:** Python 3.x
- **Library:** Telethon
- **API:** Telegram MTProto
- **Output:** JSON/CSV export
- **Entrypoints:** scraper.py

### 🧪 Примеры задач
- Extract group member list
- Download message history
- Analyze group activity
- Research community metrics
- Data backup from groups

### ⚠️ Ограничения
- Requires Telegram API credentials
- Rate limiting applies
- ToS violation risk
- Public groups only (mostly)
- Account ban possible

### 🧭 Fit / Maturity / Ops
- **Fit:** Researchers, OSINT, marketers
- **Maturity:** experimental
- **Latency/Cost:** free (API)
- **Data constraints:** Telegram credentials
- **Ops friction:** medium (API setup)

### Full links
- Repo: https://github.com/Amirwpi/Telegram_Scraper
- Stars: 9
- Maturity: active

---

## openagent (openagentoa)

**TL;DR:** Platform для создания, battle и trade AI agents. Gamified AI agent marketplace. Create agents с кастомными abilities, battle других agents, trade на marketplace. Web3 + AI fusion концепт. Early experimental project.

### Быстрый выбор
- ✅ Используй если:
  - Gamified AI agents interest
  - Web3 + AI fusion
  - Trading agent mechanics
  - Experimental AI projects
  - Community/game mechanics
- ❌ Не используй если:
  - Production AI needed
  - Serious business use case
  - No crypto/gaming interest

### 🚀 Запуск
```bash
git clone https://github.com/openagentoa/openagent
cd openagent
npm install
npm run dev
```

### 🧩 Архитектура
- **Platform:** Web-based
- **Features:** create, battle, trade agents
- **Model:** Gamified AI marketplace
- **Tech:** Web3 integration
- **Entrypoints:** web app

### 🧪 Примеры задач
- Create custom AI agent
- Battle other agents
- Trade agents on marketplace
- Explore AI gaming concepts
- Community competitions

### ⚠️ Ограничения
- Very early stage (8 stars)
- Experimental concept
- Limited documentation
- Web3 dependency
- Not production-ready

### 🧭 Fit / Maturity / Ops
- **Fit:** AI gamers, Web3 enthusiasts
- **Maturity:** experimental
- **Latency/Cost:** free to explore
- **Data constraints:** wallet/account
- **Ops friction:** medium

### Full links
- Repo: https://github.com/openagentoa/openagent
- Stars: 8
- Maturity: active

---

## AGInterface

**TL;DR:** Modular interactive chat interface для agentic AI systems. React-based UI для работы с AI agents. Customizable panels и conversation views. Предназначен для построения chat interfaces к agent systems типа AutoGPT.

### Быстрый выбор
- ✅ Используй если:
  - Building chat UI for AI agents
  - Modular panel system needed
  - React/TypeScript project
  - AutoGPT-like interfaces
  - Customizable conversation views
- ❌ Не используй если:
  - Simple chatbot UI (overkill)
  - Non-React stack
  - Production-ready needed (small project)

### 🚀 Запуск
```bash
git clone https://github.com/JamesonRGrieve/AGInterface
cd AGInterface
npm install
npm run dev
```

### 🧩 Архитектура
- **Framework:** React/TypeScript
- **Design:** modular panels, agents
- **Features:** chat, conversation management
- **Styling:** modern UI components
- **Entrypoints:** React components

### 🧪 Примеры задач
- Agent chat interface
- Multi-panel workspace
- Conversation history views
- Agent control panel
- Custom AI frontend

### ⚠️ Ограничения
- Small project (9 stars)
- Limited backend integration
- Documentation minimal
- Experimental stage

### 🧭 Fit / Maturity / Ops
- **Fit:** Agent UI developers
- **Maturity:** experimental
- **Latency/Cost:** free (frontend)
- **Data constraints:** agent backend
- **Ops friction:** low (npm)

### Full links
- Repo: https://github.com/JamesonRGrieve/AGInterface
- Stars: 9
- Maturity: active

---

## ai-agent-demo

**TL;DR:** Demo проект для AI Agents. Образовательный пример как строить AI agents с tool calling. Python-based с OpenAI integration. Простой starter для изучения agent patterns. Minimal code для понимания концепций.

### Быстрый выбор
- ✅ Используй если:
  - Learning AI agent concepts
  - Simple reference code needed
  - Python + OpenAI stack
  - Educational purposes
  - Quick demo setup
- ❌ Не используй если:
  - Production agent needed
  - Enterprise features
  - Non-educational use case

### 🚀 Запуск
```bash
git clone https://github.com/halfordAI/ai-agent-demo
cd ai-agent-demo
pip install -r requirements.txt
# Add OPENAI_API_KEY to .env
python main.py
```

### 🧩 Архитектура
- **Language:** Python
- **AI:** OpenAI API
- **Features:** tool calling demo
- **Scale:** educational example
- **Entrypoints:** main.py

### 🧪 Примеры задач
- Learn agent patterns
- Understand tool calling
- Quick AI demo
- Teaching materials
- Reference implementation

### ⚠️ Ограничения
- Demo only (8 stars)
- Not production-ready
- Minimal documentation
- OpenAI dependency

### 🧭 Fit / Maturity / Ops
- **Fit:** Learners, educators
- **Maturity:** demo
- **Latency/Cost:** OpenAI API costs
- **Data constraints:** API key
- **Ops friction:** low

### Full links
- Repo: https://github.com/halfordAI/ai-agent-demo
- Stars: 8
- Maturity: demo

---

## GeminiSheeridVerify

**TL;DR:** Tool для верификации через SheerID для Google Gemini. Автоматизация student/education verification процесса. Получение доступа к education discounts и features. Python-based utility.

### Быстрый выбор
- ✅ Используй если:
  - Student verification для Gemini
  - Education discount access needed
  - Automation of verification
  - SheerID integration
- ❌ Не используй если:
  - Non-education account
  - Already verified
  - Legal concerns about automation

### 🚀 Запуск
```bash
git clone https://github.com/devtint/GeminiSheeridVerify
cd GeminiSheeridVerify
pip install -r requirements.txt
python main.py
```

### 🧩 Архитектура
- **Language:** Python
- **API:** SheerID verification
- **Target:** Google Gemini education
- **Entrypoints:** main.py

### 🧪 Примеры задач
- Student verification automation
- Education discount access
- Gemini feature unlock
- Verification workflow

### ⚠️ Ограничения
- Very small project (10 stars)
- May violate ToS
- Specific use case only
- Maintenance uncertain

### 🧭 Fit / Maturity / Ops
- **Fit:** Students, education users
- **Maturity:** experimental
- **Latency/Cost:** free tool
- **Data constraints:** education credentials
- **Ops friction:** low

### Full links
- Repo: https://github.com/devtint/GeminiSheeridVerify
- Stars: 10
- Maturity: active

---

## physics-liquid-glass

**TL;DR:** WebGL effect для liquid glass physics. Three.js based visual effect с реалистичным liquid distortion. Interactive demo с mouse tracking. Для web creative coding и portfolio pieces. Visually stunning effect.

### Быстрый выбор
- ✅ Используй если:
  - Portfolio/demo site effect
  - Creative coding project
  - Three.js experience
  - Visual design showcase
  - Interactive art pieces
- ❌ Не используй если:
  - Production performance critical
  - Non-visual project
  - No WebGL support needed

### 🚀 Запуск
```bash
git clone https://github.com/bobbyroe/physics-liquid-glass
cd physics-liquid-glass
npm install
npm run dev
```

### 🧩 Архитектура
- **Framework:** Three.js
- **Rendering:** WebGL shaders
- **Effect:** liquid glass distortion
- **Interaction:** mouse tracking
- **Entrypoints:** web demo

### 🧪 Примеры задач
- Portfolio hero effect
- Creative demo site
- Interactive art installation
- Visual experiments
- Design inspiration

### ⚠️ Ограничения
- Performance intensive
- WebGL required
- Effect-only (no utility)
- Small project (15 stars)

### 🧭 Fit / Maturity / Ops
- **Fit:** Designers, creative coders
- **Maturity:** active
- **Latency/Cost:** free (frontend)
- **Data constraints:** none
- **Ops friction:** low

### Full links
- Repo: https://github.com/bobbyroe/physics-liquid-glass
- Stars: 15
- Maturity: active

---

## gemini-notion-extension

**TL;DR:** Browser extension интегрирующая Google Gemini с Notion. AI-powered features для Notion workspace: summarization, writing assistance, content generation. Chrome extension для enhanced productivity.

### Быстрый выбор
- ✅ Используй если:
  - Notion power user
  - Gemini AI integration wanted
  - Chrome browser
  - Writing/summarization help needed
  - Productivity enhancement
- ❌ Не используй если:
  - Different browser (Chrome only)
  - Non-Notion workflow
  - Privacy concerns (sends data to Gemini)

### 🚀 Запуск
```bash
git clone https://github.com/PatelPratikkumar/gemini-notion-extension
cd gemini-notion-extension
npm install
npm run build
# Load unpacked extension in Chrome
```

### 🧩 Архитектура
- **Type:** Chrome Extension
- **AI:** Google Gemini API
- **Target:** Notion integration
- **Features:** summarize, generate, assist
- **Entrypoints:** extension popup

### 🧪 Примеры задач
- Summarize Notion pages
- Generate content ideas
- Writing assistance
- Note organization help
- AI-powered editing

### ⚠️ Ограничения
- Very small project (4 stars)
- Chrome only
- Gemini API key required
- Notion-specific
- Early experimental

### 🧭 Fit / Maturity / Ops
- **Fit:** Notion + AI enthusiasts
- **Maturity:** experimental
- **Latency/Cost:** Gemini API
- **Data constraints:** API key
- **Ops friction:** medium (extension setup)

### Full links
- Repo: https://github.com/PatelPratikkumar/gemini-notion-extension
- Stars: 4
- Maturity: active

---

## run-gemini-cli (Google GitHub Actions)

**TL;DR:** Official Google GitHub Action для запуска Gemini CLI. Позволяет использовать Gemini AI в GitHub workflows. Автоматизация code review, PR summarization, documentation generation. 1.7k stars от Google.

### Быстрый выбор
- ✅ Используй если:
  - GitHub Actions workflows
  - CI/CD AI integration
  - Automated code review
  - Documentation generation
  - Google Gemini preference
- ❌ Не используй если:
  - Non-GitHub CI/CD
  - Local development only
  - Different AI model preferred

### 🚀 Запуск
```yaml
# .github/workflows/gemini.yml
- uses: google-github-actions/run-gemini-cli@v1
  with:
    gemini_api_key: ${{ secrets.GEMINI_API_KEY }}
    prompt: "Review this PR for issues"
```

### 🧩 Архитектура
- **Type:** GitHub Action
- **AI:** Google Gemini CLI
- **Integration:** GitHub workflows
- **Auth:** Gemini API key
- **Entrypoints:** action.yml

### 🧪 Примеры задач
- Automated PR review
- Code summarization
- Documentation generation
- Issue triage
- Changelog creation

### ⚠️ Ограничения
- GitHub-specific
- Gemini API costs
- Rate limits apply
- Workflow integration required

### 🧭 Fit / Maturity / Ops
- **Fit:** GitHub users, DevOps
- **Maturity:** active (official Google)
- **Latency/Cost:** Gemini API pricing
- **Data constraints:** API key in secrets
- **Ops friction:** low (action config)

### Full links
- Repo: https://github.com/google-github-actions/run-gemini-cli
- Stars: 1,704
- Maturity: active

---

## hsm-service

**TL;DR:** Centralized cryptographic service используя SoftHSM v2. Hardware Security Module simulation для development/testing. Key management, signing operations, encryption. Docker-based deployment. Для разработки crypto-приложений без реального HSM.

### Быстрый выбор
- ✅ Используй если:
  - HSM development/testing
  - PKCS#11 experiments
  - Key management prototyping
  - Криптографические сервисы
  - Docker environment
- ❌ Не используй если:
  - Production HSM needed (use real HSM)
  - Non-PKCS#11 requirements
  - High security production

### 🚀 Запуск
```bash
git clone https://github.com/titaev-lv/hsm-service
cd hsm-service
docker-compose up -d
# Service available on configured port
```

### 🧩 Архитектура
- **Core:** SoftHSM v2
- **Interface:** PKCS#11
- **Deployment:** Docker
- **Features:** key storage, signing, encrypt/decrypt
- **Entrypoints:** API endpoints

### 🧪 Примеры задач
- Test PKCS#11 integration
- Key generation experiments
- Signing service prototype
- Encryption workflow testing
- HSM emulation

### ⚠️ Ограничения
- Very small project (1 star)
- Not production HSM security
- SoftHSM limitations
- Development/testing only

### 🧭 Fit / Maturity / Ops
- **Fit:** Crypto developers, testers
- **Maturity:** experimental
- **Latency/Cost:** free (Docker)
- **Data constraints:** local keys
- **Ops friction:** medium (Docker)

### Full links
- Repo: https://github.com/titaev-lv/hsm-service
- Stars: 1
- Maturity: active

---

# 🔧 SMALLER STARRED REPOS (< 10 stars)

Ниже — репозитории с меньшим количеством stars (персональные проекты, форки, нишевые инструменты).

---

## promptdc-cursor

**TL;DR:** Prompt engineering tool для Cursor IDE. Интеграция с DC (Domain Context) для enhanced prompting. Помогает структурировать контекст для AI-assisted coding. Очень ранний experimental проект.

### Быстрый выбор
- ✅ Используй если: Cursor IDE user, prompt engineering experiments, context optimization
- ❌ Не используй если: Production use, non-Cursor IDE, stable tools needed

### 🚀 Запуск
```bash
# Install as Cursor extension or clone repo
```

### 🧩 Архитектура
- **Type:** Cursor extension/tool
- **Purpose:** Prompt structuring with domain context
- **Entrypoints:** Extension

### 🧪 Примеры: Enhanced prompts for Cursor AI, context management

### ⚠️ Ограничения: 1 star, experimental, limited docs

### 🧭 Fit/Maturity/Ops: Cursor users | experimental | free | low friction

### Full links
- Stars: 1 | Maturity: experimental

---

## promptdc-vscode

**TL;DR:** Prompt engineering tool для VSCode. Аналог promptdc-cursor для VSCode environment. Domain Context integration для structured AI prompting. Experimental project.

### Быстрый выбор
- ✅ Используй если: VSCode user, prompt engineering, context optimization
- ❌ Не используй если: Production, stable extension needed

### 🚀 Запуск
```bash
# Install as VSCode extension
```

### 🧩 Архитектура
- **Type:** VSCode extension
- **Purpose:** Prompt structuring
- **Entrypoints:** Extension commands

### 🧪 Примеры: Structured prompts, context templates

### ⚠️ Ограничения: 1 star, experimental

### 🧭 Fit/Maturity/Ops: VSCode users | experimental | free | low friction

### Full links
- Stars: 1 | Maturity: experimental

---

## Threads.net-Writer

**TL;DR:** Tool для публикации в Threads.net с помощью Gemini AI. Генерация контента через LLM и автоматическая публикация. Social media automation для Threads платформы.

### Быстрый выбор
- ✅ Используй если: Threads.net presence, AI content generation, social automation
- ❌ Не используй если: Manual posting preferred, no Gemini API

### 🚀 Запуск
```bash
git clone [repo]
pip install -r requirements.txt
# Configure Gemini API key
python main.py
```

### 🧩 Архитектура
- **AI:** Google Gemini
- **Platform:** Threads.net
- **Features:** content generation, auto-post

### 🧪 Примеры: Generate thread ideas, schedule posts, AI-written updates

### ⚠️ Ограничения: 3 stars, Threads API changes, ToS considerations

### 🧭 Fit/Maturity/Ops: Social media managers | experimental | Gemini API cost | medium friction

### Full links
- Stars: 3 | Maturity: experimental

---

## QAMI

**TL;DR:** Quantum Assembly Machine Infinity — experimental quantum computing simulator/tool. Educational project для изучения quantum assembly concepts. Niche research tool.

### Быстрый выбор
- ✅ Используй если: Quantum computing interest, educational experiments, research
- ❌ Не используй если: Production quantum computing, real quantum hardware

### 🚀 Запуск
```bash
git clone [repo]
# Follow setup instructions
```

### 🧩 Архитектура
- **Type:** Quantum simulator
- **Purpose:** Educational, research
- **Entrypoints:** Main script

### 🧪 Примеры: Quantum gate experiments, assembly simulation, learning

### ⚠️ Ограничения: 3 stars, very niche, experimental

### 🧭 Fit/Maturity/Ops: Researchers, students | experimental | free | high friction

### Full links
- Stars: 3 | Maturity: experimental

---

## webscraper-ts

**TL;DR:** Web scraper на TypeScript. Lightweight scraping library для Node.js. Простой API для извлечения данных с веб-страниц. Educational/utility project.

### Быстрый выбор
- ✅ Используй если: TypeScript project, simple scraping needs, learning
- ❌ Не используй если: Production (use Playwright/Puppeteer), complex scraping

### 🚀 Запуск
```bash
npm install webscraper-ts
# or clone repo
```

### 🧩 Архитектура
- **Language:** TypeScript
- **Runtime:** Node.js
- **Features:** basic scraping, DOM parsing

### 🧪 Примеры: Extract data from static pages, simple crawling

### ⚠️ Ограничения: 2 stars, basic features, no JS rendering

### 🧭 Fit/Maturity/Ops: TS developers | experimental | free | low friction

### Full links
- Stars: 2 | Maturity: experimental

---

## scrapliz

**TL;DR:** Chrome extension для web scraping. Визуальный scraper без кода — выбирай элементы на странице и экспортируй данные. No-code approach для non-developers.

### Быстрый выбор
- ✅ Используй если: No-code scraping, visual element selection, Chrome user
- ❌ Не используй если: Programmatic scraping, automation pipelines

### 🚀 Запуск
```bash
# Load unpacked extension in Chrome
# Or install from Chrome Web Store (if available)
```

### 🧩 Архитектура
- **Type:** Chrome Extension
- **Features:** visual selector, export CSV/JSON
- **Entrypoints:** Browser action

### 🧪 Примеры: Scrape product listings, extract tables, collect links

### ⚠️ Ограничения: 3 stars, Chrome only, basic features

### 🧭 Fit/Maturity/Ops: Non-developers | experimental | free | low friction

### Full links
- Stars: 3 | Maturity: experimental

---

## twit (Hypefury fork)

**TL;DR:** Fork Twitter API client от Hypefury. Node.js library для Twitter/X API v1.1 и v2. Maintained fork оригинального twit package с исправлениями.

### Быстрый выбор
- ✅ Используй если: Node.js Twitter bot, API v1.1/v2 access, maintained fork needed
- ❌ Не используй если: Official Twitter SDK preferred, Python project

### 🚀 Запуск
```bash
npm install @hypefury/twit
```
```javascript
const Twit = require('@hypefury/twit');
const T = new Twit({ consumer_key: '...', ... });
T.post('statuses/update', { status: 'hello!' });
```

### 🧩 Архитектура
- **Language:** Node.js
- **API:** Twitter v1.1 + v2
- **Features:** tweet, stream, DM, media upload

### 🧪 Примеры: Posting tweets, streaming mentions, media upload

### ⚠️ Ограничения: 4 stars, Twitter API changes, rate limits

### 🧭 Fit/Maturity/Ops: Bot developers | active | Twitter API costs | low friction

### Full links
- Stars: 4 | Maturity: active

---

## dexbotsdev repos

**TL;DR:** Коллекция Solana/DeFi утилит от dexbotsdev. Arbitrage bots, token scrapers, trading tools. Multiple small repos (1-22 stars каждый). Educational и experimental DeFi tools.

### Быстрый выбор
- ✅ Используй если: Solana DeFi research, arbitrage learning, trading experiments
- ❌ Не используй если: Production trading (competition!), expect profits

### 🚀 Запуск
```bash
# Clone specific repo from dexbotsdev GitHub
git clone https://github.com/dexbotsdev/[repo-name]
```

### 🧩 Архитектура
- **Language:** TypeScript/Solidity
- **Chain:** Solana, EVM
- **Features:** arbitrage, scraping, trading

### 🧪 Примеры: Flash loan arb, token analysis, DEX interaction

### ⚠️ Ограничения: Small repos, not profitable without optimization, educational

### 🧭 Fit/Maturity/Ops: DeFi learners | experimental | gas costs | high friction

### Full links
- GitHub: https://github.com/dexbotsdev
- Stars: 1-22 per repo | Maturity: experimental

---

## alexkoshmelev repos

**TL;DR:** Telegram web app и dapp templates от alexkoshmelev. Starter templates для Telegram Mini Apps. React/Next.js based. TON blockchain integration examples.

### Быстрый выбор
- ✅ Используй если: Telegram Mini App development, TON dapp templates
- ❌ Не используй если: Non-Telegram app, production-ready needed

### 🚀 Запуск
```bash
git clone https://github.com/alexkoshmelev/[repo]
npm install
npm run dev
```

### 🧩 Архитектура
- **Framework:** React/Next.js
- **Platform:** Telegram Mini Apps
- **Blockchain:** TON integration

### 🧪 Примеры: Telegram webapp starter, TON wallet connect, mini app template

### ⚠️ Ограничения: 1 star, personal templates, limited documentation

### 🧭 Fit/Maturity/Ops: Telegram developers | experimental | free | medium friction

### Full links
- GitHub: https://github.com/alexkoshmelev
- Stars: 1 per repo | Maturity: experimental

---

## abdibrokhim bots

**TL;DR:** Telegram bots collection — anonymio (anonymous messages), attendance tracker, link shortener. Python-based Telegram bot templates. Educational projects.

### Быстрый выбор
- ✅ Используй если: Telegram bot development, Python bots, learning
- ❌ Не используй если: Production bots, enterprise features

### 🚀 Запуск
```bash
git clone https://github.com/abdibrokhim/[bot-name]
pip install -r requirements.txt
# Add BOT_TOKEN to .env
python main.py
```

### 🧩 Архитектура
- **Language:** Python
- **Library:** python-telegram-bot / aiogram
- **Features:** anonymous messaging, attendance, URL shortening

### 🧪 Примеры: Anonymous confession bot, team attendance tracking, link shortener

### ⚠️ Ограничения: 2 stars, basic features, personal projects

### 🧭 Fit/Maturity/Ops: Bot learners | experimental | free (Telegram) | low friction

### Full links
- GitHub: https://github.com/abdibrokhim
- Stars: 2 per repo | Maturity: experimental

---

*Last updated: January 2026*