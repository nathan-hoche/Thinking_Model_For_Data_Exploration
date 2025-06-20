import pandas as pd
import os

class DatasetInteraction:
    def __init__(self, dataset_path:str):
        self.dataset_path = dataset_path
        self.dataframes = self.load_csv_files()

    def load_csv_files(self):
        dataframes = {}
        for csv_file in os.listdir(self.dataset_path):
            if csv_file.endswith('.csv'):
                df = pd.read_csv(os.path.join(self.dataset_path, csv_file))
                dataframes[csv_file] = df
        return dataframes