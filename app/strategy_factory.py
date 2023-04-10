from strategy import Strategy
from strategy1 import WMBStrategy
from strategy2 import SSMStrategy
from strategy3 import SMEStrategy

WMB = "WMB"
SSM = "SSM"
SME = "SME"


class StrategyFactory:

    @staticmethod
    def create(name) -> Strategy:
        if name == WMB:
            return WMBStrategy()
        elif name == SSM:
            return SSMStrategy()
        elif name == SME:
            return SMEStrategy()

