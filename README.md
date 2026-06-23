# anime-recommendation-agents

A study and portfolio project for a Python AI Agent Developer opportunity.

This project is a FastAPI backend that recommends one anime from a structured request. The first milestone uses fake deterministic logic so the app is easy to run, test, and understand. Later milestones can replace the fake pieces with CrewAI agents, the official MyAnimeList API, stored preferences, RAG/vector search, PostgreSQL, Azure Service Bus, and deployment.

## Why This Project Exists

The goal is to practice building an AI-agent-style backend in small, working steps. Instead of trying to build every advanced feature at once, each milestone adds one useful concept while keeping the project runnable and testable.

## Current Milestone

Milestone 1 includes:

- FastAPI app
- `GET /health`
- `POST /recommend`
- Pydantic request and response models
- Fake MyAnimeList history import service
- Fake taste profile builder
- Deterministic recommendation service
- Placeholder CrewAI files
- Tests with pytest
- Beginner-friendly project plan

This milestone does not use real CrewAI, real MyAnimeList OAuth, a real database, RAG, Service Bus, Docker, or deployment.

## Install

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install the project with test dependencies:

```bash
pip install -e ".[dev]"
```

## Run the API

```bash
uvicorn app.main:app --reload
```

Open:

- API: `http://127.0.0.1:8000`
- Docs: `http://127.0.0.1:8000/docs`
- Health check: `http://127.0.0.1:8000/health`

Example request:

```bash
curl -X POST "http://127.0.0.1:8000/recommend" ^
  -H "Content-Type: application/json" ^
  -d "{\"user_id\":\"demo-user\",\"message\":\"I want a psychological thriller\",\"mood\":\"curious\"}"
```

## Run Tests

```bash
pytest
```

## Next Milestones

1. Improve fake recommendation rules while keeping them deterministic.
2. Add more request fields and richer explanations.
3. Add a simple in-memory preference store.
4. Add real MyAnimeList API integration behind a service/tool class.
5. Add CrewAI agents and tasks.
6. Add PostgreSQL for user preferences.
7. Add RAG/vector search for anime descriptions.
8. Add async workflows and Azure Service Bus.
9. Add Docker and deployment.
10. Polish the project as a portfolio demo.

See [docs/project_plan.md](docs/project_plan.md) for the detailed learning plan.
