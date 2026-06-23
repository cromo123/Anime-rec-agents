# Project Plan

## Project Goal

`anime-recommendation-agents` is a beginner-friendly portfolio project for learning how to build a Python backend that can grow into a multi-agent anime recommendation system.

The final version should recommend one anime by combining:

- The user's current request
- The user's current mood
- MyAnimeList history and scores
- Stored user preferences
- RAG/vector search over anime data
- A CrewAI multi-agent workflow

The first version is intentionally simple. It uses fake data and deterministic logic so every part can be understood, tested, and improved.

## High-Level Architecture

FastAPI handles HTTP requests and responses. It should not contain the main business logic.

Services contain the business logic. For example, the recommendation service decides what anime to recommend, and the profile service converts anime history into a simple taste profile.

Tools contain external capabilities that agents can use later. The MyAnimeList user list tool is fake for now, but it shows where a real API integration can live later.

Crew files are placeholders for future CrewAI agents, tasks, and orchestration. CrewAI is not imported yet.

Documentation lives in `docs/` and should stay updated as the project changes.

## Folder Structure

```text
app/
  main.py
  schemas.py
  services/
    recommendation_service.py
    mal_import_service.py
    profile_service.py
  tools/
    mal_user_list_tool.py
  crew/
    agents.py
    tasks.py
    recommendation_crew.py

tests/
docs/
```

## Phase 1: FastAPI Skeleton

Build the first working API with `/health` and `/recommend`.

What I am learning:

- How a FastAPI app starts
- How routes accept and return Pydantic models
- How to run an API locally
- How to write basic API tests

Job connection:

- Shows Python API development fundamentals
- Shows that the project can be run and tested

## Phase 2: Better Fake Recommendation Logic

Improve the deterministic rules before adding real AI.

What I am learning:

- How to separate business logic from HTTP routes
- How to keep tests stable
- How to make fake logic useful enough for development

Job connection:

- Shows careful incremental development instead of overbuilding

## Phase 3: User Preferences

Add stored user preferences in a simple way first, possibly in memory or a local file.

What I am learning:

- How user preferences affect recommendations
- How to design typed data models
- How to test stateful behavior

Job connection:

- Maps to personalization logic used in real recommendation systems

## Phase 4: Real MyAnimeList API

Replace the fake MyAnimeList import with the official MyAnimeList API.

What I am learning:

- OAuth basics
- External API clients
- Environment variables
- Keeping secrets out of code
- Testing without real network calls

Job connection:

- Shows practical integration work with a third-party API

## Phase 5: CrewAI Agents

Add CrewAI after the deterministic version is stable.

Possible agents:

- ProfileAgent
- RecommendationAgent
- CriticAgent
- ExplanationAgent
- ScheduleAgent

What I am learning:

- How agents divide responsibilities
- How agents use tools
- How orchestration differs from simple function calls

Job connection:

- Directly maps to Python AI Agent Developer work

## Phase 6: PostgreSQL

Add a database for preferences, imported anime history, and recommendation records.

What I am learning:

- Database schema design
- Persistence
- Migrations
- Test databases

Job connection:

- Shows backend data skills beyond a toy script

## Phase 7: RAG and Vector Search

Add anime descriptions, embeddings, and vector search.

What I am learning:

- How retrieval helps recommendation quality
- How to chunk and store searchable information
- How to combine user intent with retrieved context

Job connection:

- Maps to common AI application patterns

## Phase 8: Async Workflows and Azure Service Bus

Move slow work, such as imports or background analysis, into asynchronous jobs.

What I am learning:

- Message queues
- Background processing
- Retry-friendly design
- Service boundaries

Job connection:

- Shows production-oriented architecture thinking

## Phase 9: Docker and Deployment

Package the app and prepare it for deployment.

What I am learning:

- Docker basics
- Environment configuration
- Running services consistently
- Deployment documentation

Job connection:

- Shows the project can move from local development toward production

## Phase 10: Portfolio Polish

Make the project easy for a reviewer to understand quickly.

What I am learning:

- How to communicate technical decisions
- How to show progress through milestones
- How to write useful README and docs

Job connection:

- Helps the project tell a clear story during interviews

## Current Fake Pieces

The following parts are fake in Phase 1:

- MyAnimeList import
- User taste profile data source
- Recommendation intelligence
- Agent execution
- Watch planning

These fake pieces are intentional. They make the project runnable now while leaving clear places to add real integrations later.
