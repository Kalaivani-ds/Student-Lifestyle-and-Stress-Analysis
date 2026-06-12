# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("student-lifestyle-and-stress-dataset.csv")

# -----------------------------
# Basic Information
# -----------------------------

print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

print("\nColumn Names:")
print(df.columns)

# -----------------------------
# Stress Level Count
# -----------------------------

stress_count = df['Stress_Level'].value_counts()

plt.figure(figsize=(8,5))

plt.bar(stress_count.index.astype(str),
        stress_count.values)

plt.title("Stress Level Distribution")
plt.xlabel("Stress Level")
plt.ylabel("Number of Students")

plt.show()

# -----------------------------
# Sleep Hours vs Stress
# -----------------------------

plt.figure(figsize=(8,5))

plt.scatter(df['Sleep_Hours'],
            df['Stress_Level'])

plt.title("Sleep Hours vs Stress Level")
plt.xlabel("Sleep Hours")
plt.ylabel("Stress Level")

plt.show()

# -----------------------------
# Study Hours vs GPA
# -----------------------------

plt.figure(figsize=(8,5))

plt.scatter(df['Study_Hours_Per_Day'],
            df['GPA'])

plt.title("Study Hours vs GPA")
plt.xlabel("Study Hours Per Day")
plt.ylabel("GPA")

plt.show()

# -----------------------------
# Correlation Matrix
# -----------------------------

numeric_df = df.select_dtypes(include=['int64', 'float64'])

correlation = numeric_df.corr()

print("\nCorrelation Matrix:")
print(correlation)

# Heatmap using matplotlib only
plt.figure(figsize=(10,6))

plt.imshow(correlation,
           cmap='coolwarm',
           aspect='auto')

plt.colorbar()

plt.xticks(range(len(correlation.columns)),
           correlation.columns,
           rotation=90)

plt.yticks(range(len(correlation.columns)),
           correlation.columns)

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.show()

print("\nProject Executed Successfully!")