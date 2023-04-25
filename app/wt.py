from ta.trend import ema_indicator, sma_indicator

'''
WaveTrend indicator impl from Tradingview @author LazyBear. 
'''


class WaveTrend:

    def __init__(self, l1=10, l2=21, ob_l1=60, ob_l2=53, os_l1=-60, os_l2=-53, d_constant=0.015):
        self.wt1 = None
        self.wt2 = None
        self.l1 = l1
        self.l2 = l2
        self.ob_l1 = ob_l1
        self.ob_l2 = ob_l2
        self.os_l1 = os_l1
        self.os_l2 = os_l2
        self.d_constant = d_constant

    def calculate(self, close):
        ap = close
        esa = ema_indicator(ap, self.l1)
        d = ema_indicator(abs(ap - esa), self.l2)
        ci = (ap - esa) / (self.d_constant * d)
        tci = ema_indicator(ci, self.l2)

        self.wt1 = tci
        self.wt2 = sma_indicator(self.wt1, 4)

    def is_buy(self) -> bool:
        return self.wt1.tail(1).values[0] > self.wt2.tail(1).values[0]

    def is_smaller(self, val) -> bool:
        return self.wt1.tail(1).values[0] < val

    def is_oversell(self) -> bool:
        return self.wt1.tail(1).values[0] < -10
