raw_df = pd.read_csv(self.fname)
if self.source == 'yahoo':
    norm_df = raw_df[['Symbol', 'Price', 'Change', 'Change %']].copy()
    norm_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
    # fixing the price to remove unnecessary info
            norm_df.loc[:, 'price'] = norm_df['price'].str.extract(r'^([\d.]+)\s+\+')
            # updating change percent to remove special characters
            norm_df.loc[:, 'price_percent_change'] = norm_df['price_percent_change'].str.strip('+').str.strip('%')
        elif self.source == 'wsj':
            norm_df = raw_df[['Unnamed: 0', 'Last', 'Chg', '% Chg']].copy()
            norm_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
            # extract only the symbol
            norm_df.loc[:, 'symbol'] = norm_df['symbol'].str.extract(r'\((.*?)\)')
        elif self.source == 'sa':
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
            print("Unable to normalize, ensure argument is one of [yahoo, wsj, sa]")
