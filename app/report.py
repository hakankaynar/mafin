from calculation import Calculation
from user import User


class Report:

    def __init__(self, c: Calculation, u: User):
        self.email = u.email
        self.interval = c.interval
        self.user = u.username
        self.buy_tickers = []
        self.period = c.period
        self.stg = c.strategy

    def add_buy_ticker(self, ticker: str):
        self.buy_tickers.append(ticker)

    def with_user(self, user):
        self.user = user
        return self

    def with_email(self, email):
        self.email = email
        return self

    def text(self):
        txt = "\n==================================================================\n"
        txt += self.stg + " Period: " + self.period + " Interval" + self.interval + " calculation\n"
        txt += "==================================================================\n"

        for a_ticker in self.buy_tickers:
            txt += a_ticker + " is buy\n"

        return txt
