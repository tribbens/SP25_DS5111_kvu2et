from gainers.factory import GainerFactory
from gainers.process_template import ProcessGainer
import sys

if __name__=="__main__":
    # Our sample main file would look like this
    import sys

    # Make our selection, 'one' choice
    choice = str(sys.argv[1])

    # let our factory get select the family of objects for processing
    factory = GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()

    # create our process
    runner = ProcessGainer(downloader, normalizer)
    runner.process()
