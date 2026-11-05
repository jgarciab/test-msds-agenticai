# Project working instructions

These are starter working instructions. Adapt the project-specific details after agreeing the project brief. Unfilled placeholders do not grant permission.

## Purpose and project documents

Keep the brief, study design, and implementation plan in `docs/`. Paths in these instructions are relative to the project root.

The research purpose will be recorded in `docs/project_brief.md`. If it does not yet exist, help the researcher develop it before beginning analysis. When available, read `docs/study_design.md` for methodological decisions and `docs/implementation_plan.md` for the current tasks and checks. Report missing or conflicting instructions rather than inventing decisions.

## Working with the researcher

- Use familiar research terminology and explain consequential choices. Avoid software-engineering jargon where plain language will do; explain necessary technical terms.
- Distinguish documented facts, proposals, assumptions, and unresolved questions.
- Ask before changing the research question, population, measurements, or analysis methods.
- Ask when uncertainty could affect research decisions, interpretation, data access, cost, or substantial work. For minor, reversible implementation choices, use reasonable judgment and briefly state relevant assumptions.
- Work on the requested stage or implementation step. Do not begin later steps until requested.
- Prefer simple, readable approaches suited to the research question. Keep files, dependencies, and computation to the minimum needed; preserve unrelated work.
- Ask before using paid services or starting unusually costly jobs. Explain the expected cost or resource use when known.

## Files and access

- Original inputs: `data/raw/`; derived datasets: `data/processed/`; source and access documentation: `data/README.md`. Treat original inputs as read-only. Document inputs held elsewhere.
- When suitable synthetic data are supplied, develop and check scripts using them first. Access real or sensitive data only when explicitly authorised and within the approved environment. Synthetic-data checks do not replace validation on real data.
- Keep numbered analysis notebooks in the project root, reusable code in `src/`, figures in `results/figures/`, and tables in `results/tables/`. Add a project-named package under `src/` if needed. Run analysis from the project root and document commands in `README.md`.
- Data, outputs, and settings are trackable by default. Before staging, inspect intended files, including notebook outputs and local settings, for sensitive information, credentials, personal paths, and large files. Do not commit sensitive or large datasets.
- Permitted data and services: [specify]. Do not upload data or use external services without authorisation.
- Do not delete existing work, publish results, or push changes without explicit instruction.

These instructions do not enforce access restrictions. Shared defaults are in `.claude/settings.json` and `.codex/config.toml`; see `docs/permissions.md` for setup and checks. Internet access is enabled, but this does not authorise sharing data or using services.

## Software environment

- Before installing software, inspect the project's environment files and available tools. Use an existing suitable environment where possible.
- Follow the project's declared language versions and dependencies. Do not introduce a version requirement without explaining why it is needed.
- Establish where commands actually execute: the researcher's computer, a local virtual machine, or a cloud environment. Record the operating system, language version, dependencies, and run commands in `README.md`. Report uncertainty rather than assuming that file access implies execution on the same system.
- Approved software download sources: [agree package registries and any language-runtime distribution sources during setup]. Once a source is agreed, routine package downloads from it do not need a separate permission request. Ask before using an unlisted source. Software-download permission does not authorise uploading research data or override environment access controls.
- Keep installed environments out of Git. Record dependencies and versions using files suited to the chosen language, such as `pyproject.toml` with a lockfile, `requirements.txt`, or `renv.lock`. Do not use `environment.yml`. Use the project environment consistently for analysis and checks.
- Do not reuse an installed environment across incompatible operating systems. When files are shared between the host and a virtual machine, keep their installed environments separate; do not overwrite the researcher's environment.
- Report where verification ran. Execution in a virtual machine does not also verify the researcher's local setup. Document any local rerun still needed.

## Verification and reporting

- Check each implemented step against its agreed requirements, including substantive correctness.
- Use small examples with known answers where useful; distinguish these from checks of plausibility on the supplied data.
- Report what ran, the evidence obtained, failures, and checks not performed. Do not claim success from code inspection alone. Keep agent checks separate from researcher review; do not mark researcher review complete without it.

## Research records

Record enough to understand decisions, inspect evidence, and reproduce the analysis. Update the existing documents rather than creating a separate log for every task.

- `docs/study_design.md`: consequential methodological decisions, their rationale, assumptions, and unresolved research questions. Reflect changes to project scope in `docs/project_brief.md`.
- `docs/implementation_plan.md`: step completion, checks run and their results, failures, and unresolved implementation issues.
- `README.md`: input versions and locations, software requirements, and commands needed to rerun the analysis.
- In a short AI-use section of `README.md`, record the tasks assisted by AI, the extent of automation, and what the researcher reviewed. Record the provider, model identifier/version, access date, and application or API used, where available. Note relevant configuration, customisation, and whether persistent memory or previous conversation context was used. Mark unavailable details as unknown; do not guess.
- Preserve the versions of project instructions, skills, and substantive prompts used. Reference existing files and Git revisions rather than duplicating them. For complex agent interactions, document the workflow, configuration, and relevant code when a complete prompt record is impractical.
- If AI directly produces research observations or materials, such as annotations, simulated responses, or experimental stimuli, agree on a recording location before running it. Additionally preserve exact supplied prompts and instructions, input versions, raw outputs, available model settings, run counts, post-processing rules, and human validation methods and results. Record these separately for each model/task where they differ. Keep code used to make model calls and process responses.
- Record which data were provided to AI services and how sensitive information was protected. Ask the researcher to supply relevant permissions and disclosures, including funding or in-kind model access; do not infer consent, approval, or competing interests. Do not put sensitive information or credentials in shared logs or Git.

Scale the record to AI's role in the research. Routine coding assistance does not require a transcript of every interaction; direct production of research evidence requires fuller documentation. Explain inapplicable items. Clearly distinguish observed results from expectations and checks that have not been run. Recording settings supports transparency but does not guarantee identical model outputs on a rerun.

This guidance draws on [Feuerriegel et al. (2026), GUIDE-LLM, Table 1 and practical considerations](https://doi.org/10.1038/s41562-026-02492-7), adapted for this research workflow rather than reproduced as a full reporting checklist.

## Git checkpoints

- Create commits only when explicitly requested. Permission to edit or verify files does not imply permission to commit or push.
- Follow SoDa GitHub Flow: work on a short-lived branch such as `feature/short-name` and propose changes to `main` through a pull request. Use Conventional Commits (`feat:`, `fix:`, `docs:`, or `chore:`) with concise, imperative titles.
- When asked to commit, group changes by purpose and commit them separately in a logical order. Keep relevant verification with each change; avoid splitting closely related work unnecessarily.
- Review and stage only the intended changes. Preserve unrelated work and report any verification that remains incomplete.

- If permissions block a requested commit or an instruction/settings update, preserve the work and give the researcher the changes or commands to apply manually. Do not widen access or disable restrictions to complete the task.
