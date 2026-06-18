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
- Ініціалізовано git-репозиторій, перший коміт запушено на
  https://github.com/dovokado/tg_task_manager (гілка `master`).
- Додано `HANDOFF.md` — інструкція для Claude на новому ПК: як відновити
  середовище (venv, залежності), глобальний CLAUDE-KIT і стан проєкту з
  пам'яті, та з чого продовжувати беклог.

## 2026-06-19
- Додано `docs/PROJECT_STATE.md` — дзеркало стану проєкту прямо в репозиторії
  (раніше стан жив лише в `<claude-home>/memory/project_tg-task-manager.md`,
  яка не переноситься через `git clone`). Тепер свіжий клон сам по собі має
  повний контекст.
- Оновлено `CLAUDE.md` (стек: aiogram 3.x, SQLAlchemy/asyncpg/Alembic вже
  обрані; структура теки; правило синхронізації `docs/PROJECT_STATE.md` ↔
  `project_tg-task-manager.md`), `SKILL.md` (work sequence й DoD тепер
  посилаються на `docs/PROJECT_STATE.md`) та `HANDOFF.md` (Крок 4 спрощено).
