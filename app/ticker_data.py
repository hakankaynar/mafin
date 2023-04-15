from yfinance import Ticker
import yfinance as yf


class TickerData:

    def __init__(self):
        self.name = None
        self.price = None
        self.currency = None
        self.symbol = None

    def load(self, t: str):
        ticker = yf.Ticker(t)
        info = ticker.info
        self.name = info['longName']
        self.currency = info['currency']
        self.price = info['regularMarketPrice']
        self.symbol = info['symbol']
        return self

    def to_str(self):
        return self.name + " (" + self.symbol + ")"
