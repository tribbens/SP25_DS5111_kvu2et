from abc import ABC, abstractmethod
import pandas as pd
import subprocess
import os

# DOWNLOADER
class GainerDownload(ABC):
    def __init__(self, url):
        self.url = url

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
        result = subprocess.run(command, shell=True, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        html = result.stdout

        with open("raw_data.html", "w") as f:
            f.write(html)


# PROCESSORS
class GainerProcess(ABC):
    def __init__(self, fname, source):
        self.fname = fname
        self.source = source

    @abstractmethod
    def normalize(self):
        raw_df = pd.read_csv(self.fname)
        if self.source == 'yahoo':
            norm_df = raw_df[['Symbol', 'Price', 'Change', 'Change %']]
            norm_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']

        assert isinstance(norm_df, pd.DataFrame)
        self.norm_df = norm_df

    @abstractmethod
    def save_with_timestamp(self):
        pass
