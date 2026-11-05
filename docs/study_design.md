# Study design

Status: Agreed · Date: 2026-11-05

No `docs/project_brief.md` exists; at the researcher's request, the purpose is recorded in section 1 instead. This document records design decisions only; programming tasks belong in `docs/implementation_plan.md`.

## 1. Purpose and intended claims

- **Question:** Can an interactive simulation help students see how model complexity, sample size, and noise lead to underfitting and overfitting?
- **Objective:** A marimo teaching app that runs entirely in the browser (WebAssembly, WASM) and is deployed with a GitHub Action.
- **Intended claims:** None about real data. The app demonstrates a well-known statistical phenomenon on simulated data; it is teaching material, not a study.
- **Audience:** Data-science master's students who already know linear regression.

## 2. Approach

Simulation-based demonstration: students fit ordinary least-squares polynomials of varying degree to noisy samples from a known curve, then compare the fit with the true curve and with held-out test points. Only numpy, matplotlib, and marimo are used, all of which run in the browser.

## 3. Simulated data

- **Process:** y = sin(2πx) + ε, with x ~ Uniform(0, 1) and ε ~ Normal(0, σ²).
- **Training sample:** For each seed, a fixed pool of 200 x-values and 200 standard-normal noise draws is generated once. The app uses the first *n* points and scales the noise by σ, so moving the sliders changes the same sample smoothly rather than redrawing it.
- **Test sample:** 200 separate points from the same process, with a fixed seed and the current σ. Not redrawn by "New sample".

## 4. Interactivity

| Control | Range | Default | Teaching point |
|---|---|---|---|
| Polynomial degree | 1–15 | 3 | Complexity: underfit → good fit → overfit |
| Training size *n* | 16–200 | 20 | More data tames a complex model |
| Noise σ | 0–1, step 0.05 | 0.3 | Noisier data overfits sooner |
| New sample | button | — | High-degree fits change wildly between samples |

The minimum *n* is 16 so a degree-15 fit is always defined. At *n* = 16 and degree 15, the fit passes through every training point: the extreme case of overfitting.

## 5. Visualization and text

- **Fit plot (only display):** training points (solid), test points (faint), true curve (dashed), fitted curve.
- **Fixed axes:** x from 0 to 1, y from −2 to 2, so extreme high-degree fits run off the chart instead of rescaling it and flattening the true curve.
- **Text:** a short introduction and three "try this" prompts:
  1. At *n* = 20, raise the degree from 1 to 15. When does the curve stop following the sine and start chasing points?
  2. Keep degree 15 and increase *n*. What changes?
  3. At degree 15, press "New sample" several times; then repeat at degree 3.

## 6. Quality checks

Known-answer checks (details belong in the implementation plan):

- σ = 0 with a high degree: the fitted curve overlaps the true curve.
- *n* = 16, degree 15: the fit passes through every training point.
- Degree 1: the fit is a straight line.
- The same seed always produces the same data.
- The exported WASM page loads and the controls respond in a browser, not only in a local run.

## 7. Ethics and access

Not applicable: simulated data only, with no participants or personal data. Deployment creates a **public** GitHub Pages site; publishing requires the researcher's explicit go-ahead.

## 8. Expected outputs and reproducibility

| Output | What it contains | Purpose |
|---|---|---|
| marimo notebook | The interactive app | Teaching material |
| WASM HTML page, built by a GitHub Action and published to GitHub Pages | The app running in the browser, no server | Students open a link; nothing to install |

Pin dependency versions and add an AI-use note to `README.md`.

## 9. Limitations, decisions, and agreement

- With only the fit plot, students judge overfitting by eye; no number or error-versus-degree curve shows test error rising.
- One function in one dimension: the app does not show overfitting in higher dimensions or with other model types.
- Remedies such as regularization and cross-validation are out of scope.

| Decision | Choice and rationale | Status |
|---|---|---|
| Data | Noisy sine on [0, 1]; classic setup with a clear U-shaped test error | Agreed |
| Test set | 200 fixed points from the same process | Agreed |
| Controls | Degree, *n*, σ, "New sample" | Agreed |
| Visuals | Fit plot only | Agreed |
| Scope | No regularization or cross-validation | Agreed |
| Audience and prompts | As in sections 1 and 5 | Agreed |

**Researcher agreement:** Agreed by the researcher on 2026-11-05, with no conditions. Publishing to GitHub Pages still requires a separate go-ahead.
