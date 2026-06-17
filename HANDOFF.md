# HANDOFF — resume TG Task Manager on a new machine

> Paste this file's path into a fresh Claude Code session, opened inside the
> cloned project folder. Talk to the user in Ukrainian; confirm before any
> action that writes/modifies files, installs software, or pushes to git.

## Context
TG Task Manager: a Telegram bot + Gemini AI that turns ordinary chat messages
into structured Vikunja tasks, with shift-aware reminders. Repo:
https://github.com/dovokado/tg_task_manager
The fundament (venv, FastAPI/aiogram/SQLAlchemy skeleton) is already built and
pushed — see this repo's `CLAUDE.md` and `CHANGELOG.md` for what exists.

## Step 1 — verify environment
1. Confirm `git --version` and `python --version` work. If missing, guide
   manual installation (git-scm.com/download/win, python.org) the same way as
   before: explain what/why, wait for the user to confirm "готово".
2. Confirm the repo is already cloned at the current working directory
   (look for `CLAUDE.md`, `app/`, `pyproject.toml`). If not, confirm with the
   user, then `git clone https://github.com/dovokado/tg_task_manager.git`.

## Step 2 — recreate the Python environment
1. `python -m venv .venv`
2. `.venv\Scripts\pip install -e .` (Windows) — installs fastapi, aiogram,
   sqlalchemy[asyncio], asyncpg, alembic, pydantic-settings, apscheduler.
3. Verify: `uvicorn app.api.main:app` starts and `GET /health` returns
   `{"status":"ok"}`.
4. Note: `.env` is gitignored and won't exist after clone — copy
   `.env.example` to `.env` once real tokens are available; not needed yet
   for the skeleton to run.

## Step 3 — restore global Claude config (if missing)
Check whether `<claude-home>/CLAUDE.md` and `<claude-home>/memory/` already
exist on this machine.
- If they exist and look like the CLAUDE-KIT protocol — nothing to do.
- If missing: this repo includes a copy of the kit at `CLAUDE-KIT/`. Read
  `CLAUDE-KIT/INSTALL.md` and offer to run Steps 0–3 from it (global protocol
  + personal memory), confirming each write with the user as usual.

## Step 4 — restore project state memory
`project_tg-task-manager.md` (status/backlog) lives in
`<claude-home>/memory/` on the OLD machine — it does NOT travel with
`git clone`, since it's outside the repo by design (CLAUDE-KIT keeps project
memory global, not per-repo).
- Check if it already exists on this machine (e.g. copied manually together
  with the rest of `<claude-home>/memory/`).
- If missing: recreate it from this repo's `CLAUDE.md` + `CHANGELOG.md` (they
  capture the same facts — purpose, stack, decisions, backlog) and confirm
  the recreated status/backlog with the user before saving it.
- Flag to the user: this is a single point of failure for cross-machine
  continuity — consider asking whether they want project state mirrored
  inside the repo itself (e.g. `docs/PROJECT_STATE.md`) going forward, so a
  fresh clone is always self-sufficient.

## Step 5 — resume work
Read `CLAUDE.md` + `.claude/skills/tg-task-manager/SKILL.md` +
`project_tg-task-manager.md`, then continue the backlog. Last agreed next
step (as of this handoff): set up Alembic migrations against a real
PostgreSQL instance (local or Docker) before building the dialog logic —
reason: the dialog/Gemini/Vikunja logic can be mocked, but it's pointless to
build on models that have never touched a real database. Full backlog is in
`project_tg-task-manager.md` (or `CHANGELOG.md` as a fallback).

## House rules (recap — full version lives in global CLAUDE.md)
- Respond to the user in Ukrainian; code/identifiers in English; project docs
  in Ukrainian.
- Phase 1 (confirm understanding) → Phase 2 (plan, for T2-tier work) →
  confirm → execute. T0 (read-only) skips phases.
- Confirm before any action that writes files, installs software, or affects
  shared state (git push, etc.).
- Keep `BUGS.md` / `CHANGELOG.md` / `project_tg-task-manager.md` in sync with
  code changes in the same iteration.
