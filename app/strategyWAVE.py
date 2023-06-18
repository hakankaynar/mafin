from cache import Cache
from wt import WaveTrend
from strategy import Strategy
from download import DownloadedTicker


class WaveStrategy(Strategy):

    def calculate_downloaded(self, ticker: DownloadedTicker) -> bool:
        wt = WaveTrend()
        wt.calculate(ticker.close)
        return wt.is_buy() and wt.is_oversell()

    def calculate(self, t="cat", period="250d", interval="1d") -> bool:
        ticker = Cache(t)
        ticker_historical = ticker.history(period, interval)
        close = ticker_historical['Close']

        wt = WaveTrend()
        wt.calculate(close)

        return wt.is_buy() and wt.is_oversell()
