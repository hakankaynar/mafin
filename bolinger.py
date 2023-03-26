from ta.volatility import bollinger_mavg, bollinger_hband, bollinger_lband


class Bollinger:

    def __init__(self):
        self.lo = None
        self.hi = None
        self.ma = None

    def calculate(self, close):
        self.ma = bollinger_mavg(close)
        self.lo = bollinger_lband(close)
        self.hi = bollinger_hband(close)

    def is_expanding(self, period=2):
        tmp = self.hi.tail(period)

        hmin = tmp[0]

        for t in tmp:
            if t < hmin:
                return False
            else:
                hmin = t

        tmp = self.lo.tail(period)
        lmax = tmp[0]

        for t in tmp:
            if t > lmax:
                return False
            else:
                lmax = t

        return True
