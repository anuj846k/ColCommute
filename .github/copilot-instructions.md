---
name: copilot-instructions
description: "Workspace-level guidance for using Copilot Chat and the ADK agents in ColCommute."
---

# Copilot workspace instructions — ColCommute

Purpose: Provide a compact, link-first guide for Copilot Chat and contributor workflows when working with the ADK agents in this repo.

**Quick Start**

- Install dependencies: `pip install -r requirements.txt`
- Create `.env` in the repo root with `GOOGLE_API_KEY` and `DATABASE_URL` (see `colcommute/db/session.py`).
- Run dev chat: `adk web` (or `adk run colcommute`) and open the printed URL to interact with `root_agent`.
- Migrations: `python -m alembic -c alembic.ini upgrade head`

**Where to look (entry points)**

- Overview and run commands: [README.md](README.md)
- Orchestrator / app entry: [colcommute/agent.py](colcommute/agent.py)
- Ride-matching specialist: [agents/ride_matching.py](agents/ride_matching.py)
- Tools used by agents: [tools/ride_matching.py](tools/ride_matching.py)
- LLM config and model hooks: [core/llm.py](core/llm.py)
- DB models & session: [colcommute/db/models/commute_post.py](colcommute/db/models/commute_post.py) and [colcommute/db/session.py](colcommute/db/session.py)
- Example migrations: [alembic/versions/20260405_add_origin_place_fields.py](alembic/versions/20260405_add_origin_place_fields.py)

**How to ask Copilot / the agents**

Keep prompts focused, include the target file(s) and desired output. Examples:

- `Audit agents/ride_matching.py for performance and propose two micro-optimizations.`
- `Add unit tests for colcommute/db/models/commute_post.py that verify seat-matching logic.`
- `Create an Alembic migration adding origin_place fields; follow style in alembic/versions/20260405_add_origin_place_fields.py.`
- `Explain how to run the app locally and list required environment variables.`

**Conventions & expectations**

- Use `adk web` for exploratory conversations; make code changes in small, reviewable commits.
- Use Alembic for schema changes; always review generated revisions before applying.
- Prefer explicit file paths and short code examples in prompts (the agent uses those to scope changes).

**Next agent customizations to consider**

- `create-prompt.add-tests`: a prompt template to request unit tests for a specified module.
- `create-agent.migrations-helper`: an agent that scaffolds alembic revision boilerplate and sanity checks.
- `create-hook.pre-commit-format`: a pre-commit hook to run `black`/`ruff` on staged files.

Link-first principle: prefer linking to existing docs/code rather than embedding large excerpts. If a file is missing or unclear, open a short issue with the requested clarification.

---

For questions or suggested changes to these instructions, open an issue or propose an edit to this file.

**If you need fixes in the project**

- Describe the failing behavior and include relevant files or stack traces. Example: "Tests failing in `services/ride_services.py`; see traceback attached." 
- Preferred prompt for Copilot: `Find the bug in <file_or_module> and propose a minimal fix with a short test.`
- Quick triage steps you can ask the agent to run:
	- `Run static checks and list errors (ruff/flake8).`
	- `Run unit tests for <module> and show failing tests.`
	- `Suggest a minimal code change and corresponding unit test.`
- If the change touches DB schema, request an Alembic revision: `Create alembic revision to add <column> to <table>, following existing migration style.`
- For urgent or risky fixes, create an issue referencing the failing flow and assign someone for review before merging.

Use clear, focused prompts and include the smallest reproducible example when possible — the agent will propose fixes and can scaffold tests/migrations for review.
