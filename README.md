# ColCommute

A minimal multi-agent system demonstrating collaborative commute planning using the Google Agent Development Kit (ADK).

## Quick summary

ColCommute runs an `orchestrator` agent (see `colcommute/agent.py`) that delegates domain tasks to specialist agents and tools. The current prototype implements ride matching: registering commute posts, finding matches, and confirming trips.

## Project layout

```text
ColCommute/
├── agents/                 # ADK specialist agents (instructions + tool wiring)
├── tools/                  # ADK function tools (thin wrappers → services/)
├── colcommute/             # ADK app entry: root_agent (orchestrator)
│   ├── agent.py
│   └── db/                 # SQLAlchemy models, session, Alembic metadata
├── services/               # Business logic + Postgres (e.g. ride_services.py)
├── alembic/                # Migrations
└── requirements.txt
```

Local ADK development data is stored in `colcommute/.adk/` (for example, `session.db`) and is gitignored — it is not the application Postgres database.

## Quickstart

### Prerequisites

- Python 3.10+
- PostgreSQL (or a hosted Postgres instance)
- A Gemini / ADK API key (set via environment)

Install Python dependencies:

```bash
pip install -r requirements.txt
```

### Environment

Create a `.env` file in the repository root with (at minimum):

```bash
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
DATABASE_URL=postgresql+psycopg://USER:PASSWORD@HOST:5432/DATABASE_NAME
```

Other optional variables (see `colcommute/db/session.py`): `DB_CONNECT_TIMEOUT`, `DB_SSLMODE`, etc.

### Run the ADK dev server

From the repository root:

```bash
adk web
```

Open the URL printed by ADK (e.g. `http://127.0.0.1:8000`) and select the `colcommute` app to interact with `root_agent`. Alternative CLI run:

```bash
adk run colcommute
```

### Database migrations (Alembic)

Set `DATABASE_URL` in `.env`, then:

```bash
# create / upgrade DB schema
python -m alembic -c alembic.ini upgrade head

# see current revision
python -m alembic -c alembic.ini current

# create an autogenerate revision (review before applying)
python -m alembic -c alembic.ini revision --autogenerate -m "describe change"
```

## Data model (short)

- `users`: identity records (optional `external_user_id`, profile fields)
- `commute_posts`: open listings (destination fields, `time_bucket`, `vacant_seats` / `seats_needed`, FK to `users`)
- `trips`: confirmed rides that link offer and need posts after agreement

Matching is based on destination (place id or normalized text), time bucket, and seat compatibility.

## Notes & next steps

- The current prototype focuses on ride matching; routing, pricing, and notification agents are planned or stubbed.
- For manual testing, use real Place Details fields so the agent can call `register_commute_post` with valid place ids/coords.
- If you want, I can also: add badges, CI steps, or commit these changes.

---

Built with Google ADK
