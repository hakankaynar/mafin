import unittest

from cache import Cache
from supertrend import SuperTrend


class TestSuperTrend(unittest.TestCase):

    def test_run(self):
        ticker_history = Cache("cat").history("200d", "1d");

        close = ticker_history["Close"]
        st = SuperTrend()
        st.calculate(ticker_history["High"], ticker_history["Low"], close)

        print (st.is_buy(close.tail(1).values[0]))
