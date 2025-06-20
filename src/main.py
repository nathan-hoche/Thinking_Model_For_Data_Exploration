import json
from colorama import init
import os
from tqdm import tqdm

init()

from dataset_interaction import DatasetInteraction
from llm_handler import LLMHandler

os.makedirs('out', exist_ok=True)

class Processor:
    def __init__(self, verbose:bool=False):
        with open('config/config.json', 'r') as file:
            self.config = json.load(file)
        
        self.di = DatasetInteraction(dataset_path=self.config['dataset_path'])
        self.llm_handler = LLMHandler(model_name=self.config['model'], verbose=verbose)


    def process(self):
        print("Processing datasets...")
        for csv_file, df in tqdm(self.di.dataframes.items(), desc="CSV Files"):
            infos = {
                "Description": f"Make a description of this dataset: {csv_file}, which has {len(df)} rows and {len(df.columns)} columns. The different columns names are {', '.join(df.columns.tolist())}.",
                "Possibility": f"Can you list me the different study I can make for this dataset: {csv_file}, which has {len(df)} rows and {len(df.columns)} columns. The different columns names are {', '.join(df.columns.tolist())}.",
                "Visualization": f"Make a python code to visualize the following file using pandas and matplotlib: {csv_file} ({len(df)} rows and {len(df.columns)} columns). \
                You can generate multiple graph, etc... but use all the column you can! The different columns names are {', '.join(df.columns.tolist())}."
            }

            summary = f"# {csv_file}\n"
            for key, query in tqdm(infos.items(), desc=f"Info Gathering ({csv_file})"):
                response = self.llm_handler.ask(query=query)
                summary += f"\n## {key}:\n{response}\n"

            with open(f'out/{csv_file}.md', 'w+') as out_file:
                out_file.write(summary)


if __name__ == "__main__":
    processor = Processor(verbose=False)
    processor.process()
    