import unittest
from strategyDWM import DWMStrategy
from download import Download


class TestStrategy7(unittest.TestCase):

    def test_run(self):
        dl = Download("MBG.DE ASML", "3mo", "1d")
        tickers = dl.download()
        ws = DWMStrategy()
        result = ws.calculate_downloaded(tickers[0])
        self.assertTrue(result)
