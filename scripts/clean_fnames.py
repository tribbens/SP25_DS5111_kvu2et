import pandas as pd
import sys
import os
import glob

# Add the path to bin/ to import gainers modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'bin')))
from gainers.factory import GainerFactory

fname_df = pd.read_csv("fname_list.csv")
fname_list = list(fname_df['Name'])

for fname in fname_list:
    new_fname = fname.strip('-')
    if new_fname[:4] == 'ygai':
        factory = GainerFactory('yahoo', fname)
        normalizer = factory.get_processor()
        normalizer.normalize()
        normalizer.save_with_timestamp()

    elif new_fname[:4] == 'wsjg':
        factory = GainerFactory('wsj', fname)
        normalizer = factory.get_processor()
        normalizer.normalize()
        normalizer.save_with_timestamp()

    elif new_fname[:4] == 'saga':
        factory = GainerFactory('sa', fname)
        normalizer = factory.get_processor()
        normalizer.normalize()
        normalizer.save_with_timestamp()

    else:
        pass
