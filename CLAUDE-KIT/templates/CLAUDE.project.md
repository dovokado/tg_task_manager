# <PROJECT NAME>

> Project-level CLAUDE.md template. Lives in the project repository root.
> Extends the global `<claude-home>/CLAUDE.md` (does not cancel it).
> This template is in English; fill the content for the project. Remove the `<…>`
> hints once filled. Note: project documentation (BUGS/CHANGELOG/notes) is Ukrainian.

## Language
Comments, documentation, user-facing text — Ukrainian.
Code (function/variable names) — English.

## Stack
<!-- List the technologies. Example: -->
- <language + version, e.g. Python 3.12>
- <framework, e.g. FastAPI + aiogram 3.x>
- <database, e.g. PostgreSQL + SQLAlchemy>
- <external APIs / services>

## Configs
<!-- Where settings and secrets live. Example: -->
Everything in `.env`, accessed via `app/config.py`.
Don't commit secrets. Example vars in `.env.example`.

## Structure
<!-- A short tree of key folders/files so Claude can orient. -->
```
<project>/
├── CLAUDE.md
├── BUGS.md
├── CHANGELOG.md
└── app/ ...
```

## Important
- `BUGS.md` — all found bugs (log immediately).
- `CHANGELOG.md` — all changes.
- <key agreements: API URL, data formats, invariants>.

## Workflow (short)
- Before working: read this file + `SKILL.md` (if present) + `project_<name>.md`.
- Code change → update the relevant docs in the same iteration.
- Task completion → deploy-summary with a DoD checklist.

## <Domain specifics>
<!-- e.g. state machine, business rules, key entities.
Example: Dialog flow: new → clarifying → confirming → done. -->
