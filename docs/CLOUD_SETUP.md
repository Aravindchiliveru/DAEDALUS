# DAEDALUS Cloud Setup

Recommended deployment:

- Database: Supabase Postgres or Neon Postgres
- Backend: Render Web Service
- Frontend: Vercel

## 1. Database

Create a Postgres database and copy the connection string.

Use this as backend environment variable:

```text
DATABASE_URL=postgresql+psycopg://USER:PASSWORD@HOST:PORT/DBNAME
```

## 2. Backend on Render

Create a new Web Service from this GitHub repository.

Settings:

```text
Root directory: backend
Build command: pip install -r requirements.txt
Start command: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Environment variables:

```text
DATABASE_URL=<your postgres connection string>
CORS_ORIGINS=https://<your-vercel-domain>
```

Health check path:

```text
/health
```

## 3. Frontend on Vercel

Create a new Vercel project from this GitHub repository.

Settings:

```text
Root directory: frontend
Build command: npm run build
Output directory: dist
```

Environment variable:

```text
VITE_API_BASE_URL=https://<your-render-backend-domain>
```

## 4. Local Development

```bash
# backend
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# frontend
cd frontend
npm install
npm run dev
```

## 5. Verification

Backend:

```text
GET /health
GET /opportunities
GET /evidence
GET /assumptions
GET /experiments
```

Frontend should show:

- Opportunity count
- Evidence count
- Assumption count
- Experiment count
- Highest-ranked opportunity
- Opportunity Atlas table
