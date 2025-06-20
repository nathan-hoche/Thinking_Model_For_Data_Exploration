import pandas as pd
import os

class DatasetInteraction:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.dataframes = self.load_csv_files()

    def load_csv_files(self):
        dataframes = {}
        for csv_file in os.listdir(self.folder_path):
            if csv_file.endswith('.csv'):
                df = pd.read_csv(os.path.join(self.folder_path, csv_file))
                dataframes[csv_file] = df
        return dataframes