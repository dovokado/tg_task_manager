# Changelog — TG Task Manager

## 2026-06-17
- Встановлено CLAUDE-KIT (глобальні налаштування Claude + шаблони проєкту).
- Створено каркас документації проєкту: `CLAUDE.md`, `SKILL.md`, `BUGS.md`,
  `CHANGELOG.md`, стан проєкту в пам'яті (`project_tg-task-manager.md`).
- Закладено фундамент коду: `.venv`, `pyproject.toml` (fastapi, uvicorn,
  aiogram, sqlalchemy[asyncio], asyncpg, alembic, pydantic-settings,
  apscheduler), `.env.example`, `.gitignore`.
- Каркас застосунку: `app/config.py` (pydantic-settings), `app/db/models.py`
  (Employee, Shift, Dialog), `app/db/session.py` (async engine), `app/bot/main.py`
  (aiogram, обробник `/start`), `app/api/main.py` (FastAPI, `/health`),
  `app/scheduler/jobs.py` (заглушка APScheduler).
- Перевірено: залежності встановлюються без помилок на Python 3.14, FastAPI
  піднімається й `/health` повертає `{"status":"ok"}`, усі модулі (bot/db/scheduler)
  імпортуються без помилок.
