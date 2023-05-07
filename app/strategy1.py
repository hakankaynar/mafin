from cache import Cache
from wt import WaveTrend
from macd import Macd
from bolinger import Bollinger
from strategy import Strategy
from download import DownloadedTicker


class WMBStrategy(Strategy):

    def calculate_downloaded(self, ticker: DownloadedTicker) -> bool:
        close = ticker.close

        wt = WaveTrend()
        wt.calculate(close)

        if wt.is_buy():
            m = Macd()
            m.calculate(close)

            if m.is_stronger_buy():
                b = Bollinger()
                b.calculate(close)
                return b.is_expanding()

        return False

    def calculate(self, t="cat", period="250d", interval="1d") -> bool:
        ticker = Cache(t)
        ticker_historical = ticker.history(period, interval)

        close = ticker_historical['Close']
        # print("Last close of " + t + " is: " + str(close.tail(1).values[0]))
        wt = WaveTrend()
        wt.calculate(close)

        # print("Wave Trend is buy: " + str(wt.is_buy()))

        m = Macd()
        m.calculate(close)

        # print("MACD is buy: " + str(m.is_stronger_buy()))

        b = Bollinger()
        b.calculate(close)

        # print("Bollinger is expanding: " + str(b.is_expanding()))

        return wt.is_buy() and m.is_stronger_buy() and b.is_expanding()
