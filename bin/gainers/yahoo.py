from base import GainerDownload
from base import GainerProcess
import os
from datetime import datetime
from zoneinfo import ZoneInfo

class GainerDownloadYahoo(GainerDownload):
    def __init__(self):
        super().__init__('https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200')

    def download(self):
        super().download()

        # capture date and time at time of download
        now = datetime.now(ZoneInfo("America/New_York"))
        self.current_date = str(now.date())
        self.current_time = str(now.time()).replace(':', '-')[:-10]

        print("Downloading yahoo gainers from:", self.url)

class GainerProcessYahoo(GainerProcess):
    def __init__(self):
        super().__init__('raw_data.html', 'yahoo')

    def normalize(self):
        super().normalize

    def save_with_timestamp(self, date, time):
        file_name = 'ygainers_' + date + '_at_' + time + '.csv'

        self.norm_df.to_csv(file_name)
        print("Saving Yahoo gainers")

test = GainerDownloadYahoo()
test_process = GainerProcessYahoo()

test.download()
test_process.normalize()
test_process.save_with_timestamp(test.current_date, test.current_time)
