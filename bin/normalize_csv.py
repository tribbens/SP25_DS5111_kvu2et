import pandas as pd
import sys
print(f'variables passed: {sys.argv}')
raw_csv_file = sys.argv[1].strip()

def normalize_csv(raw_csv_path):
    raw_df = pd.read_csv(raw_csv_path)
    
    if 'ygainers' in raw_csv_path:
        print('ygainers loaded')
        norm_df = raw_df[['Symbol', 'Price', 'Change', 'Change %']]
        norm_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
        
        return norm_df.to_csv('ygainers_norm.csv', index=False)
    
    elif 'wjsgainers' in raw_csv_path:
        print('wjsgainers loaded')
        norm_df = raw_df[['Unnamed: 0', 'Last', 'Chg', '% Chg']]
        norm_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
        # extract only the symbol
        norm_df['symbol'] = norm_df['symbol'].str.extract(r'\((.*?)\)')
        
        return norm_df.to_csv('wsjgainers_norm.csv', index=False)
    
    else:
        print('Please enter a supported file')

normalize_csv(raw_csv_file)
