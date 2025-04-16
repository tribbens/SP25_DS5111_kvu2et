from base import GainerDownload
from base import GainerProcess
import os
from datetime import datetime
from zoneinfo import ZoneInfo

class GainerDownloadTR(GainerDownload):
    def __init__(self):
        super().__init__('https://www.tipranks.com/markets/top-gainers')

    def download(self):
        super().download()

        print("Downloading tipranks gainers from:", self.url)

class GainerProcessTR(GainerProcess):
    def __init__(self, datetime_now):
        super().__init__('raw_data.html', 'tr', datetime_now)

    def normalize(self):
        super().normalize()

    def save_with_timestamp(self):
        super().save_with_timestamp()

        print("Saved tipranks gainers csv file with current date and time")

test = GainerDownloadTR()
test.download()
now = datetime.now()

process_test = GainerProcessTR(now)
process_test.normalize()
process_test.save_with_timestamp()
