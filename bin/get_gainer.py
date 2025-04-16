'''
This class allows us to make our selection and run everything
based on the user input for the variable SRC.
'''

import sys
from gainers.factory import GainerFactory
from gainers.process_template import ProcessGainer

# this file brings everything together
if __name__=="__main__":
    # Make our selection, 'one' choice
    CHOICE = str(sys.argv[1])

    # let our factory get select the family of objects for processing
    factory = GainerFactory(CHOICE)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()

    # create our process
    runner = ProcessGainer(downloader, normalizer)
    runner.process()
