'''
Placeholder module docstring
'''

from .base import GainerDownload
from .base import GainerProcess

class GainerDownloadSA(GainerDownload):
    '''
    Placeholder class docstring
    '''
    def __init__(self):
        super().__init__('https://stockanalysis.com/markets/gainers/')

    def download(self):
        super().download()

        print("Downloading stockanalysis gainers from:", self.url)

class GainerProcessSA(GainerProcess):
    '''
    Placeholder class docstring
    '''
    def __init__(self, fname, datetime_now):
        super().__init__(fname, 'sa', datetime_now)

    def normalize(self):
        super().normalize()

    def save_with_timestamp(self):
        super().save_with_timestamp()

        print("Saved stockanalysis gainers csv file with current date and time")
