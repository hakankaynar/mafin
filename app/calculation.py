from strategy_factory import WMB


class Calculation:
    def __init__(self, period="250d", interval="1d", strategy=WMB):
        self.period = period
        self.interval = interval
        self.strategy = strategy
