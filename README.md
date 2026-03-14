---
title: Multi-Agent Content Team
emoji: 🤖
colorFrom: purple
colorTo: blue
sdk: gradio
sdk_version: 4.16.0
app_file: app.py
pinned: false
---

# 🤖 Multi-Agent Content Team

A production-grade **RAG-powered multi-agent AI pipeline** that autonomously researches, debates, writes, and edits publication-ready blog articles — powered by CrewAI, GPT-4o-mini, ChromaDB, and Tavily web search.

🔗 **Live Demo**: [ajaysathri-multi-agent-content-team.hf.space](https://ajaysathri-multi-agent-content-team.hf.space)

---

## 🏗️ Architecture

```
User Input (Topic)
       ↓
Tavily Web Search ──────────────────────┐
(live web data, ~10K chars)             │
       ↓                                │
ChromaDB RAG Retrieval                  │
(past research + stored articles)       │
       ↓                                │
┌──────────────────────────────────┐    │
│      CrewAI Multi-Agent Pipeline │    │
│                                  │    │
│  🔍 Research Agent ◄─ context ───┘    │
│           ↓                          │
│  💬 Debate Agent                     │
│           ↓                          │
│  ✍️  Writer Agent                    │
│           ↓                          │
│  ✏️  Editor Agent                    │
│           ↓                          │
│  ChromaDB ◄── store research         │
│             + article embeddings     │
└──────────────────────────────────┘
       ↓
Gradio UI
  • Live step-by-step agent progress
  • Rendered HTML article
  • Live RAG knowledge base badge
  • Markdown download
```

---

## ✨ Features

- **4-Agent CrewAI Pipeline** — Research → Debate → Write → Edit, each agent building on the last
- **Tavily Web Search** — Live internet retrieval injected as context before research begins (~10K chars per query)
- **ChromaDB RAG Memory** — Persistent vector store using `all-MiniLM-L6-v2` embeddings with cosine similarity; the system gets smarter with every article generated
- **Real-Time Streaming UI** — Step-by-step agent progress with animated indicators using Python threading + queue pattern
- **Live Knowledge Base Badge** — Header badge updates live after each generation showing stored research docs and articles count
- **Markdown Download** — Every generated article available as a downloadable `.md` file
- **Example Topics** — One-click topic buttons to get started instantly

---

## 🤖 Agent Roles

| Agent | Role | Responsibility |
|-------|------|----------------|
| 🔍 Research Agent | Senior Research Analyst | Synthesizes Tavily web data + RAG context into a comprehensive research brief |
| 💬 Debate Agent | Critical Analyst | Challenges assumptions, adds multi-perspective balance and counterarguments |
| ✍️ Writer Agent | Content Strategist | Transforms research into an engaging, structured long-form blog article |
| ✏️ Editor Agent | Senior Editor | Polishes tone, flow, structure, and adds title + subtitle |

---

## 🧠 RAG Pipeline

Every generation follows this knowledge loop:

```
1. Query ChromaDB for similar past research (cosine similarity)
2. Query ChromaDB for similar past articles (avoid repetition)
3. Run Tavily web search for live facts
4. Inject all context into Research Agent prompt
5. After research → store research brief in ChromaDB
6. After editing → store final article in ChromaDB
7. Next generation retrieves all of the above as context
```

The system continuously learns — each article makes the next one richer.

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Agent Framework | CrewAI 0.11.2 |
| LLM | GPT-4o-mini (OpenAI) |
| Web Search | Tavily API |
| Vector Store | ChromaDB 0.4.24 |
| Embeddings | all-MiniLM-L6-v2 (ONNX) |
| Orchestration | LangChain 0.1.12 |
| UI | Gradio 4.16.0 |
| Deployment | HuggingFace Spaces |

---

## 🚀 Local Setup

### 1. Clone the repo
```bash
git clone https://huggingface.co/spaces/ajaysathri/multi-agent-content-team
cd multi-agent-content-team
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set environment variables
```bash
export OPENAI_API_KEY=your_openai_key
export TAVILY_API_KEY=your_tavily_key   # optional but recommended
```

### 4. Run
```bash
python app.py
```

Open `http://localhost:7860`

---

## 🔑 HuggingFace Secrets Required

| Secret | Required | Purpose |
|--------|----------|---------|
| `OPENAI_API_KEY` | ✅ Yes | Powers all 4 agents via GPT-4o-mini |
| `TAVILY_API_KEY` | ⚡ Recommended | Live web search context (falls back gracefully if missing) |

---

## 📦 Dependencies

```
openai==1.13.3
httpx==0.27.0
crewai==0.11.2
langchain==0.1.12
langchain-openai==0.0.5
langchain-community==0.0.28
pydantic==2.6.4
huggingface-hub==0.20.3
chromadb==0.4.24
tavily-python==0.3.3
gradio==4.16.0
```

> **Note on pinned versions**: These exact versions were carefully resolved to avoid conflicts between CrewAI, LangChain, OpenAI SDK, and ChromaDB on HuggingFace Spaces.

---

## 📁 Project Structure

```
multi-agent-content-team/
├── app.py                  # Main Gradio app + streaming pipeline
├── requirements.txt        # Pinned dependencies
├── runtime.txt             # Python version
├── README.md
└── core/
    ├── agents.py           # CrewAI agent definitions
    ├── crew.py             # Crew orchestration
    ├── tasks.py            # Task definitions
    ├── tools.py            # Tavily web search tool
    ├── vector_store.py     # ChromaDB RAG store
    ├── knowledge_base.py   # Knowledge base utilities
    └── memory.py           # Agent memory config
```

---

## 🧩 Key Engineering Decisions

**Why CrewAI 0.11.2?**
Later versions introduced an `embedchain` dependency that conflicts with `langchain==0.1.12`. Version 0.11.2 is the last clean version before that conflict.

**Why inject Tavily as context instead of a tool?**
CrewAI 0.11.2 tool registration is limited. Calling Tavily before the agent and injecting results directly into the task prompt is more reliable and gives the agent richer, pre-processed context.

**Why ChromaDB PersistentClient?**
Unlike the deprecated `Client`, `PersistentClient` writes to disk immediately on every upsert — no manual `.persist()` needed, making it safe for the HF Spaces environment.

---

## 📊 What Gets Stored in ChromaDB

| Collection | Content | Used For |
|-----------|---------|---------|
| `research_memory` | Research briefs per topic | Enrich future research on similar topics |
| `published_articles` | Full articles per topic | Avoid repeating angles in future articles |

---

## 👤 Author

**Ajay Sathri**  
AI/ML Engineer | Multi-Agent Systems | RAG Pipelines

---

## 📄 License

MIT
