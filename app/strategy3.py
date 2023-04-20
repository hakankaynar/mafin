import yfinance as yf
from strategy import Strategy
from macd import Macd
from stochastic import Stochastic
from ta.trend import ema_indicator


class SMEStrategy(Strategy):

    def calculate(self, t="cat", period="200d", interval="1d") -> bool:
        ticker = yf.Ticker(t)

        ticker_historical = ticker.history(period, interval, actions=False)
        close = ticker_historical['Close']
        # current = ticker.info['regularMarketPrice']

        stochastic = Stochastic()
        stochastic.calculate(high=ticker_historical['High'], low=ticker_historical['Low'], close=close)

        m = Macd()
        m.calculate(close)

        # ei = ema_indicator(close, window=200)

        # return stochastic.is_below(35) and m.is_less_than(0) and m.is_buy() and current < ei.iloc[-1]
        return stochastic.is_below(35) and m.is_less_than(0) and m.is_buy()
