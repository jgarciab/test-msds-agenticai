import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium", app_title="When a better fit predicts worse")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    from src.overfitting import OPENING_SEED, DEGREES, simulate, fit_models
    return mo, np, plt, OPENING_SEED, DEGREES, simulate, fit_models


@app.cell
def _(mo):
    mo.md("""
    # When a better fit predicts worse
    **Explore overfitting in two minutes.** Regression uses a curve to predict an
    outcome from an input. A more flexible curve can follow the signal—or chase noise.

    **1.** Move the degree slider from 1 to 5, then to 15.
    **2.** Compare training error with error on new observations.
    **3.** Generate another sample. Does the same degree still work best?
    """)
    return


@app.cell
def _(mo, OPENING_SEED):
    degree = mo.ui.slider(1, 15, value=3, step=1, label="Polynomial degree", show_value=True)
    new_sample = mo.ui.run_button(label="Generate new sample")
    get_seed, set_seed = mo.state(OPENING_SEED)
    mo.hstack([degree, new_sample], justify="start", gap=2)
    return degree, new_sample, get_seed, set_seed


@app.cell
def _(new_sample, set_seed):
    if new_sample.value:
        set_seed(lambda previous: previous + 1)
    return


@app.cell
def _(get_seed, simulate, fit_models):
    seed = get_seed()
    x_train, y_train, x_eval, y_eval = simulate(seed)
    models, train_error, eval_error = fit_models(x_train, y_train, x_eval, y_eval)
    return seed, x_train, y_train, x_eval, y_eval, models, train_error, eval_error


@app.cell
def _(mo, seed, degree, train_error, eval_error):
    mo.md(f"""
    **Sample seed: {seed}** · 30 training observations · 300 new evaluation observations · noise SD 0.3

    **Degree {degree.value}** — Training MSE: **{train_error[degree.value-1]:.3f}**
    · Evaluation MSE: **{eval_error[degree.value-1]:.3f}**
    """)
    return


@app.cell
def _(np, plt, mo, degree, x_train, y_train, x_eval, y_eval, models, DEGREES, train_error, eval_error):
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6), layout="constrained")
    grid = np.linspace(0, 1, 400)
    chosen = degree.value - 1
    axes[0].scatter(x_eval, y_eval, marker="x", s=12, alpha=0.25, color="#c45a18", label="Evaluation (new)")
    axes[0].scatter(x_train, y_train, s=36, facecolors="white", edgecolors="#2266aa", label="Training", zorder=3)
    axes[0].plot(grid, np.sin(2*np.pi*grid), "--", color="#333333", label="True signal")
    axes[0].plot(grid, models[chosen](grid), color="#2266aa", label=f"Fit: degree {degree.value}")
    axes[0].set(xlabel="Input x", ylabel="Outcome y", title="Signal or noise?", xlim=(0, 1))
    # Outlying high-degree predictions can otherwise hide all observations.
    low = min(y_train.min(), y_eval.min()) - 0.5
    high = max(y_train.max(), y_eval.max()) + 0.5
    axes[0].set_ylim(low, high)
    outside = np.any((models[chosen](grid) < low) | (models[chosen](grid) > high))
    axes[0].legend(fontsize=8)
    axes[1].plot(DEGREES, train_error, "o-", color="#2266aa", label="Training")
    axes[1].plot(DEGREES, eval_error, "x--", color="#c45a18", label="Evaluation (new)")
    axes[1].axvline(degree.value, color="#555555", linestyle=":", label="Selected degree")
    # Log-like scale preserves small errors without concealing very large ones.
    axes[1].set_yscale("symlog", linthresh=0.1)
    axes[1].set(xlabel="Polynomial degree", ylabel="Mean squared error (symlog scale)", title="Does it predict new observations?", xticks=[1, 3, 5, 7, 9, 11, 13, 15])
    axes[1].set_ylim(bottom=0)
    axes[1].legend(fontsize=8)
    chart = mo.vstack([fig, mo.md("⚠ Fitted curve extends beyond the left plot’s visible range; all errors include these predictions." if outside else "Left plot uses a fixed range for this sample; no fitted predictions are hidden.")])
    plt.close(fig)
    chart
    return


@app.cell
def _(mo):
    mo.md("""
    ### What to notice
    A straight line can **underfit** the curved signal. Increasing degree can help,
    but a very flexible curve can **overfit**: it follows noise in the training sample
    and predicts new observations poorly. Training error usually falls with complexity;
    evaluation error need not. The best degree varies between samples.

    **Which model fits training data best? Which predicts new observations best?**

    MSE is the average squared prediction error: smaller is better. The right plot
    uses a symmetric logarithmic scale (linear close to zero) so large errors remain visible.
    The dashed true curve is known because we simulated the data:
    y = sin(2πx) + Gaussian noise. Both samples come from the same process.

    **A fair comparison:** only training observations fit the model. You can use the
    evaluation errors to choose a degree here, so they are a teaching comparison,
    not an untouched final test of your chosen model. This illustration does not
    measure teaching effectiveness. No real data or student tracking are used.
    """)
    return


if __name__ == "__main__":
    app.run()
