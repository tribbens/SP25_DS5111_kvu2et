from abc import ABC, abstractmethod
import pandas as pd

# DOWNLOADER
class GainerDownload(ABC):
    def __init__(self, url):
        self.url = url

    @abstractmethod
    def download(self):
        sudo google-chrome-stable --headless --disable-gpu --dump-dom --no-sandbox --timeout=5000 self.url > raw_data.html
	raw = pd.read_html('raw_data.html')
	raw[0].to_csv('raw_data.csv')
	pass


# PROCESSORS
class GainerProcess(ABC):
    def __init__(self, df, source):
        self.raw_df = df
	self.source = source

    @abstractmethod
    def normalize(self):
        if self.source == 'yahoo':
		norm_df = raw_df[['Symbol', 'Price', 'Change', 'Change %']]
		norm_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']

		assert isinstance(norm_df, pd.DataFrame)
		self.norm_df = norm_df
	pass

    @abstractmethod
    def save_with_timestamp(self):
        pass
