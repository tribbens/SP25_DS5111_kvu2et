from factory.py import GainerDownload
from factory.py import GainerProcess

class GainerDownloadYahoo(GainerDownload):
    def __init__(self):
        pass
        

    def download(self):
        print("Downloading yahoo gainers")

class GainerProcessYahoo(GainerProcess):
    def __init__(self):
        pass

    def normalize(self):
        print("Normalizing yahoo gainers")

    def save_with_timestamp(self):
        print("Saving Yahoo gainers")
