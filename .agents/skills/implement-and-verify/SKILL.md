---
name: implement-and-verify
description: Implement, verify, or debug a requested research-analysis unit against an agreed study design and implementation plan. Also supports final analysis reruns and evidence review; use after research requirements are established.
---

# Implement and verify research work

Treat paths as relative to the project root. Read `AGENTS.md`, the relevant `docs/study_design.md` sections, and the requested unit and dependencies in `docs/implementation_plan.md`. Inspect existing code and recorded evidence. Follow the requested mode; do not turn a verification request into permission to change analysis code.

If the requested unit, required inputs, or methodological choices are missing, resolve that gap with the researcher before dependent work. Preserve the agreed scientific requirements and project access boundaries.

## Implement a unit

Make a small, readable set of changes for one requested unit. Reuse existing files and protect source data. Run the agreed checks and inspect their outputs. Explain any additional check needed to address a material correctness gap. Record actual completion evidence and leave unmet criteria open. Record work as awaiting researcher review until that review happens. Stop after the unit.

## Verify a unit

Review requirements against evidence rather than accepting previous completion claims. Where useful, use a known-answer example, manual calculation, or separate reference approach instead of repeating the implementation's logic. Separate computational correctness, agreement with the research design, plausibility, and robustness. Report passed, failed, and unchecked requirements. Do not modify analysis code during a verification-only request; report findings first.

## Fix a bug

Establish expected versus observed behaviour and reproduce the problem where possible. Distinguish code defects from data problems and methodological uncertainty. Fix within the agreed requirements; do not weaken checks or alter selection or methods merely to remove a failure. Ask about substantive changes. Use a targeted regression check when useful and rerun affected checks and dependent outputs. Record cause, remedy, and evidence.

## Final rerun and review

Follow the documented setup and run order, using a fresh environment and separate outputs where feasible and permitted. Preserve prior results for comparison. Check expected outputs, cross-unit consistency, agreed sensitivity analyses, interpretation, and required research records. Report any deviation from a fresh setup, unavailable input, unrun check, or discrepancy. A successful rerun does not by itself establish scientific validity.

## Completion

Update the existing plan's evidence and relevant run instructions rather than creating extra logs by default. Report what changed, what ran, expected versus observed results, limitations, and pending researcher decisions. Follow `AGENTS.md` for AI-use records and commits. Do not proceed to another unit, commit, push, or publish without instruction.
