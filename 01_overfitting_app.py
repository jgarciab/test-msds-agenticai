import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")

with app.setup:
    import warnings

    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np

    POOL_SIZE = 200  # points drawn per seed, for training and test data
    TEST_SEED = 0  # training seeds start at 1, so they never reuse the test data


@app.function
def true_curve(x):
    return np.sin(2 * np.pi * x)


@app.function
def draw_pool(seed):
    """x-values and standard-normal noise draws for one seed."""
    rng = np.random.default_rng(seed)
    return rng.uniform(0, 1, POOL_SIZE), rng.standard_normal(POOL_SIZE)


@app.function
def training_sample(seed, n, sigma):
    # First n points of the seed's pool, so a larger n keeps the existing points,
    # and noise scaled by sigma, so changing sigma stretches the same noise.
    x, z = draw_pool(seed)
    return x[:n], true_curve(x[:n]) + sigma * z[:n]


@app.function
def held_out_sample(sigma):
    x, z = draw_pool(TEST_SEED)
    return x, true_curve(x) + sigma * z


@app.function
def fit_polynomial(x, y, degree):
    # Ordinary least squares. The Chebyshev basis (on x rescaled to [-1, 1]) gives
    # the same polynomial as the usual powers of x, but stays numerically stable at degree 15.
    # ponytail: rare samples with two almost identical x-values make degree 15 ill-conditioned;
    # numpy then warns, which would only confuse students, so the warning is silenced.
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", np.exceptions.RankWarning)
        return np.polynomial.Chebyshev.fit(x, y, degree)


@app.function
def heldout_mse(model, sigma):
    x, y = held_out_sample(sigma)
    return np.mean((model(x) - y) ** 2)


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    # Overfitting, one slider at a time

    A model **overfits** when it learns the noise in its training data instead of the
    pattern behind it. It then looks perfect on the data it has seen and does badly on
    new data.

    Here the pattern is known: the **dashed curve**, $y = \sin(2\pi x)$. Each point is
    that curve plus random noise. The model is a polynomial fitted by least squares to
    the **blue training points** only. The **grey test points** are new data from the
    same process, which the model never sees. A good fit follows the dashed curve and
    passes through the middle of the grey cloud.
    """)
    return


@app.cell
def _():
    degree = mo.ui.slider(1, 15, value=3, label="Polynomial degree", show_value=True)
    n = mo.ui.slider(16, 200, value=20, label="Training points (n)", show_value=True)
    sigma = mo.ui.slider(0, 1, step=0.05, value=0.3, label="Noise (σ)", show_value=True)
    # The button's value is the training seed: 1 at the start, +1 per click.
    new_sample = mo.ui.button(value=1, on_click=lambda seed: seed + 1, label="New sample")
    return degree, n, new_sample, sigma


@app.cell(hide_code=True)
def _(degree, n, new_sample, sigma):
    x_train, y_train = training_sample(new_sample.value, n.value, sigma.value)
    x_test, y_test = held_out_sample(sigma.value)
    model = fit_polynomial(x_train, y_train, degree.value)
    grid = np.linspace(0, 1, 500)

    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.scatter(x_test, y_test, s=12, color="tab:gray", alpha=0.35, label="Test points")
    ax.plot(grid, true_curve(grid), "k--", label="True curve")
    ax.plot(grid, model(grid), color="tab:orange", lw=2.5, label=f"Fitted curve (degree {degree.value})")
    ax.scatter(x_train, y_train, s=30, color="tab:blue", edgecolor="white", zorder=3, label="Training points")
    # ponytail: fixed axes on purpose; wild fits run off the chart instead of squashing the true curve
    ax.set(xlim=(0, 1), ylim=(-2, 2), xlabel="x", ylabel="y")
    ax.legend(loc="upper right", fontsize="small")
    fig.tight_layout()

    mo.vstack([mo.hstack([degree, n, sigma, new_sample], justify="start", wrap=True), fig])
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Try this

    1. At *n* = 20, raise the degree from 1 to 15. When does the curve stop following the
       sine and start chasing points?
    2. Keep degree 15 and increase *n*. What changes?
    3. At degree 15, press **New sample** several times; then repeat at degree 3.
    """)
    return


@app.function
def test_noise_free_training_data_lie_on_sine():
    x, y = training_sample(seed=1, n=50, sigma=0)
    assert np.array_equal(y, true_curve(x))


@app.function
def test_high_degree_fit_recovers_sine_without_noise():
    x, y = training_sample(seed=1, n=200, sigma=0)
    grid = np.linspace(0, 1, 501)
    assert np.max(np.abs(fit_polynomial(x, y, 9)(grid) - true_curve(grid))) < 0.01


@app.function
def test_degree_15_passes_through_16_points():
    # Many seeds, because "New sample" can reach any of them. Exact interpolation is typical;
    # a rare seed with two almost identical x-values misses slightly, but must stay inside
    # the drawn marker (radius about 0.04 in data units), so it still looks like a hit.
    misses = []
    for seed in range(1, 101):
        x, y = training_sample(seed, n=16, sigma=0.3)
        misses.append(np.max(np.abs(fit_polynomial(x, y, 15)(x) - y)))
    assert np.median(misses) < 1e-6
    assert max(misses) < 0.04


@app.function
def test_degree_1_recovers_known_line():
    x = np.linspace(0, 1, 11)
    line = fit_polynomial(x, 2 * x + 1, 1).convert(kind=np.polynomial.Polynomial)
    assert np.allclose(line.coef, [1, 2])  # intercept 1, slope 2


@app.function
def test_seeds_are_reproducible_and_test_data_fixed():
    assert all(np.array_equal(a, b) for a, b in zip(training_sample(1, 20, 0.3), training_sample(1, 20, 0.3)))
    assert not np.array_equal(training_sample(1, 20, 0.3)[0], training_sample(2, 20, 0.3)[0])
    assert all(np.array_equal(a, b) for a, b in zip(held_out_sample(0.3), held_out_sample(0.3)))
    assert not np.array_equal(held_out_sample(0.3)[0][:20], training_sample(1, 20, 0.3)[0])


@app.function
def test_samples_are_nested_and_noise_scales():
    x20, y20 = training_sample(1, 20, 0.3)
    x50, y50 = training_sample(1, 50, 0.3)
    assert np.array_equal(x20, x50[:20]) and np.array_equal(y20, y50[:20])
    _, y_double = training_sample(1, 20, 0.6)
    assert np.allclose(y_double - true_curve(x20), 2 * (y20 - true_curve(x20)))


@app.function
def test_prompts_show_what_they_describe():
    # Prompt 1: at n = 20, degree 15 does worse on new data than degree 3.
    x, y = training_sample(1, 20, 0.3)
    assert heldout_mse(fit_polynomial(x, y, 15), 0.3) > 2 * heldout_mse(fit_polynomial(x, y, 3), 0.3)
    # Prompt 2: more training points tame the degree-15 fit.
    x, y = training_sample(1, 200, 0.3)
    assert heldout_mse(fit_polynomial(x, y, 15), 0.3) < 0.2  # noise alone gives 0.09
    # Prompt 3: across new samples, degree-15 fits vary far more than degree-3 fits.
    grid = np.linspace(0.05, 0.95, 200)
    def spread(degree):
        fits = [fit_polynomial(*training_sample(s, 20, 0.3), degree)(grid) for s in range(1, 21)]
        return np.std(fits, axis=0).mean()
    assert spread(15) > 5 * spread(3)


if __name__ == "__main__":
    app.run()
