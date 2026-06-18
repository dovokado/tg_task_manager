# TG Task Manager

> Project-level CLAUDE.md. Lives in the project repository root.
> Extends the global `<claude-home>/CLAUDE.md` (does not cancel it).

## Language
Comments, documentation, user-facing text — Ukrainian.
Code (function/variable names) — English.

## Stack
- Python 3.12+ (developed on 3.14, venv in `.venv`)
- FastAPI (backend logic)
- aiogram 3.x (Telegram bot interface — chosen for async-native fit with FastAPI)
- Gemini API (natural-language understanding, dialog clarification)
- PostgreSQL + SQLAlchemy 2.0 (async) + asyncpg + Alembic (employees, shifts, dialogs)
- Vikunja — self-hosted task tracker (already deployed on infra), source of truth for tasks
- APScheduler (shift-based reminder timing)
- Single VPS hosts all components

## Configs
Secrets and settings in `.env` (Telegram bot token, Gemini API key, Vikunja API
token/URL, PostgreSQL DSN). Don't commit secrets. Example vars in `.env.example`.

## Structure
```
задачник/
├── CLAUDE.md
├── BUGS.md
├── CHANGELOG.md
├── HANDOFF.md            # runbook for Claude when resuming on a new machine
├── docs/PROJECT_STATE.md # mirror of <claude-home>/memory/project_tg-task-manager.md
├── pyproject.toml
├── .env.example
├── .claude/skills/tg-task-manager/SKILL.md
└── app/
    ├── bot/              # Telegram interface (aiogram)
    ├── api/              # FastAPI backend
    ├── scheduler/        # APScheduler — shift reminders
    └── db/               # PostgreSQL models/migrations
```

## Important
- `BUGS.md` — all found bugs (log immediately).
- `CHANGELOG.md` — all changes.
- Vikunja is the system of record for finalized tasks — the bot never duplicates
  its own storage of task state, only the clarification dialog.
- The raw clarification dialog in the chat is deleted once a task is created in
  Vikunja — only the finished task card should remain visible to the team.
- Reminders go to whoever is on shift right now per the schedule, not to a fixed
  "responsible person" — if that person isn't on shift, the next person in the
  schedule gets it instead.

## Workflow (short)
- Before working: read this file + `SKILL.md` + `project_tg-task-manager.md`
  (global memory) — fall back to `docs/PROJECT_STATE.md` (in-repo mirror) if
  the global memory file isn't present on this machine yet.
- Code change → update the relevant docs in the same iteration, including
  `docs/PROJECT_STATE.md` and `project_tg-task-manager.md` together (keep
  them in sync — see `docs/PROJECT_STATE.md` header for the tie-break rule).
- Task completion → deploy-summary with a DoD checklist.

## Domain specifics
- Dialog flow (per task being created): `new → clarifying → confirming → created`.
  - `new`: user message recognized as a task candidate.
  - `clarifying`: Gemini asks for missing fields (assignee, priority, deadline).
  - `confirming`: all fields collected, shown back to user for confirmation.
  - `created`: task pushed to Vikunja, chat dialog cleaned up, card posted to the
    task channel.
- Shift-aware reminders: the scheduler resolves "who is on shift now" from the
  shift table before sending a reminder, falling back to the next scheduled person
  if the nominal assignee is off shift.
