from cache import Cache
from macd import Macd
from strategy import Strategy


class SSMStrategy(Strategy):

    def calculate(self, t="cat", period="250d", interval="1d") -> bool:
        ticker = Cache(t)

        current = ticker.info['regularMarketPrice']

        ticker_historical = ticker.history("10d", "1d")
        close = ticker_historical['Close']

        sma10 = close.mean()

        if current > sma10:
            return False

        ticker_historical = ticker.history("200d", "1d")
        close = ticker_historical['Close']

        sma200 = close.mean()

        if current < sma200:
            return False

        m = Macd()
        m.calculate(close)

        return m.is_negative() and m.is_increasing(period=2)
