# ODISSEI SoDa Agentic Research Project Starter

A starting point for research with AI agents, with you in control. Clarify your question, agree on a plan, and build an analysis you can explain and check.

The template works with different datasets, programming languages, and research methods.

## Template structure

| Location | What goes here |
|---|---|
| Project root | Numbered analysis notebooks, such as `01_exploration.ipynb`, `.qmd`, or notebook-style `.py` files. |
| [`data/`](data/README.md) | Original data in `raw/`, derived data in `processed/`, and information about sources and access in `data/README.md`. |
| `src/` | Reusable code. Add a project-specific package if needed. |
| `results/figures/` | Generated figures. |
| `results/tables/` | Generated tables. |
| `docs/` | Planning documents and other documentation. |

Run analyses from the project root and keep original data unchanged. Data, results, and shared settings can be tracked in Git by default. Check for sensitive information, credentials, and large files before committing.

Record dependencies and versions using files appropriate for your language, such as `pyproject.toml` with a lockfile, `requirements.txt`, or `renv.lock`. Do not use `environment.yml`.

### Files that guide the agent

| File or folder | Purpose |
|---|---|
| [Permission settings](docs/permissions.md) | Explains what the agent can access and how to check the settings. |
| [AGENTS.md](AGENTS.md) | Working rules for the agent: decisions to discuss, checks to run, records to keep, and when to commit. Adapt this to your project. |
| [CLAUDE.md](CLAUDE.md) | Points Claude Code to the shared instructions in `AGENTS.md`. |
| [Research prompt templates](templates/research_prompts.md) | Example prompts for planning, coding, checking, and resuming work. |
| [Planning skill](.agents/skills/develop-research-plan/SKILL.md) | Guides discussion of the project brief, study design, and implementation plan. |
| [Document templates](.agents/skills/develop-research-plan/assets/templates/) | Starting structures for those three documents. |
| [Implementation skill](.agents/skills/implement-and-verify/SKILL.md) | Guides coding, testing, debugging, and final review. |
| `.claude/skills` | Links Claude Code to the same shared skills. |

Skills give the agent a process to follow; prompts tell it what to work on next. The prompts below explicitly ask the agent to read the skill files, so they also work when automatic skill discovery is unavailable. On Windows, the `.claude/skills` link may appear as a text file; these explicit-reading prompts still work. The agent needs access to the project files.

Save agreed planning documents as `docs/project_brief.md`, `docs/study_design.md`, and `docs/implementation_plan.md`. Keep open questions visible rather than filling gaps with assumptions.

## Getting started

1. On GitHub, choose **Use this template → Create a new repository**, then open your new repository locally. Alternatively, copy the files into a new local Git repository.
2. If using a desktop app, open the folder as a project or give the agent access to it.
3. Read `AGENTS.md` and follow the [permission setup and checks](docs/permissions.md). The included settings allow internet and temporary-file access while restricting access to other personal folders.
4. Add the data documentation the agent needs. Add datasets once you have decided what the agent may access and what may be committed or shared. Use synthetic data first where possible.

## 1. Design: agree on the question and the work

### Develop a project brief

The brief captures your research idea, intended output, available resources, and practical limits. Start with this prompt, replacing the bracketed text:

```text
Read AGENTS.md and .agents/skills/develop-research-plan/SKILL.md.
Help me develop docs/project_brief.md.

My initial idea is [idea].
The intended output is [output or undecided].
Documentation is at [location or not yet available].

Start by asking me a few focused questions.
Do not inspect record-level data or write analysis code yet.
Propose a brief for me to review. Save it in docs/ once we agree.
Stop after completing the brief.
```

### Adapt the working instructions

Once the brief is agreed, make the agent's instructions specific to your project:

```text
Read docs/project_brief.md and help me adapt AGENTS.md.
Use docs/ for the brief, study design, and implementation plan.
Ask about unresolved permissions, file locations, and decisions
that need my review. Show me proposed changes before saving them.
Keep the rule that commits require an explicit request.
```

### Agree on the study design

The study design explains how you will answer the question: which data or materials you will use, how you will analyse them, and what conclusions the work can support.

```text
Read AGENTS.md and .agents/skills/develop-research-plan/SKILL.md.
Use docs/project_brief.md and the available documentation to help
me develop docs/study_design.md.
Discuss the main methodological choices and limitations with me.
Save the design in docs/ after we agree. Do not plan the coding yet.
```

### Make an implementation plan

The implementation plan turns the agreed design into small tasks, each with a clear output and checks to confirm it works. Each numbered task is called a “unit” in the plan and prompts.

```text
Read AGENTS.md and .agents/skills/develop-research-plan/SKILL.md.
Create docs/implementation_plan.md from docs/study_design.md.
Break the work into manageable tasks with clear outputs, checks,
and decisions that need my input. Include a full rerun and final review.
Show me the plan before saving it in docs/. Do not implement yet.
```

## 2. Implementation: build and check the analysis

Work through the plan one task at a time. Review the changes and checks before moving on.

```text
Read AGENTS.md and .agents/skills/implement-and-verify/SKILL.md.
Use docs/study_design.md and docs/implementation_plan.md.
Implement Unit [number] only. Run its checks, record the results
in the plan, and stop for my review. Do not commit.
```

When all tasks are complete, rerun the analysis and review the results:

```text
Read AGENTS.md and .agents/skills/implement-and-verify/SKILL.md.
Use docs/study_design.md, docs/implementation_plan.md, and README.md
for the final rerun and review. Preserve earlier outputs for comparison.
Report what ran, what the checks showed, and anything you could not verify.
Update the plan with the evidence. Do not commit or publish.
```

The [research prompt templates](templates/research_prompts.md) include further examples for debugging, resuming work, revisions, commits, and final review.

## Organising your chats

Separate chats can help keep the work manageable:

| Chat | What to do |
|---|---|
| 1 | Develop the brief, adapt `AGENTS.md`, and agree on the study design. |
| 2 | Turn the design into an implementation plan. |
| 3 | Implement and check the analysis, one task at a time. |
| 4 | Rerun the analysis and review the results. |

Use this sequence when helpful. Start a new chat sooner if the conversation becomes cluttered with abandoned approaches or conflicting instructions.

Before switching, update the project documents with agreed decisions, checks completed, and open questions. A fresh chat can help with review, but it does not replace checking the work.

## For template maintainers

Enable **Template repository** under **Settings → General** to make this repository available as a GitHub template. Projects created from it are independent copies; later changes to the template will not automatically appear in them.

Keep actual research data and project-specific decisions out of the template. Choose a licence before offering it for general reuse.

This workflow builds on the [SoDa AI-assisted research programming workshop](https://github.com/sodascience/workshop-ai-assisted-research-programming). The instructions and skills were developed for this starter; no external skill frameworks are bundled.

The guidance on documenting AI use in `AGENTS.md` draws on [Feuerriegel et al. (2026), GUIDE-LLM](https://doi.org/10.1038/s41562-026-02492-7).
