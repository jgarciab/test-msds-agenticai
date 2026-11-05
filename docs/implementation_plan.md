# Implementation plan

Status: Agreed · Date: 2026-11-05

Based on `docs/study_design.md` (Agreed 2026-11-05). A unit is one numbered task, reviewable in about 5–15 minutes. This plan contains no implementation code.

## 1. Project overview

- **Project:** A marimo app that teaches overfitting with simulated data. It runs in the browser (WebAssembly, WASM) and is deployed to GitHub Pages by a GitHub Action.
- **Environment:** Python 3.12 managed by uv (0.11.25 installed), recorded in `pyproject.toml` and `uv.lock`. Packages: marimo, numpy, matplotlib, and pytest for checks. Runs on the researcher's Mac; the system Python (3.9.6) is too old and is not used. In the browser, Pyodide supplies its own numpy and matplotlib versions.
- **Data:** Simulated inside the app; nothing is stored in `data/`.
- **Deliverables:** `01_overfitting_app.py`, `.github/workflows/deploy.yml`, README instructions, and a public GitHub Pages site (published only after the researcher's go-ahead).

### Working principles

- Complete one requested unit at a time, in dependency order.
- A unit is complete when its changes are reviewed and explainable, it runs without unexplained errors, its checks have run with results recorded under *Evidence*, and the researcher has reviewed it. Agent checks and researcher review are recorded separately.
- Do not change the agreed design without asking. Do not commit or push without an explicit request.

## 2. Project organisation

- `01_overfitting_app.py` (project root): the whole app, including simulation, fitting, controls, plot, text, and the known-answer checks as test functions. Kept in one file because the WASM export bundles only the notebook; helper code in `src/` would not reach the browser. This departs from the `src/` default in `AGENTS.md`.
- `.github/workflows/deploy.yml`: build and deploy.
- `dist/`: local export output, excluded from Git.
- `data/`, `src/`, `results/`: unused; the app simulates its own data and produces no saved outputs.

## 3. Implementation overview

| Unit | Purpose and output | Depends on | Status |
|---|---|---|---|
| 1.1 | Python environment: `pyproject.toml`, `uv.lock` | None | Complete (researcher approved 2026-11-05) |
| 2.1 | Simulation and fitting functions with known-answer checks | 1.1 | Checks passed; awaiting researcher review |
| 2.2 | Controls and fit plot | 2.1 | Checks passed; awaiting researcher review |
| 2.3 | Introduction and three prompts | 2.2 | Checks passed; wording awaiting researcher approval |
| 3.1 | Local WASM export, checked in a browser | 2.3 | Checks passed; awaiting researcher review |
| 3.2 | GitHub Action to build and deploy to Pages | 3.1 | See evidence; awaiting researcher review |
| 4.1 | README: setup, commands, deployment, AI use | 3.2 | Checks passed; awaiting researcher review |

**Change of procedure (2026-11-05):** After approving Unit 1.1, the researcher asked the agent to "push through and implement everything else without asking any questions", and to discard any changes on GitHub in favour of this work. Units 2.1–4.1 were therefore implemented without per-unit researcher review; open decisions were settled by the agent's stated defaults (section 6); and the work was pushed directly to `main`, replacing the remote `main` (which held a different implementation merged from PR #1), instead of using a feature branch and pull request.

## 4. Implementation units

### Stage 1 — Environment

#### Unit 1.1 — Set up the Python environment

- **Requirements:** `pyproject.toml` requiring Python 3.12 with marimo, numpy, and matplotlib; pytest as a development dependency; dependencies locked in `uv.lock`.
- **Checks:** `uv run python --version` reports 3.12; marimo, numpy, and matplotlib import without errors; installed versions are recorded below.
- **Decision point (blocks start):** Approve PyPI (packages) and uv's Python downloads as software sources; `AGENTS.md` leaves approved sources unspecified. *Resolved 2026-11-05: researcher approved PyPI and uv's python-build-standalone downloads, and chose to verify in a temporary environment outside the project folder.*
- **Evidence** (agent checks, 2026-11-05, researcher's Mac, macOS 27.0.1 arm64, inside the Claude Code sandbox):
  - Changes: created `pyproject.toml` (name `overfitting-app`, `requires-python = ">=3.12,<3.13"`, dependencies added with `uv add`) and `uv.lock` (42 packages, no personal paths).
  - Environment: temporary, outside the project and Proton Drive. The sandbox blocks uv's default folders in the home directory, so these were set: `UV_CACHE_DIR`, `UV_PYTHON_INSTALL_DIR`, `UV_PYTHON_BIN_DIR`, and `UV_PROJECT_ENVIRONMENT`, all under the session's `$TMPDIR`. uv downloaded Python 3.12.13. No `.venv` was created in the project.
  - `uv run python --version` → `Python 3.12.13` (expected 3.12: pass).
  - Imports succeed; installed versions: marimo 0.25.2, numpy 2.5.4, matplotlib 3.11.2, pytest 9.2.0 (pass). `uv run marimo --version` → 0.25.2.
  - `uv lock --check` → lockfile consistent with `pyproject.toml` (pass).
  - Warnings seen, caused by the sandbox blocking the home directory, not by the project: matplotlib could not write `~/.matplotlib` and used a temporary cache; marimo could not read `~/.config/marimo/marimo.toml`. Not expected outside the sandbox.
  - Not checked: the researcher's own environment. Running `uv sync` in the researcher's terminal is still needed to create it; a project `.venv` would sync to Proton Drive unless `UV_PROJECT_ENVIRONMENT` points elsewhere.
  - Approved software sources also recorded in `AGENTS.md` (2026-11-05).
  - Researcher review: approved 2026-11-05. Changes are uncommitted.

### Stage 2 — App

#### Unit 2.1 — Simulate data and fit polynomials

- **Requirements:**
  - Training data: per seed, a pool of 200 x-values (Uniform(0, 1)) and 200 standard-normal noise draws; the app uses the first *n* and multiplies the noise by σ.
  - Test data: 200 points from the same process, fixed seed, current σ.
  - Fit: ordinary least-squares polynomial of a given degree, using a numerically stable basis so degree 15 is not dominated by rounding error; evaluated on a grid over [0, 1].
- **Checks** (`uv run pytest 01_overfitting_app.py`), each against an answer known independently of the code:
  - σ = 0: training y equals sin(2πx) exactly.
  - σ = 0, *n* = 200, degree 9: the fitted curve is within 0.01 of sin(2πx) on [0, 1].
  - *n* = 16, degree 15: the fit passes through all 16 training points (residuals ≈ 0).
  - Degree 1 fitted to y = 2x + 1 recovers slope 2 and intercept 1.
  - The same seed gives identical data; a new seed changes the training data but not the test data.
  - The first 20 training points at *n* = 20 are identical to the first 20 at *n* = 50.
- **Decision point:** None.
- **Evidence** (agent checks, 2026-11-05, researcher's Mac in the Claude Code sandbox, temporary environment as in 1.1):
  - Changes: `01_overfitting_app.py` with functions `true_curve`, `draw_pool`, `training_sample`, `held_out_sample`, `fit_polynomial` (least squares in the Chebyshev basis, which gives the same polynomial as powers of x but is numerically stable), `heldout_mse`, and seven test functions. Test data use seed 0; training seeds start at 1.
  - `uv run pytest 01_overfitting_app.py` → 7 passed. Added beyond the plan: σ scaling (doubling σ doubles each noise term) and a check that the three prompts show what they describe (section 2.3 evidence).
  - Negative control: a copy whose fit always uses degree 1 fails 3 of 7 checks (high-degree recovery, degree-15 interpolation, prompts), as expected.
  - Finding: the first version of the interpolation check (all residuals < 1e-6 for seeds 1–100) failed on seed 100, where two training x-values are 0.00008 apart and degree 15 is ill-conditioned. Over seeds 1–1000: median miss 1e-11; 17 seeds above 1e-6; 1 seed above 1e-3 (worst 0.018). The check now requires median < 1e-6 and every miss < 0.04 (the drawn marker radius in data units), matching the design's visible claim that the curve passes through every point. numpy's `RankWarning` for those rare seeds is silenced so students do not see it.
  - `marimo check` → no issues.
  - Researcher review: pending.

#### Unit 2.2 — Add controls and the fit plot

- **Requirements:** Degree slider 1–15 (default 3); training size *n* 16–200 (default 20); noise σ 0–1, step 0.05 (default 0.3); "New sample" button that changes the training seed only. Fit plot with training points (solid), test points (faint), true curve (dashed), and fitted curve; legend; fixed axes x 0–1, y −2 to 2.
- **Checks** (inspected in `uv run marimo edit 01_overfitting_app.py`):
  - The default view matches the design.
  - Degree 1 gives a straight line.
  - *n* = 16, degree 15: the curve passes through every training point and runs off the chart between them.
  - σ = 0: the training points lie on the dashed curve.
  - "New sample" moves the training points; the test points stay.
  - Increasing *n* keeps the existing training points.
  - The axes never rescale.
- **Decision point:** None.
- **Evidence** (agent checks, 2026-11-05): A local `marimo edit` server could not run because the sandbox blocks local ports, so the checks were made on the WASM export in the browser pane (Unit 3.1), which runs the same notebook.
  - Slider ranges and defaults read from the page: degree 1–15 (3), *n* 16–200 (20), σ 0–1 (0.3); σ moves in 0.05 steps (six right-arrow presses from 0 reached 0.3).
  - Default view matches the design (four layers, legend, fixed axes): pass.
  - Degree 1 → straight line: pass. *n* = 16, degree 15 → passes through every training point and runs off the chart between them: pass. σ = 0 → all points on the dashed curve: pass. "New sample" → training points and fit change, grey test cloud unchanged: pass. Axes stayed at x 0–1, y −2 to 2 throughout: pass.
  - Nested samples when *n* increases: checked by the 2.1 test, not by eye.
  - Keyboard: sliders respond to Home and arrow keys once focused by click or Tab.
  - Researcher review: pending.

#### Unit 2.3 — Add the introduction and prompts

- **Requirements:** A short introduction (what overfitting is, what the plot shows) and the three prompts from design section 5.
- **Checks:** Following each prompt in the app shows the behaviour it describes: (1) at high degree the fit leaves the sine and chases points; (2) increasing *n* calms the degree-15 fit; (3) the degree-15 fit changes far more across new samples than the degree-3 fit.
- **Decision point:** The researcher approves the wording for the audience.
- **Evidence** (agent checks, 2026-11-05): The introduction explains overfitting and the four plot layers; the prompts are verbatim from design section 5. The `test_prompts_show_what_they_describe` check passes, with these values on seed 1, σ = 0.3 (test MSE; noise alone gives 0.09):
  - Prompt 1 (*n* = 20): degree 1 → 0.314, 3 → 0.107, 5 → 0.122, 9 → 10.4, 15 → 2.6 × 10⁶. Test error rises sharply above degree 5.
  - Prompt 2: degree 15 with *n* = 200 → 0.102.
  - Prompt 3: mean spread of fitted curves over 20 samples (x in 0.05–0.95): degree 3 → 0.135, degree 15 → 3332.
  - In the browser, degree 14 with *n* = 192 closely followed the sine.
  - Researcher approval of the wording: pending.

### Stage 3 — Deployment

#### Unit 3.1 — Export to WASM and check in a browser

- **Requirements:** Export the notebook with `marimo export html-wasm` to `dist/`; add `dist/` to `.gitignore`.
- **Checks:** Serve `dist/` locally and open it in a browser: the page loads; numpy and matplotlib load in the browser; all four controls respond; no errors in the browser console; the 2.2 checks for degree 1, *n* = 16 with degree 15, and "New sample" still hold.
- **Note:** The sandbox may block a local web server; if so, the agent provides the command for the researcher to run.
- **Decision point (blocks start):** Show the app only (code hidden), or let students see the code? *Agent default, at the researcher's request not to ask: app only (`--mode run`, code hidden). Reversible with `--show-code`.*
- **Evidence** (agent checks, 2026-11-05):
  - `marimo export html-wasm 01_overfitting_app.py -o dist --mode run` succeeded. In the sandbox it first failed because marimo calls Ruff through `uv tool`, whose default folder is in the blocked home directory; setting `UV_TOOL_DIR` to `$TMPDIR` fixed it. GitHub runners are unaffected. `dist/` added to `.gitignore`.
  - Serving `dist/` locally failed: the sandbox does not allow binding a local port. Instead, a `--single-file` export (same notebook, assets from a CDN) was opened in the browser pane. The page loaded, Pyodide installed numpy and matplotlib, and all four controls worked (checks in 2.2). No Python errors on the page.
  - Console: one error, `localStorage` blocked inside a `data:` URL, caused by how the preview pane loads local files; not expected on https.
  - Not checked locally: the multi-file `dist/` build served over HTTP. That is the build GitHub deploys; it is checked on the live site (3.2).
  - The marimo export also copies marimo's own asset files into `dist/`, including a `CLAUDE.md` from the marimo package. These are published with the site; harmless, noted for transparency.
  - Researcher review: pending.

#### Unit 3.2 — Add the GitHub Action

- **Requirements:** On a push to `main` or a manual trigger: install from `uv.lock`, run the checks, export with the same command as 3.1, and deploy `dist/` to GitHub Pages. Failing checks block deployment.
- **Checks before push:** The export command matches 3.1; checks run before deployment; the workflow file parses.
- **Checks after push (only with the researcher's go-ahead):** The Action run succeeds; the Pages URL loads and the controls respond.
- **Decision point (blocks push):** The researcher enables Pages (Settings → Pages → Source: GitHub Actions) and gives an explicit go-ahead to push and publish publicly. Changes go through a feature branch and pull request to `main`, as `AGENTS.md` requires.
- **Evidence** (agent checks, 2026-11-05):
  - `.github/workflows/deploy.yml`: build job runs `uv sync --locked` → `uv run pytest 01_overfitting_app.py` → the same export command as 3.1 → upload `dist/`; the deploy job needs build, so failing checks stop deployment. Action versions are the latest major tags found with `git ls-remote` that day: checkout v7, setup-uv v7, upload-pages-artifact v5, deploy-pages v5.
  - The workflow file parses as YAML, and its build steps are in the order above.
  - Pages was already enabled for the repository (the site answered before this push).
  - After push: see the final evidence in section 5.
  - Researcher review: pending.

### Stage 4 — Documentation

#### Unit 4.1 — Update the README

- **Requirements:** A project section with purpose, environment (OS, Python, uv), commands (set up, run, check, export), deployment and public URL, and an AI-use section: Claude Code, model `claude-opus-5-5`, access date, tasks assisted, extent of automation, and what the researcher reviewed. Unknown details are marked as unknown.
- **Checks:** Every README command runs as written from the project root; links resolve.
- **Decision point (blocks start):** Replace the template README, or add the project section above it? *Agent default, at the researcher's request not to ask: project section added above the template guide, which is kept unchanged below a divider.*
- **Evidence** (agent checks, 2026-11-05):
  - `uv sync`, `uv run pytest 01_overfitting_app.py` (7 passed) and the export command ran as written from the project root.
  - Not run in the sandbox: `marimo run`, `marimo edit` and `python -m http.server`, because local ports are blocked. The researcher should try them once.
  - Links to `docs/` and the workflow resolve. The live URL `https://javier.science/test-msds-agenticai/` (where `jgarciab.github.io/test-msds-agenticai/` redirects) answered 200 before deployment.
  - AI-use section written; the access date and model are from the session environment. Persistent memory: none used.
  - Researcher review: pending.

## 5. Full rerun and final review

- **Execution:** In a fresh clone: `uv sync`, `uv run pytest 01_overfitting_app.py`, export to `dist/`, and check the page in a browser. After merging to `main`, check the Action run and the public URL.
- **Expected outputs:** Passing checks; a working page in `dist/`; the live Pages site.
- **Checks across units:** The browser version and a local `marimo run` agree on the 2.2 spot checks; slider ranges and defaults match design section 4.
- **Reproducibility:** `uv.lock`, the Python version, fixed seeds, and the Pyodide package versions used in the browser (which may differ from the lockfile).
- **AI-use records:** The README AI-use section meets `AGENTS.md`.
- **Teaching review:** The researcher works through the three prompts as a student would and confirms that the app teaches the intended points and that the design's limitations (fit plot only, one dimension) are acceptable.

### Final completion criteria

- [ ] All units meet their completion criteria.
- [ ] The full rerun produces the expected outputs.
- [ ] The app has been reviewed against the agreed design.
- [ ] Another person can rerun and deploy it from the README.
- [ ] AI-use records are present, with unknown details marked.
- [ ] Remaining limitations and incomplete checks are reported.
- [ ] Changes have been reviewed; Git checkpoints made if requested.

**Final evidence:** —

## 6. Open issues and revisions

| Affected units | Issue | Reason | Researcher decision |
|---|---|---|---|
| 1.1 | Approve PyPI and uv's Python downloads as software sources | `AGENTS.md` leaves sources unspecified | Agreed 2026-11-05 (both approved) |
| 3.1 | App only, or code visible to students | Not settled in the study design | Agent default (app only); researcher has not decided |
| 3.2 | Enable Pages; go-ahead to push and publish publicly | Publishing requires explicit permission | Go-ahead given 2026-11-05 ("push through… discard [remote changes] and add yours"); Pages was already enabled |
| 4.1 | Replace the template README or add a project section | Preserve existing content unless told otherwise | Agent default (add above); researcher has not decided |

## 7. Plan agreement

**Researcher agreement:** Agreed by the researcher on 2026-11-05. The decisions in section 6 remain open and are resolved at their units.
