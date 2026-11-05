# Research prompt templates

Replace bracketed fields. These prompts select a stage; the skills provide the detailed process. No stage authorises automatic commits.

## Choose your agent

- **Codex:** use the `$develop-research-plan` and `$implement-and-verify` forms below.
- **Claude Code:** replace them with `/develop-research-plan` and `/implement-and-verify`. The repository's `.claude/skills` link provides discovery.
- **Explicit-reading fallback:** replace `Use $develop-research-plan` with “Read AGENTS.md and .agents/skills/develop-research-plan/SKILL.md and follow that guidance”. For the other skill, substitute `.agents/skills/implement-and-verify/SKILL.md`. Keep the remainder of the request. This works with file-capable agents even without skill discovery.

Start with the [setup instructions](../README.md#getting-started). If the Claude Code skills link does not work, use the explicit-reading fallback above. Save planning documents in `docs/`; read and run project files from the project root. The [chat suggestions](../README.md#organising-your-chats) are a flexible default. Use the resume prompt when starting a new chat.

## Brief and working instructions

```text
Use $develop-research-plan to help me develop docs/project_brief.md.
My initial idea is [idea], and intended output is [output or undecided].
Documentation is at [location or not yet available].
Start with focused questions; do not inspect record-level data or write
analysis code yet. Propose a brief for review and save it after I agree.
Stop after the brief.
```

After agreeing the brief:

```text
Read docs/project_brief.md and help me adapt AGENTS.md. Ask about unresolved
permissions, file locations, and researcher decision points. Present proposed
changes before saving them; retain the explicit-request commit policy.
```

## Study design

```text
Use $develop-research-plan to co-create docs/study_design.md from the agreed brief
and available documentation. Discuss consequential choices and relevant
limitations with me. Save the design after agreement; do not plan or code yet.
```

## Implementation plan

```text
Use $develop-research-plan to create docs/implementation_plan.md from our agreed
study design. Include manageable units, specific checks, decision points,
and final rerun requirements. Present it for agreement before saving.
Do not implement yet.
```

## Implement, verify, or fix

```text
Use $implement-and-verify to implement Unit [number] only. Run its checks,
record evidence, and stop. Do not commit.
```

```text
Use $implement-and-verify to verify Unit [number] against its requirements
and the study design. Report evidence and gaps; do not change analysis code.
```

```text
Use $implement-and-verify to investigate Unit [number]. Expected: [behaviour].
Observed: [behaviour]. Error or reproduction steps: [details]. Fix within
agreed requirements, rerun affected checks, and record the outcome.
Ask if a methodological decision is needed. Do not commit.
```

## Resume, revise, commit, and finish

```text
Read AGENTS.md, docs/project_brief.md, docs/study_design.md,
docs/implementation_plan.md, and the run instructions in README.md. Inspect the
project state without changing it. Summarise progress, evidence, open issues,
and uncommitted changes; identify the next eligible unit and wait for my choice.
```

```text
Review this proposed change: [change]. Explain consequences for the design,
plan, and completed work. Discuss options before adopting it. After agreement,
update affected sections and identify work to repeat. Do not implement yet.
```

```text
Review and commit [unit or scope], following AGENTS.md. Report incomplete
verification before committing. Include only intended changes, grouped
sensibly by purpose. If permissions block a commit, leave the files intact
and give me the commands to run myself. Do not widen access.
Report commits and remaining changes. Do not push.
```

```text
Use $implement-and-verify for the final documented rerun and review.
Check outputs, sensitivity analyses, interpretation, and research records.
Report evidence and gaps, preserving earlier outputs. Do not commit or publish.
```
