import yaml
from yaml.loader import SafeLoader


class StrategyConfig:
    CFG_FROM_FILE = {}

    @staticmethod
    def read_cfg():
        with open('strategies.yaml') as f:
            StrategyConfig.CFG_FROM_FILE = yaml.load(f, Loader=SafeLoader)

    @staticmethod
    def read_name(code):
        strategies = StrategyConfig.CFG_FROM_FILE['strategies']
        return strategies[code]['name']

    @staticmethod
    def read_definition(code):
        strategies = StrategyConfig.CFG_FROM_FILE['strategies']
        return strategies[code]['definition']


