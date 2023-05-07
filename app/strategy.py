from download import DownloadedTicker
class Strategy:

    def calculate(self, t="cat", period="250d", interval="1d") -> bool:
        pass

    def calculate_downloaded(self, ticker: DownloadedTicker) -> bool:
        pass
