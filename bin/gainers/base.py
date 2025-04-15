from abc import ABC, abstractmethod
import pandas as pd
import subprocess

# DOWNLOADER
class GainerDownload(ABC):
    def __init__(self, url):
        self.url = url

    @abstractmethod
    def download(self):
        command = "sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 " + self.url + " > raw_data.html"
        subprocess.run(command, shell=True)
        raw = pd.read_html('raw_data.html')
        raw[0].to_csv('raw_data.csv')


# PROCESSORS
class GainerProcess(ABC):
    def __init__(self, fname, source):
        self.fname = fname
        self.source = source

    @abstractmethod
    def normalize(self):
        raw_df = pd.read_csv(file_name)
        if self.source == 'yahoo':
            norm_df = raw_df[['Symbol', 'Price', 'Change', 'Change %']]
            norm_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']

        assert isinstance(norm_df, pd.DataFrame)
        self.norm_df = norm_df
        pass

    @abstractmethod
    def save_with_timestamp(self):
        pass
