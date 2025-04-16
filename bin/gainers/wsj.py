from base import GainerDownload
from base import GainerProcess
import os
from datetime import datetime
from zoneinfo import ZoneInfo

class GainerDownloadWSJ(GainerDownload):
    def __init__(self):
        now = datetime.now(ZoneInfo("America/New_York"))
        super().__init__('https://www.wsj.com/market-data/stocks/us/movers', now)

    def download(self):
        super().download()

        print("Downloading wsj gainers from:", self.url)

class GainerProcessWSJ(GainerProcess):
    def __init__(self, datetime):
        super().__init__('raw_data.html', 'wsj', datetime)

    def normalize(self):
        super().normalize()

    def save_with_timestamp(self):
        super().save_with_timestamp()

test = GainerDownloadWSJ()
test_process = GainerProcessWSJ(test.datetime_now)

test.download()
test_process.normalize()
test_process.save_with_timestamp()
