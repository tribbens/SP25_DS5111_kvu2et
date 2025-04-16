'''
Placeholder module docstring
'''

from datetime import datetime
from zoneinfo import ZoneInfo
from .yahoo import GainerDownloadYahoo, GainerProcessYahoo
from .wsj import GainerDownloadWSJ, GainerProcessWSJ
from .sa import GainerDownloadSA, GainerProcessSA

# FACTORY
class GainerFactory:
    '''
    This class takes a user input and determines which classes to use based on that input

    Inputs: SRC = yahoo, wsj, or sa
    Outputs: appropriate classes for downloader and processor
    '''

    def __init__(self, choice):
        '''
        Placeholder class docstring
        '''
        assert choice in ['yahoo', 'wsj', 'sa',  'test'], f"Unrecognized gainer type {choice}"
        self.choice = choice
        # define datetime_now
        self.datetime_now = datetime.now()

    def get_downloader(self):
        '''
        Placeholder class docstring
        '''
        # capture current date and time
        self.datetime_now = datetime.now(ZoneInfo("America/New_York"))
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        if self.choice == 'wsj':
            return GainerDownloadWSJ()
        if self.choice == 'sa':
            return GainerDownloadSA()

    def get_processor(self):
        '''
        Placeholder class docstring
        '''
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerProcessYahoo(self.datetime_now)
        if self.choice == 'wsj':
            return GainerProcessWSJ(self.datetime_now)
        if self.choice == 'sa':
            return GainerProcessSA(self.datetime_now)
