from ta.trend import macd
from ta.trend import ema_indicator


class Macd:

    def __init__(self):
        self.signal = None
        self.base = None

    def calculate(self, close):
        self.base = macd(close)
        self.signal = ema_indicator(self.base, 9)

    def is_buy(self):
        return self.base[-1] > self.signal[-1]

    def is_stronger_buy(self, period=3):

        tmp = self.base.tail(period) - self.signal.tail(period)
        for t in tmp:
            if t < 0:
                t = 0
        lmax = tmp[0]

        for t in tmp:
            if t < lmax:
                return False
            elif t > 0:
                lmax = t

        return False if lmax == 0 else True
