# Project Stack

## Overview

This project is a full-stack AI agent monitoring application combining a modern Next.js frontend with a Python-based agentic backend.

---

## Tech Stack

### Frontend
- **[Next.js](https://nextjs.org/)** — React framework for production
- **[shadcn/ui](https://ui.shadcn.com/)** — Accessible, composable UI components

### Backend
- **[Python](https://www.python.org/)** — Core backend language
- **[OpenAI Agents SDK](https://openai.github.io/openai-agents-python/)** — Agent orchestration and tool use
- **[Temporal](https://temporal.io/)** — Durable workflow engine for monitoring agent workflows
- **[LiteLLM](https://www.litellm.ai/)** — Unified LLM proxy, used here to route calls through the Gemini API

---

## Prerequisites

- **Node.js** (v18+) and **pnpm**
- **Python** (3.11+) and **uv**
- A running **Temporal** server (local or cloud)
- A valid **Gemini API key**

---

## Quick Start

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <your-project>
```

### 2. Frontend

```bash
cd frontend

# Install dependencies
pnpm install

# Start the dev server
pnpm dev
```

The frontend will be available at `http://localhost:3000`.

### 3. Backend

```bash
cd backend

# Create a virtual environment and install dependencies
uv sync

# Run the backend server
uv run main.py
```

### 4. Environment Variables

Create a `.env` file in the backend directory:

```env
GEMINI_API_KEY=your-gemini-api-key-here
```

And in the frontend directory:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 5. Temporal Worker

```bash
cd backend

# Start the Temporal workflow worker
uv run worker.py
```

> Make sure your Temporal server is running before starting the worker. For local development, you can use the [Temporal CLI](https://docs.temporal.io/cli):
> ```bash
> temporal server start-dev
> ```

---

## Project Structure

```
.
├── frontend/          # Next.js app with shadcn/ui
│   ├── app/
│   ├── components/
│   └── package.json
│
└── backend/           # Python backend
    ├── agents/        # OpenAI Agents SDK definitions
    ├── workflows/     # Temporal workflow definitions
    ├── main.py        # API entrypoint
    ├── worker.py      # Temporal worker entrypoint
    └── pyproject.toml
```
