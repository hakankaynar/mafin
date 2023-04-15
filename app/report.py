from calculation import Calculation
from user import User
from strategy_config import StrategyConfig
from ticker_data import TickerData


class Report:

    def __init__(self, c: Calculation, u: User):
        self.email = u.email
        self.interval = c.interval
        self.user = u.username
        self.buy_tickers = []
        self.period = c.period
        self.stg = c.strategy

    def add_buy_ticker(self, ticker: TickerData):
        self.buy_tickers.append(ticker)

    def with_user(self, user):
        self.user = user
        return self

    def with_email(self, email):
        self.email = email
        return self

    def text(self):

        if not self.buy_tickers:
            return ''

        txt = "\n===============================\n"
        txt += StrategyConfig.read_name(self.stg) + '\n\n'
        txt += StrategyConfig.read_definition(self.stg) + '\n'
        txt += "Period: " + self.period + " Interval: " + self.interval + ""
        txt += "\n===============================\n"

        for a_ticker in self.buy_tickers:
            txt += a_ticker.to_str() + "\n"

        return txt
