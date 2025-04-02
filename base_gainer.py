from abc import ABC, abstractmethod

# FACTORY
class GainerFactory:
    def __init__(self, choice):
        assert choice in ['yahoo', 'wsj', 'test'], f"Unrecognized gainer type {choice}"
        self.choice = choice 

    def get_downloader(self):
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerDownloadYahoo()
        elif self.choice == 'wsj':
            return GainerDownloadWSJ()

    def get_processor(self):
        # trigger off url to return correct downloader
        if self.choice == 'yahoo':
            return GainerProcessYahoo()
        elif self.choice == 'wsj':
            return GainerProcessWSJ()

# DOWNLOADER
class GainerDownload(ABC):
    def __init__(self):
        self.url = url

    @abstractmethod
    def download(self):
        pass

class GainerDownloadYahoo(GainerDownload):
    def __init__(self):
        pass
        

    def download(self):
        print("Downloading yahoo gainers")

class GainerDownloadWSJ(GainerDownload):
    def __init__(self):
        pass

    def download(self):
        print("Downloading WSJ gainers")




# PROCESSORS 
class GainerProcess(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def normalize(self):
        pass

    @abstractmethod
    def save_with_timestamp(self):
        pass

class GainerProcessYahoo(GainerProcess):
    def __init__(self):
        pass

    def normalize(self):
        print("Normalizing yahoo gainers")

    def save_with_timestamp(self):
        print("Saving Yahoo gainers")
# ITS OWN SEPARATE FILE
class GainerProcessWSJ(GainerProcess):
    def __init__(self):
        pass

    def normalize(self):
        print("Normalizing WSJ gainers")

    def save_with_timestamp(self):
        print("Saving WSJ gainers")

# TEMPLATE
class ProcessGainer:
    def __init__(self, gainer_downloader, gainer_normalizer):
        self.downloader = gainer_downloader
        self.normalizer = gainer_normalizer

    def _download(self):
        self.downloader.download()

    def _normalize(self):
        self.normalizer.normalize()

    def _save_to_file(self):
        self.normalizer.save_with_timestamp()

    def process(self):
        self._download()
        self._normalize()
        self._save_to_file()

if __name__=="__main__":
    # Our sample main file would look like this
    import sys
   
    # Make our selection, 'one' choice
    choice = sys.argv[1]

    # let our factory get select the family of objects for processing
    factory = GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()

    # create our process
    runner = ProcessGainer(downloader, normalizer)
    runner.process()




