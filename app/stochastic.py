from ta.momentum import StochasticOscillator


class Stochastic:

    def __init__(self, window=70, smooth=10, buy_limit=35):
        self.stoch = None
        self.window = window
        self.smooth = smooth

    def calculate(self, high, low, close):
        self.stoch = StochasticOscillator(high, low, close, window=self.window, smooth_window=self.smooth).stoch();

    def is_below(self, value) -> bool:
        return self.stoch.tail(1).values[0] < value
