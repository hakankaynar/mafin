from cache import Cache
from wt import WaveTrend
from macd import Macd
from bolinger import Bollinger
from strategy import Strategy


class WaveStrategy(Strategy):

    def calculate(self, t="cat", period="250d", interval="1d") -> bool:
        ticker = Cache(t)
        ticker_historical = ticker.history(period, interval)
        close = ticker_historical['Close']

        wt = WaveTrend()
        wt.calculate(close)

        return wt.is_buy() and wt.is_oversell()
