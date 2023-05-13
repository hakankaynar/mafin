from ta.volatility import DonchianChannel
from strategy import Strategy
from download import DownloadedTicker
from cache import Cache


class DonchianStrategy(Strategy):

    def calculate_downloaded(self, ticker: DownloadedTicker) -> bool:

        dc = DonchianChannel(high=ticker.high, low=ticker.low, close=ticker.close, window=30, offset=1)
        current = ticker.close.tail(1).values[0]

        return dc.donchian_channel_hband().tail(1).values[0] < current

    def calculate(self, t="cat", period="250d", interval="1d") -> bool:
        ticker = Cache(t)
        ticker_historical = ticker.history(period, interval)
        close = ticker_historical['Close']
        high = ticker_historical['High']
        low = ticker_historical['Low']

        dc = DonchianChannel(high=high, low=low, close=close, window=30, offset=1)
        current = close.tail(1).values[0]

        return dc.donchian_channel_hband().tail(1).values[0] < current
