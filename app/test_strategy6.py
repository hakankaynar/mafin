import unittest
from strategy6 import DonchianStrategy


class TestStrategy5(unittest.TestCase):

    def test_run(self):
        ws = DonchianStrategy()
        result = ws.calculate(t="KO")
        self.assertTrue(result)
