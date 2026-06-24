import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_ai_learning_lab.csv")

# Create total_score column
df["total_score"] = df["assignment_score"] + df["quiz_score"]

# Create performance_level column
def get_performance(score):
    if score >= 160:
        return "Excellent"
    elif score >= 120:
        return "Good"
    elif score >= 80:
        return "Average"
    else:
        return "Needs Support"

df["performance_level"] = df["total_score"].apply(get_performance)

# Print average assignment score
print("Average Assignment Score:")
print(df["assignment_score"].mean())

# Print average quiz score
print("\nAverage Quiz Score:")
print(df["quiz_score"].mean())

# Print average study hours
print("\nAverage Study Hours:")
print(df["study_hours"].mean())

# Print number of students in each performance level
print("\nStudents in Each Performance Level:")
print(df["performance_level"].value_counts())

# Print average score topic-wise
print("\nAverage Total Score Topic-wise:")
print(df.groupby("topic")["total_score"].mean())

# Print average score batch-wise
print("\nAverage Total Score Batch-wise:")
print(df.groupby("batch")["total_score"].mean())

# Print students who need support
print("\nStudents Needing Support:")
print(
    df[df["performance_level"] == "Needs Support"][
        ["student_id", "student_name", "total_score"]
    ]
)