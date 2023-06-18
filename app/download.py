import yfinance as yfc


class DownloadedTicker:

    def __init__(self, name, high, low, close):
        self.name = name
        self.high = high
        self.low = low
        self.close = close


class Download:

    def __init__(self, tickers, period, interval):
        self.tickers = tickers
        self.period = period
        self.interval = interval

    def download(self):
        downloaded = yfc.download(tickers=self.tickers, interval=self.interval, period=self.period, group_by='ticker')
        print("Downloaded size: " + str(len(downloaded)))
        tickers = []
        for ticker in self.tickers.split(' '):
            try:
                tickers.append(DownloadedTicker(name=ticker, low=downloaded[ticker]['Low'], high=downloaded[ticker]['High'], close=downloaded[ticker]['Close']))
            except KeyError as ke:
                print(ticker + " Key error:", ke)
        return tickers



