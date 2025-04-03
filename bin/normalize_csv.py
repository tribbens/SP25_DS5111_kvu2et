'''
This module provides functions to normalize csv files into a standard format with four columns.
It supports files that contain 'ygainers' or 'wsjgainers' in the filename.
'''

# was looking for the OOP and design phase that follows.  Let me know if I'm looking in the wrong branch, but I"m pretty sure I branched of the oop one...

import sys
import pandas as pd

def normalize_csv(raw_csv_path):
    '''
    This function does the standardization for raw csv files.
    '''
    if 'ygainers' in raw_csv_path:
        raw_df = pd.read_csv(raw_csv_path)
        print('ygainers loaded')
        norm_df = raw_df[['Symbol', 'Price', 'Change', 'Change %']]
        norm_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']

        assert isinstance(norm_df, pd.DataFrame)
        return norm_df.to_csv('ygainers_norm.csv', index=False)

    if 'wsjgainers' in raw_csv_path:
        raw_df = pd.read_csv(raw_csv_path)
        print('wsjgainers loaded')
        norm_df = raw_df[['Unnamed: 0', 'Last', 'Chg', '% Chg']]
        norm_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
        # extract only the symbol
        norm_df['symbol'] = norm_df['symbol'].str.extract(r'\((.*?)\)')

        assert isinstance(norm_df, pd.DataFrame)
        return norm_df.to_csv('wsjgainers_norm.csv', index=False)

    print('Please enter a supported file')
    return None

# this ensures it doesn't run when imported
if __name__ == '__main__':
    assert len(sys.argv) == 2, "too many inputs, expects 2"
    raw_csv_file = sys.argv[1].strip()

    normalize_csv(raw_csv_file)
