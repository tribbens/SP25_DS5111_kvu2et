'''
This module implements classes from the other modules for data from WSJ.
'''

from .base import GainerDownload
from .base import GainerProcess

class GainerDownloadWSJ(GainerDownload):
    '''
    This class builds on the GainerDownload class
    and downloads from the wsj url path.
    '''
    def __init__(self):
        super().__init__('https://www.wsj.com/market-data/stocks/us/movers')

    def download(self):
        super().download()

        print("Downloading wsj gainers from:", self.url)

class GainerProcessWSJ(GainerProcess):
    '''
    This class builds on the GainerProcess class
    and process the raw_data.csv file into a processed
    gainers csv file with the date and time.
    '''
    def __init__(self, fname, datetime_now):
        super().__init__(fname, 'wsj', datetime_now)

    def normalize(self):
        super().normalize()

    def save_with_timestamp(self):
        super().save_with_timestamp()

        print("Saved wsj gainers csv file with current date and time")
