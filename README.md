# <div align="center">ColCommute</div>

ColCommute is a commute-matching backend for student carpooling. It combines:

- Google ADK agents for chat-driven ride coordination
- FastAPI endpoints for authentication
- SQLAlchemy + Alembic for persistence
- Google Maps geocoding and routing for route-aware matching

## What It Does

ColCommute currently supports:

- user signup and login with JWT auth
- fetching the current logged-in user
- posting commute offers and ride requests
- matching riders with drivers on the same route, including middle-of-route pickup cases
- searching for ride offers on a route, with fallback to nearby ride requests
- confirming trips
- tracking trip lifecycle: `confirmed -> in_progress -> completed -> paid`
- persisting payment records and ride feedback
- fare splitting helpers

## Project Layout

```text
ColCommute/
|-- agents/                  # ADK agents
|-- api/                     # FastAPI app and auth routes
|-- alembic/                 # Database migrations
|-- colcommute/
|   |-- agent.py             # Root ADK agent
|   `-- db/                  # SQLAlchemy models and session config
|-- core/                    # Shared config, including model selection
|-- services/                # Business logic
|-- tests/                   # Focused backend tests
`-- tools/                   # ADK tool wrappers
```

## Requirements

- Python 3.10+
- PostgreSQL
- Google API / Gemini access
- Google Maps API key for geocoding and routing

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment

Create a `.env` file in the repo root.

Minimum useful setup:

```bash
DATABASE_URL=postgresql+psycopg://USER:PASSWORD@HOST:5432/DATABASE_NAME
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
GOOGLE_MAPS_API_KEY=YOUR_GOOGLE_MAPS_API_KEY
JWT_SECRET_KEY=CHANGE_ME
```

Also supported:

- `GOOGLE_MAP_API_KEY` as an alternative to `GOOGLE_MAPS_API_KEY`
- `DB_CONNECT_TIMEOUT`
- `DB_SSLMODE`
- `COLCOMMUTE_MODEL`
- `COLCOMMUTE_FALLBACK_MODEL`

Default model behavior:

- primary model: `gemini-2.5-flash-lite`
- fallback model: `gemini-2.5-flash`

## Database Setup

Run migrations:

```bash
python -m alembic -c alembic.ini upgrade head
```

Check current revision:

```bash
python -m alembic -c alembic.ini current
```

## Run The Services

### Run FastAPI

```bash
uvicorn api.main:app --reload
```

Useful endpoints:

- `GET /health`
- `POST /auth/signup`
- `POST /auth/login`
- `GET /auth/me`

Swagger UI will be available at:

```text
http://127.0.0.1:8000/docs
```

### Run ADK

```bash
adk web
```

Or:

```bash
adk run colcommute
```

## Auth Flow

1. Sign up or log in
2. Save the returned bearer token
3. Call `GET /auth/me`
4. Use the returned `external_user_id` when a user-specific ride action needs identity

## Matching Behavior

Ride matching uses:

- destination compatibility by place ID or nearby coordinates
- route corridor matching, so a rider can be picked up in the middle of a driver route
- broader location-text fallback, so queries like `Ghaziabad` can match more specific places like `ABESIT Ghaziabad`
- time bucket compatibility
- offer/request seat compatibility

If no ride offers are found for a route search, the system can also return nearby ride requests as a fallback.

## Data Model

- `users`: auth and user identity records
- `commute_posts`: open ride offers or ride requests
- `trips`: confirmed rides with lifecycle status
- `trip_payments`: persisted payment rows
- `trip_feedback`: persisted ride feedback

## Tests

There are focused tests for:

- auth endpoints
- pricing
- ride posting and matching
- trip lifecycle

Some local environments may not have `pytest` installed, but the files are under `tests/` and compile cleanly.

## Notes

- Route quality depends on good geocoding data.
- Obvious out-of-region geocoding results are rejected for India-based searches.
- Old bad rows already inserted in the database may still need manual cleanup.

---

Built with Google ADK, FastAPI, SQLAlchemy, and Google Maps.
