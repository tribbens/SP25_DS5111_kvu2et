'''
Placeholder module docstring
'''

# TEMPLATE
class ProcessGainer:
    '''
    This class is a simple way to pull the disparate classes together
    to make them run more easily in the main file.
    '''
    def __init__(self, gainer_downloader, gainer_normalizer):
        '''
        Placeholder method docstring
        '''
        self.downloader = gainer_downloader
        self.normalizer = gainer_normalizer

    def _download(self):
        '''
        Placeholder method docstring
        '''
        self.downloader.download()

    def _normalize(self):
        '''
        Placeholder method docstring
        '''
        self.normalizer.normalize()

    def _save_to_file(self):
        '''
        Placeholder method docstring
        '''
        self.normalizer.save_with_timestamp()

    def process(self):
        '''
        Placeholder method docstring
        '''
        self._download()
        self._normalize()
        self._save_to_file()
