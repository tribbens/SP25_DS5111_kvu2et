from factory import GainerDownload
from factory import GainerProcess

class GainerDownloadWSJ(GainerDownload):
    def __init__(self):
        pass

    def download(self):
        print("Downloading WSJ gainers")


class GainerProcessWSJ(GainerProcess):
    def __init__(self):
        pass

    def normalize(self):
        print("Normalizing WSJ gainers")
	raw_df = pd.read_csv(raw_csv_path)
        norm_df = raw_df[['Unnamed: 0', 'Last', 'Chg', '% Chg']]
        norm_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']
        # extract only the symbol
        norm_df['symbol'] = norm_df['symbol'].str.extract(r'\((.*?)\)')

        assert isinstance(norm_df, pd.DataFrame)
        return norm_df.to_csv('wsjgainers_norm.csv', index=False)

    def save_with_timestamp(self):
        print("Saving WSJ gainers")
