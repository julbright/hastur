import unittest
from hastur.distributions import BetaDistribution
from hastur.exceptions import InsufficientObservationsError

class BetaDistribution_tester(unittest.TestCase):

    def setUp(self):
        self.instance = BetaDistribution(alpha = 10, beta = 10)

    def test_n_obs_returns_int(self):
        self.assertIsInstance(self.instance.n_obs, int)

    def test_n_obs_weakly_greater_than_alpha(self):
        self.assertGreaterEqual(self.instance.n_obs, self.instance.alpha)

    def test_n_obs_weakly_greater_than_beta(self):
        self.assertGreaterEqual(self.instance.n_obs, self.instance.beta)

    def test_mode_returns_float(self):
        self.assertIsInstance(self.instance.mode, float)

    def test_mode_weakly_less_than_one(self):
        self.assertLessEqual(self.instance.mode, 1)

    def test_mode_fails_if_n_obs_less_than_three(self):
        self.instance.alpha=1
        self.instance.beta=1

        def call_mode():
            return self.instance.mode

        self.assertRaises(InsufficientObservationsError, call_mode)

    def test_update_with_fail_increments_beta_by_one(self):
        start_value = self.instance.beta
        self.instance.update(0)
        self.assertEqual(start_value, self.instance.beta-1)

    def test_update_with_success_increments_alpha_by_one(self):
        start_value = self.instance.alpha
        self.instance.update(1)
        self.assertEqual(start_value, self.instance.alpha-1)

    def test_random_draw_returns_float(self):
        self.assertIsInstance(self.instance.random_draw, float)

    def test_random_draw_returns_weakly_less_than_one(self):
        self.assertLessEqual(self.instance.random_draw, 1)

    def test_random_draw_returns_InsufficientObservationsError_when_alpha_is_zero(self):
        self.instance.alpha = 0
        self.instance.beta = 4

        def call_random_draw():
            return self.instance.random_draw
        self.assertRaises(InsufficientObservationsError, call_random_draw)

    def test_random_draw_returns_InsufficientObservationsError_when_beta_is_zero(self):
        self.instance.alpha = 9
        self.instance.beta = 0

        def call_random_draw():
            return self.instance.random_draw
        self.assertRaises(InsufficientObservationsError, call_random_draw)
    
