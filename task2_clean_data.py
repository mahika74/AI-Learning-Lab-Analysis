import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("ai_learning_lab.csv")

# 1. Remove duplicate rows
df = df.drop_duplicates()

# 2. Strip extra spaces
df["student_name"] = df["student_name"].str.strip()
df["topic"] = df["topic"].str.strip()
df["tool_used"] = df["tool_used"].str.strip()

# 3. Convert columns to title case
df["attendance"] = df["attendance"].str.title()
df["lab_completed"] = df["lab_completed"].str.title()
df["api_used"] = df["api_used"].str.title()

# 4. Replace invalid assignment_score values
df.loc[
    (df["assignment_score"] < 0) |
    (df["assignment_score"] > 100),
    "assignment_score"
] = np.nan

# 5. Replace invalid quiz_score values
df.loc[
    (df["quiz_score"] < 0) |
    (df["quiz_score"] > 100),
    "quiz_score"
] = np.nan

# 6. Replace invalid study_hours values
df.loc[
    df["study_hours"] < 0,
    "study_hours"
] = np.nan

# 7. Replace invalid feedback_rating values
df.loc[
    (df["feedback_rating"] < 1) |
    (df["feedback_rating"] > 5),
    "feedback_rating"
] = np.nan

# 8. Fill missing values
df["assignment_score"] = df["assignment_score"].fillna(
    df["assignment_score"].mean()
)

df["quiz_score"] = df["quiz_score"].fillna(
    df["quiz_score"].mean()
)

df["study_hours"] = df["study_hours"].fillna(
    df["study_hours"].median()
)

df["feedback_rating"] = df["feedback_rating"].fillna(
    df["feedback_rating"].median()
)

# 9. Print shape of cleaned DataFrame
print("Shape of Cleaned DataFrame:")
print(df.shape)

# 10. Print missing values after cleaning
print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

# 11. Save cleaned dataset
df.to_csv("cleaned_ai_learning_lab.csv", index=False)

print("\nCleaned dataset saved as 'cleaned_ai_learning_lab.csv'")