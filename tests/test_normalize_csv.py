import pandas as pd
import sys
import os
import glob

# Add the path to bin/ to import gainers modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'bin')))

from gainers.factory import GainerFactory

def test_normalize_ygainers():
    # normalize test data from the data folder without downloading
    factory = GainerFactory('yahoo', 'tests/data/yahoo_test_raw.csv')
    normalizer = factory.get_processor()
    normalizer.normalize()
    normalizer.save_with_timestamp()

    match = glob.glob("ygain*.csv")
    ygain_df = pd.read_csv(match[0])

    # check column names
    correct_cols = ['symbol', 'price', 'price_change', 'price_percent_change']
    for col in ygain_df.columns:
        assert col in correct_cols, f'{col} is not an expected column name'

    # check number of columns
    assert len(ygain_df.columns) == 4, 'too many columns, expects 4'

def test_normalize_wsjgainers():
    factory = GainerFactory('wsj', 'tests/data/wsj_test_raw.csv')
    normalizer = factory.get_processor()
    normalizer.normalize()
    normalizer.save_with_timestamp()

    match = glob.glob("wsjgain*.csv")
    wsj_df = pd.read_csv(match[0])

    # check column names
    correct_cols = ['symbol', 'price', 'price_change', 'price_percent_change']
    for col in wsj_df.columns:
        assert col in correct_cols, f'{col} is not an expected column name'

    # check number of columns
    assert len(wsj_df.columns) == 4, 'too many columns, expects 4'

