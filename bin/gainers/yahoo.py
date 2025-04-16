from .base import GainerDownload
from .base import GainerProcess
import os

class GainerDownloadYahoo(GainerDownload):
    def __init__(self):
        super().__init__('https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200')

    def download(self):
        super().download()

        print("Downloading yahoo gainers from:", self.url)

class GainerProcessYahoo(GainerProcess):
    def __init__(self, datetime_now):
        super().__init__('raw_data.html', 'yahoo', datetime_now)

    def normalize(self):
        super().normalize()

    def save_with_timestamp(self):
        super().save_with_timestamp()

        print("Saved yahoo gainers csv file with current date and time")
