import sys
import pandas as pd
sys.path.append('.')
import bin.normalize_csv

def test_normalize_ygainers():
    ygain_df = pd.read_csv('ygainers_norm.csv')

    # check column names
    correct_cols = ['symbol', 'price', 'price_change', 'price_percent_change']
    for col in ygain_df.columns:
        assert col in correct_cols, f'{col} is not an expected column name'

    # check number of columns
    assert len(ygain_df.columns) == 4, 'too many columns, expects 4'

def test_normalize_wjsgainers():

