import sys
import pandas as pd
sys.path.append('.')
import bin.normalize_csv

def test_normalize_ygainers():
    # this is great! Having some test data is great for testing and for reference.
    # one thing to change though, is moving the test data inside the tests/ directory
    # so the tests are self contained.  So you would probably go further, say to have a tests/data/ directory
    # See if you can move the test files there and if you get stuck let me know, there may be some finnaggling with paths needed
    ygain_df = pd.read_csv('ygainers_norm.csv')

    # check column names
    correct_cols = ['symbol', 'price', 'price_change', 'price_percent_change']
    for col in ygain_df.columns:
        assert col in correct_cols, f'{col} is not an expected column name'

    # check number of columns
    assert len(ygain_df.columns) == 4, 'too many columns, expects 4'

def test_normalize_wjsgainers():
    wsj_df = pd.read_csv('wsjgainers_norm.csv')

    # check column names
    correct_cols = ['symbol', 'price', 'price_change', 'price_percent_change']
    for col in wsj_df.columns:
        assert col in correct_cols, f'{col} is not an expected column name'

    # check number of columns
    assert len(wsj_df.columns) == 4, 'too many columns, expects 4'
