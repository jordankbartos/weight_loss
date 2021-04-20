import pandas as pd
import os

class ParquetCachedDF:
    def __init__(self, file_path):
        self.file_path = file_path
        if os.path.isfile(file_path):
            self.df = pd.read_parquet(file_path)
        else:
            self.df = None

    def get_df(self):
        return self.df

    def save_df(self, file_path=None):
        if file_path is None:
            file_path = self.file_path

        if self.df is None:
            raise ValueError("Cannot save empty dataframe")
        else:
            self.df.to_parquet(file_path)

    def set_df(self, df):
        self.df = df
