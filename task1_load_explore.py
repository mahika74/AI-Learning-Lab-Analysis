import pandas as pd

# 1 & 2. Load CSV file into a DataFrame
df = pd.read_csv("ai_learning_lab.csv")

# 3. Print the shape of the dataset
print("Dataset Shape:")
print(df.shape)

# 4. Print the first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# 5. Print all column names
print("\nColumn Names:")
print(df.columns.tolist())

# 6. Print data types using .info()
print("\nDataset Info:")
df.info()

# 7. Print missing value count for each column
print("\nMissing Values Count:")
print(df.isnull().sum())

# 8. Print the number of duplicate rows
print("\nNumber of Duplicate Rows:")
print(df.duplicated().sum())

# 9. Print value counts of the 'topic' column
print("\nValue Counts of 'topic' Column:")
print(df["topic"].value_counts())

# 10. Print value counts of the 'attendance' column
print("\nValue Counts of 'attendance' Column:")
print(df["attendance"].value_counts())