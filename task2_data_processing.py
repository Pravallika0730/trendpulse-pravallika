import json
import pandas as pd
import os

# File path (use your latest JSON file name)
input_file = "data/trends_20260414.json"
output_file = "data/cleaned_trends.csv"

# Load JSON
with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(data)

print("Original data shape:", df.shape)

# -------- CLEANING -------- #

# 1. Remove duplicates
df = df.drop_duplicates()

# 2. Remove missing values
df = df.dropna()

# 3. Fix data types
df["score"] = df["score"].astype(int)
df["num_comments"] = df["num_comments"].astype(int)

# 4. Clean text (optional but good)
df["title"] = df["title"].str.strip()

print("Cleaned data shape:", df.shape)

# Save as CSV
df.to_csv(output_file, index=False)

print(f"Cleaned data saved to {output_file}")