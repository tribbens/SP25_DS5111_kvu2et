from factory.py import GainerDownload
from factory.py import GainerProcess

class GainerDownloadYahoo(GainerDownload):
    def __init__(self):
        pass
        
    def download(self):
        print("Downloading yahoo gainers")


class GainerProcessYahoo(GainerProcess):
    def __init__(self):
        pass

    def normalize(self):
        print("Normalizing yahoo gainers")
	raw_df = pd.read_csv(raw_csv_path)
        norm_df = raw_df[['Symbol', 'Price', 'Change', 'Change %']]
        norm_df.columns = ['symbol', 'price', 'price_change', 'price_percent_change']

        assert isinstance(norm_df, pd.DataFrame)
        return norm_df.to_csv('ygainers_norm.csv', index=False)

    def save_with_timestamp(self):
        print("Saving Yahoo gainers")
