import os
import pandas as pd

curr_dir = "temp/"
final_dir = "final/"

# iterate through
for fname in os.listdir(curr_dir):
    raw_df = pd.read_csv(curr_dir+fname)
    if fname[0] == 'y': # yahoo case
        norm_df = raw_df[['Symbol', 'Price', 'Change', 'Change %']].copy()
        norm_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
        # fixing the price to remove unnecessary info
        norm_df.loc[:, 'price'] = norm_df['price'].str.extract(r'^([\d.]+)\s+\+')
        # updating change percent to remove special characters
        norm_df.loc[:, 'price_percent_change'] = norm_df['price_percent_change'].str.strip('+').str.strip('%')
    elif fname[0] == 'w':
        norm_df = raw_df[['Unnamed: 0', 'Last', 'Chg', '% Chg']].copy()
        norm_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
        # extract only the symbol
        norm_df.loc[:, 'symbol'] = norm_df['symbol'].str.extract(r'\((.*?)\)')
    elif fname[0] == 's':
        norm_df = raw_df[['Symbol', 'Stock Price', '% Change']].copy()
        norm_df.columns = ['symbol', 'price',  'price_percent_change']
        # remove special characters
        norm_df.loc[:, 'price_percent_change'] = norm_df['price_percent_change'].str.replace(
        r'[,%]', '', regex=True)
        # price change does not exist, going to calculate as an estimate
        norm_df['price_change'] = norm_df['price'] * (norm_df['price_percent_change'].astype(
        float)  / 100)
        norm_df = norm_df[['symbol', 'price', 'price_change', 'price_percent_change']]
        norm_df['price_change'] = norm_df['price_change'].round(2)
    else:
        print("Unable to normalize, ensure files begin with one of [ygainer, wsjgainer, sagainer]")

    norm_df.to_csv(final_dir+fname, index=False)
