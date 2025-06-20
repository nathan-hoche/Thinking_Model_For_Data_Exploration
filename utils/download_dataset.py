import kagglehub

kagglehub.login()

# Download latest version
path = kagglehub.dataset_download("kendallgillies/nflstatistics")

print("Path to dataset files:", path)