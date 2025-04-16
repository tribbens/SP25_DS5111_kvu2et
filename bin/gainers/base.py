'''
Placeholder module docstring
'''

from abc import ABC, abstractmethod
import os
import subprocess
import pandas as pd

# DOWNLOADER
class GainerDownload(ABC):
    '''
    Placeholder class docstring
    '''
    def __init__(self, url):
        '''
        Placeholder method docstring
        '''
        self.url = url

    @abstractmethod
    def download(self):
        '''
        Placeholder class docstring
        '''
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
        with open("raw_data.html", "w", encoding="utf-8") as f:
            f.write(html)

        # create raw csv file
        raw = pd.read_html("raw_data.html")
        raw[0].to_csv("raw_data.csv")


# PROCESSORS
class GainerProcess(ABC):
    '''
    Placeholder class docstring
    '''
    def __init__(self, fname, source, datetime_now):
        '''
        Placeholder class docstring
        '''
        self.fname = fname
        self.source = source
        self.datetime_now = datetime_now

    @abstractmethod
    def normalize(self):
        '''
        Placeholder class docstring
        '''
        raw_df = pd.read_csv(self.fname)
        if self.source == 'yahoo':
            norm_df = raw_df[['Symbol', 'Price', 'Change', 'Change %']]
            norm_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
            # fixing the price
            norm_df['price'] = norm_df['price'].str.extract(r'^([\d.]+)\s+\+')
        elif self.source == 'wsj':
            norm_df = raw_df[['Unnamed: 0', 'Last', 'Chg', '% Chg']]
            norm_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
            # extract only the symbol
            norm_df['symbol'] = norm_df['symbol'].str.extract(r'\((.*?)\)')
        elif self.source == 'sa':
            norm_df = raw_df[['Symbol', 'Stock Price', '% Change']]
            norm_df.columns = ['symbol', 'price',  'price_percent_change']
            # remove special characters
            norm_df['price_percent_change'] = norm_df['price_percent_change'].str.replace(
                r'[,%]', '', regex=True)
            # price change does not exist, going to calculate as an estimate
            norm_df['price_change'] = norm_df['price'] * (norm_df['price_percent_change'].astype(
                float)  / 100)
            norm_df = norm_df[['symbol', 'price', 'price_change', 'price_percent_change']]
            norm_df['price_change'] = norm_df['price_change'].round(2)
        else:
            print("Unable to normalize, ensure argument is one of [yahoo, wsj, sa]")

        assert isinstance(norm_df, pd.DataFrame)
        self.norm_df = norm_df

    @abstractmethod
    def save_with_timestamp(self):
        '''
        Placeholder class docstring
        '''
        now = self.datetime_now
        date = str(now.date())
        time = str(now.time()).replace(':', '-')[:-10]
        if self.source == 'yahoo':
            file_name = 'ygainers_' + date + '_at_' + time + '.csv'
            self.norm_df.to_csv(file_name, index=False)
        elif self.source == 'wsj':
            file_name = 'wsjgainers_' + date + '_at_' + time + '.csv'
            self.norm_df.to_csv(file_name, index=False)
        elif self.source == 'sa':
            file_name = 'sagainers_' + date + '_at_' + time + '.csv'
            self.norm_df.to_csv(file_name, index=False)
        else:
            print("Unable to save, make sure argument is one of [yahoo, wsj, sa]")

        # file clearnup
        os.remove('raw_data.csv')
        os.remove('raw_data.html')
