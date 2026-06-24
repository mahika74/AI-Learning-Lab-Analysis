import pandas as pd
import matplotlib.pyplot as plt
import json

# Load dataset
df = pd.read_csv("cleaned_ai_learning_lab.csv")

# Create total_score
df["total_score"] = df["assignment_score"] + df["quiz_score"]

# Create performance_level column - Added to resolve KeyError
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
# -----------------------------------
# 1. Average Total Score by Topic
# -----------------------------------
plt.figure(figsize=(12, 5))
df.groupby("topic")["total_score"].mean().plot(kind="bar")
plt.title("Average Total Score by Topic")
plt.xlabel("Topic")
plt.ylabel("Average Total Score")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("topic_score_chart.png")
plt.close()

# -----------------------------------
# 2. Student Count by Performance Level
# -----------------------------------
plt.figure(figsize=(8, 5))

df["performance_level"].value_counts().plot(kind="bar")

plt.title("Student Count by Performance Level")
plt.xlabel("Performance Level")
plt.ylabel("Student Count")
plt.tight_layout()

plt.savefig("performance_level_chart.png")
plt.close()

# -----------------------------------
# 3. Attendance Distribution
# -----------------------------------
plt.figure(figsize=(6, 6))

df["attendance"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Attendance Distribution")
plt.ylabel("")
plt.tight_layout()

plt.savefig("attendance_chart.png")
plt.close()

# -----------------------------------
# 4. Average Study Hours by Topic
# -----------------------------------
plt.figure(figsize=(12, 5))

df.groupby("topic")["study_hours"].mean().plot(kind="line")

plt.title("Average Study Hours by Topic")
plt.xlabel("Topic")
plt.ylabel("Average Study Hours")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("study_hours_chart.png")
plt.close()

# -----------------------------------
# 5. Summary Dictionary
# -----------------------------------
summary = {
    "total_students": len(df),
    "average_assignment_score": round(df["assignment_score"].mean(), 2),
    "average_quiz_score": round(df["quiz_score"].mean(), 2),
    "average_study_hours": round(df["study_hours"].mean(), 2),
    "most_common_topic": df["topic"].mode()[0]
}

# Save summary as JSON
with open("learning_summary.json", "w") as file:
    json.dump(summary, file, indent=4)

print("Charts saved successfully:")
print("topic_score_chart.png")
print("performance_level_chart.png")
print("attendance_chart.png")
print("study_hours_chart.png")

print("\nSummary JSON saved:")
print("learning_summary.json")

print("\nSummary:")
print(summary)