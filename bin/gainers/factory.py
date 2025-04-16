from .yahoo import GainerDownloadYahoo, GainerProcessYahoo
from .wsj import GainerDownloadWSJ, GainerProcessWSJ
from .sa import GainerDownloadSA, GainerProcessSA
from datetime import datetime
from zoneinfo import ZoneInfo

# FACTORY
class GainerFactory:
    def __init__(self, choice):
        assert choice in ['yahoo', 'wsj', 'sa',  'test'], f"Unrecognized gainer type {choice}"
        self.choice = choice

    def get_downloader(self):
        # capture current date and time
        self.datetime_now = datetime.now(ZoneInfo("America/New_York"))
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        elif self.choice == 'wsj':
            return GainerDownloadWSJ()
        elif self.choice == 'sa':
            return GainerDownloadSA()

    def get_processor(self):
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerProcessYahoo(self.datetime_now)
        elif self.choice == 'wsj':
            return GainerProcessWSJ(self.datetime_now)
        elif self.choice == 'sa':
            return GainerProcessSA(self.datetime_now)
