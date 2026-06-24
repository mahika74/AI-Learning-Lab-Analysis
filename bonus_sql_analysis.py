# bonus_sql_analysis.py

import pandas as pd
import sqlite3

# Load cleaned dataset
df = pd.read_csv("cleaned_ai_learning_lab.csv")

# Create total_score column (needed for Query 3)
df["total_score"] = df["assignment_score"] + df["quiz_score"]

# Create SQLite database
conn = sqlite3.connect("learning_lab.db")

# Store DataFrame as a table
df.to_sql(
    "student_learning",
    conn,
    if_exists="replace",
    index=False
)

# ------------------------------------
# Query 1: Average assignment score by topic
# ------------------------------------
query1 = """
SELECT topic, AVG(assignment_score) AS avg_assignment_score
FROM student_learning
GROUP BY topic;
"""

print("Query 1: Average Assignment Score by Topic")
print(pd.read_sql_query(query1, conn))

# ------------------------------------
# Query 2: Student count by batch
# ------------------------------------
query2 = """
SELECT batch, COUNT(*) AS student_count
FROM student_learning
GROUP BY batch;
"""

print("\nQuery 2: Student Count by Batch")
print(pd.read_sql_query(query2, conn))

# ------------------------------------
# Query 3: Students with total score below 80
# ------------------------------------
query3 = """
SELECT student_name, total_score
FROM student_learning
WHERE total_score < 80;
"""

print("\nQuery 3: Students with Total Score Below 80")
print(pd.read_sql_query(query3, conn))

# Close connection
conn.close()

print("\nDatabase 'learning_lab.db' created successfully.")