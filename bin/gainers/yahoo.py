'''
This module implements classes for data from Yahoo Finance.
'''

from .base import GainerDownload
from .base import GainerProcess

class GainerDownloadYahoo(GainerDownload):
    '''
    Placeholder class docstring
    '''
    def __init__(self):
        super().__init__('https://finance.yahoo.com/markets/stocks/gainers/?start=0&count=200')

    def download(self):
        super().download()

        print("Downloading yahoo gainers from:", self.url)

class GainerProcessYahoo(GainerProcess):
    '''
    Placeholder class docstring
    '''
    def __init__(self, fname, datetime_now):
        super().__init__(fname, 'yahoo',  datetime_now)

    def normalize(self):
        super().normalize()

    def save_with_timestamp(self):
        super().save_with_timestamp()

        print("Saved yahoo gainers csv file with current date and time")
