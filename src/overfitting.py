"""Small, reproducible simulation and training-only polynomial regression."""
import numpy as np
from numpy.polynomial import Polynomial

OPENING_SEED = 42
NOISE_SD = 0.3
DEGREES = np.arange(1, 16)


def simulate(seed=OPENING_SEED):
    """Independent random streams keep evaluation data out of training."""
    train_rng, eval_rng = [np.random.default_rng(s) for s in np.random.SeedSequence(seed).spawn(2)]
    def draw(rng, size):
        x = rng.uniform(0, 1, size)
        return x, np.sin(2 * np.pi * x) + rng.normal(0, NOISE_SD, size)
    return (*draw(train_rng, 30), *draw(eval_rng, 300))


def mse(observed, predicted):
    return float(np.mean((np.asarray(observed) - np.asarray(predicted)) ** 2))


def fit_models(x_train, y_train, x_eval, y_eval):
    """Scaled polynomial basis avoids a raw-power Vandermonde on [0, 1]."""
    models = [Polynomial.fit(x_train, y_train, int(d), domain=[0, 1]) for d in DEGREES]
    train_error = np.array([mse(y_train, m(x_train)) for m in models])
    eval_error = np.array([mse(y_eval, m(x_eval)) for m in models])
    return models, train_error, eval_error
