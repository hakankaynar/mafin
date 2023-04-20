from abc import ABC

import yfinance as yfc
from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter


class CachedLimiterSession(CacheMixin, LimiterMixin, Session, ABC):
    pass


class Cache(yfc.Ticker):

    def __init__(self, ticker):
        session = CachedLimiterSession(limiter=Limiter(RequestRate(2, Duration.SECOND * 5),
                                                       bucket_class=MemoryQueueBucket),
                                       backend=SQLiteCache("yfinance.cache"))
        super(Cache, self).__init__(ticker=ticker, session=session)

    @property
    def info(self) -> dict:
        return super(Cache, self).info

    def history(self, period, interval):
        return super(Cache, self).history(period, interval, actions=False)