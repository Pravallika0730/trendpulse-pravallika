import pandas as pd

# Load data
file_path = "data/cleaned_trends.csv"
df = pd.read_csv(file_path)

print("Dataset shape:", df.shape)

# ---------------- ANALYSIS ---------------- #

# 1. Top 5 highest scored posts
top_posts = df.sort_values(by="score", ascending=False).head(5)
print("\nTop 5 posts by score:")
print(top_posts[["title", "score"]])

# 2. Average score per category
avg_score = df.groupby("category")["score"].mean()
print("\nAverage score per category:")
print(avg_score)

# 3. Total posts per category
count_category = df["category"].value_counts()
print("\nNumber of posts per category:")
print(count_category)

# 4. Most commented post
most_commented = df.sort_values(by="num_comments", ascending=False).head(1)
print("\nMost commented post:")
print(most_commented[["title", "num_comments"]])

# 5. Category with highest average comments
avg_comments = df.groupby("category")["num_comments"].mean()
print("\nAverage comments per category:")
print(avg_comments)