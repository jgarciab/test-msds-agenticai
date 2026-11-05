import unittest
import numpy as np
from src.overfitting import simulate, fit_models, mse


class SimulationChecks(unittest.TestCase):
    def test_reproducible_and_separate_samples(self):
        a, b = simulate(42), simulate(42)
        for left, right in zip(a, b):
            np.testing.assert_array_equal(left, right)
        self.assertEqual([len(v) for v in a], [30, 30, 300, 300])
        self.assertFalse(np.array_equal(a[0], a[2][:30]))
        self.assertFalse(np.array_equal(a[0], simulate(43)[0]))
        self.assertTrue(all(np.all((x >= 0) & (x <= 1)) for x in [a[0], a[2]]))

    def test_known_answer_mse(self):
        self.assertEqual(mse([1, 3], [2, 1]), 2.5)

    def test_fits_are_training_only(self):
        x, y, xe, ye = simulate(42)
        models, training, _ = fit_models(x, y, xe, ye)
        other, changed_training, _ = fit_models(x, y, xe[::-1], ye + 100)
        np.testing.assert_array_equal(training, changed_training)
        for a, b in zip(models, other):
            np.testing.assert_array_equal(a.coef, b.coef)

    def test_stability_and_training_error(self):
        for seed in [42, 43, 44, 45, 46]:
            models, training, evaluation = fit_models(*simulate(seed))
            self.assertTrue(np.isfinite(training).all() and np.isfinite(evaluation).all())
            self.assertTrue(np.all(np.diff(training) <= 1e-8))
            self.assertTrue(all(np.isfinite(m(np.linspace(0, 1, 400))).all() for m in models))

    def test_noiseless_polynomial_reference(self):
        x = np.linspace(0, 1, 30)
        y = 1 + 2*x - 3*x*x
        models, _, _ = fit_models(x, y, x, y)
        np.testing.assert_allclose(models[1](x), y, atol=1e-12)


if __name__ == '__main__':
    unittest.main()
