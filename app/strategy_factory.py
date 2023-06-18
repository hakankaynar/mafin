from strategy import Strategy
from strategyWMB import WMBStrategy
from strategySSM import SSMStrategy
from strategySME import SMEStrategy
from strategyWAVE import WaveStrategy
from strategySW import WaveSuperStrategy
from strategyDON import DonchianStrategy
from strategyDWM import DWMStrategy
from strategyWM import WMStrategy

WMB = "WMB"
SSM = "SSM"
SME = "SME"
WAVE = "WAVE"
SW = "SW"
DON = "DON"
DWM = "DWM"
WM = "WM"


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
        elif code == WM:
            return WMStrategy()
