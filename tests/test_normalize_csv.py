import pandas as pd
import sys
import os

# Add the path to bin/ to import gainers modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'bin')))

from gainers.factory import GainerFactory
from gainers.process_template import ProcessGainer

def test_output_ygainers():
    ygain_df = pd.read_csv('tests/data/yahoo_test_clean.csv')

    # check column names
    correct_cols = ['symbol', 'price', 'price_change', 'price_percent_change']
    for col in ygain_df.columns:
        assert col in correct_cols, f'{col} is not an expected column name'

    # check number of columns
    assert len(ygain_df.columns) == 4, 'too many columns, expects 4'

def test_output_wsjgainers():
    wsj_df = pd.read_csv('tests/data/wsj_test_clean.csv')

    # check column names
    correct_cols = ['symbol', 'price', 'price_change', 'price_percent_change']
    for col in wsj_df.columns:
        assert col in correct_cols, f'{col} is not an expected column name'

    # check number of columns
    assert len(wsj_df.columns) == 4, 'too many columns, expects 4'

def test_general_yahoo():
    factory = GainerFactor('yahoo')
    normalizer = facto
