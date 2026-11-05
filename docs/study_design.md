# Study design: teaching overfitting

Status: Agreed · Date: 2026-11-05

The user's stated goal serves as the brief; no separate project brief or debrief is required for this design.

## Objective and scope

Create a simple interactive marimo app showing students why fitting training observations more closely can make predictions on new observations worse. Students should distinguish training fit from predictive performance and recognize underfitting and overfitting. Include a brief introduction to regression as a curve used to predict an outcome from an input; this is an accessibility default rather than a confirmed statement about students' prior knowledge. Deliver the app as a browser-based WASM app, deployed through GitHub Actions to GitHub Pages.

This is a teaching demonstration using simulated data, not a study of teaching effectiveness or evidence about a real population.

## Simulated data and models

- Generate one input uniformly on [0, 1] and an outcome from y = sin(2πx) + independent, mean-zero Gaussian noise.
- Use 30 training observations and 300 independently generated evaluation observations from the same process. These sizes keep the training sample visibly small and the evaluation comparison less variable.
- Keep sample sizes and noise level fixed, with Gaussian noise standard deviation 0.3. This choice is intended to leave the underlying pattern visible while allowing overfitting to appear; its teaching clarity remains to be checked in the finished demonstration.
- Use a fixed, recorded random seed for the opening example. Record the seed for each newly generated sample so examples can be reproduced.
- Fit polynomial regression with degrees 1–15, using only training observations. Evaluate each fitted model on the separate evaluation observations.
- Compare mean squared error (the average squared prediction error), calculated separately for training and evaluation observations.

## Interactivity and visualizations

Provide a polynomial-degree slider from 1 to 15 and a “Generate new sample” button. Changing degree keeps the current data fixed; generating a new sample replaces both independent samples while keeping the data-generating process unchanged.

Show two side-by-side plots:

1. Training and evaluation observations with distinct visual markers, the true noiseless curve, and the fitted curve for the selected degree. Keep the training observations visually prominent and the evaluation observations subdued to limit clutter.
2. Training and evaluation mean squared error across all degrees, highlighting the selected degree.

Use clear labels and distinguish curves and observation groups by more than color alone. Explain that the true curve is known because the data are simulated.

Ask: “Which model fits the training data best? Which predicts new observations best?” Encourage students to change degree, then generate another sample to see how the comparison varies.

## Interpretation and quality criteria

Training error should generally fall as polynomial degree increases, while evaluation error may rise when a model fits sample noise. The exact evaluation-error pattern and best degree can vary between samples; do not promise a particular curve shape on every draw.

Keep evaluation observations out of model fitting and any fitted preprocessing. Since students can inspect evaluation error to choose complexity, describe it as a teaching comparison, not an untouched final test of the selected model.

Before presenting the app, verify sample independence, reproducibility from recorded seeds, correct error calculations, and consistent updates of both plots and the selected-degree highlight. Check that numerical instability does not masquerade as overfitting. Inspect the opening example and additional samples for a clear and honest illustration. These are design criteria, not completed checks or an implementation plan.

## Ethics, outputs, and reproducibility

Use only locally simulated numerical observations; no real participant data, student tracking, or external data services are needed. No learning-outcome evaluation or participant recruitment is included.

The intended output is a marimo teaching app with brief explanations, the two controls, and the two plots. Students run the simulations and model fitting in their browser using WASM, without installing Python or connecting to a Python application server. Use browser-compatible dependencies and keep computation small enough for responsive interaction. Initial loading may require network downloads of the runtime and packages; offline operation is not a requirement.

Deploy the static app to GitHub Pages through a GitHub Actions workflow. This is an agreed delivery requirement; workflow configuration and publication are later implementation activities. Readiness includes checking that the exported WASM app loads and that both controls and plots behave correctly in a browser, rather than relying only on native Python checks or a successful deployment job. No deployment or browser compatibility has been verified at this stage.

Preserve the generating formula, sample sizes, noise standard deviation, seeds, model definitions, error definition, software versions, and export/deployment configuration with the eventual app so the demonstration can be reconstructed. No data generation or app implementation has occurred at this design stage.

## Agreement and conditions

The user approved the simulated-data approach, controls, plots, model range, and teaching scope on 2026-11-05, and subsequently confirmed overfitting as the topic and requested this update following the proposal of noise standard deviation 0.3 and WASM delivery through GitHub Actions to GitHub Pages. These choices are recorded as agreed. The brief regression introduction remains a stated accessibility default. Teaching clarity, numerical stability, and browser compatibility remain validation requirements, not completed checks. This update covers design only; it does not implement the app, configure deployment, or assess teaching effectiveness.
