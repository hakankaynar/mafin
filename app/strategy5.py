from cache import Cache
from ichimoku import Ichimoku
from strategy import Strategy
from bolinger import Bollinger


class IBStrategy(Strategy):

    def calculate(self, t="cat", period="250d", interval="1d") -> bool:
        ticker = Cache(t)
        ticker_historical = ticker.history(period, interval)

        ichimoku = Ichimoku()
        ichimoku.calculate(high=ticker_historical['High'], low=ticker_historical['Low'])

        if not ichimoku.is_conv():
            return False

        close = ticker_historical['Close']
        current = ticker.info['regularMarketPrice']

        bollinger = Bollinger()
        bollinger.calculate(close);

        return bollinger.is_bigger_then_ma(current)
