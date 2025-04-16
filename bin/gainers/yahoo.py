from base import GainerDownload
from base import GainerProcess
import os
from datetime import datetime
from zoneinfo import ZoneInfo

class GainerDownloadYahoo(GainerDownload):
    def __init__(self):
        now = datetime.now(ZoneInfo("America/New_York"))
        super().__init__('https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200', now)

    def download(self):
        super().download()

        print("Downloading yahoo gainers from:", self.url)

class GainerProcessYahoo(GainerProcess):
    def __init__(self, datetime):
        super().__init__('raw_data.html', 'yahoo', datetime)
        self.current_datetime = datetime

    def normalize(self):
        super().normalize()

    def save_with_timestamp(self):
        super().save_with_timestamp()

test = GainerDownloadYahoo()
test_process = GainerProcessYahoo(test.datetime_now)

test.download()
test_process.normalize()
test_process.save_with_timestamp()
