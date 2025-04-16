from abc import ABC, abstractmethod
import pandas as pd
import subprocess
import os
from datetime import datetime
from zoneinfo import ZoneInfo

# DOWNLOADER
class GainerDownload(ABC):
    def __init__(self, url, datetime):
        self.url = url
        self.datetime_now = datetime

    @abstractmethod
    def download(self):
        env = os.environ.copy()
        env['DBUS_SESSION_BUS_ADDRESS'] = '/dev/null'
        command = [
            "google-chrome-stable",
            "--headless",
            "--disable-gpu",
            "--dump-dom",
            "--no-sandbox",
            "--timeout=10000",
            self.url
        ]
        result = subprocess.run(command, capture_output=True, text=True,
            check=True, env=env)

        html = result.stdout
        with open("raw_data.html", "w") as f:
            f.write(html)


# PROCESSORS
class GainerProcess(ABC):
    def __init__(self, fname, source, current_datetime):
        self.fname = fname
        self.source = source
        self.now = current_datetime

    @abstractmethod
    def normalize(self):
        raw = pd.read_html(self.fname)
        raw[0].to_csv('raw_data.csv')
        raw_df = pd.read_csv('raw_data.csv')
        if self.source == 'yahoo':
            norm_df = raw_df[['Symbol', 'Price', 'Change', 'Change %']]
            norm_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']

        assert isinstance(norm_df, pd.DataFrame)
        self.norm_df = norm_df

    @abstractmethod
    def save_with_timestamp(self):
        now = self.now
        date = str(now.date())
        time = str(now.time()).replace(':', '-')[:-10]

        file_name = 'ygainers_' + date + '_at_' + time + '.csv'
        self.norm_df.to_csv(file_name)

        # file clearnup
        os.remove('raw_data.csv')
        os.remove('raw_data.html')
