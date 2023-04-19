from ta.trend import IchimokuIndicator


class Ichimoku:

    def __init__(self):
        self.conv = None
        self.span_b = None
        self.span_a = None
        self.base = None

    def calculate(self, high, low):
        ichimoku = IchimokuIndicator(high=high, low=low)
        self.base = ichimoku.ichimoku_base_line()
        self.conv = ichimoku.ichimoku_conversion_line()
        self.span_a = ichimoku.ichimoku_a()
        self.span_b = ichimoku.ichimoku_b()

    def is_inside_cloud(self, current):
        return (self.span_a[-1] >= current >= self.span_b[-1]) or \
               (self.span_b[-1] >= current >= self.span_a[-1])

    def is_over_cloud(self, current):
        return current > self.span_a[-1] and current > self.span_b[-1]

    def is_conv(self):
        return self.conv[-1] > self.base[-1]
