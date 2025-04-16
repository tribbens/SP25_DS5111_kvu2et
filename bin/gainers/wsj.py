from base import GainerDownload
from base import GainerProcess
import os

class GainerDownloadWSJ(GainerDownload):
    def __init__(self):
        super().__init__('https://www.wsj.com/market-data/stocks/us/movers')

    def download(self):
        super().download()

        print("Downloading wsj gainers from:", self.url)

class GainerProcessWSJ(GainerProcess):
    def __init__(self, datetime_now):
        super().__init__('raw_data.html', 'wsj', datetime_now)

    def normalize(self):
        super().normalize()

    def save_with_timestamp(self):
        super().save_with_timestamp()
