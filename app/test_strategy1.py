import unittest
from strategyWMB import WMBStrategy
from download import Download


class TestStrategy7(unittest.TestCase):

    def test_run(self):
        dl = Download("CSCO ASML", "2y", "1wk")
        tickers = dl.download()
        ws = WMBStrategy()
        result = ws.calculate_downloaded(tickers[0])
        self.assertTrue(result)
