# What can the AI agent access?

This template includes settings for Claude Code and Codex. They let the agent work on your project while limiting access to other files on your computer.

With these settings, the agent can:

- Read and edit analysis files in the project folder.
- Run analysis code and use temporary files.
- Access the internet, for example to download packages or public data.

Access to unrelated personal files is restricted, with exceptions for software and temporary files needed to run commands. The settings use a **sandbox**: a restricted environment that limits what commands can access. They disable requests to retry blocked commands outside it. Existing personal or institutional settings can affect the result, so check the setup below.

`AGENTS.md` gives the agent working instructions. The settings apply access restrictions. You can change these defaults; they do not replace your institution's requirements.

## Getting started

Open the project folder in your agent and review its files before accepting any request to trust the project. The settings are already included:

| Agent | Settings file | How to check |
|---|---|---|
| Claude Code | [`.claude/settings.json`](../.claude/settings.json) | Type `/sandbox` to check that the sandbox is enabled. |
| Codex | [`.codex/config.toml`](../.codex/config.toml) | Type `/status` to inspect permissions. Codex loads project settings only after you trust the project. |

Use an up-to-date version. Codex permission profiles are still in development; older `sandbox_mode` settings can override this profile. If the checks below fail, use `/debug-config` in Codex to identify conflicting settings. Claude Code needs version 2.1.257 or later for the file-read restriction. Its sandbox works on macOS, Linux, and Windows through WSL2 (a Linux environment for Windows). If the sandbox is unavailable, these settings stop Claude Code rather than letting commands run without it.

## Try it before adding research data

Start a new session and ask the agent to:

1. Read the project README and create a small test file in the project.
2. Run a simple R or Python calculation and create a temporary file.
3. Download a public webpage using code.
4. Try reading a harmless test file you placed outside the project, in another personal folder. This should be blocked. Ask it to try both its file-reading tool, if available, and a command.

Use a dummy file for the last check, never a real confidential document. Do not grant access to that folder during the test. Ask the agent to report what worked, what was blocked, and what it could not check, then remove the test files.

If something fails, ask the agent to explain why before changing permissions. An R library or Python installation may need access to a specific location. Grant only the access needed. Existing personal or institutional settings can override these defaults; ask for help checking them rather than turning off the restrictions.

## If a commit or settings change is blocked

The Codex profile protects Git's internal files and the `.agents/` and `.codex/` folders. This can prevent the agent from making commits or updating skills and settings, even when you ask it to. Ask it to show the changes or Git commands, then apply them yourself in your own editor or terminal. You can still review and save analysis work without removing these protections.

The rule to leave original data unchanged is a working instruction. These settings do not make `data/raw/` technically read-only.

## Before sharing files

Internet access does not mean you have permission to upload research data. Only provide data to AI services when your project's agreements and institutional rules allow it. Files the agent reads may be sent to its AI provider.

Data and settings can be included in Git by default. Review them, including saved notebook outputs, before committing or sharing. Keep sensitive or large datasets and passwords or API keys out of Git. Files named `.env`, commonly used for credentials, are already excluded.

These settings concern local commands and file access. Connected services and browser tools have separate permissions. Cloud versions of the agents may also use different settings, so check their access controls separately.

For technical details, see the [Claude Code documentation](https://code.claude.com/docs/en/sandboxing) and [Codex documentation](https://learn.chatgpt.com/docs/permissions).
