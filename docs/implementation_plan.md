# Implementation plan: teaching overfitting

Status: Agreed · Date: 2026-11-05

Based on `docs/study_design.md`.

Build a marimo app using the agreed noisy sine data, polynomial degrees 1–15, two controls, and two plots. Deliver it as a WASM app through GitHub Actions to GitHub Pages.

A **unit** is one small task, sized for roughly 5–15 minutes of review. Work in order, one requested unit at a time. Each unit depends on the preceding units.

| Unit | Task and output | Checks |
|---|---|---|
| 1. Prepare environment | Record minimal browser-compatible dependencies, versions, and setup commands. | Dependencies import; marimo WASM export is supported. Confirm download sources before installation. |
| 2. Generate simulated data | Reproducible simulation in `src/`: 30 training and 300 independent evaluation observations, noise SD 0.3, recorded seeds. | Correct sizes and formula; same seed reproduces data; training and evaluation use separate random draws. |
| 3. Fit models and calculate errors | Training-only polynomial fits for degrees 1–15, predictions, and mean squared errors. | Known-answer error calculation; evaluation data cannot affect fits; finite predictions and numerical stability; training error does not materially increase with degree. |
| 4. Build interactive app | `01_overfitting.py` with degree slider, new-sample button, two plots, and short teaching explanations. | Degree changes preserve data; new samples replace both datasets; plots and highlights agree; labels distinguish groups beyond color. |
| 5. Validate WASM export | Static browser app and documented export command. | Serve the export locally; verify browser loading, both controls, plots, seed reproducibility, and responsive interaction without a Python application server. |
| 6. Prepare deployment | GitHub Actions workflow exporting and deploying to GitHub Pages; README setup, run, deployment, and AI-use records. | Workflow builds the expected artifact; dependencies and project-site paths are correct. Confirm repository Pages settings and permissions before publication. |
| 7. Final rerun and review | Fresh documented setup, checks, export, and browser rerun; evidence recorded in this plan. After authorized publication, check the deployed app too. | Opening example reproduces; degrees 1, intermediate values, and 15 work; several recorded seeds behave correctly. Researcher reviews teaching clarity and interpretation separately. |

## Completion record

### Unit 1 — Implemented; awaiting researcher review (2026-11-05)

- Outputs: `pyproject.toml`, `uv.lock`, ignored `.venv`, and setup/version/AI-use documentation in `README.md`. Python 3.12 is selected to match the available native interpreter; browser Python is supplied separately by Pyodide. Direct dependencies: marimo 0.25.2, NumPy 2.5.4, Matplotlib 3.11.2.
- Source approval: user explicitly approved PyPI (`pypi.org`, `files.pythonhosted.org`) before installation. TLS and artifact verification remained enabled.
- Passed: `uv lock --default-index https://pypi.org/simple` resolved 38 packages; `uv sync --frozen --default-index https://pypi.org/simple` installed 35 applicable packages. Repeating `uv sync --frozen --offline` checked 35 packages without changes.
- Passed: imports of all three dependencies and an in-memory Matplotlib PNG render. `.venv/bin/marimo export html-wasm --help` confirms the supported export command. Export of a temporary minimal marimo notebook with `--mode run` produced a nonempty `index.html` and static assets, with exit status 0. Temporary notebook and output were removed automatically; no teaching app or simulation was created.
- Diagnosed and resolved: the initial export failed because uv tried writing to the read-only home cache; Matplotlib and Fontconfig also reported unwritable defaults. The README's writable cache/configuration variables resolved these issues; imports, PNG rendering, and export then passed. Export obtains marimo's pinned Ruff 0.15.18 helper through uv.
- Scope: verified on managed Linux x86_64, Python 3.12.14, uv 0.13.4. Browser execution and compatibility of exact package versions remain unverified until Unit 5; no deployment, student interaction, or local-computer validation was performed.
- Researcher review: pending. No commit, push, or publication was made. Units 2–7 remain not started.

A successful build alone does not establish browser or deployment success.

## Conditions and agreement

Use only simulated data; keep environments out of Git. Package sources PyPI and `files.pythonhosted.org` were explicitly approved before Unit 1 installation. No commits, pushes, or publication without explicit instruction.

