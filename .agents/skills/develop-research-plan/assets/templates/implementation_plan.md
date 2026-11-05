# Implementation plan

Status: Draft / Agreed / Needs revision · Date: [YYYY-MM-DD]

Save the completed plan as `docs/implementation_plan.md`. Paths below are relative to the project root. A unit is one numbered task. Keep the plan proportionate to the project; use only the stages and detail needed.

Based on `docs/study_design.md`. Define manageable steps with observable outputs and checks. Include no implementation code. Do not resolve open methodological questions silently.

## 1. Project overview

- **Project:** [Name and brief purpose.]
- **Study design:** [docs/study_design.md and agreed version or date.]
- **Language and software environment:** [Language, required software, and how the environment is recorded.]
- **Data and documentation:** [Locations and versions; access restrictions.]
- **Final deliverables:** [Analysis outputs and instructions for reproducing them.]

### Working principles

- Complete one requested unit at a time, in dependency order.
- Aim for units that can be reviewed in approximately 5–15 minutes; computation may take longer. Split work that is too large to understand and review together.
- Give each unit one clear objective and a small, reviewable set of changes. Prefer working on one file where practical, but keep closely related implementation and verification changes together. Several units may develop the same file.
- Keep code readable and dependencies minimal. Reuse existing work and preserve unrelated content.
- Verify substantive correctness against the agreed requirements, not merely whether the code runs.
- Do not silently resolve open methodological choices. Ask the researcher before changing the agreed design.
- Review verified changes before saving a Git checkpoint. Create commits only when explicitly requested, following `AGENTS.md`.

## 2. Project organisation

[Start with the layout in README.md: planning documents in docs/, notebooks in the project root, reusable code in src/, data in data/, and outputs in results/. Describe any additions, run order, which files belong in Git, and how original data remain protected.]

## 3. Implementation overview

Group related units into stages, such as data preparation and analysis. Number units within stages (1.1, 1.2, 2.1). Arrange them so each uses only available inputs and completed dependencies.

| Unit | Purpose and output | Depends on | Status |
|---|---|---|---|
| 1.1 | [Task and output] | [None or earlier unit] | Not started |
| 1.2 | [Task and output] | [Earlier unit] | Not started |

## 4. Implementation units

Repeat the stage and unit structure below as needed. Write requirements and checks before implementation; fill in completion evidence after execution.

### Stage 1 — [Stage name]

**Stage objective:** [How this stage contributes to the study design.]

#### Unit 1.1 — [Action and object]

**Research purpose**

[One objective and its connection to the study design.]

**Dependencies and inputs**

[Prior units, files, relevant variables, input versions, and decisions required.]

**Implementation requirements**

[Specify concrete behaviour, including selection, linking, or calculation rules. Describe what must happen without writing implementation code.]

**Deliverable**

[Files to create or modify, expected contents, and resulting outputs.]

**Verification requirements**

[Specify observable checks, expected results, and failure conditions. Distinguish small examples with known answers from checks requiring inspection of the supplied data. Avoid verifying the calculation solely by repeating its own logic.]

**Researcher decision point**

[Any unresolved choice that blocks this unit, what information is needed, and when to ask; otherwise None.]

**Completion criteria**

- [ ] Changes have been reviewed and can be explained.
- [ ] The unit runs without unexplained errors.
- [ ] Required checks have been run and their results inspected.
- [ ] Failures and blocking questions have been resolved; remaining limitations are recorded.
- [ ] Completion evidence is recorded below.

**Completion evidence**

[Keep unchecked criteria open. Distinguish agent checks from researcher review; do not mark that review complete without it. Record commands or checks run, observed results, remaining issues, and researcher review. Record a Git checkpoint if requested and made; otherwise state that changes remain uncommitted.]

## 5. Full rerun and final review

- **Execution:** [How to run the complete analysis from documented inputs in a fresh environment.]
- **Expected outputs:** [Tables, figures, and other deliverables, with locations.]
- **Checks across units:** [How to check that intermediate outputs and final results are consistent.]
- **Reproducibility:** [Input versions, software requirements, random seeds where relevant, and run instructions to preserve.]
- **AI-use records:** [Check the records required by `AGENTS.md`: AI's role, researcher oversight, available model and access details, and versions of instructions, skills, and substantive prompts. If AI produces research observations or materials, also check the agreed records of inputs, outputs, settings, post-processing, and validation. Reference their locations rather than duplicating them; mark unavailable details as unknown.]
- **Scientific review:** [Sensitivity analyses and interpretation checks required by the study design.]

### Final completion criteria

- [ ] All required units meet their completion criteria.
- [ ] The full analysis runs in the documented order and produces the expected outputs.
- [ ] Results and sensitivity analyses have been reviewed against the agreed design.
- [ ] Another researcher has sufficient instructions and permitted inputs to rerun the analysis.
- [ ] Required AI-use records are present, with unavailable or inapplicable details identified.
- [ ] Remaining limitations and incomplete checks are clearly reported.
- [ ] Changes have been reviewed; Git checkpoints have been made if requested.

**Final evidence:** [Record the full rerun, checks, review, and unresolved issues.]

## 6. Open issues and revisions

| Affected units | Issue or proposed change | Reason | Researcher decision |
|---|---|---|---|
| [Unit numbers] | [Change] | [Why] | [Open / Agreed / Rejected] |

When a revision is needed, explain its consequences for the design and completed work. Obtain agreement for substantive changes, update affected sections without rewriting unrelated content, and revisit any units whose correctness is affected.

## 7. Plan agreement

Before implementation, confirm that:

- [ ] The plan covers the agreed study design and intended outputs.
- [ ] Units are manageable, with clear requirements, deliverables, and dependencies.
- [ ] Each unit has concrete verification requirements.
- [ ] Open methodological decisions have explicit researcher decision points.
- [ ] The final rerun and scientific review are included.

**Researcher agreement:** [Record agreement, date, and any conditions. AI proposals do not constitute researcher agreement.]
