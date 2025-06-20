import pandas as pd
import os

FOLDER_PATH = "/home/Yukiche/.cache/kagglehub/datasets/kendallgillies/nflstatistics/versions/1"

for csv_file in os.listdir(FOLDER_PATH):
    if csv_file.endswith('.csv'):
        print(f"Processing CSV file: {csv_file}")

        # Replace with the correct path to your CSV file
        df = pd.read_csv(f"{FOLDER_PATH}/{csv_file}")

        # Display the first five rows
        print(df.head())
