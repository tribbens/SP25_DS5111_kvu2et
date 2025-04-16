import pandas as pd
from bin import gainers

def test_output_ygainers():
    ygain_df = pd.read_csv('data/ygainers_test_clean.csv')

    # check column names
    correct_cols = ['symbol', 'price', 'price_change', 'price_percent_change']
    for col in ygain_df.columns:
        assert col in correct_cols, f'{col} is not an expected column name'

    # check number of columns
    assert len(ygain_df.columns) == 4, 'too many columns, expects 4'

def test_output_wsjgainers():
    wsj_df = pd.read_csv('data/wsjgainers_test_clean.csv')

    # check column names
    correct_cols = ['symbol', 'price', 'price_change', 'price_percent_change']
    for col in wsj_df.columns:
        assert col in correct_cols, f'{col} is not an expected column name'

    # check number of columns
    assert len(wsj_df.columns) == 4, 'too many columns, expects 4'
