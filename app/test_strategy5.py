import unittest
from strategy5 import WaveSuperStrategy


class TestStrategy5(unittest.TestCase):

    def test_run(self):
        ws = WaveSuperStrategy();
        result = ws.calculate(t="KO");
        self.assertTrue(result)
