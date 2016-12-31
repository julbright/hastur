import unittest
from hastur.bandits import Bandit
from hastur.bandits import GreedyBandit
from hastur.bandits import EpsilonGreedyBandit
from hastur.bandits import BayesianBandit
from hastur.bandits import EpsilonBayesianBandit
from hastur.bandits import UpperConfidenceBoundBandit
from hastur.observations import Observation
from hastur.exceptions import InsufficientObservationsError
from hastur.arms import Arm


class Bandit_tester(unittest.TestCase):

    def setUp(self):
        self.instance = Bandit()
        self.arm = Arm()

    def tearDown(self):
        pass

    def test_n_arms_returns_int(self):
        self.assertIsInstance(self.instance.n_arms, int)

    def test_add_arm_increases_n_arms(self):
        current_arms = self.instance.n_arms
        self.instance.add_arm(Arm())
        new_arms = self.instance.n_arms
        self.assertGreater(new_arms, current_arms)

    def test_add_arm_increments_n_arms_by_one(self):
        current_arms = self.instance.n_arms
        self.instance.add_arm(Arm())
        new_arms = self.instance.n_arms
        self.assertEqual(new_arms-1, current_arms)

    def test_add_arm_returns_string(self):
        name = self.instance.add_arm(Arm())
        self.assertIsInstance(name, str)

    def test_means_returns_dict(self):
        self.assertIsInstance(self.instance.means, dict)

    def test_variances_returns_dict(self):
        self.assertIsInstance(self.instance.variances, dict)

    def test_disarm_sets_arms_to_empty_dict(self):
        self.instance.disarm()
        self.assertEqual(self.instance.arms, dict())

    def test_empty_bandit_means_returns_dict(self):
        self.instance.disarm()
        self.assertIsInstance(self.instance.means, dict)

    def test_empty_bandit_variances_returns_dict(self):
        self.instance.disarm()
        self.assertIsInstance(self.instance.variances, dict)

    def test_amputate_fails_on_bad_name(self):
        self.instance.add_arm(Arm(), arm_name='hello')
        self.assertRaises(KeyError,self.instance.amputate, arm_name='im_an_arm_that_doesnt_exist')

    def test_amputate_returns_string_on_success(self):
        self.instance.add_arm(Arm(), arm_name='hello')
        self.assertIsInstance(self.instance.amputate(arm_name='hello'), str)

    def test_not_empty_select_random_arm_returns_tuple(self):

        self.instance.disarm()
        added = self.instance.add_arm(Arm())
        self.instance.arms[added].update(Observation(value=1))
        self.instance.arms[added].update(Observation(value=0))
        arm = self.instance._select_random_arm()
        self.assertIsInstance(arm, tuple)

    def test_empty_select_random_arm_raises_InsufficientObservationsError(self):

        self.instance.disarm()
        added = self.instance.add_arm(Arm())
        self.assertRaises(InsufficientObservationsError,self.instance._select_random_arm)

    def test_not_empty_select_best_arm_returns_tuple(self):

        self.instance.disarm()
        added = self.instance.add_arm(Arm())
        self.instance.arms[added].update(Observation(value=1))
        self.instance.arms[added].update(Observation(value=0))
        arm = self.instance._select_best_arm()
        self.assertIsInstance(arm, tuple)

    def test_empty_select_best_arm_raises_InsufficientObservationsError(self):

        self.instance.disarm()
        added = self.instance.add_arm(Arm())
        self.assertRaises(InsufficientObservationsError,self.instance._select_best_arm)

    def test_not_empty_select_arm_returns_tuple(self):

        self.instance.disarm()
        added = self.instance.add_arm(Arm())
        self.instance.arms[added].update(Observation(value=1))
        self.instance.arms[added].update(Observation(value=0))
        arm = self.instance.select_arm()
        self.assertIsInstance(arm, tuple)

    def test_empty_select_arm_raises_InsufficientObservationsError(self):

        self.instance.disarm()
        added = self.instance.add_arm(Arm())
        self.assertRaises(InsufficientObservationsError,self.instance.select_arm)

class GreedyBandit_tester(Bandit_tester):
    def setUp(self):
        self.instance = GreedyBandit()


class EpsilonGreedyBandit_tester(GreedyBandit_tester):
    def setUp(self):
        self.instance = EpsilonGreedyBandit(epsilon=0.1)


class BayesianBandit_tester(Bandit_tester):
    def setUp(self):
        self.instance = BayesianBandit()


    def test_distributions_returns_dict(self):

        self.assertIsInstance(self.instance.distributions, dict)

class EpsilonBayesianBandit_tester(BayesianBandit_tester):
    def setUp(self):
        self.instance = EpsilonBayesianBandit(epsilon=0.1)

class UpperConfidenceBoundBandit_tester(Bandit_tester):
    def setUp(self):
        self.instance = UpperConfidenceBoundBandit()

    def test_plays_returns_dictionary(self):
        self.assertIsInstance(self.instance.plays, dict)

    def test_total_plays_returns_int(self):
        self.assertIsInstance(self.instance.total_plays, int)

    def test_empty_ucb_raises_InsufficientObservationsError(self):
        self.instance.disarm()
        added = self.instance.add_arm(Arm())
        self.assertRaises(InsufficientObservationsError, self.instance._ucb, arm_name=added)


