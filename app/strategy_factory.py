from strategy import Strategy
from strategy1 import WMBStrategy
from strategy2 import SSMStrategy
from strategy3 import SMEStrategy
from strategy4 import WStrategy
from strategy5 import IBStrategy

WMB = "WMB"
SSM = "SSM"
SME = "SME"
W = "W"
IB = "IB"


class StrategyFactory:

    @staticmethod
    def create(code) -> Strategy:
        if code == WMB:
            return WMBStrategy()
        elif code == SSM:
            return SSMStrategy()
        elif code == SME:
            return SMEStrategy()
        elif code == W:
            return WStrategy()
        elif code == IB:
            return IBStrategy()
