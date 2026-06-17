# INSTALL — runbook for Claude

> You are Claude Code. The user pointed you at this file to install the
> "CLAUDE Starter Kit". Follow these steps in order.
>
> **Communication rules (apply for the whole installation):**
> - Talk to the user **in Ukrainian**. Explain every step: what you will do and why.
> - Before ANY action that writes or modifies files/settings, state exactly what
>   will change and **wait for the user's confirmation** ("так"/"ні").
> - If a target file already exists, show its current state and propose a merge
>   instead of overwriting. Never clobber the user's existing config silently.
> - Report honestly: if a step fails or is skipped, say so.

---

## Step 0 — Detect environment

1. Determine the OS (Windows / macOS / Linux) and the Claude home directory:
   - Windows: `C:\Users\<user>\.claude\`
   - macOS / Linux: `~/.claude/`
2. Confirm the path to the kit folder (the folder containing this `INSTALL.md`),
   so you know where `global/` and `templates/` live.
3. Tell the user, in Ukrainian, the detected OS and the two paths you will use.
   Ask them to confirm before continuing.

---

## Step 1 — Verify Claude Code is installed

- Confirm the user is running inside Claude Code (they are, since you're reading this).
- If `~/.claude/` does not exist yet, it will be created in Step 2 — note that.

---

## Step 2 — Install the global behavior layer

This makes Claude read the protocol on every session start, in every project.

1. **Global protocol file** → copy `global/CLAUDE.md` (in this kit) to
   `<claude-home>/CLAUDE.md`.
   - If `<claude-home>/CLAUDE.md` already exists: do NOT overwrite. Show its
     contents, and propose prepending the kit's protocol above the existing text.
     Confirm with the user first.

2. **Memory index + memory files** → copy:
   - `global/MEMORY.md` → `<claude-home>/memory/MEMORY.md`
   - `global/memory/*.md` → `<claude-home>/memory/`
   - Create the `memory/` directory if missing.
   - If `MEMORY.md` already exists: merge the index sections rather than overwrite.

3. Explain to the user (in Ukrainian) what each file does:
   - `CLAUDE.md` — behavior protocol (phases, complexity tiers, fast-mode, safety).
   - `MEMORY.md` — the index Claude loads each session.
   - `memory/*.md` — persistent facts (identity, language, working rules).

---

## Step 3 — Fill in the user's personal memory

Work through these with the user, in Ukrainian, and edit the files in
`<claude-home>/memory/`:

1. `user_identity.md` — ask the user their name, roles, email; write them in.
   Keep surnames in their original spelling (no transliteration).
2. `user_language.md` — already set to Ukrainian; confirm that's correct.
3. `feedback_confirm_before_changes.md` — no edit needed; just explain it governs
   the "confirm before acting" behavior.

After editing, ensure each is referenced by one line in `MEMORY.md`.

---

## Step 4 — Set up project templates (per project)

Explain: these make Claude work well *inside a specific project*. Do this for each
project the user names (you can also just install the templates and explain how to
reuse them later).

For a given project root:
1. Copy `templates/CLAUDE.project.md` → `<project-root>/CLAUDE.md`, then help the
   user fill Language / Stack / Configs / Important / Structure.
2. Copy `templates/SKILL.md` → `<project-root>/.claude/skills/<name>/SKILL.md`
   (or simpler: `<project-root>/docs/SKILL.md` referenced from the project CLAUDE.md).
3. Copy `templates/project_NAME.md` → `<claude-home>/memory/project_<name>.md` and
   add a one-line reference under "Projects" in `MEMORY.md`.

Reminder to state to the user: **project documentation is written in Ukrainian**
(BUGS.md, CHANGELOG.md, notes, the project state file), while skill/operational
files stay in English.

---

## Step 5 — Obsidian + MCP (from scratch)

Guide the user through this interactively, in Ukrainian, confirming each action.

> **Why MCP, not direct file edits:** the MCP server talks to Obsidian through its
> official Local REST API — it sees the vault structure, frontmatter, tags and links
> correctly and won't desync the cache the way raw `.md` edits can.

1. **Install Obsidian** — https://obsidian.md . Create a new vault
   (e.g. `Knowledge`); record the full vault folder path.
2. **Enable the Local REST API plugin** — Obsidian → Settings → Community plugins →
   enable community plugins → Browse → install **"Local REST API"** → Enable.
   In its settings, copy the **API Key** and note the port
   (typically `27124` HTTPS / `27123` HTTP).
3. **Add the MCP server to Claude Code.** The exact npm package name evolves —
   search for a current "obsidian mcp server" that uses the Local REST API and
   check its README for the exact env var names. Typical shape:
   ```
   claude mcp add obsidian \
     --env OBSIDIAN_API_KEY=<API_KEY> \
     --env OBSIDIAN_HOST=127.0.0.1 \
     --env OBSIDIAN_PORT=27124 \
     -- npx -y <obsidian-mcp-package>
   ```
   Or add it manually to `.mcp.json`:
   ```json
   {
     "mcpServers": {
       "obsidian": {
         "command": "npx",
         "args": ["-y", "<obsidian-mcp-package>"],
         "env": {
           "OBSIDIAN_API_KEY": "<API_KEY>",
           "OBSIDIAN_HOST": "127.0.0.1",
           "OBSIDIAN_PORT": "27124"
         }
       }
     }
   }
   ```
4. **Verify:** Obsidian must be running (the API works only while Obsidian is open).
   In Claude Code run `/mcp` — `obsidian` should show "connected". Then ask Claude
   to list the vault's notes; it should return real content.

Common issues to tell the user about:
- connection refused → Obsidian not running, or Local REST API disabled
- 401 unauthorized → wrong API key
- SSL/cert error → switch to HTTP port 27123 or allow the self-signed cert per README
- server missing from `/mcp` → check `.mcp.json` syntax and that `npx` is on PATH

---

## Step 6 — Final check

Walk the user through this checklist (in Ukrainian) and confirm each item:

- [ ] `<claude-home>/CLAUDE.md` contains the global protocol
- [ ] `<claude-home>/memory/` has MEMORY.md + the memory files, personalized
- [ ] At least one project has its own `CLAUDE.md` (+ SKILL.md, project_*.md)
- [ ] Obsidian installed, vault created, MCP connected and verified via `/mcp`

Then tell the user, in Ukrainian, that setup is complete and how to start: just
open Claude Code in any project — the protocol and memory load automatically.
