
import unittest
from hastur.arms import Arm
from hastur.observations import Observation
from hastur.exceptions import ExcessiveObservationsError
from hastur.exceptions import InsufficientObservationsError
import statistics


class Arm_tester(unittest.TestCase):

    def setUp(self):
        self.no_max_size_instance = Arm()
        self.size_ten_instance = Arm(maxsize=10)
        self.success_observation = Observation(value=1)
        self.failure_observation = Observation(value=0)


    def tearDown(self):
        pass



    def test_arm_size_returns_int(self):
        self.assertIsInstance(self.no_max_size_instance.size, int)

    def test_arm_size_increases_on_update(self):
        current_size = self.no_max_size_instance.size
        self.no_max_size_instance.update(self.success_observation)
        new_size = self.no_max_size_instance.size

        self.assertGreater(new_size, current_size)

    def test_arm_size_increments_by_one_on_update(self):
        current_size = self.no_max_size_instance.size
        self.no_max_size_instance.update(self.success_observation)
        new_size = self.no_max_size_instance.size

        self.assertEqual(new_size-1, current_size)

    def test_arm_observations_equals_empty_list_after_reset(self):
        self.no_max_size_instance.reset()
        self.assertEqual(self.no_max_size_instance.observations, [])

    def test_arm_isfull_returns_bool(self):
        self.assertIsInstance(self.no_max_size_instance.is_full, bool)

    def test_arm_with_infite_size_is_not_full(self):
        self.assertFalse(self.no_max_size_instance.is_full)
    
    def test_arm_with_max_size_if_full_when_size_equals_max_size(self):
        self.size_ten_instance.reset()
        for _ in range(0, 10):
            self.size_ten_instance.update(self.success_observation)

        self.assertTrue(self.size_ten_instance.is_full)

    def test_arm_update_fail_when_full(self):
        self.size_ten_instance.reset()

        for _ in range(0, 10):
            self.size_ten_instance.update(self.success_observation)

        self.assertRaises(ExcessiveObservationsError, self.size_ten_instance.update, self.success_observation)

    def test_arm_update_success_when_not_full(self):
        self.size_ten_instance.reset()

        self.size_ten_instance.update(self.success_observation)
        self.assertEqual(self.size_ten_instance.observations, [self.success_observation])

    def test_arm_empty_mean_raises_error(self):
        self.no_max_size_instance.reset()

        def call_mean():  # doing this because assertRaises expected a callable object.
            return self.no_max_size_instance.mean

        self.assertRaises(InsufficientObservationsError, call_mean)

    def test_arm_not_empty_mean_returns_float(self):
        self.no_max_size_instance.update(self.success_observation)
        m = self.no_max_size_instance.mean
        self.assertIsInstance(m, float)

    def test_arm_empty_value_returns_empty_list(self):
        self.no_max_size_instance.reset()
        self.assertEqual(self.no_max_size_instance.values, [])

    def test_arm_not_empty_value_returns_list(self):
        self.no_max_size_instance.update(self.success_observation)
        self.assertIsInstance(self.no_max_size_instance.values, list)

    def test_arm_empty_variance_raises_error(self):
        self.no_max_size_instance.reset()

        def call_variance():  # doing this because assertRaises expected a callable object.
            return self.no_max_size_instance.variance

        self.assertRaises(InsufficientObservationsError, call_variance)

    def test_arm_one_observation_variance_raises_error(self):
        self.no_max_size_instance.reset()

        def call_variance():  # doing this because assertRaises expected a callable object.
            return self.no_max_size_instance.variance

        self.no_max_size_instance.update(self.success_observation)

        self.assertRaises(InsufficientObservationsError, call_variance)


    def test_arm_two_observations_variance_returns_float(self):
        self.no_max_size_instance.reset()


        self.no_max_size_instance.update(self.success_observation)
        self.no_max_size_instance.update(self.failure_observation)

        self.assertIsInstance(self.no_max_size_instance.variance, float)
        