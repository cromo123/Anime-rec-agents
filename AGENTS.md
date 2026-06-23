# AGENTS.md

Guidance for AI coding agents working on this repository.

## Project

Project name: `anime-recommendation-agents`

This is a study and portfolio project for a Python AI Agent Developer opportunity.

The goal is to build a FastAPI backend that recommends anime using a future CrewAI multi-agent workflow. The final system should use:

- The user's current request
- The user's current mood
- MyAnimeList history and scores
- Stored user preferences
- RAG/vector search
- Multiple specialized agents

The final recommendation should return one anime with a structured explanation.

## Current Development Philosophy

The user is a beginner with this stack. Keep the code clean, simple, and beginner-readable.

Prefer small working milestones over large complex implementations. Each milestone should be runnable, testable, and easy to understand.

Do not build the full production system early. Start with simple deterministic behavior, then replace pieces with real integrations later when requested.

## Technology Targets

Use or prepare for:

- Python 3.11+
- FastAPI
- Pydantic
- pytest
- CrewAI later
- Official MyAnimeList API later
- PostgreSQL later
- Vector database/RAG later
- Azure Service Bus later
- Docker/deploy later

## Hard Rules

1. Do not implement everything at once.
2. Keep every milestone runnable and testable.
3. Prefer simple deterministic fake logic before real AI/API logic.
4. Keep external API integrations behind service/tool classes.
5. Do not hardcode secrets, tokens, API keys, or credentials.
6. Use `.env.example` for environment variable examples.
7. Every API response should be structured and typed with Pydantic models.
8. Add tests for every meaningful feature.
9. Do not add real CrewAI, real MyAnimeList OAuth, database, RAG, or Azure Service Bus until explicitly requested.
10. Keep documentation updated as the project evolves.

## Architecture Direction

Keep responsibilities separated:

- FastAPI handles HTTP routing and request/response concerns.
- Services contain business logic.
- Tools contain external capabilities that agents can later use.
- Crew files contain future CrewAI agents, tasks, and orchestration.
- Database files will be added later.
- Documentation lives in `docs/`.

Suggested future layout:

```text
anime-recommendation-agents/
  app/
    main.py
    api/
      routes/
    models/
    services/
    tools/
    crew/
  tests/
  docs/
  .env.example
  README.md
```

Adjust the layout only when it makes the project easier to understand.

## Initial Goal

The first working milestone should create a FastAPI skeleton with:

- `/health` endpoint
- `/recommend` endpoint
- Fake recommendation logic
- Fake MyAnimeList user history import service
- Tests
- Documentation explaining project phases

The fake logic should be deterministic and obvious. For example, it can choose a recommendation based on mood, preferred genre, or a small in-memory anime list.

## API Guidelines

- Use Pydantic request and response models.
- Keep response shapes stable and explicit.
- Prefer clear field names over clever abstractions.
- Return one anime recommendation, not a long ranked list, unless requested later.
- Include a structured explanation, such as:
  - why this anime matches the request
  - how mood influenced the recommendation
  - how fake MAL history influenced the recommendation
  - what future agent/tool would improve the answer

## Testing Guidelines

Use `pytest`.

Add tests for:

- Health endpoint behavior
- Recommend endpoint request/response shape
- Fake recommendation service behavior
- Fake MyAnimeList history import service behavior

Tests should be simple and readable. Avoid heavy mocking unless it keeps external behavior isolated.

## External Integrations

Do not call real external APIs until requested.

When external integrations are added later:

- Put API access behind service/tool classes.
- Read secrets from environment variables.
- Document required variables in `.env.example`.
- Add tests that avoid real network calls by default.

## Documentation

Keep `README.md` and files in `docs/` current.

Documentation should explain:

- What milestone the project is on
- How to run the app
- How to run tests
- What is fake for now
- What will be replaced later by CrewAI, MyAnimeList, database, RAG, Service Bus, Docker, or deployment work

## Style

- Favor boring, readable Python.
- Keep functions small.
- Use descriptive names.
- Avoid premature abstractions.
- Avoid adding large frameworks or dependencies without a clear milestone reason.
- Prefer explicit imports and straightforward control flow.

When unsure, choose the simplest working implementation that teaches the next useful concept.
