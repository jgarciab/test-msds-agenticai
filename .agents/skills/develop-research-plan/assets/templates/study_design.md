# Study design

Status: Draft / Agreed with open questions / Agreed · Date: [YYYY-MM-DD]

Save the completed design as `docs/study_design.md`. Paths are relative to the project root.

Based on `docs/project_brief.md`. Replace bracketed text and label unresolved choices. This document explains the research methods; programming tasks belong in `docs/implementation_plan.md`.

Use the common sections below, then address the additional considerations relevant to your design. Write “Not applicable” with a short reason where appropriate. This is a starting point, not a substitute for method-specific guidance. Keep proposals, agreed decisions, and open questions distinct.

## 1. Research question, objectives, and intended claims

- **Question:** [What do you want to understand?]
- **Objectives:** [What would answering the question contribute?]
- **Intended claims:** [Describe, interpret, explore, explain, predict, or estimate causal effects? Specify hypotheses if relevant, distinguishing prior hypotheses from exploratory questions.]
- **Scope of interpretation:** [To whom, where, and when might the findings apply? What claims would the design not support?]

## 2. Study approach and rationale

[Describe and justify the approach: for example, secondary-data analysis, survey, experiment, interviews, ethnography, document analysis, or mixed methods. Explain how it connects the question to evidence. Identify any theoretical framework and major assumptions. For mixed methods, explain how the components inform each other.]

## 3. Population, sampling, and data

- **Population or setting:** [Target population, cases, geographic scope, and observation period.]
- **Units:** [Units of sampling, observation, and analysis; explain differences and repeated or nested observations.]
- **Sources or collection:** [Existing data locations, versions, and documentation, or recruitment and data-collection procedures. Distinguish documented properties from those requiring inspection.]
- **Selection and coverage:** [Sampling rationale, intended sample size and justification, inclusion/exclusion rules, and differences between available and target populations.]
- **Preparation:** [Linking rules and dates, cleaning, missing data, non-response, or attrition where relevant. Explain decisions that could change who or what is represented.]

## 4. Concepts, measurements, and research materials

| Concept or material | Measurement, source, or interpretation approach | Rationale or uncertainty |
|---|---|---|
| [Concept] | [How it is measured] | [Why; what remains open] |

[Specify variable roles only where relevant; a descriptive or qualitative study need not have an outcome and predictors. Define derived measures, reference groups, coding frameworks, instruments, stimuli, and spatial or temporal definitions as needed. Discuss measurement validity, reliability, and ambiguity.]

## 5. Analysis strategy and justification

[Describe preparation, exploration, and the main analysis in conceptual terms. Explain the comparisons, models, interpretive procedures, or synthesis methods and why they answer the question. Identify relevant assumptions, how uncertainty will be represented, and how evidence will support conclusions. Avoid implementation code or a programming task breakdown.]

## 6. Quality checks, uncertainty, and robustness

- **Data and materials:** [What must be checked about coverage, linking, dates, measurement, or collection?]
- **Implementation correctness:** [What calculations or processing steps need known-answer examples or other independent checks? Detailed executable checks belong in the implementation plan.]
- **Scientific credibility:** [How will assumptions, alternative explanations, uncertainty, and relevant quality criteria be assessed?]
- **Sensitivity:** [Which alternative selections, definitions, analytical choices, or interpretations could change the conclusions?]

## 7. Ethics, access, and participant protection

[Record permissions, consent and ethics-review requirements where applicable; data minimisation, storage, access, and sharing restrictions; and risks to participants or represented groups. Explain what information may be supplied to AI services, researcher oversight, and how AI-generated research material will be validated if used. Mark unconfirmed permissions as unresolved. Refer to the project brief and working instructions rather than duplicating operational details.]

## 8. Expected outputs and reproducibility

| Output | What it contains | Connection to the question |
|---|---|---|
| [Table, figure, themes, report, or other output] | [Description] | [Purpose] |

[Identify the final deliverable. Specify what must be preserved to reconstruct or assess the work: input versions, analysis procedures and code, software, methodological decisions, and relevant AI-use records. Explain restrictions on sharing and what can be provided instead. For qualitative work, distinguish transparency of the analytic process from an expectation of identical interpretations.]

## 9. Limitations, decisions, and agreement

[Identify major threats to interpretation and generalisation, including selection, measurement, practical constraints, and unresolved assumptions. If using synthetic data, explain what the exercise demonstrates and why results are not evidence about the real population.]

| Decision | Choice and rationale | Status / information needed |
|---|---|---|
| [Decision] | [Choice] | [Agreed / Provisional / Open] |

### Design review

- [ ] The question, objectives, and scope of claims are clear.
- [ ] The approach, selection, measurements or materials, and analysis are justified.
- [ ] Relevant quality checks, ethics, and access requirements are addressed.
- [ ] Expected outputs and reproducibility needs are specified.
- [ ] Relevant additional design considerations below have been addressed.
- [ ] Open questions are identified, including what must be resolved before dependent work begins.

**Researcher agreement:** [Record agreement, date, and any conditions. AI proposals do not constitute researcher agreement.]

When methods change, explain why, update the affected sections and implementation plan, and revisit dependent work. Distinguish changes made before examining results from those informed by results. Record any preregistration or protocol and deviations where applicable.

## 10. Additional design considerations

Address applicable prompts in the relevant sections above, then remove unused guidance. These examples are not exhaustive; add method-specific requirements where needed.

- **Observational quantitative research:** [Dependence or clustering, weighting, uncertainty, and model assumptions. For causal claims, specify the effect of interest, identification strategy, confounding, and assumptions needed to interpret the estimate causally.]
- **Experiments:** [Assignment and comparison conditions, sample-size rationale, blinding where relevant, adherence, exclusions, outcome timing, and participant protections.]
- **Qualitative research:** [Case or participant selection, researcher positionality and relationships, collection procedures, analytic tradition, reflexivity, and appropriate credibility checks. Do not assume agreement between coders is required for every approach.]
- **Prediction:** [Training and evaluation separation, leakage prevention, performance criteria, calibration where relevant, and generalisation to the intended setting.]
- **Surveys and longitudinal research:** [Recruitment, questionnaire design, non-response, weights, attrition, repeated observations, timing, and missing-data strategies.]
- **Computational text analysis or AI-generated measurements:** [Corpus construction, annotation procedures, human validation, model/prompt versions, processing rules, and risks of systematic measurement error or contamination.]
