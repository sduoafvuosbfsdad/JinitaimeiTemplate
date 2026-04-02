# Jinitaimei1234 Full Stack Template

Simple full-stack auth starter with:

- `frontend/`: React + Vite app
- `backend/`: FastAPI service
- `database`: PostgreSQL in Docker

## Current Setup

The project is wired for local development with Docker Compose:

- Frontend runs on `http://localhost:9178`
- Backend runs on `http://localhost:6767`
- PostgreSQL runs on `localhost:5432`

The frontend container runs Vite directly, so changes show up immediately during development.
The backend container runs `uvicorn` with `--reload` enabled for auto-refresh.

## Services

- `frontend`
  - Built from `./frontend/Dockerfile`
  - Starts Vite on port `9178`
- `backend`
  - Built from `./backend/Dockerfile.dev`
  - Starts FastAPI with Uvicorn on port `6767`
- `database`
  - Uses `postgres:18.3-alpine`
  - Initializes with:
    - user: `caixukun`
    - password: `Jinitaimei1234`
    - database: `XiaoHeiZi`

## Development

Start everything with:

```bash
docker compose -f docker-compose.dev.yml up --build
```

Useful URLs:

- Frontend: `http://localhost:9178`
- Backend: `http://localhost:6767`

## Backend Endpoint

The backend currently exposes a simple root route:

- `GET /` returns `Hello, World!`

## Notes

- The backend compose file uses a health check against the FastAPI root route.
- The frontend compose file points directly to the Vite dev server.
- `db_data` is stored in a named Docker volume so the database persists between runs.
