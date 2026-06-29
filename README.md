# DAEDALUS

DAEDALUS is a Technology Compass for deep-tech research decisions.

It is not an AI scientist yet. v0.1 is a disciplined internal system for:

- storing engineering opportunities,
- scoring them objectively,
- preserving evidence,
- tracking assumptions,
- and designing falsifiable experiments.

## Core Principle

> No claim without evidence. No evidence without measurement. No measurement without understanding the physics.

## Stack

- Frontend: React + TypeScript + Vite
- Backend: FastAPI + SQLModel
- Database: PostgreSQL
- Deployment: Docker Compose locally; Render/Vercel/Supabase or Neon for cloud

## Local Run

```bash
docker compose up --build
```

Open:

```text
Frontend: http://localhost:5173
API docs: http://localhost:8000/docs
```

## Cloud Setup

See [`docs/CLOUD_SETUP.md`](docs/CLOUD_SETUP.md).

Recommended cloud setup:

- Vercel for frontend
- Render for backend
- Supabase or Neon Postgres for database

## v0.1 Modules

1. Opportunity database
2. Evidence register
3. Assumption library
4. Opportunity scoring engine
5. Experiment planner

## v0.2 Direction

- Add create/edit forms in UI
- Add authentication
- Add CSV import/export
- Add paper/patent source tracking
- Add richer scoring explanations
- Add first 20 Atlas opportunities
