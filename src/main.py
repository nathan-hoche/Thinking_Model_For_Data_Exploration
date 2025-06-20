import json

from dataset_interaction import DatasetInteraction

class Processor:
    def __init__(self):
        with open('config/config.json', 'r') as file:
            self.config = json.load(file)
        
        self.di = DatasetInteraction(dataset_path=self.config['dataset_path'])

    def process(self):
        print("Processing datasets...")
        for csv_file, df in self.di.dataframes.items():
            print(f"Processing {csv_file} with {len(df)} rows and {len(df.columns)} columns.")

if __name__ == "__main__":
    processor = Processor()
    processor.process()
    print("Processing complete.")
    