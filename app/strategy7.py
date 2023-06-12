from ta.volatility import DonchianChannel
from strategy import Strategy
from download import DownloadedTicker
from wt import WaveTrend
from macd import Macd


class DWMStrategy(Strategy):

    def calculate_downloaded(self, ticker: DownloadedTicker) -> bool:

        dc = DonchianChannel(high=ticker.high, low=ticker.low, close=ticker.close, window=30, offset=1)
        current = ticker.close.tail(1).values[0]

        if dc.donchian_channel_hband().tail(1).values[0] < current :
            wt = WaveTrend()
            wt.calculate(ticker.close)

            if wt.is_buy():
                m = Macd()
                m.calculate(ticker.close)
                return m.is_buy()

        return False

    def calculate(self, t="cat", period="250d", interval="1d") -> bool:
        return False
