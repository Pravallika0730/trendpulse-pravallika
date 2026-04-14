import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/cleaned_trends.csv")

# Create larger figure (fix layout issue)
fig, axes = plt.subplots(3, 1, figsize=(8, 12))

# -------- GRAPH 1: Count per category --------
count_category = df["category"].value_counts()
count_category.plot(kind="bar", ax=axes[0])
axes[0].set_title("Number of Posts per Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Count")

# -------- GRAPH 2: Average Score --------
avg_score = df.groupby("category")["score"].mean()
avg_score.plot(kind="bar", ax=axes[1])
axes[1].set_title("Average Score per Category")
axes[1].set_xlabel("Category")
axes[1].set_ylabel("Average Score")

# -------- GRAPH 3: Average Comments --------
avg_comments = df.groupby("category")["num_comments"].mean()
avg_comments.plot(kind="bar", ax=axes[2])
axes[2].set_title("Average Comments per Category")
axes[2].set_xlabel("Category")
axes[2].set_ylabel("Average Comments")

# Adjust layout
plt.tight_layout()

# Show all graphs together
plt.show(block=True)