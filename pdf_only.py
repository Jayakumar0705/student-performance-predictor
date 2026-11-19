import pandas as pd

# Create the dataset
data = {
    'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Score': [35, 45, 48, 52, 60, 68, 75, 82, 88, 95]
}

df = pd.DataFrame(data)

# Display first 5 rows
print("First 5 rows:")
print(df.head())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())

# Display data statistics
print("\nData statistics:")
print(df.describe())

# Display average study hours and exam score
print("\nAverage study hours:", df["Hours"].mean())
print("Average exam score:", df["Score"].mean())