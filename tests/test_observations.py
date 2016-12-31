import unittest
from hastur.observations import Observation

class Observation_tester(unittest.TestCase):
    def setUp(self):
        self.success_instance = Observation(1)
        self.fail_instance = Observation(0)

    def test_nothing_yet(self):
        pass