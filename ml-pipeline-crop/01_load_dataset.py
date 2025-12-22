import pandas as pd

df = pd.read_csv("../datasets/structured/Crop_recommendation.csv")
print(df.head())

print("Shape:", df.shape)

print("Missing values:\n", df.isnull().sum())