The user accepted this plan on 2026-11-05 and subsequently authorized Unit 1 only. Researcher review of Unit 1 and the eventual completed app remains outstanding.

## Remaining units — execution evidence (2026-11-05)

The user's subsequent instruction authorized proceeding through the remaining units without intermediate questions. Earlier per-unit stopping conditions are superseded for this implementation pass. No commit, push, or hosted publication was requested or performed.

- **Unit 2 implemented:** `src/overfitting.py` generates the agreed sine signal with Gaussian SD 0.3, 30 training and 300 evaluation observations, independent spawned random streams, and reproducible seeds. Opening seed 42; each button click advances it by one. The preserved formula, seed and generator reproduce the samples; no datasets or AI-generated observations were stored.
- **Unit 3 implemented:** scaled NumPy polynomial fits for degrees 1–15, training-only fitting, and separate MSE arrays. `tests/test_overfitting.py` contains five passing tests: reproducibility/sample sizes and separation; known-answer MSE 2.5; evaluation perturbations cannot change fitted coefficients; finite predictions and nonincreasing training error for seeds 42–46; and exact recovery of a noiseless quadratic within 1e-12. Independence follows from separate random streams, not a sample-correlation claim.
- **Unit 4 implemented:** `01_overfitting.py` contains both controls, two side-by-side plots, error summaries, seeds, and teaching text. All eight cells execute natively. Chromium checks passed degrees 1, 8, 15 while retaining seed 42 and two new-sample clicks producing 43 and 44. Accessible keyboard slider interaction worked. Plots use distinct markers and line styles. To retain readability for extreme fits, the left plot warns about predictions beyond its visible range; the error plot uses an explicitly labeled symmetric logarithmic scale. These presentation choices do not exclude observations or alter error calculations.
- **Unit 5 partially verified:** `marimo export html-wasm 01_overfitting.py --mode run -o _site` succeeds and packages `src` in a pure-Python wheel. A local static HTTP server served the output to Chromium. Browser runtime initialization failed at the required `wasm.marimo.app/pyodide-lock.json` request (`ERR_TUNNEL_CONNECTION_FAILED`), an environment proxy restriction. Added `wasm.marimo.app` to the configuration draft; save confirmed, activation requires environment-settings review/save and publication. No TLS checks or proxy controls were bypassed. Actual WASM controls and package versions remain unchecked.
- **Unit 6 implemented, deployment unverified:** `.github/workflows/pages.yml` installs pinned uv and the frozen lock, runs tests and notebook checks, exports `_site`, and uses GitHub Pages artifact/deploy actions. Build has read-only repository permissions; only the deploy job has Pages write and OIDC permissions. Workflow structure and relative export/local-wheel asset paths were inspected. README documents Pages settings and commands. GitHub-hosted execution, repository Pages settings, environment permissions and hosted behavior were not tested; no changes were pushed.
- **Unit 7 rerun completed for available checks:** installed the frozen lock into a fresh `/tmp/overfitting-final-venv` using the existing verified cache; all five tests passed, `marimo check` passed, and export to a separate `/tmp/overfitting-final-site` passed. This verifies a fresh installed environment, not fresh remote downloads. Native browser checks and visual inspection were performed; WASM execution and hosted review remain blocked/unrun as described above. Researcher review and confirmation of teaching clarity remain pending. AI-use and run instructions are in README.

**Current status:** app implementation and deployment configuration are present and uncommitted. Do not claim end-to-end WASM or hosted readiness until the remaining browser and deployment checks pass. No assessment of teaching effectiveness was performed.

## Push and deployment request (2026-11-05)

The user explicitly authorized pushing and deploying. Changes are prepared on `feature/overfitting-app` following AGENTS.md's pull-request workflow. Git remote access succeeds, but GitHub API access is blocked by the environment proxy (CONNECT HTTP 403 at `api.github.com`), before GitHub authentication can be evaluated. Network additions for `api.github.com` and `jgarciab.github.io` were saved in the environment draft, preserving the pending `wasm.marimo.app` addition. Pull-request creation, merge, Actions monitoring, Pages configuration, and hosted validation require that network change to be activated. No successful deployment is claimed.
