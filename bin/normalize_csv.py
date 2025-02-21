import pandas as pd
import sys

raw_csv_file = sys.argv[1].strip()

def normalize_csv(raw_csv_path):
    raw_df = pd.read_csv(raw_csv_path)
    
    if 'ygainers' in raw_csv_path:
        norm_df = raw_df[['Symbol', 'Price', 'Change', 'Change %']]
        norm_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
        
        return norm_df.to_csv('ygainers_norm.csv', index=False)
    
    elif 'wjsgainers' in raw_csv_path:
        norm_df = raw_df[['Symbol', 'Price', 'Change', 'Change %']]
        norm_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
        
        return norm_df.to_csv('wsjgainers_norm.csv', index=False)

normalize_csv(raw_csv_file)
