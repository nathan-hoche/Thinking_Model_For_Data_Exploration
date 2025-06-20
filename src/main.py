import json
from colorama import init

init()

from dataset_interaction import DatasetInteraction
from llm_handler import LLMHandler

class Processor:
    def __init__(self):
        with open('config/config.json', 'r') as file:
            self.config = json.load(file)
        
        self.di = DatasetInteraction(dataset_path=self.config['dataset_path'])
        self.llm_handler = LLMHandler(model_name=self.config['model'])

    def process(self):
        print("Processing datasets...")
        for csv_file, df in self.di.dataframes.items():
            print(f"Processing {csv_file} ({len(df)} rows X {len(df.columns)} columns)")
            #self.llm_handler.ask("Hello how are you?")

if __name__ == "__main__":
    processor = Processor()
    processor.process()
    print("Processing complete.")
    