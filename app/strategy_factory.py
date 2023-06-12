from strategy import Strategy
from strategy1 import WMBStrategy
from strategy2 import SSMStrategy
from strategy3 import SMEStrategy
from strategy4 import WaveStrategy
from strategy5 import WaveSuperStrategy
from strategy6 import DonchianStrategy
from strategy7 import DWMStrategy

WMB = "WMB"
SSM = "SSM"
SME = "SME"
WAVE = "WAVE"
SW = "SW"
DON = "DON"
DWM = "DWM"


class StrategyFactory:

    @staticmethod
    def create(code) -> Strategy:
        if code == WMB:
            return WMBStrategy()
        elif code == SSM:
            return SSMStrategy()
        elif code == SME:
            return SMEStrategy()
        elif code == WAVE:
            return WaveStrategy()
        elif code == SW:
            return WaveSuperStrategy()
        elif code == DON:
            return DonchianStrategy()
        elif code == DWM:
            return DWMStrategy()
