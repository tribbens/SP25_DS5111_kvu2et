import sys
from gainers.factory import GainerFactory
from gainers.process_template import ProcessGainer

if __name__=="__main__":
    '''
    Input: SRC = yahoo, wsj, or sa
    Output: normalized csv file with the date

    This function pulls everything from the gainers package together
    It takes the user input for the variable SRC and runs the appropriate classes.
    '''
    # Our sample main file would look like this
    import sys

    # Make our selection, 'one' choice
    CHOICE = str(sys.argv[1])

    # let our factory get select the family of objects for processing
    factory = GainerFactory(CHOICE)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()

    # create our process
    runner = ProcessGainer(downloader, normalizer)
    runner.process()
