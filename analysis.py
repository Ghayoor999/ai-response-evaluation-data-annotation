import pandas as pd

df = pd.read_csv("data/ai_response_evaluation_dataset.csv")

print("Records:", len(df))
print("\nOverall labels:")
print(df["overall_label"].value_counts())

print("\nIssue types:")
print(df["issue_type"].value_counts())

print("\nMissing values:")
print(df.isna().sum())
