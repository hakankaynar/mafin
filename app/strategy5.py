from cache import Cache
from wt import WaveTrend
from strategy import Strategy
from supertrend import SuperTrend


class WaveSuperStrategy(Strategy):

    def calculate(self, t="cat", period="250d", interval="1d") -> bool:
        ticker = Cache(t)
        ticker_historical = ticker.history(period, interval)
        close = ticker_historical['Close']

        wt = WaveTrend()
        wt.calculate(close)

        st = SuperTrend()
        st.calculate(ticker_historical['High'], ticker_historical['Low'], close)

        return wt.is_buy() and wt.is_smaller(val=25) and st.is_buy(close.tail(1).values[0])
