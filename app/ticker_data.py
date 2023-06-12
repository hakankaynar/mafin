from cache import Cache
from requests.exceptions import HTTPError
import logging


class TickerData:
    logger = logging.getLogger(__name__)

    def __init__(self):
        self.name = None
        self.price = None
        self.currency = None
        self.symbol = None

    def load(self, t: str):
        self.name = t
        self.currency = ''
        self.price = ''
        self.symbol = ''

        return self

    def to_str(self):
        return self.name + " (" + self.symbol + ")"
