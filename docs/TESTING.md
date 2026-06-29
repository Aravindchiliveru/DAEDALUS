# DAEDALUS Testing Guide

## Backend smoke test

After starting the backend, verify:

```bash
curl http://localhost:8000/health
curl http://localhost:8000/opportunities
```

Expected health response:

```json
{"status":"ok","system":"DAEDALUS"}
```

## Frontend smoke test

Start frontend and open:

```text
http://localhost:5173
```

You should see:

- DAEDALUS v0.1 hero section
- Metrics cards
- Highest-ranked opportunity
- Opportunity Atlas table
- Evidence register
- Assumption library
- Experiment planner

## Cloud verification

Backend:

```text
https://<backend-domain>/health
https://<backend-domain>/opportunities
```

Frontend:

```text
https://<frontend-domain>
```

## Known v0.1 limitation

v0.1 is read-heavy and seed-data driven. Create/edit forms will be added in v0.2.
