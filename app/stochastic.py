from ta.momentum import StochasticOscillator


class Stochastic:

    def __init__(self, window=70, smooth=10, buy_limit=35):
        self.stoch = None
        self.window = window
        self.smooth = smooth
        self.buy_limit = buy_limit

    def calculate(self, high, low, close):
        self.stoch = StochasticOscillator(high, low, close, window=self.window, smooth_window=self.smooth).stoch();

    def is_buy(self):
        return self.stoch.iloc[-1] < self.buy_limit
