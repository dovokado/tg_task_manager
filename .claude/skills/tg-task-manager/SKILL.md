# SKILL: TG Task Manager — workflow

> The project workflow. Claude reads this FIRST, before writing code or docs.
> This file is in English; project documentation it produces is in Ukrainian.

## When to apply
Any change to code or documentation in this project.

## Work sequence
1. Read the project `CLAUDE.md` + this `SKILL.md` + `project_tg-task-manager.md` (state).
2. Phase 1: confirm understanding of the request.
3. Phase 2: analysis + plan → confirmation (for T2).
4. Make the changes.
5. Sync the documentation (see below).
6. Deploy-summary + DoD checklist.

## Code ↔ documentation sync
- Logic/model/API change → update the relevant docs in the **same** iteration.
- Documentation is written in Ukrainian; code comments in Ukrainian per the language rule.

## Definition of Done (hard gate)
Don't say "done" until **every** item is met and verified:
- [ ] Code works (run / tested, not just written)
- [ ] `BUGS.md` updated (new bugs logged / fixed ones marked)
- [ ] `CHANGELOG.md` updated
- [ ] Documentation is in sync with the code
- [ ] `project_tg-task-manager.md` updated (status / backlog)

## Decision log (ADR) — only when needed
If a decision was made where **rejected alternatives** are worth remembering,
create a short record in `docs/decisions/NNN-<topic>.md`
(context → decision → rejected options → consequences). Write it in Ukrainian.

## Deploy-summary (closing format)
- What was done (1-3 lines).
- Which files changed.
- DoD checklist (above) — every item.
- What's left / risks (if any).
