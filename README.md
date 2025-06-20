# Thinking model for Data Exploration and Visualization

## Introduction

This project is a simple example on how to use a thinking model to explore and visualize data. The goal is to provide a structured approach to understanding data through exploration, analysis, and visualization.

## Usage

To use this project, you will firest need to install the required packages. You can do this by running:

```bash
pip install -r requirements.txt
```

Then, you can run the main script with the following command:

```bash
python src/main.py
```

## Explanation

For this project, I used the **Qwen3:0.6B** model, using **Ollama** for the inference. The model is designed to help you think about data exploration and visualization in a structured way.

This project will generate a very basic summary of the data, containing the following sections:
- **Description**: A brief description of the dataset; based on the file name and the different column names
- **Proposed Studies**: A list of potential studies that can be conducted with the dataset, including a brief description of each study.
- **Visualization**: A step-by-step approach to visualize the data using Python libraries like `pandas` and `matplotlib`.

> You can view the generated summaries in the `docs` folder. ![Example 1](docs/Basic_Stats.csv.md) & ![Example 2](docs/Career_Stats_Defensive.csv.md)


> [!NOTE]
> This is a very fast and simple project, a lot of improvements can be made!