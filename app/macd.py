from ta.trend import MACD
from ta.trend import ema_indicator


class Macd:

    def __init__(self):
        self.signal = None
        self.base = None

    def calculate(self, close, smooth=9):
        self.base = MACD(close=close, window_sign=smooth).macd()
        self.signal = ema_indicator(self.base, smooth)

    def is_buy(self):
        return self.base[-1] > self.signal[-1]

    def is_less_than(self, value):
        return self.base[-1] < value and self.signal[-1] < value

    def is_stronger_buy(self, period=3):

        if not self.is_buy():
            return False

        return self.is_increasing(period)

    def is_negative(self):
        return self.base[-1] < 0

    def is_increasing(self, period=3):
        tmp = self.base.tail(period) - self.signal.tail(period)
        lmax = tmp[0]

        for t in tmp:
            if t < lmax:
                return False
            elif t >= lmax:
                lmax = t

        return True
