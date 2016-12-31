import unittest


class World_tester(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_world_is_sane(self):
        self.assertEqual(2, (1+1))

    